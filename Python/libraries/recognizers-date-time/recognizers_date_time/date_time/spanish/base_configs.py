#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from typing import Pattern
from recognizers_text.utilities import RegExpUtility
from recognizers_date_time.date_time.base_date import DateTimeUtilityConfiguration
from recognizers_date_time.resources.spanish_date_time import SpanishDateTime


class SpanishDateTimeUtilityConfiguration(DateTimeUtilityConfiguration):

    later_regex: Pattern = RegExpUtility.get_safe_reg_exp(SpanishDateTime.LaterRegex)
    ago_regex: Pattern = RegExpUtility.get_safe_reg_exp(SpanishDateTime.AgoRegex)
    in_connector_regex: Pattern = RegExpUtility.get_safe_reg_exp(SpanishDateTime.InConnectorRegex)
    range_unit_regex: Pattern = RegExpUtility.get_safe_reg_exp(SpanishDateTime.RangeUnitRegex)
    am_desc_regex: Pattern = RegExpUtility.get_safe_reg_exp(SpanishDateTime.AmDescRegex)
    pm_desc__regex: Pattern = RegExpUtility.get_safe_reg_exp(SpanishDateTime.PmDescRegex)
    am_pm_desc_regex: Pattern = RegExpUtility.get_safe_reg_exp(SpanishDateTime.AmPmDescRegex)
    time_unit_regex: Pattern = RegExpUtility.get_safe_reg_exp(SpanishDateTime.TimeUnitRegex)
    within_next_prefix_regex: Pattern = RegExpUtility.get_safe_reg_exp(SpanishDateTime.WithinNextPrefixRegex)
    common_date_prefix_regex: Pattern = RegExpUtility.get_safe_reg_exp(SpanishDateTime.CommonDatePrefixRegex)
    range_prefix_regex: Pattern = RegExpUtility.get_safe_reg_exp(SpanishDateTime.RangePrefixRegex)
    date_unit_regex: Pattern = RegExpUtility.get_safe_reg_exp(SpanishDateTime.DateUnitRegex)
    check_both_before_after: bool = SpanishDateTime.CheckBothBeforeAfter
