#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from recognizers_number.culture import CultureInfo
from recognizers_number.number.german.extractors import GermanNumberExtractor, NumberMode
from recognizers_number.number.german.parsers import GermanNumberParserConfiguration
from recognizers_number.number.parser_factory import AgnosticNumberParserFactory, ParserType
from recognizers_number_with_unit.number_with_unit.parsers import NumberWithUnitParserConfiguration
from recognizers_number_with_unit.resources.german_numeric_with_unit import GermanNumericWithUnit
from recognizers_text.culture import Culture
from recognizers_text.extractor import Extractor
from recognizers_text.parser import Parser


class GermanNumberWithUnitParserConfiguration(NumberWithUnitParserConfiguration):

    internal_number_extractor: Extractor = GermanNumberExtractor(NumberMode.DEFAULT)
    connector_token: str = GermanNumericWithUnit.ConnectorToken

    def __init__(self, culture_info: CultureInfo):
        culture_info = culture_info or CultureInfo(Culture.German)
        super().__init__(culture_info)
        self.internal_number_parser: Parser = AgnosticNumberParserFactory.get_parser(
            ParserType.NUMBER, GermanNumberParserConfiguration(culture_info))


class GermanCurrencyParserConfiguration(GermanNumberWithUnitParserConfiguration):

    def __init__(self, culture_info: CultureInfo = None):
        super().__init__(culture_info)
        self.add_dict_to_unit_map(GermanNumericWithUnit.CurrencySuffixList)
        self.add_dict_to_unit_map(GermanNumericWithUnit.CurrencyPrefixList)
        self.currency_name_to_iso_code_map = GermanNumericWithUnit.CurrencyNameToIsoCodeMap
        self.currency_fraction_code_list = GermanNumericWithUnit.FractionalUnitNameToCodeMap
