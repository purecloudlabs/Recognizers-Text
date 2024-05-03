#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.
import copy
from abc import abstractmethod
from typing import List, Pattern, Match, Optional
from collections import namedtuple
import regex

from recognizers_text.extractor import Extractor, ExtractResult
from recognizers_number.resources.base_numbers import BaseNumbers
from recognizers_number.number.models import LongFormatType
from recognizers_number.number.constants import Constants

ReVal = namedtuple('ReVal', ['re', 'val'])
ReRe = namedtuple('ReRe', ['reKey', 'reVal'])
MatchesVal = namedtuple('MatchesVal', ['matches', 'val'])


class BaseNumberExtractor(Extractor):

    extract_type: str

    @property
    @abstractmethod
    def regexes(self) -> List[ReVal]:
        raise NotImplementedError

    @property
    def ambiguity_filters_dict(self) -> List[ReRe]:
        return []

    @property
    def _negative_number_terms(self) -> Optional[Pattern]:
        return None

    def extract(self, source: str) -> List[ExtractResult]:
        if source is None or len(source.strip()) == 0:
            return list()
        result: List[ExtractResult] = list()
        match_source = dict()
        matched: List[bool] = [False] * len(source)

        matches_list = list(map(
            lambda x: MatchesVal(matches=list(regex.finditer(x.re, source)),
                                 val=x.val), self.regexes))
        matches_list = list(filter(lambda x: len(x.matches) > 0, matches_list))
        for ml in matches_list:
            for m in ml.matches:
                for j in range(len(m.group())):
                    matched[m.start() + j] = True
                # Keep Source Data for extra information
                match_source[m] = ml.val

        last = -1
        for i in range(len(source)):
            if not matched[i]:
                last = i
            else:
                if i + 1 == len(source) or not matched[i + 1]:
                    start = last + 1
                    length = i - last
                    substr = source[start:start + length]
                    src_match = next((x for x in iter(match_source) if (
                        x.start() == start and (
                            x.end() - x.start()) == length)), None)

                    # extract negative numbers
                    if self._negative_number_terms is not None:
                        match = regex.search(self._negative_number_terms,
                                             source[0:start])
                        if match is not None:
                            start = match.start()
                            length = length + match.end() - match.start()
                            substr = source[start:start + length]

                    if src_match is not None:
                        value = ExtractResult()
                        value.start = start
                        value.length = length
                        value.text = substr
                        value.type = self.extract_type
                        value.data = match_source.get(src_match, None)
                        result.append(value)

        result = self._filter_ambiguity(result, source)
        return result

    def _filter_ambiguity(self, ers: List[ExtractResult], text: str) -> List[ExtractResult]:
        if self.ambiguity_filters_dict is not None:
            for item in self.ambiguity_filters_dict:
                if regex.search(item.reKey, text):
                    matches = list(regex.finditer(item.reVal, text))
                    if matches and len(matches):
                        ers = list(filter(lambda x: self._filter_item(x, matches), ers))
        return ers

    def _filter_item(self, er: ExtractResult, matches: List[Match]) -> bool:
        for match in matches:
            if match.start() < er.start + er.length and match.end() > er.start:
                return False

        return True

    def _generate_format_regex(self, format_type: LongFormatType,
                               placeholder: str = None) -> str:
        if placeholder is None:
            placeholder = BaseNumbers.PlaceHolderDefault

        if format_type.decimals_mark is None:
            re_definition = BaseNumbers.IntegerRegexDefinition(
                placeholder,
                regex.escape(format_type.thousands_mark)
            )
        else:
            re_definition = BaseNumbers.DoubleRegexDefinition(
                placeholder,
                regex.escape(format_type.thousands_mark),
                regex.escape(format_type.decimals_mark),
            )
        return re_definition


SourcePositionResults = namedtuple('SourcePositionResults',
                                   ['source', 'position', 'results'])


class BaseMergedNumberExtractor(Extractor):

    def __init__(self, number_extractor):
        self._number_extractor = number_extractor

    @property
    @abstractmethod
    def _round_number_integer_regex_with_locks(self) -> Pattern:
        pass

    @property
    @abstractmethod
    def _connector_regex(self) -> Pattern:
        pass

    def extract(self, source: str) -> List[ExtractResult]:
        result = []

        ers = self._number_extractor.extract(source)

        if len(ers) == 0:
            return result

        groups = [0] * len(ers)

        for idx in range(len(ers) - 1):
            if not ers[idx].data.startswith("Integer") or not ers[idx + 1].data.startswith("Integer"):
                groups[idx + 1] = groups[idx] + 1
                continue

            match = regex.search(self._round_number_integer_regex_with_locks, ers[idx].text)

            if not match or match.endpos != ers[idx].length:
                groups[idx + 1] = groups[idx] + 1
                continue

            middle_begin = ers[idx].start + ers[idx].length
            middle_end = ers[idx + 1].start
            middle_str = source[middle_begin:middle_end].strip()

            # Separated by whitespace
            if not middle_str:
                groups[idx + 1] = groups[idx]
                continue

            # Separated by connectors
            match = regex.search(self._connector_regex, middle_str)
            if match and match.pos == 0 and match.endpos == len(middle_str):
                groups[idx + 1] = groups[idx]
            else:
                groups[idx + 1] = groups[idx] + 1

        for idx in range(len(ers)):

            if idx == 0 or groups[idx] != groups[idx - 1]:

                tmp_extract_result = copy.deepcopy(ers[idx])

                value = ExtractResult()
                value.start = tmp_extract_result.start
                value.length = tmp_extract_result.length
                value.text = tmp_extract_result.text
                value.type = tmp_extract_result.type
                value.data = tmp_extract_result.data
                tmp_extract_result.data = [value]

                result.append(tmp_extract_result)

            # Reduce extract results in same group
            if idx + 1 < len(ers) and groups[idx + 1] == groups[idx]:

                group = groups[idx]

                period_begin = result[group].start
                period_end = ers[idx + 1].start + ers[idx + 1].length

                result[group].length = period_end - period_begin
                result[group].text = source[period_begin:period_end]
                result[group].type = Constants.SYS_NUM
                if isinstance(result[group].data, list):
                    result[group].data.append(ers[idx + 1])
                else:
                    result[group].data = [ers[idx + 1]]

        for idx in range(len(result)):
            inner_data = result[idx].data
            if inner_data and len(inner_data) == 1:
                result[idx] = inner_data[0]

        return result
