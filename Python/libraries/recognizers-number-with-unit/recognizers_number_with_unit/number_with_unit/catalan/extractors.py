from typing import Dict, List, Pattern

from recognizers_number.culture import CultureInfo
from recognizers_number.number.catalan.extractors import CatalanNumberExtractor
from recognizers_number.number.models import NumberMode
from recognizers_number_with_unit.number_with_unit.constants import Constants
from recognizers_number_with_unit.number_with_unit.extractors import NumberWithUnitExtractorConfiguration
from recognizers_number_with_unit.resources.base_units import BaseUnits
from recognizers_number_with_unit.resources.catalan_numeric_with_unit import CatalanNumericWithUnit
from recognizers_text.culture import Culture
from recognizers_text.extractor import Extractor
from recognizers_text.utilities import RegExpUtility


class CatalanNumberWithUnitExtractorConfiguration(NumberWithUnitExtractorConfiguration):

    ambiguity_filters_dict: Dict[Pattern, Pattern] = None
    unit_num_extractor: Extractor = CatalanNumberExtractor(NumberMode.Unit)
    build_prefix: str = CatalanNumericWithUnit.BuildPrefix
    build_suffix: str = CatalanNumericWithUnit.BuildSuffix
    connector_token: str = CatalanNumericWithUnit.ConnectorToken
    compound_unit_connector_regex: Pattern = RegExpUtility.get_safe_reg_exp(
        CatalanNumericWithUnit.CompoundUnitConnectorRegex)
    non_unit_regex: Pattern = RegExpUtility.get_safe_reg_exp(BaseUnits.PmNonUnitRegex)
    ambiguous_unit_number_multiplier_regex: Pattern = None
    culture_info: CultureInfo = None

    def expand_half_suffix(self, source, result, numbers):
        pass

    def __init__(self, culture_info: CultureInfo):
        culture_info = culture_info or CultureInfo(Culture.Catalan)
        super().__init__(culture_info)


class CatalanCurrencyExtractorConfiguration(CatalanNumberWithUnitExtractorConfiguration):

    extract_type: str = Constants.SYS_UNIT_CURRENCY
    suffix_list: Dict[str, str] = CatalanNumericWithUnit.CurrencySuffixList
    prefix_list: Dict[str, str] = CatalanNumericWithUnit.CurrencyPrefixList
    ambiguous_unit_list: List[str] = CatalanNumericWithUnit.AmbiguousCurrencyUnitList
    culture_info: CultureInfo = None

    def __init__(self, culture_info: CultureInfo = None):
        super().__init__(culture_info)
