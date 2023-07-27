from typing import Dict, Pattern

from recognizers_number import BaseNumberExtractor, BaseNumberParser
from recognizers_number.number.catalan.parsers import CatalanNumberParserConfiguration
from recognizers_number.number.catalan.extractors import CatalanCardinalExtractor, CatalanIntegerExtractor, CatalanOrdinalExtractor

from ...resources.catalan_date_time import CatalanDateTime
from ..extractors import DateTimeExtractor
from ..parsers import DateTimeParser
from ..base_configs import BaseDateParserConfiguration, DateTimeUtilityConfiguration
from ..base_date import BaseDateExtractor, BaseDateParser
from ..base_time import BaseTimeExtractor, BaseTimeParser
from ..base_duration import BaseDurationExtractor, BaseDurationParser
from ..base_dateperiod import BaseDatePeriodExtractor, BaseDatePeriodParser
from ..base_timeperiod import BaseTimePeriodExtractor, BaseTimePeriodParser
from ..base_datetime import BaseDateTimeExtractor, BaseDateTimeParser
from ..base_datetimeperiod import BaseDateTimePeriodExtractor, BaseDateTimePeriodParser
from ..base_timezone import BaseTimeZoneParser
from .base_configs import CatalanDateTimeUtilityConfiguration
from .date_extractor_config import CatalanDateExtractorConfiguration
from .date_parser_config import CatalanDateParserConfiguration
from .time_extractor_config import CatalanTimeExtractorConfiguration
from .time_parser_config import CatalanTimeParserConfiguration
from .duration_extractor_config import CatalanDurationExtractorConfiguration
from .duration_parser_config import CatalanDurationParserConfiguration
from .dateperiod_extractor_config import CatalanDatePeriodExtractorConfiguration
from .dateperiod_parser_config import CatalanDatePeriodParserConfiguration
from .timeperiod_extractor_config import CatalanTimePeriodExtractorConfiguration
from .timeperiod_parser_config import CatalanTimePeriodParserConfiguration
from .datetime_extractor_config import CatalanDateTimeExtractorConfiguration
from .datetime_parser_config import CatalanDateTimeParserConfiguration
from .datetimeperiod_extractor_config import CatalanDateTimePeriodExtractorConfiguration
from .datetimeperiod_parser_config import CatalanDateTimePeriodParserConfiguration


class CatalanCommonDateTimeParserConfiguration(BaseDateParserConfiguration):
    @property
    def time_zone_parser(self) -> DateTimeParser:
        return self._time_zone_parser

    @property
    def check_both_before_after(self) -> Pattern:
        return self._check_both_before_after

    @property
    def cardinal_extractor(self) -> BaseNumberExtractor:
        return self._cardinal_extractor

    @property
    def integer_extractor(self) -> BaseNumberExtractor:
        return self._integer_extractor

    @property
    def ordinal_extractor(self) -> BaseNumberExtractor:
        return self._ordinal_extractor

    @property
    def number_parser(self) -> BaseNumberParser:
        return self._number_parser

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
    def duration_extractor(self) -> DateTimeExtractor:
        return self._duration_extractor

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
    def date_parser(self) -> DateTimeParser:
        return self._date_parser

    @property
    def time_parser(self) -> DateTimeParser:
        return self._time_parser

    @property
    def date_time_parser(self) -> DateTimeParser:
        return self._date_time_parser

    @property
    def duration_parser(self) -> DateTimeParser:
        return self._duration_parser

    @property
    def date_period_parser(self) -> DateTimeParser:
        return self._date_period_parser

    @property
    def time_period_parser(self) -> DateTimeParser:
        return self._time_period_parser

    @property
    def date_time_period_parser(self) -> DateTimeParser:
        return self._date_time_period_parser

    @property
    def month_of_year(self) -> Dict[str, int]:
        return self._month_of_year

    @property
    def numbers(self) -> Dict[str, int]:
        return self._numbers

    @property
    def unit_value_map(self) -> Dict[str, int]:
        return self._unit_value_map

    @property
    def season_map(self) -> Dict[str, str]:
        return self._season_map

    @property
    def unit_map(self) -> Dict[str, str]:
        return self._unit_map

    @property
    def cardinal_map(self) -> Dict[str, int]:
        return self._cardinal_map

    @property
    def day_of_month(self) -> Dict[str, int]:
        return self._day_of_month

    @property
    def day_of_week(self) -> Dict[str, int]:
        return self._day_of_week

    @property
    def double_numbers(self) -> Dict[str, int]:
        return self._double_numbers

    @property
    def utility_configuration(self) -> DateTimeUtilityConfiguration:
        return None

    def __init__(self):
        BaseDateParserConfiguration.__init__(self)

        self._utility_configuration = CatalanDateTimeUtilityConfiguration()
        self._time_zone_parser = BaseTimeZoneParser()
        self._unit_map = None
        self._unit_value_map = None
        self._season_map = None
        self._cardinal_map = None
        self._day_of_week = CatalanDateTime.DayOfWeek
        self._month_of_year = CatalanDateTime.MonthOfYear
        self._numbers = None
        self._double_numbers = None
        self._check_both_before_after = CatalanDateTime.CheckBothBeforeAfter
        self._cardinal_extractor = CatalanCardinalExtractor()
        self._integer_extractor = CatalanIntegerExtractor()
        self._ordinal_extractor = CatalanOrdinalExtractor()

        self._number_parser = BaseNumberParser(
            CatalanNumberParserConfiguration())
        self._date_extractor = BaseDateExtractor(
            CatalanDateExtractorConfiguration())
        self._time_extractor = None
        self._duration_extractor = None
        self._date_period_extractor = None
        self._time_period_extractor = None
        self._date_time_extractor = None
        self._date_time_period_extractor = None
        self._duration_parser = None
        self._date_parser = BaseDateParser(
            CatalanDateParserConfiguration(self))
        self._time_parser = None
        self._date_period_parser = None
        self._time_period_parser = None
        self._date_time_parser = None
        self._date_time_period_parser = None
