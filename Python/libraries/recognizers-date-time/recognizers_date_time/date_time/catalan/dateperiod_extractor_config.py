from typing import List, Pattern

from recognizers_text import Extractor
from recognizers_text.utilities import RegExpUtility
from recognizers_number.number import BaseNumberParser, BaseNumberExtractor
from recognizers_number.number.catalan.extractors import CatalanIntegerExtractor,\
    CatalanCardinalExtractor, CatalanOrdinalExtractor
from recognizers_number.number.catalan.parsers import CatalanNumberParserConfiguration
from ...resources.base_date_time import BaseDateTime
from ...resources.catalan_date_time import CatalanDateTime
from ..extractors import DateTimeExtractor
from ..base_duration import BaseDurationExtractor
from ..base_date import BaseDateExtractor
from ..base_dateperiod import DatePeriodExtractorConfiguration, MatchedIndex
from .duration_extractor_config import CatalanDurationExtractorConfiguration
from .date_extractor_config import CatalanDateExtractorConfiguration


class CatalanDatePeriodExtractorConfiguration(DatePeriodExtractorConfiguration):
    @property
    def year_period_regex(self) -> Pattern:
        return self._year_period_regex

    @property
    def all_half_year_regex(self):
        return self._all_half_year_regex

    @property
    def previous_prefix_regex(self) -> Pattern:
        return self._previous_prefix_regex

    @property
    def check_both_before_after(self) -> Pattern:
        return self._check_both_before_after

    @property
    def previous_prefix_regex(self) -> Pattern:
        return self._previous_prefix_regex

    @property
    def check_both_before_after(self) -> Pattern:
        return self._check_both_before_after

    @property
    def time_unit_regex(self) -> Pattern:
        return self._time_unit_regex

    @property
    def ordinal_extractor(self) -> Extractor:
        return self._ordinal_extractor

    @property
    def cardinal_extractor(self) -> Extractor:
        return self._cardinal_extractor

    @property
    def within_next_prefix_regex(self) -> Pattern:
        return self._within_next_prefix_regex

    @property
    def simple_cases_regexes(self) -> List[Pattern]:
        return self._simple_cases_regexes

    @property
    def illegal_year_regex(self) -> Pattern:
        return self._illegal_year_regex

    @property
    def year_regex(self) -> Pattern:
        return self._year_regex

    @property
    def decade_with_century_regex(self) -> Pattern:
        return self._decade_with_century_regex

    @property
    def till_regex(self) -> Pattern:
        return self._till_regex

    @property
    def followed_unit(self) -> Pattern:
        return self._followed_unit

    @property
    def number_combined_with_unit(self) -> Pattern:
        return self._number_combined_with_unit

    @property
    def past_regex(self) -> Pattern:
        return self._past_regex

    @property
    def future_regex(self) -> Pattern:
        return self._future_regex

    @property
    def week_of_regex(self) -> Pattern:
        return self._week_of_regex

    @property
    def month_of_regex(self) -> Pattern:
        return self._month_of_regex

    @property
    def date_unit_regex(self) -> Pattern:
        return self._date_unit_regex

    @property
    def in_connector_regex(self) -> Pattern:
        return self._in_connector_regex

    @property
    def range_unit_regex(self) -> Pattern:
        return self._range_unit_regex

    @property
    def date_point_extractor(self) -> DateTimeExtractor:
        return self._date_point_extractor

    @property
    def integer_extractor(self) -> BaseNumberExtractor:
        return self._integer_extractor

    @property
    def number_parser(self) -> BaseNumberParser:
        return self._number_parser

    @property
    def duration_extractor(self) -> DateTimeExtractor:
        return self._duration_extractor

    @property
    def now_regex(self) -> Pattern:
        return self._now_regex

    @property
    def future_suffix_regex(self) -> Pattern:
        return self._future_suffix_regex

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
    def duration_date_restrictions(self) -> [str]:
        return self._duration_date_restrictions

    @property
    def month_num_regex(self) -> Pattern:
        return self._month_num_regex

    @property
    def century_suffix_regex(self) -> Pattern:
        return self._century_suffix_regex

    def __init__(self):
        self._year_period_regex = RegExpUtility.get_safe_reg_exp(CatalanDateTime.YearPeriodRegex)
        self._previous_prefix_regex = RegExpUtility.get_safe_reg_exp(CatalanDateTime.PastRegex)
        self._simple_cases_regexes = [
            self._year_period_regex,
            RegExpUtility.get_safe_reg_exp(CatalanDateTime.SimpleCasesRegex),
            RegExpUtility.get_safe_reg_exp(CatalanDateTime.DayBetweenRegex),
            RegExpUtility.get_safe_reg_exp(CatalanDateTime.OneWordPeriodRegex),
            RegExpUtility.get_safe_reg_exp(CatalanDateTime.MonthWithYearRegex),
            RegExpUtility.get_safe_reg_exp(CatalanDateTime.MonthNumWithYearRegex),
            RegExpUtility.get_safe_reg_exp(CatalanDateTime.YearRegex),
            RegExpUtility.get_safe_reg_exp(CatalanDateTime.WeekOfMonthRegex),
            RegExpUtility.get_safe_reg_exp(CatalanDateTime.WeekOfYearRegex),
            RegExpUtility.get_safe_reg_exp(CatalanDateTime.MonthFrontBetweenRegex),
            RegExpUtility.get_safe_reg_exp(CatalanDateTime.MonthFrontSimpleCasesRegex),
            RegExpUtility.get_safe_reg_exp(CatalanDateTime.QuarterRegex),
            RegExpUtility.get_safe_reg_exp(CatalanDateTime.QuarterRegexYearFront),
            RegExpUtility.get_safe_reg_exp(CatalanDateTime.SeasonRegex),
            RegExpUtility.get_safe_reg_exp(CatalanDateTime.RestOfDateRegex),
            RegExpUtility.get_safe_reg_exp(CatalanDateTime.LaterEarlyPeriodRegex),
            RegExpUtility.get_safe_reg_exp(CatalanDateTime.WeekWithWeekDayRangeRegex),
            RegExpUtility.get_safe_reg_exp(CatalanDateTime.YearPlusNumberRegex),
            RegExpUtility.get_safe_reg_exp(CatalanDateTime.WhichWeekRegex),
            RegExpUtility.get_safe_reg_exp(CatalanDateTime.ReferenceDatePeriodRegex),
        ]
        self._check_both_before_after = CatalanDateTime.CheckBothBeforeAfter
        self._time_unit_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.TimeUnitRegex)
        self._within_next_prefix_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.WithinNextPrefixRegex
        )
        self._illegal_year_regex = RegExpUtility.get_safe_reg_exp(
            BaseDateTime.IllegalYearRegex)
        self._year_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.YearRegex)
        self._till_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.TillRegex)
        self._followed_unit = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.FollowedDateUnit)
        self._number_combined_with_unit = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.NumberCombinedWithDateUnit)
        self._past_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.PastRegex)
        self._future_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.FutureRegex)
        self._week_of_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.WeekOfRegex)
        self._month_of_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.MonthOfRegex)
        self._date_unit_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.DateUnitRegex)
        self._in_connector_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.InConnectorRegex)
        self._range_unit_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.RangeUnitRegex)
        self._all_half_year_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.AllHalfYearRegex)
        self.from_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.FromRegex)
        self.range_connector_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.RangeConnectorRegex)
        self.between_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.BetweenRegex)

        self._date_point_extractor = BaseDateExtractor(
            CatalanDateExtractorConfiguration())
        self._integer_extractor = CatalanIntegerExtractor()
        self._number_parser = BaseNumberParser(
            CatalanNumberParserConfiguration())
        self._duration_extractor = BaseDurationExtractor(
            CatalanDurationExtractorConfiguration())
        self._now_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.NowRegex)
        self._future_suffix_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.FutureSuffixRegex
        )
        self._ago_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.AgoRegex
        )
        self._later_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.LaterRegex
        )
        self._less_than_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.LessThanRegex
        )
        self._more_than_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.MoreThanRegex
        )
        self._duration_date_restrictions = CatalanDateTime.DurationDateRestrictions
        self._month_num_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.MonthNumRegex
        )
        self._century_suffix_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.CenturySuffixRegex
        )
        self._check_both_before_after = False
        self._cardinal_extractor = CatalanCardinalExtractor()
        self._ordinal_extractor = CatalanOrdinalExtractor()
        self._decade_with_century_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.DecadeWithCenturyRegex)
        self._previous_prefix_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.PreviousPrefixRegex
        )

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
