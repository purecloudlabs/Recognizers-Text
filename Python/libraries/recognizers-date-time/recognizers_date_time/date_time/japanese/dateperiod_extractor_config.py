#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from typing import List, Pattern, Dict

from recognizers_text import Extractor, Parser, RegExpUtility
from recognizers_number import JapaneseNumberExtractor, JapaneseNumberParserConfiguration, BaseNumberParser, \
    JapaneseCardinalExtractor, JapaneseOrdinalExtractor
from .date_extractor_config import JapaneseDateExtractorConfiguration
from ..CJK.base_date import BaseCJKDateExtractor
from ..CJK.base_dateperiod import CJKDatePeriodExtractorConfiguration
from ...resources.base_date_time import BaseDateTime
from ...resources.japanese_date_time import JapaneseDateTime
from ..extractors import DateTimeExtractor
from ..base_dateperiod import MatchedIndex


class JapaneseDatePeriodExtractorConfiguration(CJKDatePeriodExtractorConfiguration):

    @property
    def till_regex(self) -> Pattern:
        return self._till_regex

    @property
    def range_prefix_regex(self) -> Pattern:
        return self._range_prefix_regex

    @property
    def range_suffix_regex(self) -> Pattern:
        return self._range_suffix_regex

    @property
    def strict_year_regex(self) -> Pattern:
        return self._strict_year_regex

    @property
    def year_in_cjk_regex(self) -> Pattern:
        return self._year_in_cjk_regex

    @property
    def simple_cases_regex(self) -> Pattern:
        return self._simple_cases_regex

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
    def week_of_month_regex(self) -> Pattern:
        return self._week_of_month_regex

    @property
    def week_of_year_regex(self) -> Pattern:
        return self._week_of_year_regex

    @property
    def week_of_date_regex(self) -> Pattern:
        return self._week_of_date_regex

    @property
    def month_of_year_regex(self) -> Pattern:
        return self._month_of_year_regex

    @property
    def which_week_regex(self) -> Pattern:
        return self._which_week_regex

    @property
    def followed_unit(self) -> Pattern:
        return self._followed_unit

    @property
    def number_combined_with_unit(self) -> Pattern:
        return self._number_combined_with_unit

    @property
    def year_to_year_regex(self) -> Pattern:
        return self._year_to_year_regex

    @property
    def year_to_year_suffix_required_regex(self) -> Pattern:
        return self._year_to_year_suffix_required_regex

    @property
    def month_to_month_regex(self) -> Pattern:
        return self._month_to_month_regex

    @property
    def month_to_month_suffix_required_regex(self) -> Pattern:
        return self._month_to_month_suffix_required_regex

    @property
    def day_to_day_regex(self) -> Pattern:
        return self._day_to_day_regex

    @property
    def day_regex_for_period(self) -> Pattern:
        return self._day_regex_for_period

    @property
    def month_day_regex(self) -> Pattern:
        return self._month_day_regex

    @property
    def year_month_range(self) -> Pattern:
        return self._year_month_range

    @property
    def year_month_day_range(self) -> Pattern:
        return self._year_month_day_range

    @property
    def past_regex(self) -> Pattern:
        return self._past_regex

    @property
    def future_regex(self) -> Pattern:
        return self._future_regex

    @property
    def week_with_weekday_range_regex(self) -> Pattern:
        return self._week_with_weekday_range_regex

    @property
    def first_last_of_year_regex(self) -> Pattern:
        return self._first_last_of_year_regex

    @property
    def season_with_year_regex(self) -> Pattern:
        return self._season_with_year_regex

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
    def special_month_regex(self) -> Pattern:
        return self._special_month_regex

    @property
    def special_year_regex(self) -> Pattern:
        return self._special_year_regex

    @property
    def day_regex(self) -> Pattern:
        return self._day_regex

    @property
    def day_regex_in_cjk(self) -> Pattern:
        return self._day_regex_in_cjk

    @property
    def month_num_regex(self) -> Pattern:
        return self._month_num_regex

    @property
    def this_regex(self) -> Pattern:
        return self._this_regex

    @property
    def date_unit_regex(self) -> Pattern:
        return self._date_unit_regex

    @property
    def last_regex(self) -> Pattern:
        return self._last_regex

    @property
    def next_regex(self) -> Pattern:
        return self._next_regex

    @property
    def relative_month_regex(self) -> Pattern:
        return self._relative_month_regex

    @property
    def later_early_period_regex(self) -> Pattern:
        return self._later_early_period_regex

    @property
    def date_point_with_ago_and_later(self) -> Pattern:
        return self._date_point_with_ago_and_later

    @property
    def reference_date_period_regex(self) -> Pattern:
        return self._reference_date_period_regex

    @property
    def complex_date_period_regex(self) -> Pattern:
        return self._complex_date_period_regex

    @property
    def month_regex(self) -> Pattern:
        return self._month_regex

    @property
    def year_regex(self) -> Pattern:
        return self._year_regex

    @property
    def year_regex_in_number(self) -> Pattern:
        return self._year_regex_in_number

    @property
    def zero_to_nine_integer_regex_cjk(self) -> Pattern:
        return self._zero_to_nine_integer_regex_cjk

    @property
    def month_suffix_regex(self) -> Pattern:
        return self._month_suffix_regex

    @property
    def unit_regex(self) -> Pattern:
        return self._unit_regex

    @property
    def duration_unit_regex(self) -> Pattern:
        return self._duration_unit_regex

    @property
    def season_regex(self):
        return self._season_regex

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
    def duration_extractor(self):
        raise NotImplementedError

    @property
    def within_next_prefix_regex(self) -> Pattern:
        return self._within_next_prefix_regex

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
    def year_period_regex(self) -> Pattern:
        return self._year_period_regex

    @property
    def century_suffix_regex(self) -> Pattern:
        return self._century_suffix_regex

    @property
    def simple_cases_regexes(self) -> List[Pattern]:
        return self._simple_cases_regexes

    @property
    def date_point_extractor(self) -> DateTimeExtractor:
        return self._date_point_extractor

    @property
    def integer_extractor(self) -> Extractor:
        return self._integer_extractor

    @property
    def number_parser(self) -> Parser:
        return self._number_parser

    @property
    def now_regex(self) -> Pattern:
        return self._now_regex

    @property
    def illegal_year_regex(self) -> Pattern:
        return self._illegal_year_regex

    @property
    def in_connector_regex(self) -> Pattern:
        return self._in_connector_regex

    @property
    def month_of_regex(self) -> Pattern:
        return self._month_of_regex

    @property
    def previous_prefix_regex(self) -> Pattern:
        return self._previous_prefix_regex

    @property
    def range_unit_regex(self) -> Pattern:
        return self._range_unit_regex

    @property
    def week_of_regex(self) -> Pattern:
        return self._week_of_regex

    @property
    def zhijian_regex(self) -> Pattern:
        return self._zhijian_regex

    @property
    def ambiguity_filters_dict(self) -> Dict[Pattern, Pattern]:
        return self._ambiguity_filters_dict

    def __init__(self):
        super().__init__()
        self._till_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.DatePeriodTillRegex)
        self._range_prefix_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.DatePeriodRangePrefixRegex)
        self._range_suffix_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.DatePeriodRangeSuffixRegex)
        self._strict_year_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.StrictYearRegex)
        self._year_in_cjk_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.DatePeriodYearInCJKRegex)
        self._simple_cases_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.SimpleCasesRegex),
        self._year_and_month = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.YearAndMonth)
        self._pure_num_year_and_month = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.PureNumYearAndMonth)
        self._simple_year_and_month = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.SimpleYearAndMonth)
        self._one_word_period_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.OneWordPeriodRegex)
        self._week_of_month_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.WeekOfMonthRegex)
        self._week_of_year_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.WeekOfYearRegex)
        self._week_of_date_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.WeekOfDateRegex)
        self._month_of_year_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.MonthOfDateRegex)
        self._which_week_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.WhichWeekRegex)
        self._followed_unit = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.FollowedUnit)
        self._number_combined_with_unit = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.NumberCombinedWithUnit)
        self._year_to_year_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.YearToYear)
        self._year_to_year_suffix_required_regex = RegExpUtility.get_safe_reg_exp(
            JapaneseDateTime.YearToYearSuffixRequired)
        self._month_to_month_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.MonthToMonth)
        self._month_to_month_suffix_required_regex = RegExpUtility.get_safe_reg_exp(
            JapaneseDateTime.MonthToMonthSuffixRequired)
        self._day_to_day_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.DayToDay)
        self._day_regex_for_period = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.DayRegexForPeriod)
        self._month_day_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.MonthDayRange)
        self._year_month_range = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.YearMonthRange)
        self._year_month_day_range = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.YearMonthDayRange)
        self._past_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.PastRegex)
        self._future_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.FutureRegex)
        self._week_with_weekday_range_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.WeekWithWeekDayRangeRegex)
        self._first_last_of_year_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.WeekWithWeekDayRangeRegex)
        self._season_with_year_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.SeasonWithYear)
        self._quarter_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.QuarterRegex)
        self._decade_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.DecadeRegex)
        self._century_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.CenturyRegex)
        self._special_month_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.SpecialMonthRegex)
        self._special_year_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.SpecialYearRegex)

        self._day_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.DayRegex)
        self._day_regex_in_cjk = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.DatePeriodDayRegexInCJK)
        self._month_num_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.MonthNumRegex)
        self._this_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.DatePeriodThisRegex)
        self._date_unit_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.DateUnitRegex)
        self._last_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.DatePeriodLastRegex)
        self._next_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.DatePeriodNextRegex)
        self._relative_month_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.RelativeMonthRegex)
        self._later_early_period_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.LaterEarlyPeriodRegex)
        self._date_point_with_ago_and_later = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.DatePointWithAgoAndLater)
        self._reference_date_period_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.ReferenceDatePeriodRegex)
        self._complex_date_period_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.ComplexDatePeriodRegex)
        self._month_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.MonthRegex)
        self._year_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.YearRegex)
        self._year_regex_in_number = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.YearRegexInNumber)
        self._zero_to_nine_integer_regex_cjk = RegExpUtility.get_safe_reg_exp(
            JapaneseDateTime.ZeroToNineIntegerRegexCJK)
        self._month_suffix_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.MonthSuffixRegex)
        self._unit_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.UnitRegex)
        self._duration_unit_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.DurationUnitRegex)
        self._season_regex = JapaneseDateTime.SeasonRegex
        self._from_prefix = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.DateTimePeriodFromPrefixRegex)
        self._from_suffix = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.DateTimePeriodFromSuffixRegex)
        self._zhijian_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.ZhijianRegex)

        self._simple_cases_regexes = [
            RegExpUtility.get_safe_reg_exp(JapaneseDateTime.SimpleCasesRegex),
            RegExpUtility.get_safe_reg_exp(JapaneseDateTime.OneWordPeriodRegex),
            RegExpUtility.get_safe_reg_exp(JapaneseDateTime.StrictYearRegex),
            RegExpUtility.get_safe_reg_exp(JapaneseDateTime.YearToYear),
            RegExpUtility.get_safe_reg_exp(JapaneseDateTime.YearToYearSuffixRequired),
            RegExpUtility.get_safe_reg_exp(JapaneseDateTime.MonthToMonth),
            RegExpUtility.get_safe_reg_exp(JapaneseDateTime.DayToDay),
            RegExpUtility.get_safe_reg_exp(JapaneseDateTime.YearMonthRange),
            RegExpUtility.get_safe_reg_exp(JapaneseDateTime.MonthDayRange),
            RegExpUtility.get_safe_reg_exp(JapaneseDateTime.YearMonthDayRange),
            RegExpUtility.get_safe_reg_exp(JapaneseDateTime.MonthToMonthSuffixRequired),
            RegExpUtility.get_safe_reg_exp(JapaneseDateTime.YearAndMonth),
            RegExpUtility.get_safe_reg_exp(JapaneseDateTime.PureNumYearAndMonth),
            RegExpUtility.get_safe_reg_exp(JapaneseDateTime.DatePeriodYearInCJKRegex),
            RegExpUtility.get_safe_reg_exp(JapaneseDateTime.SpecialMonthRegex),
            RegExpUtility.get_safe_reg_exp(JapaneseDateTime.SpecialYearRegex),
            RegExpUtility.get_safe_reg_exp(JapaneseDateTime.WeekOfMonthRegex),
            RegExpUtility.get_safe_reg_exp(JapaneseDateTime.WeekOfYearRegex),
            RegExpUtility.get_safe_reg_exp(JapaneseDateTime.WeekOfDateRegex),
            RegExpUtility.get_safe_reg_exp(JapaneseDateTime.MonthOfDateRegex),
            RegExpUtility.get_safe_reg_exp(JapaneseDateTime.WhichWeekRegex),
            RegExpUtility.get_safe_reg_exp(JapaneseDateTime.LaterEarlyPeriodRegex),
            RegExpUtility.get_safe_reg_exp(JapaneseDateTime.SeasonWithYear),
            RegExpUtility.get_safe_reg_exp(JapaneseDateTime.QuarterRegex),
            RegExpUtility.get_safe_reg_exp(JapaneseDateTime.DecadeRegex),
            RegExpUtility.get_safe_reg_exp(JapaneseDateTime.CenturyRegex),
            RegExpUtility.get_safe_reg_exp(JapaneseDateTime.ReferenceDatePeriodRegex),
            RegExpUtility.get_safe_reg_exp(JapaneseDateTime.DatePointWithAgoAndLater)
        ]
        self._date_point_extractor = BaseCJKDateExtractor(JapaneseDateExtractorConfiguration())
        self._integer_extractor = JapaneseNumberExtractor()
        self._cardinal_extractor = JapaneseCardinalExtractor()
        self._ordinal_extractor = JapaneseOrdinalExtractor()

        self._number_parser = BaseNumberParser(JapaneseNumberParserConfiguration())
        self._now_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.NowRegex)
        self._ambiguity_filters_dict = JapaneseDateTime.AmbiguityFiltersDict

        # TODO When the implementation for these properties is added, change the None values to their respective Regexps
        self._previous_prefix_regex = None
        self._check_both_before_after = None
        self._century_suffix_regex = None
        self._year_period_regex = None
        self._duration_date_restrictions = None
        self._more_than_regex = None
        self._less_than_regex = None
        self._later_regex = None
        self._ago_regex = None
        self._future_suffix_regex = None
        self._within_next_prefix_regex = None
        self._time_unit_regex = None

        self._illegal_year_regex = RegExpUtility.get_safe_reg_exp(BaseDateTime.IllegalYearRegex)
        self._in_connector_regex = None
        self._month_of_regex = None
        self._previous_prefix_regex = None
        self._range_unit_regex = None
        self._week_of_regex = None

        self._duration_extractor = None

    def get_between_token_index(self, source : str) -> MatchedIndex:
        match = self.zhijian_regex.match(source)
        if match and match.success:
            index = match.length
            return MatchedIndex(True, index)
        return MatchedIndex(False, -1)

    def get_from_token_index(self, source: str) -> MatchedIndex:

        match = RegExpUtility.match_end(self._from_prefix, source, trim=True)
        if match and match.success:
            return MatchedIndex(True, match.start())
        else:
            match = RegExpUtility.match_begin(self._from_suffix, source, trim=True)
        if match:
            return MatchedIndex(True, match.start() + match.length())

        return MatchedIndex(False, -1)

    def has_connector_token(self, source: str) -> bool:
        return RegExpUtility.is_exact_match(self._in_connector_regex, source, trim=True)
