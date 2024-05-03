#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from typing import Pattern
from recognizers_text.utilities import RegExpUtility
from recognizers_date_time.date_time.base_date import DateTimeUtilityConfiguration
from recognizers_date_time.resources.english_date_time import EnglishDateTime


class EnglishDateTimeUtilityConfiguration(DateTimeUtilityConfiguration):

    later_regex: Pattern = RegExpUtility.get_safe_reg_exp( EnglishDateTime.LaterRegex)
    ago_regex: Pattern = RegExpUtility.get_safe_reg_exp( EnglishDateTime.AgoRegex)
    in_connector_regex: Pattern = RegExpUtility.get_safe_reg_exp( EnglishDateTime.InConnectorRegex)
    range_unit_regex: Pattern = RegExpUtility.get_safe_reg_exp( EnglishDateTime.RangeUnitRegex)
    am_desc_regex: Pattern = RegExpUtility.get_safe_reg_exp( EnglishDateTime.AmDescRegex)
    pm_desc__regex: Pattern = RegExpUtility.get_safe_reg_exp( EnglishDateTime.PmDescRegex)
    am_pm_desc_regex: Pattern = RegExpUtility.get_safe_reg_exp( EnglishDateTime.AmPmDescRegex)
    time_unit_regex: Pattern = RegExpUtility.get_safe_reg_exp( EnglishDateTime.TimeUnitRegex)
    within_next_prefix_regex: Pattern = RegExpUtility.get_safe_reg_exp( EnglishDateTime.WithinNextPrefixRegex)
    common_date_prefix_regex: Pattern = RegExpUtility.get_safe_reg_exp( EnglishDateTime.CommonDatePrefixRegex)
    range_prefix_regex: Pattern = RegExpUtility.get_safe_reg_exp( EnglishDateTime.RangePrefixRegex )
    date_unit_regex: Pattern = RegExpUtility.get_safe_reg_exp( EnglishDateTime.DateUnitRegex )
    check_both_before_after: bool = EnglishDateTime.CheckBothBeforeAfter
