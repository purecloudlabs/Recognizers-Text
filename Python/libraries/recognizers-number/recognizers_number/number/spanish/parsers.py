#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from typing import Dict, List, Optional, Pattern

import regex

from recognizers_number.culture import CultureInfo
from recognizers_number.number.parsers import BaseNumberParserConfiguration
from recognizers_number.resources.spanish_numeric import SpanishNumeric
from recognizers_text.culture import Culture
from recognizers_text.parser import ParseResult
from recognizers_text.utilities import RegExpUtility


class SpanishNumberParserConfiguration(BaseNumberParserConfiguration):

    lang_marker: str = SpanishNumeric.LangMarker
    is_multi_decimal_separator_culture: bool = SpanishNumeric.MultiDecimalSeparatorCulture

    decimal_separator_char: str = SpanishNumeric.DecimalSeparatorChar
    fraction_marker_token: str = SpanishNumeric.FractionMarkerToken
    non_decimal_separator_char: str = SpanishNumeric.NonDecimalSeparatorChar
    half_a_dozen_text: str = SpanishNumeric.HalfADozenText
    word_separator_token: str = SpanishNumeric.WordSeparatorToken

    written_decimal_separator_texts: List[str] = SpanishNumeric.WrittenDecimalSeparatorTexts
    written_group_separator_texts: List[str] = SpanishNumeric.WrittenGroupSeparatorTexts
    written_integer_separator_texts: List[str] = SpanishNumeric.WrittenIntegerSeparatorTexts
    written_fraction_separator_texts: List[str] = SpanishNumeric.WrittenFractionSeparatorTexts
    non_standard_separator_variants: List[str] = SpanishNumeric.NonStandardSeparatorVariants

    cardinal_number_map: Dict[str, int] = SpanishNumeric.CardinalNumberMap
    round_number_map: Dict[str, int] = SpanishNumeric.RoundNumberMap

    negative_number_sign_regex: Pattern = RegExpUtility.get_safe_reg_exp(SpanishNumeric.NegativeNumberSignRegex)
    half_a_dozen_regex: Pattern = RegExpUtility.get_safe_reg_exp(SpanishNumeric.HalfADozenRegex)
    digital_number_regex: Pattern = RegExpUtility.get_safe_reg_exp(SpanishNumeric.DigitalNumberRegex)
    round_multiplier_regex: Pattern = RegExpUtility.get_safe_reg_exp(SpanishNumeric.RoundMultiplierRegex)

    @property
    def ordinal_number_map(self) -> Dict[str, int]:
        _ordinal_number_map: Dict[str, int] = SpanishNumeric.OrdinalNumberMap
        for prefix_key in SpanishNumeric.PrefixCardinalMap:
            for suffix_key in SpanishNumeric.SuffixOrdinalMap:
                if prefix_key + suffix_key not in _ordinal_number_map:
                    prefix_value = SpanishNumeric.PrefixCardinalMap[prefix_key]
                    suffix_value = SpanishNumeric.SuffixOrdinalMap[suffix_key]
                    _ordinal_number_map[prefix_key + suffix_key] = prefix_value * suffix_value
        return _ordinal_number_map

    def __init__(self, culture_info: Optional[CultureInfo] = None):
        culture_info = culture_info or CultureInfo(Culture.Spanish)
        super().__init__(culture_info)

    def normalize_token_set(self, tokens: List[str], context: ParseResult) -> List[str]:
        result: List[str] = list()
        for token in tokens:
            temp_word = regex.sub(r'^s+', '', token)
            temp_word = regex.sub(r's+$', '', temp_word)
            if temp_word in self.ordinal_number_map:
                result.append(temp_word)
                continue
            if temp_word.endswith('avo') or temp_word.endswith('ava'):
                oringinal_temp_word = temp_word
                new_length = len(temp_word)
                temp_word = oringinal_temp_word[0:new_length-3]
                if temp_word in self.cardinal_number_map:
                    result.append(temp_word)
                    continue
                else:
                    temp_word = oringinal_temp_word[0:new_length-2]
                    if temp_word in self.cardinal_number_map:
                        result.append(temp_word)
                        continue
            result.append(token)

        # The following piece of code is needed to compute the fraction pattern number+'y medio'
        # e.g. 'cinco y medio' ('five and a half') where the numerator is omitted in Spanish.
        # It works by inserting the numerator 'un' ('a') in the list result
        # so that the pattern is correctly processed.
        if len(result) > 2:
            if result[len(result) - 1] == SpanishNumeric.OneHalfTokens[1] and \
                    result[len(result) - 2] == SpanishNumeric.WordSeparatorToken:
                result[len(result) - 2] = SpanishNumeric.WrittenFractionSeparatorTexts[0]
                result.insert(len(result) - 1, SpanishNumeric.OneHalfTokens[0])

        return result

    def resolve_composite_number(self, number_str: str) -> int:
        if number_str in self.ordinal_number_map:
            return self.ordinal_number_map[number_str]
        if number_str in self.cardinal_number_map:
            return self.cardinal_number_map[number_str]

        value = 0
        final_value = 0
        str_builder = ''
        last_good_char = 0

        number_str_len = len(number_str)
        i = 0
        while i < number_str_len:
            str_builder += number_str[i]
            if (str_builder in self.cardinal_number_map and
                    self.cardinal_number_map[str_builder] > 0):
                last_good_char = i
                value = self.cardinal_number_map[str_builder]
            if i+1 == number_str_len:
                final_value += value
                str_builder = ''
                last_good_char += 1
                i = last_good_char
                value = 0
            else:
                i += 1

        return final_value
