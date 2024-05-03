#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from typing import List, Pattern, Dict

from recognizers_text import RegExpUtility
from recognizers_number import BaseNumberExtractor, BaseNumberParser
from ...resources import ChineseDateTime
from ..constants import Constants
from ..extractors import DateTimeExtractor
from ..base_date import DateTimeUtilityConfiguration
from ..base_date import DateExtractorConfiguration
from ...resources.base_date_time import BaseDateTime


class ChineseDateExtractorConfiguration(DateExtractorConfiguration):

    ordinal_extractor: BaseNumberExtractor = None
    integer_extractor: BaseNumberExtractor = None
    number_parser: BaseNumberParser = None
    duration_extractor: DateTimeExtractor = None
    utility_configuration: DateTimeUtilityConfiguration = None
    check_both_before_after: bool = None

    day_of_week: Dict[str, int] = {}
    month_of_year: Dict[str, int] = {}

    range_connector_symbol_regex: Pattern = RegExpUtility.get_safe_reg_exp(BaseDateTime.RangeConnectorSymbolRegex)
    week_day_start: Pattern = None
    week_day_end: Pattern = None
    month_end: Pattern = None
    of_month: Pattern = None
    for_the_regex: Pattern = None
    week_day_and_day_of_month_regex: Pattern = None
    relative_month_regex: Pattern = None
    week_day_regex: Pattern = None
    since_year_suffix_regex: Pattern = None
    range_unit_regex: Pattern = None
    in_connector_regex: Pattern = None
    less_than_regex: Pattern = None
    more_than_regex: Pattern = None
    year_suffix: Pattern = None
    prefix_article_regex: Pattern = None
    week_day_and_day_regex: Pattern = None
    strict_relative_regex: Pattern = None

    datetime_period_unit_regex: Pattern = RegExpUtility.get_safe_reg_exp( ChineseDateTime.DateTimePeriodUnitRegex )
    after_regex: Pattern = RegExpUtility.get_safe_reg_exp( ChineseDateTime.AfterRegex )
    before_regex: Pattern = RegExpUtility.get_safe_reg_exp( ChineseDateTime.BeforeRegex )
    date_unit_regex: Pattern = RegExpUtility.get_safe_reg_exp( ChineseDateTime.UnitRegex )
    next_prefix_regex: Pattern = RegExpUtility.get_safe_reg_exp( ChineseDateTime.NextPrefixRegex )
    last_prefix_regex: Pattern = RegExpUtility.get_safe_reg_exp( ChineseDateTime.LastPrefixRegex )
    this_prefix_regex: Pattern = RegExpUtility.get_safe_reg_exp( ChineseDateTime.ThisPrefixRegex )
    date_year_in_chinese_regex: Pattern = RegExpUtility.get_safe_reg_exp( ChineseDateTime.DateYearInCJKRegex )
    zero_to_nine_integer_regex_chinese: Pattern = RegExpUtility.get_safe_reg_exp( ChineseDateTime.ZeroToNineIntegerRegexCJK )
    relative_regex: Pattern = RegExpUtility.get_safe_reg_exp( ChineseDateTime.RelativeRegex )
    year_regex: Pattern = RegExpUtility.get_safe_reg_exp( ChineseDateTime.YearRegex )
    month_num_regex: Pattern = RegExpUtility.get_safe_reg_exp( ChineseDateTime.MonthNumRegex )
    day_regex_num_in_chinese: Pattern = RegExpUtility.get_safe_reg_exp( ChineseDateTime.DayRegexNumInCJK )
    date_day_regex_in_chinese: Pattern = RegExpUtility.get_safe_reg_exp( ChineseDateTime.DateDayRegexInCJK )
    day_regex: Pattern = RegExpUtility.get_safe_reg_exp( ChineseDateTime.DayRegex )
    month_regex: Pattern = RegExpUtility.get_safe_reg_exp( ChineseDateTime.MonthRegex )

    implicit_date_list: List[Pattern] = [
        RegExpUtility.get_safe_reg_exp(ChineseDateTime.LunarRegex),
        RegExpUtility.get_safe_reg_exp(ChineseDateTime.SpecialDayRegex),
        RegExpUtility.get_safe_reg_exp(ChineseDateTime.DateThisRegex),
        RegExpUtility.get_safe_reg_exp(ChineseDateTime.DateLastRegex),
        RegExpUtility.get_safe_reg_exp(ChineseDateTime.DateNextRegex),
        RegExpUtility.get_safe_reg_exp(ChineseDateTime.WeekDayRegex),
        RegExpUtility.get_safe_reg_exp(ChineseDateTime.WeekDayOfMonthRegex),
        RegExpUtility.get_safe_reg_exp(ChineseDateTime.SpecialDate)
    ]

    @property
    def date_regex_list(self) -> List[Pattern]:
        return [
            RegExpUtility.get_safe_reg_exp(ChineseDateTime.DateRegexList1),
            RegExpUtility.get_safe_reg_exp(ChineseDateTime.DateRegexList2),
            RegExpUtility.get_safe_reg_exp(ChineseDateTime.DateRegexList3),
            RegExpUtility.get_safe_reg_exp(ChineseDateTime.DateRegexList4),
            RegExpUtility.get_safe_reg_exp(ChineseDateTime.DateRegexList5),
            RegExpUtility.get_safe_reg_exp(ChineseDateTime.DateRegexList6),
            RegExpUtility.get_safe_reg_exp(ChineseDateTime.DateRegexList7),
            RegExpUtility.get_safe_reg_exp(ChineseDateTime.DateRegexList8)
        ]
