from typing import List, Pattern

from recognizers_date_time.date_time.arabic.base_configs import ArabicDateTimeUtilityConfiguration
from recognizers_date_time.date_time.arabic.duration_extractor_config import ArabicDurationExtractorConfiguration
from recognizers_date_time.date_time.base_date import DateExtractorConfiguration, DateTimeUtilityConfiguration
from recognizers_date_time.date_time.base_duration import BaseDurationExtractor
from recognizers_date_time.date_time.constants import Constants
from recognizers_date_time.date_time.extractors import DateTimeExtractor
from recognizers_date_time.resources import ArabicDateTime
from recognizers_number import (
    ArabicIntegerExtractor,
    ArabicNumberParserConfiguration,
    ArabicOrdinalExtractor,
    BaseNumberExtractor,
    BaseNumberParser,
)
from recognizers_text.utilities import RegExpUtility


class ArabicDateExtractorConfiguration(DateExtractorConfiguration):

    def __init__(self):
        super().__init__(ArabicDateTime())
        self.ordinal_extractor: BaseNumberExtractor = ArabicOrdinalExtractor()
        self.integer_extractor: BaseNumberExtractor = ArabicIntegerExtractor()
        self.number_parser: BaseNumberParser = BaseNumberParser(ArabicNumberParserConfiguration())
        self.duration_extractor: DateTimeExtractor = BaseDurationExtractor(ArabicDurationExtractorConfiguration())
        self.utility_configuration: DateTimeUtilityConfiguration = ArabicDateTimeUtilityConfiguration()
        self.implicit_date_list: List[Pattern] = [
            RegExpUtility.get_safe_reg_exp(ArabicDateTime.OnRegex),
            RegExpUtility.get_safe_reg_exp(ArabicDateTime.RelaxedOnRegex),
            RegExpUtility.get_safe_reg_exp(ArabicDateTime.SpecialDayRegex),
            RegExpUtility.get_safe_reg_exp(ArabicDateTime.ThisRegex),
            RegExpUtility.get_safe_reg_exp(ArabicDateTime.LastDateRegex),
            RegExpUtility.get_safe_reg_exp(ArabicDateTime.NextDateRegex),
            RegExpUtility.get_safe_reg_exp(ArabicDateTime.SingleWeekDayRegex),
            RegExpUtility.get_safe_reg_exp(ArabicDateTime.WeekDayOfMonthRegex),
            RegExpUtility.get_safe_reg_exp(ArabicDateTime.SpecialDate),
            RegExpUtility.get_safe_reg_exp(ArabicDateTime.SpecialDayWithNumRegex),
            RegExpUtility.get_safe_reg_exp(ArabicDateTime.RelativeWeekDayRegex),
        ]

    @property
    def date_regex_list(self) -> List[Pattern]:
        if ArabicDateTime.DefaultLanguageFallback == Constants.DEFAULT_LANGUAGE_FALLBACK_DMY:
            date_extractor_4 = ArabicDateTime.DateExtractor5
            date_extractor_5 = ArabicDateTime.DateExtractor8
            date_extractor_6 = ArabicDateTime.DateExtractor7L
            date_extractor_7 = ArabicDateTime.DateExtractor9S
            date_extractor_8 = ArabicDateTime.DateExtractor4
            date_extractor_9 = ArabicDateTime.DateExtractor6
            date_extractor_10 = ArabicDateTime.DateExtractor9L
            date_extractor_11 = ArabicDateTime.DateExtractor7S
        else:
            date_extractor_4 = ArabicDateTime.DateExtractor4
            date_extractor_5 = ArabicDateTime.DateExtractor6
            date_extractor_6 = ArabicDateTime.DateExtractor7L
            date_extractor_7 = ArabicDateTime.DateExtractor7S
            date_extractor_8 = ArabicDateTime.DateExtractor5
            date_extractor_9 = ArabicDateTime.DateExtractor8
            date_extractor_10 = ArabicDateTime.DateExtractor9L
            date_extractor_11 = ArabicDateTime.DateExtractor9S

        return [
            RegExpUtility.get_safe_reg_exp(ArabicDateTime.DateExtractor1),
            RegExpUtility.get_safe_reg_exp(ArabicDateTime.DateExtractor3),
            RegExpUtility.get_safe_reg_exp(date_extractor_4),
            RegExpUtility.get_safe_reg_exp(date_extractor_5),
            RegExpUtility.get_safe_reg_exp(date_extractor_6),
            RegExpUtility.get_safe_reg_exp(date_extractor_7),
            RegExpUtility.get_safe_reg_exp(date_extractor_8),
            RegExpUtility.get_safe_reg_exp(date_extractor_9),
            RegExpUtility.get_safe_reg_exp(date_extractor_10),
            RegExpUtility.get_safe_reg_exp(date_extractor_11),
            RegExpUtility.get_safe_reg_exp(ArabicDateTime.DateExtractorA),
            RegExpUtility.get_safe_reg_exp(ArabicDateTime.DateExtractorB),
        ]
