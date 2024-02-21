from typing import List, Pattern
from recognizers_text.utilities import RegExpUtility
from ...resources.minimal_date_time import  MinimalDateTime
from ..base_time import TimeExtractorConfiguration


class MinimalTimeExtractorConfiguration(TimeExtractorConfiguration):
    @property
    def time_zone_extractor(self):
        return None

    @property
    def options(self):
        return self._options

    @property
    def dmy_date_format(self) -> bool:
        return self._dmy_date_format

    @property
    def time_regex_list(self) -> List[Pattern]:
        return self._time_regex_list

    @property
    def at_regex(self) -> Pattern:
        return None

    @property
    def ish_regex(self) -> Pattern:
        return None

    @property
    def time_before_after_regex(self) -> Pattern:
        return None

    def __init__(self):
        super().__init__()
        self._time_regex_list: List[Pattern] = MinimalTimeExtractorConfiguration.get_time_regex_list()

    @staticmethod
    def get_time_regex_list() -> List[Pattern]:
        return [
            RegExpUtility.get_safe_reg_exp(MinimalDateTime.TimeRegex1),
            RegExpUtility.get_safe_reg_exp(MinimalDateTime.TimeRegex2),
            RegExpUtility.get_safe_reg_exp(MinimalDateTime.TimeRegex3),
            RegExpUtility.get_safe_reg_exp(MinimalDateTime.TimeRegex12),
            RegExpUtility.get_safe_reg_exp(MinimalDateTime.ConnectNumRegex)
        ]
