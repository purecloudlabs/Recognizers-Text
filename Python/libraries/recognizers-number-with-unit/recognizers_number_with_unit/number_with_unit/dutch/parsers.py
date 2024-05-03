#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from recognizers_number.culture import CultureInfo
from recognizers_number.number.dutch.extractors import DutchNumberExtractor, NumberMode
from recognizers_number.number.dutch.parsers import DutchNumberParserConfiguration
from recognizers_number.number.parser_factory import AgnosticNumberParserFactory, ParserType
from recognizers_number_with_unit.number_with_unit.parsers import NumberWithUnitParserConfiguration
from recognizers_number_with_unit.resources.dutch_numeric_with_unit import DutchNumericWithUnit
from recognizers_text import Culture
from recognizers_text.extractor import Extractor
from recognizers_text.parser import Parser


class DutchNumberWithUnitParserConfiguration(NumberWithUnitParserConfiguration):

    internal_number_extractor: Extractor = DutchNumberExtractor(NumberMode.DEFAULT)
    connector_token: str = ''

    def __init__(self, culture_info: CultureInfo):
        culture_info = culture_info or CultureInfo(Culture.Dutch)
        super().__init__(culture_info)
        self.internal_number_parser: Parser = AgnosticNumberParserFactory.get_parser(
            ParserType.NUMBER, DutchNumberParserConfiguration(culture_info))


class DutchCurrencyParserConfiguration(DutchNumberWithUnitParserConfiguration):

    def __init__(self, culture_info: CultureInfo = None):
        super().__init__(culture_info)
        self.add_dict_to_unit_map(DutchNumericWithUnit.CurrencySuffixList)
        self.add_dict_to_unit_map(DutchNumericWithUnit.CurrencyPrefixList)
        self.currency_name_to_iso_code_map = DutchNumericWithUnit.CurrencyNameToIsoCodeMap
        self.currency_fraction_code_list = DutchNumericWithUnit.FractionalUnitNameToCodeMap

