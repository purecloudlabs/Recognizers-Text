#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from typing import Pattern, List, Dict
from recognizers_number import (BaseNumberExtractor, BaseNumberParser,
                                FrenchOrdinalExtractor, FrenchIntegerExtractor, FrenchNumberParserConfiguration)
from recognizers_text.utilities import RegExpUtility
from ...resources.french_date_time import FrenchDateTime
from ..extractors import DateTimeExtractor
from ..base_duration import BaseDurationExtractor
from ..base_date import DateExtractorConfiguration
from ..utilities import DateTimeUtilityConfiguration
from .duration_extractor_config import FrenchDurationExtractorConfiguration
from .base_configs import FrenchDateTimeUtilityConfiguration
from ..constants import Constants
from ...resources.base_date_time import BaseDateTime
from ..utilities import DateTimeOptions


class FrenchDateExtractorConfiguration(DateExtractorConfiguration):

    ordinal_extractor: BaseNumberExtractor = FrenchOrdinalExtractor()
    integer_extractor: BaseNumberExtractor = FrenchIntegerExtractor()
    number_parser: BaseNumberParser = BaseNumberParser(FrenchNumberParserConfiguration())
    duration_extractor: DateTimeExtractor = BaseDurationExtractor(FrenchDurationExtractorConfiguration())
    utility_configuration: DateTimeUtilityConfiguration = FrenchDateTimeUtilityConfiguration()
    check_both_before_after: bool = FrenchDateTime.CheckBothBeforeAfter

    day_of_week: Dict[str, int] = FrenchDateTime.DayOfWeek
    month_of_year: Dict[str, int] = FrenchDateTime.MonthOfYear

    month_end: Pattern = RegExpUtility.get_safe_reg_exp(FrenchDateTime.MonthEnd)
    of_month: Pattern = RegExpUtility.get_safe_reg_exp(FrenchDateTime.OfMonth)
    date_unit_regex: Pattern = RegExpUtility.get_safe_reg_exp(FrenchDateTime.DateUnitRegex)
    for_the_regex: Pattern = RegExpUtility.get_safe_reg_exp(FrenchDateTime.ForTheRegex)
    week_day_and_day_of_month_regex: Pattern = RegExpUtility.get_safe_reg_exp(FrenchDateTime.WeekDayAndDayOfMonthRegex)
    relative_month_regex: Pattern = RegExpUtility.get_safe_reg_exp(FrenchDateTime.RelativeMonthRegex)
    week_day_regex: Pattern = RegExpUtility.get_safe_reg_exp(FrenchDateTime.WeekDayRegex)
    range_connector_symbol_regex: Pattern = RegExpUtility.get_safe_reg_exp(BaseDateTime.RangeConnectorSymbolRegex)
    strict_relative_regex: Pattern = RegExpUtility.get_safe_reg_exp(FrenchDateTime.StrictRelativeRegex)
    year_suffix: Pattern = RegExpUtility.get_safe_reg_exp(FrenchDateTime.YearSuffix)
    prefix_article_regex: Pattern = RegExpUtility.get_safe_reg_exp(FrenchDateTime.PrefixArticleRegex)
    week_day_end: Pattern = RegExpUtility.get_safe_reg_exp(FrenchDateTime.WeekDayEnd)
    more_than_regex: Pattern = RegExpUtility.get_safe_reg_exp(FrenchDateTime.MoreThanRegex)
    less_than_regex: Pattern = RegExpUtility.get_safe_reg_exp(FrenchDateTime.LessThanRegex)
    in_connector_regex: Pattern = RegExpUtility.get_safe_reg_exp(FrenchDateTime.InConnectorRegex)
    range_unit_regex: Pattern = RegExpUtility.get_safe_reg_exp(FrenchDateTime.RangeUnitRegex)
    since_year_suffix_regex: Pattern = RegExpUtility.get_safe_reg_exp(FrenchDateTime.SinceYearSuffixRegex)
    week_day_and_day_regex: Pattern = RegExpUtility.get_safe_reg_exp(FrenchDateTime.WeekDayAndDayRegex)
    week_day_start: Pattern = RegExpUtility.get_safe_reg_exp(FrenchDateTime.WeekDayStart)

    implicit_date_list: List[Pattern] = [
        RegExpUtility.get_safe_reg_exp(FrenchDateTime.OnRegex),
        RegExpUtility.get_safe_reg_exp(FrenchDateTime.RelaxedOnRegex),
        RegExpUtility.get_safe_reg_exp(FrenchDateTime.SpecialDayRegex),
        RegExpUtility.get_safe_reg_exp(FrenchDateTime.ThisRegex),
        RegExpUtility.get_safe_reg_exp(FrenchDateTime.LastDateRegex),
        RegExpUtility.get_safe_reg_exp(FrenchDateTime.NextDateRegex),
        RegExpUtility.get_safe_reg_exp(FrenchDateTime.StrictWeekDay),
        RegExpUtility.get_safe_reg_exp(FrenchDateTime.WeekDayOfMonthRegex),
        RegExpUtility.get_safe_reg_exp(FrenchDateTime.SpecialDate),
    ]

    @property
    def date_regex_list(self) -> List[Pattern]:
        if FrenchDateTime.DefaultLanguageFallback == Constants.DEFAULT_LANGUAGE_FALLBACK_DMY:
            date_extractor_4 = FrenchDateTime.DateExtractor5
            date_extractor_5 = FrenchDateTime.DateExtractor4
            date_extractor_6 = FrenchDateTime.DateExtractor7
            date_extractor_7 = FrenchDateTime.DateExtractor6
        else:
            date_extractor_4 = FrenchDateTime.DateExtractor4
            date_extractor_5 = FrenchDateTime.DateExtractor5
            date_extractor_6 = FrenchDateTime.DateExtractor6
            date_extractor_7 = FrenchDateTime.DateExtractor7

        return [
            RegExpUtility.get_safe_reg_exp(FrenchDateTime.DateExtractor1),
            RegExpUtility.get_safe_reg_exp(FrenchDateTime.DateExtractor2),
            RegExpUtility.get_safe_reg_exp(FrenchDateTime.DateExtractor3),
            RegExpUtility.get_safe_reg_exp(date_extractor_4),
            RegExpUtility.get_safe_reg_exp(date_extractor_5),
            RegExpUtility.get_safe_reg_exp(date_extractor_6),
            RegExpUtility.get_safe_reg_exp(date_extractor_7),
            RegExpUtility.get_safe_reg_exp(FrenchDateTime.DateExtractor8),
            RegExpUtility.get_safe_reg_exp(FrenchDateTime.DateExtractor9),
            RegExpUtility.get_safe_reg_exp(FrenchDateTime.DateExtractorA),
        ]

