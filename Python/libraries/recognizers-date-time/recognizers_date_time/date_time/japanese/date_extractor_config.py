#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from typing import List, Pattern, Dict

from recognizers_text import RegExpUtility
from recognizers_number import JapaneseIntegerExtractor, JapaneseOrdinalExtractor, CJKNumberParser, \
    JapaneseNumberParserConfiguration
from ...resources import JapaneseDateTime
from ..base_date import DateExtractorConfiguration
from ...resources.base_date_time import BaseDateTime


class JapaneseDateExtractorConfiguration(DateExtractorConfiguration):

    @property
    def integer_extractor(self) -> JapaneseIntegerExtractor:
        return self._integer_extractor

    @property
    def ordinal_extractor(self) -> JapaneseOrdinalExtractor:
        return self._ordinal_extractor

    @property
    def duration_extractor(self):
        raise NotImplementedError

    @property
    def number_parser(self) -> CJKNumberParser:
        return self._number_parser

    @property
    def week_day_regex(self) -> Pattern:
        return self._week_day_regex

    @property
    def lunar_regex(self) -> Pattern:
        return self._lunar_regex

    @property
    def this_regex(self) -> Pattern:
        return self._this_regex

    @property
    def last_regex(self) -> Pattern:
        return self._last_regex

    @property
    def next_regex(self) -> Pattern:
        return self._next_regex

    @property
    def special_day_regex(self) -> Pattern:
        return self._special_day_regex

    @property
    def week_day_of_month_regex(self) -> Pattern:
        return self._week_day_of_month

    @property
    def special_date_regex(self) -> Pattern:
        return self._special_date_regex

    @property
    def special_day_with_num_regex(self) -> Pattern:
        return self._special_day_with_num_regex

    @property
    def before_regex(self) -> Pattern:
        return self._before_regex

    @property
    def after_regex(self) -> Pattern:
        return self._after_regex

    @property
    def week_day_start_end_regex(self) -> Pattern:
        return self._week_day_start_end_regex

    @property
    def datetime_period_unit_regex(self) -> Pattern:
        return self._datetime_period_unit_regex

    @property
    def range_connector_symbol_regex(self) -> Pattern:
        return self._range_connector_symbol_regex

    @property
    def month_regex(self) -> Pattern:
        return self._month_regex

    @property
    def day_regex(self):
        return self._day_regex

    @property
    def date_day_regex_in_cjk(self) -> Pattern:
        return self._date_day_regex_in_CJK

    @property
    def day_regex_num_in_cjk(self) -> Pattern:
        return self._day_regex_num_in_CJK

    @property
    def month_num_regex(self) -> Pattern:
        return self._month_num_regex

    @property
    def week_day_and_day_regex(self) -> Pattern:
        return self._week_day_and_day_regex

    @property
    def duration_relative_duration_unit_regex(self):
        return self._duration_relative_duration_unit_regex

    @property
    def year_regex(self) -> Pattern:
        return self._year_regex

    @property
    def relative_regex(self) -> Pattern:
        return self._relative_regex

    @property
    def relative_month_regex(self) -> Pattern:
        return self._relative_month_regex

    @property
    def zero_to_nine_integer_regex_cjk(self) -> Pattern:
        return self._zero_to_nine_integer_regex_cjk

    @property
    def date_year_in_cjk_regex(self) -> Pattern:
        return self._date_year_in_cjk_regex

    @property
    def this_prefix_regex(self) -> Pattern:
        return self._this_prefix_regex

    @property
    def last_prefix_regex(self) -> Pattern:
        return self._last_prefix_regex

    @property
    def next_prefix_regex(self) -> Pattern:
        return self._next_prefix_regex

    @property
    def date_unit_regex(self) -> Pattern:
        return self._date_unit_regex

    @property
    def dynasty_year_regex(self):
        return self._dynasty_year_regex

    @property
    def dynasty_start_year_regex(self):
        return self._dynasty_start_year_regex

    @property
    def date_regex_list(self) -> List[Pattern]:
        return self._date_regex_list

    @property
    def implicit_date_list(self) -> List[Pattern]:
        return self._implicit_date_list

    @property
    def prefix_article_regex(self) -> Pattern:
        return self._prefix_article_regex

    @property
    def month_of_year(self) -> Dict[str, int]:
        return self._month_of_year

    @property
    def year_suffix(self) -> Pattern:
        return self._year_suffix

    @property
    def more_than_regex(self) -> Pattern:
        return self._more_than_regex

    @property
    def less_than_regex(self) -> Pattern:
        return self._less_than_regex

    @property
    def in_connector_regex(self) -> Pattern:
        return self._in_connector_regex

    @property
    def range_unit_regex(self) -> Pattern:
        return self._range_unit_regex

    @property
    def since_year_suffix_regex(self) -> Pattern:
        return self._since_year_suffix_regex

    @property
    def day_of_week(self) -> Pattern:
        return self._day_of_week

    @property
    def check_both_before_after(self) -> bool:
        return self._check_both_before_after

    @property
    def week_day_start(self) -> Pattern:
        return self._week_day_start

    @property
    def week_day_end(self) -> Pattern:
        return self._week_day_end

    @property
    def week_day_and_day_of_month_regex(self) -> Pattern:
        return self._week_day_and_day_of_month_regex

    @property
    def utility_configuration(self) -> Pattern:
        return self._utility_configuration

    @property
    def strict_relative_regex(self) -> Pattern:
        return self._strict_relative_regex

    @property
    def of_month(self) -> Pattern:
        return self._of_month

    @property
    def month_end(self) -> Pattern:
        return self._month_end

    @property
    def for_the_regex(self) -> Pattern:
        return self._for_the_regex

    def __init__(self):
        self._integer_extractor = JapaneseIntegerExtractor()
        self._ordinal_extractor = JapaneseOrdinalExtractor()
        self._number_parser = CJKNumberParser(JapaneseNumberParserConfiguration())

        self._week_day_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.WeekDayRegex)
        self._lunar_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.LunarRegex)
        self._this_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.DateThisRegex)
        self._last_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.DateLastRegex)
        self._next_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.DateNextRegex)
        self._special_day_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.SpecialDayRegex)
        self._week_day_of_month = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.WeekDayOfMonthRegex)
        self._special_date_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.SpecialDate)
        self._special_day_with_num_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.SpecialDayWithNumRegex)
        self._before_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.BeforeRegex)
        self._after_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.AfterRegex)
        self._week_day_start_end_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.WeekDayStartEnd)
        self._datetime_period_unit_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.DateTimePeriodUnitRegex)
        self._range_connector_symbol_regex = RegExpUtility.get_safe_reg_exp(BaseDateTime.RangeConnectorSymbolRegex)
        self._month_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.MonthRegex)
        self._day_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.DayRegex)
        self._date_day_regex_in_CJK = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.DateDayRegexInCJK)
        self._day_regex_num_in_CJK = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.DayRegexNumInCJK)
        self._month_num_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.MonthNumRegex)
        self._week_day_and_day_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.WeekDayAndDayRegex)
        self._duration_relative_duration_unit_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.DurationRelativeDurationUnitRegex)
        self._year_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.YearRegex)
        self._relative_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.RelativeRegex)
        self._relative_month_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.RelativeMonthRegex)
        self._zero_to_nine_integer_regex_cjk = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.ZeroToNineIntegerRegexCJK)
        self._date_year_in_cjk_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.DateYearInCJKRegex)
        self._this_prefix_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.ThisPrefixRegex)
        self._last_prefix_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.LastPrefixRegex)
        self._next_prefix_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.NextPrefixRegex)
        self._date_unit_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.UnitRegex)
        self._dynasty_year_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.DynastyYearRegex)
        self._dynasty_start_year_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.DynastyStartYear)
        self._day_of_week = JapaneseDateTime.ParserConfigurationDayOfWeek
        self._month_of_year = JapaneseDateTime.ParserConfigurationMonthOfYear

        self._date_regex_list = [
            RegExpUtility.get_safe_reg_exp(JapaneseDateTime.DateRegexList1),
            RegExpUtility.get_safe_reg_exp(JapaneseDateTime.DateRegexList2),
            RegExpUtility.get_safe_reg_exp(JapaneseDateTime.DateRegexList3),
            RegExpUtility.get_safe_reg_exp(JapaneseDateTime.DateRegexList4),
            RegExpUtility.get_safe_reg_exp(JapaneseDateTime.DateRegexList5),
            RegExpUtility.get_safe_reg_exp(JapaneseDateTime.DateRegexList6),
            RegExpUtility.get_safe_reg_exp(JapaneseDateTime.DateRegexList7),
            RegExpUtility.get_safe_reg_exp(JapaneseDateTime.DateRegexList8),
            RegExpUtility.get_safe_reg_exp(JapaneseDateTime.DateRegexList9),
            RegExpUtility.get_safe_reg_exp(JapaneseDateTime.DateRegexList10)
        ]
        self._implicit_date_list = [
            RegExpUtility.get_safe_reg_exp(JapaneseDateTime.SpecialDayWithNumRegex),
            RegExpUtility.get_safe_reg_exp(JapaneseDateTime.SpecialDayRegex),
            RegExpUtility.get_safe_reg_exp(JapaneseDateTime.DateThisRegex),
            RegExpUtility.get_safe_reg_exp(JapaneseDateTime.DateLastRegex),
            RegExpUtility.get_safe_reg_exp(JapaneseDateTime.DateNextRegex),
            RegExpUtility.get_safe_reg_exp(JapaneseDateTime.WeekDayRegex),
            RegExpUtility.get_safe_reg_exp(JapaneseDateTime.WeekDayOfMonthRegex),
            RegExpUtility.get_safe_reg_exp(JapaneseDateTime.SpecialDate),
            RegExpUtility.get_safe_reg_exp(JapaneseDateTime.WeekDayAndDayRegex)
        ]

        self._check_both_before_after = False

        # TODO When the implementation for these properties is added, change the None values to their respective Regexps
        self._since_year_suffix_regex = None
        self._range_unit_regex = None
        self._in_connector_regex = None
        self._less_than_regex = None
        self._more_than_regex = None
        self._year_suffix = None
        self._prefix_article_regex = None
        self._week_day_start = None
        self._week_day_end = None
        self._duration_extractor = None
        self._week_day_and_day_of_month_regex = None
        self._utility_configuration = None
        self._strict_relative_regex = None
        self._of_month = None
        self._month_end = None
        self._for_the_regex = None

