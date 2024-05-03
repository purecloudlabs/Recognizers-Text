#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from recognizers_number.culture import CultureInfo
from recognizers_number.number.japanese.extractors import JapaneseNumberExtractor, JapaneseNumberExtractorMode
from recognizers_number.number.japanese.parsers import JapaneseNumberParserConfiguration
from recognizers_number.number.parser_factory import AgnosticNumberParserFactory, ParserType
from recognizers_number_with_unit.number_with_unit.parsers import NumberWithUnitParserConfiguration
from recognizers_number_with_unit.resources.japanese_numeric_with_unit import JapaneseNumericWithUnit
from recognizers_text.culture import Culture
from recognizers_text.extractor import Extractor
from recognizers_text.parser import Parser


class JapaneseNumberWithUnitParserConfiguration(NumberWithUnitParserConfiguration):

    internal_number_extractor: Extractor = JapaneseNumberExtractor(JapaneseNumberExtractorMode.EXTRACT_ALL)
    connector_token: str = JapaneseNumericWithUnit.ConnectorToken

    def __init__(self, culture_info: CultureInfo):
        culture_info = culture_info or CultureInfo(Culture.Japanese)
        super().__init__(culture_info)
        self.internal_number_parser: Parser = AgnosticNumberParserFactory.get_parser(
            ParserType.NUMBER, JapaneseNumberParserConfiguration(culture_info))


class JapaneseCurrencyParserConfiguration(JapaneseNumberWithUnitParserConfiguration):

    def __init__(self, culture_info: CultureInfo = None):
        super().__init__(culture_info)
        self.add_dict_to_unit_map(JapaneseNumericWithUnit.CurrencySuffixList)
        self.add_dict_to_unit_map(JapaneseNumericWithUnit.CurrencyPrefixList)
        self.currency_name_to_iso_code_map = JapaneseNumericWithUnit.CurrencyNameToIsoCodeMap
        self.currency_fraction_code_list = JapaneseNumericWithUnit.FractionalUnitNameToCodeMap

