from typing import Pattern
from recognizers_text.utilities import RegExpUtility
from recognizers_date_time.date_time.base_date import DateTimeUtilityConfiguration
from recognizers_date_time.resources.minimal_date_time import MinimalDateTime


class MinimalDateTimeUtilityConfiguration(DateTimeUtilityConfiguration):

    @property
    def date_unit_regex(self) -> Pattern:
        return None

    @property
    def ago_regex(self) -> Pattern:
        return None

    @property
    def later_regex(self) -> Pattern:
        return None

    @property
    def in_connector_regex(self) -> Pattern:
        return None

    @property
    def range_unit_regex(self) -> Pattern:
        return None

    @property
    def check_both_before_after(self) -> Pattern:
        return None

    @property
    def range_prefix_regex(self) -> Pattern:
        return None

    @property
    def am_desc_regex(self) -> Pattern:
        return self._am_desc_regex

    @property
    def pm_desc__regex(self) -> Pattern:
        return self._pm_desc__regex

    @property
    def am_pm_desc_regex(self) -> Pattern:
        return self._am_pm_desc_regex

    def __init__(self):

        self._am_desc_regex = RegExpUtility.get_safe_reg_exp(
            MinimalDateTime.AmDescRegex)
        self._pm_desc__regex = RegExpUtility.get_safe_reg_exp(
            MinimalDateTime.PmDescRegex)
        self._am_pm_desc_regex = RegExpUtility.get_safe_reg_exp(
            MinimalDateTime.AmPmDescRegex)
        self._check_both_before_after = MinimalDateTime.CheckBothBeforeAfter
