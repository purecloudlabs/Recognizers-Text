from typing import Dict, Pattern, Optional, List
import regex

from recognizers_text.culture import Culture
from recognizers_text.utilities import RegExpUtility
from recognizers_text.extractor import ExtractResult
from recognizers_text.parser import ParseResult
from recognizers_text.meta_data import MetaData
from recognizers_number.culture import CultureInfo
from recognizers_number.number.parsers import BaseNumberParserConfiguration
from recognizers_number.resources.minimal_numeric import MinimalNumeric
from recognizers_number.number.parsers import BaseNumberParser, NumberParserConfiguration


class MinimalNumberParserConfiguration(BaseNumberParserConfiguration):

    @property
    def cardinal_number_map(self) -> Dict[str, int]:
        return None

    @property
    def ordinal_number_map(self) -> Dict[str, int]:
        return None

    @property
    def round_number_map(self) -> Dict[str, int]:
        return None

    @property
    def digital_number_regex(self) -> Pattern:
        return None

    @property
    def fraction_marker_token(self) -> str:
        return None

    @property
    def negative_number_sign_regex(self) -> Pattern:
        return self._negative_number_sign_regex

    @property
    def half_a_dozen_regex(self) -> Pattern:
        return None

    @property
    def half_a_dozen_text(self) -> str:
        return None

    @property
    def word_separator_token(self) -> str:
        return None

    @property
    def written_decimal_separator_texts(self) -> List[str]:
        return None

    @property
    def written_group_separator_texts(self) -> List[str]:
        return None

    @property
    def written_integer_separator_texts(self) -> List[str]:
        return None

    @property
    def written_fraction_separator_texts(self) -> List[str]:
        return None

    @property
    def non_standard_separator_variants(self) -> List[str]:
        return None

    @property
    def is_multi_decimal_separator_culture(self) -> bool:
        return None

    @property
    def round_multiplier_regex(self) -> Pattern:
        return None

    @property
    def culture_info(self):
        return self._culture_info

    @property
    def lang_marker(self) -> str:
        return self._lang_marker

    @property
    def non_decimal_separator_char(self) -> str:
        return self._non_decimal_separator_char

    @property
    def decimal_separator_char(self) -> str:
        return self._decimal_separator_char

    def __init__(self, culture_info=None, decimal_point_separator: bool = True):
        if culture_info is None:
            culture_info = CultureInfo(Culture.Minimal)

        self._culture_info = culture_info
        self._lang_marker = MinimalNumeric.LangMarker

        # Allows user to choose whether to use a ',' or '.' as a decimal separator
        # decimal_point_separator=True uses a decimal point as decimal separator and comma as thousands separator
        # decimal_point_separator=False uses a comma as decimal separator and decimal point as thousands separator
        if decimal_point_separator:
            self._decimal_separator_char = MinimalNumeric.DecimalSeparatorChar
            self._non_decimal_separator_char = MinimalNumeric.NonDecimalSeparatorChar
        else:
            self._decimal_separator_char = MinimalNumeric.NonDecimalSeparatorChar
            self._non_decimal_separator_char = MinimalNumeric.DecimalSeparatorChar

        self._negative_number_sign_regex = RegExpUtility.get_safe_reg_exp(
            MinimalNumeric.NegativeNumberSignRegex)


class MinimalNumberParser(BaseNumberParser):
    def __init__(self, config: BaseNumberParserConfiguration):
        self.config: NumberParserConfiguration = config
        self.supported_types: List[str] = list()

        self.arabic_number_regex: Pattern = RegExpUtility.get_safe_reg_exp(
            r'\d+', flags=regex.I | regex.S)
        self.round_number_set: List[str] = []
        self.is_non_standard_separator_variant = False

    def parse(self, source: ExtractResult) -> Optional[ParseResult]:
        # Check if the parser is configured to support specific types
        if self.supported_types and source.type not in self.supported_types:
            return None
        ret: Optional[ParseResult] = None
        extra = source.data if isinstance(source.data, str) else None
        if not extra:
            if self.arabic_number_regex.search(source.text):
                extra = 'Num'
            else:
                extra = self.config.lang_marker

        if isinstance(source.data, List):
            ers = source.data
            inner_prs = [self.parse(rs) for rs in ers]
            merged_prs = []

            val = 0
            count = 0

            for idx in range(len(inner_prs)):
                val += inner_prs[idx].value
                if (idx + 1 >= len(inner_prs)) or not self.__is_mergeable(float(str(inner_prs[idx].value)),
                                                                          float(str(inner_prs[idx + 1].value))):
                    start = ers[idx - count].start
                    length = ers[idx].start + ers[idx].length - start

                    parsed_result = ParseResult()
                    parsed_result.start = start
                    parsed_result.length = length
                    parsed_result.value = val
                    parsed_result.text = source.text[start - source.start:length]
                    parsed_result.type = source.type
                    parsed_result.data = None

                    merged_prs.append(parsed_result)
                    if val != 0:
                        final_val = val
                    val = 0
                    count = 0

                else:
                    count += 1

            ret = ParseResult()
            ret.start = source.start
            ret.length = source.length
            ret.text = source.text
            ret.type = source.type
            ret.value = val + final_val
            ret.data = merged_prs
        elif 'Num' in extra:
            ret = self._digit_number_parse(source)
        elif 'Pow' in extra:
            ret = self._power_number_parse(source)

        if isinstance(ret.data, List):
            for parsed_result in ret.data:
                ret.resolution_str = self._get_resolution_string(parsed_result.value)
        elif ret and ret.value is not None:

            # Use culture_info to format values
            ret.resolution_str = self.config.culture_info.format(
                ret.value) if self.config.culture_info is not None else repr(ret.value)

            ret.resolution_str = self._get_resolution_string(ret.value)
            ret.text = ret.text.lower()

        return ret

    def _digit_number_parse(self, ext_result: ExtractResult) -> ParseResult:
        result = ParseResult()
        result.start = ext_result.start
        result.length = ext_result.length
        result.text = ext_result.text
        result.type = ext_result.type
        result.meta_data = MetaData() if not result.meta_data else result.meta_data

        # [1] 24
        # [2] 12 32/33
        # [3] 1,000,000
        # [4] 234.567
        # [5] 44/55

        power = 1
        handle = ext_result.text.lower()

        # Scale used in the calculate of double
        result.value = self._get_digital_value(handle, power)

        return result

