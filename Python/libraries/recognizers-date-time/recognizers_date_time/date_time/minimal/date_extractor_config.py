from typing import Pattern, List, Dict
from recognizers_number import (BaseNumberExtractor, MinimalNumberParser, MinimalIntegerExtractor,
                                MinimalNumberParserConfiguration)
from recognizers_text.utilities import RegExpUtility
from recognizers_date_time.resources.minimal_date_time import MinimalDateTime
from recognizers_date_time.resources.base_date_time import BaseDateTime


class MinimalDateExtractorConfiguration:

    @property
    def month_of_year(self) -> Dict[str, int]:
        return self._month_of_year

    @property
    def check_both_before_after(self) -> bool:
        return self._check_both_before_after

    @property
    def date_regex_list(self) -> List[Pattern]:
        return self._date_regex_list

    @property
    def integer_extractor(self) -> BaseNumberExtractor:
        return self._integer_extractor

    @property
    def number_parser(self) -> MinimalNumberParser:
        return self._number_parser

    @property
    def range_connector_symbol_regex(self) -> Pattern:
        return self._range_connector_symbol_regex

    @property
    def strict_relative_regex(self):
        return ""

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

        self._integer_extractor = MinimalIntegerExtractor()
        self._number_parser = MinimalNumberParser(
            MinimalNumberParserConfiguration())
        self._range_connector_symbol_regex = RegExpUtility.get_safe_reg_exp(
            BaseDateTime.RangeConnectorSymbolRegex
        )
        self._check_both_before_after = MinimalDateTime.CheckBothBeforeAfter
        self._month_of_year = MinimalDateTime.MonthOfYear
