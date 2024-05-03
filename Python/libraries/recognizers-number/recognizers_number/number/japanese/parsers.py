#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from typing import List, Dict, Pattern, Optional

from recognizers_text.utilities import RegExpUtility
from recognizers_text.culture import Culture
from recognizers_text.parser import ParseResult
from recognizers_number.resources.japanese_numeric import JapaneseNumeric
from recognizers_number.number.cjk_parsers import CJKNumberParserConfiguration
from recognizers_number.culture import CultureInfo


class JapaneseNumberParserConfiguration(CJKNumberParserConfiguration):

    lang_marker: str = JapaneseNumeric.LangMarker
    is_multi_decimal_separator_culture: bool = JapaneseNumeric.MultiDecimalSeparatorCulture

    decimal_separator_char: str = JapaneseNumeric.DecimalSeparatorChar
    fraction_marker_token: str = JapaneseNumeric.FractionMarkerToken
    non_decimal_separator_char: str = JapaneseNumeric.NonDecimalSeparatorChar
    half_a_dozen_text: str = JapaneseNumeric.HalfADozenText
    word_separator_token: str = JapaneseNumeric.WordSeparatorToken
    zero_char: str = JapaneseNumeric.ZeroChar
    pair_char: str = JapaneseNumeric.PairChar

    written_decimal_separator_texts: List[str] = []
    written_group_separator_texts: List[str] = []
    written_integer_separator_texts: List[str] = []
    written_fraction_separator_texts: List[str] = []
    non_standard_separator_variants: List[str] = []

    cardinal_number_map: Dict[str, int] = {}
    ordinal_number_map: Dict[str, int] = {}
    round_number_map: Dict[str, int] = JapaneseNumeric.RoundNumberMap
    zero_to_nine_map: Dict[str, int] = JapaneseNumeric.ZeroToNineMap
    round_number_map_char: Dict[str, int] = JapaneseNumeric.RoundNumberMapChar
    full_to_half_map: Dict[str, str] = JapaneseNumeric.FullToHalfMap
    unit_map: Dict[str, str] = JapaneseNumeric.UnitMap
    trato_sim_map: Dict[str, int] = None

    round_direct_list: List[str] = JapaneseNumeric.RoundDirectList
    ten_chars: List[str] = JapaneseNumeric.TenChars

    negative_number_sign_regex: Pattern = RegExpUtility.get_safe_reg_exp(JapaneseNumeric.NegativeNumberSignRegex)
    half_a_dozen_regex: Optional[Pattern] = None
    digital_number_regex: Pattern = RegExpUtility.get_safe_reg_exp(JapaneseNumeric.DigitalNumberRegex)
    round_multiplier_regex: Optional[Pattern] = None
    double_and_round_regex: Pattern = RegExpUtility.get_safe_reg_exp(JapaneseNumeric.DoubleAndRoundRegex)
    frac_split_regex: Pattern = RegExpUtility.get_safe_reg_exp(JapaneseNumeric.FracSplitRegex)
    point_regex = JapaneseNumeric.PointRegex
    spe_get_number_regex: Pattern = RegExpUtility.get_safe_reg_exp(JapaneseNumeric.SpeGetNumberRegex)
    pair_regex: Pattern = RegExpUtility.get_safe_reg_exp(JapaneseNumeric.PairRegex)
    round_number_integer_regex: Pattern = RegExpUtility.get_safe_reg_exp(JapaneseNumeric.RoundNumberIntegerRegex)
    digit_num_regex: str = JapaneseNumeric.DigitNumRegex
    dozen_regex: str = JapaneseNumeric.DozenRegex
    percentage_regex: str = JapaneseNumeric.PercentageRegex

    def __init__(self, culture_info: Optional[CultureInfo] = None):
        culture_info = culture_info or CultureInfo(Culture.Japanese)
        super().__init__(culture_info)

    def normalize_token_set(self, tokens: List[str], context: ParseResult) -> List[str]:
        return tokens

    def resolve_composite_number(self, number_str: str) -> int:
        return 0
