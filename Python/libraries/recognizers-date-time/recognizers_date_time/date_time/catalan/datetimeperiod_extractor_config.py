#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from typing import List, Pattern

from recognizers_number import BaseNumberExtractor, CatalanCardinalExtractor
from recognizers_text.utilities import RegExpUtility
from ...resources.catalan_date_time import CatalanDateTime
from ..extractors import DateTimeExtractor
from ..base_datetimeperiod import DateTimePeriodExtractorConfiguration, MatchedIndex
from ..base_date import BaseDateExtractor
from ..base_time import BaseTimeExtractor
from ..base_duration import BaseDurationExtractor
from ..base_timeperiod import BaseTimePeriodExtractor
from ..base_datetime import BaseDateTimeExtractor
from ..base_timezone import BaseTimeZoneExtractor
from .date_extractor_config import CatalanDateExtractorConfiguration
from .time_extractor_config import CatalanTimeExtractorConfiguration
from .duration_extractor_config import CatalanDurationExtractorConfiguration
from .timeperiod_extractor_config import CatalanTimePeriodExtractorConfiguration
from .datetime_extractor_config import CatalanDateTimeExtractorConfiguration
from ..utilities import DateTimeOptions
from .timezone_extractor_config import CatalanTimeZoneExtractorConfiguration


class CatalanDateTimePeriodExtractorConfiguration(DateTimePeriodExtractorConfiguration):
    @property
    def future_regex(self) -> BaseNumberExtractor:
        return self._future_regex

    @property
    def past_regex(self) -> BaseNumberExtractor:
        return self._past_regex

    @property
    def check_both_before_after(self) -> Pattern:
        return self._check_both_before_after

    @property
    def suffix_regex(self) -> Pattern:
        return self._suffix_regex

    @property
    def options(self):
        return self._options

    @property
    def dmy_date_format(self) -> bool:
        return self._dmy_date_format

    @property
    def cardinal_extractor(self) -> BaseNumberExtractor:
        return self._cardinal_extractor

    @property
    def single_date_extractor(self) -> DateTimeExtractor:
        return self._single_date_extractor

    @property
    def single_time_extractor(self) -> DateTimeExtractor:
        return self._single_time_extractor

    @property
    def single_date_time_extractor(self) -> DateTimeExtractor:
        return self._single_date_time_extractor

    @property
    def duration_extractor(self) -> DateTimeExtractor:
        return self._duration_extractor

    @property
    def time_period_extractor(self) -> DateTimeExtractor:
        return self._time_period_extractor

    @property
    def time_zone_extractor(self) -> DateTimeExtractor:
        return self._time_zone_extractor

    @property
    def simple_cases_regexes(self) -> List[Pattern]:
        return self._simple_cases_regexes

    @property
    def preposition_regex(self) -> Pattern:
        return self._preposition_regex

    @property
    def till_regex(self) -> Pattern:
        return self._till_regex

    @property
    def specific_time_of_day_regex(self) -> Pattern:
        return self._specific_time_of_day_regex

    @property
    def time_of_day_regex(self) -> Pattern:
        return self._time_of_day_regex

    @property
    def period_time_of_day_with_date_regex(self) -> Pattern:
        return self._period_time_of_day_with_date_regex

    @property
    def followed_unit(self) -> Pattern:
        return self._followed_unit

    @property
    def number_combined_with_unit(self) -> Pattern:
        return self._number_combined_with_unit

    @property
    def time_unit_regex(self) -> Pattern:
        return self._time_unit_regex

    @property
    def previous_prefix_regex(self) -> Pattern:
        return self._past_prefix_regex

    @property
    def next_prefix_regex(self) -> Pattern:
        return self._next_prefix_regex

    @property
    def relative_time_unit_regex(self) -> Pattern:
        return self._relative_time_unit_regex

    @property
    def rest_of_date_time_regex(self) -> Pattern:
        return self._rest_of_date_time_regex

    @property
    def week_day_regex(self) -> Pattern:
        return self._week_day_regex

    @property
    def general_ending_regex(self) -> Pattern:
        return self._general_ending_regex

    @property
    def middle_pause_regex(self) -> Pattern:
        return self._middle_pause_regex

    @property
    def within_next_prefix_regex(self) -> Pattern:
        return self._within_next_prefix_regex

    @property
    def token_before_date(self) -> str:
        return self._token_before_date

    @property
    def future_suffix_regex(self) -> Pattern:
        return self._future_suffix_regex

    @property
    def date_unit_regex(self) -> Pattern:
        return self._date_unit_regex

    @property
    def am_desc_regex(self) -> Pattern:
        return self._am_desc_regex

    @property
    def pm_desc_regex(self) -> Pattern:
        return self._pm_desc_regex

    @property
    def prefix_day_regex(self) -> Pattern:
        return self._prefix_day_regex

    @property
    def before_regex(self) -> Pattern:
        return self._before_regex

    @property
    def after_regex(self) -> Pattern:
        return self._after_regex

    def __init__(self):
        super().__init__()
        self._check_both_before_after = CatalanDateTime.CheckBothBeforeAfter
        self._simple_cases_regexes = [
            RegExpUtility.get_safe_reg_exp(CatalanDateTime.PureNumFromTo),
            RegExpUtility.get_safe_reg_exp(CatalanDateTime.PureNumBetweenAnd)
        ]
        self._preposition_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.PrepositionRegex)
        self._till_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.TillRegex)
        self._specific_time_of_day_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.SpecificTimeOfDayRegex)
        self._time_of_day_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.TimeOfDayRegex)
        self._followed_unit = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.FollowedUnit)
        self._time_unit_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.UnitRegex)
        self._past_prefix_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.PastRegex)
        self._next_prefix_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.NextPrefixRegex)
        self._number_combined_with_unit = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.DateTimePeriodNumberCombinedWithUnit)
        self._week_day_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.WeekDayRegex)
        self._period_time_of_day_with_date_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.PeriodTimeOfDayWithDateRegex)
        self._relative_time_unit_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.RelativeTimeUnitRegex)
        self._rest_of_date_time_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.RestOfDateTimeRegex)
        self._general_ending_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.GeneralEndingRegex)
        self._middle_pause_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.MiddlePauseRegex)

        self.from_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.FromRegex)
        self.range_connector_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.RangeConnectorRegex)
        self.between_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.BetweenRegex)

        self._cardinal_extractor = CatalanCardinalExtractor()

        self._single_date_extractor = BaseDateExtractor(
            CatalanDateExtractorConfiguration())
        self._single_time_extractor = BaseTimeExtractor(
            CatalanTimeExtractorConfiguration())
        self._single_date_time_extractor = BaseDateTimeExtractor(
            CatalanDateTimeExtractorConfiguration())
        self._duration_extractor = BaseDurationExtractor(
            CatalanDurationExtractorConfiguration())
        self._time_period_extractor = BaseTimePeriodExtractor(
            CatalanTimePeriodExtractorConfiguration())
        self._time_zone_extractor = BaseTimeZoneExtractor(
            CatalanTimeZoneExtractorConfiguration())
        self._within_next_prefix_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.WithinNextPrefixRegex
        )
        self._time_unit_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.TimeUnitRegex
        )
        self._token_before_date = CatalanDateTime.TokenBeforeDate
        self._within_next_prefix_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.WithinNextPrefixRegex
        )
        self._future_suffix_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.FutureSuffixRegex
        )
        self._date_unit_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.DateUnitRegex
        )
        self._am_desc_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.AmDescRegex
        )
        self._pm_desc_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.PmDescRegex
        )
        self._prefix_day_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.PrefixDayRegex
        )
        self._before_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.BeforeRegex
        )
        self._after_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.AfterRegex
        )
        self._options = DateTimeOptions.NONE
        self._suffix_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.SuffixRegex
        )
        self._check_both_before_after = CatalanDateTime.CheckBothBeforeAfter
        self._past_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.PastRegex
        )
        self._future_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.FutureRegex
        )

    def get_from_token_index(self, source: str) -> MatchedIndex:
        match = self.from_regex.search(source)
        if match:
            return MatchedIndex(True, match.start())

        return MatchedIndex(False, -1)

    def get_between_token_index(self, source: str) -> MatchedIndex:
        match = self.between_regex.search(source)
        if match:
            return MatchedIndex(True, match.start())

        return MatchedIndex(False, -1)

    def has_connector_token(self, source: str) -> MatchedIndex:
        match = self.range_connector_regex.search(source)
        if match:
            return MatchedIndex(True, match.start())

        return MatchedIndex(False, -1)
