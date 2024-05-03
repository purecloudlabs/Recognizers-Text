#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from typing import Dict, Pattern, List, Optional

from recognizers_text.utilities import RegExpUtility
from recognizers_text.culture import Culture
from recognizers_text.parser import ParseResult
from recognizers_number.culture import CultureInfo
from recognizers_number.number.parsers import BaseNumberParserConfiguration
from recognizers_number.resources.dutch_numeric import DutchNumeric


class DutchNumberParserConfiguration(BaseNumberParserConfiguration):

    lang_marker: str = DutchNumeric.LangMarker
    is_multi_decimal_separator_culture: bool = DutchNumeric.MultiDecimalSeparatorCulture

    decimal_separator_char: str = DutchNumeric.DecimalSeparatorChar
    fraction_marker_token: str = DutchNumeric.FractionMarkerToken
    non_decimal_separator_char: str = DutchNumeric.NonDecimalSeparatorChar
    half_a_dozen_text: str = DutchNumeric.HalfADozenText
    word_separator_token: str = DutchNumeric.WordSeparatorToken

    written_decimal_separator_texts: List[str] = DutchNumeric.WrittenDecimalSeparatorTexts
    written_group_separator_texts: List[str] = DutchNumeric.WrittenGroupSeparatorTexts
    written_integer_separator_texts: List[str] = DutchNumeric.WrittenIntegerSeparatorTexts
    written_fraction_separator_texts: List[str] = DutchNumeric.WrittenFractionSeparatorTexts
    non_standard_separator_variants: List[str] = []

    cardinal_number_map: Dict[str, int] = DutchNumeric.CardinalNumberMap
    ordinal_number_map: Dict[str, int] = DutchNumeric.OrdinalNumberMap
    round_number_map: Dict[str, int] = DutchNumeric.RoundNumberMap

    negative_number_sign_regex: Pattern = RegExpUtility.get_safe_reg_exp(DutchNumeric.NegativeNumberSignRegex)
    half_a_dozen_regex: Pattern = RegExpUtility.get_safe_reg_exp(DutchNumeric.HalfADozenRegex)
    digital_number_regex: Pattern = RegExpUtility.get_safe_reg_exp(DutchNumeric.DigitalNumberRegex)
    round_multiplier_regex: Pattern = RegExpUtility.get_safe_reg_exp(DutchNumeric.RoundMultiplierRegex)
    fraction_units_regex: Pattern = RegExpUtility.get_safe_reg_exp(DutchNumeric.FractionUnitsRegex)
    fraction_half_regex: Pattern = RegExpUtility.get_safe_reg_exp(DutchNumeric.FractionHalfRegex)

    def __init__(self, culture_info: Optional[CultureInfo] = None):
        culture_info = culture_info or CultureInfo(Culture.Dutch)
        super().__init__(culture_info)

    # Same behavior as the base but also handles numbers such as tweeënhalf and tweeëneenhalf
    def normalize_token_set(self, tokens: List[str], context: ParseResult) -> List[str]:
        frac_words: List[str] = super().normalize_token_set(tokens, context)

        # The following piece of code is needed to compute the fraction pattern number+'ënhalf'
        # e.g. 'tweeënhalf' ('two and a half'). Similarly for "ëneenhalf", e.g. tweeëneenhalf.
        length = 2
        try:
            frac_words.remove("/")  # .remove() raises a value error so this must be caught
        except ValueError:
            pass
        for idx, word in enumerate(frac_words):
            if self.fraction_half_regex.search(word):
                frac_words[idx] = word[0:(len(word) - 6)]
                frac_words.append(self.written_fraction_separator_texts[0])
                frac_words.append(DutchNumeric.OneHalfTokens[0])
                frac_words.append(DutchNumeric.OneHalfTokens[1])
                length = 4
            elif m := self.fraction_units_regex.search(word):
                if m.group("onehalf"):
                    frac_words[idx] = DutchNumeric.OneHalfTokens[0]
                    frac_words.append(self.written_fraction_separator_texts[0])
                    frac_words.append(DutchNumeric.OneHalfTokens[0])
                    frac_words.append(DutchNumeric.OneHalfTokens[1])
                    length = 4
                if m.group("quarter"):
                    frac_words[idx] = word[0:len("drie")]
                    frac_words.append(self.written_fraction_separator_texts[0])
                    frac_words.append(word[len(frac_words[idx]):len("kwartaal") + len(frac_words[idx])])
                    length = 3

        fracLen = len(frac_words)

        if fracLen > length and frac_words[fracLen - length - 1] != DutchNumeric.WordSeparatorToken:
            if not (all(i in frac_words for i in ["op", "de"]) or all(i in frac_words for i in ["van", "de"])
                    or all(i in frac_words for i in ["uit", "de"])):
                frac_words.insert(fracLen - length, DutchNumeric.WordSeparatorToken)

        return frac_words
