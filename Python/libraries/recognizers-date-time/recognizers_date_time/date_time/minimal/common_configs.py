from typing import Dict, Pattern
from recognizers_number.number.minimal import MinimalNumberExtractor, MinimalNumberParser
from recognizers_number.number.minimal.parsers import MinimalNumberParserConfiguration
from recognizers_number.number.minimal.extractors import MinimalCardinalExtractor, MinimalIntegerExtractor

from recognizers_date_time.resources.minimal_date_time import MinimalDateTime
from recognizers_date_time.date_time.extractors import DateTimeExtractor
from recognizers_date_time.date_time.parsers import DateTimeParser
from recognizers_date_time.date_time.base_configs import DateTimeUtilityConfiguration
from recognizers_date_time.date_time.base_minimal_configs import BaseMinimalDateParserConfiguration
from recognizers_date_time.date_time.base_timezone import BaseTimeZoneParser
from recognizers_date_time.date_time.minimal.base_configs import MinimalDateTimeUtilityConfiguration
from recognizers_date_time.date_time.minimal.date_extractor_config import MinimalDateExtractorConfiguration
from recognizers_date_time.date_time.minimal.date_parser_config import MinimalDateParserConfiguration
from recognizers_date_time.date_time.minimal.time_extractor_config import MinimalTimeExtractorConfiguration
from recognizers_date_time.date_time.minimal.time_parser_config import MinimalTimeParserConfiguration
from recognizers_date_time.date_time.minimal.base_minimal_date import BaseMinimalDateParser
from recognizers_date_time.date_time.minimal.base_minimal_time import BaseMinimalTimeExtractor, BaseMinimalTimeParser


class MinimalCommonDateTimeParserConfiguration:
    @property
    def month_of_year(self) -> Dict[str, int]:
        return self._month_of_year

    @property
    def time_zone_parser(self) -> DateTimeParser:
        return self._time_zone_parser

    @property
    def check_both_before_after(self) -> Pattern:
        return self._check_both_before_after

    @property
    def cardinal_extractor(self) -> MinimalNumberExtractor:
        return self._cardinal_extractor

    @property
    def integer_extractor(self) -> MinimalNumberExtractor:
        return self._integer_extractor

    @property
    def number_parser(self) -> MinimalNumberParser:
        return self._number_parser

    @property
    def date_extractor(self) -> DateTimeExtractor:
        return self._date_extractor

    @property
    def time_extractor(self) -> DateTimeExtractor:
        return self._time_extractor

    @property
    def date_parser(self) -> DateTimeParser:
        return self._date_parser

    @property
    def time_parser(self) -> DateTimeParser:
        return self._time_parser

    @property
    def day_of_month(self) -> Dict[str, int]:
        return self._day_of_month

    @property
    def utility_configuration(self) -> DateTimeUtilityConfiguration:
        return self._utility_configuration

    def __init__(self, dmyDateFormat: bool = True):
        BaseMinimalDateParserConfiguration.__init__(self)

        self._month_of_year = MinimalDateTime.MonthOfYear
        self._utility_configuration = MinimalDateTimeUtilityConfiguration()
        self._time_zone_parser = BaseTimeZoneParser()
        self._check_both_before_after = MinimalDateTime.CheckBothBeforeAfter
        self._cardinal_extractor = MinimalCardinalExtractor()
        self._integer_extractor = MinimalIntegerExtractor()
        self._number_parser = MinimalNumberParser(
            MinimalNumberParserConfiguration())
        self._date_extractor = BaseMinimalDateParser(
            MinimalDateExtractorConfiguration(dmyDateFormat))
        self._time_extractor = BaseMinimalTimeExtractor(MinimalTimeExtractorConfiguration())
        self._date_parser = BaseMinimalDateParser(
            MinimalDateParserConfiguration(self))
        self._time_parser = BaseMinimalTimeParser(MinimalTimeParserConfiguration(self))
