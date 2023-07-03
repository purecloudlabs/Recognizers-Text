#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from typing import Dict

from recognizers_number import BaseNumberExtractor, JapaneseCardinalExtractor, JapaneseIntegerExtractor, \
    JapaneseOrdinalExtractor, BaseNumberParser, JapaneseNumberParserConfiguration
from ..CJK.base_date import BaseCJKDateParser, BaseCJKDateExtractor, CJKDateParserConfiguration
from ..CJK.base_dateperiod import BaseCJKDatePeriodExtractor

from ...resources import JapaneseDateTime, BaseDateTime
from ..extractors import DateTimeExtractor
from ..parsers import DateTimeParser
from ..base_timezone import BaseTimeZoneParser
from .date_extractor_config import JapaneseDateExtractorConfiguration
from .dateperiod_extractor_config import JapaneseDatePeriodExtractorConfiguration
from .date_parser_config import JapaneseDateParserConfiguration


class JapaneseCommonDateTimeParserConfiguration(CJKDateParserConfiguration):

    @property
    def time_zone_parser(self) -> DateTimeParser:
        return self._time_zone_parser

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
    def date_period_extractor(self) -> DateTimeExtractor:
        return self._date_period_extractor

    @property
    def date_parser(self) -> DateTimeParser:
        return self._date_parser

    @property
    def month_of_year(self) -> Dict[str, int]:
        return self._month_of_year

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
    def day_of_week(self) -> Dict[str, int]:
        return self._day_of_week

    def __init__(self):
        super().__init__()
        self._time_zone_parser = BaseTimeZoneParser()
        self._unit_map = JapaneseDateTime.ParserConfigurationUnitMap
        self._unit_value_map = JapaneseDateTime.ParserConfigurationUnitValueMap
        self._season_map = JapaneseDateTime.ParserConfigurationSeasonMap
        self._cardinal_map = JapaneseDateTime.ParserConfigurationCardinalMap
        self._day_of_week = JapaneseDateTime.ParserConfigurationDayOfWeek
        self._month_of_year = JapaneseDateTime.ParserConfigurationMonthOfYear

        self._cardinal_extractor = JapaneseCardinalExtractor()
        self._integer_extractor = JapaneseIntegerExtractor()
        self._ordinal_extractor = JapaneseOrdinalExtractor()

        self._day_of_month = {
            **BaseDateTime.DayOfMonthDictionary, **JapaneseDateTime.ParserConfigurationDayOfMonth}
        self._number_parser = BaseNumberParser(
            JapaneseNumberParserConfiguration())

        self._date_extractor = BaseCJKDateExtractor(
            JapaneseDateExtractorConfiguration())
        self._date_period_extractor = BaseCJKDatePeriodExtractor(
            JapaneseDatePeriodExtractorConfiguration())
        self._date_parser = BaseCJKDateParser(JapaneseDateParserConfiguration(self))
