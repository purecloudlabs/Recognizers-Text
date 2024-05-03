#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from typing import Pattern, List, Dict
from recognizers_number import (BaseNumberExtractor, BaseNumberParser,
                                EnglishOrdinalExtractor, EnglishIntegerExtractor, EnglishNumberParserConfiguration)
from recognizers_text.utilities import RegExpUtility
from ...resources.english_date_time import EnglishDateTime
from ..extractors import DateTimeExtractor
from ..base_duration import BaseDurationExtractor
from ..base_date import DateExtractorConfiguration
from ..utilities import DateTimeUtilityConfiguration
from .duration_extractor_config import EnglishDurationExtractorConfiguration
from .base_configs import EnglishDateTimeUtilityConfiguration
from ...resources.base_date_time import BaseDateTime


class EnglishDateExtractorConfiguration(DateExtractorConfiguration):

    ordinal_extractor: BaseNumberExtractor = EnglishOrdinalExtractor()
    integer_extractor: BaseNumberExtractor = EnglishIntegerExtractor()
    number_parser: BaseNumberParser = BaseNumberParser(EnglishNumberParserConfiguration())
    duration_extractor: DateTimeExtractor = BaseDurationExtractor(EnglishDurationExtractorConfiguration())
    utility_configuration: DateTimeUtilityConfiguration = EnglishDateTimeUtilityConfiguration()
    check_both_before_after: bool = EnglishDateTime.CheckBothBeforeAfter

    month_end: Pattern = RegExpUtility.get_safe_reg_exp(EnglishDateTime.MonthEnd)
    of_month: Pattern = RegExpUtility.get_safe_reg_exp(EnglishDateTime.OfMonth)
    date_unit_regex: Pattern = RegExpUtility.get_safe_reg_exp(EnglishDateTime.DateUnitRegex)
    for_the_regex: Pattern = RegExpUtility.get_safe_reg_exp(EnglishDateTime.ForTheRegex)
    week_day_and_day_of_month_regex: Pattern = RegExpUtility.get_safe_reg_exp(EnglishDateTime.WeekDayAndDayOfMonthRegex)
    relative_month_regex: Pattern = RegExpUtility.get_safe_reg_exp(EnglishDateTime.RelativeMonthRegex)
    week_day_regex: Pattern = RegExpUtility.get_safe_reg_exp(EnglishDateTime.WeekDayRegex)

    day_of_week: Dict[str, int] = EnglishDateTime.DayOfWeek
    month_of_year: Dict[str, int] = EnglishDateTime.MonthOfYear

    range_connector_symbol_regex: Pattern = RegExpUtility.get_safe_reg_exp(BaseDateTime.RangeConnectorSymbolRegex)
    strict_relative_regex: Pattern = RegExpUtility.get_safe_reg_exp(EnglishDateTime.StrictRelativeRegex)
    year_suffix: Pattern = RegExpUtility.get_safe_reg_exp(EnglishDateTime.YearSuffix)
    prefix_article_regex: Pattern = RegExpUtility.get_safe_reg_exp(EnglishDateTime.PrefixArticleRegex)
    week_day_end: Pattern = RegExpUtility.get_safe_reg_exp(EnglishDateTime.WeekDayEnd)
    week_day_start: Pattern = RegExpUtility.get_safe_reg_exp(EnglishDateTime.WeekDayStart)
    more_than_regex: Pattern = RegExpUtility.get_safe_reg_exp(EnglishDateTime.MoreThanRegex)
    less_than_regex: Pattern = RegExpUtility.get_safe_reg_exp(EnglishDateTime.LessThanRegex)
    in_connector_regex: Pattern = RegExpUtility.get_safe_reg_exp(EnglishDateTime.InConnectorRegex)
    range_unit_regex: Pattern = RegExpUtility.get_safe_reg_exp(EnglishDateTime.RangeUnitRegex)
    since_year_suffix_regex: Pattern = RegExpUtility.get_safe_reg_exp(EnglishDateTime.SinceYearSuffixRegex)
    week_day_and_day_regex: Pattern = RegExpUtility.get_safe_reg_exp(EnglishDateTime.WeekDayAndDayRegex)
    month_regex: Pattern = RegExpUtility.get_safe_reg_exp(EnglishDateTime.MonthRegex)
    month_num_regex: Pattern = RegExpUtility.get_safe_reg_exp(EnglishDateTime.MonthNumRegex)
    year_regex: Pattern = RegExpUtility.get_safe_reg_exp(EnglishDateTime.YearRegex)
    day_regex: Pattern = RegExpUtility.get_safe_reg_exp(EnglishDateTime.DayRegex)
    written_month_regex: Pattern = RegExpUtility.get_safe_reg_exp(EnglishDateTime.WrittenMonthRegex)
    month_suffix_regex: Pattern = RegExpUtility.get_safe_reg_exp(EnglishDateTime.MonthSuffixRegex)

    implicit_date_list: List[Pattern] = [
        RegExpUtility.get_safe_reg_exp(EnglishDateTime.OnRegex),
        RegExpUtility.get_safe_reg_exp(EnglishDateTime.RelaxedOnRegex),
        RegExpUtility.get_safe_reg_exp(EnglishDateTime.SpecialDayRegex),
        RegExpUtility.get_safe_reg_exp(EnglishDateTime.ThisRegex),
        RegExpUtility.get_safe_reg_exp(EnglishDateTime.LastDateRegex),
        RegExpUtility.get_safe_reg_exp(EnglishDateTime.NextDateRegex),
        RegExpUtility.get_safe_reg_exp(EnglishDateTime.SingleWeekDayRegex),
        RegExpUtility.get_safe_reg_exp(EnglishDateTime.WeekDayOfMonthRegex),
        RegExpUtility.get_safe_reg_exp(EnglishDateTime.SpecialDate),
        RegExpUtility.get_safe_reg_exp(EnglishDateTime.SpecialDayWithNumRegex),
        RegExpUtility.get_safe_reg_exp(EnglishDateTime.RelativeWeekDayRegex)
    ]

    @property
    def date_regex_list(self) -> List[Pattern]:
        if self._dmy_date_format:
            date_extractor_4 = EnglishDateTime.DateExtractor5
            date_extractor_5 = EnglishDateTime.DateExtractor8
            date_extractor_6 = EnglishDateTime.DateExtractor9L
            date_extractor_7 = EnglishDateTime.DateExtractor9S
            date_extractor_8 = EnglishDateTime.DateExtractor4
            date_extractor_9 = EnglishDateTime.DateExtractor6
            date_extractor_10 = EnglishDateTime.DateExtractor7L
            date_extractor_11 = EnglishDateTime.DateExtractor7S
        else:
            date_extractor_4 = EnglishDateTime.DateExtractor4
            date_extractor_5 = EnglishDateTime.DateExtractor6
            date_extractor_6 = EnglishDateTime.DateExtractor7L
            date_extractor_7 = EnglishDateTime.DateExtractor7S
            date_extractor_8 = EnglishDateTime.DateExtractor5
            date_extractor_9 = EnglishDateTime.DateExtractor8
            date_extractor_10 = EnglishDateTime.DateExtractor9L
            date_extractor_11 = EnglishDateTime.DateExtractor9S

        return [
            RegExpUtility.get_safe_reg_exp(EnglishDateTime.DateExtractor1),
            RegExpUtility.get_safe_reg_exp(EnglishDateTime.DateExtractor3),
            RegExpUtility.get_safe_reg_exp(date_extractor_4),
            RegExpUtility.get_safe_reg_exp(date_extractor_5),
            RegExpUtility.get_safe_reg_exp(date_extractor_6),
            RegExpUtility.get_safe_reg_exp(date_extractor_7),
            RegExpUtility.get_safe_reg_exp(date_extractor_8),
            RegExpUtility.get_safe_reg_exp(date_extractor_9),
            RegExpUtility.get_safe_reg_exp(date_extractor_10),
            RegExpUtility.get_safe_reg_exp(date_extractor_11),
            RegExpUtility.get_safe_reg_exp(EnglishDateTime.DateExtractorA),
        ]

    def __init__(self, dmyDateFormat: bool = False):
        self._dmy_date_format = dmyDateFormat
