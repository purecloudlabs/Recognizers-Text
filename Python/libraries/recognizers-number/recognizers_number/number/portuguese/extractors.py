#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

import regex
from typing import Pattern, List, Optional

from recognizers_text.utilities import RegExpUtility
from recognizers_number.number.models import NumberMode, LongFormatMode
from recognizers_number.resources.portuguese_numeric import PortugueseNumeric
from recognizers_number.number.extractors import ReVal, ReRe, BaseNumberExtractor
from recognizers_number.number.constants import Constants


class PortugueseNumberExtractor(BaseNumberExtractor):
    extract_type: str = Constants.SYS_NUM

    @property
    def regexes(self) -> List[ReVal]:
        _regexes: List[ReVal] = []
        cardinal_ex: Optional[PortugueseCardinalExtractor] = None

        if self.mode is NumberMode.PURE_NUMBER:
            cardinal_ex = PortugueseCardinalExtractor(
                PortugueseNumeric.PlaceHolderPureNumber)
        elif self.mode is NumberMode.CURRENCY:
            _regexes.append(ReVal(re=RegExpUtility.get_safe_reg_exp(
                PortugueseNumeric.CurrencyRegex), val='IntegerNum'))

        cardinal_ex = cardinal_ex or PortugueseCardinalExtractor()
        _regexes.extend(cardinal_ex.regexes)
        fraction_ex = PortugueseFractionExtractor(self.mode)
        _regexes.extend(fraction_ex.regexes)
        return _regexes

    @property
    def ambiguity_filters_dict(self) -> List[ReRe]:
        _ambiguity_filters_dict: List[ReRe] = list()
        if self.mode != NumberMode.Unit:
            for key, value in PortugueseNumeric.AmbiguityFiltersDict.items():
                _ambiguity_filters_dict.append(ReRe(reKey=RegExpUtility.get_safe_reg_exp(key),
                                                    reVal=RegExpUtility.get_safe_reg_exp(value)))
        return _ambiguity_filters_dict

    @property
    def _negative_number_terms(self) -> Pattern:
        return RegExpUtility.get_safe_reg_exp(PortugueseNumeric.NegativeNumberTermsRegex)

    def __init__(self, mode: NumberMode = NumberMode.DEFAULT):
        self.mode = mode


class PortugueseCardinalExtractor(BaseNumberExtractor):
    extract_type: str = Constants.SYS_NUM_CARDINAL

    @property
    def regexes(self) -> List[ReVal]:
        return (PortugueseIntegerExtractor(self.placeholder).regexes +
                PortugueseDoubleExtractor(self.placeholder).regexes)

    def __init__(self, placeholder: str = PortugueseNumeric.PlaceHolderDefault):
        self.placeholder = placeholder


class PortugueseIntegerExtractor(BaseNumberExtractor):
    extract_type: str = Constants.SYS_NUM_INTEGER

    @property
    def regexes(self) -> List[ReVal]:
        return [
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    PortugueseNumeric.NumbersWithPlaceHolder(self.placeholder)),
                val='IntegerNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    PortugueseNumeric.NumbersWithSuffix, regex.S),
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
                    PortugueseNumeric.RoundNumberIntegerRegexWithLocks),
                val='IntegerNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    PortugueseNumeric.NumbersWithDozenSuffix),
                val='IntegerNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    PortugueseNumeric.AllIntRegexWithLocks),
                val='IntegerPor'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    PortugueseNumeric.AllIntRegexWithDozenSuffixLocks),
                val='IntegerPor')
        ]

    def __init__(self, placeholder: str = PortugueseNumeric.PlaceHolderDefault):
        self.placeholder = placeholder


class PortugueseDoubleExtractor(BaseNumberExtractor):
    extract_type: str = Constants.SYS_NUM_DOUBLE

    @property
    def regexes(self) -> List[ReVal]:
        return [
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    PortugueseNumeric.DoubleDecimalPointRegex(self.placeholder)),
                val='DoubleNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    PortugueseNumeric.DoubleWithoutIntegralRegex(self.placeholder)),
                val='DoubleNum'),
            ReVal(
                re=PortugueseNumeric.DoubleWithMultiplierRegex,
                val='DoubleNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    PortugueseNumeric.DoubleWithRoundNumber),
                val='DoubleNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    PortugueseNumeric.DoubleAllFloatRegex),
                val='DoublePor'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    PortugueseNumeric.DoubleExponentialNotationRegex),
                val='DoublePow'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    PortugueseNumeric.DoubleCaretExponentialNotationRegex),
                val='DoublePow'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(self._generate_format_regex(
                    LongFormatMode.DOUBLE_DOT_COMMA, self.placeholder)),
                val='DoubleNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(self._generate_format_regex(
                    LongFormatMode.DOUBLE_NO_BREAK_SPACE_COMMA, self.placeholder)),
                val='DoubleNum')
        ]

    def __init__(self, placeholder: str = PortugueseNumeric.PlaceHolderDefault):
        self.placeholder = placeholder


class PortugueseFractionExtractor(BaseNumberExtractor):
    extract_type: str = Constants.SYS_NUM_FRACTION

    @property
    def regexes(self) -> List[ReVal]:
        _regexes = [
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    PortugueseNumeric.FractionNotationWithSpacesRegex),
                val='FracNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    PortugueseNumeric.FractionNotationRegex),
                val='FracNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    PortugueseNumeric.FractionNounRegex),
                val='FracPor'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    PortugueseNumeric.FractionNounWithArticleRegex),
                val='FracPor')
        ]
        if self.mode != NumberMode.Unit:
            _regexes.append(ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    PortugueseNumeric.FractionPrepositionRegex),
                val='FracPor'))
        return _regexes

    def __init__(self, mode: NumberMode = NumberMode.DEFAULT):
        self.mode = mode


class PortugueseOrdinalExtractor(BaseNumberExtractor):
    extract_type: str = Constants.SYS_NUM_ORDINAL

    @property
    def regexes(self) -> List[ReVal]:
        return [
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    PortugueseNumeric.OrdinalSuffixRegex),
                val='OrdinalNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    PortugueseNumeric.OrdinalEnglishRegex),
                val='OrdinalPor')
        ]
