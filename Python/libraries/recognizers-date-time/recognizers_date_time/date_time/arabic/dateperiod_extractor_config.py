
from recognizers_date_time.date_time.arabic.date_extractor_config import ArabicDateExtractorConfiguration
from recognizers_date_time.date_time.arabic.duration_extractor_config import ArabicDurationExtractorConfiguration
from recognizers_date_time.date_time.base_date import BaseDateExtractor
from recognizers_date_time.date_time.base_dateperiod import DatePeriodExtractorConfiguration, MatchedIndex
from recognizers_date_time.date_time.base_duration import BaseDurationExtractor
from recognizers_date_time.resources.arabic_date_time import ArabicDateTime
from recognizers_number import ArabicCardinalExtractor, ArabicOrdinalExtractor
from recognizers_number.number import BaseNumberParser
from recognizers_number.number.arabic.extractors import ArabicIntegerExtractor
from recognizers_number.number.arabic.parsers import ArabicNumberParserConfiguration
from recognizers_text.utilities import RegExpUtility


class ArabicDatePeriodExtractorConfiguration(DatePeriodExtractorConfiguration):

    def __init__(self):
        super().__init__(ArabicDateTime())
        self.ordinal_extractor = ArabicOrdinalExtractor()
        self.cardinal_extractor = ArabicCardinalExtractor()
        self.cardinal_extractor = ArabicCardinalExtractor()
        self.date_point_extractor = BaseDateExtractor(ArabicDateExtractorConfiguration())
        self.number_parser = BaseNumberParser(ArabicNumberParserConfiguration())
        self.duration_extractor = BaseDurationExtractor(ArabicDurationExtractorConfiguration())
        self.integer_extractor = ArabicIntegerExtractor()
        self.from_regex = RegExpUtility.get_safe_reg_exp(ArabicDateTime.FromRegex)
        self.simple_cases_regexes = [
            RegExpUtility.get_safe_reg_exp(ArabicDateTime.SimpleCasesRegex),
            RegExpUtility.get_safe_reg_exp(ArabicDateTime.BetweenRegex),
            RegExpUtility.get_safe_reg_exp(ArabicDateTime.OneWordPeriodRegex),
            RegExpUtility.get_safe_reg_exp(ArabicDateTime.MonthWithYear),
            RegExpUtility.get_safe_reg_exp(ArabicDateTime.MonthNumWithYear),
            RegExpUtility.get_safe_reg_exp(ArabicDateTime.YearRegex),
            RegExpUtility.get_safe_reg_exp(ArabicDateTime.WeekOfMonthRegex),
            RegExpUtility.get_safe_reg_exp(ArabicDateTime.WeekOfYearRegex),
            RegExpUtility.get_safe_reg_exp(ArabicDateTime.MonthFrontBetweenRegex),
            RegExpUtility.get_safe_reg_exp(ArabicDateTime.MonthFrontSimpleCasesRegex),
            RegExpUtility.get_safe_reg_exp(ArabicDateTime.QuarterRegex),
            RegExpUtility.get_safe_reg_exp(ArabicDateTime.QuarterRegexYearFront),
            RegExpUtility.get_safe_reg_exp(ArabicDateTime.AllHalfYearRegex),
            RegExpUtility.get_safe_reg_exp(ArabicDateTime.SeasonRegex),
            RegExpUtility.get_safe_reg_exp(ArabicDateTime.WhichWeekRegex),
            RegExpUtility.get_safe_reg_exp(ArabicDateTime.RestOfDateRegex),
            RegExpUtility.get_safe_reg_exp(ArabicDateTime.LaterEarlyPeriodRegex),
            RegExpUtility.get_safe_reg_exp(ArabicDateTime.WeekWithWeekDayRangeRegex),
            RegExpUtility.get_safe_reg_exp(ArabicDateTime.YearPlusNumberRegex),
            RegExpUtility.get_safe_reg_exp(ArabicDateTime.DecadeWithCenturyRegex),
            RegExpUtility.get_safe_reg_exp(ArabicDateTime.RelativeDecadeRegex),
            RegExpUtility.get_safe_reg_exp(ArabicDateTime.ReferenceDatePeriodRegex)
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
        return RegExpUtility.is_exact_match(self.range_connector_regex, source, True)
