#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from typing import Pattern, List
from recognizers_number import (BaseNumberExtractor, BaseNumberParser,
                                ItalianOrdinalExtractor, ItalianIntegerExtractor, ItalianNumberParserConfiguration)
from recognizers_text.utilities import RegExpUtility
from ...resources.italian_date_time import ItalianDateTime
from ..base_duration import BaseDurationExtractor
from ..base_date import DateExtractorConfiguration, DateTimeUtilityConfiguration
from ..utilities import DateTimeUtilityConfiguration
from .duration_extractor_config import ItalianDurationExtractorConfiguration
from .base_configs import ItalianDateTimeUtilityConfiguration
from ..constants import Constants


class ItalianDateExtractorConfiguration(DateExtractorConfiguration):

    def __init__(self):
        super().__init__(ItalianDateTime())
        self.ordinal_extractor: BaseNumberExtractor = ItalianOrdinalExtractor()
        self.integer_extractor: BaseNumberExtractor = ItalianIntegerExtractor()
        self.number_parser: BaseNumberParser = BaseNumberParser(ItalianNumberParserConfiguration())
        self.duration_extractor = BaseDurationExtractor(ItalianDurationExtractorConfiguration())
        self.utility_configuration: DateTimeUtilityConfiguration = ItalianDateTimeUtilityConfiguration()
        self.implicit_date_list: List[Pattern] = [
            RegExpUtility.get_safe_reg_exp(ItalianDateTime.OnRegex),
            RegExpUtility.get_safe_reg_exp(ItalianDateTime.RelaxedOnRegex),
            RegExpUtility.get_safe_reg_exp(ItalianDateTime.SpecialDayRegex),
            RegExpUtility.get_safe_reg_exp(ItalianDateTime.ThisRegex),
            RegExpUtility.get_safe_reg_exp(ItalianDateTime.LastDateRegex),
            RegExpUtility.get_safe_reg_exp(ItalianDateTime.NextDateRegex),
            RegExpUtility.get_safe_reg_exp(ItalianDateTime.StrictWeekDay),
            RegExpUtility.get_safe_reg_exp(ItalianDateTime.WeekDayOfMonthRegex),
            RegExpUtility.get_safe_reg_exp(ItalianDateTime.SpecialDate),
        ]

    @property
    def date_regex_list(self) -> List[Pattern]:
        if ItalianDateTime.DefaultLanguageFallback == Constants.DEFAULT_LANGUAGE_FALLBACK_DMY:
            date_extractor_4 = ItalianDateTime.DateExtractor5
            date_extractor_5 = ItalianDateTime.DateExtractor4
            date_extractor_6 = ItalianDateTime.DateExtractor7
            date_extractor_7 = ItalianDateTime.DateExtractor6
        else:
            date_extractor_4 = ItalianDateTime.DateExtractor4
            date_extractor_5 = ItalianDateTime.DateExtractor5
            date_extractor_6 = ItalianDateTime.DateExtractor6
            date_extractor_7 = ItalianDateTime.DateExtractor7

        return [
            RegExpUtility.get_safe_reg_exp(ItalianDateTime.DateExtractor1),
            RegExpUtility.get_safe_reg_exp(ItalianDateTime.DateExtractor2),
            RegExpUtility.get_safe_reg_exp(ItalianDateTime.DateExtractor3),
            RegExpUtility.get_safe_reg_exp(date_extractor_4),
            RegExpUtility.get_safe_reg_exp(date_extractor_5),
            RegExpUtility.get_safe_reg_exp(date_extractor_6),
            RegExpUtility.get_safe_reg_exp(date_extractor_7),
            RegExpUtility.get_safe_reg_exp(ItalianDateTime.DateExtractor8),
            RegExpUtility.get_safe_reg_exp(ItalianDateTime.DateExtractor9),
            RegExpUtility.get_safe_reg_exp(ItalianDateTime.DateExtractorA),
        ]

