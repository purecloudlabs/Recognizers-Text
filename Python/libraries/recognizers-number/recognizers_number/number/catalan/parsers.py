from typing import Dict, List, Optional, Pattern

from recognizers_number.culture import CultureInfo
from recognizers_number.number.parsers import BaseNumberParserConfiguration
from recognizers_number.resources.catalan_numeric import CatalanNumeric
from recognizers_text.culture import Culture
from recognizers_text.parser import ParseResult
from recognizers_text.utilities import RegExpUtility


class CatalanNumberParserConfiguration(BaseNumberParserConfiguration):

    lang_marker: str = CatalanNumeric.LangMarker
    is_multi_decimal_separator_culture: bool = CatalanNumeric.MultiDecimalSeparatorCulture

    decimal_separator_char: str = CatalanNumeric.DecimalSeparatorChar
    fraction_marker_token: str = CatalanNumeric.FractionMarkerToken
    non_decimal_separator_char: str = CatalanNumeric.NonDecimalSeparatorChar
    half_a_dozen_text: str = CatalanNumeric.HalfADozenText
    word_separator_token: str = CatalanNumeric.WordSeparatorToken

    written_decimal_separator_texts: List[str] = CatalanNumeric.WrittenDecimalSeparatorTexts
    written_group_separator_texts: List[str] = CatalanNumeric.WrittenGroupSeparatorTexts
    written_integer_separator_texts: List[str] = CatalanNumeric.WrittenIntegerSeparatorTexts
    written_fraction_separator_texts: List[str] = CatalanNumeric.WrittenFractionSeparatorTexts
    non_standard_separator_variants: List[str] = CatalanNumeric.NonStandardSeparatorVariants

    ordinal_number_map: Dict[str, int] = CatalanNumeric.OrdinalNumberMap
    cardinal_number_map: Dict[str, int] = CatalanNumeric.CardinalNumberMap
    round_number_map: Dict[str, int] = CatalanNumeric.RoundNumberMap

    negative_number_sign_regex: Pattern = RegExpUtility.get_safe_reg_exp(CatalanNumeric.NegativeNumberSignRegex)
    half_a_dozen_regex: Pattern = RegExpUtility.get_safe_reg_exp(CatalanNumeric.HalfADozenRegex)
    digital_number_regex: Pattern = RegExpUtility.get_safe_reg_exp(CatalanNumeric.DigitalNumberRegex)
    round_multiplier_regex: Pattern = RegExpUtility.get_safe_reg_exp(CatalanNumeric.RoundMultiplierRegex)

    def __init__(self, culture_info: Optional[CultureInfo] = None):
        culture_info = culture_info or CultureInfo(Culture.Catalan)
        super().__init__(culture_info)

    def normalize_token_set(self, tokens: List[str], context: ParseResult) -> List[str]:
        frac_words: List[str] = super().normalize_token_set(tokens, context)

        # The following piece of code is needed to compute the fraction pattern number+'i mig' and 'un quart de'
        # e.g. 'dos i mig' ('two and a half') where the numerator is omitted in Catalan and 'un quart de milió'
        # It works by inserting the numerator 'un' ('a') in the catalan numbers regex
        # so that the pattern is correctly processed.
        if len(frac_words) >= 2:
            if (
                frac_words[-1] in CatalanNumeric.FractionalTokens
                and frac_words[-2] == CatalanNumeric.WordSeparatorToken
            ):
                frac_words.insert(-1, CatalanNumeric.FractionWithoutNumeratorToken)
            elif (
                frac_words[-1] in CatalanNumeric.WrittenFractionSeparatorTexts
                and frac_words[-2] in CatalanNumeric.FractionalTokens
            ):
                frac_words.pop(-1)
        return frac_words
