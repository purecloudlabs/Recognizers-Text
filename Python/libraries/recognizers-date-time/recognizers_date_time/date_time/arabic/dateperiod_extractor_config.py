from typing import List, Pattern

from recognizers_text.utilities import RegExpUtility
from recognizers_number.number import BaseNumberParser
from recognizers_number.number.arabic.extractors import ArabicIntegerExtractor
from recognizers_number.number.arabic.parsers import ArabicNumberParserConfiguration
from recognizers_date_time.resources.base_date_time import BaseDateTime
from recognizers_date_time.resources.arabic_date_time import ArabicDateTime
from recognizers_date_time.date_time.extractors import DateTimeExtractor
from recognizers_date_time.date_time.base_duration import BaseDurationExtractor
from recognizers_date_time.date_time.base_date import BaseDateExtractor
from recognizers_date_time.date_time.base_dateperiod import DatePeriodExtractorConfiguration, MatchedIndex
from recognizers_date_time.date_time.arabic.date_extractor_config import ArabicDateExtractorConfiguration
from recognizers_date_time.date_time.arabic.duration_extractor_config import ArabicDurationExtractorConfiguration
from recognizers_text.extractor import Extractor
from recognizers_number import ArabicOrdinalExtractor, BaseNumberExtractor, ArabicCardinalExtractor


class ArabicDatePeriodExtractorConfiguration(DatePeriodExtractorConfiguration):

    @property
    def till_regex(self) -> Pattern:
        return self._till_regex

    @property
    def range_connector_regex(self) -> Pattern:
        return self._range_connector_regex

    @property
    def day_regex(self) -> Pattern:
        return self._day_regex

    @property
    def month_num_regex(self) -> Pattern:
        return self._month_num_regex

    @property
    def illegal_year_regex(self) -> Pattern:
        return self._illegal_year_regex


    @property
    def week_day_regex(self) -> Pattern:
        return self._week_day_regex

    @property
    def relative_month_regex(self) -> Pattern:
        return self._relative_month_regex

    @property
    def month_suffix_regex(self) -> Pattern:
        return self._month_suffix_regex

    @property
    def written_month_regex(self) -> Pattern:
        return self._written_month_regex

    @property
    def date_unit_regex(self) -> Pattern:
        return self._date_unit_regex

    @property
    def time_unit_regex(self) -> Pattern:
        return self._time_unit_regex

    @property
    def previous_prefix_regex(self) -> Pattern:
        return self._previous_prefix_regex

    @property
    def next_prefix_regex(self) -> Pattern:
        return self._next_prefix_regex

    @property
    def future_suffix_regex(self) -> Pattern:
        return self._future_suffix_regex

    @property
    def now_regex(self) -> Pattern:
        return self._now_regex

    @property
    def simple_cases_regexes(self) -> List[Pattern]:
        return self._simple_cases_regexes

    @property
    def followed_unit(self) -> Pattern:
        return self._followed_unit

    @property
    def number_combined_with_unit(self) -> Pattern:
        return self._number_combined_with_unit


    @property
    def week_of_regex(self) -> Pattern:
        return self._week_of_regex

    @property
    def month_of_regex(self) -> Pattern:
        return self._month_of_regex

    @property
    def in_connector_regex(self) -> Pattern:
        return self._in_connector_regex

    @property
    def range_unit_regex(self) -> Pattern:
        return self._range_unit_regex

    @property
    def within_next_prefix_regex(self) -> Pattern:
        return self._within_next_prefix_regex

    @property
    def rest_of_date_regex(self) -> Pattern:
        return self._rest_of_date_regex

    @property
    def later_early_year_regex(self) -> Pattern:
        return self._later_early_year_regex

    @property
    def week_with_week_day_range_regex(self) -> Pattern:
        return self._week_with_week_day_range_regex

    @property
    def year_period_regex(self) -> Pattern:
        return self._year_period_regex

    @property
    def complex_date_period_regex(self) -> Pattern:
        return self._complex_date_period_regex

    @property
    def ago_regex(self) -> Pattern:
        return self._ago_regex

    @property
    def later_regex(self) -> Pattern:
        return self._later_regex

    @property
    def less_than_regex(self) -> Pattern:
        return self._less_than_regex

    @property
    def more_than_regex(self) -> Pattern:
        return self._more_than_regex

    @property
    def century_suffix_regex(self) -> Pattern:
        return self._century_suffix_regex

    @property
    def first_last_regex(self) -> Pattern:
        return self._first_last_regex

    @property
    def of_year_regex(self) -> Pattern:
        return self._of_year_regex

    @property
    def from_regex(self) -> Pattern:
        return self._from_regex

    @property
    def between_token_regex(self) -> Pattern:
        return self._between_token_regex

    @property
    def date_point_extractor(self) -> DateTimeExtractor:
        return self._date_point_extractor

    @property
    def ordinal_extractor(self) -> BaseNumberExtractor:
        return self._ordinal_extractor

    @property
    def cardinal_extractor(self) -> Extractor:
        return self._cardinal_extractor

    @property
    def number_parser(self) -> BaseNumberParser:
        return self._number_parser

    @property
    def duration_extractor(self) -> DateTimeExtractor:
        return self._duration_extractor

    @property
    def check_both_before_after(self) -> bool:
        return self._check_both_before_after

    @property
    def past_regex(self) -> Pattern:
        return self._past_regex

    @property
    def future_regex(self) -> Pattern:
        return self._future_regex

    @property
    def duration_date_restrictions(self) -> [str]:
        return self._duration_date_restrictions

    @property
    def integer_extractor(self) -> BaseNumberExtractor:
        return self._integer_extractor

    @property
    def year_regex(self) -> Pattern:
        return self._year_regex

    def __init__(self):
        self._of_year_regex = RegExpUtility.get_safe_reg_exp(ArabicDateTime.OfYearRegex)
        self._week_with_week_day_range_regex = RegExpUtility.get_safe_reg_exp(ArabicDateTime.WeekWithWeekDayRangeRegex)
        self._later_early_year_regex = RegExpUtility.get_safe_reg_exp(ArabicDateTime.LaterEarlyPeriodRegex)
        self._all_half_year_regex = RegExpUtility.get_safe_reg_exp(ArabicDateTime.AllHalfYearRegex)
        self._complex_date_period_regex = RegExpUtility.get_safe_reg_exp(ArabicDateTime.ComplexDatePeriodRegex)
        self._rest_of_date_regex = RegExpUtility.get_safe_reg_exp(ArabicDateTime.RestOfDateRegex)
        self._which_week_regex = RegExpUtility.get_safe_reg_exp(ArabicDateTime.WhichWeekRegex)
        self._next_prefix_regex = RegExpUtility.get_safe_reg_exp(ArabicDateTime.NextPrefixRegex)
        self._month_suffix_regex = RegExpUtility.get_safe_reg_exp(ArabicDateTime.MonthSuffixRegex)
        self._relative_month_regex = RegExpUtility.get_safe_reg_exp(ArabicDateTime.RelativeMonthRegex)
        self._written_month_regex = RegExpUtility.get_safe_reg_exp(ArabicDateTime.WrittenMonthRegex)
        self._week_day_regex = RegExpUtility.get_safe_reg_exp(ArabicDateTime.WeekDayRegex)
        self._day_regex = RegExpUtility.get_safe_reg_exp(ArabicDateTime.DayRegex)
        self._range_connector_regex = RegExpUtility.get_safe_reg_exp(ArabicDateTime.RangeConnectorRegex)
        self._time_unit_regex = RegExpUtility.get_safe_reg_exp(ArabicDateTime.TimeUnitRegex)
        self._first_last_regex = RegExpUtility.get_safe_reg_exp(ArabicDateTime.FirstLastRegex)
        self._between_token_regex = RegExpUtility.get_safe_reg_exp(ArabicDateTime.BetweenTokenRegex)
        self._previous_prefix_regex = RegExpUtility.get_safe_reg_exp(
            ArabicDateTime.PastSuffixRegex)
        self._check_both_before_after = ArabicDateTime.CheckBothBeforeAfter
        self._week_of_month_regex = ArabicDateTime.WeekOfMonthRegex

        self._simple_cases_regexes = [
            RegExpUtility.get_safe_reg_exp(ArabicDateTime.SimpleCasesRegex),
            RegExpUtility.get_safe_reg_exp(ArabicDateTime.BetweenRegex),
            RegExpUtility.get_safe_reg_exp(ArabicDateTime.OneWordPeriodRegex),
            RegExpUtility.get_safe_reg_exp(ArabicDateTime.MonthWithYear),
            RegExpUtility.get_safe_reg_exp(ArabicDateTime.MonthNumWithYear),
            RegExpUtility.get_safe_reg_exp(ArabicDateTime.YearRegex),
            RegExpUtility.get_safe_reg_exp(ArabicDateTime.WeekOfMonthRegex),
            RegExpUtility.get_safe_reg_exp(ArabicDateTime.WeekOfYearRegex),
            RegExpUtility.get_safe_reg_exp(
                ArabicDateTime.MonthFrontBetweenRegex),
            RegExpUtility.get_safe_reg_exp(
                ArabicDateTime.MonthFrontSimpleCasesRegex),
            RegExpUtility.get_safe_reg_exp(ArabicDateTime.QuarterRegex),
            RegExpUtility.get_safe_reg_exp(
                ArabicDateTime.QuarterRegexYearFront),
            RegExpUtility.get_safe_reg_exp(ArabicDateTime.AllHalfYearRegex),
            RegExpUtility.get_safe_reg_exp(ArabicDateTime.SeasonRegex),
            RegExpUtility.get_safe_reg_exp(ArabicDateTime.WhichWeekRegex),
            RegExpUtility.get_safe_reg_exp(ArabicDateTime.RestOfDateRegex),
            RegExpUtility.get_safe_reg_exp(
                ArabicDateTime.LaterEarlyPeriodRegex),
            RegExpUtility.get_safe_reg_exp(
                ArabicDateTime.WeekWithWeekDayRangeRegex),
            RegExpUtility.get_safe_reg_exp(ArabicDateTime.YearPlusNumberRegex),
            RegExpUtility.get_safe_reg_exp(ArabicDateTime.DecadeWithCenturyRegex),
            RegExpUtility.get_safe_reg_exp(ArabicDateTime.RelativeDecadeRegex),
            RegExpUtility.get_safe_reg_exp(ArabicDateTime.ReferenceDatePeriodRegex)
        ]

        self._check_both_before_after = ArabicDateTime.CheckBothBeforeAfter
        self._illegal_year_regex = RegExpUtility.get_safe_reg_exp(
            BaseDateTime.IllegalYearRegex)
        self._year_regex = RegExpUtility.get_safe_reg_exp(
            ArabicDateTime.YearRegex)
        self._till_regex = RegExpUtility.get_safe_reg_exp(
            ArabicDateTime.TillRegex)
        self._followed_unit = RegExpUtility.get_safe_reg_exp(
            ArabicDateTime.FollowedDateUnit)
        self._number_combined_with_unit = RegExpUtility.get_safe_reg_exp(
            ArabicDateTime.NumberCombinedWithDateUnit)
        self._past_regex = RegExpUtility.get_safe_reg_exp(
            ArabicDateTime.PreviousPrefixRegex)
        self._future_regex = RegExpUtility.get_safe_reg_exp(
            ArabicDateTime.NextPrefixRegex)
        self._week_of_regex = RegExpUtility.get_safe_reg_exp(
            ArabicDateTime.WeekOfRegex)
        self._month_of_regex = RegExpUtility.get_safe_reg_exp(
            ArabicDateTime.MonthOfRegex)
        self._date_unit_regex = RegExpUtility.get_safe_reg_exp(
            ArabicDateTime.DateUnitRegex)
        self._within_next_prefix_regex = RegExpUtility.get_safe_reg_exp(
            ArabicDateTime.WithinNextPrefixRegex)
        self._in_connector_regex = RegExpUtility.get_safe_reg_exp(
            ArabicDateTime.InConnectorRegex)
        self._range_unit_regex = RegExpUtility.get_safe_reg_exp(
            ArabicDateTime.RangeUnitRegex)

        self._from_regex = RegExpUtility.get_safe_reg_exp(
            ArabicDateTime.FromRegex)
        self.before_regex = RegExpUtility.get_safe_reg_exp(
            ArabicDateTime.BeforeRegex)

        self._date_point_extractor = BaseDateExtractor(
            ArabicDateExtractorConfiguration())
        self._number_parser = BaseNumberParser(
            ArabicNumberParserConfiguration())
        self._duration_extractor = BaseDurationExtractor(ArabicDurationExtractorConfiguration())
        self._integer_extractor = ArabicIntegerExtractor()
        self._now_regex = RegExpUtility.get_safe_reg_exp(
            ArabicDateTime.NowRegex)
        self._future_suffix_regex = RegExpUtility.get_safe_reg_exp(
            ArabicDateTime.FutureSuffixRegex
        )
        self._ago_regex = RegExpUtility.get_safe_reg_exp(
            ArabicDateTime.AgoRegex
        )
        self._later_regex = RegExpUtility.get_safe_reg_exp(
            ArabicDateTime.LaterRegex
        )
        self._less_than_regex = RegExpUtility.get_safe_reg_exp(
            ArabicDateTime.LessThanRegex
        )
        self._more_than_regex = RegExpUtility.get_safe_reg_exp(
            ArabicDateTime.MoreThanRegex
        )
        self._duration_date_restrictions = ArabicDateTime.DurationDateRestrictions
        self._year_period_regex = RegExpUtility.get_safe_reg_exp(
            ArabicDateTime.YearPeriodRegex
        )
        self._month_num_regex = RegExpUtility.get_safe_reg_exp(
            ArabicDateTime.MonthNumRegex
        )
        self._century_suffix_regex = RegExpUtility.get_safe_reg_exp(
            ArabicDateTime.CenturySuffixRegex
        )
        self._decade_with_century_regex = RegExpUtility.get_safe_reg_exp(
            ArabicDateTime.DecadeWithCenturyRegex
        )
        self._ordinal_extractor = ArabicOrdinalExtractor()
        self._cardinal_extractor = ArabicCardinalExtractor()
        self._previous_prefix_regex = RegExpUtility.get_safe_reg_exp(
            ArabicDateTime.PreviousPrefixRegex
        )
        self._cardinal_extractor = ArabicCardinalExtractor()
        self._time_unit_regex = RegExpUtility.get_safe_reg_exp(ArabicDateTime.TimeUnitRegex)

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
        return RegExpUtility.is_exact_match(self.has_connector_token, source)
