#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from typing import List, Dict, Pattern, Optional
from collections import namedtuple
from decimal import Decimal, getcontext
import copy
import regex

from recognizers_text.utilities import RegExpUtility
from recognizers_text.culture import Culture
from recognizers_text.parser import ParseResult
from recognizers_number.resources.chinese_numeric import ChineseNumeric
from recognizers_number.number.cjk_parsers import CJKNumberParser
from recognizers_number.number.parsers import BaseNumberParser, BaseNumberParserConfiguration
from recognizers_number.culture import CultureInfo


class ChineseNumberParserConfiguration(BaseNumberParserConfiguration):

    lang_marker: str = ChineseNumeric.LangMarker
    is_multi_decimal_separator_culture: bool = ChineseNumeric.MultiDecimalSeparatorCulture

    decimal_separator_char: str = ChineseNumeric.DecimalSeparatorChar
    fraction_marker_token: str = ChineseNumeric.FractionMarkerToken
    non_decimal_separator_char: str = ChineseNumeric.NonDecimalSeparatorChar
    half_a_dozen_text: str = ChineseNumeric.HalfADozenText
    word_separator_token: str = ChineseNumeric.WordSeparatorToken
    zero_char: str = ChineseNumeric.ZeroChar
    pair_char: str = ChineseNumeric.PairChar

    written_decimal_separator_texts: List[str] = []
    written_group_separator_texts: List[str] = []
    written_integer_separator_texts: List[str] = []
    written_fraction_separator_texts: List[str] = []
    non_standard_separator_variants: List[str] = []

    cardinal_number_map: Dict[str, int] = {}
    ordinal_number_map: Dict[str, int] = {}
    round_number_map: Dict[str, int] = ChineseNumeric.RoundNumberMap
    zero_to_nine_map: Dict[str, int] = ChineseNumeric.ZeroToNineMap
    round_number_map_char: Dict[str, int] = ChineseNumeric.RoundNumberMapChar
    full_to_half_map: Dict[str, str] = ChineseNumeric.FullToHalfMap
    unit_map: Dict[str, str] = ChineseNumeric.UnitMap
    trato_sim_map: Dict[str, str] = ChineseNumeric.TratoSimMap

    round_direct_list: List[str] = ChineseNumeric.RoundDirectList
    ten_chars: List[str] = ChineseNumeric.TenChars

    negative_number_sign_regex = RegExpUtility.get_safe_reg_exp(ChineseNumeric.NegativeNumberSignRegex)
    half_a_dozen_regex: Optional[Pattern] = None
    digital_number_regex = RegExpUtility.get_safe_reg_exp(ChineseNumeric.DigitalNumberRegex)
    round_multiplier_regex: Optional[Pattern] = None
    double_and_round_regex: Pattern = RegExpUtility.get_safe_reg_exp(ChineseNumeric.DoubleAndRoundRegex)
    frac_split_regex: Pattern = RegExpUtility.get_safe_reg_exp(ChineseNumeric.FracSplitRegex)
    spe_get_number_regex: Pattern = RegExpUtility.get_safe_reg_exp(ChineseNumeric.SpeGetNumberRegex)
    pair_regex: Pattern = RegExpUtility.get_safe_reg_exp(ChineseNumeric.PairRegex)
    digit_num_regex: str = ChineseNumeric.DigitNumRegex
    dozen_regex: str = ChineseNumeric.DozenRegex
    percentage_regex: str = ChineseNumeric.PercentageRegex
    percentage_num_regex: str = ChineseNumeric.PercentageNumRegex
    point_regex: str = ChineseNumeric.PointRegex

    def __init__(self, culture_info: Optional[CultureInfo] = None):
        culture_info = culture_info or CultureInfo(Culture.Chinese)
        super().__init__(culture_info)

    def normalize_token_set(self, tokens: List[str], context: ParseResult) -> List[str]:
        return tokens

    def resolve_composite_number(self, number_str: str) -> int:
        return 0
