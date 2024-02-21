from typing import Dict, List, Pattern

from recognizers_text.culture import Culture
from recognizers_text.extractor import Extractor
from recognizers_text.utilities import RegExpUtility
from recognizers_number.culture import CultureInfo
from recognizers_number.number.models import NumberMode
from recognizers_number.number.minimal.extractors import MinimalNumberExtractor
from recognizers_number_with_unit.number_with_unit.constants import Constants
from recognizers_number_with_unit.number_with_unit.extractors import NumberWithUnitExtractorConfiguration
from recognizers_number_with_unit.resources.minimal_numeric_with_unit import MinimalNumericWithUnit
from recognizers_number_with_unit.resources.base_units import BaseUnits


class MinimalNumberWithUnitExtractorConfiguration(NumberWithUnitExtractorConfiguration):
    @property
    def ambiguity_filters_dict(self) -> Dict[Pattern, Pattern]:
        return None

    @property
    def unit_num_extractor(self) -> Extractor:
        return self._unit_num_extractor

    @property
    def build_prefix(self) -> str:
        return self._build_prefix

    @property
    def build_suffix(self) -> str:
        return self._build_suffix

    @property
    def connector_token(self) -> str:
        return MinimalNumericWithUnit.ConnectorToken

    @property
    def compound_unit_connector_regex(self) -> Pattern:
        return self._compound_unit_connector_regex

    @property
    def non_unit_regex(self) -> Pattern:
        return self._pm_non_unit_regex

    @property
    def ambiguous_unit_number_multiplier_regex(self) -> Pattern:
        return None

    def expand_half_suffix(self, source, result, numbers):
        pass

    def __init__(self, culture_info: CultureInfo):
        if culture_info is None:
            culture_info = CultureInfo(Culture.Minimal)
        super().__init__(culture_info)
        self._unit_num_extractor = MinimalNumberExtractor(NumberMode.Unit)
        self._build_prefix = MinimalNumericWithUnit.BuildPrefix
        self._build_suffix = MinimalNumericWithUnit.BuildSuffix
        self._compound_unit_connector_regex = RegExpUtility.get_safe_reg_exp(
            MinimalNumericWithUnit.CompoundUnitConnectorRegex)
        self._pm_non_unit_regex = RegExpUtility.get_safe_reg_exp(
            BaseUnits.PmNonUnitRegex)


class MinimalCurrencyExtractorConfiguration(MinimalNumberWithUnitExtractorConfiguration):
    @property
    def extract_type(self) -> str:
        return Constants.SYS_UNIT_CURRENCY

    @property
    def suffix_list(self) -> Dict[str, str]:
        return self._suffix_list

    @property
    def prefix_list(self) -> Dict[str, str]:
        return self._prefix_list

    @property
    def ambiguous_unit_list(self) -> List[str]:
        return self._ambiguous_unit_list

    def __init__(self, culture_info: CultureInfo = None):
        super().__init__(culture_info)
        self._suffix_list = MinimalNumericWithUnit.CurrencySuffixList
        self._prefix_list = MinimalNumericWithUnit.CurrencyPrefixList
        self._ambiguous_unit_list = MinimalNumericWithUnit.AmbiguousCurrencyUnitList