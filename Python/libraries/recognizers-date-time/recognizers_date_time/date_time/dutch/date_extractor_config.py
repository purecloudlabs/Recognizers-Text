#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from typing import Pattern, List, Dict
from recognizers_number import (BaseNumberExtractor, BaseNumberParser,
                                DutchOrdinalExtractor, DutchIntegerExtractor, DutchNumberParserConfiguration)
from recognizers_text.utilities import RegExpUtility
from ...resources.dutch_date_time import DutchDateTime
from ..extractors import DateTimeExtractor
from ..base_duration import BaseDurationExtractor
from ..base_date import DateExtractorConfiguration
from ..utilities import DateTimeUtilityConfiguration
from .duration_extractor_config import DutchDurationExtractorConfiguration
from .base_configs import DutchDateTimeUtilityConfiguration
from ..constants import Constants
from ...resources.base_date_time import BaseDateTime


class DutchDateExtractorConfiguration(DateExtractorConfiguration):

    ordinal_extractor: BaseNumberExtractor = DutchOrdinalExtractor()
    integer_extractor: BaseNumberExtractor = DutchIntegerExtractor()
    number_parser: BaseNumberParser = BaseNumberParser(DutchNumberParserConfiguration())
    duration_extractor: DateTimeExtractor = BaseDurationExtractor(DutchDurationExtractorConfiguration())
    utility_configuration: DateTimeUtilityConfiguration = DutchDateTimeUtilityConfiguration()
    check_both_before_after: bool = DutchDateTime.CheckBothBeforeAfter

    day_of_week: Dict[str, int] = DutchDateTime.DayOfWeek
    month_of_year: Dict[str, int] = DutchDateTime.MonthOfYear

    implicit_date_list: List[Pattern] = [
        RegExpUtility.get_safe_reg_exp(DutchDateTime.OnRegex),
        RegExpUtility.get_safe_reg_exp(DutchDateTime.RelaxedOnRegex),
        RegExpUtility.get_safe_reg_exp(DutchDateTime.SpecialDayRegex),
        RegExpUtility.get_safe_reg_exp(DutchDateTime.ThisRegex),
        RegExpUtility.get_safe_reg_exp(DutchDateTime.LastDateRegex),
        RegExpUtility.get_safe_reg_exp(DutchDateTime.NextDateRegex),
        RegExpUtility.get_safe_reg_exp(DutchDateTime.SingleWeekDayRegex),
        RegExpUtility.get_safe_reg_exp(DutchDateTime.WeekDayOfMonthRegex),
        RegExpUtility.get_safe_reg_exp(DutchDateTime.SpecialDate),
        RegExpUtility.get_safe_reg_exp(DutchDateTime.SpecialDayWithNumRegex),
        RegExpUtility.get_safe_reg_exp(DutchDateTime.RelativeWeekDayRegex),
    ]
    month_end: Pattern = RegExpUtility.get_safe_reg_exp( DutchDateTime.MonthEnd)
    of_month: Pattern = RegExpUtility.get_safe_reg_exp(DutchDateTime.OfMonth)
    date_unit_regex: Pattern = RegExpUtility.get_safe_reg_exp( DutchDateTime.DateUnitRegex)
    for_the_regex: Pattern = RegExpUtility.get_safe_reg_exp( DutchDateTime.ForTheRegex)
    week_day_and_day_of_month_regex: Pattern = RegExpUtility.get_safe_reg_exp( DutchDateTime.WeekDayAndDayOfMonthRegex)
    relative_month_regex: Pattern = RegExpUtility.get_safe_reg_exp( DutchDateTime.RelativeMonthRegex)
    week_day_regex: Pattern = RegExpUtility.get_safe_reg_exp( DutchDateTime.WeekDayRegex)
    range_connector_symbol_regex: Pattern = RegExpUtility.get_safe_reg_exp( BaseDateTime.RangeConnectorSymbolRegex )
    strict_relative_regex: Pattern = RegExpUtility.get_safe_reg_exp( DutchDateTime.StrictRelativeRegex )
    year_suffix: Pattern = RegExpUtility.get_safe_reg_exp( DutchDateTime.YearSuffix )
    prefix_article_regex: Pattern = RegExpUtility.get_safe_reg_exp( DutchDateTime.PrefixArticleRegex )
    week_day_end: Pattern = RegExpUtility.get_safe_reg_exp( DutchDateTime.WeekDayEnd )
    more_than_regex: Pattern = RegExpUtility.get_safe_reg_exp( DutchDateTime.MoreThanRegex )
    less_than_regex: Pattern = RegExpUtility.get_safe_reg_exp( DutchDateTime.LessThanRegex )
    in_connector_regex: Pattern = RegExpUtility.get_safe_reg_exp( DutchDateTime.InConnectorRegex )
    range_unit_regex: Pattern = RegExpUtility.get_safe_reg_exp( DutchDateTime.RangeUnitRegex )
    since_year_suffix_regex: Pattern = RegExpUtility.get_safe_reg_exp( DutchDateTime.SinceYearSuffixRegex )
    week_day_and_day_regex: Pattern = RegExpUtility.get_safe_reg_exp( DutchDateTime.WeekDayAndDayRegex )
    week_day_start: Pattern = RegExpUtility.get_safe_reg_exp( DutchDateTime.WeekDayStart )

    @property
    def date_regex_list(self) -> List[Pattern]:
        if DutchDateTime.DefaultLanguageFallback == Constants.DEFAULT_LANGUAGE_FALLBACK_DMY:
            date_extractor_4 = DutchDateTime.DateExtractor5
            date_extractor_5 = DutchDateTime.DateExtractor8
            date_extractor_6 = DutchDateTime.DateExtractor9L
            date_extractor_7 = DutchDateTime.DateExtractor9S
            date_extractor_8 = DutchDateTime.DateExtractor4
            date_extractor_9 = DutchDateTime.DateExtractor6
            date_extractor_10 = DutchDateTime.DateExtractor7L
            date_extractor_11 = DutchDateTime.DateExtractor7S
        else:
            date_extractor_4 = DutchDateTime.DateExtractor4
            date_extractor_5 = DutchDateTime.DateExtractor6
            date_extractor_6 = DutchDateTime.DateExtractor7L
            date_extractor_7 = DutchDateTime.DateExtractor7S
            date_extractor_8 = DutchDateTime.DateExtractor5
            date_extractor_9 = DutchDateTime.DateExtractor8
            date_extractor_10 = DutchDateTime.DateExtractor9L
            date_extractor_11 = DutchDateTime.DateExtractor9S

        return [
            RegExpUtility.get_safe_reg_exp(DutchDateTime.DateExtractor1),
            RegExpUtility.get_safe_reg_exp(DutchDateTime.DateExtractor3),
            RegExpUtility.get_safe_reg_exp(date_extractor_4),
            RegExpUtility.get_safe_reg_exp(date_extractor_5),
            RegExpUtility.get_safe_reg_exp(date_extractor_6),
            RegExpUtility.get_safe_reg_exp(date_extractor_7),
            RegExpUtility.get_safe_reg_exp(date_extractor_8),
            RegExpUtility.get_safe_reg_exp(date_extractor_9),
            RegExpUtility.get_safe_reg_exp(date_extractor_10),
            RegExpUtility.get_safe_reg_exp(date_extractor_11),
            RegExpUtility.get_safe_reg_exp(DutchDateTime.DateExtractorA),
        ]
