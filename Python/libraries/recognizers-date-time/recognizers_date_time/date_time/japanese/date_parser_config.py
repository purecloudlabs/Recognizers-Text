#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from typing import List, Pattern, Dict

from recognizers_text import RegExpUtility, Extractor, Parser
from recognizers_number import CJKNumberParser, JapaneseIntegerExtractor, JapaneseNumberParserConfiguration, \
    JapaneseOrdinalExtractor, JapaneseCardinalExtractor
from .date_extractor_config import JapaneseDateExtractorConfiguration

from ...resources.japanese_date_time import JapaneseDateTime
from ..constants import Constants
from ..base_date import DateParserConfiguration


class JapaneseDateParserConfiguration(DateParserConfiguration):

    @property
    def plus_one_day_regex(self) -> Pattern:
        return self._plus_one_day_regex

    @property
    def minus_one_day_regex(self) -> Pattern:
        return self._minus_one_day_regex

    @property
    def plus_two_day_regex(self) -> Pattern:
        return self._plus_two_day_regex

    @property
    def minus_two_day_regex(self) -> Pattern:
        return self._minus_two_day_regex

    @property
    def plus_three_day_regex(self) -> Pattern:
        return self._plus_three_day_regex

    @property
    def minus_three_day_regex(self) -> Pattern:
        return self._minus_three_day_regex

    @property
    def plus_four_day_regex(self) -> Pattern:
        return self._plus_four_day_regex

    @property
    def next_month_regex(self) -> Pattern:
        return self._next_month_regex

    @property
    def last_month_regex(self) -> Pattern:
        return self._last_month_regex

    @property
    def last_week_day_regex(self) -> Pattern:
        return self._last_week_day_regex

    @property
    def date_regex(self) -> List[Pattern]:
        return self._date_regex

    @property
    def special_date_regex(self) -> Pattern:
        return self._special_date_regex

    @property
    def special_day_regex(self) -> Pattern:
        return self._special_day_regex

    @property
    def week_day_regex(self) -> Pattern:
        return self._week_day_regex

    @property
    def lunar_regex(self) -> Pattern:
        return self._lunar_regex

    @property
    def unit_regex(self) -> Pattern:
        return self._unit_regex

    @property
    def before_regex(self) -> Pattern:
        return self._before_regex

    @property
    def after_regex(self) -> Pattern:
        return self._after_regex

    @property
    def dynasty_start_year(self) -> Pattern:
        return self._dynasty_start_year

    @property
    def dynasty_year_regex(self) -> Pattern:
        return self._dynasty_year_regex

    @property
    def dynasty_year_map(self) -> Dict[str, int]:
        return self._dynasty_year_map

    @property
    def next_regex(self) -> Pattern:
        return self._next_regex

    @property
    def this_regex(self) -> Pattern:
        return self._this_regex

    @property
    def last_regex(self) -> Pattern:
        return self._last_regex

    @property
    def week_day_of_month_regex(self) -> any:
        return self._week_day_of_month_regex

    @property
    def week_day_and_day_regex(self) -> Pattern:
        return self._week_day_and_day_regex

    @property
    def duration_relative_duration_unit_regex(self) -> Pattern:
        return self._duration_relative_duration_unit_regex

    @property
    def special_day_with_num_regex(self) -> Pattern:
        return self._special_day_with_num_regex

    @property
    def cardinal_map(self) -> Dict[str, int]:
        return self._cardinal_map

    @property
    def unit_map(self) -> Dict[str, int]:
        return self._unit_map

    @property
    def day_of_month(self) -> Dict[str, int]:
        return self._day_of_month

    @property
    def day_of_week(self) -> Dict[str, int]:
        return self._day_of_week

    @property
    def month_of_year(self) -> Dict[str, int]:
        return self._month_of_year

    @property
    def ordinal_extractor(self) -> Extractor:
        return self._ordinal_extractor

    @property
    def integer_extractor(self) -> Extractor:
        return self._integer_extractor

    @property
    def cardinal_extractor(self) -> Extractor:
        return self._cardinal_extractor

    @property
    def date_extractor(self) -> JapaneseDateExtractorConfiguration:
        return self._date_extractor

    @property
    def duration_extractor(self) -> any:
        return None

    @property
    def number_parser(self) -> Parser:
        return self._number_parser

    @property
    def duration_parser(self) -> any:
        return None

    @property
    def on_regex(self) -> any:
        return None

    @property
    def month_regex(self) -> any:
        return None

    @property
    def for_the_regex(self) -> any:
        return None

    @property
    def relative_month_regex(self) -> any:
        return None

    @property
    def relative_week_day_regex(self) -> any:
        return None

    @property
    def utility_configuration(self) -> any:
        return None

    @property
    def date_token_prefix(self) -> any:
        return None

    @property
    def check_both_before_after(self) -> any:
        return self._check_both_before_after

    @property
    def week_day_and_day_of_month_regex(self) -> any:
        return self._week_day_and_day_of_month_regex

    def get_swift_day(self, source: str) -> int:
        source = source.strip().lower()
        swift = 0
        if self.plus_one_day_regex.search(source):
            swift = 1
        elif self.minus_one_day_regex.search(source):
            swift = -1
        elif self.plus_three_day_regex.search(source):
            swift = 3
        elif self.plus_four_day_regex.search(source):
            swift = 4
        elif self.minus_three_day_regex.search(source):
            swift = -3
        elif self.plus_two_day_regex.search(source):
            swift = 2
        elif self.minus_two_day_regex.search(source):
            swift = -2
        return swift

    def get_swift_month(self, source: str) -> int:
        source = source.strip().lower()
        swift = 0
        if source.startswith(JapaneseDateTime.ParserConfigurationNextMonthRegex):
            swift = 1
        elif source.startswith(JapaneseDateTime.ParserConfigurationLastMonthRegex):
            swift = -1
        return swift

    def is_cardinal_last(self, source: str) -> bool:
        return source == JapaneseDateTime.ParserConfigurationLastWeekDayRegex

    def __init__(self):
        self._plus_one_day_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.PlusOneDayRegex)
        self._minus_one_day_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.MinusOneDayRegex)
        self._plus_two_day_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.PlusTwoDayRegex)
        self._minus_two_day_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.MinusTwoDayRegex)
        self._plus_three_day_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.PlusThreeDayRegex)
        self._minus_three_day_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.MinusThreeDayRegex)
        self._plus_four_day_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.PlusFourDayRegex)
        self._next_month_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.ParserConfigurationNextMonthRegex)
        self._last_month_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.ParserConfigurationLastMonthRegex)
        self._last_week_day_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.ParserConfigurationLastWeekDayRegex)

        self._integer_extractor = JapaneseIntegerExtractor()
        self._ordinal_extractor = JapaneseOrdinalExtractor()
        self._cardinal_extractor = JapaneseCardinalExtractor()
        self._number_parser = CJKNumberParser(JapaneseNumberParserConfiguration())
        self._date_extractor = JapaneseDateExtractorConfiguration()

        self._date_regex = (JapaneseDateExtractorConfiguration()).date_regex_list
        self._special_date_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.SpecialDate)
        self._special_day_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.SpecialDayRegex)
        self._week_day_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.WeekDayRegex)
        self._lunar_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.LunarRegex)
        self._unit_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.DateUnitRegex)
        self._before_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.BeforeRegex)
        self._after_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.AfterRegex)
        self._dynasty_start_year = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.DynastyStartYear)
        self._dynasty_year_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.DynastyYearRegex)
        self._dynasty_year_map = JapaneseDateTime.DynastyYearMap
        self._next_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.DateNextRegex)
        self._this_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.DateThisRegex)
        self._last_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.DateLastRegex)
        self._week_day_of_month_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.WeekDayOfMonthRegex)
        self._week_day_and_day_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.WeekDayAndDayRegex)
        self._duration_relative_duration_unit_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.DurationRelativeDurationUnitRegex)
        self._special_day_with_num_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.SpecialDayWithNumRegex)

        self._cardinal_map = JapaneseDateTime.ParserConfigurationCardinalMap
        self._unit_map = JapaneseDateTime.ParserConfigurationUnitMap
        self._day_of_month = JapaneseDateTime.ParserConfigurationDayOfMonth
        self._day_of_week = JapaneseDateTime.ParserConfigurationDayOfWeek
        self._month_of_year = JapaneseDateTime.ParserConfigurationMonthOfYear

        # Regex precedence where the order between D and M varies is controlled by DefaultLanguageFallback
        if JapaneseDateTime.DefaultLanguageFallback == Constants.DEFAULT_LANGUAGE_FALLBACK_DMY:
            order_regex_list = [JapaneseDateTime.DateRegexList5, JapaneseDateTime.DateRegexList4]
        else:
            order_regex_list = [JapaneseDateTime.DateRegexList4, JapaneseDateTime.DateRegexList5]

        if JapaneseDateTime.DefaultLanguageFallback in [Constants.DEFAULT_LANGUAGE_FALLBACK_DMY,
                                                        Constants.DEFAULT_LANGUAGE_FALLBACK_YMD]:
            order_regex_list.extend([JapaneseDateTime.DateRegexList7, JapaneseDateTime.DateRegexList6])
        else:
            order_regex_list.extend([JapaneseDateTime.DateRegexList6, JapaneseDateTime.DateRegexList7])
        self._date_regex.extend([RegExpUtility.get_safe_reg_exp(ii) for ii in order_regex_list])

        # TODO When the implementation for these properties is added, change the None values to their respective Regexps
        self._check_both_before_after = None
        self._week_day_and_day_of_month_regex = None
