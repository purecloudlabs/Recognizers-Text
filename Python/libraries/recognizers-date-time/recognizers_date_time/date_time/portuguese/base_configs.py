#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from typing import Pattern
from recognizers_text.utilities import RegExpUtility
from recognizers_date_time.date_time.base_date import DateTimeUtilityConfiguration
from recognizers_date_time.resources.portuguese_date_time import PortugueseDateTime


class PortugueseDateTimeUtilityConfiguration(DateTimeUtilityConfiguration):

    later_regex: Pattern = RegExpUtility.get_safe_reg_exp(PortugueseDateTime.LaterRegex)
    ago_regex: Pattern = RegExpUtility.get_safe_reg_exp(PortugueseDateTime.AgoRegex)
    in_connector_regex: Pattern = RegExpUtility.get_safe_reg_exp(PortugueseDateTime.InConnectorRegex)
    range_unit_regex: Pattern = RegExpUtility.get_safe_reg_exp(PortugueseDateTime.RangeUnitRegex)
    am_desc_regex: Pattern = RegExpUtility.get_safe_reg_exp(PortugueseDateTime.AmDescRegex)
    pm_desc__regex: Pattern = RegExpUtility.get_safe_reg_exp(PortugueseDateTime.PmDescRegex)
    am_pm_desc_regex: Pattern = RegExpUtility.get_safe_reg_exp(PortugueseDateTime.AmPmDescRegex)
    time_unit_regex: Pattern = RegExpUtility.get_safe_reg_exp(PortugueseDateTime.TimeUnitRegex)
    within_next_prefix_regex: Pattern = RegExpUtility.get_safe_reg_exp(PortugueseDateTime.WithinNextPrefixRegex)
    common_date_prefix_regex: Pattern = RegExpUtility.get_safe_reg_exp(PortugueseDateTime.CommonDatePrefixRegex)
    range_prefix_regex: Pattern = RegExpUtility.get_safe_reg_exp(PortugueseDateTime.RangePrefixRegex)
    date_unit_regex: Pattern = RegExpUtility.get_safe_reg_exp(PortugueseDateTime.DateUnitRegex)
    check_both_before_after: bool = PortugueseDateTime.CheckBothBeforeAfter
