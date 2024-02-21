from typing import Pattern

from recognizers_text.utilities import RegExpUtility
from recognizers_date_time.date_time.minimal.common_configs import MinimalCommonDateTimeParserConfiguration
from recognizers_date_time.date_time.base_date import BaseDateParser
from recognizers_date_time.date_time.base_time import BaseTimeParser
from recognizers_date_time.date_time.base_minimal_merged import MinimalMergedParserConfiguration
from recognizers_date_time.resources.minimal_date_time import MinimalDateTime, BaseDateTime
from recognizers_date_time.date_time.parsers import DateTimeParser


class BaseMinimalMergedParserConfiguration(MinimalCommonDateTimeParserConfiguration, MinimalMergedParserConfiguration):
    @property
    def around_regex(self) -> Pattern:
        return RegExpUtility.get_safe_reg_exp(f'^[.]')

    @property
    def equal_regex(self) -> Pattern:
        return self._equal_regex

    @property
    def year_regex(self) -> Pattern:
        return self._year_regex

    @property
    def suffix_after(self) -> Pattern:
        return RegExpUtility.get_safe_reg_exp(f'^[.]')

    @property
    def before_regex(self) -> Pattern:
        return RegExpUtility.get_safe_reg_exp(f'^[.]')

    @property
    def after_regex(self) -> Pattern:
        return RegExpUtility.get_safe_reg_exp(f'^[.]')

    @property
    def since_regex(self) -> Pattern:
        return RegExpUtility.get_safe_reg_exp(f'^[.]')

    @property
    def date_parser(self) -> BaseDateParser:
        return self._date_parser

    @property
    def time_parser(self) -> BaseTimeParser:
        return self._time_parser

    @property
    def date_time_parser(self) -> BaseTimeParser:
        return None

    @property
    def time_zone_parser(self) -> DateTimeParser:
        return self._time_zone_parser

    def __init__(self, config, dmyDateFormat = True):
        MinimalCommonDateTimeParserConfiguration.__init__(self, dmyDateFormat)
        self._time_zone_parser = config.time_zone_parser
        self._equal_regex = RegExpUtility.get_safe_reg_exp(BaseDateTime.EqualRegex)
        self._year_regex = RegExpUtility.get_safe_reg_exp(MinimalDateTime.YearRegex)
