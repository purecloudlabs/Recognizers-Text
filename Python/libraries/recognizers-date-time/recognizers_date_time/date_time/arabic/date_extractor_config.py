from typing import Pattern, List, Dict
from recognizers_number import (BaseNumberExtractor, BaseNumberParser,
                                ArabicOrdinalExtractor, ArabicIntegerExtractor, ArabicNumberParserConfiguration)
from recognizers_text.utilities import RegExpUtility
from recognizers_date_time.resources import ArabicDateTime, BaseDateTime
from recognizers_date_time.date_time.extractors import DateTimeExtractor
from recognizers_date_time.date_time.base_date import DateExtractorConfiguration
from recognizers_date_time.date_time.base_duration import BaseDurationExtractor
from recognizers_date_time.date_time.utilities import DateTimeUtilityConfiguration
from recognizers_date_time.date_time.arabic.base_configs import ArabicDateTimeUtilityConfiguration
from recognizers_date_time.date_time.arabic.duration_extractor_config import ArabicDurationExtractorConfiguration
from recognizers_date_time.date_time.constants import Constants


class ArabicDateExtractorConfiguration(DateExtractorConfiguration):

    ordinal_extractor: BaseNumberExtractor = ArabicOrdinalExtractor()
    integer_extractor: BaseNumberExtractor = ArabicIntegerExtractor()
    number_parser: BaseNumberParser = BaseNumberParser(ArabicNumberParserConfiguration())
    duration_extractor: DateTimeExtractor = BaseDurationExtractor(ArabicDurationExtractorConfiguration())
    utility_configuration: DateTimeUtilityConfiguration = ArabicDateTimeUtilityConfiguration()
    check_both_before_after: bool = ArabicDateTime.CheckBothBeforeAfter

    day_of_week: Dict[str, int] = ArabicDateTime.DayOfWeek
    month_of_year: Dict[str, int] = ArabicDateTime.MonthOfYear

    year_regex: Pattern = RegExpUtility.get_safe_reg_exp(ArabicDateTime.YearRegex)
    before_after_regex: Pattern = RegExpUtility.get_safe_reg_exp(ArabicDateTime.BeforeAfterRegex)
    month_num_regex: Pattern = RegExpUtility.get_safe_reg_exp(ArabicDateTime.MonthNumRegex)
    month_regex: Pattern = RegExpUtility.get_safe_reg_exp(ArabicDateTime.MonthRegex)
    of_month: Pattern = RegExpUtility.get_safe_reg_exp(ArabicDateTime.OfMonth)
    month_end: Pattern = RegExpUtility.get_safe_reg_exp(ArabicDateTime.MonthEnd)
    week_day_end: Pattern = RegExpUtility.get_safe_reg_exp(ArabicDateTime.WeekDayEnd)
    week_day_start: Pattern = RegExpUtility.get_safe_reg_exp(ArabicDateTime.WeekDayStart)
    date_unit_regex: Pattern = RegExpUtility.get_safe_reg_exp(ArabicDateTime.DateUnitRegex)
    for_the_regex: Pattern = RegExpUtility.get_safe_reg_exp(ArabicDateTime.ForTheRegex)
    week_day_and_day_of_month_regex: Pattern = RegExpUtility.get_safe_reg_exp(ArabicDateTime.WeekDayAndDayOfMonthRegex)
    week_day_and_day_regex: Pattern = RegExpUtility.get_safe_reg_exp(ArabicDateTime.WeekDayAndDayRegex)
    relative_month_regex: Pattern = RegExpUtility.get_safe_reg_exp(ArabicDateTime.RelativeMonthRegex)
    strict_relative_regex: Pattern = RegExpUtility.get_safe_reg_exp(ArabicDateTime.StrictRelativeRegex)
    week_day_regex: Pattern = RegExpUtility.get_safe_reg_exp(ArabicDateTime.WeekDayRegex)
    prefix_article_regex: Pattern = RegExpUtility.get_safe_reg_exp(ArabicDateTime.PrefixArticleRegex)
    year_suffix: Pattern = RegExpUtility.get_safe_reg_exp(ArabicDateTime.YearSuffix)
    less_than_regex: Pattern = RegExpUtility.get_safe_reg_exp(ArabicDateTime.LessThanRegex)
    more_than_regex: Pattern = RegExpUtility.get_safe_reg_exp(ArabicDateTime.MoreThanRegex)
    in_connector_regex: Pattern = RegExpUtility.get_safe_reg_exp(ArabicDateTime.InConnectorRegex)
    since_year_suffix_regex: Pattern = RegExpUtility.get_safe_reg_exp(ArabicDateTime.SinceYearSuffixRegex)
    range_unit_regex: Pattern = RegExpUtility.get_safe_reg_exp(ArabicDateTime.RangeUnitRegex)
    range_connector_symbol_regex: Pattern = RegExpUtility.get_safe_reg_exp(BaseDateTime.RangeConnectorSymbolRegex)

    implicit_date_list: List[Pattern] = [
        RegExpUtility.get_safe_reg_exp(ArabicDateTime.OnRegex),
        RegExpUtility.get_safe_reg_exp(ArabicDateTime.RelaxedOnRegex),
        RegExpUtility.get_safe_reg_exp(ArabicDateTime.SpecialDayRegex),
        RegExpUtility.get_safe_reg_exp(ArabicDateTime.ThisRegex),
        RegExpUtility.get_safe_reg_exp(ArabicDateTime.LastDateRegex),
        RegExpUtility.get_safe_reg_exp(ArabicDateTime.NextDateRegex),
        RegExpUtility.get_safe_reg_exp(ArabicDateTime.SingleWeekDayRegex),
        RegExpUtility.get_safe_reg_exp(ArabicDateTime.WeekDayOfMonthRegex),
        RegExpUtility.get_safe_reg_exp(ArabicDateTime.SpecialDate),
        RegExpUtility.get_safe_reg_exp(ArabicDateTime.SpecialDayWithNumRegex),
        RegExpUtility.get_safe_reg_exp(ArabicDateTime.RelativeWeekDayRegex),
    ]

    @property
    def date_regex_list(self) -> List[Pattern]:
        if ArabicDateTime.DefaultLanguageFallback == Constants.DEFAULT_LANGUAGE_FALLBACK_DMY:
            date_extractor_4 = ArabicDateTime.DateExtractor5
            date_extractor_5 = ArabicDateTime.DateExtractor8
            date_extractor_6 = ArabicDateTime.DateExtractor7L
            date_extractor_7 = ArabicDateTime.DateExtractor9S
            date_extractor_8 = ArabicDateTime.DateExtractor4
            date_extractor_9 = ArabicDateTime.DateExtractor6
            date_extractor_10 = ArabicDateTime.DateExtractor9L
            date_extractor_11 = ArabicDateTime.DateExtractor7S
        else:
            date_extractor_4 = ArabicDateTime.DateExtractor4
            date_extractor_5 = ArabicDateTime.DateExtractor6
            date_extractor_6 = ArabicDateTime.DateExtractor7L
            date_extractor_7 = ArabicDateTime.DateExtractor7S
            date_extractor_8 = ArabicDateTime.DateExtractor5
            date_extractor_9 = ArabicDateTime.DateExtractor8
            date_extractor_10 = ArabicDateTime.DateExtractor9L
            date_extractor_11 = ArabicDateTime.DateExtractor9S

        return [
            RegExpUtility.get_safe_reg_exp(ArabicDateTime.DateExtractor1),
            RegExpUtility.get_safe_reg_exp(ArabicDateTime.DateExtractor3),
            RegExpUtility.get_safe_reg_exp(date_extractor_4),
            RegExpUtility.get_safe_reg_exp(date_extractor_5),
            RegExpUtility.get_safe_reg_exp(date_extractor_6),
            RegExpUtility.get_safe_reg_exp(date_extractor_7),
            RegExpUtility.get_safe_reg_exp(date_extractor_8),
            RegExpUtility.get_safe_reg_exp(date_extractor_9),
            RegExpUtility.get_safe_reg_exp(date_extractor_10),
            RegExpUtility.get_safe_reg_exp(date_extractor_11),
            RegExpUtility.get_safe_reg_exp(ArabicDateTime.DateExtractorA),
            RegExpUtility.get_safe_reg_exp(ArabicDateTime.DateExtractorB),
        ]
