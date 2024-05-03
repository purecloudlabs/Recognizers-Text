#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from typing import Dict, Pattern, List, Optional
import regex

from recognizers_text.utilities import RegExpUtility
from recognizers_text.culture import Culture
from recognizers_text.parser import ParseResult
from recognizers_number.culture import CultureInfo
from recognizers_number.number.parsers import BaseNumberParserConfiguration
from recognizers_number.resources.portuguese_numeric import PortugueseNumeric


class PortugueseNumberParserConfiguration(BaseNumberParserConfiguration):

    lang_marker: str = PortugueseNumeric.LangMarker
    is_multi_decimal_separator_culture: bool = PortugueseNumeric.MultiDecimalSeparatorCulture

    decimal_separator_char: str = PortugueseNumeric.DecimalSeparatorChar
    fraction_marker_token: str = PortugueseNumeric.FractionMarkerToken
    non_decimal_separator_char: str = PortugueseNumeric.NonDecimalSeparatorChar
    half_a_dozen_text: str = PortugueseNumeric.HalfADozenText
    word_separator_token: str = PortugueseNumeric.WordSeparatorToken

    written_decimal_separator_texts: List[str] = PortugueseNumeric.WrittenDecimalSeparatorTexts
    written_group_separator_texts: List[str] = PortugueseNumeric.WrittenGroupSeparatorTexts
    written_integer_separator_texts: List[str] = PortugueseNumeric.WrittenIntegerSeparatorTexts
    written_fraction_separator_texts: List[str] = PortugueseNumeric.WrittenFractionSeparatorTexts
    non_standard_separator_variants: List[str] = []

    cardinal_number_map: Dict[str, int] = PortugueseNumeric.CardinalNumberMap
    ordinal_number_map: Dict[str, int] = PortugueseNumeric.OrdinalNumberMap
    round_number_map: Dict[str, int] = PortugueseNumeric.RoundNumberMap

    negative_number_sign_regex: Pattern = RegExpUtility.get_safe_reg_exp(PortugueseNumeric.NegativeNumberSignRegex)
    half_a_dozen_regex: Pattern = RegExpUtility.get_safe_reg_exp(PortugueseNumeric.HalfADozenRegex)
    digital_number_regex: Pattern = RegExpUtility.get_safe_reg_exp(PortugueseNumeric.DigitalNumberRegex)
    round_multiplier_regex: Pattern = RegExpUtility.get_safe_reg_exp(PortugueseNumeric.RoundMultiplierRegex)

    def __init__(self, culture_info: Optional[CultureInfo] = None):
        culture_info = culture_info or CultureInfo(Culture.Portuguese)
        super().__init__(culture_info)

    def normalize_token_set(self, tokens: List[str], context: ParseResult) -> List[str]:
        result = []

        for token in tokens:
            temp_word = regex.sub(r'^s+|s+$', '', token)
            if temp_word in self.ordinal_number_map:
                result.append(temp_word)
                break

            # ends with 'avo' or 'ava'
            if any(suffix for suffix in PortugueseNumeric.WrittenFractionSuffix if temp_word.endswith(suffix)):
                orig_temp_word = temp_word
                new_length = len(orig_temp_word)
                temp_word = orig_temp_word[0:new_length - 3]
                if not temp_word:
                    break
                elif temp_word in self.cardinal_number_map:
                    result.append(temp_word)
                    break
                else:
                    temp_word = orig_temp_word[0:new_length - 2]
                    if temp_word in self.cardinal_number_map:
                        result.append(temp_word)
                        break
            result.append(token)

        # The following piece of code is needed to compute the fraction pattern number+'e meio'
        # e.g. 'cinco e meio' ('five and a half') where the numerator is omitted in Portuguese.
        # It works by inserting the numerator 'um' ('a') in the list result
        # so that the pattern is correctly processed.
        if len(result) > 2:
            if result[len(result) - 1] == PortugueseNumeric.OneHalfTokens[1] and \
                    result[len(result) - 2] == PortugueseNumeric.WordSeparatorToken:
                result[len(result) - 2] = PortugueseNumeric.WrittenFractionSeparatorTexts[0]
                result.insert(len(result) - 1, PortugueseNumeric.OneHalfTokens[0])

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
        i = 0
        while i < len(number_str):
            str_builder += number_str[i]
            if str_builder in self.cardinal_number_map and self.cardinal_number_map[str_builder] > value:
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
