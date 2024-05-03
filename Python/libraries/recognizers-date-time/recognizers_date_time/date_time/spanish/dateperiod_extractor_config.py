#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from typing import List, Pattern

from recognizers_text import Extractor
from recognizers_text.utilities import RegExpUtility
from recognizers_number.number import BaseNumberParser, BaseNumberExtractor
from recognizers_number.number.spanish.extractors import SpanishIntegerExtractor,\
    SpanishCardinalExtractor, SpanishOrdinalExtractor
from recognizers_number.number.spanish.parsers import SpanishNumberParserConfiguration
from ...resources.base_date_time import BaseDateTime
from ...resources.spanish_date_time import SpanishDateTime
from ..extractors import DateTimeExtractor
from ..base_duration import BaseDurationExtractor
from ..base_date import BaseDateExtractor
from ..base_dateperiod import DatePeriodExtractorConfiguration, MatchedIndex
from .duration_extractor_config import SpanishDurationExtractorConfiguration
from .date_extractor_config import SpanishDateExtractorConfiguration


class SpanishDatePeriodExtractorConfiguration(DatePeriodExtractorConfiguration):

    def __init__(self):
        super().__init__(SpanishDateTime())
        self.ordinal_extractor = SpanishOrdinalExtractor()
        self.cardinal_extractor = SpanishCardinalExtractor()
        self.cardinal_extractor = SpanishCardinalExtractor()
        self.date_point_extractor = BaseDateExtractor(SpanishDateExtractorConfiguration())
        self.number_parser = BaseNumberParser(SpanishNumberParserConfiguration())
        self.duration_extractor = BaseDurationExtractor(SpanishDurationExtractorConfiguration())
        self.integer_extractor = SpanishIntegerExtractor()
        self.between_regex = RegExpUtility.get_safe_reg_exp(SpanishDateTime.BetweenRegex)
        self.year_period_regex = RegExpUtility.get_safe_reg_exp(SpanishDateTime.YearPeriodRegex)
        self.past_regex = RegExpUtility.get_safe_reg_exp(SpanishDateTime.PastRegex)
        self.simple_cases_regexes = [
            self.year_period_regex,
            RegExpUtility.get_safe_reg_exp(SpanishDateTime.SimpleCasesRegex),
            RegExpUtility.get_safe_reg_exp(SpanishDateTime.DayBetweenRegex),
            RegExpUtility.get_safe_reg_exp(SpanishDateTime.OneWordPeriodRegex),
            RegExpUtility.get_safe_reg_exp(SpanishDateTime.MonthWithYearRegex),
            RegExpUtility.get_safe_reg_exp(SpanishDateTime.MonthNumWithYearRegex),
            RegExpUtility.get_safe_reg_exp(SpanishDateTime.YearRegex),
            RegExpUtility.get_safe_reg_exp(SpanishDateTime.WeekOfMonthRegex),
            RegExpUtility.get_safe_reg_exp(SpanishDateTime.WeekOfYearRegex),
            RegExpUtility.get_safe_reg_exp(SpanishDateTime.MonthFrontBetweenRegex),
            RegExpUtility.get_safe_reg_exp(SpanishDateTime.MonthFrontSimpleCasesRegex),
            RegExpUtility.get_safe_reg_exp(SpanishDateTime.QuarterRegex),
            RegExpUtility.get_safe_reg_exp(SpanishDateTime.QuarterRegexYearFront),
            RegExpUtility.get_safe_reg_exp(SpanishDateTime.SeasonRegex),
            RegExpUtility.get_safe_reg_exp(SpanishDateTime.RestOfDateRegex),
            RegExpUtility.get_safe_reg_exp(SpanishDateTime.LaterEarlyPeriodRegex),
            RegExpUtility.get_safe_reg_exp(SpanishDateTime.WeekWithWeekDayRangeRegex),
            RegExpUtility.get_safe_reg_exp(SpanishDateTime.YearPlusNumberRegex),
            RegExpUtility.get_safe_reg_exp(SpanishDateTime.WhichWeekRegex),
            RegExpUtility.get_safe_reg_exp(SpanishDateTime.ReferenceDatePeriodRegex),
        ]

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

    def has_connector_token(self, source: str) -> bool:
        return not self.range_connector_regex.search(source) is None
