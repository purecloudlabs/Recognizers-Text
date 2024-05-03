#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from typing import Pattern, List
from recognizers_number import (BaseNumberExtractor, BaseNumberParser,
                                EnglishOrdinalExtractor, EnglishIntegerExtractor, EnglishNumberParserConfiguration)
from recognizers_text.utilities import RegExpUtility
from ...resources.english_date_time import EnglishDateTime
from ..extractors import DateTimeExtractor
from ..base_duration import BaseDurationExtractor
from ..base_date import DateExtractorConfiguration, DateTimeUtilityConfiguration
from ..utilities import DateTimeUtilityConfiguration
from .duration_extractor_config import EnglishDurationExtractorConfiguration
from .base_configs import EnglishDateTimeUtilityConfiguration


class EnglishDateExtractorConfiguration(DateExtractorConfiguration):

    def __init__(self, dmyDateFormat: bool = False):
        self._dmy_date_format = dmyDateFormat
        super().__init__(EnglishDateTime())
        self.ordinal_extractor: BaseNumberExtractor = EnglishOrdinalExtractor()
        self.integer_extractor: BaseNumberExtractor = EnglishIntegerExtractor()
        self.number_parser: BaseNumberParser = BaseNumberParser(EnglishNumberParserConfiguration())
        self.duration_extractor: DateTimeExtractor = BaseDurationExtractor(EnglishDurationExtractorConfiguration())
        self.utility_configuration: DateTimeUtilityConfiguration = EnglishDateTimeUtilityConfiguration()
        self.implicit_date_list: List[Pattern] = [
            RegExpUtility.get_safe_reg_exp(EnglishDateTime.OnRegex),
            RegExpUtility.get_safe_reg_exp(EnglishDateTime.RelaxedOnRegex),
            RegExpUtility.get_safe_reg_exp(EnglishDateTime.SpecialDayRegex),
            RegExpUtility.get_safe_reg_exp(EnglishDateTime.ThisRegex),
            RegExpUtility.get_safe_reg_exp(EnglishDateTime.LastDateRegex),
            RegExpUtility.get_safe_reg_exp(EnglishDateTime.NextDateRegex),
            RegExpUtility.get_safe_reg_exp(EnglishDateTime.SingleWeekDayRegex),
            RegExpUtility.get_safe_reg_exp(EnglishDateTime.WeekDayOfMonthRegex),
            RegExpUtility.get_safe_reg_exp(EnglishDateTime.SpecialDate),
            RegExpUtility.get_safe_reg_exp(EnglishDateTime.SpecialDayWithNumRegex),
            RegExpUtility.get_safe_reg_exp(EnglishDateTime.RelativeWeekDayRegex)
        ]

    @property
    def date_regex_list(self) -> List[Pattern]:
        if self._dmy_date_format:
            date_extractor_4 = EnglishDateTime.DateExtractor5
            date_extractor_5 = EnglishDateTime.DateExtractor8
            date_extractor_6 = EnglishDateTime.DateExtractor9L
            date_extractor_7 = EnglishDateTime.DateExtractor9S
            date_extractor_8 = EnglishDateTime.DateExtractor4
            date_extractor_9 = EnglishDateTime.DateExtractor6
            date_extractor_10 = EnglishDateTime.DateExtractor7L
            date_extractor_11 = EnglishDateTime.DateExtractor7S
        else:
            date_extractor_4 = EnglishDateTime.DateExtractor4
            date_extractor_5 = EnglishDateTime.DateExtractor6
            date_extractor_6 = EnglishDateTime.DateExtractor7L
            date_extractor_7 = EnglishDateTime.DateExtractor7S
            date_extractor_8 = EnglishDateTime.DateExtractor5
            date_extractor_9 = EnglishDateTime.DateExtractor8
            date_extractor_10 = EnglishDateTime.DateExtractor9L
            date_extractor_11 = EnglishDateTime.DateExtractor9S

        return [
            RegExpUtility.get_safe_reg_exp(EnglishDateTime.DateExtractor1),
            RegExpUtility.get_safe_reg_exp(EnglishDateTime.DateExtractor3),
            RegExpUtility.get_safe_reg_exp(date_extractor_4),
            RegExpUtility.get_safe_reg_exp(date_extractor_5),
            RegExpUtility.get_safe_reg_exp(date_extractor_6),
            RegExpUtility.get_safe_reg_exp(date_extractor_7),
            RegExpUtility.get_safe_reg_exp(date_extractor_8),
            RegExpUtility.get_safe_reg_exp(date_extractor_9),
            RegExpUtility.get_safe_reg_exp(date_extractor_10),
            RegExpUtility.get_safe_reg_exp(date_extractor_11),
            RegExpUtility.get_safe_reg_exp(EnglishDateTime.DateExtractorA),
        ]
