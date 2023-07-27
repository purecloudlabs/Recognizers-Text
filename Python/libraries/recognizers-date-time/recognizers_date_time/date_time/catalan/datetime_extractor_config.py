from typing import Pattern
import regex

from recognizers_text.utilities import RegExpUtility
from ...resources.catalan_date_time import CatalanDateTime
from ..extractors import DateTimeExtractor
from ..base_date import BaseDateExtractor
from ..base_time import BaseTimeExtractor
from ..base_duration import BaseDurationExtractor
from ..base_datetime import DateTimeExtractorConfiguration
from .base_configs import CatalanDateTimeUtilityConfiguration
from .date_extractor_config import CatalanDateExtractorConfiguration
from .time_extractor_config import CatalanTimeExtractorConfiguration
from .duration_extractor_config import CatalanDurationExtractorConfiguration
from ..utilities import DateTimeOptions


class CatalanDateTimeExtractorConfiguration(DateTimeExtractorConfiguration):
    @property
    def dmy_date_format(self) -> bool:
        return self._dmy_date_format

    @property
    def date_point_extractor(self) -> DateTimeExtractor:
        return self._date_point_extractor

    @property
    def time_point_extractor(self) -> DateTimeExtractor:
        return self._time_point_extractor

    @property
    def duration_extractor(self) -> DateTimeExtractor:
        return self._duration_extractor

    @property
    def suffix_regex(self) -> Pattern:
        return self._suffix_regex

    @property
    def now_regex(self) -> Pattern:
        return self._now_regex

    @property
    def time_of_today_after_regex(self) -> Pattern:
        return self._time_of_today_after_regex

    @property
    def time_of_day_regex(self) -> Pattern:
        return self._time_of_day_regex

    @property
    def specific_time_of_day_regex(self) -> Pattern:
        return self._specific_time_of_day_regex

    @property
    def simple_time_of_today_after_regex(self) -> Pattern:
        return self._simple_time_of_today_after_regex

    @property
    def night_regex(self) -> Pattern:
        return self._night_regex

    @property
    def time_of_today_before_regex(self) -> Pattern:
        return self._time_of_today_before_regex

    @property
    def simple_time_of_today_before_regex(self) -> Pattern:
        return self._simple_time_of_today_before_regex

    @property
    def specific_end_of_regex(self) -> Pattern:
        return self._specific_end_of_regex

    @property
    def unspecific_end_of_regex(self) -> Pattern:
        return self._unspecific_end_of_regex

    @property
    def unit_regex(self) -> Pattern:
        return self._unit_regex

    @property
    def utility_configuration(self) -> CatalanDateTimeUtilityConfiguration:
        return self._utility_configuration

    @property
    def number_as_time_regex(self) -> Pattern:
        return self._number_as_time_regex

    @property
    def date_number_connector_regex(self) -> Pattern:
        return self._date_number_connector_regex

    @property
    def suffix_after_regex(self) -> Pattern:
        return self._suffix_after_regex

    @property
    def year_suffix(self) -> Pattern:
        return self._year_suffix

    @property
    def year_regex(self) -> Pattern:
        return self._year_regex

    def __init__(self):
        super().__init__()
        self.preposition_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.PrepositionRegex)
        self._now_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.NowRegex)
        self._suffix_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.SuffixRegex)

        self._time_of_day_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.TimeOfDayRegex)
        self._specific_time_of_day_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.SpecificTimeOfDayRegex)
        self._time_of_today_after_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.TimeOfTodayAfterRegex)
        self._time_of_today_before_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.TimeOfTodayBeforeRegex)
        self._simple_time_of_today_after_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.SimpleTimeOfTodayAfterRegex)
        self._simple_time_of_today_before_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.SimpleTimeOfTodayBeforeRegex)
        self._specific_end_of_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.SpecificEndOfRegex)
        self._unspecific_end_of_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.UnspecificEndOfRegex)
        self._unit_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.TimeUnitRegex)
        self.connector_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.ConnectorRegex)
        self._night_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.TimeOfDayRegex)
        self._number_as_time_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.NumberAsTimeRegex)
        self._date_number_connector_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.DateNumberConnectorRegex
        )
        self._suffix_after_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.SuffixAfterRegex
        )
        self._year_suffix = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.YearSuffix
        )
        self._year_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.YearRegex
        )

        self._date_point_extractor = BaseDateExtractor(
            CatalanDateExtractorConfiguration())
        self._time_point_extractor = BaseTimeExtractor(
            CatalanTimeExtractorConfiguration())
        self._duration_extractor = BaseDurationExtractor(
            CatalanDurationExtractorConfiguration())
        self._utility_configuration = CatalanDateTimeUtilityConfiguration()
        self._options = DateTimeOptions.NONE

    def is_connector_token(self, source: str) -> bool:
        return source.strip() == '' or regex.search(self.connector_regex, source) is not None or regex.search(
            self.preposition_regex, source) is not None
