from typing import Pattern

from recognizers_date_time.resources import BaseDateTimeResource
from recognizers_text.utilities import RegExpUtility


class DateTimeUtilityConfiguration:

    def __init__(self, resource: BaseDateTimeResource):
        self.later_regex: Pattern = RegExpUtility.get_safe_reg_exp(resource.LaterRegex)
        self.ago_regex: Pattern = RegExpUtility.get_safe_reg_exp(resource.AgoRegex)
        self.in_connector_regex: Pattern = RegExpUtility.get_safe_reg_exp(resource.InConnectorRegex)
        self.since_year_suffix_regex: Pattern = RegExpUtility.get_safe_reg_exp(resource.SinceYearSuffixRegex)
        self.within_next_prefix_regex: Pattern = RegExpUtility.get_safe_reg_exp(resource.WithinNextPrefixRegex)
        self.am_desc_regex: Pattern = RegExpUtility.get_safe_reg_exp(resource.AmDescRegex)
        self.pm_desc__regex: Pattern = RegExpUtility.get_safe_reg_exp(resource.PmDescRegex)
        self.am_pm_desc_regex: Pattern = RegExpUtility.get_safe_reg_exp(resource.AmPmDescRegex)
        self.range_unit_regex: Pattern = RegExpUtility.get_safe_reg_exp(resource.RangeUnitRegex)
        self.time_unit_regex: Pattern = RegExpUtility.get_safe_reg_exp(resource.TimeUnitRegex)
        self.date_unit_regex: Pattern = RegExpUtility.get_safe_reg_exp(resource.DateUnitRegex)
        self.common_date_prefix_regex: Pattern = RegExpUtility.get_safe_reg_exp(resource.CommonDatePrefixRegex)
        self.range_prefix_regex: Pattern = RegExpUtility.get_safe_reg_exp(resource.RangePrefixRegex)
        self.check_both_before_after: bool = resource.CheckBothBeforeAfter
