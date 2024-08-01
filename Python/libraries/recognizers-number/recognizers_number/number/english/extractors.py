#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from typing import List, Pattern

import regex

from recognizers_number.number.constants import Constants
from recognizers_number.number.extractors import BaseMergedNumberExtractor, BaseNumberExtractor, ReRe, ReVal
from recognizers_number.number.models import LongFormatMode, NumberMode
from recognizers_number.resources.english_numeric import EnglishNumeric
from recognizers_text.utilities import RegExpUtility


class EnglishNumberExtractor(BaseNumberExtractor):
    extract_type: str = Constants.SYS_NUM

    @property
    def regexes(self) -> List[ReVal]:
        _regexes: List[ReVal] = []
        cardinal_ex: EnglishCardinalExtractor = None

        if self.mode is NumberMode.PURE_NUMBER:
            cardinal_ex = EnglishCardinalExtractor(EnglishNumeric.PlaceHolderPureNumber)
        elif self.mode is NumberMode.CURRENCY:
            _regexes.append(ReVal(re=RegExpUtility.get_safe_reg_exp(EnglishNumeric.CurrencyRegex), val='IntegerNum'))

        cardinal_ex = cardinal_ex or EnglishCardinalExtractor()
        _regexes.extend(cardinal_ex.regexes)

        fraction_ex = EnglishFractionExtractor(self.mode)
        _regexes.extend(fraction_ex.regexes)
        return _regexes

    @property
    def ambiguity_filters_dict(self) -> List[ReRe]:
        _ambiguity_filters_dict: List[ReRe] = []
        if self.mode != NumberMode.Unit:
            for key, value in EnglishNumeric.AmbiguityFiltersDict.items():
                _ambiguity_filters_dict.append(
                    ReRe(reKey=RegExpUtility.get_safe_reg_exp(key), reVal=RegExpUtility.get_safe_reg_exp(value))
                )
        return _ambiguity_filters_dict

    @property
    def _negative_number_terms(self) -> Pattern:
        return RegExpUtility.get_safe_reg_exp(EnglishNumeric.NegativeNumberTermsRegex)

    def __init__(self, mode: NumberMode = NumberMode.DEFAULT):
        self.mode = mode


class EnglishCardinalExtractor(BaseNumberExtractor):
    extract_type: str = Constants.SYS_NUM_CARDINAL

    @property
    def regexes(self) -> List[ReVal]:
        return EnglishIntegerExtractor(self.placeholder).regexes + EnglishDoubleExtractor(self.placeholder).regexes

    def __init__(self, placeholder: str = EnglishNumeric.PlaceHolderDefault):
        self.placeholder = placeholder


class EnglishIntegerExtractor(BaseNumberExtractor):
    extract_type: str = Constants.SYS_NUM_INTEGER

    @property
    def regexes(self) -> List[ReVal]:
        return [
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(EnglishNumeric.NumbersWithPlaceHolder(self.placeholder)),
                val='IntegerNum',
            ),
            ReVal(re=RegExpUtility.get_safe_reg_exp(EnglishNumeric.NumbersWithSuffix, regex.S), val='IntegerNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    self._generate_format_regex(LongFormatMode.INTEGER_COMMA, self.placeholder)
                ),
                val='IntegerNum',
            ),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    self._generate_format_regex(LongFormatMode.INTEGER_BLANK, self.placeholder)
                ),
                val='IntegerNum',
            ),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    self._generate_format_regex(LongFormatMode.INTEGER_NO_BREAK_SPACE, self.placeholder)
                ),
                val='IntegerNum',
            ),
            ReVal(re=RegExpUtility.get_safe_reg_exp(EnglishNumeric.RoundNumberIntegerRegexWithLocks), val='IntegerNum'),
            ReVal(re=RegExpUtility.get_safe_reg_exp(EnglishNumeric.NumbersWithDozenSuffix), val='IntegerNum'),
            ReVal(re=RegExpUtility.get_safe_reg_exp(EnglishNumeric.AllIntRegexWithLocks), val='IntegerEng'),
            ReVal(re=RegExpUtility.get_safe_reg_exp(EnglishNumeric.AllIntRegexWithDozenSuffixLocks), val='IntegerEng'),
        ]

    def __init__(self, placeholder: str = EnglishNumeric.PlaceHolderDefault):
        self.placeholder = placeholder


class EnglishDoubleExtractor(BaseNumberExtractor):
    extract_type: str = Constants.SYS_NUM_DOUBLE

    @property
    def regexes(self) -> List[ReVal]:
        return [
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(EnglishNumeric.DoubleDecimalPointRegex(self.placeholder)),
                val='DoubleNum',
            ),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(EnglishNumeric.DoubleWithoutIntegralRegex(self.placeholder)),
                val='DoubleNum',
            ),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    self._generate_format_regex(LongFormatMode.DOUBLE_COMMA_DOT, self.placeholder)
                ),
                val='DoubleNum',
            ),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    self._generate_format_regex(LongFormatMode.DOUBLE_NO_BREAK_SPACE_DOT, self.placeholder)
                ),
                val='DoubleNum',
            ),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(EnglishNumeric.DoubleWithMultiplierRegex, regex.S), val='DoubleNum'
            ),
            ReVal(re=RegExpUtility.get_safe_reg_exp(EnglishNumeric.DoubleWithRoundNumber), val='DoubleNum'),
            ReVal(re=RegExpUtility.get_safe_reg_exp(EnglishNumeric.DoubleAllFloatRegex), val='DoubleEng'),
            ReVal(re=RegExpUtility.get_safe_reg_exp(EnglishNumeric.DoubleExponentialNotationRegex), val='DoublePow'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(EnglishNumeric.DoubleCaretExponentialNotationRegex), val='DoublePow'
            ),
        ]

    def __init__(self, placeholder: str = EnglishNumeric.PlaceHolderDefault):
        self.placeholder = placeholder


class EnglishFractionExtractor(BaseNumberExtractor):
    extract_type: str = Constants.SYS_NUM_FRACTION

    @property
    def regexes(self) -> List[ReVal]:
        _regexes = [
            ReVal(re=RegExpUtility.get_safe_reg_exp(EnglishNumeric.FractionNotationWithSpacesRegex), val='FracNum'),
            ReVal(re=RegExpUtility.get_safe_reg_exp(EnglishNumeric.FractionNotationRegex), val='FracNum'),
            ReVal(re=RegExpUtility.get_safe_reg_exp(EnglishNumeric.FractionNounRegex), val='FracEng'),
            ReVal(re=RegExpUtility.get_safe_reg_exp(EnglishNumeric.FractionNounWithArticleRegex), val='FracEng'),
        ]
        if self.mode != NumberMode.Unit:
            _regexes.append(
                ReVal(re=RegExpUtility.get_safe_reg_exp(EnglishNumeric.FractionPrepositionRegex), val='FracEng')
            )
        return _regexes

    def __init__(self, mode: NumberMode):
        self.mode = mode


class EnglishOrdinalExtractor(BaseNumberExtractor):
    extract_type: str = Constants.SYS_NUM_ORDINAL

    @property
    def regexes(self) -> List[ReVal]:
        return [
            ReVal(re=EnglishNumeric.OrdinalSuffixRegex, val='OrdinalNum'),
            ReVal(re=EnglishNumeric.OrdinalNumericRegex, val='OrdinalNum'),
            ReVal(re=EnglishNumeric.OrdinalEnglishRegex, val='OrdEng'),
            ReVal(re=EnglishNumeric.OrdinalRoundNumberRegex, val='OrdEng'),
        ]


class EnglishMergedNumberExtractor(BaseMergedNumberExtractor):

    @property
    def _round_number_integer_regex_with_locks(self) -> Pattern:
        return RegExpUtility.get_safe_reg_exp(EnglishNumeric.RoundNumberIntegerRegexWithLocks)

    @property
    def _connector_regex(self) -> Pattern:
        return RegExpUtility.get_safe_reg_exp(EnglishNumeric.ConnectorRegex)

    def __init__(self, mode: NumberMode = NumberMode.DEFAULT):
        self._number_extractor = EnglishNumberExtractor(mode)
