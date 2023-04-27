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

    def __init__(self):
        super().__init__(JapaneseDateExtractorConfiguration())

    def extract(self, source: str, reference: datetime = None) -> List[ExtractResult]:
        tokens = self.basic_regex_match(source)
        tokens.extend(self.implicit_date(source))
        # tokens.extend(self.duration_with_ago_and_later(source))

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

    def duration_with_ago_and_later(self, source: str, reference: datetime) -> List[Token]:
        ret: List[Token] = list()
        duration_er = self.config.duration_extractor.extract(source, reference)

        for er in duration_er:
            pos = er.start + er.length
            if pos < len(source):
                suffix = source[pos]
                before_match = RegExpUtility.get_matches(self.config.before_regex, suffix)
                after_match = RegExpUtility.get_matches(self.config.after_regex, suffix)

                if (before_match and suffix.startswith(before_match[0])) \
                        or (after_match and suffix.startswith(after_match[0])):
                    meta_data = MetaData()
                    meta_data.is_duration_with_ago_and_later = True
                    ret.append(Token(er.start, pos + 1, meta_data))

        ret.extend(self.extend_with_week_day(ret, source))

        return ret

    def extend_with_week_day(self, ret: List[Token], source: str):

        new_ret: List[Token]

        for er in ret:
            before_str = source[0:er.start]
            after_str = source[:er.start + er.end]
            before_match = self.config.week_day_start_end.match(before_str)
            after_match = self.config.week_day_start_end.match(after_str)

            if before_match or after_match:
                start = before_match.index() if before_match else er.start
                end = er.end if before_match else er.end + after_match.index() + after_match.len()

                meta_data = MetaData()
                meta_data.is_duration_date_with_weekday = True
                ret.append(Token(start, end + 1, meta_data))
                new_ret.append(ret)

        return new_ret
