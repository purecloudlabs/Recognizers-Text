#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from typing import Pattern, List, NamedTuple
import regex

from recognizers_text.utilities import RegExpUtility
from recognizers_number.number.models import NumberMode, LongFormatMode
from recognizers_number.resources import BaseNumbers
from recognizers_number.resources.french_numeric import FrenchNumeric
from recognizers_number.number.extractors import ReVal, ReRe, BaseNumberExtractor
from recognizers_number.number.constants import Constants


class FrenchNumberExtractor(BaseNumberExtractor):
    extract_type: str = Constants.SYS_NUM

    @property
    def regexes(self) -> List[ReVal]:
        _regexes: List[ReVal] = []
        cardinal_ex: FrenchCardinalExtractor = None

        if self.mode is NumberMode.PURE_NUMBER:
            cardinal_ex = FrenchCardinalExtractor(
                FrenchNumeric.PlaceHolderPureNumber)
        elif self.mode is NumberMode.CURRENCY:
            _regexes.append(ReVal(re=RegExpUtility.get_safe_reg_exp(
                FrenchNumeric.CurrencyRegex), val='IntegerNum'))

        cardinal_ex = cardinal_ex or FrenchCardinalExtractor()
        _regexes.extend(cardinal_ex.regexes)

        fraction_ex = FrenchFractionExtractor(self.mode)
        _regexes.extend(fraction_ex.regexes)
        return _regexes

    @property
    def ambiguity_filters_dict(self) -> List[ReRe]:
        _ambiguity_filters_dict: List[ReRe] = list()
        if self.mode != NumberMode.Unit:
            for key, value in FrenchNumeric.AmbiguityFiltersDict.items():
                _ambiguity_filters_dict.append(ReRe(reKey=RegExpUtility.get_safe_reg_exp(key),
                                                    reVal=RegExpUtility.get_safe_reg_exp(value)))
        return _ambiguity_filters_dict

    @property
    def _negative_number_terms(self) -> Pattern:
        return RegExpUtility.get_safe_reg_exp(FrenchNumeric.NegativeNumberTermsRegex)

    def __init__(self, mode: NumberMode = NumberMode.DEFAULT):
        self.mode = mode


class FrenchCardinalExtractor(BaseNumberExtractor):
    extract_type: str = Constants.SYS_NUM_CARDINAL

    @property
    def regexes(self) -> List[ReVal]:
        return (FrenchIntegerExtractor(self.placeholder).regexes +
                FrenchDoubleExtractor(self.placeholder).regexes)

    def __init__(self, placeholder: str = FrenchNumeric.PlaceHolderDefault):
        self.placeholder = placeholder


class FrenchIntegerExtractor(BaseNumberExtractor):
    extract_type: str = Constants.SYS_NUM_INTEGER

    @property
    def regexes(self) -> List[ReVal]:
        return [
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    FrenchNumeric.NumbersWithPlaceHolder(self.placeholder), regex.I),
                val='IntegerNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    FrenchNumeric.NumbersWithSuffix, regex.S),
                val='IntegerNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(self._generate_format_regex(
                    LongFormatMode.INTEGER_DOT, self.placeholder), regex.V1),
                val='IntegerNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(self._generate_format_regex(
                    LongFormatMode.INTEGER_BLANK, self.placeholder)),
                val='IntegerNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(self._generate_format_regex(
                    LongFormatMode.INTEGER_NO_BREAK_SPACE, self.placeholder)),
                val='IntegerNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(FrenchNumeric.RoundNumberIntegerRegexWithLocks),
                val='IntegerNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(FrenchNumeric.NumbersWithDozenSuffix),
                val='IntegerNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(FrenchNumeric.AllIntRegexWithLocks),
                val=f'Integer{FrenchNumeric.LangMarker}'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(FrenchNumeric.AllIntRegexWithDozenSuffixLocks),
                val=f'Integer{FrenchNumeric.LangMarker}')
        ]

    def __init__(self, placeholder: str = FrenchNumeric.PlaceHolderDefault):
        self.placeholder = placeholder


class FrenchDoubleExtractor(BaseNumberExtractor):
    extract_type: str = Constants.SYS_NUM_DOUBLE

    @property
    def regexes(self) -> List[ReVal]:
        return [
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    FrenchNumeric.DoubleDecimalPointRegex(self.placeholder)),
                val='DoubleNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    FrenchNumeric.DoubleWithoutIntegralRegex(self.placeholder)),
                val='DoubleNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(self._generate_format_regex(
                    LongFormatMode.DOUBLE_DOT_COMMA, self.placeholder)),
                val='DoubleNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(self._generate_format_regex(
                    LongFormatMode.DOUBLE_NO_BREAK_SPACE_COMMA, self.placeholder)),
                val='DoubleNum'),
            ReVal(
                re=FrenchNumeric.DoubleWithMultiplierRegex,
                val='DoubleNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    FrenchNumeric.DoubleWithRoundNumber),
                val='DoubleNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    FrenchNumeric.DoubleAllFloatRegex),
                val=f'Double{FrenchNumeric.LangMarker}'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    FrenchNumeric.DoubleExponentialNotationRegex),
                val='DoublePow'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    FrenchNumeric.DoubleCaretExponentialNotationRegex),
                val='DoublePow')
        ]

    def __init__(self, placeholder: str = FrenchNumeric.PlaceHolderDefault):
        self.placeholder = placeholder


class FrenchFractionExtractor(BaseNumberExtractor):
    extract_type: str = Constants.SYS_NUM_FRACTION

    @property
    def regexes(self) -> List[ReVal]:
        _regexes = [
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    FrenchNumeric.FractionNotationWithSpacesRegex),
                val='FracNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    FrenchNumeric.FractionNotationRegex),
                val='FracNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    FrenchNumeric.FractionNounRegex),
                val=f'Frac{FrenchNumeric.LangMarker}'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    FrenchNumeric.FractionNounWithArticleRegex),
                val=f'Frac{FrenchNumeric.LangMarker}')
        ]

        if self.mode != NumberMode.Unit:
            _regexes.append(
                ReVal(
                    re=RegExpUtility.get_safe_reg_exp(
                        FrenchNumeric.FractionPrepositionRegex),
                    val=f'Frac{FrenchNumeric.LangMarker}'))
        return _regexes

    def __init__(self, mode: NumberMode = NumberMode.DEFAULT):
        self.mode = mode


class FrenchOrdinalExtractor(BaseNumberExtractor):
    extract_type: str = Constants.SYS_NUM_ORDINAL

    @property
    def regexes(self) -> List[ReVal]:
        return [
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    FrenchNumeric.OrdinalSuffixRegex),
                val='OrdinalNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    FrenchNumeric.OrdinalFrenchRegex),
                val=f'Ord{FrenchNumeric.LangMarker}')
        ]
