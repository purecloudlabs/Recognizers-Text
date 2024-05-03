#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from typing import Pattern
from recognizers_text.utilities import RegExpUtility
from ...resources.german_date_time import GermanDateTime
from ..base_date import DateTimeUtilityConfiguration


class GermanDateTimeUtilityConfiguration(DateTimeUtilityConfiguration):

    later_regex: Pattern = RegExpUtility.get_safe_reg_exp(GermanDateTime.LaterRegex)
    ago_regex: Pattern = RegExpUtility.get_safe_reg_exp(GermanDateTime.AgoRegex)
    in_connector_regex: Pattern = RegExpUtility.get_safe_reg_exp(GermanDateTime.InConnectorRegex)
    range_unit_regex: Pattern = RegExpUtility.get_safe_reg_exp(GermanDateTime.RangeUnitRegex)
    am_desc_regex: Pattern = RegExpUtility.get_safe_reg_exp(GermanDateTime.AmDescRegex)
    pm_desc__regex: Pattern = RegExpUtility.get_safe_reg_exp(GermanDateTime.PmDescRegex)
    am_pm_desc_regex: Pattern = RegExpUtility.get_safe_reg_exp(GermanDateTime.AmPmDescRegex)
    time_unit_regex: Pattern = RegExpUtility.get_safe_reg_exp(GermanDateTime.TimeUnitRegex)
    within_next_prefix_regex: Pattern = RegExpUtility.get_safe_reg_exp(GermanDateTime.WithinNextPrefixRegex)
    common_date_prefix_regex: Pattern = RegExpUtility.get_safe_reg_exp(GermanDateTime.CommonDatePrefixRegex)
    range_prefix_regex: Pattern = RegExpUtility.get_safe_reg_exp(GermanDateTime.RangePrefixRegex)
    date_unit_regex: Pattern = RegExpUtility.get_safe_reg_exp(GermanDateTime.DateUnitRegex)
    check_both_before_after: bool = GermanDateTime.CheckBothBeforeAfter
