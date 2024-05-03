from typing import Pattern
from recognizers_text.utilities import RegExpUtility
from recognizers_date_time.date_time.base_date import DateTimeUtilityConfiguration
from recognizers_date_time.resources.catalan_date_time import CatalanDateTime


class CatalanDateTimeUtilityConfiguration(DateTimeUtilityConfiguration):

    later_regex: Pattern = RegExpUtility.get_safe_reg_exp(f'^[.]')
    ago_regex: Pattern = RegExpUtility.get_safe_reg_exp(f'^[.]')
    in_connector_regex: Pattern = RegExpUtility.get_safe_reg_exp(CatalanDateTime.InConnectorRegex)
    range_unit_regex: Pattern = RegExpUtility.get_safe_reg_exp(CatalanDateTime.RangeUnitRegex)
    am_desc_regex: Pattern = RegExpUtility.get_safe_reg_exp(CatalanDateTime.AmDescRegex)
    pm_desc__regex: Pattern = RegExpUtility.get_safe_reg_exp(CatalanDateTime.PmDescRegex)
    am_pm_desc_regex: Pattern = RegExpUtility.get_safe_reg_exp(CatalanDateTime.AmPmDescRegex)
    within_next_prefix_regex: Pattern = RegExpUtility.get_safe_reg_exp(f'^[.]')
    common_date_prefix_regex: Pattern = RegExpUtility.get_safe_reg_exp(f'^[.]')
    range_prefix_regex: Pattern = RegExpUtility.get_safe_reg_exp(CatalanDateTime.RangePrefixRegex)
    date_unit_regex: Pattern = RegExpUtility.get_safe_reg_exp(f'^[.]')
    time_unit_regex: Pattern = RegExpUtility.get_safe_reg_exp(f'^[.]')
    check_both_before_after: bool = CatalanDateTime.CheckBothBeforeAfter
