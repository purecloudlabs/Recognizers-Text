#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from typing import Dict, List, Pattern

from recognizers_number.culture import CultureInfo
from recognizers_number.number.dutch.extractors import DutchNumberExtractor, NumberMode
from recognizers_number.number.dutch.parsers import DutchNumberParserConfiguration
from recognizers_number.number.parser_factory import AgnosticNumberParserFactory, ParserType
from recognizers_number_with_unit.number_with_unit.constants import Constants
from recognizers_number_with_unit.number_with_unit.extractors import NumberWithUnitExtractorConfiguration
from recognizers_number_with_unit.number_with_unit.parsers import NumberWithUnitParserConfiguration
from recognizers_number_with_unit.resources.base_units import BaseUnits
from recognizers_number_with_unit.resources.dutch_numeric_with_unit import DutchNumericWithUnit
from recognizers_text import Culture
from recognizers_text.extractor import Extractor
from recognizers_text.parser import Parser
from recognizers_text.utilities import DefinitionLoader, RegExpUtility


class DutchNumberWithUnitExtractorConfiguration(NumberWithUnitExtractorConfiguration):

    ambiguity_filters_dict: Dict[Pattern, Pattern] = DefinitionLoader.load_ambiguity_filters(
        DutchNumericWithUnit.AmbiguityFiltersDict
    )
    unit_num_extractor: Extractor = DutchNumberExtractor(NumberMode.Unit)
    build_prefix: str = DutchNumericWithUnit.BuildPrefix
    build_suffix: str = DutchNumericWithUnit.BuildSuffix
    connector_token: str = ''
    compound_unit_connector_regex: Pattern = RegExpUtility.get_safe_reg_exp(
        DutchNumericWithUnit.CompoundUnitConnectorRegex
    )
    non_unit_regex: Pattern = RegExpUtility.get_safe_reg_exp(BaseUnits.PmNonUnitRegex)
    ambiguous_unit_number_multiplier_regex: Pattern = None
    culture_info: CultureInfo = None

    def expand_half_suffix(self, source, result, numbers):
        pass

    def __init__(self, culture_info: CultureInfo):
        culture_info = culture_info or CultureInfo(Culture.Dutch)
        super().__init__(culture_info)


class DutchCurrencyExtractorConfiguration(DutchNumberWithUnitExtractorConfiguration):

    extract_type: str = Constants.SYS_UNIT_CURRENCY
    suffix_list: Dict[str, str] = DutchNumericWithUnit.CurrencySuffixList
    prefix_list: Dict[str, str] = DutchNumericWithUnit.CurrencyPrefixList
    ambiguous_unit_list: List[str] = DutchNumericWithUnit.AmbiguousCurrencyUnitList
    culture_info: CultureInfo = None

    def __init__(self, culture_info: CultureInfo = None):
        super().__init__(culture_info)


class DutchNumberWithUnitParserConfiguration(NumberWithUnitParserConfiguration):

    internal_number_extractor: Extractor = DutchNumberExtractor(NumberMode.DEFAULT)
    connector_token: str = ''

    def __init__(self, culture_info: CultureInfo):
        culture_info = culture_info or CultureInfo(Culture.Dutch)
        super().__init__(culture_info)
        self.internal_number_parser: Parser = AgnosticNumberParserFactory.get_parser(
            ParserType.NUMBER, DutchNumberParserConfiguration(culture_info)
        )


class DutchCurrencyParserConfiguration(DutchNumberWithUnitParserConfiguration):

    def __init__(self, culture_info: CultureInfo = None):
        super().__init__(culture_info)
        self.add_dict_to_unit_map(DutchNumericWithUnit.CurrencySuffixList)
        self.add_dict_to_unit_map(DutchNumericWithUnit.CurrencyPrefixList)
        self.currency_name_to_iso_code_map = DutchNumericWithUnit.CurrencyNameToIsoCodeMap
        self.currency_fraction_code_list = DutchNumericWithUnit.FractionalUnitNameToCodeMap
