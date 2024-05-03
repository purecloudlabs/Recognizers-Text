#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from typing import Pattern, List, Dict
from recognizers_number import (BaseNumberExtractor, BaseNumberParser,
                                FrenchOrdinalExtractor, FrenchIntegerExtractor, FrenchNumberParserConfiguration)
from recognizers_text.utilities import RegExpUtility
from ...resources.french_date_time import FrenchDateTime
from ..extractors import DateTimeExtractor
from ..base_duration import BaseDurationExtractor
from ..base_date import DateExtractorConfiguration, DateTimeUtilityConfiguration
from ..utilities import DateTimeUtilityConfiguration
from .duration_extractor_config import FrenchDurationExtractorConfiguration
from .base_configs import FrenchDateTimeUtilityConfiguration
from ..constants import Constants
from ...resources.base_date_time import BaseDateTime
from ..utilities import DateTimeOptions


class FrenchDateExtractorConfiguration(DateExtractorConfiguration):

    def __init__(self):
        super().__init__(FrenchDateTime())
        self.ordinal_extractor: BaseNumberExtractor = FrenchOrdinalExtractor()
        self.integer_extractor: BaseNumberExtractor = FrenchIntegerExtractor()
        self.number_parser: BaseNumberParser = BaseNumberParser(FrenchNumberParserConfiguration())
        self.duration_extractor: DateTimeExtractor = BaseDurationExtractor(FrenchDurationExtractorConfiguration())
        self.utility_configuration: DateTimeUtilityConfiguration = FrenchDateTimeUtilityConfiguration()
        self.implicit_date_list: List[Pattern] = [
            RegExpUtility.get_safe_reg_exp(FrenchDateTime.OnRegex),
            RegExpUtility.get_safe_reg_exp(FrenchDateTime.RelaxedOnRegex),
            RegExpUtility.get_safe_reg_exp(FrenchDateTime.SpecialDayRegex),
            RegExpUtility.get_safe_reg_exp(FrenchDateTime.ThisRegex),
            RegExpUtility.get_safe_reg_exp(FrenchDateTime.LastDateRegex),
            RegExpUtility.get_safe_reg_exp(FrenchDateTime.NextDateRegex),
            RegExpUtility.get_safe_reg_exp(FrenchDateTime.StrictWeekDay),
            RegExpUtility.get_safe_reg_exp(FrenchDateTime.WeekDayOfMonthRegex),
            RegExpUtility.get_safe_reg_exp(FrenchDateTime.SpecialDate),
        ]

    @property
    def date_regex_list(self) -> List[Pattern]:
        if FrenchDateTime.DefaultLanguageFallback == Constants.DEFAULT_LANGUAGE_FALLBACK_DMY:
            date_extractor_4 = FrenchDateTime.DateExtractor5
            date_extractor_5 = FrenchDateTime.DateExtractor4
            date_extractor_6 = FrenchDateTime.DateExtractor7
            date_extractor_7 = FrenchDateTime.DateExtractor6
        else:
            date_extractor_4 = FrenchDateTime.DateExtractor4
            date_extractor_5 = FrenchDateTime.DateExtractor5
            date_extractor_6 = FrenchDateTime.DateExtractor6
            date_extractor_7 = FrenchDateTime.DateExtractor7

        return [
            RegExpUtility.get_safe_reg_exp(FrenchDateTime.DateExtractor1),
            RegExpUtility.get_safe_reg_exp(FrenchDateTime.DateExtractor2),
            RegExpUtility.get_safe_reg_exp(FrenchDateTime.DateExtractor3),
            RegExpUtility.get_safe_reg_exp(date_extractor_4),
            RegExpUtility.get_safe_reg_exp(date_extractor_5),
            RegExpUtility.get_safe_reg_exp(date_extractor_6),
            RegExpUtility.get_safe_reg_exp(date_extractor_7),
            RegExpUtility.get_safe_reg_exp(FrenchDateTime.DateExtractor8),
            RegExpUtility.get_safe_reg_exp(FrenchDateTime.DateExtractor9),
            RegExpUtility.get_safe_reg_exp(FrenchDateTime.DateExtractorA),
        ]

