from typing import Pattern, List, NamedTuple
from collections import namedtuple
import regex

from recognizers_text.extractor import ExtractResult
from recognizers_number.number.models import NumberMode, LongFormatMode
from recognizers_number.resources.minimal_numeric import MinimalNumeric
from recognizers_number.number.extractors import ReVal, ReRe, BaseNumberExtractor
from recognizers_number.number.constants import Constants

ReVal = namedtuple('ReVal', ['re', 'val'])
ReRe = namedtuple('ReRe', ['reKey', 'reVal'])
MatchesVal = namedtuple('MatchesVal', ['matches', 'val'])


class MinimalNumberExtractor(BaseNumberExtractor):
    @property
    def regexes(self) -> List[ReVal]:
        return self.__regexes

    @property
    def ambiguity_filters_dict(self) -> List[ReRe]:
        return self.__ambiguity_filters_dict

    @property
    def _extract_type(self) -> str:
        return Constants.SYS_NUM

    def __init__(self, mode: NumberMode = NumberMode.DEFAULT):
        self.__regexes: List[ReVal] = list()
        cardinal_ex: MinimalCardinalExtractor = None

        if mode is NumberMode.PURE_NUMBER:
            cardinal_ex = MinimalCardinalExtractor(
                MinimalNumeric.PlaceHolderPureNumber)
        elif mode is NumberMode.CURRENCY:
            self.__regexes.append(
                ReVal(re=MinimalNumeric.CurrencyRegex, val='IntegerNum'))

        if cardinal_ex is None:
            cardinal_ex = MinimalCardinalExtractor()

        self.__regexes.extend(cardinal_ex.regexes)

        ambiguity_filters_dict: List[ReRe] = list()

        self.__ambiguity_filters_dict = ambiguity_filters_dict

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
                    substr = source[start:start + length].strip()
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
                            substr = source[start:start + length].strip()

                    if src_match is not None:
                        value = ExtractResult()
                        value.start = start
                        value.length = length
                        value.text = substr
                        value.type = self._extract_type
                        value.data = match_source.get(src_match, None)
                        result.append(value)

        result = self._filter_ambiguity(result, source)
        return result


class MinimalCardinalExtractor(BaseNumberExtractor):
    @property
    def regexes(self) -> List[ReVal]:
        return self.__regexes

    @property
    def _extract_type(self) -> str:
        return Constants.SYS_NUM_CARDINAL

    def __init__(self, placeholder: str = MinimalNumeric.PlaceHolderDefault):
        self.__regexes: List[ReVal] = list()

        # Add integer regexes
        integer_ex = MinimalIntegerExtractor(placeholder)
        self.__regexes.extend(integer_ex.regexes)

        # Add double regexes
        double_ex = MinimalDoubleExtractor(placeholder)
        self.__regexes.extend(double_ex.regexes)


class MinimalIntegerExtractor(BaseNumberExtractor):
    @property
    def regexes(self) -> List[
            NamedTuple('re_val', [('re', Pattern), ('val', str)])]:
        return self.__regexes

    @property
    def _extract_type(self) -> str:
        return Constants.SYS_NUM_INTEGER

    def __init__(self, placeholder: str = MinimalNumeric.PlaceHolderDefault):
        self.__regexes = [
            ReVal(
                re=MinimalNumeric.NumbersWithPlaceHolder(placeholder),
                val='IntegerNum'),
            ReVal(
                re=MinimalNumeric.NumbersWithSuffix,
                val='IntegerNum'),
            ReVal(
                re=self._generate_format_regex(LongFormatMode.INTEGER_DOT,
                                               placeholder),
                val='IntegerNum'),
            ReVal(
                re=self._generate_format_regex(LongFormatMode.INTEGER_BLANK,
                                               placeholder),
                val='IntegerNum'),
            ReVal(
                re=self._generate_format_regex(
                    LongFormatMode.INTEGER_NO_BREAK_SPACE, placeholder),
                val='IntegerNum')
        ]


class MinimalDoubleExtractor(BaseNumberExtractor):
    @property
    def regexes(self) -> List[
            NamedTuple('re_val', [('re', Pattern), ('val', str)])]:
        return self.__regexes

    @property
    def _extract_type(self) -> str:
        return Constants.SYS_NUM_DOUBLE

    def __init__(self, placeholder: str = MinimalNumeric.PlaceHolderDefault):
        self.__regexes = [
            ReVal(
                re=MinimalNumeric.DoubleDecimalPointRegex(placeholder),
                val='DoubleNum'),
            ReVal(
                re=MinimalNumeric.DoubleWithoutIntegralRegex(placeholder),
                val='DoubleNum'),
            ReVal(
                re=MinimalNumeric.DoubleWithMultiplierRegex,
                val='DoubleNum'),
            ReVal(
                re=MinimalNumeric.DoubleExponentialNotationRegex,
                val='DoublePow'),
            ReVal(
                re=MinimalNumeric.DoubleCaretExponentialNotationRegex,
                val='DoublePow'),
            ReVal(
                re=self._generate_format_regex(LongFormatMode.DOUBLE_DOT_COMMA,
                                               placeholder),
                val='DoubleNum'),
            ReVal(
                re=self._generate_format_regex(
                    LongFormatMode.DOUBLE_NO_BREAK_SPACE_COMMA,
                    placeholder),
                val='DoubleNum')
        ]
