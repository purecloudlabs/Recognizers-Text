from re import Pattern
from typing import List, Optional

import regex

from recognizers_text.utilities import RegExpUtility
from recognizers_number.number.extractors import ReVal, ReRe, BaseNumberExtractor, \
    BaseMergedNumberExtractor
from recognizers_number.number.models import NumberMode, LongFormatMode
from recognizers_number.number.number_options import NumberOptions
from recognizers_number.resources.arabic_numeric import ArabicNumeric
from recognizers_number.number.constants import Constants


class ArabicNumberExtractor(BaseNumberExtractor):
    extract_type: str = Constants.SYS_NUM

    @property
    def ambiguity_filters_dict(self) -> List[ReRe]:
        # Do not filter the ambiguous number cases like 'that one' in NumberWithUnit, otherwise they can't be resolved.
        _ambiguity_filters_dict: List[ReRe] = []

        if self.mode is not NumberMode.Unit:
            for key, value in ArabicNumeric.AmbiguityFiltersDict.items():
                _ambiguity_filters_dict.append(
                    ReRe(reKey=RegExpUtility.get_safe_reg_exp(key), reVal=RegExpUtility.get_safe_reg_exp(value))
                )
        return _ambiguity_filters_dict

    @property
    def ambiguous_fraction_connectors(self) -> Pattern:
        return RegExpUtility.get_safe_reg_exp(ArabicNumeric.AmbiguousFractionConnectorsRegex)

    @property
    def regexes(self) -> List[ReVal]:
        _regexes: List[ReVal] = []

        cardinal_ex: Optional[ArabicCardinalExtractor] = None
        if self.mode is NumberMode.PURE_NUMBER:
            cardinal_ex = ArabicCardinalExtractor(ArabicNumeric.PlaceHolderDefault)
        elif self.mode is NumberMode.CURRENCY:
            _regexes.append(
                ReVal(re=RegExpUtility.get_safe_reg_exp(ArabicNumeric.CurrencyRegex), val='IntegerNum'))

        cardinal_ex = cardinal_ex or ArabicCardinalExtractor()
        _regexes.extend(cardinal_ex.regexes)
        fraction_ex = ArabicFractionExtractor(self.mode)
        _regexes.extend(fraction_ex.regexes)
        return _regexes

    @property
    def relative_reference(self) -> Pattern:
        return RegExpUtility.get_safe_reg_exp(ArabicNumeric.RelativeOrdinalRegex)

    @property
    def _negative_number_terms(self) -> Pattern:
        return RegExpUtility.get_safe_reg_exp(ArabicNumeric.NegativeNumberTermsRegex)

    def __init__(self, mode: NumberMode = NumberMode.DEFAULT):
        self.mode = mode


class ArabicCardinalExtractor(BaseNumberExtractor):
    extract_type: str = Constants.SYS_NUM_CARDINAL

    @property
    def regexes(self) -> List[ReVal]:
        return (ArabicIntegerExtractor(self.placeholder).regexes +
                ArabicDoubleExtractor(self.placeholder).regexes)

    def __init__(self, placeholder: str = ArabicNumeric.PlaceHolderDefault):
        self.placeholder = placeholder


class ArabicIntegerExtractor(BaseNumberExtractor):
    extract_type: str = Constants.SYS_NUM_INTEGER

    @property
    def regexes(self) -> List[ReVal]:
        return [
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    ArabicNumeric.NumbersWithPlaceHolder(self.placeholder)
                ),
                val='IntegerNum'
            ),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    ArabicNumeric.NumbersWithSuffix, regex.S
                ),
                val='IntegerNum'
            ),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    ArabicNumeric.RoundNumberIntegerRegexWithLocks
                ),
                val='IntegerNum'
            ),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    ArabicNumeric.NumbersWithDozenSuffix
                ),
                val='IntegerNum'
            ),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    ArabicNumeric.AllIntRegexWithLocks
                ),
                val=f'Integer{ArabicNumeric.LangMarker}'
            ),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    ArabicNumeric.AllIntRegexWithDozenSuffixLocks
                ),
                val=f'Integer{ArabicNumeric.LangMarker}'
            ),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    self._generate_format_regex(LongFormatMode.INTEGER_COMMA, self.placeholder)
                ),
                val='IntegerNum'
            ),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    self._generate_format_regex(LongFormatMode.INTEGER_DOT, self.placeholder)
                ),
                val='IntegerNum'
            ),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    self._generate_format_regex(LongFormatMode.INTEGER_BLANK, self.placeholder)
                ),
                val='IntegerNum'
            ),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    self._generate_format_regex(LongFormatMode.INTEGER_NO_BREAK_SPACE, self.placeholder)
                ),
                val='IntegerNum'
            ),
        ]

    def __init__(self, placeholder: str = ArabicNumeric.PlaceHolderDefault):
        self.placeholder = placeholder


class ArabicDoubleExtractor(BaseNumberExtractor):
    extract_type: str = Constants.SYS_NUM_DOUBLE

    @property
    def regexes(self) -> List[ReVal]:
        return [
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    ArabicNumeric.DoubleDecimalPointRegex(self.placeholder)
                ),
                val='DoubleNum'
            ),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    ArabicNumeric.DoubleWithoutIntegralRegex(self.placeholder)
                ),
                val='DoubleNum'
            ),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    ArabicNumeric.DoubleWithMultiplierRegex
                ),
                val='DoubleNum'
            ),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    ArabicNumeric.DoubleWithRoundNumber
                ),
                val='DoubleNum'
            ),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    ArabicNumeric.DoubleAllFloatRegex
                ),
                val=f'Double{ArabicNumeric.LangMarker}'
            ),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    ArabicNumeric.DoubleExponentialNotationRegex
                ),
                val='DoubleNum'
            ),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    ArabicNumeric.DoubleCaretExponentialNotationRegex
                ),
                val='DoubleNum'
            ),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    self._generate_format_regex(LongFormatMode.DOUBLE_COMMA_DOT, self.placeholder)
                ),
                val='DoubleNum'
            ),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    self._generate_format_regex(LongFormatMode.DOUBLE_NUM_BLANK_DOT, self.placeholder)
                ),
                val='DoubleNum'
            ),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    self._generate_format_regex(LongFormatMode.DOUBLE_NO_BREAK_SPACE_DOT, self.placeholder)
                ),
                val='DoubleNum'
            ),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    ArabicNumeric.DoubleWithThousandMarkRegex(self.placeholder)
                ),
                val='DoubleNum'
            ),
        ]

    def __init__(self, placeholder: str):
        self.placeholder = placeholder


class ArabicFractionExtractor(BaseNumberExtractor):
    extract_type: str = Constants.SYS_NUM_FRACTION

    @property
    def regexes(self) -> List[ReVal]:
        _regexes = [
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(ArabicNumeric.FractionNotationWithSpacesRegex),
                val='FracNum'
            ),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(ArabicNumeric.FractionNotationWithSpacesRegex2),
                val='FracNum'
            ),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(ArabicNumeric.FractionNotationRegex),
                val='FracNum'
            ),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(ArabicNumeric.FractionNounRegex),
                val=f'Frac{ArabicNumeric.LangMarker}'
            ),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(ArabicNumeric.FractionNounWithArticleRegex),
                val=f'Frac{ArabicNumeric.LangMarker}'
            ),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(ArabicNumeric.FractionWithOrdinalPrefix),
                val=f'Frac{ArabicNumeric.LangMarker}'
            ),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(ArabicNumeric.FractionWithPartOfPrefix),
                val=f'Frac{ArabicNumeric.LangMarker}'
            )
        ]
        # Not add FractionPrepositionRegex when the mode is Unit to avoid wrong recognize cases like "$1000 over 3"
        if self.mode is not NumberMode.Unit:
            _regexes.append(
                ReVal(
                    re=RegExpUtility.get_safe_reg_exp(ArabicNumeric.FractionPrepositionRegex),
                    val=f'Frac{ArabicNumeric.LangMarker}'
                )
            )
        return _regexes

    def __init__(self, mode):
        self.mode = mode


class ArabicOrdinalExtractor(BaseNumberExtractor):
    extract_type: str = Constants.SYS_NUM_ORDINAL

    @property
    def ambiguous_fraction_connectors(self):
        return RegExpUtility.get_safe_reg_exp(ArabicNumeric.AmbiguousFractionConnectorsRegex)

    @property
    def regexes(self) -> List[ReVal]:
        return [
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(ArabicNumeric.OrdinalNumericRegex),
                val='OrdinalNum'
            ),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(ArabicNumeric.OrdinalEnglishRegex),
                val=f'Ordinal{ArabicNumeric.LangMarker}'
            ),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(ArabicNumeric.OrdinalRoundNumberRegex),
                val=f'Ordinal{ArabicNumeric.LangMarker}'
            ),
        ]

    @property
    def relative_reference(self):
        return RegExpUtility.get_safe_reg_exp(ArabicNumeric.RelativeOrdinalRegex)


class ArabicMergedNumberExtractor(BaseMergedNumberExtractor):

    @property
    def _round_number_integer_regex_with_locks(self) -> Pattern:
        return RegExpUtility.get_safe_reg_exp(ArabicNumeric.RoundNumberIntegerRegexWithLocks)

    @property
    def _connector_regex(self) -> Pattern:
        return RegExpUtility.get_safe_reg_exp(ArabicNumeric.ConnectorRegex)

    def __init__(self, mode: NumberMode = NumberMode.DEFAULT):
        self._number_extractor = ArabicNumberExtractor(mode)
