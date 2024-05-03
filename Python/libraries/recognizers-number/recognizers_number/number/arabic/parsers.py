from re import Pattern
from typing import List, Dict, Optional, Any


from recognizers_text.utilities import RegExpUtility
from recognizers_text.culture import Culture
from recognizers_number.culture import CultureInfo
from recognizers_number.number.parsers import BaseNumberParserConfiguration
from recognizers_number.resources.arabic_numeric import ArabicNumeric


class ArabicNumberParserConfiguration(BaseNumberParserConfiguration):

    lang_marker: str = ArabicNumeric.LangMarker
    is_compound_number_language: bool = ArabicNumeric.CompoundNumberLanguage
    is_multi_decimal_separator_culture: bool = ArabicNumeric.MultiDecimalSeparatorCulture

    decimal_separator_char: str = ArabicNumeric.DecimalSeparatorChar
    fraction_marker_token: str = ArabicNumeric.FractionMarkerToken
    non_decimal_separator_char: str = ArabicNumeric.NonDecimalSeparatorChar
    half_a_dozen_text: str = ArabicNumeric.HalfADozenText
    word_separator_token: str = ArabicNumeric.WordSeparatorToken
    non_standard_separator_variants: List[str] = []
    non_decimal_separator_text: str = ''

    written_decimal_separator_texts: List[str] = ArabicNumeric.WrittenDecimalSeparatorTexts
    written_group_separator_texts: List[str] = ArabicNumeric.WrittenGroupSeparatorTexts
    written_integer_separator_texts: List[str] = ArabicNumeric.WrittenIntegerSeparatorTexts
    written_fraction_separator_texts: List[str] = ArabicNumeric.WrittenFractionSeparatorTexts

    cardinal_number_map: Dict[str, int] = ArabicNumeric.CardinalNumberMap
    ordinal_number_map: Dict[str, int] = ArabicNumeric.OrdinalNumberMap
    relative_reference_offset_map: Dict[str, str] = ArabicNumeric.RelativeReferenceOffsetMap
    relative_reference_relative_to_map: Dict[str, str] = ArabicNumeric.RelativeReferenceRelativeToMap
    round_number_map: Dict[str, int] = ArabicNumeric.RoundNumberMap

    half_a_dozen_regex: Pattern = RegExpUtility.get_safe_reg_exp(ArabicNumeric.HalfADozenRegex)
    digital_number_regex: Pattern = RegExpUtility.get_safe_reg_exp(ArabicNumeric.DigitalNumberRegex)
    negative_number_sign_regex: Pattern = RegExpUtility.get_safe_reg_exp(ArabicNumeric.NegativeNumberSignRegex)
    fraction_preposition_regex: Pattern = RegExpUtility.get_safe_reg_exp(ArabicNumeric.FractionPrepositionRegex)
    round_multiplier_regex: Pattern = RegExpUtility.get_safe_reg_exp(ArabicNumeric.RoundMultiplierRegex)

    def __init__(self, culture_info: Optional[CultureInfo] = None):
        culture_info = culture_info or CultureInfo(Culture.Arabic)
        super().__init__(culture_info)

    def get_lang_specific_int_value(self, match_strs: List[str]) -> (bool, int):
        result = (False, 0)

        # @TODO "و" should be moved to Arabic YAML file.

        #    Workaround to solve "و" which means "and" before rounded number in Arabic.
        #    ألف و مائة = one thousand and one hundred #
        #    But in Arabic there is no integer before hundred, because it's 100 by default.
        if len(match_strs) == 1 and match_strs[0] == "و":
            result = (True, 1)

        return result
