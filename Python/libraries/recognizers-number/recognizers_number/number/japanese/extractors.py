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
    extract_type: str = Constants.SYS_NUM

    @property
    def regexes(self) -> List[ReVal]:
        return (JapaneseCardinalExtractor(self.mode).regexes +
                JapaneseFractionExtractor().regexes)

    def __init__(self, mode: JapaneseNumberExtractorMode = JapaneseNumberExtractorMode.DEFAULT):
        self.mode = mode


class JapaneseCardinalExtractor(BaseNumberExtractor):
    extract_type: str = Constants.SYS_NUM_CARDINAL

    @property
    def regexes(self) -> List[ReVal]:
        return (JapaneseIntegerExtractor(self.mode).regexes +
                JapaneseDoubleExtractor().regexes)

    def __init__(self, mode: JapaneseNumberExtractorMode = JapaneseNumberExtractorMode.DEFAULT):
        self.mode = mode


class JapaneseIntegerExtractor(BaseNumberExtractor):
    extract_type: str = Constants.SYS_NUM_INTEGER

    @property
    def regexes(self) -> List[ReVal]:
        _regexes = [
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
        if self.mode == JapaneseNumberExtractorMode.DEFAULT:
            _regexes.append(
                # 一百五十五, 负一亿三百二十二. Uses an allow list to avoid extracting "西九条" from "九"
                ReVal(
                    re=RegExpUtility.get_safe_reg_exp(
                        JapaneseNumeric.NumbersWithAllowListRegex),
                    val='IntegerJpn'
                )
            )
        elif self.mode == JapaneseNumberExtractorMode.EXTRACT_ALL:
            _regexes.append(
                # 一百五十五, 负一亿三百二十二, "西九条" from "九". Uses no allow lists and extracts all potential integers (useful in Units, for example).
                ReVal(
                    re=RegExpUtility.get_safe_reg_exp(
                        JapaneseNumeric.NumbersAggressiveRegex),
                    val='IntegerJpn'
                )
            )
        return _regexes

    def __init__(self, mode: JapaneseNumberExtractorMode = JapaneseNumberExtractorMode.DEFAULT):
        self.mode = mode


class JapaneseDoubleExtractor(BaseNumberExtractor):
    extract_type: str = Constants.SYS_NUM_DOUBLE

    @property
    def regexes(self) -> List[ReVal]:
        return [
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
    extract_type: str = Constants.SYS_NUM_FRACTION

    @property
    def regexes(self) -> List[ReVal]:
        return [
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
    extract_type: str = Constants.SYS_NUM_ORDINAL

    @property
    def regexes(self) -> List[ReVal]:
        return [
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
