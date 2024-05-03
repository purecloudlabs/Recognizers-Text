#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from recognizers_number.culture import CultureInfo
from recognizers_number.number.parser_factory import AgnosticNumberParserFactory, ParserType
from recognizers_number.number.spanish.extractors import NumberMode, SpanishNumberExtractor
from recognizers_number.number.spanish.parsers import SpanishNumberParserConfiguration
from recognizers_number_with_unit.number_with_unit.parsers import NumberWithUnitParserConfiguration
from recognizers_number_with_unit.resources.spanish_numeric_with_unit import SpanishNumericWithUnit
from recognizers_text.culture import Culture
from recognizers_text.extractor import Extractor
from recognizers_text.parser import Parser


class SpanishNumberWithUnitParserConfiguration(NumberWithUnitParserConfiguration):

    internal_number_extractor: Extractor = SpanishNumberExtractor(NumberMode.DEFAULT)
    connector_token: str = SpanishNumericWithUnit.ConnectorToken

    def __init__(self, culture_info: CultureInfo):
        culture_info = culture_info or CultureInfo(Culture.Spanish)
        super().__init__(culture_info)
        self.internal_number_parser: Parser = AgnosticNumberParserFactory.get_parser(
            ParserType.NUMBER, SpanishNumberParserConfiguration(culture_info))


class SpanishCurrencyParserConfiguration(SpanishNumberWithUnitParserConfiguration):

    def __init__(self, culture_info: CultureInfo = None):
        super().__init__(culture_info)
        self.add_dict_to_unit_map(SpanishNumericWithUnit.CurrencySuffixList)
        self.add_dict_to_unit_map(SpanishNumericWithUnit.CurrencyPrefixList)
        self.currency_name_to_iso_code_map = SpanishNumericWithUnit.CurrencyNameToIsoCodeMap
        self.currency_fraction_code_list = SpanishNumericWithUnit.FractionalUnitNameToCodeMap

