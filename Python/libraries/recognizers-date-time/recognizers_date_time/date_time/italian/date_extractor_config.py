#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from typing import Pattern, List, Dict
from recognizers_number import (BaseNumberExtractor, BaseNumberParser,
                                ItalianOrdinalExtractor, ItalianIntegerExtractor, ItalianNumberParserConfiguration)
from recognizers_text.utilities import RegExpUtility
from ...resources.italian_date_time import ItalianDateTime
from ..extractors import DateTimeExtractor
from ..base_duration import BaseDurationExtractor
from ..base_date import DateExtractorConfiguration
from ..utilities import DateTimeUtilityConfiguration
from .duration_extractor_config import ItalianDurationExtractorConfiguration
from .base_configs import ItalianDateTimeUtilityConfiguration
from ..constants import Constants
from ...resources.base_date_time import BaseDateTime
from ..utilities import DateTimeOptions


class ItalianDateExtractorConfiguration(DateExtractorConfiguration):

    ordinal_extractor: BaseNumberExtractor = ItalianOrdinalExtractor()
    integer_extractor: BaseNumberExtractor = ItalianIntegerExtractor()
    number_parser: BaseNumberParser = BaseNumberParser(ItalianNumberParserConfiguration())
    duration_extractor = BaseDurationExtractor(ItalianDurationExtractorConfiguration())
    utility_configuration: DateTimeUtilityConfiguration = ItalianDateTimeUtilityConfiguration()
    check_both_before_after: bool = ItalianDateTime.CheckBothBeforeAfter

    month_of_year: Dict[str, int] = ItalianDateTime.MonthOfYear
    day_of_week: Dict[str, int] = ItalianDateTime.DayOfWeek

    month_end: Pattern = RegExpUtility.get_safe_reg_exp(ItalianDateTime.MonthEnd)
    of_month: Pattern = RegExpUtility.get_safe_reg_exp(ItalianDateTime.OfMonth)
    date_unit_regex: Pattern = RegExpUtility.get_safe_reg_exp(ItalianDateTime.DateUnitRegex)
    for_the_regex: Pattern = RegExpUtility.get_safe_reg_exp(ItalianDateTime.ForTheRegex)
    week_day_and_day_of_month_regex: Pattern = RegExpUtility.get_safe_reg_exp(ItalianDateTime.WeekDayAndDayOfMonthRegex)
    relative_month_regex: Pattern = RegExpUtility.get_safe_reg_exp(ItalianDateTime.RelativeMonthRegex)
    week_day_regex: Pattern = RegExpUtility.get_safe_reg_exp(ItalianDateTime.WeekDayRegex)
    range_connector_symbol_regex: Pattern = RegExpUtility.get_safe_reg_exp(BaseDateTime.RangeConnectorSymbolRegex)
    strict_relative_regex: Pattern = RegExpUtility.get_safe_reg_exp(ItalianDateTime.StrictRelativeRegex)
    year_suffix: Pattern = RegExpUtility.get_safe_reg_exp(ItalianDateTime.YearSuffix)
    prefix_article_regex: Pattern = RegExpUtility.get_safe_reg_exp(ItalianDateTime.PrefixArticleRegex)
    week_day_end: Pattern = RegExpUtility.get_safe_reg_exp(ItalianDateTime.WeekDayEnd)
    more_than_regex: Pattern = RegExpUtility.get_safe_reg_exp(ItalianDateTime.MoreThanRegex)
    less_than_regex: Pattern = RegExpUtility.get_safe_reg_exp(ItalianDateTime.LessThanRegex)
    in_connector_regex: Pattern = RegExpUtility.get_safe_reg_exp(ItalianDateTime.InConnectorRegex)
    range_unit_regex: Pattern = RegExpUtility.get_safe_reg_exp(ItalianDateTime.RangeUnitRegex)
    since_year_suffix_regex: Pattern = RegExpUtility.get_safe_reg_exp(ItalianDateTime.SinceYearSuffixRegex)
    week_day_and_day_regex: Pattern = RegExpUtility.get_safe_reg_exp(ItalianDateTime.WeekDayAndDayRegex)
    week_day_start: Pattern = RegExpUtility.get_safe_reg_exp(ItalianDateTime.WeekDayStart)

    implicit_date_list: List[Pattern] = [
        RegExpUtility.get_safe_reg_exp(ItalianDateTime.OnRegex),
        RegExpUtility.get_safe_reg_exp(ItalianDateTime.RelaxedOnRegex),
        RegExpUtility.get_safe_reg_exp(ItalianDateTime.SpecialDayRegex),
        RegExpUtility.get_safe_reg_exp(ItalianDateTime.ThisRegex),
        RegExpUtility.get_safe_reg_exp(ItalianDateTime.LastDateRegex),
        RegExpUtility.get_safe_reg_exp(ItalianDateTime.NextDateRegex),
        RegExpUtility.get_safe_reg_exp(ItalianDateTime.StrictWeekDay),
        RegExpUtility.get_safe_reg_exp(ItalianDateTime.WeekDayOfMonthRegex),
        RegExpUtility.get_safe_reg_exp(ItalianDateTime.SpecialDate),
    ]

    @property
    def date_regex_list(self) -> List[Pattern]:
        if ItalianDateTime.DefaultLanguageFallback == Constants.DEFAULT_LANGUAGE_FALLBACK_DMY:
            date_extractor_4 = ItalianDateTime.DateExtractor5
            date_extractor_5 = ItalianDateTime.DateExtractor4
            date_extractor_6 = ItalianDateTime.DateExtractor7
            date_extractor_7 = ItalianDateTime.DateExtractor6
        else:
            date_extractor_4 = ItalianDateTime.DateExtractor4
            date_extractor_5 = ItalianDateTime.DateExtractor5
            date_extractor_6 = ItalianDateTime.DateExtractor6
            date_extractor_7 = ItalianDateTime.DateExtractor7

        return [
            RegExpUtility.get_safe_reg_exp(ItalianDateTime.DateExtractor1),
            RegExpUtility.get_safe_reg_exp(ItalianDateTime.DateExtractor2),
            RegExpUtility.get_safe_reg_exp(ItalianDateTime.DateExtractor3),
            RegExpUtility.get_safe_reg_exp(date_extractor_4),
            RegExpUtility.get_safe_reg_exp(date_extractor_5),
            RegExpUtility.get_safe_reg_exp(date_extractor_6),
            RegExpUtility.get_safe_reg_exp(date_extractor_7),
            RegExpUtility.get_safe_reg_exp(ItalianDateTime.DateExtractor8),
            RegExpUtility.get_safe_reg_exp(ItalianDateTime.DateExtractor9),
            RegExpUtility.get_safe_reg_exp(ItalianDateTime.DateExtractorA),
        ]

