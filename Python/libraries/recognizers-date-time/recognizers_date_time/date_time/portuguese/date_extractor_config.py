#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from typing import List, Pattern

from recognizers_number import (
    BaseNumberExtractor,
    BaseNumberParser,
    PortugueseIntegerExtractor,
    PortugueseNumberParserConfiguration,
    PortugueseOrdinalExtractor,
)
from recognizers_text.utilities import RegExpUtility

from ...resources.portuguese_date_time import PortugueseDateTime
from ..base_date import DateExtractorConfiguration, DateTimeUtilityConfiguration
from ..base_duration import BaseDurationExtractor
from ..constants import Constants
from ..utilities import DateTimeUtilityConfiguration
from .base_configs import PortugueseDateTimeUtilityConfiguration
from .duration_extractor_config import PortugueseDurationExtractorConfiguration


class PortugueseDateExtractorConfiguration(DateExtractorConfiguration):

    def __init__(self):
        super().__init__(PortugueseDateTime())
        self.ordinal_extractor: BaseNumberExtractor = PortugueseOrdinalExtractor()
        self.integer_extractor: BaseNumberExtractor = PortugueseIntegerExtractor()
        self.number_parser: BaseNumberParser = BaseNumberParser(PortugueseNumberParserConfiguration())
        self.duration_extractor: BaseDurationExtractor = BaseDurationExtractor(
            PortugueseDurationExtractorConfiguration()
        )
        self.utility_configuration: DateTimeUtilityConfiguration = PortugueseDateTimeUtilityConfiguration()
        self.implicit_date_list: List[Pattern] = [
            RegExpUtility.get_safe_reg_exp(PortugueseDateTime.OnRegex),
            RegExpUtility.get_safe_reg_exp(PortugueseDateTime.RelaxedOnRegex),
            RegExpUtility.get_safe_reg_exp(PortugueseDateTime.SpecialDayRegex),
            RegExpUtility.get_safe_reg_exp(PortugueseDateTime.ThisRegex),
            RegExpUtility.get_safe_reg_exp(PortugueseDateTime.LastDateRegex),
            RegExpUtility.get_safe_reg_exp(PortugueseDateTime.NextDateRegex),
            RegExpUtility.get_safe_reg_exp(PortugueseDateTime.WeekDayRegex),
            RegExpUtility.get_safe_reg_exp(PortugueseDateTime.WeekDayOfMonthRegex),
            RegExpUtility.get_safe_reg_exp(PortugueseDateTime.SpecialDateRegex),
        ]

    @property
    def date_regex_list(self) -> List[Pattern]:
        if PortugueseDateTime.DefaultLanguageFallback == Constants.DEFAULT_LANGUAGE_FALLBACK_DMY:
            date_extractor_4 = PortugueseDateTime.DateExtractor5
            date_extractor_5 = PortugueseDateTime.DateExtractor4
            date_extractor_6 = PortugueseDateTime.DateExtractor8
            date_extractor_8 = PortugueseDateTime.DateExtractor6
            date_extractor_7 = PortugueseDateTime.DateExtractor9
            date_extractor_9 = PortugueseDateTime.DateExtractor7
        else:
            date_extractor_4 = PortugueseDateTime.DateExtractor4
            date_extractor_5 = PortugueseDateTime.DateExtractor5
            date_extractor_6 = PortugueseDateTime.DateExtractor6
            date_extractor_8 = PortugueseDateTime.DateExtractor8
            date_extractor_7 = PortugueseDateTime.DateExtractor7
            date_extractor_9 = PortugueseDateTime.DateExtractor9

        return [
            RegExpUtility.get_safe_reg_exp(PortugueseDateTime.DateExtractor1),
            RegExpUtility.get_safe_reg_exp(PortugueseDateTime.DateExtractor2),
            RegExpUtility.get_safe_reg_exp(PortugueseDateTime.DateExtractor3),
            RegExpUtility.get_safe_reg_exp(date_extractor_4),
            RegExpUtility.get_safe_reg_exp(date_extractor_5),
            RegExpUtility.get_safe_reg_exp(date_extractor_6),
            RegExpUtility.get_safe_reg_exp(date_extractor_7),
            RegExpUtility.get_safe_reg_exp(date_extractor_8),
            RegExpUtility.get_safe_reg_exp(date_extractor_9),
            RegExpUtility.get_safe_reg_exp(PortugueseDateTime.DateExtractor10),
        ]
