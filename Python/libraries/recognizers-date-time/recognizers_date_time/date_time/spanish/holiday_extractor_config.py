#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from typing import List, Pattern

from recognizers_text.utilities import RegExpUtility

from ...resources.spanish_date_time import SpanishDateTime
from ..base_holiday import HolidayExtractorConfiguration


class SpanishHolidayExtractorConfiguration(HolidayExtractorConfiguration):
    @property
    def holiday_regexes(self) -> List[Pattern]:
        return self._holiday_regexes

    def __init__(self):
        self._holiday_regexes = [
            RegExpUtility.get_safe_reg_exp(SpanishDateTime.HolidayRegex1),
            RegExpUtility.get_safe_reg_exp(SpanishDateTime.HolidayRegex2),
            RegExpUtility.get_safe_reg_exp(SpanishDateTime.HolidayRegex3),
        ]
