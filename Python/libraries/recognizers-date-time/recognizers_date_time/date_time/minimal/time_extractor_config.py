from typing import List, Pattern
from recognizers_text.utilities import RegExpUtility
from ...resources.minimal_date_time import MinimalDateTime


class MinimalTimeExtractorConfiguration:
    @property
    def options(self):
        return 0

    @property
    def time_regex_list(self) -> List[Pattern]:
        return self._time_regex_list

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
