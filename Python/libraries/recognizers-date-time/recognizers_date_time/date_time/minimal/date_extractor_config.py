from typing import Pattern, List, Dict
from recognizers_number import (BaseNumberExtractor, MinimalNumberParser, MinimalIntegerExtractor,
                                MinimalNumberParserConfiguration, MinimalOrdinalExtractor)
from recognizers_text.utilities import RegExpUtility
from ...resources.minimal_date_time import MinimalDateTime
from ..extractors import DateTimeExtractor
from ..base_date import DateExtractorConfiguration
from .base_configs import MinimalDateTimeUtilityConfiguration
from ..constants import Constants
from ...resources.base_date_time import BaseDateTime


class MinimalDateExtractorConfiguration(DateExtractorConfiguration):

    @property
    def month_end(self) -> Pattern:
        return RegExpUtility.get_safe_reg_exp(f'^[.]')

    @property
    def week_day_end(self) -> Pattern:
        return RegExpUtility.get_safe_reg_exp(f'^[.]')

    @property
    def week_day_start(self) -> Pattern:
        return RegExpUtility.get_safe_reg_exp(f'^[.]')

    @property
    def of_month(self) -> Pattern:
        return RegExpUtility.get_safe_reg_exp(f'^[.]')

    @property
    def date_unit_regex(self) -> Pattern:
        return RegExpUtility.get_safe_reg_exp(f'^[.]')

    @property
    def for_the_regex(self) -> Pattern:
        return RegExpUtility.get_safe_reg_exp(f'^[.]')

    @property
    def week_day_and_day_of_month_regex(self) -> Pattern:
        return RegExpUtility.get_safe_reg_exp(f'^[.]')

    @property
    def week_day_and_day_regex(self) -> Pattern:
        return RegExpUtility.get_safe_reg_exp(f'^[.]')

    @property
    def relative_month_regex(self) -> Pattern:
        return RegExpUtility.get_safe_reg_exp(f'^[.]')

    @property
    def week_day_regex(self) -> Pattern:
        return RegExpUtility.get_safe_reg_exp(f'^[.]')

    @property
    def prefix_article_regex(self) -> Pattern:
        return RegExpUtility.get_safe_reg_exp(f'^[.]')

    @property
    def day_of_week(self) -> Dict[str, int]:
        None

    @property
    def month_of_year(self) -> Dict[str, int]:
        self._month_of_year

    @property
    def ordinal_extractor(self):
        return self._ordinal_extractor

    @property
    def utility_configuration(self):
        None

    @property
    def strict_relative_regex(self) -> Pattern:
        return RegExpUtility.get_safe_reg_exp(f'^[.]')

    @property
    def year_suffix(self) -> Pattern:
        return RegExpUtility.get_safe_reg_exp(f'^[.]')

    @property
    def more_than_regex(self) -> Pattern:
        return RegExpUtility.get_safe_reg_exp(f'^[.]')

    @property
    def less_than_regex(self) -> Pattern:
        return RegExpUtility.get_safe_reg_exp(f'^[.]')

    @property
    def in_connector_regex(self) -> Pattern:
        return RegExpUtility.get_safe_reg_exp(f'^[.]')

    @property
    def range_unit_regex(self) -> Pattern:
        return RegExpUtility.get_safe_reg_exp(f'^[.]')

    @property
    def since_year_suffix_regex(self) -> Pattern:
        return RegExpUtility.get_safe_reg_exp(f'^[.]')

    @property
    def check_both_before_after(self) -> bool:
        return self._check_both_before_after

    @property
    def date_regex_list(self) -> List[Pattern]:
        return self._date_regex_list

    @property
    def implicit_date_list(self) -> List[Pattern]:
        return self._implicit_date_list

    @property
    def integer_extractor(self) -> BaseNumberExtractor:
        return self._integer_extractor

    @property
    def number_parser(self) -> MinimalNumberParser:
        return self._number_parser

    @property
    def duration_extractor(self) -> DateTimeExtractor:
        return None

    @property
    def range_connector_symbol_regex(self) -> Pattern:
        return self._range_connector_symbol_regex

    def __init__(self, dmyDateFormat: bool = True):
        self._check_both_before_after = False
        if dmyDateFormat:
            date_extractor_4 = MinimalDateTime.DateExtractor5
            date_extractor_7 = MinimalDateTime.DateExtractor9S
            date_extractor_8 = MinimalDateTime.DateExtractor4
            date_extractor_11 = MinimalDateTime.DateExtractor7S
        else:
            date_extractor_4 = MinimalDateTime.DateExtractor4
            date_extractor_7 = MinimalDateTime.DateExtractor7S
            date_extractor_8 = MinimalDateTime.DateExtractor5
            date_extractor_11 = MinimalDateTime.DateExtractor9S

        self._date_regex_list = [
            RegExpUtility.get_safe_reg_exp(date_extractor_4),
            RegExpUtility.get_safe_reg_exp(date_extractor_7),
            RegExpUtility.get_safe_reg_exp(date_extractor_8),
            RegExpUtility.get_safe_reg_exp(date_extractor_11),
        ]

        self._implicit_date_list = []
        self._integer_extractor = MinimalIntegerExtractor()
        self._number_parser = MinimalNumberParser(
            MinimalNumberParserConfiguration())
        self._utility_configuration = MinimalDateTimeUtilityConfiguration()
        self._range_connector_symbol_regex = RegExpUtility.get_safe_reg_exp(
            BaseDateTime.RangeConnectorSymbolRegex
        )
        self._check_both_before_after = MinimalDateTime.CheckBothBeforeAfter
        self._ordinal_extractor = MinimalOrdinalExtractor()
        self._month_of_year = MinimalDateTime.MonthOfYear
