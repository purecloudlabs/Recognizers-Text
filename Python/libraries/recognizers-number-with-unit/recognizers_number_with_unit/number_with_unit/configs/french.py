#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from typing import Dict, List, Pattern

from recognizers_number.culture import CultureInfo
from recognizers_number.number.french.extractors import FrenchNumberExtractor, NumberMode
from recognizers_number.number.french.parsers import FrenchNumberParserConfiguration
from recognizers_number.number.parser_factory import AgnosticNumberParserFactory, ParserType
from recognizers_number_with_unit.number_with_unit.constants import Constants
from recognizers_number_with_unit.number_with_unit.extractors import NumberWithUnitExtractorConfiguration
from recognizers_number_with_unit.number_with_unit.parsers import NumberWithUnitParserConfiguration
from recognizers_number_with_unit.resources.base_units import BaseUnits
from recognizers_number_with_unit.resources.french_numeric_with_unit import FrenchNumericWithUnit
from recognizers_text.culture import Culture
from recognizers_text.extractor import Extractor
from recognizers_text.parser import Parser
from recognizers_text.utilities import RegExpUtility


class FrenchNumberWithUnitExtractorConfiguration(NumberWithUnitExtractorConfiguration):

    ambiguity_filters_dict: Dict[Pattern, Pattern] = FrenchNumericWithUnit.AmbiguityFiltersDict
    unit_num_extractor: Extractor = FrenchNumberExtractor(NumberMode.Unit)
    build_prefix: str = FrenchNumericWithUnit.BuildPrefix
    build_suffix: str = FrenchNumericWithUnit.BuildSuffix
    connector_token: str = FrenchNumericWithUnit.ConnectorToken
    compound_unit_connector_regex: Pattern = RegExpUtility.get_safe_reg_exp(
        FrenchNumericWithUnit.CompoundUnitConnectorRegex
    )
    non_unit_regex: Pattern = RegExpUtility.get_safe_reg_exp(BaseUnits.PmNonUnitRegex)
    ambiguous_unit_number_multiplier_regex: Pattern = None
    culture_info: CultureInfo = None

    def expand_half_suffix(self, source, result, numbers):
        pass

    def __init__(self, culture_info: CultureInfo):
        culture_info = culture_info or CultureInfo(Culture.French)
        super().__init__(culture_info)


class FrenchCurrencyExtractorConfiguration(FrenchNumberWithUnitExtractorConfiguration):

    extract_type: str = Constants.SYS_UNIT_CURRENCY
    suffix_list: Dict[str, str] = FrenchNumericWithUnit.CurrencySuffixList
    prefix_list: Dict[str, str] = FrenchNumericWithUnit.CurrencyPrefixList
    ambiguous_unit_list: List[str] = FrenchNumericWithUnit.AmbiguousCurrencyUnitList
    culture_info: CultureInfo = None

    def __init__(self, culture_info: CultureInfo = None):
        super().__init__(culture_info)


class FrenchNumberWithUnitParserConfiguration(NumberWithUnitParserConfiguration):

    internal_number_extractor: Extractor = FrenchNumberExtractor(NumberMode.DEFAULT)
    connector_token: str = FrenchNumericWithUnit.ConnectorToken

    def __init__(self, culture_info: CultureInfo):
        culture_info = culture_info or CultureInfo(Culture.French)
        super().__init__(culture_info)
        self.internal_number_parser: Parser = AgnosticNumberParserFactory.get_parser(
            ParserType.NUMBER, FrenchNumberParserConfiguration(culture_info)
        )


class FrenchCurrencyParserConfiguration(FrenchNumberWithUnitParserConfiguration):

    def __init__(self, culture_info: CultureInfo = None):
        super().__init__(culture_info)
        self.add_dict_to_unit_map(FrenchNumericWithUnit.CurrencySuffixList)
        self.add_dict_to_unit_map(FrenchNumericWithUnit.CurrencyPrefixList)
        self.currency_name_to_iso_code_map = FrenchNumericWithUnit.CurrencyNameToIsoCodeMap
        self.currency_fraction_code_list = FrenchNumericWithUnit.FractionalUnitNameToCodeMap
