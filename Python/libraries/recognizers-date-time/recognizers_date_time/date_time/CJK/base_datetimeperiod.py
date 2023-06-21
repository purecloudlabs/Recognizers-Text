from abc import abstractmethod
from datetime import datetime, timedelta
from collections import namedtuple
from typing import List, Optional, Pattern, Dict, Match

import regex

from recognizers_text.extractor import Extractor, ExtractResult
from recognizers_text.parser import Parser, ParseResult
from recognizers_date_time.date_time.constants import Constants
from recognizers_date_time.date_time import DateTimeExtractor, DateTimeParser
from recognizers_date_time.date_time.utilities import DateTimeOptionsConfiguration, Token, ExtractResultExtension, \
    RegExpUtility, DateTimeParseResult, DateTimeResolutionResult, TimexUtil, DateUtils

MatchedIndex = namedtuple('MatchedIndex', ['matched', 'index'])
MatchedTimeRegex = namedtuple(
    'MatchedTimeRegex', ['matched', 'timex', 'begin_hour', 'end_hour', 'end_min'])
MatchedTimeRegexAndSwift = namedtuple(
    'MatchedTimeRegex', ['matched', 'timex', 'begin_hour', 'end_hour', 'end_min', 'swift'])
BeginEnd = namedtuple('BeginEnd', ['begin', 'end'])


class CJKDateTimePeriodExtractorConfiguration(DateTimeOptionsConfiguration):
    @property
    @abstractmethod
    def preposition_regex(self) -> Pattern:
        raise NotImplementedError

    @property
    @abstractmethod
    def till_regex(self) -> Pattern:
        raise NotImplementedError

    @property
    @abstractmethod
    def specific_time_of_day_regex(self) -> Pattern:
        raise NotImplementedError

    @property
    @abstractmethod
    def time_of_day_regex(self) -> Pattern:
        raise NotImplementedError

    @property
    @abstractmethod
    def followed_unit(self) -> Pattern:
        raise NotImplementedError

    @property
    @abstractmethod
    def unit_regex(self) -> Pattern:
        raise NotImplementedError

    @property
    @abstractmethod
    def past_regex(self) -> Pattern:
        raise NotImplementedError

    @property
    @abstractmethod
    def future_regex(self) -> Pattern:
        raise NotImplementedError

    @property
    @abstractmethod
    def time_period_left_regex(self) -> Pattern:
        raise NotImplementedError

    @property
    @abstractmethod
    def relative_regex(self) -> Pattern:
        raise NotImplementedError

    @property
    @abstractmethod
    def rest_of_date_regex(self) -> Pattern:
        raise NotImplementedError

    @property
    @abstractmethod
    def am_pm_desc_regex(self) -> Pattern:
        raise NotImplementedError

    @property
    @abstractmethod
    def this_regex(self) -> Pattern:
        raise NotImplementedError

    @property
    @abstractmethod
    def before_after_regex(self) -> Pattern:
        raise NotImplementedError

    @property
    @abstractmethod
    def cardinal_extractor(self) -> Extractor:
        raise NotImplementedError

    @property
    @abstractmethod
    def single_date_extractor(self) -> DateTimeExtractor:
        raise NotImplementedError

    @property
    @abstractmethod
    def single_time_extractor(self) -> DateTimeExtractor:
        raise NotImplementedError

    @property
    @abstractmethod
    def single_date_time_extractor(self) -> DateTimeExtractor:
        raise NotImplementedError

    @property
    @abstractmethod
    def duration_extractor(self) -> DateTimeExtractor:
        raise NotImplementedError

    @property
    @abstractmethod
    def time_period_extractor(self) -> DateTimeExtractor:
        raise NotImplementedError

    @abstractmethod
    def get_from_token_index(self, text: str) -> MatchedIndex:
        raise NotImplementedError

    @abstractmethod
    def has_connector_token(self, text: str) -> bool:
        raise NotImplementedError

    @abstractmethod
    def get_between_token_index(self, text: str) -> MatchedIndex:
        raise NotImplementedError


class BaseCJKDateTimePeriodExtractor(DateTimeExtractor):
    @property
    def extractor_type_name(self) -> str:
        return Constants.SYS_DATETIME_DATETIME

    def __init__(self, config: CJKDateTimePeriodExtractorConfiguration):
        self.config = config

    def extract(self, source: str, reference_time: datetime = None) -> List[ExtractResult]:
        if reference_time is None:
            reference_time = datetime.now()
        # Date and time Extractions should be extracted from the text only once,
        # and shared in the methods below, passed by value

    def merge_date_and_time_period(self, text: str, data_ers: List[ExtractResult], time_range_ers: List[ExtractResult]) \
            -> List[Token]:
        ret: List[Token] = list()
        time_points: List[ExtractResult] = list()

        # handle the overlap problem
        j = 0
        for data_er in data_ers:
            time_points.append(data_er)
            while j < len(time_range_ers) and time_range_ers[j].start + time_range_ers[j].length <= data_er.start:
                time_points.append(time_range_ers[j])
                j += 1

            while j < len(time_range_ers) and ExtractResultExtension.is_overlap(time_range_ers[j], data_er):
                j += 1

        while j < len(time_range_ers):
            time_points.append(time_range_ers[j])
            j += 1

        time_points = sorted(time_points, key=lambda x: x.start)

        # merge {Date} {TimePeriod}
        idx = 0
        while idx < len(time_points) - 1:
            if time_points[idx].type == Constants.SYS_DATETIME_DATE and \
                    time_points[idx + 1].type == Constants.SYS_DATETIME_TIMEPERIOD:
                middle_begin = time_points[idx].start + time_points[idx].length
                middle_end = time_points[idx + 1].start

                middle_str = text[middle_begin: middle_end - middle_begin].strip().lower()
                if middle_str and RegExpUtility.is_exact_match(self.config.preposition_regex, middle_str, True):
                    period_begin = time_points[idx].start
                    period_end = time_points[idx + 1].start + time_points[idx + 1].length
                    ret.append(Token(period_begin, period_end))
                    idx += 2
                    continue
                idx += 1
            idx += 1
        return ret

    def merge_two_time_points(self, text: str, date_time_ers: List[ExtractResult], time_ers: List[ExtractResult]) \
            -> List[Token]:
        ret: List[Token] = list()
        time_points: List[ExtractResult] = list()

        # handle the overlap problem
        j = 0
        for date_time_er in date_time_ers:
            time_points.append(date_time_er)
            while j < len(time_ers) and time_ers[j].start + time_ers[j].length <= date_time_er.start:
                time_points.append(time_ers[j])
                j += 1
            while j < len(time_ers) and ExtractResultExtension.is_overlap(time_ers[j], date_time_er):
                j += 1

        while j < len(time_ers):
            time_points.append(time_ers[j])

        time_points = sorted(time_points, key=lambda x: x.start)

        # merge "{TimePoint} to {TimePoint}", "between {TimePoint} and {TimePoint}"
        idx = 0
        while idx < len(time_points) - 1:
            # if both ends are Time. then this is a TimePeriod, not a DateTimePeriod
            if time_points[idx].type == Constants.SYS_DATETIME_TIME \
                    and time_points[idx + 1].type == Constants.SYS_DATETIME_TIME:
                idx += 1
                continue

            middle_begin = time_points[idx].start + time_points[idx].length
            middle_end = time_points[idx + 1].start

            middle_str = text[middle_begin: middle_end - middle_begin].strip().lower()

            # handle "{TimePoint} to {TimePoint}"
            if RegExpUtility.is_exact_match(self.config.till_regex, middle_str, True):
                period_begin = time_points[idx].start
                period_end = time_points[idx + 1].start + time_points[idx + 1].length

                # handle "from"
                before_str = time_points[idx].start
                match_from = self.config.get_from_token_index(before_str)
                from_token_index = match_from if match_from.matched else self.config.get_between_token_index(before_str)

                if from_token_index.matched:
                    period_begin = from_token_index.index
                else:
                    after_str = text[period_end:len(text) - period_end]
                    after_token_index = self.config.get_from_token_index(after_str)
                    if after_token_index.matched:
                        period_end += after_token_index.index

                ret.append(Token(period_begin, period_end))
                idx += 2
                continue

            # handle "between {TimePoint} and {TimePoint}"
            if self.config.has_connector_token(middle_str):
                period_begin = time_points[idx].start
                period_end = time_points[idx + 1].start + time_points[idx + 1].length

                # handle "between"
                after_str = text[period_end:len(text) - period_end]
                after_token_between_index = self.config.get_between_token_index(after_str)
                if after_token_between_index.matched:
                    ret.append(Token(period_begin, period_end + idx))
                    idx += 2
                    continue

            idx += 1

        return ret

    def match_night(self, text: str, reference_time: datetime) -> List[Token]:
        ret: List[Token] = list()
        text = text.strip().lower()

        matches = regex.finditer(self.config.specific_time_of_day_regex, text)
        ret.extend(map(lambda x: Token(x.start(), x.end()), matches))

        # Date followed by morning, afternoon
        ers = self.config.single_date_extractor.extract(text, reference_time)
        if len(ers) == 0:
            return ret

        for er in ers:
            after_str = text[er.start + er.length]
            match = regex.search(self.config.time_of_day_regex, after_str)
            if match:
                middle_str = after_str[0:match.start()]
                if not middle_str.strip() or regex.search(self.config.preposition_regex, middle_str):
                    ret.append(Token(er.start, er.start + er.length + match.end()))
        return ret

    # Cases like "2015年1月1日の2時以降", "On January 1, 2015 after 2:00"
    def merge_date_with_time_period_suffix(self, text: str, date_ers: List[ExtractResult],
                                           time_ers: List[ExtractResult]) -> List[Token]:
        ret: List[Token] = list()

        if not date_ers:
            return ret
        if not time_ers:
            return ret

        ers = date_ers
        ers.extend(time_ers)

        ers = sorted(ers, key=lambda x: x.start)

        i = 0
        while i < len(ers) - 1:
            j = i + 1
            while j < len(ers) and ExtractResultExtension.is_overlap(ers[i], ers[j]):
                j += 1
            if j >= len(ers):
                break

            if ers[i].type == Constants.SYS_DATETIME_DATE and ers[j].type == Constants.SYS_DATETIME_TIME:
                middle_begin = ers[i].start + ers[i].length
                middle_end = ers[j].start

                if middle_begin > middle_end:
                    i = j + 1
                    continue

                middle_str = text[middle_begin: middle_end - middle_begin].strip()

                match = regex.match(self.config.before_after_regex, middle_str)
                if match:
                    begin = ers[i].start
                    end = ers[j].start + ers[j].length
                    ret.append(Token(begin, end))

                i = j + 1
                continue
            i = j
        return ret

    # Extract patterns that involve durations e.g. "Within 5 hours from now"
    def match_duration(self, text: str, reference: datetime) -> List[Token]:
        ret: List[Token] = list()
        text = text.strip().lower()
        duration_extractions: List[ExtractResult] = self.config.duration_extractor.extract(text, reference)

        for duration_extraction in duration_extractions:
            if not regex.search(self.config.unit_regex, duration_extraction.text):
                continue
            duration = Token(duration_extraction.start, duration_extraction.start + duration_extraction.length)
            before_str = text[0:duration.start]
            after_str = text[duration.start + duration.length:].strip()

            if not before_str and not after_str:
                continue

            start_out = -1
            end_out = -1
            match = regex.match(self.config.future_regex, after_str)

            in_prefix_match = regex.match(self.config.this_regex, before_str)
            in_prefix = True if in_prefix_match else False

            if match.groups(Constants.WITHIN_GROUP_NAME):
                start_token = in_prefix_match.start() if in_prefix else duration.start
                within_length = len(RegExpUtility.get_group(match, Constants.WITHIN_GROUP_NAME))
                end_token = duration.end + (match.start() + match.end() if in_prefix else 0)

                match = regex.match(self.config.unit_regex, text[duration.start:duration.length])

                if match:
                    start_out = start_token
                    end_out = end_token + within_length if in_prefix else end_token

                ret.append(Token(start_out, end_out))

        return ret

    def match_relative_unit(self, text: str) -> List[Token]:
        ret: List[Token] = list()
        matches = list(regex.finditer(self.config.rest_of_date_regex, text))
        ret.extend(map(lambda x: Token(x.start(), x.end()), matches))
        return ret

    def match_date_with_period_suffix(self, text: str, date_ers: List[ExtractResult]) -> List[Token]:
        ret: List[Token] = list()

        for date_er in date_ers:
            date_str_end = date_er.start + date_er.length
            after_str = text[date_str_end: len(text) - date_str_end]
            match_after = RegExpUtility.match_begin(self.config.time_period_left_regex, after_str, True)
            if match_after.success:
                ret.append(Token(date_er.start, date_str_end + match_after.index + match_after.length))

        return ret

    def match_number_with_unit(self, text: str) -> List[Token]:
        ret: List[Token] = list()
        durations: List[Token] = list()

        ers = self.config.cardinal_extractor.extract(text)

        for er in ers:
            after_str = text[er.start + er.length:]
            followed_unit_match = RegExpUtility.match_begin(self.config.followed_unit, after_str, True)

            if followed_unit_match.success:
                durations.append(Token(er.start, er.start + er.length + len(followed_unit_match.group())))

            past_regex_match = RegExpUtility.match_begin(self.config.past_regex, after_str, True)
            if past_regex_match.success:
                durations.append(Token(er.start, er.start + er.length + len(past_regex_match.group())))

        for match in RegExpUtility.get_matches(self.config.unit_regex, text):
            durations.append(Token(match.start(), match.end()))

        for duration in durations:
            before_str = text[0:duration.start]
            if not before_str.strip():
                continue

            past_regex_match = RegExpUtility.match_end(self.config.past_regex, before_str, True)
            if past_regex_match.success:
                ret.append(Token(match.start(), duration.end))
                continue

            future_regex_match = RegExpUtility.match_end(self.config.future_regex, before_str, True)
            if future_regex_match.success:
                ret.append(Token(match.start(), duration.end))

            time_period_left_regex_match = RegExpUtility.match_end(self.config.time_period_left_regex, before_str, True)
            if time_period_left_regex_match.success:
                ret.append(Token(match.start(), duration.end))

        return ret


class CJKDateTimePeriodParserConfiguration(DateTimeOptionsConfiguration):
    @property
    @abstractmethod
    def date_extractor(self) -> DateTimeExtractor:
        raise NotImplementedError

    @property
    @abstractmethod
    def time_extractor(self) -> DateTimeExtractor:
        raise NotImplementedError

    @property
    @abstractmethod
    def date_time_extractor(self) -> DateTimeExtractor:
        raise NotImplementedError

    @property
    @abstractmethod
    def time_period_extractor(self) -> DateTimeExtractor:
        raise NotImplementedError

    @property
    @abstractmethod
    def duration_extractor(self) -> DateTimeExtractor:
        raise NotImplementedError

    @property
    @abstractmethod
    def duration_parser(self) -> DateTimeExtractor:
        raise NotImplementedError

    @property
    @abstractmethod
    def cardinal_extractor(self) -> Extractor:
        raise NotImplementedError

    @property
    @abstractmethod
    def cardinal_parser(self) -> Parser:
        raise NotImplementedError

    @property
    @abstractmethod
    def date_parser(self) -> DateTimeParser:
        raise NotImplementedError

    @property
    @abstractmethod
    def time_parser(self) -> DateTimeParser:
        raise NotImplementedError

    @property
    @abstractmethod
    def date_time_parser(self) -> DateTimeParser:
        raise NotImplementedError

    @property
    @abstractmethod
    def time_period_parser(self) -> DateTimeParser:
        raise NotImplementedError

    @property
    @abstractmethod
    def specific_time_of_day_regex(self) -> Pattern:
        raise NotImplementedError

    @property
    @abstractmethod
    def time_of_day_regex(self) -> Pattern:
        raise NotImplementedError

    @property
    @abstractmethod
    def next_regex(self) -> Pattern:
        raise NotImplementedError

    @property
    @abstractmethod
    def last_regex(self) -> Pattern:
        raise NotImplementedError

    @property
    @abstractmethod
    def past_regex(self) -> Pattern:
        raise NotImplementedError

    @property
    @abstractmethod
    def future_regex(self) -> Pattern:
        raise NotImplementedError

    @property
    @abstractmethod
    def weekday_regex(self) -> Pattern:
        raise NotImplementedError

    @property
    @abstractmethod
    def time_period_left_regex(self) -> Pattern:
        raise NotImplementedError

    @property
    @abstractmethod
    def unit_regex(self) -> Pattern:
        raise NotImplementedError

    @property
    @abstractmethod
    def rest_of_date_regex(self) -> Pattern:
        raise NotImplementedError

    @property
    @abstractmethod
    def am_pm_desc_regex(self) -> Pattern:
        raise NotImplementedError

    @property
    @abstractmethod
    def unit_map(self) -> Dict[str, str]:
        raise NotImplementedError

    @abstractmethod
    def get_matched_time_range(self, text: str) -> MatchedTimeRegex:
        raise NotImplementedError

    @abstractmethod
    def get_matched_time_range_and_swift(self, text: str) -> MatchedTimeRegexAndSwift:
        raise NotImplementedError


class BaseCJKDateTimePeriodParser(DateTimeParser):
    @property
    def parser_type_name(self) -> str:
        return Constants.SYS_DATETIME_DATETIME

    def __init__(self, config: CJKDateTimePeriodParserConfiguration):
        self.config = config

    def parse(self, source: ExtractResult, reference: datetime = None) -> Optional[DateTimeParseResult]:
        reference_date = reference if reference is not None else datetime.now()

        value = None

    def filter_result(self, query: str, candidare_results: List[DateTimeParseResult]) -> List[DateTimeParseResult]:
        return candidare_results

    def merge_date_and_time_period(self, text: str, reference_time: datetime) -> DateTimeResolutionResult:
        ret = DateTimeResolutionResult()

        er1 = self.config.date_extractor.extract(text, reference_time)
        er2 = self.config.time_period_extractor.extract(text, reference_time)

        if len(er1) != 1 or len(er2) != 1:
            return ret

        pr1 = self.config.date_parser.parse(er1[0], reference_time)
        pr2 = self.config.time_period_parser.parse(er2[0], reference_time)
        time_range = tuple(pr2.value.future_value)
        begin_time = time_range[0]
        end_time = time_range[1]
        future_date = pr1.value.future_value
        past_date = pr1.value.past_value

        # handle cases with time like 25時 which resolve to the next day
        swift_day = 0
        timex_hours = TimexUtil.parse_hours_from_time_period_timex(pr2.timex_str)
        ampm_desc_regex_match = regex.match(self.config.am_pm_desc_regex, text)

        if ampm_desc_regex_match and timex_hours[0] < Constants.HALF_DAY_HOUR_COUNT and timex_hours[
            1] < Constants.HALF_DAY_HOUR_COUNT:
            ret.comment = Constants.COMMENT_AMPM

        if timex_hours[0] > Constants.DAY_HOUR_COUNT:
            past_date = past_date + timedelta(days=1)
            future_date = future_date + timedelta(days=1)
        elif timex_hours[1] > Constants.DAY_HOUR_COUNT:
            swift_day += 1

        past_date_alt = past_date + timedelta(days=swift_day)
        future_date_alt = future_date + timedelta(days=swift_day)

        ret.future_value = (
            DateUtils.safe_create_from_min_value(
                future_date.year, future_date.month, future_date.day,
                begin_time.hour, begin_time.minute, begin_time.second),
            DateUtils.safe_create_from_min_value(
                future_date_alt.year, future_date_alt.month, future_date_alt.day,
                end_time.hour, end_time.minute, end_time.second)
        )

        ret.past_value = (
            DateUtils.safe_create_from_min_value(
                past_date.year, past_date.month, past_date.day,
                begin_time.hour, begin_time.minute, begin_time.second),
            DateUtils.safe_create_from_min_value(
                past_date_alt.year, past_date_alt.month, past_date_alt.day,
                end_time.hour, end_time.minute, end_time.second)
        )

        ret.timex = TimexUtil.generate_split_date_time_period_timex(pr1.timex_str, pr2.timex_str)
        ret.success = True if ret.timex else False

        return ret

    def parse_date_with_time_period_suffix(self, text: str, reference_time: datetime):
        ret = DateTimeResolutionResult()

        return ret
