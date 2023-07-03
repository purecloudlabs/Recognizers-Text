#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from typing import Pattern, List, Dict

from recognizers_text import RegExpUtility
from ..CJK import CJKMergedExtractorConfiguration
from ..CJK.base_dateperiod import BaseCJKDatePeriodExtractor
from ..CJK.base_date import BaseCJKDateExtractor
from ..japanese import JapaneseDateExtractorConfiguration, JapaneseDatePeriodExtractorConfiguration
from ...resources.japanese_date_time import JapaneseDateTime, BaseDateTime
from ..extractors import DateTimeExtractor


class JapaneseMergedExtractorConfiguration(CJKMergedExtractorConfiguration):

    @property
    def date_extractor(self) -> DateTimeExtractor:
        return self._date_extractor

    @property
    def date_period_extractor(self) -> DateTimeExtractor:
        return self._date_period_extractor

    @property
    def after_regex(self) -> Pattern:
        return self._after_regex

    @property
    def before_regex(self) -> Pattern:
        return self._before_regex

    @property
    def unspecified_date_period_regex(self) -> Pattern:
        return self._unspecified_date_period_regex

    @property
    def since_prefix_regex(self) -> Pattern:
        return self._since_prefix_regex

    @property
    def since_suffix_regex(self) -> Pattern:
        return self._since_suffix_regex
    @property
    def around_prefix_regex(self) -> Pattern:
        return self._around_prefix_regex

    @property
    def around_suffix_regex(self) -> Pattern:
        return self._around_suffix_regex

    @property
    def until_regex(self) -> Pattern:
        return self._until_regex

    @property
    def equal_regex(self) -> Pattern:
        return self._equal_regex

    @property
    def ambiguous_range_modifier_prefix(self) -> Pattern:
        return self._ambiguous_range_modifier_prefix

    @property
    def day_of_month(self) -> Dict[str, int]:
        return self._day_of_month

    @property
    def ambiguity_filters_dict(self) -> {}:
        return self._ambiguity_filters_dict

    @property
    def superfluous_word_matcher(self) -> Pattern:
        return self._superfluous_word_matcher

    @property
    def fail_fast_regex(self) -> Pattern:
        return self._fail_fast_regex

    @property
    def suffix_after_regex(self) -> Pattern:
        return self._suffix_after_regex

    @property
    def potential_ambiguous_range_regex(self) -> Pattern:
        return self._potential_ambiguous_range_regex

    @property
    def around_regex(self) -> Pattern:
        return self._around_regex

    @property
    def term_filter_regexes(self) -> List[Pattern]:
        return self._term_filter_regexes

    @property
    def datetime_alt_extractor(self) -> any:
        return self._datetime_alt_extractor

    @property
    def time_zone_extractor(self) -> any:
        return self._time_zone_extractor

    @property
    def time_extractor(self):
        return self._time_zone_extractor

    @property
    def duration_extractor(self):
        return self._duration_extractor

    @property
    def date_time_extractor(self):
        return self._date_time_extractor

    @property
    def time_period_extractor(self):
        return self._time_period_extractor

    @property
    def date_time_period_extractor(self):
        return self._date_time_period_extractor

    @property
    def set_extractor(self):
        return self._set_extractor

    @property
    def holiday_extractor(self):
        return self._holiday_extractor

    def __init__(self):

        super().__init__()
        self._date_extractor = BaseCJKDateExtractor(JapaneseDateExtractorConfiguration())
        self._date_period_extractor = BaseCJKDatePeriodExtractor(JapaneseDatePeriodExtractorConfiguration())

        self._after_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.AfterRegex)
        self._before_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.BeforeRegex)
        self._unspecified_date_period_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.UnspecificDatePeriodRegex)
        self._since_prefix_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.ParserConfigurationSincePrefix)
        self._since_suffix_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.ParserConfigurationSinceSuffix)
        self._around_prefix_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.ParserConfigurationAroundPrefix)
        self._around_suffix_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.ParserConfigurationAroundSuffix)
        self._until_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.ParserConfigurationUntil)
        self._equal_regex = RegExpUtility.get_safe_reg_exp(BaseDateTime.EqualRegex)
        self._ambiguous_range_modifier_prefix = RegExpUtility.get_safe_reg_exp(
            JapaneseDateTime.AmbiguousRangeModifierPrefix)

        self._ambiguity_filters_dict = JapaneseDateTime.AmbiguityFiltersDict
        self._day_of_month = JapaneseDateTime.ParserConfigurationDayOfMonth

        # TODO When the implementation for these properties is added, change the None values to their respective Regexps
        self._superfluous_word_matcher = None
        self._fail_fast_regex = None
        self._suffix_after_regex = None
        self._potential_ambiguous_range_regex = None
        self._around_regex = None
        self._term_filter_regexes = None
        self._datetime_alt_extractor = None
        self._time_zone_extractor = None

        self._time_extractor = None
        self._duration_extractor = None
        self._date_time_extractor = None
        self._time_period_extractor = None
        self._date_time_period_extractor = None
        self._set_extractor = None
        self._holiday_extractor = None
