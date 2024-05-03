#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from typing import Dict, List, Optional, Pattern

from recognizers_number.culture import CultureInfo
from recognizers_number.number.parsers import BaseNumberParserConfiguration
from recognizers_number.resources.french_numeric import FrenchNumeric
from recognizers_text.culture import Culture
from recognizers_text.parser import ParseResult
from recognizers_text.utilities import RegExpUtility


class FrenchNumberParserConfiguration(BaseNumberParserConfiguration):

    lang_marker: str = FrenchNumeric.LangMarker
    is_multi_decimal_separator_culture: bool = FrenchNumeric.MultiDecimalSeparatorCulture

    decimal_separator_char: str = FrenchNumeric.DecimalSeparatorChar
    fraction_marker_token: str = FrenchNumeric.FractionMarkerToken
    non_decimal_separator_char: str = FrenchNumeric.NonDecimalSeparatorChar
    half_a_dozen_text: str = FrenchNumeric.HalfADozenText
    word_separator_token: str = FrenchNumeric.WordSeparatorToken

    written_decimal_separator_texts: List[str] = FrenchNumeric.WrittenDecimalSeparatorTexts
    written_group_separator_texts: List[str] = FrenchNumeric.WrittenGroupSeparatorTexts
    written_integer_separator_texts: List[str] = FrenchNumeric.WrittenIntegerSeparatorTexts
    written_fraction_separator_texts: List[str] = FrenchNumeric.WrittenFractionSeparatorTexts
    non_standard_separator_variants: List[str] = []

    cardinal_number_map: Dict[str, int] = FrenchNumeric.CardinalNumberMap
    ordinal_number_map: Dict[str, int] = FrenchNumeric.OrdinalNumberMap
    round_number_map: Dict[str, int] = FrenchNumeric.RoundNumberMap

    negative_number_sign_regex: Pattern = RegExpUtility.get_safe_reg_exp(FrenchNumeric.NegativeNumberSignRegex)
    half_a_dozen_regex: Pattern = RegExpUtility.get_safe_reg_exp(FrenchNumeric.HalfADozenRegex)
    digital_number_regex: Pattern = RegExpUtility.get_safe_reg_exp(FrenchNumeric.DigitalNumberRegex)
    round_multiplier_regex: Pattern = RegExpUtility.get_safe_reg_exp(FrenchNumeric.RoundMultiplierRegex)

    def __init__(self, culture_info: Optional[CultureInfo] = None):
        culture_info = culture_info or CultureInfo(Culture.French)
        super().__init__(culture_info)

    def normalize_token_set(self, tokens: List[str], context: ParseResult) -> List[str]:
        frac_words: List[str] = super().normalize_token_set(tokens, context)

        # The following piece of code is needed to compute the fraction pattern number+'et demi'
        # e.g. 'deux et demi' ('two and a half') where the numerator is omitted in French.
        # It works by inserting the numerator 'un' ('a') in the list frac_words
        #
        if len(frac_words) > 2:
            if frac_words[len(frac_words) - 1] == FrenchNumeric.OneHalfTokens[1] and \
                    frac_words[len(frac_words) - 2] == FrenchNumeric.WordSeparatorToken:
                frac_words.insert(len(frac_words) - 1, FrenchNumeric.OneHalfTokens[0])

        return frac_words

    def resolve_composite_number(self, number_str: str) -> int:
        if number_str in self.ordinal_number_map:
            return self.ordinal_number_map[number_str]
        if number_str in self.cardinal_number_map:
            return self.cardinal_number_map[number_str]

        value = 0
        final_value = 0
        str_builder = ''
        last_good_char = 0
        i = 0
        while i < len(number_str):
            str_builder += number_str[i]
            if (str_builder in self.cardinal_number_map
                    and self.cardinal_number_map[str_builder] > value):
                last_good_char = i
                value = self.cardinal_number_map[str_builder]

            if (i + 1) == len(number_str):
                final_value += value
                str_builder = ''
                i = last_good_char
                last_good_char += 1
                value = 0
            i += 1

        return final_value
