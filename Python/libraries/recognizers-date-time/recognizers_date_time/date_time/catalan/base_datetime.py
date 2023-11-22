from typing import List, Optional, Match, Pattern
from datetime import datetime
import regex

from recognizers_text.extractor import ExtractResult
from recognizers_date_time.date_time.constants import TimeTypeConstants
from recognizers_date_time.date_time.parsers import DateTimeParseResult
from recognizers_date_time.date_time.utilities import Token, merge_all_tokens, DateTimeResolutionResult, \
    DateTimeFormatUtil
from recognizers_date_time.date_time.base_datetime import MatchedTimex
from recognizers_date_time.resources.catalan_date_time import CatalanDateTime
from recognizers_text.utilities import RegExpUtility
from recognizers_date_time.date_time.extractors import DateTimeExtractor
from recognizers_date_time.date_time.parsers import DateTimeParser
from recognizers_date_time.date_time.constants import Constants


class MinimalDateTimeExtractor(DateTimeExtractor):
    @property
    def extractor_type_name(self) -> str:
        return Constants.SYS_DATETIME_DATETIME

    def extract(self, source: str, reference: datetime = None) -> List[ExtractResult]:

        tokens: List[Token] = list()
        tokens.extend(self.basic_regex_match(source))

        result = merge_all_tokens(tokens, source, self.extractor_type_name)
        return result

    # match "now"
    def basic_regex_match(self, source: str) -> List[Token]:
        tokens: List[Token] = list()
        # handle "now"
        now_regex = RegExpUtility.get_safe_reg_exp(CatalanDateTime.NowRegex)
        matches: List[Match] = list(
            regex.finditer(now_regex, source))
        tokens.extend(map(lambda x: Token(x.start(), x.end()), matches))
        return tokens


class MinimalDateTimeParser(DateTimeParser):
    @property
    def parser_type_name(self) -> str:
        return Constants.SYS_DATETIME_DATETIME

    def parse(self, source: ExtractResult, reference: datetime = None) -> Optional[DateTimeParseResult]:
        if reference is None:
            reference = datetime.now()

        result = DateTimeParseResult(source)

        if source.type is self.parser_type_name:
            source_text = source.text.lower()
            inner_result = self.parse_basic_regex(source_text, reference)

            if inner_result.success:
                inner_result.future_resolution[TimeTypeConstants.DATETIME] = DateTimeFormatUtil.format_date_time(
                    inner_result.future_value)
                inner_result.past_resolution[TimeTypeConstants.DATETIME] = DateTimeFormatUtil.format_date_time(
                    inner_result.past_value)
                result.value = inner_result
                result.timex_str = inner_result.timex if inner_result else ''
                result.resolution_str = ''

        return result

    def parse_basic_regex(self, source: str, reference: datetime) -> DateTimeResolutionResult:
        result = DateTimeResolutionResult()
        source = source.strip().lower()

        # handle "now"
        now_regex = RegExpUtility.get_safe_reg_exp(CatalanDateTime.NowRegex)
        match = regex.search(now_regex, source)
        if match and match.start() == 0 and match.group() == source:
            matched_now_timex = self.get_matched_now_timex(source, now_regex)
            result.timex = matched_now_timex.timex
            result.future_value = reference
            result.past_value = reference
            result.success = matched_now_timex.matched
        return result

    def get_matched_now_timex(self, source: str, now_time_regex: Pattern) -> MatchedTimex:

        if RegExpUtility.match_end(now_time_regex, source, True):
            return MatchedTimex(True, 'PRESENT_REF')

        return MatchedTimex(False, None)
