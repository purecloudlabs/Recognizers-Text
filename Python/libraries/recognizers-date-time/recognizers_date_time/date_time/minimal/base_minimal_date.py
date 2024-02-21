from typing import List, Optional, Dict
from datetime import datetime

from recognizers_text.extractor import ExtractResult
from ..constants import TimeTypeConstants
from ..parsers import DateTimeParseResult
from recognizers_date_time.date_time.base_date import DateExtractorConfiguration, BaseDateExtractor, \
    DateParserConfiguration, BaseDateParser


class BaseMinimalDateExtractor(BaseDateExtractor):
    def __init__(self, config: DateExtractorConfiguration):
        super().__init__(config)

    def extract(self, source: str, reference: datetime = None) -> List[ExtractResult]:
        from ..utilities import merge_all_tokens

        tokens = []
        tokens.extend(self.basic_regex_match(source))

        result = merge_all_tokens(tokens, source, self.extractor_type_name)
        return result


class BaseMinimalDateParser(BaseDateParser):

    def __init__(self, config: DateParserConfiguration):
        super().__init__(config)

    def parse(self, source: ExtractResult, reference: datetime = None) -> Optional[DateTimeParseResult]:
        from ..utilities import DateTimeFormatUtil
        if reference is None:
            reference = datetime.now()

        result_value: DateTimeParseResult = None

        if source.type is self.parser_type_name:
            source_text = source.text.lower()
            inner_result = self.parse_basic_regex_match(source_text, reference)

            if not inner_result.success:
                inner_result = self.parse_single_number(source_text, reference)

            if inner_result.success:
                inner_result.future_resolution: Dict[str, str] = dict()
                inner_result.future_resolution[TimeTypeConstants.DATE] = DateTimeFormatUtil.format_date(
                    inner_result.future_value)
                inner_result.past_resolution: Dict[str, str] = dict()
                inner_result.past_resolution[TimeTypeConstants.DATE] = DateTimeFormatUtil.format_date(
                    inner_result.past_value)
                result_value = inner_result

        result = DateTimeParseResult(source)
        result.value = result_value
        result.timex_str = result_value.timex if result_value is not None else ''
        result.resolution_str = ''

        return result
