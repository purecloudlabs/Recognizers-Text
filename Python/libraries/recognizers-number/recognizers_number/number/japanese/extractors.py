#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from typing import List
from enum import Enum

from recognizers_number.number.extractors import ReVal, BaseNumberExtractor
from recognizers_number.number.models import NumberMode
from recognizers_text.utilities import RegExpUtility
from recognizers_number.number.constants import Constants
from recognizers_number.resources.japanese_numeric import JapaneseNumeric


class JapaneseNumberExtractorMode(Enum):
    DEFAULT = 0
    EXTRACT_ALL = 1


class JapaneseNumberExtractor(BaseNumberExtractor):
    @property
    def regexes(self) -> List[ReVal]:
        return self.__regexes

    @property
    def _extract_type(self) -> str:
        return Constants.SYS_NUM

    def __init__(self, mode: JapaneseNumberExtractorMode = JapaneseNumberExtractorMode.DEFAULT):
        self.__regexes: List[ReVal] = list()

        cardinal_ex = JapaneseCardinalExtractor(mode)
        self.__regexes.extend(cardinal_ex.regexes)

        fraction_ex = JapaneseFractionExtractor()
        self.__regexes.extend(fraction_ex.regexes)


class JapaneseCardinalExtractor(BaseNumberExtractor):
    @property
    def regexes(self) -> List[ReVal]:
        return self.__regexes

    @property
    def _extract_type(self) -> str:
        return Constants.SYS_NUM_CARDINAL

    def __init__(self, mode: JapaneseNumberExtractorMode = JapaneseNumberExtractorMode.DEFAULT):
        self.__regexes: List[ReVal] = list()

        integer_ex = JapaneseIntegerExtractor(mode)
        self.__regexes.extend(integer_ex.regexes)

        double_ex = JapaneseDoubleExtractor()
        self.__regexes.extend(double_ex.regexes)


class JapaneseIntegerExtractor(BaseNumberExtractor):
    @property
    def regexes(self) -> List[ReVal]:
        return self.__regexes

    @property
    def _extract_type(self) -> str:
        return Constants.SYS_NUM_INTEGER

    def __init__(self, mode: JapaneseNumberExtractorMode = JapaneseNumberExtractorMode.DEFAULT):
        self.__regexes = [
            # 123456,  －１２３４５６
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    JapaneseNumeric.NumbersSpecialsChars),
                val='IntegerNum'),
            # 15k,  16 G
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    JapaneseNumeric.NumbersSpecialsCharsWithSuffix),
                val='IntegerNum'),
            # 1,234,  ２，３３２，１１１
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    JapaneseNumeric.DottedNumbersSpecialsChar),
                val='IntegerNum'),
            # 半百  半ダース
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    JapaneseNumeric.NumbersWithHalfDozen),
                val='IntegerJpn'),
            # 一ダース  五十ダース
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    JapaneseNumeric.NumbersWithDozen),
                val='IntegerJpn')
        ]
        if mode == JapaneseNumberExtractorMode.DEFAULT:
            self.__regexes.append(
                # 一百五十五, 负一亿三百二十二. Uses an allow list to avoid extracting "西九条" from "九"
                ReVal(
                    re=RegExpUtility.get_safe_reg_exp(
                        JapaneseNumeric.NumbersWithAllowListRegex),
                    val='IntegerJpn'
                )
            )
        elif mode == JapaneseNumberExtractorMode.EXTRACT_ALL:
            self.__regexes.append(
                # 一百五十五, 负一亿三百二十二, "西九条" from "九". Uses no allow lists and extracts all potential integers (useful in Units, for example).
                ReVal(
                    re=RegExpUtility.get_safe_reg_exp(
                        JapaneseNumeric.NumbersAggressiveRegex),
                    val='IntegerJpn'
                )
            )


class JapaneseDoubleExtractor(BaseNumberExtractor):
    @property
    def regexes(self) -> List[ReVal]:
        return self.__regexes

    @property
    def _extract_type(self) -> str:
        return Constants.SYS_NUM_DOUBLE

    def __init__(self):
        self.__regexes = [
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    JapaneseNumeric.DoubleSpecialsChars),
                val='DoubleNum'),
            # (-)2.5, can avoid cases like ip address xx.xx.xx.xx
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    JapaneseNumeric.DoubleSpecialsCharsWithNegatives),
                val='DoubleNum'),
            # (-).2
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    JapaneseNumeric.SimpleDoubleSpecialsChars),
                val='DoubleNum'),
            # 1.0 K
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    JapaneseNumeric.DoubleWithMultiplierRegex),
                val='DoubleNum'),
            # １５.２万
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    JapaneseNumeric.DoubleWithThousandsRegex),
                val='DoubleJpn'),
            # 2e6, 21.2e0
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    JapaneseNumeric.DoubleExponentialNotationRegex),
                val='DoublePow'),
            # 2^5
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    JapaneseNumeric.DoubleScientificNotationRegex),
                val='DoublePow')
        ]


class JapaneseFractionExtractor(BaseNumberExtractor):
    @property
    def regexes(self) -> List[ReVal]:
        return self.__regexes

    @property
    def _extract_type(self) -> str:
        return Constants.SYS_NUM_FRACTION

    def __init__(self):
        self.__regexes = [
            # -4 5/2,  ４ ６／３
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    JapaneseNumeric.FractionNotationSpecialsCharsRegex),
                val='FracNum'),
            # 8/3
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    JapaneseNumeric.FractionNotationRegex),
                val='FracNum'),
            # 五分の二 七分の三
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    JapaneseNumeric.AllFractionNumber),
                val='FracJpn')
        ]


class JapaneseOrdinalExtractor(BaseNumberExtractor):
    @property
    def regexes(self) -> List[ReVal]:
        return self.__regexes

    @property
    def _extract_type(self) -> str:
        return Constants.SYS_NUM_ORDINAL

    def __init__(self):
        self.__regexes = [
            # だい一百五十四
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    JapaneseNumeric.AllOrdinalRegex),
                val='OrdinalJpn'),
            # だい２５６５
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    JapaneseNumeric.OrdinalNumbersRegex),
                val='OrdinalJpn'),
            # 2折 ２.５折
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    JapaneseNumeric.NumbersFoldsPercentageRegex),
                val='OrdinalJpn')
        ]
