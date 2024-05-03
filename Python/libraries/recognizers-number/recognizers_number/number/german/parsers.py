#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from typing import Dict, List, Optional, Pattern

from recognizers_number.culture import CultureInfo
from recognizers_number.number.parsers import BaseNumberParserConfiguration
from recognizers_number.resources.german_numeric import GermanNumeric
from recognizers_text.culture import Culture
from recognizers_text.parser import ParseResult
from recognizers_text.utilities import RegExpUtility


class GermanNumberParserConfiguration(BaseNumberParserConfiguration):

    lang_marker: str = GermanNumeric.LangMarker
    is_multi_decimal_separator_culture: bool = GermanNumeric.MultiDecimalSeparatorCulture

    decimal_separator_char: str = GermanNumeric.DecimalSeparatorChar
    fraction_marker_token: str = GermanNumeric.FractionMarkerToken
    non_decimal_separator_char: str = GermanNumeric.NonDecimalSeparatorChar
    half_a_dozen_text: str = GermanNumeric.HalfADozenText
    word_separator_token: str = GermanNumeric.WordSeparatorToken

    written_decimal_separator_texts: List[str] = GermanNumeric.WrittenDecimalSeparatorTexts
    written_group_separator_texts: List[str] = GermanNumeric.WrittenGroupSeparatorTexts
    written_integer_separator_texts: List[str] = GermanNumeric.WrittenIntegerSeparatorTexts
    written_fraction_separator_texts: List[str] = GermanNumeric.WrittenFractionSeparatorTexts
    non_standard_separator_variants: List[str] = []

    cardinal_number_map: Dict[str, int] = GermanNumeric.CardinalNumberMap
    ordinal_number_map: Dict[str, int] = GermanNumeric.OrdinalNumberMap
    round_number_map: Dict[str, int] = GermanNumeric.RoundNumberMap

    negative_number_sign_regex: Pattern = RegExpUtility.get_safe_reg_exp(GermanNumeric.NegativeNumberSignRegex)
    half_a_dozen_regex: Pattern = RegExpUtility.get_safe_reg_exp(GermanNumeric.HalfADozenRegex)
    digital_number_regex: Pattern = RegExpUtility.get_safe_reg_exp(GermanNumeric.DigitalNumberRegex)
    round_multiplier_regex: Pattern = RegExpUtility.get_safe_reg_exp(GermanNumeric.RoundMultiplierRegex)
    fraction_units_regex: Pattern = RegExpUtility.get_safe_reg_exp(GermanNumeric.FractionUnitsRegex)
    fraction_half_regex: Pattern = RegExpUtility.get_safe_reg_exp(GermanNumeric.FractionHalfRegex)

    def __init__(self, culture_info: Optional[CultureInfo] = None):
        culture_info = culture_info or CultureInfo(Culture.German)
        super().__init__(culture_info)

    def normalize_token_set(self, tokens: List[str], context: ParseResult) -> List[str]:
        frac_words: List[str] = super().normalize_token_set(tokens, context)

        # The following piece of code is needed to compute the fraction pattern number+'einhalb'
        # e.g. 'zweieinhalb' ('two and a half').
        try:
            frac_words.remove("/")  # .remove() raises a value error so this must be caught
        except ValueError:
            pass
        for idx, word in enumerate(frac_words):
            if self.fraction_half_regex.search(word):  # zweieinhalb, dreienhalb etc. case
                frac_words[idx] = word[0:(len(word)-7)]
                frac_words.append(self.written_fraction_separator_texts[0])
                frac_words.append(GermanNumeric.OneHalfTokens[0])
                frac_words.append(GermanNumeric.OneHalfTokens[1])
            elif m := self.fraction_units_regex.search(word):
                if m.group("onehalf"):  # 'einundhalb' case
                    frac_words[idx] = GermanNumeric.OneHalfTokens[0]
                    frac_words.append(self.written_fraction_separator_texts[0])
                    frac_words.append(GermanNumeric.OneHalfTokens[0])
                    frac_words.append(GermanNumeric.OneHalfTokens[1])
                if m.group("quarter"):  # 'dreiviertal' case
                    frac_words[idx] = word[0:len("drei")]
                    frac_words.append(self.written_fraction_separator_texts[0])
                    frac_words.append(word[len(frac_words[idx]):len("viertel")+len(frac_words[idx])])

        return frac_words
