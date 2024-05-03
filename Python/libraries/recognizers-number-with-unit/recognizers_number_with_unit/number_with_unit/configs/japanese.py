from typing import Dict, List, Pattern

from recognizers_number_with_unit.number_with_unit.constants import Constants
from recognizers_number_with_unit.number_with_unit.extractors import NumberWithUnitExtractorConfiguration
from recognizers_number_with_unit.number_with_unit.utilities import CommonUtils
from recognizers_number_with_unit.resources.base_units import BaseUnits
from recognizers_text.utilities import DefinitionLoader, RegExpUtility
from recognizers_number.culture import CultureInfo
from recognizers_number.number.japanese.extractors import JapaneseNumberExtractor, JapaneseNumberExtractorMode
from recognizers_number.number.japanese.parsers import JapaneseNumberParserConfiguration
from recognizers_number.number.parser_factory import AgnosticNumberParserFactory, ParserType
from recognizers_number_with_unit.number_with_unit.parsers import NumberWithUnitParserConfiguration
from recognizers_number_with_unit.resources.japanese_numeric_with_unit import JapaneseNumericWithUnit
from recognizers_text.culture import Culture
from recognizers_text.extractor import Extractor
from recognizers_text.parser import Parser


class JapaneseNumberWithUnitExtractorConfiguration(NumberWithUnitExtractorConfiguration):

    ambiguity_filters_dict: Dict[Pattern, Pattern] = DefinitionLoader.load_ambiguity_filters(
        JapaneseNumericWithUnit.AmbiguityFiltersDict
    )
    unit_num_extractor: Extractor = JapaneseNumberExtractor(JapaneseNumberExtractorMode.EXTRACT_ALL)
    build_prefix: str = JapaneseNumericWithUnit.BuildPrefix
    build_suffix: str = JapaneseNumericWithUnit.BuildSuffix
    connector_token: str = JapaneseNumericWithUnit.ConnectorToken
    compound_unit_connector_regex: Pattern = RegExpUtility.get_safe_reg_exp(
        JapaneseNumericWithUnit.CompoundUnitConnectorRegex)
    non_unit_regex: Pattern = RegExpUtility.get_safe_reg_exp(BaseUnits.PmNonUnitRegex)
    ambiguous_unit_number_multiplier_regex: Pattern = None
    culture_info: CultureInfo = None

    def expand_half_suffix(self, source, result, numbers):
        return CommonUtils.expand_half_suffix(source, result, numbers, self.half_unit_regex)

    def __init__(self, culture_info: CultureInfo):
        culture_info = culture_info or CultureInfo(Culture.Japanese)
        super().__init__(culture_info)
        self.half_unit_regex = RegExpUtility.get_safe_reg_exp(JapaneseNumericWithUnit.HalfUnitRegex)


class JapaneseCurrencyExtractorConfiguration(JapaneseNumberWithUnitExtractorConfiguration):

    extract_type: str = Constants.SYS_UNIT_CURRENCY
    suffix_list: Dict[str, str] = JapaneseNumericWithUnit.CurrencySuffixList
    prefix_list: Dict[str, str] = JapaneseNumericWithUnit.CurrencyPrefixList
    ambiguous_unit_list: List[str] = JapaneseNumericWithUnit.CurrencyAmbiguousValues
    culture_info: CultureInfo = None

    def __init__(self, culture_info: CultureInfo = None):
        super().__init__(culture_info)


class JapaneseNumberWithUnitParserConfiguration(NumberWithUnitParserConfiguration):

    internal_number_extractor: Extractor = JapaneseNumberExtractor(JapaneseNumberExtractorMode.EXTRACT_ALL)
    connector_token: str = JapaneseNumericWithUnit.ConnectorToken

    def __init__(self, culture_info: CultureInfo):
        culture_info = culture_info or CultureInfo(Culture.Japanese)
        super().__init__(culture_info)
        self.internal_number_parser: Parser = AgnosticNumberParserFactory.get_parser(
            ParserType.NUMBER, JapaneseNumberParserConfiguration(culture_info))


class JapaneseCurrencyParserConfiguration(JapaneseNumberWithUnitParserConfiguration):

    def __init__(self, culture_info: CultureInfo = None):
        super().__init__(culture_info)
        self.add_dict_to_unit_map(JapaneseNumericWithUnit.CurrencySuffixList)
        self.add_dict_to_unit_map(JapaneseNumericWithUnit.CurrencyPrefixList)
        self.currency_name_to_iso_code_map = JapaneseNumericWithUnit.CurrencyNameToIsoCodeMap
        self.currency_fraction_code_list = JapaneseNumericWithUnit.FractionalUnitNameToCodeMap

