#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from abc import abstractmethod
from typing import List, Optional, Pattern, Dict, Match
from datetime import datetime, timedelta
from collections import namedtuple
import regex

from recognizers_text.utilities import RegExpUtility, QueryProcessor
from recognizers_text.extractor import Extractor, ExtractResult, Metadata
from recognizers_date_time.date_time.base_time import BaseTimeExtractor, BaseTimeParser
from .constants import Constants, TimeTypeConstants
from .extractors import DateTimeExtractor
from .parsers import DateTimeParser, DateTimeParseResult
from .utilities import Token, merge_all_tokens, DateTimeResolutionResult, \
    DateTimeUtilityConfiguration, DateTimeFormatUtil, ResolutionStartEnd, DateTimeOptionsConfiguration, DateTimeOptions


class CJKTimePeriodExtractorConfiguration(DateTimeOptionsConfiguration):
    @property
    @abstractmethod
    def regexes(self) -> Dict[regex, PeriodType]:
        raise NotImplementedError

    @property
    @abstractmethod
    def ambiguity_time_period_filters_dict(self) -> Dict[regex, regex]:
        raise NotImplementedError


class BaseCJKTimePeriodExtractor(DateTimeExtractor):
    @property
    def extractor_type_name(self) -> str:
        return Constants.SYS_DATETIME_TIMEPERIOD

    def __init__(self, config: CJKTimePeriodExtractorConfiguration):
        self.config = config

    def extract(self, source: str, reference: datetime = None) -> List[ExtractResult]:
        result: List[ExtractResult] = list()
        if not source:
            return result

        match_source: Dict[Match, any] = dict()
        matched: List[bool] = [False] * len(source)

        collections = list(map(lambda x: (
            list(regex.finditer(x[0], source)), x[1]), self.config.regexes.items()))
        collections = list(filter(lambda x: len(x[0]) > 0, collections))

        for collection in collections:
            for match in collection[0]:
                for j in range(len(match.group())):
                    matched[match.start() + j] = True
                match_source[match] = collection[1]

        last = -1
        for i in range(len(source)):
            if matched[i]:
                if i + 1 == len(source) or not matched[i + 1]:
                    start = last + 1
                    length = i - last
                    text = source[start:start + length].strip()
                    src_match = next((x for x in iter(match_source) if (
                            x.start() == start and (x.end() - x.start()) == length)), None)
                    if src_match:
                        value = ExtractResult()
                        value.start = start
                        value.length = length
                        value.text = text
                        value.type = self.extractor_type_name
                        value.data = self.__get_data(match_source, src_match)
                        result.append(value)
            else:
                last = i

        result = ExtractResultExtension.filter_ambiguity(result, source, self.config.ambiguity_time_filters_dict)

        return result


MatchedTimeRegex = namedtuple(
    'MatchedTimeRegex', ['matched', 'timex', 'begin_hour', 'end_hour', 'end_min'])


class CJKTimePeriodParserConfiguration(DateTimeOptionsConfiguration):
    @property
    @abstractmethod
    def time_extractor(self) -> DateTimeExtractor:
        raise NotImplementedError

    @property
    @abstractmethod
    def time_parser(self) -> DateTimeParser:
        raise NotImplementedError

    @property
    @abstractmethod
    def time_func(self) -> TimeFunctions:
        raise NotImplementedError

    @abstractmethod
    def get_matched_timex_range(self, text: str) -> dict:
        raise NotImplementedError


class BaseCJKTimePeriodParser(DateTimeParser):
    @property
    def parser_type_name(self) -> str:
        return Constants.SYS_DATETIME_TIMEPERIOD

    def __init__(self, config: CJKTimePeriodParserConfiguration):
        self.config = config

    def parse(self, source: ExtractResult, reference: datetime = None) -> Optional[DateTimeParseResult]:
        if reference is None:
            reference = datetime.now()

        result = DateTimeParseResult(source)
        extra: DateTimeExtra = source.data

        if not extra:
            result = self.config.time_extractor.extract(source.text, reference)
            extra = result.data

        if extra:
            parse_result = self.parse_time_of_day(source.text, reference)

            if not parse_result.success:
                parse_result = TimePeriodFunctions.Handle(self.config.time_parser, extra, reference, self.config.time_func)

            if parse_result.success:
                parse_result.future_resolution[TimeTypeConstants.START_TIME] = DateTimeFormatUtil.format_time(
                    parse_result.future_value[0])
                parse_result.future_resolution[TimeTypeConstants.END_TIME] = DateTimeFormatUtil.format_time(
                    parse_result.future_value[1])
                parse_result.past_resolution[TimeTypeConstants.START_TIME] = DateTimeFormatUtil.format_time(
                    parse_result.past_value[0])
                parse_result.past_resolution[TimeTypeConstants.END_TIME] = DateTimeFormatUtil.format_time(
                    parse_result.past_value[1])


                result.value = parse_result
                result.timex_str = parse_result.timex if parse_result is not None else ''
                result.resolution_str = ''

        return result

    def filter_results(self, query: str, candidate_results: List[DateTimeParseResult]):
        return candidate_results

    def parse_time_of_day(self, source: str, reference: datetime) -> DateTimeResolutionResult:
        result = DateTimeResolutionResult()

        day = reference.day
        month = reference.month
        year = reference.year

        parameters = self.config.get_matched_timex_range(source)
        if parameters['matched'] is False:
            return DateTimeResolutionResult()

        end_hour = parameters['end_hour']
        begin_hour = parameters['begin_hour']

        # Add "early"/"late" Mod
        if (end_hour == begin_hour + Constants.HALF_MID_DAY_DURATION_HOUR_COUNT) and \
                (begin_hour == Constants.MORNING_BEGIN_HOUR or begin_hour == Constants.AFTERNOON_BEGIN_HOUR):
            result.Comment = Constants.COMMENT_EARLY
            result.Mod = Constants.EARLY_MOD

        if (begin_hour == end_hour - Constants.HALF_MID_DAY_DURATION_HOUR_COUNT) and \
                (end_hour == Constants.MORNING_BEGIN_HOUR or end_hour == Constants.AFTERNOON_BEGIN_HOUR):
            result.Comment = Constants.COOMENT_LATE
            result.Mod = Constants.LATE_MOD

        result.timex = parameters['timex']
        result.future_value = result.past_value = [
            DateUtils.safe_create_from_min_value(
                year, month, day, parameters['begin_hour'], 0, 0),
            DateUtils.safe_create_from_min_value(
                year, month, day, parameters['end_hour'], parameters['end_min'], 0)
        ]

        result.success = True
        return result
