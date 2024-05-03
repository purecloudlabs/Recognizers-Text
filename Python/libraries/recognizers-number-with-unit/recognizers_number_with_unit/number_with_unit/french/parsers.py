#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from recognizers_number.culture import CultureInfo
from recognizers_number.number.french.extractors import FrenchNumberExtractor, NumberMode
from recognizers_number.number.french.parsers import FrenchNumberParserConfiguration
from recognizers_number.number.parser_factory import AgnosticNumberParserFactory, ParserType
from recognizers_number_with_unit.number_with_unit.parsers import NumberWithUnitParserConfiguration
from recognizers_number_with_unit.resources.french_numeric_with_unit import FrenchNumericWithUnit
from recognizers_text.culture import Culture
from recognizers_text.extractor import Extractor
from recognizers_text.parser import Parser


class FrenchNumberWithUnitParserConfiguration(NumberWithUnitParserConfiguration):

    internal_number_extractor: Extractor = FrenchNumberExtractor(NumberMode.DEFAULT)
    connector_token: str = FrenchNumericWithUnit.ConnectorToken

    def __init__(self, culture_info: CultureInfo):
        culture_info = culture_info or CultureInfo(Culture.French)
        super().__init__(culture_info)
        self.internal_number_parser: Parser = AgnosticNumberParserFactory.get_parser(
            ParserType.NUMBER, FrenchNumberParserConfiguration(culture_info))


class FrenchCurrencyParserConfiguration(FrenchNumberWithUnitParserConfiguration):

    def __init__(self, culture_info: CultureInfo = None):
        super().__init__(culture_info)
        self.add_dict_to_unit_map(FrenchNumericWithUnit.CurrencySuffixList)
        self.add_dict_to_unit_map(FrenchNumericWithUnit.CurrencyPrefixList)
        self.currency_name_to_iso_code_map = FrenchNumericWithUnit.CurrencyNameToIsoCodeMap
        self.currency_fraction_code_list = FrenchNumericWithUnit.FractionalUnitNameToCodeMap

