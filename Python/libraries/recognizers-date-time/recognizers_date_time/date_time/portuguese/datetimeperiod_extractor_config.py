#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from typing import List, Pattern

import regex

from recognizers_number import BaseNumberExtractor, PortugueseCardinalExtractor
from recognizers_text.utilities import RegExpUtility

from ...resources.portuguese_date_time import PortugueseDateTime
from ..base_date import BaseDateExtractor
from ..base_datetime import BaseDateTimeExtractor
from ..base_datetimeperiod import DateTimePeriodExtractorConfiguration, MatchedIndex
from ..base_duration import BaseDurationExtractor
from ..base_time import BaseTimeExtractor
from ..base_timeperiod import BaseTimePeriodExtractor
from ..extractors import DateTimeExtractor
from ..utilities import DateTimeOptions
from .date_extractor_config import PortugueseDateExtractorConfiguration
from .datetime_extractor_config import PortugueseDateTimeExtractorConfiguration
from .duration_extractor_config import PortugueseDurationExtractorConfiguration
from .time_extractor_config import PortugueseTimeExtractorConfiguration
from .timeperiod_extractor_config import PortugueseTimePeriodExtractorConfiguration


class PortugueseDateTimePeriodExtractorConfiguration(DateTimePeriodExtractorConfiguration):
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
        self._week_day_regex = RegExpUtility.get_safe_reg_exp(PortugueseDateTime.WeekDayRegex)
        self._check_both_before_after = PortugueseDateTime.CheckBothBeforeAfter
        self._cardinal_extractor = PortugueseCardinalExtractor()
        self._single_date_extractor = BaseDateExtractor(PortugueseDateExtractorConfiguration())
        self._single_time_extractor = BaseTimeExtractor(PortugueseTimeExtractorConfiguration())
        self._single_date_time_extractor = BaseDateTimeExtractor(PortugueseDateTimeExtractorConfiguration())
        self._duration_extractor = BaseDurationExtractor(PortugueseDurationExtractorConfiguration())
        self._time_period_extractor = BaseTimePeriodExtractor(PortugueseTimePeriodExtractorConfiguration())
        self._simple_cases_regexes = [
            RegExpUtility.get_safe_reg_exp(PortugueseDateTime.PureNumFromTo),
            RegExpUtility.get_safe_reg_exp(PortugueseDateTime.PureNumBetweenAnd),
        ]
        self._preposition_regex = RegExpUtility.get_safe_reg_exp(PortugueseDateTime.PrepositionRegex)
        self._till_regex = RegExpUtility.get_safe_reg_exp(PortugueseDateTime.TillRegex)
        self._specific_time_of_day_regex = RegExpUtility.get_safe_reg_exp(PortugueseDateTime.SpecificTimeOfDayRegex)
        self._time_of_day_regex = RegExpUtility.get_safe_reg_exp(PortugueseDateTime.TimeOfDayRegex)
        self._period_time_of_day_with_date_regex = RegExpUtility.get_safe_reg_exp(
            PortugueseDateTime.PeriodTimeOfDayWithDateRegex
        )
        self._followed_unit = RegExpUtility.get_safe_reg_exp(PortugueseDateTime.TimeFollowedUnit)
        self._number_combined_with_unit = RegExpUtility.get_safe_reg_exp(PortugueseDateTime.TimeNumberCombinedWithUnit)
        self._time_unit_regex = RegExpUtility.get_safe_reg_exp(PortugueseDateTime.TimeUnitRegex)
        self._past_prefix_regex = RegExpUtility.get_safe_reg_exp(PortugueseDateTime.PreviousPrefixRegex)
        self._next_prefix_regex = RegExpUtility.get_safe_reg_exp(PortugueseDateTime.NextPrefixRegex)
        self._relative_time_unit_regex = RegExpUtility.get_safe_reg_exp(PortugueseDateTime.RelativeTimeUnitRegex)
        self._rest_of_date_time_regex = RegExpUtility.get_safe_reg_exp(PortugueseDateTime.RestOfDateTimeRegex)
        self._general_ending_regex = RegExpUtility.get_safe_reg_exp(PortugueseDateTime.GeneralEndingRegex)
        self._middle_pause_regex = RegExpUtility.get_safe_reg_exp(PortugueseDateTime.MiddlePauseRegex)
        self.range_connector_regex = RegExpUtility.get_safe_reg_exp(PortugueseDateTime.RangeConnectorRegex)
        self._token_before_date = PortugueseDateTime.TokenBeforeDate
        self._within_next_prefix_regex = RegExpUtility.get_safe_reg_exp(PortugueseDateTime.WithinNextPrefixRegex)
        self._future_suffix_regex = RegExpUtility.get_safe_reg_exp(PortugueseDateTime.FutureSuffixRegex)
        self._date_unit_regex = RegExpUtility.get_safe_reg_exp(PortugueseDateTime.DateUnitRegex)
        self._am_desc_regex = RegExpUtility.get_safe_reg_exp(PortugueseDateTime.AmDescRegex)
        self._pm_desc_regex = RegExpUtility.get_safe_reg_exp(PortugueseDateTime.PmDescRegex)
        self._prefix_day_regex = RegExpUtility.get_safe_reg_exp(PortugueseDateTime.PrefixDayRegex)
        self._before_regex = RegExpUtility.get_safe_reg_exp(PortugueseDateTime.BeforeRegex)
        self._after_regex = RegExpUtility.get_safe_reg_exp(PortugueseDateTime.AfterRegex)
        self._suffix_regex = RegExpUtility.get_safe_reg_exp(PortugueseDateTime.SuffixRegex)
        self._options = DateTimeOptions.NONE
        self._check_both_before_after = PortugueseDateTime.CheckBothBeforeAfter

    def get_from_token_index(self, source: str) -> MatchedIndex:
        if source.endswith('from'):
            return MatchedIndex(matched=True, index=source.rfind('from'))

        return MatchedIndex(matched=False, index=-1)

    def get_between_token_index(self, source: str) -> MatchedIndex:
        if source.endswith('between'):
            return MatchedIndex(matched=True, index=source.rfind('between'))

        return MatchedIndex(matched=False, index=-1)

    def has_connector_token(self, source: str) -> bool:
        return regex.fullmatch(self.range_connector_regex, source)
