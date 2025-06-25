#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from typing import Pattern, List, NamedTuple
import regex

from recognizers_text.utilities import RegExpUtility
from recognizers_number.number.models import NumberMode, LongFormatMode
from recognizers_number.resources import BaseNumbers
from recognizers_number.resources.hungarian_numeric import HungarianNumeric
from recognizers_number.number.extractors import ReVal, ReRe, BaseNumberExtractor, BasePercentageExtractor, BaseMergedNumberExtractor
from recognizers_number.number.constants import Constants


class HungarianNumberExtractor(BaseNumberExtractor):
    @property
    def regexes(self) -> List[ReVal]:
        return self.__regexes

    @property
    def ambiguity_filters_dict(self) -> List[ReRe]:
        return self.__ambiguity_filters_dict

    @property
    def _extract_type(self) -> str:
        return Constants.SYS_NUM

    @property
    def _negative_number_terms(self) -> Pattern:
        return self.__negative_number_terms

    def __init__(self, mode: NumberMode = NumberMode.DEFAULT):
        self.__negative_number_terms = RegExpUtility.get_safe_reg_exp(
            HungarianNumeric.NegativeNumberTermsRegex)
        self.__regexes: List[ReVal] = list()
        cardinal_ex: HungarianCardinalExtractor = None

        if mode is NumberMode.PURE_NUMBER:
            cardinal_ex = HungarianCardinalExtractor(
                HungarianNumeric.PlaceHolderPureNumber)
        elif mode is NumberMode.CURRENCY:
            self.__regexes.append(ReVal(re=RegExpUtility.get_safe_reg_exp(
                BaseNumbers.CurrencyRegex), val='IntegerNum'))

        if cardinal_ex is None:
            cardinal_ex = HungarianCardinalExtractor()

        self.__regexes.extend(cardinal_ex.regexes)

        fraction_ex = HungarianFractionExtractor(mode)
        self.__regexes.extend(fraction_ex.regexes)

        ambiguity_filters_dict: List[ReRe] = list()

        if mode != NumberMode.Unit:
            for key, value in HungarianNumeric.AmbiguityFiltersDict.items():
                ambiguity_filters_dict.append(ReRe(reKey=RegExpUtility.get_safe_reg_exp(key),
                                                   reVal=RegExpUtility.get_safe_reg_exp(value)))
        self.__ambiguity_filters_dict = ambiguity_filters_dict


class HungarianCardinalExtractor(BaseNumberExtractor):
    @property
    def regexes(self) -> List[ReVal]:
        return self.__regexes

    @property
    def _extract_type(self) -> str:
        return Constants.SYS_NUM_CARDINAL

    def __init__(self, placeholder: str = HungarianNumeric.PlaceHolderDefault):
        self.__regexes: List[ReVal] = list()

        # Add integer regexes
        integer_ex = HungarianIntegerExtractor(placeholder)
        self.__regexes.extend(integer_ex.regexes)

        # Add double regexes
        double_ex = HungarianDoubleExtractor(placeholder)
        self.__regexes.extend(double_ex.regexes)


class HungarianIntegerExtractor(BaseNumberExtractor):
    @property
    def regexes(self) -> List[NamedTuple('re_val', [('re', Pattern), ('val', str)])]:
        return self.__regexes

    @property
    def _extract_type(self) -> str:
        return Constants.SYS_NUM_INTEGER

    def __init__(self, placeholder: str = HungarianNumeric.PlaceHolderDefault):
        self.__regexes = [
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    HungarianNumeric.NumbersWithPlaceHolder(placeholder)),
                val='IntegerNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    HungarianNumeric.NumbersWithSuffix, regex.S),
                val='IntegerNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(self._generate_format_regex(
                    LongFormatMode.INTEGER_COMMA, placeholder)),
                val='IntegerNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(self._generate_format_regex(
                    LongFormatMode.INTEGER_BLANK, placeholder)),
                val='IntegerNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(self._generate_format_regex(
                    LongFormatMode.INTEGER_NO_BREAK_SPACE, placeholder)),
                val='IntegerNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    HungarianNumeric.RoundNumberIntegerRegexWithLocks),
                val='IntegerNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    HungarianNumeric.NumbersWithDozenSuffix),
                val='IntegerNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    HungarianNumeric.AllIntRegexWithLocks),
                val='IntegerHun'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    HungarianNumeric.AllIntRegexWithDozenSuffixLocks),
                val='IntegerHun')
        ]


class HungarianDoubleExtractor(BaseNumberExtractor):
    @property
    def regexes(self) -> List[NamedTuple('re_val', [('re', Pattern), ('val', str)])]:
        return self.__regexes

    @property
    def _extract_type(self) -> str:
        return Constants.SYS_NUM_DOUBLE

    def __init__(self, placeholder):
        self.__regexes = [
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    HungarianNumeric.DoubleDecimalPointRegex(placeholder)),
                val='DoubleNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    HungarianNumeric.DoubleWithoutIntegralRegex(placeholder)),
                val='DoubleNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(self._generate_format_regex(
                    LongFormatMode.DOUBLE_COMMA_DOT, placeholder)),
                val='DoubleNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(self._generate_format_regex(
                    LongFormatMode.DOUBLE_NO_BREAK_SPACE_DOT, placeholder)),
                val='DoubleNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    HungarianNumeric.DoubleWithMultiplierRegex, regex.S),
                val='DoubleNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    HungarianNumeric.DoubleWithRoundNumber),
                val='DoubleNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    HungarianNumeric.DoubleAllFloatRegex),
                val='DoubleHun'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    HungarianNumeric.DoubleExponentialNotationRegex),
                val='DoublePow'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    HungarianNumeric.DoubleCaretExponentialNotationRegex),
                val='DoublePow')
        ]


class HungarianFractionExtractor(BaseNumberExtractor):
    @property
    def regexes(self) -> List[NamedTuple('re_val', [('re', Pattern), ('val', str)])]:
        return self.__regexes

    @property
    def _extract_type(self) -> str:
        return Constants.SYS_NUM_FRACTION

    def __init__(self, mode):
        self.__regexes = [
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    HungarianNumeric.FractionNotationWithSpacesRegex),
                val='FracNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    HungarianNumeric.FractionNotationRegex),
                val='FracNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    HungarianNumeric.FractionNounRegex),
                val='FracHun'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    HungarianNumeric.FractionNounWithArticleRegex),
                val='FracHun')
        ]

        if mode != NumberMode.Unit:
            self.__regexes.append(
                ReVal(
                    re=RegExpUtility.get_safe_reg_exp(
                        HungarianNumeric.FractionPrepositionRegex),
                    val='FracHun'))


class HungarianOrdinalExtractor(BaseNumberExtractor):
    @property
    def regexes(self) -> List[NamedTuple('re_val', [('re', Pattern), ('val', str)])]:
        return self.__regexes

    @property
    def _extract_type(self) -> str:
        return Constants.SYS_NUM_ORDINAL

    def __init__(self):
        self.__regexes = [
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(HungarianNumeric.OrdinalSuffixRegex),
                val='OrdinalNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(HungarianNumeric.OrdinalNumericRegex),
                val='OrdinalNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(HungarianNumeric.OrdinalHungarianRegex),
                val='OrdHun'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(HungarianNumeric.OrdinalRoundNumberRegex),
                val='OrdHun')
        ]


class HungarianPercentageExtractor(BasePercentageExtractor):
    def __init__(self):
        super().__init__(HungarianNumberExtractor(NumberMode.DEFAULT))

    def get_definitions(self) -> List[str]:
        return [
            HungarianNumeric.NumberWithSuffixPercentage,
            HungarianNumeric.NumberWithPrefixPercentage
        ]


class HungarianMergedNumberExtractor(BaseMergedNumberExtractor):

    @property
    def _round_number_integer_regex_with_locks(self) -> Pattern:
        return RegExpUtility.get_safe_reg_exp(HungarianNumeric.RoundNumberIntegerRegexWithLocks)

    @property
    def _connector_regex(self) -> Pattern:
        return RegExpUtility.get_safe_reg_exp(HungarianNumeric.ConnectorRegex)

    def __init__(self, mode: NumberMode = NumberMode.DEFAULT):
        self._number_extractor = HungarianNumberExtractor(mode)