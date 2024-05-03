#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from typing import List, Pattern

from recognizers_text.extractor import Extractor
from recognizers_text.utilities import RegExpUtility
from recognizers_number.number import BaseNumberParser, BaseNumberExtractor
from recognizers_number.number.portuguese.extractors import PortugueseIntegerExtractor
from recognizers_number.number.portuguese.parsers import PortugueseNumberParserConfiguration
from ...resources.base_date_time import BaseDateTime
from ...resources.portuguese_date_time import PortugueseDateTime
from ..extractors import DateTimeExtractor
from ..base_duration import BaseDurationExtractor
from ..base_date import BaseDateExtractor
from ..base_dateperiod import DatePeriodExtractorConfiguration, MatchedIndex
from .duration_extractor_config import PortugueseDurationExtractorConfiguration
from .date_extractor_config import PortugueseDateExtractorConfiguration
from .common_configs import PortugueseOrdinalExtractor, PortugueseCardinalExtractor


class PortugueseDatePeriodExtractorConfiguration(DatePeriodExtractorConfiguration):

    def __init__(self):
        super().__init__(PortugueseDateTime())
        self.ordinal_extractor = PortugueseOrdinalExtractor()
        self.cardinal_extractor = PortugueseCardinalExtractor()
        self.cardinal_extractor = PortugueseCardinalExtractor()
        self.date_point_extractor = BaseDateExtractor(PortugueseDateExtractorConfiguration())
        self.number_parser = BaseNumberParser(PortugueseNumberParserConfiguration())
        self.duration_extractor = BaseDurationExtractor(PortugueseDurationExtractorConfiguration())
        self.integer_extractor = PortugueseIntegerExtractor()
        self.simple_cases_regexes = [
            RegExpUtility.get_safe_reg_exp(PortugueseDateTime.SimpleCasesRegex),
            RegExpUtility.get_safe_reg_exp(PortugueseDateTime.BetweenRegex),
            RegExpUtility.get_safe_reg_exp(PortugueseDateTime.OneWordPeriodRegex),
            RegExpUtility.get_safe_reg_exp(PortugueseDateTime.MonthWithYearRegex),
            RegExpUtility.get_safe_reg_exp(PortugueseDateTime.MonthNumWithYearRegex),
            RegExpUtility.get_safe_reg_exp(PortugueseDateTime.YearRegex),
            RegExpUtility.get_safe_reg_exp(PortugueseDateTime.DecadeWithCenturyRegex),
            RegExpUtility.get_safe_reg_exp(PortugueseDateTime.WeekOfMonthRegex),
            RegExpUtility.get_safe_reg_exp(PortugueseDateTime.WeekOfYearRegex),
            RegExpUtility.get_safe_reg_exp(
                    PortugueseDateTime.MonthFrontBetweenRegex),
            RegExpUtility.get_safe_reg_exp(
                    PortugueseDateTime.MonthFrontSimpleCasesRegex),
            RegExpUtility.get_safe_reg_exp(PortugueseDateTime.QuarterRegex),
            RegExpUtility.get_safe_reg_exp(
                    PortugueseDateTime.QuarterRegexYearFront),
            RegExpUtility.get_safe_reg_exp(PortugueseDateTime.AllHalfYearRegex),
            RegExpUtility.get_safe_reg_exp(PortugueseDateTime.SeasonRegex),
            RegExpUtility.get_safe_reg_exp(PortugueseDateTime.WhichWeekRegex),
            RegExpUtility.get_safe_reg_exp(PortugueseDateTime.RestOfDateRegex),
            RegExpUtility.get_safe_reg_exp(
                    PortugueseDateTime.LaterEarlyPeriodRegex),
            RegExpUtility.get_safe_reg_exp(
                    PortugueseDateTime.WeekWithWeekDayRangeRegex),
            RegExpUtility.get_safe_reg_exp(PortugueseDateTime.YearPlusNumberRegex),
            RegExpUtility.get_safe_reg_exp(PortugueseDateTime.DecadeWithCenturyRegex),
            RegExpUtility.get_safe_reg_exp(PortugueseDateTime.RelativeDecadeRegex),
            RegExpUtility.get_safe_reg_exp(PortugueseDateTime.ReferenceDatePeriodRegex)
        ]

    def get_from_token_index(self, source: str) -> MatchedIndex:
        return MatchedIndex(True, source.rfind('from')) if source.endswith('from') else MatchedIndex(False, -1)

    def get_between_token_index(self, source: str) -> MatchedIndex:
        return MatchedIndex(True, source.rfind('between')) if source.endswith('between') else MatchedIndex(False, -1)

    def has_connector_token(self, source: str) -> bool:
        match = self.range_connector_regex.search(source)
        return len(match.group()) == len(source) if match else None
