#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from typing import Dict, List, Pattern

from recognizers_number.culture import CultureInfo
from recognizers_number.number.parser_factory import AgnosticNumberParserFactory, ParserType
from recognizers_number.number.spanish.extractors import NumberMode, SpanishNumberExtractor
from recognizers_number.number.spanish.parsers import SpanishNumberParserConfiguration
from recognizers_number_with_unit.number_with_unit.constants import Constants
from recognizers_number_with_unit.number_with_unit.extractors import NumberWithUnitExtractorConfiguration
from recognizers_number_with_unit.number_with_unit.parsers import NumberWithUnitParserConfiguration
from recognizers_number_with_unit.resources.base_units import BaseUnits
from recognizers_number_with_unit.resources.spanish_numeric_with_unit import SpanishNumericWithUnit
from recognizers_text.culture import Culture
from recognizers_text.extractor import Extractor
from recognizers_text.parser import Parser
from recognizers_text.utilities import RegExpUtility


class SpanishNumberWithUnitExtractorConfiguration(NumberWithUnitExtractorConfiguration):

    ambiguity_filters_dict: Dict[Pattern, Pattern] = None
    unit_num_extractor: Extractor = SpanishNumberExtractor(NumberMode.Unit)
    build_prefix: str = SpanishNumericWithUnit.BuildPrefix
    build_suffix: str = SpanishNumericWithUnit.BuildSuffix
    connector_token: str = SpanishNumericWithUnit.ConnectorToken
    compound_unit_connector_regex: Pattern = RegExpUtility.get_safe_reg_exp(
        SpanishNumericWithUnit.CompoundUnitConnectorRegex
    )
    non_unit_regex: Pattern = RegExpUtility.get_safe_reg_exp(BaseUnits.PmNonUnitRegex)
    ambiguous_unit_number_multiplier_regex: Pattern = None
    culture_info: CultureInfo = None

    def expand_half_suffix(self, source, result, numbers):
        pass

    def __init__(self, culture_info: CultureInfo):
        culture_info = culture_info or CultureInfo(Culture.Spanish)
        super().__init__(culture_info)


class SpanishCurrencyExtractorConfiguration(SpanishNumberWithUnitExtractorConfiguration):

    extract_type: str = Constants.SYS_UNIT_CURRENCY
    suffix_list: Dict[str, str] = SpanishNumericWithUnit.CurrencySuffixList
    prefix_list: Dict[str, str] = SpanishNumericWithUnit.CurrencyPrefixList
    ambiguous_unit_list: List[str] = SpanishNumericWithUnit.AmbiguousCurrencyUnitList
    culture_info: CultureInfo = None

    def __init__(self, culture_info: CultureInfo = None):
        super().__init__(culture_info)


class SpanishNumberWithUnitParserConfiguration(NumberWithUnitParserConfiguration):

    internal_number_extractor: Extractor = SpanishNumberExtractor(NumberMode.DEFAULT)
    connector_token: str = SpanishNumericWithUnit.ConnectorToken

    def __init__(self, culture_info: CultureInfo):
        culture_info = culture_info or CultureInfo(Culture.Spanish)
        super().__init__(culture_info)
        self.internal_number_parser: Parser = AgnosticNumberParserFactory.get_parser(
            ParserType.NUMBER, SpanishNumberParserConfiguration(culture_info)
        )


class SpanishCurrencyParserConfiguration(SpanishNumberWithUnitParserConfiguration):

    def __init__(self, culture_info: CultureInfo = None):
        super().__init__(culture_info)
        self.add_dict_to_unit_map(SpanishNumericWithUnit.CurrencySuffixList)
        self.add_dict_to_unit_map(SpanishNumericWithUnit.CurrencyPrefixList)
        self.currency_name_to_iso_code_map = SpanishNumericWithUnit.CurrencyNameToIsoCodeMap
        self.currency_fraction_code_list = SpanishNumericWithUnit.FractionalUnitNameToCodeMap
