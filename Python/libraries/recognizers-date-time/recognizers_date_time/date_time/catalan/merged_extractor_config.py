#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from typing import List, Pattern

from recognizers_text.extractor import Extractor
from recognizers_text.utilities import RegExpUtility
from recognizers_number import CatalanIntegerExtractor
from ...resources.catalan_date_time import CatalanDateTime
from ..extractors import DateTimeExtractor
from ..base_merged import MergedExtractorConfiguration
from ..base_date import BaseDateExtractor
from ..base_time import BaseTimeExtractor
from ..base_duration import BaseDurationExtractor
from ..base_dateperiod import BaseDatePeriodExtractor
from ..base_timeperiod import BaseTimePeriodExtractor
from ..base_datetime import BaseDateTimeExtractor
from ..base_datetimeperiod import BaseDateTimePeriodExtractor
from ..base_set import BaseSetExtractor
from ..base_holiday import BaseHolidayExtractor
from .date_extractor_config import CatalanDateExtractorConfiguration
from .time_extractor_config import CatalanTimeExtractorConfiguration
from .duration_extractor_config import CatalanDurationExtractorConfiguration
from .dateperiod_extractor_config import CatalanDatePeriodExtractorConfiguration
from .timeperiod_extractor_config import CatalanTimePeriodExtractorConfiguration
from .datetime_extractor_config import CatalanDateTimeExtractorConfiguration
from .datetimeperiod_extractor_config import CatalanDateTimePeriodExtractorConfiguration
from .set_extractor_config import CatalanSetExtractorConfiguration
from .holiday_extractor_config import CatalanHolidayExtractorConfiguration
from ...resources.base_date_time import BaseDateTime
from ..base_timezone import BaseTimeZoneExtractor
from .timezone_extractor_config import CatalanTimeZoneExtractorConfiguration


class CatalanMergedExtractorConfiguration(MergedExtractorConfiguration):
    @property
    def check_both_before_after(self):
        return self._check_both_before_after

    @property
    def datetime_alt_extractor(self):
        return self._datetime_alt_extractor

    @property
    def ambiguity_filters_dict(self) -> Pattern:
        return self._ambiguity_filters_dict

    @property
    def unspecified_date_period_regex(self) -> Pattern:
        return self._unspecified_date_period_regex

    @property
    def date_extractor(self) -> DateTimeExtractor:
        return self._date_extractor

    @property
    def time_extractor(self) -> DateTimeExtractor:
        return self._time_extractor

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
    def holiday_extractor(self) -> DateTimeExtractor:
        return self._holiday_extractor

    @property
    def time_zone_extractor(self):
        return self._time_zone_extractor

    @property
    def duration_extractor(self) -> DateTimeExtractor:
        return self._duration_extractor

    @property
    def set_extractor(self) -> DateTimeExtractor:
        return self._set_extractor

    @property
    def integer_extractor(self) -> Extractor:
        return self._integer_extractor

    @property
    def after_regex(self) -> Pattern:
        return self._after_regex

    @property
    def before_regex(self) -> Pattern:
        return self._before_regex

    @property
    def since_regex(self) -> Pattern:
        return self._since_regex

    @property
    def around_regex(self) -> Pattern:
        return self._around_regex

    @property
    def equal_regex(self) -> Pattern:
        return self._equal_regex

    @property
    def suffix_after_regex(self) -> Pattern:
        return self._suffix_after_regex

    @property
    def from_to_regex(self) -> Pattern:
        return self._from_to_regex

    @property
    def single_ambiguous_month_regex(self) -> Pattern:
        return self._single_ambiguous_month_regex

    @property
    def preposition_suffix_regex(self) -> Pattern:
        return self._preposition_suffix_regex

    @property
    def ambiguous_range_modifier_prefix(self) -> Pattern:
        return self._ambiguous_range_modifier_prefix

    @property
    def potential_ambiguous_range_regex(self) -> Pattern:
        return self._from_to_regex

    @property
    def number_ending_pattern(self) -> Pattern:
        return self._number_ending_pattern

    @property
    def superfluous_word_matcher(self) -> Pattern:
        return self._superfluous_word_matcher

    @property
    def fail_fast_regex(self) -> Pattern:
        return self._fail_fast_regex

    @property
    def term_filter_regexes(self) -> List[Pattern]:
        return self._term_filter_regexes

    def __init__(self, dmyDateFormat=False):
        self._integer_extractor = CatalanIntegerExtractor()
        self._date_extractor = BaseDateExtractor(
            CatalanDateExtractorConfiguration(dmyDateFormat))
        self._time_extractor = BaseTimeExtractor(
            CatalanTimeExtractorConfiguration())
        self._duration_extractor = BaseDurationExtractor(
            CatalanDurationExtractorConfiguration())
        self._date_period_extractor = BaseDatePeriodExtractor(
            CatalanDatePeriodExtractorConfiguration(dmyDateFormat))
        self._time_period_extractor = BaseTimePeriodExtractor(
            CatalanTimePeriodExtractorConfiguration())
        self._date_time_extractor = BaseDateTimeExtractor(
            CatalanDateTimeExtractorConfiguration(dmyDateFormat))
        self._date_time_period_extractor = BaseDateTimePeriodExtractor(
            CatalanDateTimePeriodExtractorConfiguration(dmyDateFormat))
        self._set_extractor = BaseSetExtractor(
            CatalanSetExtractorConfiguration(dmyDateFormat))
        self._holiday_extractor = BaseHolidayExtractor(
            CatalanHolidayExtractorConfiguration())
        self._after_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.AfterRegex)
        self._before_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.BeforeRegex)
        self._since_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.SinceRegex)
        self._from_to_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.FromToRegex)
        self._single_ambiguous_month_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.SingleAmbiguousMonthRegex)
        self._preposition_suffix_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.PrepositionSuffixRegex)
        self._ambiguous_range_modifier_prefix = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.AmbiguousRangeModifierPrefix)
        self._number_ending_pattern = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.NumberEndingPattern)
        self._term_filter_regexes = [
            RegExpUtility.get_safe_reg_exp(CatalanDateTime.OneOnOneRegex),
            RegExpUtility.get_safe_reg_exp(CatalanDateTime.SingleAmbiguousTermsRegex)
        ]
        self._unspecified_date_period_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.UnspecificDatePeriodRegex
        )
        self._ambiguity_filters_dict = CatalanDateTime.AmbiguityFiltersDict
        self._around_regex = CatalanDateTime.AroundRegex
        self._equal_regex = BaseDateTime.EqualRegex
        self._suffix_after_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.SuffixAfterRegex
        )
        self._superfluous_word_matcher = CatalanDateTime.SuperfluousWordList
        self._fail_fast_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.FailFastRegex
        )
        self._check_both_before_after = CatalanDateTime.CheckBothBeforeAfter
        self._time_zone_extractor = BaseTimeZoneExtractor(
            CatalanTimeZoneExtractorConfiguration())
        # TODO When the implementation for these properties is added, change the None values to their respective Regexps
        self._datetime_alt_extractor = None
