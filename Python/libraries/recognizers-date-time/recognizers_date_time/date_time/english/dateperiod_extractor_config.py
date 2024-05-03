#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.


from recognizers_text.utilities import RegExpUtility
from recognizers_number.number import BaseNumberParser
from recognizers_number.number.english.extractors import EnglishIntegerExtractor
from recognizers_number.number.english.parsers import EnglishNumberParserConfiguration
from ...resources.english_date_time import EnglishDateTime
from ..base_duration import BaseDurationExtractor
from ..base_date import BaseDateExtractor
from ..base_dateperiod import DatePeriodExtractorConfiguration, MatchedIndex
from .duration_extractor_config import EnglishDurationExtractorConfiguration
from .date_extractor_config import EnglishDateExtractorConfiguration
from .common_configs import EnglishOrdinalExtractor, EnglishCardinalExtractor


class EnglishDatePeriodExtractorConfiguration(DatePeriodExtractorConfiguration):

    def __init__(self, dmyDateFormat=False):
        super().__init__(EnglishDateTime())
        self.ordinal_extractor = EnglishOrdinalExtractor()
        self.cardinal_extractor = EnglishCardinalExtractor()
        self.cardinal_extractor = EnglishCardinalExtractor()
        self.date_point_extractor = BaseDateExtractor(EnglishDateExtractorConfiguration(dmyDateFormat))
        self.number_parser = BaseNumberParser(EnglishNumberParserConfiguration())
        self.duration_extractor = BaseDurationExtractor(EnglishDurationExtractorConfiguration())
        self.integer_extractor = EnglishIntegerExtractor()
        self.simple_cases_regexes = [
            RegExpUtility.get_safe_reg_exp(EnglishDateTime.SimpleCasesRegex),
            RegExpUtility.get_safe_reg_exp(EnglishDateTime.BetweenRegex),
            RegExpUtility.get_safe_reg_exp(EnglishDateTime.OneWordPeriodRegex),
            RegExpUtility.get_safe_reg_exp(EnglishDateTime.MonthWithYear),
            RegExpUtility.get_safe_reg_exp(EnglishDateTime.MonthNumWithYear),
            RegExpUtility.get_safe_reg_exp(EnglishDateTime.YearRegex),
            RegExpUtility.get_safe_reg_exp(EnglishDateTime.DecadeWithCenturyRegex),
            RegExpUtility.get_safe_reg_exp(EnglishDateTime.WeekOfMonthRegex),
            RegExpUtility.get_safe_reg_exp(EnglishDateTime.WeekOfYearRegex),
            RegExpUtility.get_safe_reg_exp(EnglishDateTime.MonthFrontBetweenRegex),
            RegExpUtility.get_safe_reg_exp(EnglishDateTime.MonthFrontSimpleCasesRegex),
            RegExpUtility.get_safe_reg_exp(EnglishDateTime.QuarterRegex),
            RegExpUtility.get_safe_reg_exp(EnglishDateTime.QuarterRegexYearFront),
            RegExpUtility.get_safe_reg_exp(EnglishDateTime.AllHalfYearRegex),
            RegExpUtility.get_safe_reg_exp(EnglishDateTime.SeasonRegex),
            RegExpUtility.get_safe_reg_exp(EnglishDateTime.WhichWeekRegex),
            RegExpUtility.get_safe_reg_exp(EnglishDateTime.RestOfDateRegex),
            RegExpUtility.get_safe_reg_exp(EnglishDateTime.LaterEarlyPeriodRegex),
            RegExpUtility.get_safe_reg_exp(EnglishDateTime.WeekWithWeekDayRangeRegex),
            RegExpUtility.get_safe_reg_exp(EnglishDateTime.YearPlusNumberRegex),
            RegExpUtility.get_safe_reg_exp(EnglishDateTime.DecadeWithCenturyRegex),
            RegExpUtility.get_safe_reg_exp(EnglishDateTime.RelativeDecadeRegex),
            RegExpUtility.get_safe_reg_exp(EnglishDateTime.ReferenceDatePeriodRegex)
        ]

    def get_from_token_index(self, source: str) -> MatchedIndex:
        return MatchedIndex(True, source.rfind('from')) if source.endswith('from') else MatchedIndex(False, -1)

    def get_between_token_index(self, source: str) -> MatchedIndex:
        return MatchedIndex(True, source.rfind('between')) if source.endswith('between') else MatchedIndex(False, -1)

    def has_connector_token(self, source: str) -> bool:
        match = self.range_connector_regex.search(source)
        return len(match.group()) == len(source) if match else None
