#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from typing import List, Pattern

from recognizers_number import (
    BaseNumberExtractor,
    BaseNumberParser,
    DutchIntegerExtractor,
    DutchNumberParserConfiguration,
    DutchOrdinalExtractor,
)
from recognizers_text.utilities import RegExpUtility

from ...resources.dutch_date_time import DutchDateTime
from ..base_date import DateExtractorConfiguration, DateTimeUtilityConfiguration
from ..base_duration import BaseDurationExtractor
from ..constants import Constants
from ..extractors import DateTimeExtractor
from ..utilities import DateTimeUtilityConfiguration
from .base_configs import DutchDateTimeUtilityConfiguration
from .duration_extractor_config import DutchDurationExtractorConfiguration


class DutchDateExtractorConfiguration(DateExtractorConfiguration):

    def __init__(self):
        super().__init__(DutchDateTime())
        self.ordinal_extractor: BaseNumberExtractor = DutchOrdinalExtractor()
        self.integer_extractor: BaseNumberExtractor = DutchIntegerExtractor()
        self.number_parser: BaseNumberParser = BaseNumberParser(DutchNumberParserConfiguration())
        self.duration_extractor: DateTimeExtractor = BaseDurationExtractor(DutchDurationExtractorConfiguration())
        self.utility_configuration: DateTimeUtilityConfiguration = DutchDateTimeUtilityConfiguration()
        self.implicit_date_list: List[Pattern] = [
            RegExpUtility.get_safe_reg_exp(DutchDateTime.OnRegex),
            RegExpUtility.get_safe_reg_exp(DutchDateTime.RelaxedOnRegex),
            RegExpUtility.get_safe_reg_exp(DutchDateTime.SpecialDayRegex),
            RegExpUtility.get_safe_reg_exp(DutchDateTime.ThisRegex),
            RegExpUtility.get_safe_reg_exp(DutchDateTime.LastDateRegex),
            RegExpUtility.get_safe_reg_exp(DutchDateTime.NextDateRegex),
            RegExpUtility.get_safe_reg_exp(DutchDateTime.SingleWeekDayRegex),
            RegExpUtility.get_safe_reg_exp(DutchDateTime.WeekDayOfMonthRegex),
            RegExpUtility.get_safe_reg_exp(DutchDateTime.SpecialDate),
            RegExpUtility.get_safe_reg_exp(DutchDateTime.SpecialDayWithNumRegex),
            RegExpUtility.get_safe_reg_exp(DutchDateTime.RelativeWeekDayRegex),
        ]

    @property
    def date_regex_list(self) -> List[Pattern]:
        if DutchDateTime.DefaultLanguageFallback == Constants.DEFAULT_LANGUAGE_FALLBACK_DMY:
            date_extractor_4 = DutchDateTime.DateExtractor5
            date_extractor_5 = DutchDateTime.DateExtractor8
            date_extractor_6 = DutchDateTime.DateExtractor9L
            date_extractor_7 = DutchDateTime.DateExtractor9S
            date_extractor_8 = DutchDateTime.DateExtractor4
            date_extractor_9 = DutchDateTime.DateExtractor6
            date_extractor_10 = DutchDateTime.DateExtractor7L
            date_extractor_11 = DutchDateTime.DateExtractor7S
        else:
            date_extractor_4 = DutchDateTime.DateExtractor4
            date_extractor_5 = DutchDateTime.DateExtractor6
            date_extractor_6 = DutchDateTime.DateExtractor7L
            date_extractor_7 = DutchDateTime.DateExtractor7S
            date_extractor_8 = DutchDateTime.DateExtractor5
            date_extractor_9 = DutchDateTime.DateExtractor8
            date_extractor_10 = DutchDateTime.DateExtractor9L
            date_extractor_11 = DutchDateTime.DateExtractor9S

        return [
            RegExpUtility.get_safe_reg_exp(DutchDateTime.DateExtractor1),
            RegExpUtility.get_safe_reg_exp(DutchDateTime.DateExtractor3),
            RegExpUtility.get_safe_reg_exp(date_extractor_4),
            RegExpUtility.get_safe_reg_exp(date_extractor_5),
            RegExpUtility.get_safe_reg_exp(date_extractor_6),
            RegExpUtility.get_safe_reg_exp(date_extractor_7),
            RegExpUtility.get_safe_reg_exp(date_extractor_8),
            RegExpUtility.get_safe_reg_exp(date_extractor_9),
            RegExpUtility.get_safe_reg_exp(date_extractor_10),
            RegExpUtility.get_safe_reg_exp(date_extractor_11),
            RegExpUtility.get_safe_reg_exp(DutchDateTime.DateExtractorA),
        ]
