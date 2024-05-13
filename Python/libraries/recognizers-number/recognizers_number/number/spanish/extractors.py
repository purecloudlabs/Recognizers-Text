#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from typing import List

from recognizers_number.number.constants import Constants
from recognizers_number.number.extractors import BaseNumberExtractor, ReRe, ReVal
from recognizers_number.number.models import LongFormatMode, NumberMode
from recognizers_number.resources.spanish_numeric import SpanishNumeric
from recognizers_text.utilities import RegExpUtility


class SpanishNumberExtractor(BaseNumberExtractor):
    extract_type: str = Constants.SYS_NUM

    @property
    def regexes(self) -> List[ReVal]:
        _regexes: List[ReVal] = []
        cardinal_ex: SpanishCardinalExtractor = None

        if self.mode is NumberMode.PURE_NUMBER:
            cardinal_ex = SpanishCardinalExtractor(SpanishNumeric.PlaceHolderPureNumber)
        elif self.mode is NumberMode.CURRENCY:
            _regexes.append(ReVal(re=SpanishNumeric.CurrencyRegex, val='IntegerNum'))

        cardinal_ex = cardinal_ex or SpanishCardinalExtractor()
        _regexes.extend(cardinal_ex.regexes)
        fraction_ex = SpanishFractionExtractor(self.mode)
        _regexes.extend(fraction_ex.regexes)
        return _regexes

    @property
    def ambiguity_filters_dict(self) -> List[ReRe]:
        _ambiguity_filters_dict: List[ReRe] = list()
        if self.mode != NumberMode.Unit:
            for key, value in SpanishNumeric.AmbiguityFiltersDict.items():
                _ambiguity_filters_dict.append(
                    ReRe(reKey=RegExpUtility.get_safe_reg_exp(key), reVal=RegExpUtility.get_safe_reg_exp(value))
                )
        return _ambiguity_filters_dict

    def __init__(self, mode: NumberMode = NumberMode.DEFAULT):
        self.mode = mode


class SpanishCardinalExtractor(BaseNumberExtractor):
    extract_type: str = Constants.SYS_NUM_CARDINAL

    @property
    def regexes(self) -> List[ReVal]:
        return SpanishIntegerExtractor(self.placeholder).regexes + SpanishDoubleExtractor(self.placeholder).regexes

    def __init__(self, placeholder: str = SpanishNumeric.PlaceHolderDefault):
        self.placeholder = placeholder


class SpanishIntegerExtractor(BaseNumberExtractor):
    extract_type: str = Constants.SYS_NUM_INTEGER

    @property
    def regexes(self) -> List[ReVal]:
        return [
            ReVal(re=SpanishNumeric.NumbersWithPlaceHolder(self.placeholder), val='IntegerNum'),
            ReVal(re=SpanishNumeric.NumbersWithSuffix, val='IntegerNum'),
            ReVal(re=self._generate_format_regex(LongFormatMode.INTEGER_DOT, self.placeholder), val='IntegerNum'),
            ReVal(re=self._generate_format_regex(LongFormatMode.INTEGER_BLANK, self.placeholder), val='IntegerNum'),
            ReVal(
                re=self._generate_format_regex(LongFormatMode.INTEGER_NO_BREAK_SPACE, self.placeholder),
                val='IntegerNum',
            ),
            ReVal(re=SpanishNumeric.RoundNumberIntegerRegexWithLocks, val='IntegerNum'),
            ReVal(re=SpanishNumeric.NumbersWithDozenSuffix, val='IntegerNum'),
            ReVal(re=SpanishNumeric.AllIntRegexWithLocks, val='IntegerSpa'),
            ReVal(re=SpanishNumeric.AllIntRegexWithDozenSuffixLocks, val='IntegerSpa'),
        ]

    def __init__(self, placeholder: str = SpanishNumeric.PlaceHolderDefault):
        self.placeholder = placeholder


class SpanishDoubleExtractor(BaseNumberExtractor):
    extract_type: str = Constants.SYS_NUM_DOUBLE

    @property
    def regexes(self) -> List[ReVal]:
        return [
            ReVal(re=SpanishNumeric.DoubleDecimalPointRegex(self.placeholder), val='DoubleNum'),
            ReVal(re=SpanishNumeric.DoubleWithoutIntegralRegex(self.placeholder), val='DoubleNum'),
            ReVal(re=SpanishNumeric.DoubleWithMultiplierRegex, val='DoubleNum'),
            ReVal(re=SpanishNumeric.DoubleWithRoundNumber, val='DoubleNum'),
            ReVal(re=SpanishNumeric.DoubleAllFloatRegex, val='DoubleSpa'),
            ReVal(re=SpanishNumeric.DoubleExponentialNotationRegex, val='DoublePow'),
            ReVal(re=SpanishNumeric.DoubleCaretExponentialNotationRegex, val='DoublePow'),
            ReVal(re=self._generate_format_regex(LongFormatMode.DOUBLE_DOT_COMMA, self.placeholder), val='DoubleNum'),
            ReVal(
                re=self._generate_format_regex(LongFormatMode.DOUBLE_NO_BREAK_SPACE_COMMA, self.placeholder),
                val='DoubleNum',
            ),
        ]

    def __init__(self, placeholder: str = SpanishNumeric.PlaceHolderDefault):
        self.placeholder = placeholder


class SpanishFractionExtractor(BaseNumberExtractor):
    extract_type: str = Constants.SYS_NUM_FRACTION

    @property
    def regexes(self) -> List[ReVal]:
        _regexes = [
            ReVal(re=SpanishNumeric.FractionNotationRegex, val='FracNum'),
            ReVal(re=SpanishNumeric.FractionNotationWithSpacesRegex, val='FracNum'),
            ReVal(re=SpanishNumeric.FractionNounRegex, val='FracSpa'),
            ReVal(re=SpanishNumeric.FractionNounWithArticleRegex, val='FracSpa'),
        ]
        if self.mode != NumberMode.Unit:
            _regexes.append(ReVal(re=SpanishNumeric.FractionPrepositionRegex, val='FracSpa'))
        return _regexes

    def __init__(self, mode: NumberMode = NumberMode.DEFAULT):
        self.mode = mode


class SpanishOrdinalExtractor(BaseNumberExtractor):
    extract_type: str = Constants.SYS_NUM_ORDINAL

    @property
    def regexes(self) -> List[ReVal]:
        return [
            ReVal(re=SpanishNumeric.OrdinalSuffixRegex, val='OrdinalNum'),
            ReVal(re=SpanishNumeric.OrdinalNounRegex, val='OrdSpa'),
        ]
