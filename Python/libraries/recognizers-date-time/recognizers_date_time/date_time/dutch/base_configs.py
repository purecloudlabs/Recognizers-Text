#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from typing import Pattern
from recognizers_text.utilities import RegExpUtility
from ...resources.dutch_date_time import DutchDateTime
from ..base_date import DateTimeUtilityConfiguration


class DutchDateTimeUtilityConfiguration(DateTimeUtilityConfiguration):

    later_regex: Pattern = RegExpUtility.get_safe_reg_exp(DutchDateTime.LaterRegex)
    ago_regex: Pattern = RegExpUtility.get_safe_reg_exp(DutchDateTime.AgoRegex)
    in_connector_regex: Pattern = RegExpUtility.get_safe_reg_exp(DutchDateTime.InConnectorRegex)
    range_unit_regex: Pattern = RegExpUtility.get_safe_reg_exp(DutchDateTime.RangeUnitRegex)
    am_desc_regex: Pattern = RegExpUtility.get_safe_reg_exp(DutchDateTime.AmDescRegex)
    pm_desc__regex: Pattern = RegExpUtility.get_safe_reg_exp(DutchDateTime.PmDescRegex)
    am_pm_desc_regex: Pattern = RegExpUtility.get_safe_reg_exp(DutchDateTime.AmPmDescRegex)
    time_unit_regex = RegExpUtility.get_safe_reg_exp(DutchDateTime.TimeUnitRegex)
    within_next_prefix_regex: Pattern = RegExpUtility.get_safe_reg_exp(DutchDateTime.WithinNextPrefixRegex)
    common_date_prefix_regex: Pattern = RegExpUtility.get_safe_reg_exp(DutchDateTime.CommonDatePrefixRegex)
    range_prefix_regex: Pattern = RegExpUtility.get_safe_reg_exp(DutchDateTime.RangePrefixRegex)
    date_unit_regex: Pattern = RegExpUtility.get_safe_reg_exp(DutchDateTime.DateUnitRegex)
    since_year_suffix_regex: Pattern = RegExpUtility.get_safe_reg_exp(DutchDateTime.SinceYearSuffixRegex)
    check_both_before_after: bool = DutchDateTime.CheckBothBeforeAfter
