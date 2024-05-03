#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from typing import Dict, List, Pattern

import regex

from recognizers_number.culture import CultureInfo
from recognizers_number.number.chinese.extractors import ChineseNumberExtractor, ChineseNumberExtractorMode
from recognizers_number.number.chinese.parsers import ChineseNumberParserConfiguration
from recognizers_number.number.parser_factory import AgnosticNumberParserFactory, ParserType
from recognizers_number_with_unit.number_with_unit.constants import Constants
from recognizers_number_with_unit.number_with_unit.extractors import NumberWithUnitExtractorConfiguration
from recognizers_number_with_unit.number_with_unit.parsers import NumberWithUnitParserConfiguration
from recognizers_number_with_unit.resources.base_units import BaseUnits
from recognizers_number_with_unit.resources.chinese_numeric_with_unit import ChineseNumericWithUnit
from recognizers_text.culture import Culture
from recognizers_text.extractor import Extractor
from recognizers_text.parser import Parser
from recognizers_text.utilities import RegExpUtility


class ChineseNumberWithUnitExtractorConfiguration(NumberWithUnitExtractorConfiguration):

    ambiguity_filters_dict: Dict[Pattern, Pattern] = None
    unit_num_extractor: Extractor = ChineseNumberExtractor(ChineseNumberExtractorMode.EXTRACT_ALL)
    build_prefix: str = ChineseNumericWithUnit.BuildPrefix
    build_suffix: str = ChineseNumericWithUnit.BuildSuffix
    connector_token: str = ChineseNumericWithUnit.ConnectorToken
    compound_unit_connector_regex: Pattern = RegExpUtility.get_safe_reg_exp(
        ChineseNumericWithUnit.CompoundUnitConnectorRegex)
    non_unit_regex: Pattern = RegExpUtility.get_safe_reg_exp(BaseUnits.PmNonUnitRegex)
    ambiguous_unit_number_multiplier_regex: Pattern = None
    culture_info: CultureInfo = None

    def expand_half_suffix(self, source, result, numbers):
        # Expand Chinese phrase to the `half` patterns when it follows closely origin phrase.
        if self._half_unit_regex and numbers:
            match = [number for number in numbers if regex.match(self._half_unit_regex, number.text)]
            if match:
                res = []
                for er in result:
                    start = er.start
                    length = er.length
                    match_suffix = [mr for mr in match if mr.start == (start + length)]
                    if len(match_suffix) == 1:
                        mr = match_suffix[0]
                        er.length += mr.length
                        er.text += mr.text
                        er.data = [er.data, mr]
                    res.append(er)
                result = res

    def __init__(self, culture_info: CultureInfo):
        culture_info = culture_info or CultureInfo(Culture.Chinese)
        super().__init__(culture_info)
        self._half_unit_regex = RegExpUtility.get_safe_reg_exp(ChineseNumericWithUnit.HalfUnitRegex)


class ChineseCurrencyExtractorConfiguration(ChineseNumberWithUnitExtractorConfiguration):

    extract_type: str = Constants.SYS_UNIT_CURRENCY
    suffix_list: Dict[str, str] = ChineseNumericWithUnit.CurrencySuffixList
    prefix_list: Dict[str, str] = ChineseNumericWithUnit.CurrencyPrefixList
    ambiguous_unit_list: List[str] = ChineseNumericWithUnit.CurrencyAmbiguousValues
    culture_info: CultureInfo = None

    def __init__(self, culture_info: CultureInfo = Culture.Chinese):
        super().__init__(culture_info)


class ChineseNumberWithUnitParserConfiguration(NumberWithUnitParserConfiguration):

    internal_number_extractor: Extractor = ChineseNumberExtractor(ChineseNumberExtractorMode.EXTRACT_ALL)
    connector_token: str = ''

    def __init__(self, culture_info: CultureInfo):
        culture_info = culture_info or CultureInfo(Culture.Chinese)
        super().__init__(culture_info)
        self.internal_number_parser: Parser = AgnosticNumberParserFactory.get_parser(
            ParserType.NUMBER, ChineseNumberParserConfiguration(culture_info))
        self.currency_name_to_iso_code_map = ChineseNumericWithUnit.CurrencyNameToIsoCodeMap
        self.currency_fraction_code_list = ChineseNumericWithUnit.FractionalUnitNameToCodeMap


class ChineseCurrencyParserConfiguration(ChineseNumberWithUnitParserConfiguration):

    def __init__(self, culture_info: CultureInfo = None):
        super().__init__(culture_info)
        self.add_dict_to_unit_map(ChineseNumericWithUnit.CurrencySuffixList)
        self.add_dict_to_unit_map(ChineseNumericWithUnit.CurrencyPrefixList)
