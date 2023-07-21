#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from typing import Pattern, List, Dict
from recognizers_number import (BaseNumberExtractor, BaseNumberParser,
                                CatalanOrdinalExtractor, CatalanIntegerExtractor, CatalanNumberParserConfiguration)
from recognizers_text.utilities import RegExpUtility
from ...resources.catalan_date_time import CatalanDateTime
from ..extractors import DateTimeExtractor
from ..base_duration import BaseDurationExtractor
from ..base_date import DateExtractorConfiguration
from ..utilities import DateTimeUtilityConfiguration
from .duration_extractor_config import CatalanDurationExtractorConfiguration
from .base_configs import CatalanDateTimeUtilityConfiguration
from ...resources.base_date_time import BaseDateTime


class CatalanDateExtractorConfiguration(DateExtractorConfiguration):
    @property
    def week_day_start(self) -> Pattern:
        return self._week_day_start

    @property
    def check_both_before_after(self) -> Pattern:
        return self._check_both_before_after

    @property
    def date_regex_list(self) -> List[Pattern]:
        return self._date_regex_list

    @property
    def implicit_date_list(self) -> List[Pattern]:
        return self._implicit_date_list

    @property
    def month_end(self) -> Pattern:
        return self._month_end

    @property
    def week_day_end(self) -> Pattern:
        return self._week_day_end

    @property
    def week_day_start(self) -> Pattern:
        return self._week_day_start

    @property
    def of_month(self) -> Pattern:
        return self._of_month

    @property
    def date_unit_regex(self) -> Pattern:
        return self._date_unit_regex

    @property
    def for_the_regex(self) -> Pattern:
        return self._for_the_regex

    @property
    def week_day_and_day_of_month_regex(self) -> Pattern:
        return self._week_day_and_day_of_month_regex

    @property
    def relative_month_regex(self) -> Pattern:
        return self._relative_month_regex

    @property
    def week_day_regex(self) -> Pattern:
        return self._week_day_regex

    @property
    def prefix_article_regex(self) -> Pattern:
        return self._prefix_article_regex

    @property
    def day_of_week(self) -> Dict[str, int]:
        return self._day_of_week

    @property
    def month_of_year(self) -> Dict[str, int]:
        return self._month_of_year

    @property
    def ordinal_extractor(self) -> BaseNumberExtractor:
        return self._ordinal_extractor

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
    def strict_relative_regex(self) -> Pattern:
        return self._strict_relative_regex

    @property
    def range_connector_symbol_regex(self) -> Pattern:
        return self._range_connector_symbol_regex

    @property
    def utility_configuration(self) -> DateTimeUtilityConfiguration:
        return self._utility_configuration

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
    def week_day_and_day_regex(self) -> Pattern:
        return self._week_day_and_day_regex

    @property
    def month_regex(self) -> Pattern:
        return self._month_regex

    @property
    def month_num_regex(self) -> Pattern:
        return self._month_num_regex

    @property
    def year_regex(self) -> Pattern:
        return self._year_regex

    @property
    def written_month_regex(self) -> Pattern:
        return self._written_month_regex

    @property
    def month_suffix_regex(self) -> Pattern:
        return self._month_suffix_regex

    def __init__(self, dmyDateFormat=False):
        self._check_both_before_after = CatalanDateTime.CheckBothBeforeAfter
        if dmyDateFormat:
            date_extractor_4 = CatalanDateTime.DateExtractor5
            date_extractor_5 = CatalanDateTime.DateExtractor8
            date_extractor_6 = CatalanDateTime.DateExtractor9L
            date_extractor_7 = CatalanDateTime.DateExtractor9S
            date_extractor_8 = CatalanDateTime.DateExtractor4
            date_extractor_9 = CatalanDateTime.DateExtractor6
            date_extractor_10 = CatalanDateTime.DateExtractor7L
            date_extractor_11 = CatalanDateTime.DateExtractor7S
        else:
            date_extractor_4 = CatalanDateTime.DateExtractor4
            date_extractor_5 = CatalanDateTime.DateExtractor6
            date_extractor_6 = CatalanDateTime.DateExtractor7L
            date_extractor_7 = CatalanDateTime.DateExtractor7S
            date_extractor_8 = CatalanDateTime.DateExtractor5
            date_extractor_9 = CatalanDateTime.DateExtractor8
            date_extractor_10 = CatalanDateTime.DateExtractor9L
            date_extractor_11 = CatalanDateTime.DateExtractor9S

        self._date_regex_list = [
            RegExpUtility.get_safe_reg_exp(CatalanDateTime.DateExtractor1),
            RegExpUtility.get_safe_reg_exp(CatalanDateTime.DateExtractor3),
            RegExpUtility.get_safe_reg_exp(date_extractor_4),
            RegExpUtility.get_safe_reg_exp(date_extractor_5),
            RegExpUtility.get_safe_reg_exp(date_extractor_6),
            RegExpUtility.get_safe_reg_exp(date_extractor_7),
            RegExpUtility.get_safe_reg_exp(date_extractor_8),
            RegExpUtility.get_safe_reg_exp(date_extractor_9),
            RegExpUtility.get_safe_reg_exp(date_extractor_10),
            RegExpUtility.get_safe_reg_exp(date_extractor_11),
            RegExpUtility.get_safe_reg_exp(CatalanDateTime.DateExtractorA),
        ]
        self._implicit_date_list = [
            RegExpUtility.get_safe_reg_exp(CatalanDateTime.OnRegex),
            RegExpUtility.get_safe_reg_exp(CatalanDateTime.RelaxedOnRegex),
            RegExpUtility.get_safe_reg_exp(CatalanDateTime.SpecialDayRegex),
            RegExpUtility.get_safe_reg_exp(CatalanDateTime.ThisRegex),
            RegExpUtility.get_safe_reg_exp(CatalanDateTime.LastDateRegex),
            RegExpUtility.get_safe_reg_exp(CatalanDateTime.NextDateRegex),
            RegExpUtility.get_safe_reg_exp(CatalanDateTime.SingleWeekDayRegex),
            RegExpUtility.get_safe_reg_exp(
                CatalanDateTime.WeekDayOfMonthRegex),
            RegExpUtility.get_safe_reg_exp(CatalanDateTime.SpecialDate),
            RegExpUtility.get_safe_reg_exp(CatalanDateTime.SpecialDayWithNumRegex),
            RegExpUtility.get_safe_reg_exp(CatalanDateTime.RelativeWeekDayRegex)
        ]
        self._month_end = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.MonthEnd)
        self._of_month = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.OfMonth)
        self._date_unit_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.DateUnitRegex)
        self._for_the_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.ForTheRegex)
        self._week_day_and_day_of_month_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.WeekDayAndDayOfMonthRegex)
        self._relative_month_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.RelativeMonthRegex)
        self._week_day_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.WeekDayRegex)
        self._day_of_week = CatalanDateTime.DayOfWeek
        self._ordinal_extractor = CatalanOrdinalExtractor()
        self._integer_extractor = CatalanIntegerExtractor()
        self._number_parser = BaseNumberParser(
            CatalanNumberParserConfiguration())
        self._duration_extractor = BaseDurationExtractor(
            CatalanDurationExtractorConfiguration())
        self._utility_configuration = CatalanDateTimeUtilityConfiguration()
        self._range_connector_symbol_regex = RegExpUtility.get_safe_reg_exp(
            BaseDateTime.RangeConnectorSymbolRegex
        )
        self._strict_relative_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.StrictRelativeRegex
        )
        self._year_suffix = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.YearSuffix
        )
        self._month_of_year = CatalanDateTime.MonthOfYear
        self._prefix_article_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.PrefixArticleRegex
        )
        self._week_day_end = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.WeekDayEnd
        )
        self._week_day_start = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.WeekDayStart
        )
        self._more_than_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.MoreThanRegex
        )
        self._less_than_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.LessThanRegex
        )
        self._in_connector_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.InConnectorRegex
        )
        self._range_unit_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.RangeUnitRegex
        )
        self._since_year_suffix_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.SinceYearSuffixRegex
        )
        self._week_day_and_day_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.WeekDayAndDayRegex
        )
        self._week_day_start = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.WeekDayStart
        )
        self._check_both_before_after = CatalanDateTime.CheckBothBeforeAfter

        self._month_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.MonthRegex
        )
        self._month_num_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.MonthNumRegex
        )
        self._year_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.YearRegex
        )
        self._day_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.DayRegex
        )
        self._written_month_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.WrittenMonthRegex
        )
        self._month_suffix_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.MonthSuffixRegex
        )
