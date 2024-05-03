from typing import Pattern, List, Optional
from recognizers_number import (BaseNumberExtractor, BaseNumberParser,
                                CatalanOrdinalExtractor, CatalanIntegerExtractor, CatalanNumberParserConfiguration)
from recognizers_text.utilities import RegExpUtility
from ...resources.catalan_date_time import CatalanDateTime
from ..extractors import DateTimeExtractor
from ..base_date import DateExtractorConfiguration, DateTimeUtilityConfiguration
from .base_configs import CatalanDateTimeUtilityConfiguration
from ..constants import Constants


class CatalanDateExtractorConfiguration(DateExtractorConfiguration):

    def __init__(self):
        super().__init__(CatalanDateTime())
        self.ordinal_extractor: BaseNumberExtractor = CatalanOrdinalExtractor()
        self.integer_extractor: BaseNumberExtractor = CatalanIntegerExtractor()
        self.duration_extractor: Optional[DateTimeExtractor] = None
        self.number_parser: BaseNumberParser = BaseNumberParser(CatalanNumberParserConfiguration())
        self.utility_configuration: DateTimeUtilityConfiguration = CatalanDateTimeUtilityConfiguration()
        self.implicit_date_list: List[Pattern] = [
            RegExpUtility.get_safe_reg_exp(CatalanDateTime.OnRegex),
            RegExpUtility.get_safe_reg_exp(CatalanDateTime.RelaxedOnRegex),
            RegExpUtility.get_safe_reg_exp(CatalanDateTime.SpecialDayRegex),
            # TODO - we might invest in resolving below in time.
            # RegExpUtility.get_safe_reg_exp(CatalanDateTime.ThisRegex),
            # RegExpUtility.get_safe_reg_exp(CatalanDateTime.LastDateRegex),
            # RegExpUtility.get_safe_reg_exp(CatalanDateTime.NextDateRegex),
            RegExpUtility.get_safe_reg_exp(CatalanDateTime.WeekDayRegex),
            # RegExpUtility.get_safe_reg_exp(
            # CatalanDateTime.WeekDayOfMonthRegex),
            RegExpUtility.get_safe_reg_exp(CatalanDateTime.SpecialDateRegex),
        ]

    @property
    def date_regex_list(self) -> List[Pattern]:
        if CatalanDateTime.DefaultLanguageFallback == Constants.DEFAULT_LANGUAGE_FALLBACK_DMY:
            date_extractor_4 = CatalanDateTime.DateExtractor5
            date_extractor_5 = CatalanDateTime.DateExtractor8
            date_extractor_6 = CatalanDateTime.DateExtractor9
            date_extractor_8 = CatalanDateTime.DateExtractor4
            date_extractor_7 = CatalanDateTime.DateExtractor6
            date_extractor_9 = CatalanDateTime.DateExtractor7
        else:
            date_extractor_4 = CatalanDateTime.DateExtractor4
            date_extractor_5 = CatalanDateTime.DateExtractor6
            date_extractor_6 = CatalanDateTime.DateExtractor7
            date_extractor_8 = CatalanDateTime.DateExtractor5
            date_extractor_7 = CatalanDateTime.DateExtractor8
            date_extractor_9 = CatalanDateTime.DateExtractor9

        return [
            RegExpUtility.get_safe_reg_exp(CatalanDateTime.DateExtractor1),
            RegExpUtility.get_safe_reg_exp(CatalanDateTime.DateExtractor2),
            RegExpUtility.get_safe_reg_exp(CatalanDateTime.DateExtractor3),
            RegExpUtility.get_safe_reg_exp(date_extractor_4),
            RegExpUtility.get_safe_reg_exp(date_extractor_5),
            RegExpUtility.get_safe_reg_exp(date_extractor_6),
            RegExpUtility.get_safe_reg_exp(date_extractor_7),
            RegExpUtility.get_safe_reg_exp(date_extractor_8),
            RegExpUtility.get_safe_reg_exp(date_extractor_9),
            RegExpUtility.get_safe_reg_exp(CatalanDateTime.DateExtractor10),
        ]
