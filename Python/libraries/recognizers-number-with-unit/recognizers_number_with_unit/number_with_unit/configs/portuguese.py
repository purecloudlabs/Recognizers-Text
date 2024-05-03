#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from typing import Dict, List, Pattern

from recognizers_number_with_unit.number_with_unit.constants import Constants
from recognizers_number_with_unit.number_with_unit.extractors import NumberWithUnitExtractorConfiguration
from recognizers_number_with_unit.resources.base_units import BaseUnits
from recognizers_text.utilities import DefinitionLoader, RegExpUtility
from recognizers_number.culture import CultureInfo
from recognizers_number.number.parser_factory import AgnosticNumberParserFactory, ParserType
from recognizers_number.number.portuguese.extractors import NumberMode, PortugueseNumberExtractor
from recognizers_number.number.portuguese.parsers import PortugueseNumberParserConfiguration
from recognizers_number_with_unit.number_with_unit.parsers import NumberWithUnitParserConfiguration
from recognizers_number_with_unit.resources.portuguese_numeric_with_unit import PortugueseNumericWithUnit
from recognizers_text.culture import Culture
from recognizers_text.extractor import Extractor
from recognizers_text.parser import Parser


class PortugueseNumberWithUnitExtractorConfiguration(NumberWithUnitExtractorConfiguration):

    ambiguity_filters_dict: Dict[Pattern, Pattern] = DefinitionLoader.load_ambiguity_filters(
        PortugueseNumericWithUnit.AmbiguityFiltersDict
    )
    unit_num_extractor: Extractor = PortugueseNumberExtractor(NumberMode.Unit)
    build_prefix: str = PortugueseNumericWithUnit.BuildPrefix
    build_suffix: str = PortugueseNumericWithUnit.BuildSuffix
    connector_token: str = PortugueseNumericWithUnit.ConnectorToken
    compound_unit_connector_regex: Pattern = RegExpUtility.get_safe_reg_exp(
        PortugueseNumericWithUnit.CompoundUnitConnectorRegex)
    non_unit_regex: Pattern = RegExpUtility.get_safe_reg_exp(BaseUnits.PmNonUnitRegex)
    ambiguous_unit_number_multiplier_regex: Pattern = None
    culture_info: CultureInfo = None

    def expand_half_suffix(self, source, result, numbers):
        pass

    def __init__(self, culture_info: CultureInfo):
        culture_info = culture_info or CultureInfo(Culture.Portuguese)
        super().__init__(culture_info)


class PortugueseCurrencyExtractorConfiguration(PortugueseNumberWithUnitExtractorConfiguration):

    extract_type: str = Constants.SYS_UNIT_CURRENCY
    suffix_list: Dict[str, str] = PortugueseNumericWithUnit.CurrencySuffixList
    prefix_list: Dict[str, str] = PortugueseNumericWithUnit.CurrencyPrefixList
    ambiguous_unit_list: List[str] = PortugueseNumericWithUnit.AmbiguousCurrencyUnitList
    culture_info: CultureInfo = None

    def __init__(self, culture_info: CultureInfo = None):
        super().__init__(culture_info)


class PortugueseNumberWithUnitParserConfiguration(NumberWithUnitParserConfiguration):

    internal_number_extractor: Extractor = PortugueseNumberExtractor(NumberMode.DEFAULT)
    connector_token: str = PortugueseNumericWithUnit.ConnectorToken

    def __init__(self, culture_info: CultureInfo):
        culture_info = culture_info or CultureInfo(Culture.Portuguese)
        super().__init__(culture_info)
        self.internal_number_parser: Parser = AgnosticNumberParserFactory.get_parser(
            ParserType.NUMBER, PortugueseNumberParserConfiguration(culture_info))


class PortugueseCurrencyParserConfiguration(PortugueseNumberWithUnitParserConfiguration):

    def __init__(self, culture_info: CultureInfo = None):
        super().__init__(culture_info)
        self.add_dict_to_unit_map(PortugueseNumericWithUnit.CurrencySuffixList)
        self.add_dict_to_unit_map(PortugueseNumericWithUnit.CurrencyPrefixList)
        self.currency_name_to_iso_code_map = PortugueseNumericWithUnit.CurrencyNameToIsoCodeMap
        self.currency_fraction_code_list = PortugueseNumericWithUnit.FractionalUnitNameToCodeMap
