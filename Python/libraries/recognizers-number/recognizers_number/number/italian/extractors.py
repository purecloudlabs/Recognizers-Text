#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from typing import List, Pattern

import regex

from recognizers_number.number.constants import Constants
from recognizers_number.number.extractors import BaseMergedNumberExtractor, BaseNumberExtractor, ReRe, ReVal
from recognizers_number.number.models import LongFormatMode, NumberMode
from recognizers_number.resources.italian_numeric import ItalianNumeric
from recognizers_text.utilities import RegExpUtility


class ItalianNumberExtractor(BaseNumberExtractor):
    extract_type: str = Constants.SYS_NUM

    @property
    def regexes(self) -> List[ReVal]:
        _regexes: List[ReVal] = []
        cardinal_ex: ItalianCardinalExtractor = None

        if self.mode is NumberMode.PURE_NUMBER:
            cardinal_ex = ItalianCardinalExtractor(
                ItalianNumeric.PlaceHolderPureNumber)
        elif self.mode is NumberMode.CURRENCY:
            _regexes.append(ReVal(re=RegExpUtility.get_safe_reg_exp(
                ItalianNumeric.CurrencyRegex), val='IntegerNum'))

        cardinal_ex = cardinal_ex or ItalianCardinalExtractor()
        _regexes.extend(cardinal_ex.regexes)
        fraction_ex = ItalianFractionExtractor(self.mode)
        _regexes.extend(fraction_ex.regexes)
        return _regexes

    @property
    def ambiguity_filters_dict(self) -> List[ReRe]:
        _ambiguity_filters_dict: List[ReRe] = []

        if self.mode != NumberMode.Unit:
            for key, value in ItalianNumeric.AmbiguityFiltersDict.items():
                _ambiguity_filters_dict.append(ReRe(reKey=RegExpUtility.get_safe_reg_exp(key),
                                                    reVal=RegExpUtility.get_safe_reg_exp(value)))
        return _ambiguity_filters_dict

    @property
    def _negative_number_terms(self) -> Pattern:
        return RegExpUtility.get_safe_reg_exp(ItalianNumeric.NegativeNumberTermsRegex)

    def __init__(self, mode: NumberMode = NumberMode.DEFAULT):
        self.mode = mode


class ItalianCardinalExtractor(BaseNumberExtractor):
    extract_type: str = Constants.SYS_NUM_CARDINAL

    @property
    def regexes(self) -> List[ReVal]:
        return (ItalianIntegerExtractor(self.placeholder).regexes +
                ItalianDoubleExtractor(self.placeholder).regexes)

    def __init__(self, placeholder: str = ItalianNumeric.PlaceHolderDefault):
        self.placeholder = placeholder


class ItalianIntegerExtractor(BaseNumberExtractor):
    extract_type: str = Constants.SYS_NUM_INTEGER

    @property
    def regexes(self) -> List[ReVal]:
        return [
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    ItalianNumeric.NumbersWithPlaceHolder(self.placeholder)),
                val='IntegerNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    ItalianNumeric.NumbersWithSuffix, regex.S),
                val='IntegerNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(self._generate_format_regex(
                    LongFormatMode.INTEGER_DOT, self.placeholder)),
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
                re=RegExpUtility.get_safe_reg_exp(
                    ItalianNumeric.RoundNumberIntegerRegexWithLocks),
                val='IntegerNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    ItalianNumeric.NumbersWithDozenSuffix),
                val='IntegerNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    ItalianNumeric.AllIntRegexWithLocks),
                val=f'Integer{ItalianNumeric.LangMarker}'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    ItalianNumeric.AllIntRegexWithDozenSuffixLocks),
                val=f'Integer{ItalianNumeric.LangMarker}')
        ]

    def __init__(self, placeholder: str = ItalianNumeric.PlaceHolderDefault):
        self.placeholder = placeholder


class ItalianDoubleExtractor(BaseNumberExtractor):
    extract_type: str = Constants.SYS_NUM_DOUBLE

    @property
    def regexes(self) -> List[ReVal]:
        return [
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    ItalianNumeric.DoubleDecimalPointRegex(self.placeholder)),
                val='DoubleNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    ItalianNumeric.DoubleWithoutIntegralRegex(self.placeholder)),
                val='DoubleNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(self._generate_format_regex(
                    LongFormatMode.DOUBLE_COMMA_DOT, self.placeholder)),
                val='DoubleNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(self._generate_format_regex(
                    LongFormatMode.DOUBLE_NO_BREAK_SPACE_DOT, self.placeholder)),
                val='DoubleNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    ItalianNumeric.DoubleWithMultiplierRegex, regex.S),
                val='DoubleNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    ItalianNumeric.DoubleWithRoundNumber),
                val='DoubleNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    ItalianNumeric.DoubleAllFloatRegex),
                val=f'Double{ItalianNumeric.LangMarker}'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    ItalianNumeric.DoubleExponentialNotationRegex),
                val='DoublePow'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    ItalianNumeric.DoubleCaretExponentialNotationRegex),
                val='DoublePow')
        ]

    def __init__(self, placeholder: str = ItalianNumeric.PlaceHolderDefault):
        self.placeholder = placeholder


class ItalianFractionExtractor(BaseNumberExtractor):
    extract_type: str = Constants.SYS_NUM_FRACTION

    @property
    def regexes(self) -> List[ReVal]:
        _regexes = [
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    ItalianNumeric.FractionNotationWithSpacesRegex),
                val='FracNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    ItalianNumeric.FractionNotationRegex),
                val='FracNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    ItalianNumeric.FractionNounRegex),
                val=f'Frac{ItalianNumeric.LangMarker}'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    ItalianNumeric.FractionNounWithArticleRegex),
                val=f'Frac{ItalianNumeric.LangMarker}')
        ]

        if self.mode != NumberMode.Unit:
            _regexes.append(
                ReVal(
                    re=RegExpUtility.get_safe_reg_exp(
                        ItalianNumeric.FractionPrepositionRegex),
                    val=f'Frac{ItalianNumeric.LangMarker}'))
        return _regexes

    def __init__(self, mode: NumberMode = NumberMode.DEFAULT):
        self.mode = mode


class ItalianOrdinalExtractor(BaseNumberExtractor):
    extract_type: str = Constants.SYS_NUM_ORDINAL

    @property
    def regexes(self) -> List[ReVal]:
        return [
            ReVal(
                re=ItalianNumeric.OrdinalSuffixRegex,
                val='OrdinalNum'),
            ReVal(
                re=ItalianNumeric.OrdinalNumericRegex,
                val='OrdinalNum'),
            ReVal(
                re=ItalianNumeric.OrdinalItalianRegex,
                val=f'Ord{ItalianNumeric.LangMarker}'),
            ReVal(
                re=ItalianNumeric.OrdinalRoundNumberRegex,
                val=f'Ord{ItalianNumeric.LangMarker}')
        ]


class ItalianMergedNumberExtractor(BaseMergedNumberExtractor):

    @property
    def _round_number_integer_regex_with_locks(self) -> Pattern:
        return RegExpUtility.get_safe_reg_exp(ItalianNumeric.RoundNumberIntegerRegexWithLocks)

    @property
    def _connector_regex(self) -> Pattern:
        return RegExpUtility.get_safe_reg_exp(ItalianNumeric.ConnectorRegex)

    def __init__(self, mode: NumberMode = NumberMode.DEFAULT):
        self._number_extractor = ItalianNumberExtractor(mode)
