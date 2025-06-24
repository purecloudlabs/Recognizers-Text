#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from typing import Dict, Pattern, List

from recognizers_text.utilities import RegExpUtility
from recognizers_text.culture import Culture
from recognizers_text.parser import ParseResult
from recognizers_number.culture import CultureInfo
from recognizers_number.number.parsers import BaseNumberParserConfiguration
from recognizers_number.resources.hungarian_numeric import HungarianNumeric


class HungarianNumberParserConfiguration(BaseNumberParserConfiguration):
    @property
    def cardinal_number_map(self) -> Dict[str, int]:
        return self._cardinal_number_map

    @property
    def ordinal_number_map(self) -> Dict[str, int]:
        return self._ordinal_number_map

    @property
    def round_number_map(self) -> Dict[str, int]:
        return self._round_number_map

    @property
    def culture_info(self):
        return self._culture_info

    @property
    def digital_number_regex(self) -> Pattern:
        return self._digital_number_regex

    @property
    def fraction_marker_token(self) -> str:
        return self._fraction_marker_token

    @property
    def negative_number_sign_regex(self) -> Pattern:
        return self._negative_number_sign_regex

    @property
    def half_a_dozen_regex(self) -> Pattern:
        return self._half_a_dozen_regex

    @property
    def half_a_dozen_text(self) -> str:
        return self._half_a_dozen_text

    @property
    def lang_marker(self) -> str:
        return self._lang_marker

    @property
    def non_decimal_separator_char(self) -> str:
        return self._non_decimal_separator_char

    @property
    def decimal_separator_char(self) -> str:
        return self._decimal_separator_char

    @property
    def word_separator_token(self) -> str:
        return self._word_separator_token

    @property
    def written_decimal_separator_texts(self) -> List[str]:
        return self._written_decimal_separator_texts

    @property
    def written_group_separator_texts(self) -> List[str]:
        return self._written_group_separator_texts

    @property
    def written_integer_separator_texts(self) -> List[str]:
        return self._written_integer_separator_texts

    @property
    def written_fraction_separator_texts(self) -> List[str]:
        return self._written_fraction_separator_texts

    @property
    def non_standard_separator_variants(self) -> List[str]:
        return self._non_standard_separator_variants

    @property
    def is_multi_decimal_separator_culture(self) -> bool:
        return self._is_multi_decimal_separator_culture

    @property
    def round_multiplier_regex(self) -> Pattern:
        return self._round_multiplier_regex

    def __init__(self, culture_info=None):
        if culture_info is None:
            culture_info = CultureInfo(Culture.Hungarian)

        self._culture_info = culture_info
        self._lang_marker = HungarianNumeric.LangMarker
        self._decimal_separator_char = HungarianNumeric.DecimalSeparatorChar
        self._fraction_marker_token = HungarianNumeric.FractionMarkerToken
        self._non_decimal_separator_char = HungarianNumeric.NonDecimalSeparatorChar
        self._half_a_dozen_text = HungarianNumeric.HalfADozenText
        self._word_separator_token = HungarianNumeric.WordSeparatorToken

        self._written_decimal_separator_texts = HungarianNumeric.WrittenDecimalSeparatorTexts
        self._written_group_separator_texts = HungarianNumeric.WrittenGroupSeparatorTexts
        self._written_integer_separator_texts = HungarianNumeric.WrittenIntegerSeparatorTexts
        self._written_fraction_separator_texts = HungarianNumeric.WrittenFractionSeparatorTexts
        self._non_standard_separator_variants = HungarianNumeric.NonStandardSeparatorVariants
        self._is_multi_decimal_separator_culture = HungarianNumeric.MultiDecimalSeparatorCulture

        self._cardinal_number_map = HungarianNumeric.CardinalNumberMap
        self._ordinal_number_map = HungarianNumeric.OrdinalNumberMap
        self._round_number_map = HungarianNumeric.RoundNumberMap
        self._negative_number_sign_regex = RegExpUtility.get_safe_reg_exp(
            HungarianNumeric.NegativeNumberSignRegex)
        self._half_a_dozen_regex = RegExpUtility.get_safe_reg_exp(
            HungarianNumeric.HalfADozenRegex)
        self._digital_number_regex = RegExpUtility.get_safe_reg_exp(
            HungarianNumeric.DigitalNumberRegex)
        self._round_multiplier_regex = RegExpUtility.get_safe_reg_exp(
            HungarianNumeric.RoundMultiplierRegex)