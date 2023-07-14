#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from typing import List, Pattern
from recognizers_text.utilities import RegExpUtility

from ..base_holiday import HolidayExtractorConfiguration
from ...resources.catalan_date_time import CatalanDateTime


class CatalanHolidayExtractorConfiguration(HolidayExtractorConfiguration):
    @property
    def holiday_regexes(self) -> List[Pattern]:
        return self._holiday_regexes

    def __init__(self):
        self._holiday_regexes = [
            RegExpUtility.get_safe_reg_exp(CatalanDateTime.HolidayRegex1),
            RegExpUtility.get_safe_reg_exp(CatalanDateTime.HolidayRegex2),
            RegExpUtility.get_safe_reg_exp(CatalanDateTime.HolidayRegex3)
        ]
