from typing import Pattern, List, Dict

from recognizers_text.utilities import RegExpUtility
from recognizers_number import BaseNumberExtractor, BaseNumberParser
from ...resources.minimal_date_time import MinimalDateTime
from ..extractors import DateTimeExtractor
from ..parsers import DateTimeParser
from ..utilities import DateTimeUtilityConfiguration
from ..base_date import DateParserConfiguration
from ..base_configs import BaseDateParserConfiguration


class MinimalDateParserConfiguration(DateParserConfiguration):
    @property
    def on_regex(self) -> Pattern:
        return RegExpUtility.get_safe_reg_exp(f'^[.]')


    @property
    def special_day_regex(self) -> Pattern:
        return RegExpUtility.get_safe_reg_exp(f'^[.]')


    @property
    def special_day_with_num_regex(self) -> Pattern:
        return RegExpUtility.get_safe_reg_exp(f'^[.]')


    @property
    def next_regex(self) -> Pattern:
        return RegExpUtility.get_safe_reg_exp(f'^[.]')


    @property
    def unit_regex(self) -> Pattern:
        return RegExpUtility.get_safe_reg_exp(f'^[.]')


    @property
    def month_regex(self) -> Pattern:
        return RegExpUtility.get_safe_reg_exp(f'^[.]')


    @property
    def week_day_regex(self) -> Pattern:
        return RegExpUtility.get_safe_reg_exp(f'^[.]')


    @property
    def last_regex(self) -> Pattern:
        return RegExpUtility.get_safe_reg_exp(f'^[.]')


    @property
    def this_regex(self) -> Pattern:
        return RegExpUtility.get_safe_reg_exp(f'^[.]')


    @property
    def week_day_of_month_regex(self) -> Pattern:
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
    def relative_week_day_regex(self) -> Pattern:
        return RegExpUtility.get_safe_reg_exp(f'^[.]')

    @property
    def date_token_prefix(self) -> str:
        return ""

    def get_swift_day(self, source: str) -> int:
        return RegExpUtility.get_safe_reg_exp(f'^[.]')

    def get_swift_month(self, source: str) -> int:
        return None

    def is_cardinal_last(self, source: str) -> bool:
        return None

    @property
    def check_both_before_after(self) -> bool:
        return self._check_both_before_after

    @property
    def ordinal_extractor(self) -> BaseNumberExtractor:
        return self._ordinal_extractor

    @property
    def integer_extractor(self) -> BaseNumberExtractor:
        return self._integer_extractor

    @property
    def cardinal_extractor(self) -> BaseNumberExtractor:
        return self._cardinal_extractor

    @property
    def date_extractor(self) -> DateTimeExtractor:
        return self._date_extractor

    @property
    def duration_extractor(self) -> DateTimeExtractor:
        return None


    @property
    def duration_parser(self) -> DateTimeParser:
         return None


    @property
    def number_parser(self) -> BaseNumberParser:
        return self._number_parser

    @property
    def month_of_year(self) -> Dict[str, int]:
        return self._month_of_year

    @property
    def day_of_month(self) -> Dict[str, int]:
        return self._day_of_month

    @property
    def day_of_week(self) -> Dict[str, int]:
        return self._day_of_week

    @property
    def unit_map(self) -> Dict[str, str]:
        return self._unit_map

    @property
    def cardinal_map(self) -> Dict[str, int]:
        return self._cardinal_map

    @property
    def date_regex(self) -> List[Pattern]:
        return self._date_regex

    @property
    def utility_configuration(self) -> DateTimeUtilityConfiguration:
        return self._utility_configuration

    _relative_day_regex = None

    _next_prefix_regex = None

    _past_prefix_regex = None


    def __init__(self, config: BaseDateParserConfiguration):
        self._ordinal_extractor = config.ordinal_extractor
        self._integer_extractor = config.integer_extractor
        self._cardinal_extractor = config.cardinal_extractor
        self._date_extractor = config.date_extractor
        self._number_parser = config.number_parser
        self._month_of_year = config.month_of_year
        self._day_of_month = config.day_of_month
        self._day_of_week = config.day_of_week
        self._unit_map = config.unit_map
        self._cardinal_map = config.cardinal_map
        self._date_regex = config.date_extractor.config.date_regex_list
        self._utility_configuration = config.utility_configuration
        self._check_both_before_after = MinimalDateTime.CheckBothBeforeAfter

    def __normalize(self, source: str) -> str:
        return source.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').\
            replace('ú', 'u').replace('à', 'a')
