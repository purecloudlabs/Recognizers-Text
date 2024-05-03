from typing import Pattern, List, Dict
from recognizers_number import (BaseNumberExtractor, BaseNumberParser,
                                CatalanOrdinalExtractor, CatalanIntegerExtractor, CatalanNumberParserConfiguration)
from recognizers_text.utilities import RegExpUtility
from ...resources.catalan_date_time import CatalanDateTime
from ..extractors import DateTimeExtractor
from ..base_date import DateExtractorConfiguration
from ..utilities import DateTimeUtilityConfiguration
from .base_configs import CatalanDateTimeUtilityConfiguration
from ..constants import Constants
from ...resources.base_date_time import BaseDateTime


class CatalanDateExtractorConfiguration(DateExtractorConfiguration):

    ordinal_extractor: BaseNumberExtractor = CatalanOrdinalExtractor()
    integer_extractor: BaseNumberExtractor = CatalanIntegerExtractor()
    duration_extractor: DateTimeExtractor = None
    number_parser: BaseNumberParser = BaseNumberParser(CatalanNumberParserConfiguration())
    utility_configuration: DateTimeUtilityConfiguration = CatalanDateTimeUtilityConfiguration()
    check_both_before_after: bool = CatalanDateTime.CheckBothBeforeAfter

    day_of_week: Dict[str, int] = {}
    month_of_year: Dict[str, int] = CatalanDateTime.MonthOfYear

    month_end: Pattern = RegExpUtility.get_safe_reg_exp(CatalanDateTime.MonthEndRegex)
    of_month: Pattern = RegExpUtility.get_safe_reg_exp(CatalanDateTime.OfMonthRegex)
    date_unit_regex: Pattern = RegExpUtility.get_safe_reg_exp(f'^[.]')
    for_the_regex: Pattern = RegExpUtility.get_safe_reg_exp(f'^[.]')
    week_day_and_day_of_month_regex: Pattern = RegExpUtility.get_safe_reg_exp(
        CatalanDateTime.WeekDayAndDayOfMonthRegex)
    relative_month_regex: Pattern = RegExpUtility.get_safe_reg_exp(f'^[.]')
    week_day_regex: Pattern = RegExpUtility.get_safe_reg_exp(
        CatalanDateTime.WeekDayRegex)
    range_connector_symbol_regex = RegExpUtility.get_safe_reg_exp(
        BaseDateTime.RangeConnectorSymbolRegex
    )
    strict_relative_regex = RegExpUtility.get_safe_reg_exp(f'^[.]')
    year_suffix = RegExpUtility.get_safe_reg_exp(CatalanDateTime.YearSuffixRegex)
    prefix_article_regex = RegExpUtility.get_safe_reg_exp(f'^[.]')
    week_day_end = RegExpUtility.get_safe_reg_exp(
        CatalanDateTime.WeekDayEnd
    )
    more_than_regex = RegExpUtility.get_safe_reg_exp(f'^[.]')
    less_than_regex = RegExpUtility.get_safe_reg_exp(f'^[.]')
    in_connector_regex = RegExpUtility.get_safe_reg_exp(
        CatalanDateTime.InConnectorRegex
    )
    range_unit_regex = RegExpUtility.get_safe_reg_exp(
        CatalanDateTime.RangeUnitRegex
    )
    since_year_suffix_regex = RegExpUtility.get_safe_reg_exp(f'^[.]')
    week_day_and_day_regex = RegExpUtility.get_safe_reg_exp(
        CatalanDateTime.WeekDayAndDayRegex
    )
    week_day_start = RegExpUtility.get_safe_reg_exp(CatalanDateTime.WeekDayStart)

    implicit_date_list: List[Pattern] = [
        RegExpUtility.get_safe_reg_exp(CatalanDateTime.OnRegex),
        RegExpUtility.get_safe_reg_exp(CatalanDateTime.RelaxedOnRegex),
        RegExpUtility.get_safe_reg_exp(CatalanDateTime.SpecialDayRegex),
        # TODO - we might invest in resolving below in time.
        # RegExpUtility.get_safe_reg_exp(CatalanDateTime.ThisRegex),
        # RegExpUtility.get_safe_reg_exp(CatalanDateTime.LastDateRegex),
        # RegExpUtility.get_safe_reg_exp(CatalanDateTime.NextDateRegex),
        RegExpUtility.get_safe_reg_exp(CatalanDateTime.WeekDayRegex),
        # RegExpUtility.get_safe_reg_exp(
        # CatalanDateTime.WeekDayOfMonthRegex),
        RegExpUtility.get_safe_reg_exp(CatalanDateTime.SpecialDateRegex),
    ]

    @property
    def date_regex_list(self) -> List[Pattern]:
        if CatalanDateTime.DefaultLanguageFallback == Constants.DEFAULT_LANGUAGE_FALLBACK_DMY:
            date_extractor_4 = CatalanDateTime.DateExtractor5
            date_extractor_5 = CatalanDateTime.DateExtractor8
            date_extractor_6 = CatalanDateTime.DateExtractor9
            date_extractor_8 = CatalanDateTime.DateExtractor4
            date_extractor_7 = CatalanDateTime.DateExtractor6
            date_extractor_9 = CatalanDateTime.DateExtractor7
        else:
            date_extractor_4 = CatalanDateTime.DateExtractor4
            date_extractor_5 = CatalanDateTime.DateExtractor6
            date_extractor_6 = CatalanDateTime.DateExtractor7
            date_extractor_8 = CatalanDateTime.DateExtractor5
            date_extractor_7 = CatalanDateTime.DateExtractor8
            date_extractor_9 = CatalanDateTime.DateExtractor9

        return [
            RegExpUtility.get_safe_reg_exp(CatalanDateTime.DateExtractor1),
            RegExpUtility.get_safe_reg_exp(CatalanDateTime.DateExtractor2),
            RegExpUtility.get_safe_reg_exp(CatalanDateTime.DateExtractor3),
            RegExpUtility.get_safe_reg_exp(date_extractor_4),
            RegExpUtility.get_safe_reg_exp(date_extractor_5),
            RegExpUtility.get_safe_reg_exp(date_extractor_6),
            RegExpUtility.get_safe_reg_exp(date_extractor_7),
            RegExpUtility.get_safe_reg_exp(date_extractor_8),
            RegExpUtility.get_safe_reg_exp(date_extractor_9),
            RegExpUtility.get_safe_reg_exp(CatalanDateTime.DateExtractor10),
        ]
