from typing import Dict, List, Pattern

from recognizers_number.culture import CultureInfo
from recognizers_number.number.arabic.extractors import ArabicNumberExtractor
from recognizers_number.number.models import NumberMode
from recognizers_number_with_unit.number_with_unit.constants import Constants
from recognizers_number_with_unit.number_with_unit.extractors import NumberWithUnitExtractorConfiguration
from recognizers_number_with_unit.resources.arabic_numeric_with_unit import ArabicNumericWithUnit
from recognizers_number_with_unit.resources.base_units import BaseUnits
from recognizers_text.culture import Culture
from recognizers_text.extractor import Extractor
from recognizers_text.utilities import RegExpUtility


class ArabicNumberWithUnitExtractorConfiguration(NumberWithUnitExtractorConfiguration):

    ambiguity_filters_dict: Dict[Pattern, Pattern] = None
    unit_num_extractor: Extractor = ArabicNumberExtractor(NumberMode.Unit)
    build_prefix: str = ArabicNumericWithUnit.BuildPrefix
    build_suffix: str = ArabicNumericWithUnit.BuildSuffix
    connector_token: str = None
    compound_unit_connector_regex: Pattern = RegExpUtility.get_safe_reg_exp(
        ArabicNumericWithUnit.CompoundUnitConnectorRegex)
    non_unit_regex: Pattern = RegExpUtility.get_safe_reg_exp(BaseUnits.PmNonUnitRegex)
    ambiguous_unit_number_multiplier_regex: Pattern = None
    culture_info: CultureInfo = None

    def expand_half_suffix(self, source, result, numbers):
        pass

    def __init__(self, culture_info: CultureInfo):
        culture_info = culture_info or CultureInfo(Culture.Arabic)
        super().__init__(culture_info)


class ArabicCurrencyExtractorConfiguration(ArabicNumberWithUnitExtractorConfiguration):

    extract_type: str = Constants.SYS_UNIT_CURRENCY
    suffix_list: Dict[str, str] = ArabicNumericWithUnit.CurrencySuffixList
    prefix_list: Dict[str, str] = ArabicNumericWithUnit.CurrencyPrefixList
    ambiguous_unit_list: List[str] = ArabicNumericWithUnit.AmbiguousCurrencyUnitList
    culture_info: CultureInfo = None

    def __init__(self, culture_info: CultureInfo = None):
        super().__init__(culture_info)
