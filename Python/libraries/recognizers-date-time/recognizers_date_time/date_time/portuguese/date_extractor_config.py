#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from typing import Pattern, List, Dict
from recognizers_number import (BaseNumberExtractor, BaseNumberParser,
                                PortugueseOrdinalExtractor, PortugueseIntegerExtractor, PortugueseNumberParserConfiguration)
from recognizers_text.utilities import RegExpUtility
from ...resources.portuguese_date_time import PortugueseDateTime
from ..extractors import DateTimeExtractor
from ..base_duration import BaseDurationExtractor
from ..base_date import DateExtractorConfiguration
from ..utilities import DateTimeUtilityConfiguration
from .duration_extractor_config import PortugueseDurationExtractorConfiguration
from .base_configs import PortugueseDateTimeUtilityConfiguration
from ..constants import Constants
from ...resources.base_date_time import BaseDateTime


class PortugueseDateExtractorConfiguration(DateExtractorConfiguration):

    ordinal_extractor: BaseNumberExtractor = PortugueseOrdinalExtractor()
    integer_extractor: BaseNumberExtractor = PortugueseIntegerExtractor()
    number_parser: BaseNumberParser = BaseNumberParser(PortugueseNumberParserConfiguration())
    duration_extractor: BaseDurationExtractor = BaseDurationExtractor(PortugueseDurationExtractorConfiguration())
    utility_configuration: DateTimeUtilityConfiguration = PortugueseDateTimeUtilityConfiguration()
    check_both_before_after: bool = PortugueseDateTime.CheckBothBeforeAfter

    month_end: Pattern = RegExpUtility.get_safe_reg_exp(PortugueseDateTime.MonthEndRegex)
    of_month: Pattern = RegExpUtility.get_safe_reg_exp(PortugueseDateTime.OfMonthRegex)
    date_unit_regex: Pattern = RegExpUtility.get_safe_reg_exp(PortugueseDateTime.DateUnitRegex)
    for_the_regex: Pattern = RegExpUtility.get_safe_reg_exp(PortugueseDateTime.ForTheRegex)
    week_day_and_day_of_month_regex: Pattern = RegExpUtility.get_safe_reg_exp(PortugueseDateTime.WeekDayAndDayOfMonthRegex)
    relative_month_regex: Pattern = RegExpUtility.get_safe_reg_exp(PortugueseDateTime.RelativeMonthRegex)
    week_day_regex: Pattern = RegExpUtility.get_safe_reg_exp(PortugueseDateTime.WeekDayRegex)
    day_of_week = PortugueseDateTime.DayOfWeek
    range_connector_symbol_regex: Pattern = RegExpUtility.get_safe_reg_exp(BaseDateTime.RangeConnectorSymbolRegex)
    strict_relative_regex: Pattern = RegExpUtility.get_safe_reg_exp(PortugueseDateTime.StrictRelativeRegex)
    year_suffix: Pattern = RegExpUtility.get_safe_reg_exp(PortugueseDateTime.YearSuffix)
    month_of_year = PortugueseDateTime.MonthOfYear
    prefix_article_regex: Pattern = RegExpUtility.get_safe_reg_exp(PortugueseDateTime.PrefixArticleRegex)
    week_day_end: Pattern = RegExpUtility.get_safe_reg_exp(PortugueseDateTime.WeekDayEnd)
    more_than_regex: Pattern = RegExpUtility.get_safe_reg_exp(PortugueseDateTime.MoreThanRegex)
    less_than_regex: Pattern = RegExpUtility.get_safe_reg_exp(PortugueseDateTime.LessThanRegex)
    in_connector_regex: Pattern = RegExpUtility.get_safe_reg_exp(PortugueseDateTime.InConnectorRegex)
    range_unit_regex: Pattern = RegExpUtility.get_safe_reg_exp(PortugueseDateTime.RangeUnitRegex)
    since_year_suffix_regex: Pattern = RegExpUtility.get_safe_reg_exp(PortugueseDateTime.SinceYearSuffixRegex)
    week_day_and_day_regex: Pattern = RegExpUtility.get_safe_reg_exp(PortugueseDateTime.WeekDayAndDayRegex)
    week_day_start: Pattern = RegExpUtility.get_safe_reg_exp(PortugueseDateTime.WeekDayStart)

    implicit_date_list: List[Pattern] = [
        RegExpUtility.get_safe_reg_exp(PortugueseDateTime.OnRegex),
        RegExpUtility.get_safe_reg_exp(PortugueseDateTime.RelaxedOnRegex),
        RegExpUtility.get_safe_reg_exp(PortugueseDateTime.SpecialDayRegex),
        RegExpUtility.get_safe_reg_exp(PortugueseDateTime.ThisRegex),
        RegExpUtility.get_safe_reg_exp(PortugueseDateTime.LastDateRegex),
        RegExpUtility.get_safe_reg_exp(PortugueseDateTime.NextDateRegex),
        RegExpUtility.get_safe_reg_exp(PortugueseDateTime.WeekDayRegex),
        RegExpUtility.get_safe_reg_exp(PortugueseDateTime.WeekDayOfMonthRegex),
        RegExpUtility.get_safe_reg_exp(PortugueseDateTime.SpecialDateRegex),
    ]

    @property
    def date_regex_list(self) -> List[Pattern]:
        if PortugueseDateTime.DefaultLanguageFallback == Constants.DEFAULT_LANGUAGE_FALLBACK_DMY:
            date_extractor_4 = PortugueseDateTime.DateExtractor5
            date_extractor_5 = PortugueseDateTime.DateExtractor4
            date_extractor_6 = PortugueseDateTime.DateExtractor8
            date_extractor_8 = PortugueseDateTime.DateExtractor6
            date_extractor_7 = PortugueseDateTime.DateExtractor9
            date_extractor_9 = PortugueseDateTime.DateExtractor7
        else:
            date_extractor_4 = PortugueseDateTime.DateExtractor4
            date_extractor_5 = PortugueseDateTime.DateExtractor5
            date_extractor_6 = PortugueseDateTime.DateExtractor6
            date_extractor_8 = PortugueseDateTime.DateExtractor8
            date_extractor_7 = PortugueseDateTime.DateExtractor7
            date_extractor_9 = PortugueseDateTime.DateExtractor9

        return [
            RegExpUtility.get_safe_reg_exp(PortugueseDateTime.DateExtractor1),
            RegExpUtility.get_safe_reg_exp(PortugueseDateTime.DateExtractor2),
            RegExpUtility.get_safe_reg_exp(PortugueseDateTime.DateExtractor3),
            RegExpUtility.get_safe_reg_exp(date_extractor_4),
            RegExpUtility.get_safe_reg_exp(date_extractor_5),
            RegExpUtility.get_safe_reg_exp(date_extractor_6),
            RegExpUtility.get_safe_reg_exp(date_extractor_7),
            RegExpUtility.get_safe_reg_exp(date_extractor_8),
            RegExpUtility.get_safe_reg_exp(date_extractor_9),
            RegExpUtility.get_safe_reg_exp(PortugueseDateTime.DateExtractor10),
        ]

