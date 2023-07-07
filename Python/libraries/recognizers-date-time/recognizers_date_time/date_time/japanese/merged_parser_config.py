#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.
from typing import Pattern

from recognizers_text import RegExpUtility
from .common_configs import JapaneseCommonDateTimeParserConfiguration
from recognizers_date_time.date_time.CJK.base_merged import CJKMergedParserConfiguration

from ...resources.japanese_date_time import JapaneseDateTime, BaseDateTime

class JapaneseMergedParserConfiguration(JapaneseCommonDateTimeParserConfiguration, CJKMergedParserConfiguration):

    @property
    def before_regex(self) -> Pattern:
        return self._before_regex

    @property
    def after_regex(self) -> Pattern:
        return self._after_regex

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
    def equal_regex(self) -> Pattern:
        return self._equal_regex

    @property
    def until_regex(self) -> Pattern:
        return self._until_regex

    @property
    def year_regex(self) -> Pattern:
        return self._year_regex

    @property
    def around_regex(self) -> Pattern:
        return self._around_regex

    @property
    def suffix_after(self) -> Pattern:
        return self._suffix_after

    @property
    def since_regex(self) -> Pattern:
        return self._since_regex

    def __init__(self, config):

        super().__init__()
        self.config = config
        self._before_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.MergedBeforeRegex)
        self._after_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.MergedAfterRegex)
        self._since_prefix_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.ParserConfigurationSincePrefix)
        self._since_suffix_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.ParserConfigurationSinceSuffix)
        self._around_prefix_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.ParserConfigurationAroundPrefix)
        self._around_suffix_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.ParserConfigurationAroundSuffix)
        self._equal_regex = RegExpUtility.get_safe_reg_exp(BaseDateTime.EqualRegex)
        self._until_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.ParserConfigurationUntil)
        self._year_regex = RegExpUtility.get_safe_reg_exp(JapaneseDateTime.YearRegex)

        # TODO When the implementation for these properties is added, change the None values to their respective Regexps
        self._around_regex = None
        self._suffix_after = None
        self._since_regex = None
