#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from typing import Dict, Pattern, List, Optional

from recognizers_text.utilities import RegExpUtility
from recognizers_text.culture import Culture
from recognizers_text.parser import ParseResult
from recognizers_number.culture import CultureInfo
from recognizers_number.number.parsers import BaseNumberParserConfiguration
from recognizers_number.resources.italian_numeric import ItalianNumeric


class ItalianNumberParserConfiguration(BaseNumberParserConfiguration):

    lang_marker: str = ItalianNumeric.LangMarker
    is_multi_decimal_separator_culture: bool = ItalianNumeric.MultiDecimalSeparatorCulture

    decimal_separator_char: str = ItalianNumeric.DecimalSeparatorChar
    fraction_marker_token: str = ItalianNumeric.FractionMarkerToken
    non_decimal_separator_char: str = ItalianNumeric.NonDecimalSeparatorChar
    half_a_dozen_text: str = ItalianNumeric.HalfADozenText
    word_separator_token: str = ItalianNumeric.WordSeparatorToken

    written_decimal_separator_texts: List[str] = ItalianNumeric.WrittenDecimalSeparatorTexts
    written_group_separator_texts: List[str] = ItalianNumeric.WrittenGroupSeparatorTexts
    written_integer_separator_texts: List[str] = ItalianNumeric.WrittenIntegerSeparatorTexts
    written_fraction_separator_texts: List[str] = ItalianNumeric.WrittenFractionSeparatorTexts
    non_standard_separator_variants: List[str] = []

    cardinal_number_map: Dict[str, int] = ItalianNumeric.CardinalNumberMap
    ordinal_number_map: Dict[str, int] = ItalianNumeric.OrdinalNumberMap
    round_number_map: Dict[str, int] = ItalianNumeric.RoundNumberMap

    negative_number_sign_regex: Pattern = RegExpUtility.get_safe_reg_exp(ItalianNumeric.NegativeNumberSignRegex)
    half_a_dozen_regex: Pattern = RegExpUtility.get_safe_reg_exp(ItalianNumeric.HalfADozenRegex)
    digital_number_regex: Pattern = RegExpUtility.get_safe_reg_exp(ItalianNumeric.DigitalNumberRegex)
    round_multiplier_regex: Pattern = RegExpUtility.get_safe_reg_exp(ItalianNumeric.RoundMultiplierRegex)

    def __init__(self, culture_info: Optional[CultureInfo] = None):
        culture_info = culture_info or CultureInfo(Culture.Italian)
        super().__init__(culture_info)

    def normalize_token_set(self, tokens: List[str], context: ParseResult) -> List[str]:
        frac_words: List[str] = super().normalize_token_set(tokens, context)

        # The following piece of code is needed to compute the fraction pattern number+'e mezzo'
        # e.g. 'due e mezzo' ('two and a half') where the numerator is omitted in Italian.
        # It works by inserting the numerator 'un' ('a') in the list frac_words
        # so that the pattern is correctly processed.
        if len(frac_words) > 2:
            if frac_words[len(frac_words) - 1] == ItalianNumeric.OneHalfTokens[1] and \
                    frac_words[len(frac_words) - 2] == ItalianNumeric.WordSeparatorToken:
                frac_words[len(frac_words) - 2] = ItalianNumeric.WrittenFractionSeparatorTexts[0]
                frac_words.insert(len(frac_words) - 1, ItalianNumeric.OneHalfTokens[0])

        return frac_words
