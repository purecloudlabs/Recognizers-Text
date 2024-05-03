from typing import List

from recognizers_text.utilities import RegExpUtility
from recognizers_number.number.models import NumberMode, LongFormatMode
from recognizers_number.resources.catalan_numeric import CatalanNumeric
from recognizers_number.number.extractors import ReVal, ReRe, BaseNumberExtractor
from recognizers_number.number.constants import Constants


class CatalanNumberExtractor(BaseNumberExtractor):
    extract_type: str = Constants.SYS_NUM

    @property
    def regexes(self) -> List[ReVal]:
        _regexes: List[ReVal] = []
        cardinal_ex: CatalanCardinalExtractor = None

        if self.mode is NumberMode.PURE_NUMBER:
            cardinal_ex = CatalanCardinalExtractor(
                CatalanNumeric.PlaceHolderPureNumber)
        elif self.mode is NumberMode.CURRENCY:
            _regexes.append(
                ReVal(re=CatalanNumeric.CurrencyRegex, val='IntegerNum'))

        cardinal_ex = cardinal_ex or CatalanCardinalExtractor()
        _regexes.extend(cardinal_ex.regexes)

        fraction_ex = CatalanFractionExtractor(self.mode)
        _regexes.extend(fraction_ex.regexes)
        return _regexes

    @property
    def ambiguity_filters_dict(self) -> List[ReRe]:
        _ambiguity_filters_dict: List[ReRe] = []

        if self.mode != NumberMode.Unit:
            for key, value in CatalanNumeric.AmbiguityFiltersDict.items():
                _ambiguity_filters_dict.append(ReRe(reKey=RegExpUtility.get_safe_reg_exp(key),
                                                   reVal=RegExpUtility.get_safe_reg_exp(value)))
        return _ambiguity_filters_dict

    def __init__(self, mode: NumberMode = NumberMode.DEFAULT):
        self.mode = mode


class CatalanCardinalExtractor(BaseNumberExtractor):
    extract_type: str = Constants.SYS_NUM_CARDINAL

    @property
    def regexes(self) -> List[ReVal]:
        return (CatalanIntegerExtractor(self.placeholder).regexes +
                CatalanDoubleExtractor(self.placeholder).regexes)

    def __init__(self, placeholder: str = CatalanNumeric.PlaceHolderDefault):
        self.placeholder = placeholder


class CatalanIntegerExtractor(BaseNumberExtractor):
    extract_type: str = Constants.SYS_NUM_INTEGER

    @property
    def regexes(self) -> List[ReVal]:
        return [
            ReVal(
                re=CatalanNumeric.NumbersWithPlaceHolder(self.placeholder),
                val='IntegerNum'),
            ReVal(
                re=CatalanNumeric.NumbersWithSuffix,
                val='IntegerNum'),
            ReVal(
                re=self._generate_format_regex(LongFormatMode.INTEGER_DOT,
                                               self.placeholder),
                val='IntegerNum'),
            ReVal(
                re=self._generate_format_regex(LongFormatMode.INTEGER_BLANK,
                                               self.placeholder),
                val='IntegerNum'),
            ReVal(
                re=self._generate_format_regex(
                    LongFormatMode.INTEGER_NO_BREAK_SPACE, self.placeholder),
                val='IntegerNum'),
            ReVal(
                re=CatalanNumeric.RoundNumberIntegerRegexWithLocks,
                val='IntegerNum'),
            ReVal(
                re=CatalanNumeric.NumbersWithDozenSuffix,
                val='IntegerNum'),
            ReVal(
                re=CatalanNumeric.AllIntRegexWithLocks,
                val='IntegerCat'),
        ]

    def __init__(self, placeholder: str = CatalanNumeric.PlaceHolderDefault):
        self.placeholder = placeholder


class CatalanDoubleExtractor(BaseNumberExtractor):
    extract_type: str = Constants.SYS_NUM_DOUBLE

    @property
    def regexes(self) -> List[ReVal]:
        return [
            ReVal(
                re=CatalanNumeric.DoubleDecimalPointRegex(self.placeholder),
                val='DoubleNum'),
            ReVal(
                re=CatalanNumeric.DoubleWithoutIntegralRegex(self.placeholder),
                val='DoubleNum'),
            ReVal(
                re=CatalanNumeric.DoubleWithMultiplierRegex,
                val='DoubleNum'),
            ReVal(
                re=CatalanNumeric.DoubleWithRoundNumber,
                val='DoubleNum'),
            ReVal(
                re=CatalanNumeric.DoubleAllFloatRegex,
                val='DoubleCat'),
            ReVal(
                re=CatalanNumeric.DoubleExponentialNotationRegex,
                val='DoublePow'),
            ReVal(
                re=CatalanNumeric.DoubleCaretExponentialNotationRegex,
                val='DoublePow'),
            ReVal(
                re=self._generate_format_regex(LongFormatMode.DOUBLE_DOT_COMMA,
                                               self.placeholder),
                val='DoubleNum'),
            ReVal(
                re=self._generate_format_regex(
                    LongFormatMode.DOUBLE_NO_BREAK_SPACE_COMMA,
                    self.placeholder),
                val='DoubleNum')
        ]

    def __init__(self, placeholder: str = CatalanNumeric.PlaceHolderDefault):
        self.placeholder = placeholder


class CatalanFractionExtractor(BaseNumberExtractor):
    extract_type: str = Constants.SYS_NUM_FRACTION

    @property
    def regexes(self) -> List[ReVal]:
        _regexes = [
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    CatalanNumeric.FractionNotationWithSpacesRegex),
                val='FracNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    CatalanNumeric.FractionNotationRegex),
                val='FracNum'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    CatalanNumeric.FractionNounRegex),
                val=f'Frac{CatalanNumeric.LangMarker}'),
            ReVal(
                re=RegExpUtility.get_safe_reg_exp(
                    CatalanNumeric.FractionNounWithArticleRegex),
                val=f'Frac{CatalanNumeric.LangMarker}')
        ]

        if self.mode != NumberMode.Unit:
            _regexes.append(
                ReVal(
                    re=RegExpUtility.get_safe_reg_exp(
                        CatalanNumeric.FractionPrepositionRegex),
                    val=f'Frac{CatalanNumeric.LangMarker}'))
        return _regexes

    def __init__(self, mode):
        self.mode = mode


class CatalanOrdinalExtractor(BaseNumberExtractor):
    extract_type: str = Constants.SYS_NUM_ORDINAL

    @property
    def regexes(self) -> List[ReVal]:
        return [
            ReVal(
                re=CatalanNumeric.OrdinalSuffixRegex,
                val='OrdinalNum'),
            ReVal(
                re=CatalanNumeric.SuffixRoundNumberOrdinalRegex,
                val='OrdCat')
        ]
