from typing import Pattern

from recognizers_text.utilities import RegExpUtility
from recognizers_number.number.extractors import BaseNumberExtractor
from recognizers_number.number.arabic.extractors import ArabicCardinalExtractor
from ...resources.arabic_date_time import ArabicDateTime
from ..base_duration import DurationExtractorConfiguration


class ArabicDurationExtractorConfiguration(DurationExtractorConfiguration):

    @property
    def special_number_unit_regex(self):
        return self._special_number_unit_regex

    @property
    def check_both_before_after(self):
        return self._check_both_before_after

    @property
    def all_regex(self) -> Pattern:
        return self._all_regex

    @property
    def half_regex(self) -> Pattern:
        return self._half_regex

    @property
    def followed_unit(self) -> Pattern:
        return self._followed_unit

    @property
    def number_combined_with_unit(self) -> Pattern:
        return self._number_combined_with_unit

    @property
    def an_unit_regex(self) -> Pattern:
        return self._an_unit_regex

    @property
    def inexact_number_unit_regex(self) -> Pattern:
        return self._inexact_number_unit_regex

    @property
    def suffix_and_regex(self) -> Pattern:
        return self._suffix_and_regex

    @property
    def relative_duration_unit_regex(self) -> Pattern:
        return self._relative_duration_unit_regex

    @property
    def cardinal_extractor(self) -> BaseNumberExtractor:
        return self._cardinal_extractor

    @property
    def during_regex(self) -> Pattern:
        return self._during_regex

    @property
    def unit_map(self) -> Pattern:
        return self._unit_map

    @property
    def unit_value_map(self) -> {}:
        return self._unit_value_map

    @property
    def duration_unit_regex(self) -> {}:
        return self._duration_unit_regex

    @property
    def duration_connector_regex(self) -> Pattern:
        return self._duration_connector_regex

    @property
    def more_than_regex(self) -> Pattern:
        return self._more_than_regex

    @property
    def less_than_regex(self) -> Pattern:
        return self._less_than_regex

    @property
    def conjunction_regex(self) -> Pattern:
        return self._conjunction_regex

    @property
    def inexact_number_regex(self) -> Pattern:
        return self._inexact_number_regex

    def __init__(self):
        super().__init__()
        self._check_both_before_after = ArabicDateTime.CheckBothBeforeAfter
        self._all_regex: Pattern = RegExpUtility.get_safe_reg_exp(
            ArabicDateTime.AllRegex)
        self._half_regex: Pattern = RegExpUtility.get_safe_reg_exp(
            ArabicDateTime.HalfRegex)
        self._followed_unit: Pattern = RegExpUtility.get_safe_reg_exp(
            ArabicDateTime.DurationFollowedUnit)
        self._number_combined_with_unit: Pattern = RegExpUtility.get_safe_reg_exp(
            ArabicDateTime.NumberCombinedWithDurationUnit)
        self._an_unit_regex: Pattern = RegExpUtility.get_safe_reg_exp(
            ArabicDateTime.AnUnitRegex)
        self._inexact_number_unit_regex: Pattern = RegExpUtility.get_safe_reg_exp(
            ArabicDateTime.InexactNumberUnitRegex)
        self._suffix_and_regex: Pattern = RegExpUtility.get_safe_reg_exp(
            ArabicDateTime.SuffixAndRegex)
        self._relative_duration_unit_regex: Pattern = RegExpUtility.get_safe_reg_exp(
            ArabicDateTime.RelativeDurationUnitRegex
        )
        self._during_regex: Pattern = RegExpUtility.get_safe_reg_exp(
            ArabicDateTime.DuringRegex
        )
        self._cardinal_extractor: BaseNumberExtractor = ArabicCardinalExtractor()
        self._unit_map = ArabicDateTime.UnitMap
        self._unit_value_map = ArabicDateTime.UnitValueMap
        self._duration_unit_regex = RegExpUtility.get_safe_reg_exp(
            ArabicDateTime.DurationUnitRegex
        )
        self._duration_connector_regex = RegExpUtility.get_safe_reg_exp(
            ArabicDateTime.DurationConnectorRegex
        )
        self._more_than_regex = RegExpUtility.get_safe_reg_exp(
            ArabicDateTime.MoreThanRegex
        )
        self._less_than_regex = RegExpUtility.get_safe_reg_exp(
            ArabicDateTime.LessThanRegex
        )
        self._conjunction_regex = RegExpUtility.get_safe_reg_exp(
            ArabicDateTime.ConjunctionRegex
        )
        self._inexact_number_regex = RegExpUtility.get_safe_reg_exp(
            ArabicDateTime.InexactNumberRegex
        )
        self._special_number_with_unit_regex = None
        self._check_both_before_after = ArabicDateTime.CheckBothBeforeAfter
        # TODO When the implementation for these properties is added, change the None values to their respective Regexps
        self._special_number_unit_regex = None
