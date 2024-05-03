#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from recognizers_number.culture import CultureInfo
from recognizers_number.number.english.extractors import EnglishNumberExtractor, NumberMode
from recognizers_number.number.english.parsers import EnglishNumberParserConfiguration
from recognizers_number.number.parser_factory import AgnosticNumberParserFactory, ParserType
from recognizers_number_with_unit.number_with_unit.parsers import NumberWithUnitParserConfiguration
from recognizers_number_with_unit.resources.english_numeric_with_unit import EnglishNumericWithUnit
from recognizers_text import Culture
from recognizers_text.extractor import Extractor
from recognizers_text.parser import Parser


class EnglishNumberWithUnitParserConfiguration(NumberWithUnitParserConfiguration):

    internal_number_extractor: Extractor = EnglishNumberExtractor(NumberMode.DEFAULT)
    connector_token: str = ''

    def __init__(self, culture_info: CultureInfo):
        culture_info = culture_info or CultureInfo(Culture.English)
        super().__init__(culture_info)
        self.internal_number_parser: Parser = AgnosticNumberParserFactory.get_parser(
            ParserType.NUMBER, EnglishNumberParserConfiguration(culture_info))


class EnglishCurrencyParserConfiguration(EnglishNumberWithUnitParserConfiguration):

    def __init__(self, culture_info: CultureInfo = None):
        super().__init__(culture_info)
        self.add_dict_to_unit_map(EnglishNumericWithUnit.CurrencySuffixList)
        self.add_dict_to_unit_map(EnglishNumericWithUnit.CurrencyPrefixList)
        self.currency_name_to_iso_code_map = EnglishNumericWithUnit.CurrencyNameToIsoCodeMap
        self.currency_fraction_code_list = EnglishNumericWithUnit.FractionalUnitNameToCodeMap

