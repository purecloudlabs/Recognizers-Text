#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from typing import Pattern

from recognizers_text.utilities import RegExpUtility
from ...resources.catalan_date_time import CatalanDateTime
from ..extractors import DateTimeExtractor
from ..base_set import SetExtractorConfiguration
from ..base_date import BaseDateExtractor
from ..base_time import BaseTimeExtractor
from ..base_duration import BaseDurationExtractor
from ..base_dateperiod import BaseDatePeriodExtractor
from ..base_timeperiod import BaseTimePeriodExtractor
from ..base_datetime import BaseDateTimeExtractor
from ..base_datetimeperiod import BaseDateTimePeriodExtractor
from .date_extractor_config import CatalanDateExtractorConfiguration
from .time_extractor_config import CatalanTimeExtractorConfiguration
from .duration_extractor_config import CatalanDurationExtractorConfiguration
from .dateperiod_extractor_config import CatalanDatePeriodExtractorConfiguration
from .timeperiod_extractor_config import CatalanTimePeriodExtractorConfiguration
from .datetime_extractor_config import CatalanDateTimeExtractorConfiguration
from .datetimeperiod_extractor_config import CatalanDateTimePeriodExtractorConfiguration
from recognizers_number import BaseNumberExtractor
from recognizers_number.number.catalan.extractors import CatalanCardinalExtractor


class CatalanSetExtractorConfiguration(SetExtractorConfiguration):
    @property
    def last_regex(self) -> Pattern:
        return self._last_regex

    @property
    def each_prefix_regex(self) -> Pattern:
        return self._each_prefix_regex

    @property
    def periodic_regex(self) -> Pattern:
        return self._periodic_regex

    @property
    def each_unit_regex(self) -> Pattern:
        return self._each_unit_regex

    @property
    def each_day_regex(self) -> Pattern:
        return self._each_day_regex

    @property
    def before_each_day_regex(self) -> Pattern:
        return self._before_each_day_regex

    @property
    def set_week_day_regex(self) -> Pattern:
        return self._set_week_day_regex

    @property
    def set_each_regex(self) -> Pattern:
        return self._set_each_regex

    @property
    def duration_extractor(self) -> DateTimeExtractor:
        return self._duration_extractor

    @property
    def time_extractor(self) -> DateTimeExtractor:
        return self._time_extractor

    @property
    def date_extractor(self) -> DateTimeExtractor:
        return self._date_extractor

    @property
    def date_time_extractor(self) -> DateTimeExtractor:
        return self._date_time_extractor

    @property
    def date_period_extractor(self) -> DateTimeExtractor:
        return self._date_period_extractor

    @property
    def time_period_extractor(self) -> DateTimeExtractor:
        return self._time_period_extractor

    @property
    def date_time_period_extractor(self) -> DateTimeExtractor:
        return self._date_time_period_extractor

    @property
    def cardinal_extractor(self) -> BaseNumberExtractor:
        return self._cardinal_extractor

    def __init__(self):
        self._last_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.LastDateRegex)
        self._periodic_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.PeriodicRegex)
        self._each_unit_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.EachUnitRegex)
        self._each_prefix_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.EachPrefixRegex)
        self._each_day_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.EachDayRegex)
        self._before_each_day_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.BeforeEachDayRegex)
        self._set_each_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.SetEachRegex)
        self._set_week_day_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.SetWeekDayRegex)

        self._duration_extractor = BaseDurationExtractor(
            CatalanDurationExtractorConfiguration())
        self._time_extractor = BaseTimeExtractor(
            CatalanTimeExtractorConfiguration())
        self._date_extractor = BaseDateExtractor(
            CatalanDateExtractorConfiguration())
        self._date_time_extractor = BaseDateTimeExtractor(
            CatalanDateTimeExtractorConfiguration())
        self._date_period_extractor = BaseDatePeriodExtractor(
            CatalanDatePeriodExtractorConfiguration())
        self._time_period_extractor = BaseTimePeriodExtractor(
            CatalanTimePeriodExtractorConfiguration())
        self._date_time_period_extractor = BaseDateTimePeriodExtractor(
            CatalanDateTimePeriodExtractorConfiguration())
        self._cardinal_extractor = CatalanCardinalExtractor()
