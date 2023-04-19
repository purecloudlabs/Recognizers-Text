#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from typing import Pattern, Dict
import regex

from recognizers_number import JapaneseIntegerExtractor, CJKNumberParser, JapaneseNumberParserConfiguration, \
    JapaneseCardinalExtractor
from recognizers_text import RegExpUtility
from .date_extractor import JapaneseDateExtractor
from ...resources.japanese_date_time import JapaneseDateTime
from ..base_dateperiod import DatePeriodParserConfiguration
from .date_parser import JapaneseDateParser


class JapaneseDatePeriodParserConfiguration(DatePeriodParserConfiguration):

    @property
    def integer_extractor(self) -> JapaneseIntegerExtractor:
        return self._integer_extractor

    @property
    def number_parser(self) -> CJKNumberParser:
        return self._number_parser

    @property
    def date_extractor(self) -> JapaneseDateExtractor:
        return self._date_extractor

    @property
    def cardinal_extractor(self) -> JapaneseCardinalExtractor:
        return self._cardinal_extractor

    @property
    def date_parser(self) -> JapaneseDateParser:
        return self._date_parser

    @property
    def dynasty_year_regex(self) -> Pattern:
        return self._dynasty_year_regex

    @property
    def dynasty_start_year(self) -> Pattern:
        return self._dynasty_start_year

    @property
    def dynasty_year_map(self) -> Dict[str, int]:
        return self._dynasty_year_map

    @property
    def simple_cases_regex(self) -> Pattern:
        return self._simple_cases_regex

    @property
    def this_regex(self) -> Pattern:
        return self._this_regex

    @property
    def next_regex(self) -> Pattern:
        return self._next_regex

    @property
    def last_regex(self) -> Pattern:
        return self._last_regex

    @property
    def next_month_regex(self) -> Pattern:
        return self._next_month_regex

    @property
    def after_next_month_regex(self) -> Pattern:
        return self._after_next_month_regex

    @property
    def last_month_regex(self) -> Pattern:
        return self._last_month_regex

    @property
    def next_year_regex(self) -> Pattern:
        return self._next_year_regex

    @property
    def after_next_year_regex(self) -> Pattern:
        return self._after_next_year_regex

    @property
    def last_year_regex(self) -> Pattern:
        return self._last_year_regex

    @property
    def this_year_regex(self) -> Pattern:
        return self._this_year_regex

    @property
    def year_to_year(self) -> Pattern:
        return self._year_to_year

    @property
    def year_to_year_suffix_required(self) -> Pattern:
        return self._year_to_year_suffix_required

    @property
    def year_regex(self) -> Pattern:
        return self._year_regex

    @property
    def year_cjk_regex(self) -> Pattern:
        return self._year_cjk_regex

    @property
    def month_to_month_regex(self) -> Pattern:
        return self._month_to_month_regex

    @property
    def month_to_month_regex_suffix_required(self) -> Pattern:
        return self._month_to_month_regex_suffix_required

    @property
    def day_to_day(self) -> Pattern:
        return self._day_to_day

    @property
    def month_day_range_regex(self) -> Pattern:
        return self._month_day_range_regex

    @property
    def day_regex_for_period(self) -> Pattern:
        return self._day_regex_for_period

    @property
    def month_regex(self) -> Pattern:
        return self._month_regex

    @property
    def special_month_regex(self) -> Pattern:
        return self._special_month_regex

    @property
    def special_year_regex(self) -> Pattern:
        return self._special_year_regex

    @property
    def year_and_month(self) -> Pattern:
        return self._year_and_month

    @property
    def pure_num_year_and_month(self) -> Pattern:
        return self._pure_num_year_and_month

    @property
    def simple_year_and_month(self) -> Pattern:
        return self._simple_year_and_month

    @property
    def one_word_period_regex(self) -> Pattern:
        return self._one_word_period_regex

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
    def week_with_week_day_range_regex(self) -> Pattern:
        return self._week_with_week_day_range_regex

    @property
    def unit_regex(self) -> Pattern:
        return self._unit_regex

    @property
    def duration_unit_regex(self) -> Pattern:
        return self._duration_unit_regex

    @property
    def week_of_year_regex(self) -> Pattern:
        return self._week_of_year_regex

    @property
    def week_of_month_regex(self) -> Pattern:
        return self._week_of_month_regex

    @property
    def week_of_date_regex(self) -> Pattern:
        return self._week_of_date_regex

    @property
    def month_of_date_regex(self) -> Pattern:
        return self._month_of_date_regex

    @property
    def which_week_regex(self) -> Pattern:
        return self._which_week_regex

    @property
    def first_last_of_year_regex(self) -> Pattern:
        return self._first_last_of_year_regex

    @property
    def season_regex(self) -> Pattern:
        return self._season_regex

    @property
    def quarter_regex(self) -> Pattern:
        return self._quarter_regex

    @property
    def decade_regex(self) -> Pattern:
        return self._decade_regex

    @property
    def century_regex(self) -> Pattern:
        return self._century_regex

    @property
    def relative_regex(self) -> Pattern:
        return self._relative_regex

    @property
    def relative_month_regex(self) -> Pattern:
        return self._relative_month_regex

    @property
    def later_early_period_regex(self) -> Pattern:
        return self._later_early_period_regex

    @property
    def date_period_with_ago_and_later(self) -> Pattern:
        return self._date_period_with_ago_and_later

    @property
    def reference_date_period_regex(self) -> Pattern:
        return self._reference_date_period_regex

    @property
    def complex_date_period_regex(self) -> Pattern:
        return self._complex_date_period_regex

    @property
    def duration_relative_duration_unit_regex(self) -> Pattern:
        return self._duration_relative_duration_unit_regex

    @property
    def unit_map(self) -> Dict[str, int]:
        return self._unit_map

    @property
    def cardinal_map(self) -> Dict[str, int]:
        return self._cardinal_map

    @property
    def day_of_month(self) -> Dict[str, int]:
        return self._day_of_month

    @property
    def season_map(self) -> Dict[str, int]:
        return self._season_map

    @property
    def ago_regex(self) -> Pattern:
        return self._ago_regex

    @property
    def all_half_year_regex(self) -> Pattern:
        return self._all_half_year_regex

    @property
    def between_regex(self) -> Pattern:
        return self._between_regex

    @property
    def check_both_before_after(self) -> Pattern:
        return self._check_both_before_after

    @property
    def complex_dateperiod_regex(self) -> Pattern:
        return self._complex_dateperiod_regex

    @property
    def decade_with_century_regex(self) -> Pattern:
        return self._decade_with_century_regex

    @property
    def duration_extractor(self):
        return self._duration_extractor

    @property
    def duration_parser(self):
        raise NotImplementedError

    @property
    def later_regex(self) -> Pattern:
        return self._later_regex

    @property
    def in_connector_regex(self) -> Pattern:
        return self._in_connector_regex

    @property
    def less_than_regex(self) -> Pattern:
        return self._less_than_regex

    @property
    def month_front_between_regex(self) -> Pattern:
        return self._month_front_between_regex

    @property
    def month_front_simple_cases_regex(self) -> Pattern:
        return self._month_front_simple_cases_regex

    @property
    def month_num_with_year(self) -> Pattern:
        return self._month_num_with_year

    @property
    def month_of_regex(self) -> Pattern:
        return self._month_of_regex

    @property
    def month_of_year(self) -> Pattern:
        return self._month_of_year

    @property
    def month_with_year(self) -> Pattern:
        return self._month_with_year

    @property
    def now_regex(self) -> Pattern:
        return self._now_regex

    @property
    def quarter_regex_year_front(self) -> Pattern:
        return self._quarter_regex_year_front

    @property
    def rest_of_date_regex(self) -> Pattern:
        return self._rest_of_date_regex

    @property
    def token_before_date(self) -> str:
        return self._token_before_date

    @property
    def unspecific_end_of_range_regex(self) -> Pattern:
        return self._unspecific_end_of_range_regex

    @property
    def week_of_regex(self) -> Pattern:
        return self._week_of_regex

    def __init__(self):
        self._integer_extractor = JapaneseIntegerExtractor()
        self._number_parser = CJKNumberParser(JapaneseNumberParserConfiguration())
        self._date_extractor = JapaneseDateExtractor()
        self._cardinal_extractor = JapaneseCardinalExtractor()
        self._date_parser = JapaneseDateParser()

        self._dynasty_year_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.DynastyYearRegex)
        self._dynasty_start_year = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.DynastyStartYear)
        self._dynasty_year_map = JapaneseDateTime.DynastyYearMap
        self._simple_cases_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.SimpleCasesRegex)
        self._this_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.DateThisRegex)
        self._next_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.DateNextRegex)
        self._wom_previous_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.WoMPreviousRegex)
        self._wom_next_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.WoMNextRegex)
        self._wom_last_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.WoMLastRegex)
        self._next_prefix_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.NextPrefixRegex)
        self._after_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.AfterRegex)
        self._last_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.DateLastRegex)
        self._next_month_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.ParserConfigurationNextMonthRegex)
        self._after_next_month_regex = RegExpUtility.get_safe_reg_exp(
            JapaneseDateTime.ParserConfigurationAfterNextMonthRegex)
        self._last_month_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.ParserConfigurationLastMonthRegex)
        self._next_year_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.ParserConfigurationNextYearRegex)
        self._after_next_year_regex = RegExpUtility.get_safe_reg_exp(
            JapaneseDateTime.ParserConfigurationAfterNextYearRegex)
        self._last_year_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.ParserConfigurationLastYearRegex)
        self._this_year_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.ParserConfigurationThisYearRegex)

        self._year_to_year = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.YearToYear)
        self._year_to_year_suffix_required = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.YearToYearSuffixRequired)
        self._year_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.YearRegex)
        self._year_cjk_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.DateYearInCJKRegex)
        self._month_to_month_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.MonthToMonth)
        self._month_to_month_regex_suffix_required = RegExpUtility.get_safe_reg_exp(
            JapaneseDateTime.MonthToMonthSuffixRequired)
        self._day_to_day = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.DayToDay)
        self._month_day_range_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.MonthDayRange)
        self._day_regex_for_period = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.DayRegexForPeriod)
        self._month_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.MonthRegex)
        self._special_month_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.SpecialMonthRegex)
        self._special_year_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.SpecialYearRegex)
        self._year_and_month = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.YearAndMonth)
        self._pure_num_year_and_month = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.PureNumYearAndMonth)
        self._simple_year_and_month = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.SimpleYearAndMonth)
        self._one_word_period_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.OneWordPeriodRegex)
        self._number_combined_with_unit = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.NumberCombinedWithUnit)
        self._past_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.PastRegex)
        self._future_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.FutureRegex)
        self._week_with_week_day_range_regex = RegExpUtility.get_safe_reg_exp(
            JapaneseDateTime.WeekWithWeekDayRangeRegex)
        self._unit_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.UnitRegex)
        self._duration_unit_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.DurationUnitRegex)
        self._week_of_month_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.WeekOfMonthRegex)
        self._week_of_year_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.WeekOfYearRegex)
        self._week_of_date_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.WeekOfDateRegex)
        self._month_of_date_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.MonthOfDateRegex)
        self._which_week_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.WhichWeekRegex)
        self._first_last_of_year_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.FirstLastOfYearRegex)
        self._season_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.SeasonRegex)
        self._quarter_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.QuarterRegex)
        self._decade_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.DecadeRegex)
        self._century_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.CenturyRegex)
        self._relative_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.RelativeRegex)
        self._relative_month_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.RelativeMonthRegex)
        self._later_early_period_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.LaterEarlyPeriodRegex)
        self._date_period_with_ago_and_later = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.DatePointWithAgoAndLater)
        self._reference_date_period_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.ReferenceDatePeriodRegex)
        self._complex_date_period_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.ComplexDatePeriodRegex)
        self._duration_relative_duration_unit_regex = RegExpUtility.get_safe_reg_exp(
            JapaneseDateTime.DurationRelativeDurationUnitRegex)
        self._now_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.NowRegex)
        self._unit_map = JapaneseDateTime.ParserConfigurationUnitMap
        self._cardinal_map = JapaneseDateTime.ParserConfigurationCardinalMap
        self._day_of_month = JapaneseDateTime.ParserConfigurationDayOfMonth
        self._season_map = JapaneseDateTime.ParserConfigurationSeasonMap
        self._token_before_date = ' on '
        self._all_half_year_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.HalfYearRegex)
        self._complex_dateperiod_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.ComplexDatePeriodRegex)
        self._month_of_year = JapaneseDateTime.ParserConfigurationMonthOfYear
        self._rest_of_date_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.RestOfDateRegex)


        # TODO When the implementation for these properties is added, change the None values to their respective Regexps

        self._decade_with_century_regex = None
        self._later_regex = None
        self._ago_regex = None
        self._check_both_before_after = None
        self._relative_decade_regex = None
        self._between_regex = None
        self._duration_extractor = None
        self._duration_parser = None
        self._in_connector_regex = None
        self._less_than_regex = None
        self._month_front_between_regex = None
        self._month_front_simple_cases_regex = None
        self._month_num_with_year = None
        self._month_of_regex = None
        self._month_with_year = None
        self._quarter_regex_year_front = None
        self._unspecific_end_of_range_regex = None
        self._week_of_regex = None

    def is_month_only(self, source: str) -> bool:
        trimmed_source = source.strip().lower()
        return any(trimmed_source.endswith(o) for o in JapaneseDateTime.MonthTerms)

    def is_weekend(self, source: str) -> bool:
        trimmed_source = source.strip().lower()
        return any(trimmed_source.endswith(o) for o in JapaneseDateTime.WeekendTerms)

    def is_week_only(self, source: str) -> bool:
        trimmed_source = source.strip().lower()
        return any(trimmed_source.endswith(o) for o in JapaneseDateTime.WeekTerms)

    def is_year_only(self, source: str) -> bool:
        trimmed_source = source.strip().lower()
        return any(trimmed_source.endswith(o) for o in JapaneseDateTime.YearTerms)

    def is_this_year(self, source: str) -> bool:
        trimmed_source = source.strip().lower()
        return any(trimmed_source == o for o in JapaneseDateTime.ThisYearTerms)

    def is_year_to_date(self, source: str) -> bool:
        trimmed_source = source.strip().lower()
        return any(trimmed_source == o for o in JapaneseDateTime.YearToDateTerms)

    def is_month_to_date(self, source: str) -> bool:
        trimmed_source = source.strip().lower()
        return any(trimmed_source == o for o in JapaneseDateTime.MonthToDateTerms)

    def is_last_year(self, source: str) -> bool:
        trimmed_source = source.strip().lower()
        return any(trimmed_source == o for o in JapaneseDateTime.LastYearTerms)

    def is_next_year(self, source: str) -> bool:
        trimmed_source = source.strip().lower()
        return any(trimmed_source == o for o in JapaneseDateTime.NextYearTerms)

    def is_year_after_next(self, source: str) -> bool:
        trimmed_source = source.strip().lower()
        return any(trimmed_source == o for o in JapaneseDateTime.YearAfterNextTerms)

    def is_year_before_last(self, source: str) -> bool:
        trimmed_source = source.strip().lower()
        return any(trimmed_source == o for o in JapaneseDateTime.YearBeforeLastTerms)

    def get_swift_day_or_month(self, source: str) -> int:
        source = source.strip().lower()
        if self._next_prefix_regex.search(source):
            return 1
        if self._after_regex.search(source):
            return 2
        if self._last_regex.search(source):
            return -1
        if self._next_regex.search(source):
            return 1
        return 0

    def get_swift_month(self, source: str) -> int:
        value = 0

        if self.next_month_regex.search(source):
            value = 1
        elif self.last_month_regex.search(source):
            value = -1
        elif self.after_next_month_regex.search(source):
            value = 2

        return value

    def get_swift_year(self, source: str) -> int:
        value = 0

        if self.after_next_year_regex.search(source):
            value = 2
        elif self.next_year_regex.search(source):
            value = 1
        elif self._last_year_regex.search(source):
            value = -1
        elif self.this_year_regex.search(source):
            value = 0

        return value

    def is_future(self, source) -> bool:
        return not self.this_regex.search(source) or self.next_regex.search(source) is None

    def is_last_cardinal(self, source) -> bool:
        trimmed_source = source.strip().lower()
        return not self.last_regex.search(trimmed_source) is None
