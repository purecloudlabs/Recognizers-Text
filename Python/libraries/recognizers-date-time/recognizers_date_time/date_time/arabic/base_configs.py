from typing import Pattern
from recognizers_text.utilities import RegExpUtility
from recognizers_date_time.resources.arabic_date_time import ArabicDateTime
from recognizers_date_time.date_time.base_date import DateTimeUtilityConfiguration


class ArabicDateTimeUtilityConfiguration(DateTimeUtilityConfiguration):

    later_regex: Pattern = RegExpUtility.get_safe_reg_exp(ArabicDateTime.LaterRegex)
    ago_regex: Pattern = RegExpUtility.get_safe_reg_exp(ArabicDateTime.AgoRegex)
    in_connector_regex: Pattern = RegExpUtility.get_safe_reg_exp(ArabicDateTime.InConnectorRegex)
    since_year_suffix_regex: Pattern = RegExpUtility.get_safe_reg_exp(ArabicDateTime.SinceYearSuffixRegex)
    within_next_prefix_regex: Pattern = RegExpUtility.get_safe_reg_exp(ArabicDateTime.WithinNextPrefixRegex)
    am_desc_regex: Pattern = RegExpUtility.get_safe_reg_exp(ArabicDateTime.AmDescRegex)
    pm_desc__regex: Pattern = RegExpUtility.get_safe_reg_exp(ArabicDateTime.PmDescRegex)
    am_pm_desc_regex: Pattern = RegExpUtility.get_safe_reg_exp(ArabicDateTime.AmPmDescRegex)
    range_unit_regex: Pattern = RegExpUtility.get_safe_reg_exp(ArabicDateTime.RangeUnitRegex)
    time_unit_regex: Pattern = RegExpUtility.get_safe_reg_exp(ArabicDateTime.TimeUnitRegex)
    date_unit_regex: Pattern = RegExpUtility.get_safe_reg_exp(ArabicDateTime.DateUnitRegex)
    common_date_prefix_regex: Pattern = RegExpUtility.get_safe_reg_exp(ArabicDateTime.CommonDatePrefixRegex)
    range_prefix_regex: Pattern = RegExpUtility.get_safe_reg_exp(ArabicDateTime.RangePrefixRegex)
    check_both_before_after: bool = ArabicDateTime.CheckBothBeforeAfter
