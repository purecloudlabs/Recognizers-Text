#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.


from recognizers_number import ItalianCardinalExtractor, ItalianOrdinalExtractor
from recognizers_number.number import BaseNumberParser
from recognizers_number.number.italian.extractors import ItalianCardinalExtractor, ItalianIntegerExtractor
from recognizers_number.number.italian.parsers import ItalianNumberParserConfiguration
from recognizers_text.utilities import RegExpUtility

from ...resources.italian_date_time import ItalianDateTime
from ..base_date import BaseDateExtractor
from ..base_dateperiod import DatePeriodExtractorConfiguration, MatchedIndex
from ..base_duration import BaseDurationExtractor
from .date_extractor_config import ItalianDateExtractorConfiguration
from .duration_extractor_config import ItalianDurationExtractorConfiguration


class ItalianDatePeriodExtractorConfiguration(DatePeriodExtractorConfiguration):

    def __init__(self):
        super().__init__(ItalianDateTime())
        self.ordinal_extractor = ItalianOrdinalExtractor()
        self.cardinal_extractor = ItalianCardinalExtractor()
        self.cardinal_extractor = ItalianCardinalExtractor()
        self.date_point_extractor = BaseDateExtractor(ItalianDateExtractorConfiguration())
        self.number_parser = BaseNumberParser(ItalianNumberParserConfiguration())
        self.duration_extractor = BaseDurationExtractor(ItalianDurationExtractorConfiguration())
        self.integer_extractor = ItalianIntegerExtractor()
        self.from_regex = RegExpUtility.get_safe_reg_exp(ItalianDateTime.FromRegex)
        self.connector_and_regex = RegExpUtility.get_safe_reg_exp(ItalianDateTime.ConnectorAndRegex)
        self.simple_cases_regexes = [
            RegExpUtility.get_safe_reg_exp(ItalianDateTime.SimpleCasesRegex),
            RegExpUtility.get_safe_reg_exp(ItalianDateTime.BetweenRegex),
            RegExpUtility.get_safe_reg_exp(ItalianDateTime.OneWordPeriodRegex),
            RegExpUtility.get_safe_reg_exp(ItalianDateTime.MonthWithYear),
            RegExpUtility.get_safe_reg_exp(ItalianDateTime.MonthNumWithYear),
            RegExpUtility.get_safe_reg_exp(ItalianDateTime.YearRegex),
            RegExpUtility.get_safe_reg_exp(ItalianDateTime.YearPeriodRegex),
            RegExpUtility.get_safe_reg_exp(ItalianDateTime.WeekOfYearRegex),
            RegExpUtility.get_safe_reg_exp(ItalianDateTime.WeekDayOfMonthRegex),
            RegExpUtility.get_safe_reg_exp(ItalianDateTime.MonthFrontBetweenRegex),
            RegExpUtility.get_safe_reg_exp(ItalianDateTime.MonthFrontSimpleCasesRegex),
            RegExpUtility.get_safe_reg_exp(ItalianDateTime.QuarterRegex),
            RegExpUtility.get_safe_reg_exp(ItalianDateTime.QuarterRegexYearFront),
            RegExpUtility.get_safe_reg_exp(ItalianDateTime.SeasonRegex),
            RegExpUtility.get_safe_reg_exp(ItalianDateTime.LaterEarlyPeriodRegex),
            RegExpUtility.get_safe_reg_exp(ItalianDateTime.WeekWithWeekDayRangeRegex),
            RegExpUtility.get_safe_reg_exp(ItalianDateTime.YearPlusNumberRegex),
            RegExpUtility.get_safe_reg_exp(ItalianDateTime.DecadeWithCenturyRegex),
            RegExpUtility.get_safe_reg_exp(ItalianDateTime.RelativeDecadeRegex),
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
        return self.connector_and_regex.search(source) is not None
