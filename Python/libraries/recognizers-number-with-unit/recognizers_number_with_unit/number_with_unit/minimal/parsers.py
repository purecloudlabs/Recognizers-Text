from recognizers_text.culture import Culture
from recognizers_text.extractor import Extractor
from recognizers_text.parser import Parser
from recognizers_number.culture import CultureInfo
from recognizers_number.number.minimal.extractors import MinimalNumberExtractor, NumberMode
from recognizers_number.number.parser_factory import AgnosticNumberParserFactory, ParserType
from recognizers_number.number.minimal.parsers import MinimalNumberParserConfiguration
from recognizers_number_with_unit.number_with_unit.parsers import NumberWithUnitParserConfiguration
from recognizers_number_with_unit.resources.minimal_numeric_with_unit import MinimalNumericWithUnit


class MinimalNumberWithUnitParserConfiguration(NumberWithUnitParserConfiguration):
    @property
    def internal_number_parser(self) -> Parser:
        return self._internal_number_parser

    @property
    def internal_number_extractor(self) -> Extractor:
        return self._internal_number_extractor

    @property
    def connector_token(self) -> str:
        return MinimalNumericWithUnit.ConnectorToken

    def __init__(self, culture_info: CultureInfo, decimal_point_separator=True):
        if culture_info is None:
            culture_info = CultureInfo(Culture.Minimal)
        super().__init__(culture_info)
        self._internal_number_extractor = MinimalNumberExtractor(
            NumberMode.DEFAULT)
        self._internal_number_parser = AgnosticNumberParserFactory.get_parser(
            ParserType.NUMBER,
            MinimalNumberParserConfiguration(culture_info, decimal_point_separator=decimal_point_separator))


class MinimalCurrencyParserConfiguration(MinimalNumberWithUnitParserConfiguration):
    def __init__(self, culture_info: CultureInfo = None, decimal_point_separator=True):
        super().__init__(culture_info, decimal_point_separator)
        self.add_dict_to_unit_map(MinimalNumericWithUnit.CurrencySuffixList)
        self.add_dict_to_unit_map(MinimalNumericWithUnit.CurrencyPrefixList)
        self.currency_name_to_iso_code_map = MinimalNumericWithUnit.CurrencyNameToIsoCodeMap
        self.currency_fraction_code_list = MinimalNumericWithUnit.FractionalUnitNameToCodeMap
