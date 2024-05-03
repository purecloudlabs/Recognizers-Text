from typing import Dict, List, Pattern

import regex

from recognizers_text.utilities import RegExpUtility

from ...resources.catalan_date_time import CatalanDateTime
from ..base_configs import BaseDateParserConfiguration, DateTimeUtilityConfiguration
from ..base_time import AdjustParams, TimeParserConfiguration
from .time_extractor_config import CatalanTimeExtractorConfiguration


class CatalanTimeParserConfiguration(TimeParserConfiguration):
    @property
    def time_token_prefix(self) -> str:
        return self._time_token_prefix

    @property
    def at_regex(self) -> Pattern:
        return self._at_regex

    @property
    def time_regexes(self) -> List[Pattern]:
        return self._time_regexes

    @property
    def numbers(self) -> Dict[str, int]:
        return self._numbers

    @property
    def utility_configuration(self) -> DateTimeUtilityConfiguration:
        return self._utility_configuration

    def __init__(self, config: BaseDateParserConfiguration):
        self._time_token_prefix: str = CatalanDateTime.TimeTokenPrefix
        self._at_regex: Pattern = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.AtRegex)
        self._time_regexes: List[Pattern] = CatalanTimeExtractorConfiguration.get_time_regex_list(
        )
        self.less_than_one_hour = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.LessThanOneHour)
        self.time_suffix = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.TimeSuffix)

        self._utility_configuration = config.utility_configuration
        self._numbers: Dict[str, int] = config.numbers

    def adjust_by_prefix(self, prefix: str, adjust: AdjustParams):
        delta_min = 0
        prefix = prefix.strip().lower()

        if prefix.startswith('menys quart') or prefix.startswith('quarts') or prefix.startswith('tres quarts') or \
                prefix.startswith('quart menys') or prefix.startswith('3/4'):
            delta_min = -45
        elif prefix.startswith('i quart'):
            delta_min = 15
        elif prefix.startswith('quart') or prefix.startswith('un quart') or prefix.startswith('1/4'):
            delta_min = -15
        elif (prefix.startswith('mitjana') or prefix.startswith('i mitjana') or prefix.startswith('i mitja') or
              prefix.startswith('mitja') or prefix.startswith('1/2') or prefix.startswith('2/4')):
            delta_min = 30
        elif prefix.startswith("dos quarts"):
            delta_min = -30
        else:
            match = regex.search(self.less_than_one_hour, prefix)
            if match:
                min_str = RegExpUtility.get_group(match, 'deltamin')
                if min_str:
                    delta_min = int(min_str)
                else:
                    min_str = RegExpUtility.get_group(
                        match, 'deltaminnum').lower()
                    delta_min = self.numbers.get(min_str)

        if (
                prefix.endswith('passades') or prefix.endswith('passats') or
                prefix.endswith('passades les') or prefix.endswith('passats les') or
                prefix.endswith('passades de les') or prefix.endswith(
            'passats de les')
        ):
            # deltaMin it's positive
            pass
        elif (
                prefix.endswith('per a la') or prefix.endswith('per a les') or
                prefix.endswith('abans de la') or prefix.endswith('abans de les')
        ):
            delta_min = delta_min * -1

        adjust.minute += delta_min

        if adjust.minute < 0:
            if adjust.minute == -15:
                adjust.hour -= 1
                adjust.minute += 30
            elif adjust.minute == -45:
                adjust.hour -= 1
                adjust.minute += 90
            else:
                adjust.hour -= 1
                adjust.minute += 60

        adjust.has_minute = True

    def adjust_by_suffix(self, suffix: str, adjust: AdjustParams):
        suffix = suffix.strip().lower()

        delta_hour = 0
        match = regex.match(self.time_suffix, suffix)

        if match and match.group() == suffix:
            oclock_str = RegExpUtility.get_group(match, 'oclock')
            if not oclock_str:
                am_str = RegExpUtility.get_group(match, 'am')
                if am_str:
                    if adjust.hour >= 12:
                        delta_hour -= 12

                    adjust.has_am = True

                pm_str = RegExpUtility.get_group(match, 'pm')
                if pm_str:
                    if adjust.hour < 12:
                        delta_hour = 12

                    adjust.has_pm = True

        adjust.hour = (adjust.hour + delta_hour) % 24
