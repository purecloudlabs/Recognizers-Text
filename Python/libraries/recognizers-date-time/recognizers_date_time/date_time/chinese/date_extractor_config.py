#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from typing import List, Pattern, Dict

from recognizers_text import RegExpUtility
from recognizers_number import BaseNumberExtractor, BaseNumberParser
from ...resources import ChineseDateTime
from ..constants import Constants
from ..extractors import DateTimeExtractor
from ..base_date import DateTimeUtilityConfiguration
from ..base_date import DateExtractorConfiguration
from ...resources.base_date_time import BaseDateTime


class ChineseDateExtractorConfiguration(DateExtractorConfiguration):

    def __init__(self):
        super().__init__(ChineseDateTime())
        self.implicit_date_list: List[Pattern] = [
            RegExpUtility.get_safe_reg_exp(ChineseDateTime.LunarRegex),
            RegExpUtility.get_safe_reg_exp(ChineseDateTime.SpecialDayRegex),
            RegExpUtility.get_safe_reg_exp(ChineseDateTime.DateThisRegex),
            RegExpUtility.get_safe_reg_exp(ChineseDateTime.DateLastRegex),
            RegExpUtility.get_safe_reg_exp(ChineseDateTime.DateNextRegex),
            RegExpUtility.get_safe_reg_exp(ChineseDateTime.WeekDayRegex),
            RegExpUtility.get_safe_reg_exp(ChineseDateTime.WeekDayOfMonthRegex),
            RegExpUtility.get_safe_reg_exp(ChineseDateTime.SpecialDate)
        ]

    @property
    def date_regex_list(self) -> List[Pattern]:
        return [
            RegExpUtility.get_safe_reg_exp(ChineseDateTime.DateRegexList1),
            RegExpUtility.get_safe_reg_exp(ChineseDateTime.DateRegexList2),
            RegExpUtility.get_safe_reg_exp(ChineseDateTime.DateRegexList3),
            RegExpUtility.get_safe_reg_exp(ChineseDateTime.DateRegexList4),
            RegExpUtility.get_safe_reg_exp(ChineseDateTime.DateRegexList5),
            RegExpUtility.get_safe_reg_exp(ChineseDateTime.DateRegexList6),
            RegExpUtility.get_safe_reg_exp(ChineseDateTime.DateRegexList7),
            RegExpUtility.get_safe_reg_exp(ChineseDateTime.DateRegexList8)
        ]
