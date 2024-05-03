#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from recognizers_number.culture import CultureInfo
from recognizers_number.number.italian.extractors import ItalianNumberExtractor, NumberMode
from recognizers_number.number.italian.parsers import ItalianNumberParserConfiguration
from recognizers_number.number.parser_factory import AgnosticNumberParserFactory, ParserType
from recognizers_number_with_unit.number_with_unit.parsers import NumberWithUnitParserConfiguration
from recognizers_number_with_unit.resources.italian_numeric_with_unit import ItalianNumericWithUnit
from recognizers_text.culture import Culture
from recognizers_text.extractor import Extractor
from recognizers_text.parser import Parser


class ItalianNumberWithUnitParserConfiguration(NumberWithUnitParserConfiguration):

    internal_number_extractor: Extractor = ItalianNumberExtractor(NumberMode.DEFAULT)
    connector_token: str = ItalianNumericWithUnit.ConnectorToken

    def __init__(self, culture_info: CultureInfo):
        culture_info = culture_info or CultureInfo(Culture.Italian)
        super().__init__(culture_info)
        self.internal_number_parser: Parser = AgnosticNumberParserFactory.get_parser(
            ParserType.NUMBER, ItalianNumberParserConfiguration(culture_info))


class ItalianCurrencyParserConfiguration(ItalianNumberWithUnitParserConfiguration):

    def __init__(self, culture_info: CultureInfo = None):
        super().__init__(culture_info)
        self.add_dict_to_unit_map(ItalianNumericWithUnit.CurrencySuffixList)
        self.add_dict_to_unit_map(ItalianNumericWithUnit.CurrencyPrefixList)
        self.currency_name_to_iso_code_map = ItalianNumericWithUnit.CurrencyNameToIsoCodeMap
        self.currency_fraction_code_list = ItalianNumericWithUnit.FractionalUnitNameToCodeMap
