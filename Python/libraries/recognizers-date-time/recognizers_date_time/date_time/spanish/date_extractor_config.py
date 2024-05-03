#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from typing import Pattern, List, Dict
from recognizers_number import (BaseNumberExtractor, BaseNumberParser,
                                SpanishOrdinalExtractor, SpanishIntegerExtractor, SpanishNumberParserConfiguration)
from recognizers_text.utilities import RegExpUtility
from ...resources.spanish_date_time import SpanishDateTime
from ..extractors import DateTimeExtractor
from ..base_duration import BaseDurationExtractor
from ..base_date import DateExtractorConfiguration, DateTimeUtilityConfiguration
from ..utilities import DateTimeUtilityConfiguration
from .duration_extractor_config import SpanishDurationExtractorConfiguration
from .base_configs import SpanishDateTimeUtilityConfiguration
from ..constants import Constants
from ...resources.base_date_time import BaseDateTime


class SpanishDateExtractorConfiguration(DateExtractorConfiguration):

    def __init__(self):
        super().__init__(SpanishDateTime())
        self.ordinal_extractor: BaseNumberExtractor = SpanishOrdinalExtractor()
        self.integer_extractor: BaseNumberExtractor = SpanishIntegerExtractor()
        self.number_parser: BaseNumberParser = BaseNumberParser(SpanishNumberParserConfiguration())
        self.duration_extractor: BaseDurationExtractor = BaseDurationExtractor(SpanishDurationExtractorConfiguration())
        self.utility_configuration: DateTimeUtilityConfiguration = SpanishDateTimeUtilityConfiguration()
        self.implicit_date_list: List[Pattern] = [
            RegExpUtility.get_safe_reg_exp(SpanishDateTime.OnRegex),
            RegExpUtility.get_safe_reg_exp(SpanishDateTime.RelaxedOnRegex),
            RegExpUtility.get_safe_reg_exp(SpanishDateTime.SpecialDayRegex),
            RegExpUtility.get_safe_reg_exp(SpanishDateTime.ThisRegex),
            RegExpUtility.get_safe_reg_exp(SpanishDateTime.LastDateRegex),
            RegExpUtility.get_safe_reg_exp(SpanishDateTime.NextDateRegex),
            RegExpUtility.get_safe_reg_exp(SpanishDateTime.WeekDayRegex),
            RegExpUtility.get_safe_reg_exp(SpanishDateTime.WeekDayOfMonthRegex),
            RegExpUtility.get_safe_reg_exp(SpanishDateTime.SpecialDateRegex),
        ]

    @property
    def date_regex_list(self) -> List[Pattern]:
        if SpanishDateTime.DefaultLanguageFallback == Constants.DEFAULT_LANGUAGE_FALLBACK_DMY:
            date_extractor_4 = SpanishDateTime.DateExtractor5
            date_extractor_5 = SpanishDateTime.DateExtractor8
            date_extractor_6 = SpanishDateTime.DateExtractor9
            date_extractor_8 = SpanishDateTime.DateExtractor4
            date_extractor_7 = SpanishDateTime.DateExtractor6
            date_extractor_9 = SpanishDateTime.DateExtractor7
        else:
            date_extractor_4 = SpanishDateTime.DateExtractor4
            date_extractor_5 = SpanishDateTime.DateExtractor6
            date_extractor_6 = SpanishDateTime.DateExtractor7
            date_extractor_8 = SpanishDateTime.DateExtractor5
            date_extractor_7 = SpanishDateTime.DateExtractor8
            date_extractor_9 = SpanishDateTime.DateExtractor9

        return [
            RegExpUtility.get_safe_reg_exp(SpanishDateTime.DateExtractor1),
            RegExpUtility.get_safe_reg_exp(SpanishDateTime.DateExtractor2),
            RegExpUtility.get_safe_reg_exp(SpanishDateTime.DateExtractor3),
            RegExpUtility.get_safe_reg_exp(date_extractor_4),
            RegExpUtility.get_safe_reg_exp(date_extractor_5),
            RegExpUtility.get_safe_reg_exp(date_extractor_6),
            RegExpUtility.get_safe_reg_exp(date_extractor_7),
            RegExpUtility.get_safe_reg_exp(date_extractor_8),
            RegExpUtility.get_safe_reg_exp(date_extractor_9),
            RegExpUtility.get_safe_reg_exp(SpanishDateTime.DateExtractor10),
        ]

