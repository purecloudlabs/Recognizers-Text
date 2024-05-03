#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.


from recognizers_number import DutchCardinalExtractor, DutchOrdinalExtractor
from recognizers_number.number import BaseNumberParser
from recognizers_number.number.dutch.extractors import DutchCardinalExtractor, DutchIntegerExtractor
from recognizers_number.number.dutch.parsers import DutchNumberParserConfiguration
from recognizers_text.utilities import RegExpUtility

from ...resources.dutch_date_time import DutchDateTime
from ..base_date import BaseDateExtractor
from ..base_dateperiod import DatePeriodExtractorConfiguration, MatchedIndex
from ..base_duration import BaseDurationExtractor
from .date_extractor_config import DutchDateExtractorConfiguration
from .duration_extractor_config import DutchDurationExtractorConfiguration


class DutchDatePeriodExtractorConfiguration(DatePeriodExtractorConfiguration):

    def __init__(self):
        super().__init__(DutchDateTime())
        self.ordinal_extractor = DutchOrdinalExtractor()
        self.cardinal_extractor = DutchCardinalExtractor()
        self.cardinal_extractor = DutchCardinalExtractor()
        self.date_point_extractor = BaseDateExtractor(DutchDateExtractorConfiguration())
        self.number_parser = BaseNumberParser(DutchNumberParserConfiguration())
        self.duration_extractor = BaseDurationExtractor(DutchDurationExtractorConfiguration())
        self.integer_extractor = DutchIntegerExtractor()
        self.from_regex = RegExpUtility.get_safe_reg_exp(DutchDateTime.FromRegex)
        self.simple_cases_regexes = [
            RegExpUtility.get_safe_reg_exp(DutchDateTime.SimpleCasesRegex),
            RegExpUtility.get_safe_reg_exp(DutchDateTime.BetweenRegex),
            RegExpUtility.get_safe_reg_exp(DutchDateTime.OneWordPeriodRegex),
            RegExpUtility.get_safe_reg_exp(DutchDateTime.MonthWithYear),
            RegExpUtility.get_safe_reg_exp(DutchDateTime.MonthNumWithYear),
            RegExpUtility.get_safe_reg_exp(DutchDateTime.YearRegex),
            RegExpUtility.get_safe_reg_exp(DutchDateTime.WeekOfMonthRegex),
            RegExpUtility.get_safe_reg_exp(DutchDateTime.WeekOfYearRegex),
            RegExpUtility.get_safe_reg_exp(DutchDateTime.MonthFrontBetweenRegex),
            RegExpUtility.get_safe_reg_exp(DutchDateTime.MonthFrontSimpleCasesRegex),
            RegExpUtility.get_safe_reg_exp(DutchDateTime.QuarterRegex),
            RegExpUtility.get_safe_reg_exp(DutchDateTime.QuarterRegexYearFront),
            RegExpUtility.get_safe_reg_exp(DutchDateTime.AllHalfYearRegex),
            RegExpUtility.get_safe_reg_exp(DutchDateTime.SeasonRegex),
            RegExpUtility.get_safe_reg_exp(DutchDateTime.WhichWeekRegex),
            RegExpUtility.get_safe_reg_exp(DutchDateTime.RestOfDateRegex),
            RegExpUtility.get_safe_reg_exp(DutchDateTime.LaterEarlyPeriodRegex),
            RegExpUtility.get_safe_reg_exp(DutchDateTime.WeekWithWeekDayRangeRegex),
            RegExpUtility.get_safe_reg_exp(DutchDateTime.YearPlusNumberRegex),
            RegExpUtility.get_safe_reg_exp(DutchDateTime.DecadeWithCenturyRegex),
            RegExpUtility.get_safe_reg_exp(DutchDateTime.RelativeDecadeRegex),
            RegExpUtility.get_safe_reg_exp(DutchDateTime.ReferenceDatePeriodRegex),
        ]

    def get_from_token_index(self, source: str) -> MatchedIndex:
        match = self.from_regex.search(source)
        if match:
            return MatchedIndex(True, match.start())

        return MatchedIndex(False, -1)

    def get_between_token_index(self, source: str) -> MatchedIndex:
        match = self.between_token_regex.search(source)
        if match:
            return MatchedIndex(True, match.start())

        return MatchedIndex(False, -1)

    def has_connector_token(self, source: str) -> bool:
        return self.range_connector_regex.search(source) is not None
