#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from typing import Dict, List, Pattern

from recognizers_number.culture import CultureInfo
from recognizers_number.number.english.extractors import EnglishNumberExtractor
from recognizers_number.number.models import NumberMode
from recognizers_number_with_unit.number_with_unit.constants import Constants
from recognizers_number_with_unit.number_with_unit.extractors import NumberWithUnitExtractorConfiguration
from recognizers_number_with_unit.resources.base_units import BaseUnits
from recognizers_number_with_unit.resources.english_numeric_with_unit import EnglishNumericWithUnit
from recognizers_text.culture import Culture
from recognizers_text.extractor import Extractor
from recognizers_text.utilities import DefinitionLoader, RegExpUtility


class EnglishNumberWithUnitExtractorConfiguration(NumberWithUnitExtractorConfiguration):

    ambiguity_filters_dict: Dict[Pattern, Pattern] = DefinitionLoader.load_ambiguity_filters(
        EnglishNumericWithUnit.AmbiguityFiltersDict)
    unit_num_extractor: Extractor = EnglishNumberExtractor(NumberMode.Unit)
    build_prefix: str = EnglishNumericWithUnit.BuildPrefix
    build_suffix: str = EnglishNumericWithUnit.BuildSuffix
    connector_token: str = ''
    compound_unit_connector_regex: Pattern = RegExpUtility.get_safe_reg_exp(
        EnglishNumericWithUnit.CompoundUnitConnectorRegex)
    non_unit_regex: Pattern = RegExpUtility.get_safe_reg_exp(BaseUnits.PmNonUnitRegex)
    ambiguous_unit_number_multiplier_regex: Pattern = None
    culture_info: CultureInfo = None

    def expand_half_suffix(self, source, result, numbers):
        pass

    def __init__(self, culture_info: CultureInfo):
        culture_info = culture_info or CultureInfo(Culture.English)
        super().__init__(culture_info)


class EnglishCurrencyExtractorConfiguration(EnglishNumberWithUnitExtractorConfiguration):

    ambiguity_filters_dict: Dict[Pattern, Pattern] = EnglishNumericWithUnit.AmbiguityFiltersDict
    extract_type: str = Constants.SYS_UNIT_CURRENCY
    suffix_list: Dict[str, str] = EnglishNumericWithUnit.CurrencySuffixList
    prefix_list: Dict[str, str] = EnglishNumericWithUnit.CurrencyPrefixList
    ambiguous_unit_list: List[str] = EnglishNumericWithUnit.AmbiguousCurrencyUnitList
    culture_info: CultureInfo = None

    def __init__(self, culture_info: CultureInfo = None):
        super().__init__(culture_info)
