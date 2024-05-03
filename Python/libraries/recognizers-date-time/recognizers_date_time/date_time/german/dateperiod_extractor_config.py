#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.


from recognizers_text.utilities import RegExpUtility
from recognizers_number.number import BaseNumberParser
from recognizers_number.number.german.extractors import GermanIntegerExtractor, GermanCardinalExtractor
from recognizers_number.number.german.parsers import GermanNumberParserConfiguration
from ...resources.german_date_time import GermanDateTime
from ..base_duration import BaseDurationExtractor
from ..base_date import BaseDateExtractor
from ..base_dateperiod import DatePeriodExtractorConfiguration, MatchedIndex
from .duration_extractor_config import GermanDurationExtractorConfiguration
from .date_extractor_config import GermanDateExtractorConfiguration
from recognizers_number import GermanOrdinalExtractor, GermanCardinalExtractor


class GermanDatePeriodExtractorConfiguration(DatePeriodExtractorConfiguration):

    def __init__(self):
        super().__init__(GermanDateTime())
        self.ordinal_extractor = GermanOrdinalExtractor()
        self.cardinal_extractor = GermanCardinalExtractor()
        self.cardinal_extractor = GermanCardinalExtractor()
        self.date_point_extractor = BaseDateExtractor(GermanDateExtractorConfiguration())
        self.number_parser = BaseNumberParser(GermanNumberParserConfiguration())
        self.duration_extractor = BaseDurationExtractor(GermanDurationExtractorConfiguration())
        self.integer_extractor = GermanIntegerExtractor()
        self.from_regex = RegExpUtility.get_safe_reg_exp(GermanDateTime.FromRegex)
        self.simple_cases_regexes = [
            RegExpUtility.get_safe_reg_exp(GermanDateTime.SimpleCasesRegex),
            RegExpUtility.get_safe_reg_exp(GermanDateTime.BetweenRegex),
            RegExpUtility.get_safe_reg_exp(GermanDateTime.OneWordPeriodRegex),
            RegExpUtility.get_safe_reg_exp(GermanDateTime.MonthWithYear),
            RegExpUtility.get_safe_reg_exp(GermanDateTime.MonthNumWithYear),
            RegExpUtility.get_safe_reg_exp(GermanDateTime.YearRegex),
            RegExpUtility.get_safe_reg_exp(GermanDateTime.YearPeriodRegex),
            RegExpUtility.get_safe_reg_exp(GermanDateTime.WeekOfYearRegex),
            RegExpUtility.get_safe_reg_exp(GermanDateTime.WeekDayOfMonthRegex),
            RegExpUtility.get_safe_reg_exp(
                    GermanDateTime.MonthFrontBetweenRegex),
            RegExpUtility.get_safe_reg_exp(
                    GermanDateTime.MonthFrontSimpleCasesRegex),
            RegExpUtility.get_safe_reg_exp(GermanDateTime.QuarterRegex),
            RegExpUtility.get_safe_reg_exp(
                    GermanDateTime.QuarterRegexYearFront),
            RegExpUtility.get_safe_reg_exp(GermanDateTime.SeasonRegex),
            RegExpUtility.get_safe_reg_exp(
                    GermanDateTime.LaterEarlyPeriodRegex),
            RegExpUtility.get_safe_reg_exp(
                    GermanDateTime.WeekWithWeekDayRangeRegex),
            RegExpUtility.get_safe_reg_exp(GermanDateTime.YearPlusNumberRegex),
            RegExpUtility.get_safe_reg_exp(GermanDateTime.DecadeWithCenturyRegex),
            RegExpUtility.get_safe_reg_exp(GermanDateTime.RelativeDecadeRegex)
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
        return self.range_connector_regex.search(source) is not None
