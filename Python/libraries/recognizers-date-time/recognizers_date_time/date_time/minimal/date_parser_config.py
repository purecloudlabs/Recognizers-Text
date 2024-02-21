from typing import Pattern, List, Dict

from recognizers_number import BaseNumberExtractor, BaseNumberParser
from recognizers_date_time.resources.minimal_date_time import MinimalDateTime
from recognizers_date_time.date_time.extractors import DateTimeExtractor
from recognizers_date_time.date_time.utilities import DateTimeUtilityConfiguration


class MinimalDateParserConfiguration:

    @property
    def date_token_prefix(self) -> str:
        return ""

    @property
    def check_both_before_after(self) -> bool:
        return self._check_both_before_after

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
    def number_parser(self) -> BaseNumberParser:
        return self._number_parser

    @property
    def month_of_year(self) -> Dict[str, int]:
        return self._month_of_year

    @property
    def day_of_month(self) -> Dict[str, int]:
        return self._day_of_month

    @property
    def date_regex(self) -> List[Pattern]:
        return self._date_regex

    @property
    def utility_configuration(self) -> DateTimeUtilityConfiguration:
        return self._utility_configuration

    def __init__(self, config):
        self._integer_extractor = config.integer_extractor
        self._cardinal_extractor = config.cardinal_extractor
        self._date_extractor = config.date_extractor
        self._number_parser = config.number_parser
        self._month_of_year = config.month_of_year
        self._day_of_month = config.day_of_month
        self._date_regex = config.date_extractor.config.date_regex_list
        self._utility_configuration = config.utility_configuration
        self._check_both_before_after = MinimalDateTime.CheckBothBeforeAfter

    def __normalize(self, source: str) -> str:
        return source.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').\
            replace('ú', 'u').replace('à', 'a')
