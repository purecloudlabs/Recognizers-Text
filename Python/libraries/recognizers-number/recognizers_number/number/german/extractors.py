#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from typing import Pattern, List, NamedTuple
import regex

from recognizers_text.utilities import RegExpUtility
from recognizers_number.number.models import NumberMode, LongFormatMode
from recognizers_number.resources import BaseNumbers
from recognizers_number.resources.german_numeric import GermanNumeric
from recognizers_number.number.extractors import ReVal, ReRe, BaseNumberExtractor, BaseMergedNumberExtractor
from recognizers_number.number.constants import Constants


class GermanNumberExtractor(BaseNumberExtractor):
    extract_type: str = Constants.SYS_NUM

    @property
    def regexes(self) -> List[ReVal]:
        _regexes: List[ReVal] = list()
        cardinal_ex: GermanCardinalExtractor = None

        if self.mode is NumberMode.PURE_NUMBER:
            cardinal_ex = GermanCardinalExtractor(
                GermanNumeric.PlaceHolderPureNumber)
        elif self.mode is NumberMode.CURRENCY:
            _regexes.append(ReVal(re=RegExpUtility.get_safe_reg_exp(
                GermanNumeric.CurrencyRegex), val='IntegerNum'))

        cardinal_ex = cardinal_ex or GermanCardinalExtractor()
        _regexes.extend(cardinal_ex.regexes)
        fraction_ex = GermanFractionExtractor(self.mode)
        _regexes.extend(fraction_ex.regexes)
        return _regexes

    @property
    def ambiguity_filters_dict(self) -> List[ReRe]:
        _ambiguity_filters_dict: List[ReRe] = list()
        if self.mode != NumberMode.Unit:
            for key, value in GermanNumeric.AmbiguityFiltersDict.items():
                _ambiguity_filters_dict.append(ReRe(reKey=RegExpUtility.get_safe_reg_exp(key),
                                                    reVal=RegExpUtility.get_safe_reg_exp(value)))
        return _ambiguity_filters_dict

    @property
    def _negative_number_terms(self) -> Pattern:
        return RegExpUtility.get_safe_reg_exp(GermanNumeric.NegativeNumberTermsRegex)

    def __init__(self, mode: NumberMode = NumberMode.DEFAULT):
        self.mode = mode


class GermanCardinalExtractor(BaseNumberExtractor):
    extract_type: str = Constants.SYS_NUM_CARDINAL

    @property
    def regexes(self) -> List[ReVal]:
        return (GermanIntegerExtractor(self.placeholder).regexes +
                GermanDoubleExtractor(self.placeholder).regexes)

    def __init__(self, placeholder: str = GermanNumeric.PlaceHolderDefault):
        self.placeholder = placeholder


class GermanIntegerExtractor(BaseNumberExtractor):
    extract_type: str = Constants.SYS_NUM_INTEGER

    @property
    def regexes(self) -> List[ReVal]:
        return [
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    GermanNumeric.NumbersWithPlaceHolder(self.placeholder)),
                val='IntegerNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    GermanNumeric.NumbersWithSuffix, regex.S),
                val='IntegerNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(self._generate_format_regex(
                    LongFormatMode.INTEGER_COMMA, self.placeholder)),
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
                    GermanNumeric.RoundNumberIntegerRegexWithLocks),
                val='IntegerNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    GermanNumeric.NumbersWithDozenSuffix),
                val='IntegerNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    GermanNumeric.AllIntRegexWithLocks),
                val='IntegerGer'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    GermanNumeric.AllIntRegexWithDozenSuffixLocks),
                val='IntegerGer')
        ]

    def __init__(self, placeholder: str = GermanNumeric.PlaceHolderDefault):
        self.placeholder = placeholder


class GermanDoubleExtractor(BaseNumberExtractor):
    extract_type: str = Constants.SYS_NUM_DOUBLE

    @property
    def regexes(self) -> List[ReVal]:
        return [
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    GermanNumeric.DoubleDecimalPointRegex(self.placeholder)),
                val='DoubleNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    GermanNumeric.DoubleWithoutIntegralRegex(self.placeholder)),
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
                    GermanNumeric.DoubleWithMultiplierRegex, regex.S),
                val='DoubleNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    GermanNumeric.DoubleWithRoundNumber),
                val='DoubleNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    GermanNumeric.DoubleAllFloatRegex),
                val='DoubleGer'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    GermanNumeric.DoubleExponentialNotationRegex),
                val='DoublePow'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    GermanNumeric.DoubleCaretExponentialNotationRegex),
                val='DoublePow')
        ]

    def __init__(self, placeholder: str = GermanNumeric.PlaceHolderDefault):
        self.placeholder = placeholder


class GermanFractionExtractor(BaseNumberExtractor):
    extract_type: str = Constants.SYS_NUM_FRACTION

    @property
    def regexes(self) -> List[ReVal]:
        _regexes = [
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    GermanNumeric.FractionNotationWithSpacesRegex),
                val='FracNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    GermanNumeric.FractionNotationRegex),
                val='FracNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    GermanNumeric.FractionNounRegex),
                val='FracGer'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    GermanNumeric.FractionNounWithArticleRegex),
                val='FracGer')
        ]

        if self.mode != NumberMode.Unit:
            _regexes.append(
                ReVal(
                    re=RegExpUtility.get_safe_reg_exp(
                        GermanNumeric.FractionPrepositionRegex),
                    val='FracGer'))
        return _regexes

    def __init__(self, mode: NumberMode = NumberMode.DEFAULT):
        self.mode = mode


class GermanOrdinalExtractor(BaseNumberExtractor):
    extract_type: str = Constants.SYS_NUM_ORDINAL

    @property
    def regexes(self) -> List[ReVal]:
        return [
            ReVal(re=GermanNumeric.OrdinalSuffixRegex, val='OrdinalNum'),
            ReVal(re=GermanNumeric.OrdinalNumericRegex, val='OrdinalNum'),
            ReVal(re=GermanNumeric.OrdinalGermanRegex, val='OrdGer'),
            ReVal(re=GermanNumeric.OrdinalRoundNumberRegex, val='OrdGer')
        ]


class GermanMergedNumberExtractor(BaseMergedNumberExtractor):

    @property
    def _round_number_integer_regex_with_locks(self) -> Pattern:
        return RegExpUtility.get_safe_reg_exp(GermanNumeric.RoundNumberIntegerRegexWithLocks)

    @property
    def _connector_regex(self) -> Pattern:
        return RegExpUtility.get_safe_reg_exp(GermanNumeric.ConnectorRegex)

    def __init__(self, mode: NumberMode = NumberMode.DEFAULT):
        self._number_extractor = GermanNumberExtractor(mode)
