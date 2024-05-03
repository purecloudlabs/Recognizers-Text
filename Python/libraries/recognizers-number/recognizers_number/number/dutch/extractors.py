from typing import List, Optional, Pattern

import regex

from recognizers_number.number.constants import Constants
from recognizers_number.number.extractors import BaseMergedNumberExtractor, BaseNumberExtractor, ReRe, ReVal
from recognizers_number.number.models import LongFormatMode, NumberMode
from recognizers_number.resources.dutch_numeric import DutchNumeric
from recognizers_text.utilities import RegExpUtility


class DutchNumberExtractor(BaseNumberExtractor):
    extract_type: str = Constants.SYS_NUM

    @property
    def regexes(self) -> List[ReVal]:
        _regexes: List[ReVal] = list()
        cardinal_ex: Optional[DutchCardinalExtractor] = None

        if self.mode is NumberMode.PURE_NUMBER:
            cardinal_ex = DutchCardinalExtractor(
                DutchNumeric.PlaceHolderPureNumber)
        elif self.mode is NumberMode.CURRENCY:
            _regexes.append(ReVal(re=RegExpUtility.get_safe_reg_exp(
                DutchNumeric.CurrencyRegex), val='IntegerNum'))

        cardinal_ex = cardinal_ex or DutchCardinalExtractor()
        _regexes.extend(cardinal_ex.regexes)

        fraction_ex = DutchFractionExtractor(self.mode)
        _regexes.extend(fraction_ex.regexes)
        return _regexes

    @property
    def ambiguity_filters_dict(self) -> List[ReRe]:
        _ambiguity_filters_dict: List[ReRe] = []

        if self.mode != NumberMode.Unit:
            for key, value in DutchNumeric.AmbiguityFiltersDict.items():
                _ambiguity_filters_dict.append(ReRe(reKey=RegExpUtility.get_safe_reg_exp(key),
                                                    reVal=RegExpUtility.get_safe_reg_exp(value)))
        return _ambiguity_filters_dict

    @property
    def _negative_number_terms(self) -> Pattern:
        return RegExpUtility.get_safe_reg_exp(DutchNumeric.NegativeNumberTermsRegex)

    def __init__(self, mode: NumberMode = NumberMode.DEFAULT):
        self.mode = mode


class DutchCardinalExtractor(BaseNumberExtractor):
    extract_type: str = Constants.SYS_NUM_CARDINAL

    @property
    def regexes(self) -> List[ReVal]:
        return (DutchIntegerExtractor(self.placeholder).regexes +
                DutchDoubleExtractor(self.placeholder).regexes)

    def __init__(self, placeholder: str = DutchNumeric.PlaceHolderDefault):
        self.placeholder = placeholder


class DutchIntegerExtractor(BaseNumberExtractor):
    extract_type: str = Constants.SYS_NUM_INTEGER

    @property
    def regexes(self) -> List[ReVal]:
        return [
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    DutchNumeric.NumbersWithPlaceHolder(self.placeholder)),
                val='IntegerNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    DutchNumeric.NumbersWithSuffix, regex.S),
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
                    DutchNumeric.RoundNumberIntegerRegexWithLocks),
                val='IntegerNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    DutchNumeric.NumbersWithDozenSuffix),
                val='IntegerNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    DutchNumeric.AllIntRegexWithLocks),
                val='IntegerDut'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    DutchNumeric.AllIntRegexWithDozenSuffixLocks),
                val='IntegerDut')
        ]

    def __init__(self, placeholder: str = DutchNumeric.PlaceHolderDefault):
        self.placeholder = placeholder


class DutchDoubleExtractor(BaseNumberExtractor):
    extract_type: str = Constants.SYS_NUM_DOUBLE

    @property
    def regexes(self) -> List[ReVal]:
        return [
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    DutchNumeric.DoubleDecimalPointRegex(self.placeholder)),
                val='DoubleNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    DutchNumeric.DoubleWithoutIntegralRegex(self.placeholder)),
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
                re=RegExpUtility.get_safe_reg_exp(self._generate_format_regex(
                    LongFormatMode.DOUBLE_NUM_BLANK_COMMA, self.placeholder)),
                val='DoubleNum'),
            ReVal(
                re=DutchNumeric.DoubleWithMultiplierRegex,
                val='DoubleNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    DutchNumeric.DoubleWithRoundNumber),
                val='DoubleNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    DutchNumeric.DoubleAllFloatRegex),
                val=f'Double{DutchNumeric.LangMarker}'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    DutchNumeric.DoubleExponentialNotationRegex),
                val='DoublePow'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    DutchNumeric.DoubleCaretExponentialNotationRegex),
                val='DoublePow')
        ]

    def __init__(self, placeholder):
        self.placeholder = placeholder


class DutchFractionExtractor(BaseNumberExtractor):
    extract_type: str = Constants.SYS_NUM_FRACTION

    @property
    def regexes(self) -> List[ReVal]:
        _regexes = [
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    DutchNumeric.FractionNotationWithSpacesRegex),
                val='FracNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    DutchNumeric.FractionNotationRegex),
                val='FracNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    DutchNumeric.FractionNounRegex),
                val=f'Frac{DutchNumeric.LangMarker}'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    DutchNumeric.FractionNounWithArticleRegex),
                val=f'Frac{DutchNumeric.LangMarker}')
        ]
        if self.mode != NumberMode.Unit:
            _regexes.append(
                ReVal(
                    re=RegExpUtility.get_safe_reg_exp(
                        DutchNumeric.FractionPrepositionRegex),
                    val=f'Frac{DutchNumeric.LangMarker}'))
        return _regexes

    def __init__(self, mode):
        self.mode = mode


class DutchOrdinalExtractor(BaseNumberExtractor):
    extract_type: str = Constants.SYS_NUM_ORDINAL

    @property
    def regexes(self) -> List[ReVal]:
        return [
            ReVal(
                re=DutchNumeric.OrdinalSuffixRegex,
                val='OrdinalNum'),
            ReVal(
                re=DutchNumeric.OrdinalNumericRegex,
                val='OrdinalNum'),
            ReVal(
                re=DutchNumeric.OrdinalDutchRegex,
                val='OrdDut'),
            ReVal(
                re=DutchNumeric.OrdinalRoundNumberRegex,
                val='OrdDut')
        ]


class DutchMergedNumberExtractor(BaseMergedNumberExtractor):

    @property
    def _round_number_integer_regex_with_locks(self) -> Pattern:
        return RegExpUtility.get_safe_reg_exp(DutchNumeric.RoundNumberIntegerRegexWithLocks)

    @property
    def _connector_regex(self) -> Pattern:
        return RegExpUtility.get_safe_reg_exp(DutchNumeric.ConnectorRegex)

    def __init__(self, mode: NumberMode = NumberMode.DEFAULT):
        self._number_extractor = DutchNumberExtractor(mode)
