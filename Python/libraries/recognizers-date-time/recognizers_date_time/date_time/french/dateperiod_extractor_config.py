#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from typing import List, Pattern

from recognizers_text.utilities import RegExpUtility
from recognizers_number.number import BaseNumberParser
from recognizers_number.number.french.extractors import FrenchIntegerExtractor, FrenchCardinalExtractor
from recognizers_number.number.french.parsers import FrenchNumberParserConfiguration
from ...resources.base_date_time import BaseDateTime
from ...resources.french_date_time import FrenchDateTime
from ..extractors import DateTimeExtractor
from ..base_duration import BaseDurationExtractor
from ..base_date import BaseDateExtractor
from ..base_dateperiod import DatePeriodExtractorConfiguration, MatchedIndex
from .duration_extractor_config import FrenchDurationExtractorConfiguration
from .date_extractor_config import FrenchDateExtractorConfiguration
from recognizers_text.extractor import Extractor
from recognizers_number import FrenchOrdinalExtractor, BaseNumberExtractor, FrenchCardinalExtractor


class FrenchDatePeriodExtractorConfiguration(DatePeriodExtractorConfiguration):

    def __init__(self):
        super().__init__(FrenchDateTime())
        self.ordinal_extractor = FrenchOrdinalExtractor()
        self.cardinal_extractor = FrenchCardinalExtractor()
        self.cardinal_extractor = FrenchCardinalExtractor()
        self.date_point_extractor = BaseDateExtractor(FrenchDateExtractorConfiguration())
        self.number_parser = BaseNumberParser(FrenchNumberParserConfiguration())
        self.duration_extractor = BaseDurationExtractor(FrenchDurationExtractorConfiguration())
        self.integer_extractor = FrenchIntegerExtractor()
        self.connector_and_regex = RegExpUtility.get_safe_reg_exp(FrenchDateTime.ConnectorAndRegex)
        self.week_day_of_month_regex = RegExpUtility.get_safe_reg_exp(FrenchDateTime.WeekDayOfMonthRegex)
        self.past_regex = RegExpUtility.get_safe_reg_exp(FrenchDateTime.PastSuffixRegex)
        self.simple_cases_regexes = [
             RegExpUtility.get_safe_reg_exp(FrenchDateTime.SimpleCasesRegex),
             RegExpUtility.get_safe_reg_exp(FrenchDateTime.BetweenRegex),
             RegExpUtility.get_safe_reg_exp(FrenchDateTime.OneWordPeriodRegex),
             RegExpUtility.get_safe_reg_exp(FrenchDateTime.MonthWithYear),
             RegExpUtility.get_safe_reg_exp(FrenchDateTime.MonthNumWithYear),
             RegExpUtility.get_safe_reg_exp(FrenchDateTime.YearRegex),
             RegExpUtility.get_safe_reg_exp(FrenchDateTime.YearPeriodRegex),
             RegExpUtility.get_safe_reg_exp(FrenchDateTime.WeekOfYearRegex),
             RegExpUtility.get_safe_reg_exp(FrenchDateTime.WeekDayOfMonthRegex),
             RegExpUtility.get_safe_reg_exp(FrenchDateTime.MonthFrontBetweenRegex),
             RegExpUtility.get_safe_reg_exp(FrenchDateTime.MonthFrontSimpleCasesRegex),
             RegExpUtility.get_safe_reg_exp(FrenchDateTime.QuarterRegex),
             RegExpUtility.get_safe_reg_exp(FrenchDateTime.QuarterRegexYearFront),
             RegExpUtility.get_safe_reg_exp(FrenchDateTime.SeasonRegex),
             RegExpUtility.get_safe_reg_exp(FrenchDateTime.LaterEarlyPeriodRegex),
             RegExpUtility.get_safe_reg_exp(FrenchDateTime.WeekWithWeekDayRangeRegex),
             RegExpUtility.get_safe_reg_exp(FrenchDateTime.YearPlusNumberRegex),
             RegExpUtility.get_safe_reg_exp(FrenchDateTime.DecadeWithCenturyRegex),
             RegExpUtility.get_safe_reg_exp(FrenchDateTime.RelativeDecadeRegex)
        ]

    def get_from_token_index(self, source: str) -> MatchedIndex:
        match = self.from_regex.search(source)
        if match:
            return MatchedIndex(True, match.start())

        return MatchedIndex(False, -1)

    def get_between_token_index(self, source: str) -> MatchedIndex:
        match = self.before_regex.search(source)
        if match:
            return MatchedIndex(True, match.start())

        return MatchedIndex(False, -1)

    def has_connector_token(self, source: str) -> bool:
        return not self.connector_and_regex.search(source) is None
