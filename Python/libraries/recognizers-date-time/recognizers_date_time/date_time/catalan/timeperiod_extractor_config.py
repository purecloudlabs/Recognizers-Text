from typing import List, Pattern

from recognizers_text.utilities import RegExpUtility
from recognizers_text.extractor import Extractor
from recognizers_number.number.catalan.extractors import CatalanIntegerExtractor
from ...resources.catalan_date_time import CatalanDateTime
from ..extractors import DateTimeExtractor
from ..base_timeperiod import TimePeriodExtractorConfiguration, MatchedIndex
from ..base_time import BaseTimeExtractor
from ..base_timezone import BaseTimeZoneExtractor
from .time_extractor_config import CatalanTimeExtractorConfiguration
from .base_configs import CatalanDateTimeUtilityConfiguration
from ..utilities import DateTimeOptions
from .timezone_extractor_config import CatalanTimeZoneExtractorConfiguration


class CatalanTimePeriodExtractorConfiguration(TimePeriodExtractorConfiguration):

    @property
    def check_both_before_after(self) -> bool:
        return self._check_both_before_after

    @property
    def dmy_date_format(self) -> bool:
        return self._dmy_date_format

    @property
    def options(self):
        return self._options

    @property
    def simple_cases_regex(self) -> List[Pattern]:
        return self._simple_cases_regex

    @property
    def till_regex(self) -> Pattern:
        return self._till_regex

    @property
    def time_of_day_regex(self) -> Pattern:
        return self._time_of_day_regex

    @property
    def general_ending_regex(self) -> Pattern:
        return self._general_ending_regex

    @property
    def single_time_extractor(self) -> DateTimeExtractor:
        return self._single_time_extractor

    @property
    def integer_extractor(self) -> Extractor:
        return self._integer_extractor

    @property
    def token_before_date(self) -> str:
        return self._token_before_date

    @property
    def pure_number_regex(self) -> List[Pattern]:
        return self._pure_number_regex

    @property
    def time_zone_extractor(self) -> DateTimeExtractor:
        return self._time_zone_extractor

    def __init__(self):
        super().__init__()
        self._single_time_extractor = BaseTimeExtractor(
            CatalanTimeExtractorConfiguration())
        self._integer_extractor = CatalanIntegerExtractor()
        self.utility_configuration = CatalanDateTimeUtilityConfiguration()

        self._simple_cases_regex: List[Pattern] = [
            RegExpUtility.get_safe_reg_exp(CatalanDateTime.PureNumFromTo),
            RegExpUtility.get_safe_reg_exp(CatalanDateTime.PureNumBetweenAnd),
            RegExpUtility.get_safe_reg_exp(CatalanDateTime.SpecificTimeFromTo),
            RegExpUtility.get_safe_reg_exp(CatalanDateTime.SpecificTimeBetweenAnd)
        ]

        self._till_regex: Pattern = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.TillRegex)
        self._time_of_day_regex: Pattern = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.TimeOfDayRegex)
        self._general_ending_regex: Pattern = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.GeneralEndingRegex)

        self.from_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.FromRegex)
        self.range_connector_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.RangeConnectorRegex)
        self.between_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.BetweenRegex)
        self._token_before_date = CatalanDateTime.TokenBeforeDate
        self._pure_number_regex = [CatalanDateTime.PureNumFromTo, CatalanDateTime.PureNumFromTo]
        self._options = DateTimeOptions.NONE
        self._time_zone_extractor = BaseTimeZoneExtractor(
            CatalanTimeZoneExtractorConfiguration())
        self._check_both_before_after = CatalanDateTime.CheckBothBeforeAfter

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

    def is_connector_token(self, source: str) -> MatchedIndex:
        return self.range_connector_regex.search(source)
