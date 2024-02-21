from typing import List, Pattern

from recognizers_text import RegExpUtility, Extractor
from recognizers_number import MinimalIntegerExtractor
from recognizers_date_time.resources.minimal_date_time import MinimalDateTime
from recognizers_date_time.date_time.extractors import DateTimeExtractor
from recognizers_date_time.date_time.base_minimal_merged import MinimalMergedExtractorConfiguration
from recognizers_date_time.date_time.minimal.base_minimal_date import BaseMinimalDateExtractor
from recognizers_date_time.date_time.minimal.base_minimal_time import BaseMinimalTimeExtractor
from recognizers_date_time.date_time.minimal.date_extractor_config import MinimalDateExtractorConfiguration
from recognizers_date_time.date_time.minimal.time_extractor_config import MinimalTimeExtractorConfiguration
from recognizers_date_time.resources.base_date_time import BaseDateTime


class BaseMinimalMergedExtractorConfiguration(MinimalMergedExtractorConfiguration):
    @property
    def check_both_before_after(self):
        return self._check_both_before_after

    @property
    def date_extractor(self) -> DateTimeExtractor:
        return self._date_extractor

    @property
    def time_extractor(self) -> DateTimeExtractor:
        return self._time_extractor

    @property
    def date_time_extractor(self) -> DateTimeExtractor:
        return None

    @property
    def integer_extractor(self) -> Extractor:
        return self._integer_extractor

    @property
    def equal_regex(self) -> Pattern:
        return self._equal_regex

    @property
    def ambiguous_range_modifier_prefix(self) -> None:
        return None

    @property
    def potential_ambiguous_range_regex(self) -> None:
        return None

    @property
    def number_ending_pattern(self) -> Pattern:
        return RegExpUtility.get_safe_reg_exp(f'^[.]')

    @property
    def filter_word_regex_list(self) -> List[Pattern]:
        return self._filter_word_regex_list

    def __init__(self):
        self._date_extractor = BaseMinimalDateExtractor(
            MinimalDateExtractorConfiguration())
        self._time_extractor = BaseMinimalTimeExtractor(MinimalTimeExtractorConfiguration())
        self._integer_extractor = MinimalIntegerExtractor()
        self._filter_word_regex_list = []
        self._equal_regex = BaseDateTime.EqualRegex
        self._check_both_before_after = MinimalDateTime.CheckBothBeforeAfter
