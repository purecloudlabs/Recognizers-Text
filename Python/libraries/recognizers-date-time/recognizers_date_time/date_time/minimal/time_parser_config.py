from typing import List, Pattern, Dict

from recognizers_text import RegExpUtility
from ..base_time import TimeParserConfiguration
from ..base_configs import BaseDateParserConfiguration, DateTimeUtilityConfiguration
from .time_extractor_config import MinimalTimeExtractorConfiguration
from ..parsers import DateTimeParser


class MinimalTimeParserConfiguration(TimeParserConfiguration):
    @property
    def time_token_prefix(self) -> str:
        return ""

    @property
    def at_regex(self) -> Pattern:
        return RegExpUtility.get_safe_reg_exp(f'^[.]')

    @property
    def time_regexes(self) -> List[Pattern]:
        return self._time_regexes

    @property
    def numbers(self) -> Dict[str, int]:
        return self._numbers

    @property
    def utility_configuration(self) -> DateTimeUtilityConfiguration:
        return self._utility_configuration

    @property
    def time_zone_parser(self) -> DateTimeParser:
        return self._time_zone_parser

    def __init__(self, config: BaseDateParserConfiguration):
        self._time_regexes: List[Pattern] = MinimalTimeExtractorConfiguration.get_time_regex_list()

        self._utility_configuration = config.utility_configuration
        self._numbers: Dict[str, int] = config.numbers
        self._time_zone_parser = config.time_zone_parser
