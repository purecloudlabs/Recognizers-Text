#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from typing import List, Pattern

from recognizers_number import (
    BaseNumberExtractor,
    BaseNumberParser,
    GermanIntegerExtractor,
    GermanNumberParserConfiguration,
    GermanOrdinalExtractor,
)
from recognizers_text.utilities import RegExpUtility

from ...resources.german_date_time import GermanDateTime
from ..base_date import DateExtractorConfiguration, DateTimeUtilityConfiguration
from ..base_duration import BaseDurationExtractor
from ..constants import Constants
from ..utilities import DateTimeUtilityConfiguration
from .base_configs import GermanDateTimeUtilityConfiguration
from .duration_extractor_config import GermanDurationExtractorConfiguration


class GermanDateExtractorConfiguration(DateExtractorConfiguration):

    def __init__(self):
        super().__init__(GermanDateTime())
        self.ordinal_extractor: BaseNumberExtractor = GermanOrdinalExtractor()
        self.integer_extractor: BaseNumberExtractor = GermanIntegerExtractor()
        self.number_parser: BaseNumberParser = BaseNumberParser(GermanNumberParserConfiguration())
        self.duration_extractor: BaseDurationExtractor = BaseDurationExtractor(GermanDurationExtractorConfiguration())
        self.utility_configuration: DateTimeUtilityConfiguration = GermanDateTimeUtilityConfiguration()
        self.implicit_date_list: List[Pattern] = [
            RegExpUtility.get_safe_reg_exp(GermanDateTime.OnRegex),
            RegExpUtility.get_safe_reg_exp(GermanDateTime.RelaxedOnRegex),
            RegExpUtility.get_safe_reg_exp(GermanDateTime.SpecialDayRegex),
            RegExpUtility.get_safe_reg_exp(GermanDateTime.ThisRegex),
            RegExpUtility.get_safe_reg_exp(GermanDateTime.LastDateRegex),
            RegExpUtility.get_safe_reg_exp(GermanDateTime.NextDateRegex),
            RegExpUtility.get_safe_reg_exp(GermanDateTime.SingleWeekDayRegex),
            RegExpUtility.get_safe_reg_exp(GermanDateTime.WeekDayOfMonthRegex),
            RegExpUtility.get_safe_reg_exp(GermanDateTime.SpecialDate),
        ]

    @property
    def date_regex_list(self) -> List[Pattern]:
        if GermanDateTime.DefaultLanguageFallback == Constants.DEFAULT_LANGUAGE_FALLBACK_DMY:
            date_extractor_4 = GermanDateTime.DateExtractor5
            date_extractor_5 = GermanDateTime.DateExtractor4
            date_extractor_6 = GermanDateTime.DateExtractor7
            date_extractor_7 = GermanDateTime.DateExtractor6
        else:
            date_extractor_4 = GermanDateTime.DateExtractor4
            date_extractor_5 = GermanDateTime.DateExtractor5
            date_extractor_6 = GermanDateTime.DateExtractor6
            date_extractor_7 = GermanDateTime.DateExtractor7

        return [
            RegExpUtility.get_safe_reg_exp(GermanDateTime.DateExtractor1),
            RegExpUtility.get_safe_reg_exp(GermanDateTime.DateExtractor2),
            RegExpUtility.get_safe_reg_exp(GermanDateTime.DateExtractor3),
            RegExpUtility.get_safe_reg_exp(date_extractor_4),
            RegExpUtility.get_safe_reg_exp(date_extractor_5),
            RegExpUtility.get_safe_reg_exp(date_extractor_6),
            RegExpUtility.get_safe_reg_exp(date_extractor_7),
            RegExpUtility.get_safe_reg_exp(GermanDateTime.DateExtractor8),
            RegExpUtility.get_safe_reg_exp(GermanDateTime.DateExtractor9),
            RegExpUtility.get_safe_reg_exp(GermanDateTime.DateExtractorA),
        ]
