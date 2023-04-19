#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from typing import List
from datetime import datetime
import regex
from ...resources.japanese_date_time import JapaneseDateTime

from recognizers_text import ExtractResult, RegExpUtility, MetaData
from ..utilities import merge_all_tokens, Token, get_tokens_from_regex
from ..base_date import BaseDateExtractor
from .date_extractor_config import JapaneseDateExtractorConfiguration


class JapaneseDateExtractor(BaseDateExtractor):
    before_regex = RegExpUtility.get_safe_reg_exp(
        JapaneseDateTime.BeforeRegex)
    after_regex = RegExpUtility.get_safe_reg_exp(
        JapaneseDateTime.AfterRegex)
    date_time_period_unit_regex = RegExpUtility.get_safe_reg_exp(
        JapaneseDateTime.DateTimePeriodUnitRegex)

    def __init__(self):
        super().__init__(JapaneseDateExtractorConfiguration())

    def extract(self, source: str, reference: datetime = None) -> List[ExtractResult]:
        tokens = self.basic_regex_match(source)
        tokens.extend(self.implicit_date(source))

        result = merge_all_tokens(tokens, source, self.extractor_type_name)
        return result

    def basic_regex_match(self, source: str) -> List[Token]:
        ret: List[Token] = list()

        for regexp in self.config.date_regex_list:
            ret.extend(get_tokens_from_regex(regexp, source))

        return ret

    def implicit_date(self, source: str) -> List[Token]:
        ret: List[Token] = list()

        for regexp in self.config.implicit_date_list:
            ret.extend(get_tokens_from_regex(regexp, source))

        return ret
