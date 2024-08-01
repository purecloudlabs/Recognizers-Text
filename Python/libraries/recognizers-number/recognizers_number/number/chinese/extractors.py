#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from enum import Enum
from typing import List

from recognizers_number.number.constants import Constants
from recognizers_number.number.extractors import BaseNumberExtractor, ReRe, ReVal
from recognizers_number.number.models import NumberMode
from recognizers_number.resources.chinese_numeric import ChineseNumeric
from recognizers_text.utilities import RegExpUtility


class ChineseNumberExtractorMode(Enum):
    DEFAULT = 0
    EXTRACT_ALL = 1


class ChineseNumberExtractor(BaseNumberExtractor):
    extract_type: str = Constants.SYS_NUM

    @property
    def regexes(self) -> List[ReVal]:
        return ChineseCardinalExtractor(self.mode).regexes + ChineseFractionExtractor().regexes

    @property
    def ambiguity_filters_dict(self):
        _ambiguity_filters_dict: List[ReRe] = []
        if self.mode != NumberMode.Unit:
            for key, value in ChineseNumeric.AmbiguityFiltersDict.items():
                _ambiguity_filters_dict.append(
                    ReRe(reKey=RegExpUtility.get_safe_reg_exp(key), reVal=RegExpUtility.get_safe_reg_exp(value))
                )
        return _ambiguity_filters_dict

    def __init__(self, mode: ChineseNumberExtractorMode = ChineseNumberExtractorMode.DEFAULT):
        self.mode = mode


class ChineseCardinalExtractor(BaseNumberExtractor):
    extract_type: str = Constants.SYS_NUM_CARDINAL

    @property
    def regexes(self) -> List[ReVal]:
        return ChineseIntegerExtractor(self.mode).regexes + ChineseDoubleExtractor().regexes

    def __init__(self, mode: ChineseNumberExtractorMode = ChineseNumberExtractorMode.DEFAULT):
        self.mode = mode


class ChineseIntegerExtractor(BaseNumberExtractor):
    extract_type: str = Constants.SYS_NUM_INTEGER

    @property
    def regexes(self) -> List[ReVal]:
        _regexes = [
            ReVal(re=RegExpUtility.get_safe_reg_exp(ChineseNumeric.NumbersSpecialsChars), val='IntegerNum'),
            ReVal(re=RegExpUtility.get_safe_reg_exp(ChineseNumeric.NumbersSpecialsCharsWithSuffix), val='IntegerNum'),
            ReVal(re=RegExpUtility.get_safe_reg_exp(ChineseNumeric.DottedNumbersSpecialsChar), val='IntegerNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(ChineseNumeric.NumbersWithHalfDozen),
                val=f'Integer{ChineseNumeric.LangMarker}',
            ),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(ChineseNumeric.NumbersWithDozen),
                val=f'Integer{ChineseNumeric.LangMarker}',
            ),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(ChineseNumeric.HalfUnitRegex),
                val=f'Integer{ChineseNumeric.LangMarker}',
            ),
        ]
        if self.mode == ChineseNumberExtractorMode.DEFAULT:
            _regexes.append(
                ReVal(
                    re=RegExpUtility.get_safe_reg_exp(ChineseNumeric.NumbersWithAllowListRegex),
                    val=f'Integer{ChineseNumeric.LangMarker}',
                )
            )
        elif self.mode == ChineseNumberExtractorMode.EXTRACT_ALL:
            _regexes.append(
                ReVal(
                    re=RegExpUtility.get_safe_reg_exp(ChineseNumeric.NumbersAggressiveRegex),
                    val=f'Integer{ChineseNumeric.LangMarker}',
                )
            )
        return _regexes

    def __init__(self, mode: ChineseNumberExtractorMode = ChineseNumberExtractorMode.DEFAULT):
        self.mode = mode


class ChineseDoubleExtractor(BaseNumberExtractor):
    extract_type: str = Constants.SYS_NUM_DOUBLE

    @property
    def regexes(self) -> List[ReVal]:
        return [
            ReVal(re=RegExpUtility.get_safe_reg_exp(ChineseNumeric.DoubleSpecialsChars), val='DoubleNum'),
            ReVal(re=RegExpUtility.get_safe_reg_exp(ChineseNumeric.DoubleSpecialsCharsWithNegatives), val='DoubleNum'),
            ReVal(re=RegExpUtility.get_safe_reg_exp(ChineseNumeric.SimpleDoubleSpecialsChars), val='DoubleNum'),
            ReVal(re=RegExpUtility.get_safe_reg_exp(ChineseNumeric.DoubleWithMultiplierRegex), val='DoubleNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(ChineseNumeric.DoubleWithThousandsRegex),
                val=f'Double{ChineseNumeric.LangMarker}',
            ),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(ChineseNumeric.DoubleAllFloatRegex),
                val=f'Double{ChineseNumeric.LangMarker}',
            ),
            ReVal(re=RegExpUtility.get_safe_reg_exp(ChineseNumeric.DoubleExponentialNotationRegex), val='DoublePow'),
            ReVal(re=RegExpUtility.get_safe_reg_exp(ChineseNumeric.DoubleScientificNotationRegex), val='DoublePow'),
        ]


class ChineseFractionExtractor(BaseNumberExtractor):
    extract_type: str = Constants.SYS_NUM_FRACTION

    @property
    def regexes(self) -> List[ReVal]:
        return [
            ReVal(re=RegExpUtility.get_safe_reg_exp(ChineseNumeric.FractionNotationSpecialsCharsRegex), val='FracNum'),
            ReVal(re=RegExpUtility.get_safe_reg_exp(ChineseNumeric.FractionNotationRegex), val='FracNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(ChineseNumeric.AllFractionNumber),
                val=f'Frac{ChineseNumeric.LangMarker}',
            ),
        ]


class ChineseOrdinalExtractor(BaseNumberExtractor):
    extract_type: str = Constants.SYS_NUM_ORDINAL

    @property
    def regexes(self) -> List[ReVal]:
        return [
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(ChineseNumeric.OrdinalRegex),
                val=f'Ordinal{ChineseNumeric.LangMarker}',
            ),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(ChineseNumeric.OrdinalNumbersRegex),
                val=f'Ordinal{ChineseNumeric.LangMarker}',
            ),
        ]
