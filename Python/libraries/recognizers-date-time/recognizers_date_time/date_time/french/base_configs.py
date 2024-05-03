#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from typing import Pattern
from recognizers_text.utilities import RegExpUtility
from ...resources.french_date_time import FrenchDateTime
from ..base_date import DateTimeUtilityConfiguration


class FrenchDateTimeUtilityConfiguration(DateTimeUtilityConfiguration):

    later_regex: Pattern = RegExpUtility.get_safe_reg_exp( FrenchDateTime.LaterRegex)
    ago_regex: Pattern = RegExpUtility.get_safe_reg_exp( FrenchDateTime.AgoPrefixRegex)
    in_connector_regex: Pattern = RegExpUtility.get_safe_reg_exp( FrenchDateTime.InConnectorRegex)
    range_unit_regex: Pattern = RegExpUtility.get_safe_reg_exp( FrenchDateTime.RangeUnitRegex)
    am_desc_regex: Pattern = RegExpUtility.get_safe_reg_exp( FrenchDateTime.AmDescRegex)
    pm_desc__regex: Pattern = RegExpUtility.get_safe_reg_exp( FrenchDateTime.PmDescRegex)
    am_pm_desc_regex: Pattern = RegExpUtility.get_safe_reg_exp( FrenchDateTime.AmPmDescRegex)
    time_unit_regex: Pattern = RegExpUtility.get_safe_reg_exp( FrenchDateTime.TimeUnitRegex)
    within_next_prefix_regex: Pattern = RegExpUtility.get_safe_reg_exp( FrenchDateTime.WithinNextPrefixRegex)
    common_date_prefix_regex: Pattern = RegExpUtility.get_safe_reg_exp( FrenchDateTime.CommonDatePrefixRegex)
    range_prefix_regex: Pattern = RegExpUtility.get_safe_reg_exp( FrenchDateTime.RangePrefixRegex )
    date_unit_regex: Pattern = RegExpUtility.get_safe_reg_exp( FrenchDateTime.DateUnitRegex )
    check_both_before_after: bool = FrenchDateTime.CheckBothBeforeAfter
