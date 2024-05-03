#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from typing import Dict, Pattern, List, Optional

from recognizers_text.utilities import RegExpUtility
from recognizers_text.culture import Culture
from recognizers_text.parser import ParseResult
from recognizers_number.culture import CultureInfo
from recognizers_number.number.parsers import BaseNumberParserConfiguration
from recognizers_number.resources.english_numeric import EnglishNumeric


class EnglishNumberParserConfiguration(BaseNumberParserConfiguration):

    lang_marker: str = EnglishNumeric.LangMarker
    is_multi_decimal_separator_culture: bool = EnglishNumeric.MultiDecimalSeparatorCulture

    decimal_separator_char: str = EnglishNumeric.DecimalSeparatorChar
    fraction_marker_token: str = EnglishNumeric.FractionMarkerToken
    non_decimal_separator_char: str = EnglishNumeric.NonDecimalSeparatorChar
    half_a_dozen_text: str = EnglishNumeric.HalfADozenText
    word_separator_token: str = EnglishNumeric.WordSeparatorToken

    written_decimal_separator_texts: List[str] = EnglishNumeric.WrittenDecimalSeparatorTexts
    written_group_separator_texts: List[str] = EnglishNumeric.WrittenGroupSeparatorTexts
    written_integer_separator_texts: List[str] = EnglishNumeric.WrittenIntegerSeparatorTexts
    written_fraction_separator_texts: List[str] = EnglishNumeric.WrittenFractionSeparatorTexts
    non_standard_separator_variants: List[str] = EnglishNumeric.NonStandardSeparatorVariants

    cardinal_number_map: Dict[str, int] = EnglishNumeric.CardinalNumberMap
    ordinal_number_map: Dict[str, int] = EnglishNumeric.OrdinalNumberMap
    round_number_map: Dict[str, int] = EnglishNumeric.RoundNumberMap

    negative_number_sign_regex: Pattern = RegExpUtility.get_safe_reg_exp(EnglishNumeric.NegativeNumberSignRegex)
    half_a_dozen_regex: Pattern = RegExpUtility.get_safe_reg_exp(EnglishNumeric.HalfADozenRegex)
    digital_number_regex: Pattern = RegExpUtility.get_safe_reg_exp(EnglishNumeric.DigitalNumberRegex)
    round_multiplier_regex: Pattern = RegExpUtility.get_safe_reg_exp(EnglishNumeric.RoundMultiplierRegex)

    def __init__(self, culture_info: Optional[CultureInfo] = None):
        culture_info = culture_info or CultureInfo(Culture.English)
        super().__init__(culture_info)
