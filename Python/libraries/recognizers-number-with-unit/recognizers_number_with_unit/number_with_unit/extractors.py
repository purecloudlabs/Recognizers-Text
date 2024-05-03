#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from collections import namedtuple
from copy import deepcopy
from typing import Dict, List, Match, Pattern, Set

import regex

from recognizers_number.culture import CultureInfo
from recognizers_text.extractor import Extractor, ExtractResult
from recognizers_text.matcher.match_result import MatchResult
from recognizers_text.matcher.match_strategy import MatchStrategy
from recognizers_text.matcher.number_with_unit_tokenizer import NumberWithUnitTokenizer
from recognizers_text.matcher.string_matcher import StringMatcher
from recognizers_text.utilities import RegExpUtility

from .constants import *
from .utilities import Token


PrefixUnitResult = namedtuple('PrefixUnitResult', ['offset', 'unit'])


class NumberWithUnitExtractorConfiguration:

    ambiguity_filters_dict: Dict[Pattern, Pattern]
    ambiguous_unit_list: List[str]
    ambiguous_unit_number_multiplier_regex: Pattern
    extract_type: str
    suffix_list: Dict[str, str]
    prefix_list: Dict[str, str]
    unit_num_extractor: Extractor
    build_prefix: str
    build_suffix: str
    connector_token: str
    compound_unit_connector_regex: Pattern
    non_unit_regex: Pattern
    culture_info: CultureInfo

    def expand_half_suffix(self, source, result, numbers):
        pass

    def __init__(self, culture_info: CultureInfo):
        self.culture_info = culture_info


class NumberWithUnitExtractor(Extractor):

    @property
    def separator(self):
        return ['|']

    @property
    def max_prefix_match_len(self):
        return self.__max_prefix_match_len

    @max_prefix_match_len.setter
    def max_prefix_match_len(self, value):
        self.__max_prefix_match_len = value

    @property
    def prefix_matcher(self):
        return self.__prefix_matcher

    @prefix_matcher.setter
    def prefix_matcher(self, value):
        self.__prefix_matcher = value

    @property
    def suffix_matcher(self):
        return self.__suffix_matcher

    @suffix_matcher.setter
    def suffix_matcher(self, value):
        self.__suffix_matcher = value

    @property
    def separate_regex(self):
        return self.__separate_regex

    @separate_regex.setter
    def separate_regex(self, value):
        self.__separate_regex = value

    @property
    def single_char_unit_regex(self):
        return RegExpUtility.get_safe_reg_exp(BaseUnits.SingleCharUnitRegex)

    def __init__(self, config: NumberWithUnitExtractorConfiguration):

        self.config = config
        self.max_prefix_match_len = 0

        if self.config.suffix_list:
            self.__suffix_matcher = self._build_matcher_from_set(list(self.config.suffix_list.values()))
        else:
            self.__suffix_matcher = StringMatcher()

        if self.config.prefix_list:
            for pre_match in self.config.prefix_list.values():
                match_list = str(pre_match).split(self.separator[0])
                for match in match_list:
                    if self.max_prefix_match_len >= len(match):
                        self.max_prefix_match_len = self.max_prefix_match_len
                    else:
                        self.max_prefix_match_len = len(match)

            # 2 is the maximum length of spaces.
            self.max_prefix_match_len += 2
            self.__prefix_matcher = self._build_matcher_from_set(self.config.prefix_list.values())
        else:
            self.__prefix_matcher = StringMatcher()

        self.separate_regex = self._build_separate_regex_from_config()

    def extract(self, source: str) -> List[ExtractResult]:
        if not self._pre_check_str(source):
            return []

        non_unit_match = None
        numbers = None
        unit_is_prefix = []

        mapping_prefix: Dict[float, PrefixUnitResult] = dict()
        matched = [False] * len(source)
        result = []
        prefix_matched = False
        prefix_match: List[MatchResult] = sorted(self.prefix_matcher.find(source), key=lambda o: o.start)
        suffix_match: List[MatchResult] = sorted(self.suffix_matcher.find(source), key=lambda o: o.start)

        if len(prefix_match) > 0 or len(suffix_match) > 0:

            numbers: List[ExtractResult] = sorted(self.config.unit_num_extractor.extract(source), key=lambda o: o.start)

            if (
                len(numbers) > 0
                and self.config.extract_type is Constants.SYS_UNIT_CURRENCY
                and len(prefix_match) > 0
                and len(suffix_match) > 0
            ):

                for number in numbers:
                    start = number.start
                    length = number.length
                    number_prefix = [(mr.start + mr.length) == start for mr in prefix_match]
                    number_suffix = [mr.start == (start + length) for mr in suffix_match]
                    if True in number_prefix and True in number_suffix and "," in number.text:
                        comma_index = number.start + number.text.index(",")
                        source = source[:comma_index] + " " + source[comma_index + 1 :]

                numbers: List[ExtractResult] = sorted(
                    self.config.unit_num_extractor.extract(source), key=lambda o: o.start
                )

            # Special case for cases where number multipliers clash with unit
            ambiguous_multiplier_regex = self.config.ambiguous_unit_number_multiplier_regex
            if ambiguous_multiplier_regex is not None:

                for num in numbers:
                    match = list(filter(lambda x: x.group(), regex.finditer(ambiguous_multiplier_regex, num.text)))
                    if match and len(match) == 1:
                        new_length = num.length - (match[0].span()[1] - match[0].span()[0])
                        num.text = num.text[0:new_length]
                        num.length = new_length

            for number in numbers:
                if number.start is None or number.length is None:
                    continue
                start = int(number.start)
                length = int(number.length)
                max_find_pref = min(self.max_prefix_match_len, number.start)
                max_find_suff = len(source) - start - length

                if max_find_pref != 0:
                    last_index = start
                    best_match = None

                    for m in prefix_match:
                        if m.length > 0 and m.end > start:
                            break

                        if m.length > 0 and source[m.start : m.start + (last_index - m.start)].strip() == m.text:
                            best_match = m
                            break

                    if best_match is not None:
                        off_set = last_index - best_match.start
                        unit_str = source[best_match.start : best_match.start + off_set]
                        self.add_element(mapping_prefix, number.start, (PrefixUnitResult(off_set, unit_str)))
                prefix_unit = mapping_prefix.get(start, None)
                if max_find_suff > 0:

                    max_len = 0
                    first_index = start + length

                    for m in suffix_match:

                        if m.length > 0 and m.start >= first_index:

                            end_pos = m.start + m.length - first_index
                            if max_len < end_pos:
                                mid_str = source[first_index : first_index + (m.start - first_index)]
                                if (
                                    mid_str is None
                                    or not mid_str
                                    or str.isspace(mid_str)
                                    or mid_str.strip() == self.config.connector_token
                                ):
                                    max_len = end_pos
                                if m.end < len(source) and (
                                    (mid_str.endswith('(') and source[m.end] == ')')
                                    or (mid_str.endswith('[') and source[m.end] == ']')
                                    or (mid_str.endswith('{') and source[m.end] == '}')
                                    or (mid_str.endswith('<') and source[m.end] == '>')
                                ):
                                    max_len = m.end - first_index + 1

                    if max_len != 0:
                        substr = source[start : start + length + max_len]
                        er = ExtractResult()

                        er.start = start
                        er.length = length + max_len
                        er.text = substr
                        er.type = self.config.extract_type

                        if prefix_unit is not None:
                            prefix_matched = True
                            er.start -= prefix_unit[0].offset
                            er.length += prefix_unit[0].offset
                            er.text = prefix_unit[0].unit + er.text

                        # Relative position will be used in Parser
                        number.start = start - er.start
                        er.data = number

                        # Special treatment, handle cases like '2:00 pm', '00 pm' is not dimension
                        is_not_unit = False

                        if er.type is Constants.SYS_UNIT_DIMENSION:
                            if non_unit_match is None:
                                non_unit_match = list(self.config.non_unit_regex.finditer(source))
                            for time in non_unit_match:
                                trimmed_source = source.lower()
                                index = trimmed_source.index(time.group())
                                if er.start >= time.start() and er.start + er.length <= time.start() + len(
                                    time.group()
                                ):
                                    is_not_unit = True
                                    break

                        if is_not_unit:
                            continue

                        result.append(er)
                        unit_is_prefix.append(False)

                if prefix_unit and prefix_unit is not None and not prefix_matched:
                    er = ExtractResult()
                    er.start = number.start - prefix_unit[0].offset
                    er.length = number.length + prefix_unit[0].offset
                    er.text = prefix_unit[0].unit + number.text
                    er.type = self.config.extract_type

                    # Relative position will be used in Parser
                    number.start = start - er.start
                    er.data = number
                    result.append(er)
                    unit_is_prefix.append(True)

        # Extract Separate unit
        if self.separate_regex:
            if non_unit_match is None:
                try:
                    non_unit_match = list(self.config.non_unit_regex.match(source))
                except:
                    non_unit_match = []

            self._extract_separate_units(source, result, non_unit_match)

            # Remove common ambiguous cases
            result = self._filter_ambiguity(result, source)
            # Remove entity-specific ambiguous case
            if self.config.extract_type == Constants.SYS_UNIT_DIMENSION:
                result = self._filter_ambiguity(result, source, self.config.dimension_ambiguity_filters_dict)

            if self.config.extract_type == Constants.SYS_UNIT_CURRENCY:
                result = self._select_candidates(source, result, unit_is_prefix)

        # Expand Chinese phrase to the `half` patterns when it follows closely origin phrase.
        self.config.expand_half_suffix(source, result, numbers)

        return result

    def validate_unit(self, source: str) -> bool:
        return not source.startswith('-')

    def _pre_check_str(self, source: str) -> bool:
        return len(source) != 0

    def _extract_separate_units(
        self, source: str, num_depend_source: List[ExtractResult], non_unit_matches
    ) -> List[ExtractResult]:
        result = deepcopy(num_depend_source)
        match_result: List[bool] = [False] * len(source)
        for ex_result in num_depend_source:
            start = ex_result.start
            i = 0
            while i < ex_result.length:
                match_result[start + i] = True
                i += 1

        match_collection = list(filter(lambda x: x.group(), regex.finditer(self.separate_regex, source)))
        for match in match_collection:
            i = 0
            while i < len(match.group()) and not match_result[match.start() + i]:
                i += 1
            if i == len(match.group()):
                for j in range(i):
                    match_result[j] = True

                is_not_unit = False
                if match.group() == Constants.AMBIGUOUS_TIME_TERM:
                    for time in non_unit_matches:
                        if self._dimension_inside_time(match, time):
                            is_not_unit = True

                if is_not_unit:
                    continue

                to_add = ExtractResult()
                to_add.start = match.start()
                to_add.length = len(match.group())
                to_add.text = match.group()
                to_add.type = self.config.extract_type
                num_depend_source.append(to_add)

    def _build_regex_from_set(self, definitions: List[str], ignore_case: bool = False) -> Set[Pattern]:
        return set(map(lambda x: self.__build_regex_from_str(x, ignore_case), definitions))

    def _build_matcher_from_set(self, definitions) -> StringMatcher:

        matcher = StringMatcher(match_strategy=MatchStrategy.TrieTree, tokenizer=NumberWithUnitTokenizer())

        match_term_list = list(
            map(
                lambda words: list(
                    filter(lambda word: not str.isspace(word) and word is not None, str(words).strip().split('|'))
                ),
                definitions,
            )
        )

        match_terms = self.distinct(match_term_list)

        flatten = [item for sublist in match_terms for item in sublist]

        matcher.init(flatten)

        return matcher

    def __build_regex_from_str(self, source: str, ignore_case: bool) -> Pattern:
        tokens = map(regex.escape, source.split('|'))
        definition = '|'.join(tokens)
        definition = f'{self.config.build_prefix}({definition}){self.config.build_suffix}'
        flags = regex.S + regex.I if ignore_case else regex.S
        return RegExpUtility.get_safe_reg_exp(definition, flags)

    def _build_separate_regex_from_config(self, ignore_case: bool = False) -> Pattern:
        separate_words: Set[str] = set()
        for add_word in self.config.prefix_list.values():
            separate_words |= set(filter(self.validate_unit, add_word.split('|')))
        for add_word in self.config.suffix_list.values():
            separate_words |= set(filter(self.validate_unit, add_word.split('|')))
        for to_delete in self.config.ambiguous_unit_list:
            separate_words.discard(to_delete)

        tokens = map(regex.escape, separate_words)
        if not tokens:
            return None

        tokens = sorted(tokens, key=len, reverse=True)
        definition = '|'.join(tokens)
        definition = f'{self.config.build_prefix}({definition}){self.config.build_suffix}'
        flags = regex.S + regex.I if ignore_case else regex.S
        return RegExpUtility.get_safe_reg_exp(definition, flags)

    def _dino_comparer(self, x: str, y: str) -> int:
        if not x:
            if not y:
                return 0
            else:
                return 1
        else:
            if not y:
                return -1
            else:
                if len(x) != len(y):
                    return len(y) - len(x)
                else:
                    if x.lower() < y.lower():
                        return -1
                    if y.lower() < x.lower():
                        return 1
                    return 0

    @staticmethod
    def _dimension_inside_time(dimension: Match, time: Match) -> bool:
        is_sub_match = False
        if dimension.start() >= time.start() and dimension.end() <= time.end():
            is_sub_match = True

        return is_sub_match

    @staticmethod
    def distinct(list1):

        # initialize a null list
        unique_list = []

        # traverse for all elements
        for x in list1:
            # check if exists in unique_list or not
            if x not in unique_list:
                unique_list.append(x)
            # print list
        return unique_list

    @staticmethod
    def add_element(dict, key, value):
        if key not in dict:
            dict[key] = []
        dict[key].append(value)

    def _filter_ambiguity(self, ers: List[ExtractResult], text: str, ambiguity_filter_dict=None) -> List[ExtractResult]:

        # If no filter is specified, use common AmbiguityFilter
        if ambiguity_filter_dict is None:
            ambiguity_filter_dict = self.config.ambiguity_filters_dict

        if ambiguity_filter_dict is not None:
            for regex_var in ambiguity_filter_dict:
                regexvar_value = ambiguity_filter_dict[regex_var]
                for er in ers:
                    match = list(filter(lambda x: x.group(), regex.finditer(regex_var, ers[0].text)))

                    if match and len(match) > 0:
                        try:
                            reg_match = list(filter(lambda x: x.group(), regex.finditer(regexvar_value, text)))

                            if len(reg_match) > 0:
                                ers = list(
                                    filter(
                                        lambda x: not any(
                                            [
                                                m.start() < x.start + x.length and m.start() + len(m.group()) > x.start
                                                for m in reg_match
                                            ]
                                        ),
                                        ers,
                                    )
                                )
                        except Exception:
                            pass

        # filter single-char units if not exact match
        try:
            scu_regex = self.single_char_unit_regex

            ers = list(filter(lambda er: not (er.length != len(text) and bool(regex.match(scu_regex, er.text))), ers))

        except Exception:
            pass

        return ers

    def _select_candidates(
        self, source: str, ers: List[ExtractResult], unit_is_prefix: List[bool]
    ) -> List[ExtractResult]:

        total_candidate = len(unit_is_prefix)
        have_conflict = False
        for index in range(1, total_candidate):
            if ers[index - 1].end > ers[index].start:
                have_conflict = True

        if not have_conflict:
            return ers

        prefix_result: List[ExtractResult] = []
        suffix_result: List[ExtractResult] = []
        current_end = -1

        for index in range(total_candidate):
            if current_end < ers[index].start:
                current_end = ers[index].end
                prefix_result.append(ers[index])
            else:
                if unit_is_prefix[index]:
                    prefix_result.pop(-1)
                    current_end = ers[index].end
                    prefix_result.append(ers[index])

        current_end = len(source)
        for index in range(total_candidate - 1, -1, -1):
            if current_end >= ers[index].end:
                current_end = ers[index].start
                suffix_result.append(ers[index])
            else:
                if not unit_is_prefix[index]:
                    suffix_result.pop(-1)
                    current_end = ers[index].start
                    suffix_result.append(ers[index])

        # Find prefix units with no space, e.g. '$50'.
        no_space_units: List[Token] = []
        for unit_prefix in prefix_result:
            if isinstance(unit_prefix.data, ExtractResult):
                unit_str = unit_prefix.text[: unit_prefix.data.start]
                if len(unit_str) > 0 and unit_str == unit_str.rstrip():
                    no_space_units.append(Token(unit_prefix.start, unit_prefix.start + len(unit_str)))

        # Remove from suffixResult units that are also prefix units with no space,
        # e.g. in '1 $50', '$' should not be considered a suffix unit.
        for index in range(len(suffix_result) - 1, -1, -1):
            suffix = suffix_result[index]
            if any(suffix.start <= unit.start and suffix.end >= unit.end for unit in no_space_units):
                suffix_result.pop(index)

        # Add Separate unit
        for index in range(total_candidate, len(ers)):
            prefix_result.append(ers[index])
            suffix_result.append(ers[index])

        if len(suffix_result) >= len(prefix_result):

            def sort_by_start(e):
                return e.start

            suffix_result.sort(key=sort_by_start)
            return suffix_result

        return prefix_result


class BaseMergedUnitExtractor(Extractor):
    def __init__(self, config: NumberWithUnitExtractorConfiguration):
        self.config = config

    def extract(self, source: str) -> List[ExtractResult]:
        if self.config.extract_type == Constants.SYS_UNIT_CURRENCY:
            result = self.__merged_compound_units(source)
        else:
            result = NumberWithUnitExtractor(self.config).extract(source)

        return result

    def __merged_compound_units(self, source: str):
        ers = NumberWithUnitExtractor(self.config).extract(source)
        ers = self.__merge_pure_number(source, ers)

        result = []
        groups = [0] * len(ers)

        idx = 0
        while idx < len(ers) - 1:
            if (
                ers[idx].type != ers[idx + 1].type
                and not ers[idx].type == Constants.SYS_NUM
                and not ers[idx + 1].type == Constants.SYS_NUM
            ):
                idx = idx + 1
                continue

            if isinstance(ers[idx].data, ExtractResult) and not str(ers[idx].data.data).startswith("Integer"):
                groups[idx + 1] = groups[idx] + 1
                idx = idx + 1
                continue

            middle_begin = ers[idx].start + ers[idx].length
            middle_end = ers[idx + 1].start

            middle_str = source[middle_begin : middle_begin + (middle_end - middle_begin)].strip().lower()

            # Separated by whitespace
            if not middle_str:
                groups[idx + 1] = groups[idx]
                idx = idx + 1
                continue

            # Separated by connector
            match = self.config.compound_unit_connector_regex.match(middle_str)
            if match is not None:
                splitted_match = match.string.split(" ")
            if match and match.pos == 0 and len(splitted_match[0]) == len(middle_str):
                groups[idx + 1] = groups[idx]
            else:
                groups[idx + 1] = groups[idx] + 1

            idx = idx + 1

        idx = 0
        while idx < len(ers):
            if idx == 0 or groups[idx] != groups[idx - 1]:
                tmp_extract_result = ers[idx]
                tmp = ExtractResult()
                tmp.data = ers[idx].data
                tmp.length = ers[idx].length
                tmp.start = ers[idx].start
                tmp.text = ers[idx].text
                tmp.type = ers[idx].type
                tmp_extract_result.data = [tmp]

                result.append(tmp_extract_result)

            # reduce extract results in same group
            if idx + 1 < len(ers) and groups[idx + 1] == groups[idx]:
                group = groups[idx]

                period_begin = result[group].start
                period_end = ers[idx + 1].start + ers[idx + 1].length

                result[group].length = period_end - period_begin
                result[group].text = source[period_begin : period_begin + (period_end - period_begin)]
                result[group].type = Constants.SYS_UNIT_CURRENCY
                if isinstance(result[group].data, list):
                    result[group].data.append(ers[idx + 1])

            idx = idx + 1

        idx = 0
        while idx < len(result):
            inner_data = result[idx].data
            if len(inner_data) == 1:
                result[idx] = inner_data[0]
            idx = idx + 1

        result = [x for x in result if not x.type == Constants.SYS_NUM]

        return result

    def __merge_pure_number(self, source: str, ers: List[ExtractResult]) -> List[ExtractResult]:
        num_ers = self.config.unit_num_extractor.extract(source)
        unit_numbers = []
        i = j = 0
        while i < len(num_ers):
            has_behind_extraction = False

            while j < len(ers) and ers[j].start + ers[j].length < num_ers[i].start:
                has_behind_extraction = True
                j = j + 1

            if not has_behind_extraction:
                i = i + 1
                continue

            middle_begin = ers[j - 1].start + ers[j - 1].length
            middle_end = num_ers[i].start

            middle_str = source[middle_begin : middle_begin + (middle_end - middle_begin)].strip().lower()

            # separated by whitespace
            if not middle_str:
                unit_numbers.append(num_ers[i])
                i = i + 1
                continue

            match = self.config.compound_unit_connector_regex.match(middle_str)
            if match is not None:
                splitted_match = match.string.split(" ")
            if match and match.pos == 0 and len(splitted_match[0]) == len(middle_str):
                unit_numbers.append(num_ers[i])
                i = i + 1
                continue

            i = i + 1

        for extract_result in unit_numbers:
            overlap = False
            for er in ers:
                if er.start <= extract_result.start and er.start + er.length >= extract_result.start:
                    overlap = True

            if not overlap:
                ers.append(extract_result)

        ers = sorted(ers, key=lambda e: e.start)

        return ers
