from typing import Dict, List, Pattern

from recognizers_number.culture import CultureInfo
from recognizers_number.number.german.extractors import GermanNumberExtractor, NumberMode
from recognizers_number.number.german.parsers import GermanNumberParserConfiguration
from recognizers_number.number.parser_factory import AgnosticNumberParserFactory, ParserType
from recognizers_number_with_unit.number_with_unit.constants import Constants
from recognizers_number_with_unit.number_with_unit.extractors import NumberWithUnitExtractorConfiguration
from recognizers_number_with_unit.number_with_unit.parsers import NumberWithUnitParserConfiguration
from recognizers_number_with_unit.resources.base_units import BaseUnits
from recognizers_number_with_unit.resources.german_numeric_with_unit import GermanNumericWithUnit
from recognizers_text.culture import Culture
from recognizers_text.extractor import Extractor
from recognizers_text.parser import Parser
from recognizers_text.utilities import DefinitionLoader, RegExpUtility


class GermanNumberWithUnitExtractorConfiguration(NumberWithUnitExtractorConfiguration):

    ambiguity_filters_dict: Dict[Pattern, Pattern] = DefinitionLoader.load_ambiguity_filters(
        GermanNumericWithUnit.AmbiguityFiltersDict
    )
    unit_num_extractor: Extractor = GermanNumberExtractor(NumberMode.Unit)
    build_prefix: str = GermanNumericWithUnit.BuildPrefix
    build_suffix: str = GermanNumericWithUnit.BuildSuffix
    connector_token: str = GermanNumericWithUnit.ConnectorToken
    compound_unit_connector_regex: Pattern = RegExpUtility.get_safe_reg_exp(
        GermanNumericWithUnit.CompoundUnitConnectorRegex
    )
    non_unit_regex: Pattern = RegExpUtility.get_safe_reg_exp(BaseUnits.PmNonUnitRegex)
    ambiguous_unit_number_multiplier_regex: Pattern = None
    culture_info: CultureInfo = None

    def expand_half_suffix(self, source, result, numbers):
        pass

    def __init__(self, culture_info: CultureInfo):
        culture_info = culture_info or CultureInfo(Culture.German)
        super().__init__(culture_info)


class GermanCurrencyExtractorConfiguration(GermanNumberWithUnitExtractorConfiguration):

    extract_type: str = Constants.SYS_UNIT_CURRENCY
    suffix_list: Dict[str, str] = GermanNumericWithUnit.CurrencySuffixList
    prefix_list: Dict[str, str] = GermanNumericWithUnit.CurrencyPrefixList
    ambiguous_unit_list: List[str] = GermanNumericWithUnit.AmbiguousCurrencyUnitList
    culture_info: CultureInfo = None

    def __init__(self, culture_info: CultureInfo = None):
        super().__init__(culture_info)


class GermanNumberWithUnitParserConfiguration(NumberWithUnitParserConfiguration):

    internal_number_extractor: Extractor = GermanNumberExtractor(NumberMode.DEFAULT)
    connector_token: str = GermanNumericWithUnit.ConnectorToken

    def __init__(self, culture_info: CultureInfo):
        culture_info = culture_info or CultureInfo(Culture.German)
        super().__init__(culture_info)
        self.internal_number_parser: Parser = AgnosticNumberParserFactory.get_parser(
            ParserType.NUMBER, GermanNumberParserConfiguration(culture_info)
        )


class GermanCurrencyParserConfiguration(GermanNumberWithUnitParserConfiguration):

    def __init__(self, culture_info: CultureInfo = None):
        super().__init__(culture_info)
        self.add_dict_to_unit_map(GermanNumericWithUnit.CurrencySuffixList)
        self.add_dict_to_unit_map(GermanNumericWithUnit.CurrencyPrefixList)
        self.currency_name_to_iso_code_map = GermanNumericWithUnit.CurrencyNameToIsoCodeMap
        self.currency_fraction_code_list = GermanNumericWithUnit.FractionalUnitNameToCodeMap
