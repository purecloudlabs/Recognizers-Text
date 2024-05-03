#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from typing import Pattern, List, Dict
from recognizers_number import (BaseNumberExtractor, BaseNumberParser,
                                GermanOrdinalExtractor, GermanIntegerExtractor, GermanNumberParserConfiguration)
from recognizers_text.utilities import RegExpUtility
from ...resources.german_date_time import GermanDateTime
from ..extractors import DateTimeExtractor
from ..base_duration import BaseDurationExtractor
from ..base_date import DateExtractorConfiguration
from ..utilities import DateTimeUtilityConfiguration
from .duration_extractor_config import GermanDurationExtractorConfiguration
from .base_configs import GermanDateTimeUtilityConfiguration
from ..constants import Constants
from ...resources.base_date_time import BaseDateTime


class GermanDateExtractorConfiguration(DateExtractorConfiguration):

    ordinal_extractor: BaseNumberExtractor = GermanOrdinalExtractor()
    integer_extractor: BaseNumberExtractor = GermanIntegerExtractor()
    number_parser: BaseNumberParser = BaseNumberParser(GermanNumberParserConfiguration())
    duration_extractor: BaseDurationExtractor = BaseDurationExtractor(GermanDurationExtractorConfiguration())
    utility_configuration: DateTimeUtilityConfiguration = GermanDateTimeUtilityConfiguration()
    check_both_before_after: bool = GermanDateTime.CheckBothBeforeAfter

    day_of_week: Dict[str, int] = GermanDateTime.DayOfWeek
    month_of_year: Dict[str, int] = GermanDateTime.MonthOfYear

    month_end: Pattern = RegExpUtility.get_safe_reg_exp(GermanDateTime.MonthEnd)
    of_month: Pattern = RegExpUtility.get_safe_reg_exp(GermanDateTime.OfMonth)
    date_unit_regex: Pattern = RegExpUtility.get_safe_reg_exp(GermanDateTime.DateUnitRegex)
    for_the_regex: Pattern = RegExpUtility.get_safe_reg_exp(GermanDateTime.ForTheRegex)
    week_day_and_day_of_month_regex: Pattern = RegExpUtility.get_safe_reg_exp(GermanDateTime.WeekDayAndDayOfMonthRegex)
    relative_month_regex: Pattern = RegExpUtility.get_safe_reg_exp(GermanDateTime.RelativeMonthRegex)
    week_day_regex: Pattern = RegExpUtility.get_safe_reg_exp(GermanDateTime.WeekDayRegex)
    range_connector_symbol_regex: Pattern = RegExpUtility.get_safe_reg_exp(BaseDateTime.RangeConnectorSymbolRegex)
    strict_relative_regex: Pattern = RegExpUtility.get_safe_reg_exp(GermanDateTime.StrictRelativeRegex)
    year_suffix: Pattern = RegExpUtility.get_safe_reg_exp(GermanDateTime.YearSuffix)
    prefix_article_regex: Pattern = RegExpUtility.get_safe_reg_exp(GermanDateTime.PrefixArticleRegex)
    week_day_end: Pattern = RegExpUtility.get_safe_reg_exp(GermanDateTime.WeekDayEnd)
    more_than_regex: Pattern = RegExpUtility.get_safe_reg_exp(GermanDateTime.MoreThanRegex)
    less_than_regex: Pattern = RegExpUtility.get_safe_reg_exp(GermanDateTime.LessThanRegex)
    in_connector_regex: Pattern = RegExpUtility.get_safe_reg_exp(GermanDateTime.InConnectorRegex)
    range_unit_regex: Pattern = RegExpUtility.get_safe_reg_exp(GermanDateTime.RangeUnitRegex)
    since_year_suffix_regex: Pattern = RegExpUtility.get_safe_reg_exp(GermanDateTime.SinceYearSuffixRegex)
    week_day_and_day_regex: Pattern = RegExpUtility.get_safe_reg_exp(GermanDateTime.WeekDayAndDayRegex)
    week_day_start: Pattern = RegExpUtility.get_safe_reg_exp(GermanDateTime.WeekDayStart)

    implicit_date_list: List[Pattern] = [
        RegExpUtility.get_safe_reg_exp(GermanDateTime.OnRegex),
        RegExpUtility.get_safe_reg_exp(GermanDateTime.RelaxedOnRegex),
        RegExpUtility.get_safe_reg_exp(GermanDateTime.SpecialDayRegex),
        RegExpUtility.get_safe_reg_exp(GermanDateTime.ThisRegex),
        RegExpUtility.get_safe_reg_exp(GermanDateTime.LastDateRegex),
        RegExpUtility.get_safe_reg_exp(GermanDateTime.NextDateRegex),
        RegExpUtility.get_safe_reg_exp(GermanDateTime.SingleWeekDayRegex),
        RegExpUtility.get_safe_reg_exp(GermanDateTime.WeekDayOfMonthRegex),
        RegExpUtility.get_safe_reg_exp(GermanDateTime.SpecialDate),
    ]

    @property
    def date_regex_list(self) -> List[Pattern]:
        if GermanDateTime.DefaultLanguageFallback == Constants.DEFAULT_LANGUAGE_FALLBACK_DMY:
            date_extractor_4 = GermanDateTime.DateExtractor5
            date_extractor_5 = GermanDateTime.DateExtractor4
            date_extractor_6 = GermanDateTime.DateExtractor7
            date_extractor_7 = GermanDateTime.DateExtractor6
        else:
            date_extractor_4 = GermanDateTime.DateExtractor4
            date_extractor_5 = GermanDateTime.DateExtractor5
            date_extractor_6 = GermanDateTime.DateExtractor6
            date_extractor_7 = GermanDateTime.DateExtractor7

        return [
            RegExpUtility.get_safe_reg_exp(GermanDateTime.DateExtractor1),
            RegExpUtility.get_safe_reg_exp(GermanDateTime.DateExtractor2),
            RegExpUtility.get_safe_reg_exp(GermanDateTime.DateExtractor3),
            RegExpUtility.get_safe_reg_exp(date_extractor_4),
            RegExpUtility.get_safe_reg_exp(date_extractor_5),
            RegExpUtility.get_safe_reg_exp(date_extractor_6),
            RegExpUtility.get_safe_reg_exp(date_extractor_7),
            RegExpUtility.get_safe_reg_exp(GermanDateTime.DateExtractor8),
            RegExpUtility.get_safe_reg_exp(GermanDateTime.DateExtractor9),
            RegExpUtility.get_safe_reg_exp(GermanDateTime.DateExtractorA),
        ]

