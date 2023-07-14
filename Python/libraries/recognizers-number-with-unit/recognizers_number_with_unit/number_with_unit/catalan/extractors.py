#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from typing import Dict, List, Pattern

from recognizers_text.culture import Culture
from recognizers_text.extractor import Extractor
from recognizers_text.utilities import RegExpUtility
from recognizers_number.culture import CultureInfo
from recognizers_number.number.models import NumberMode
from recognizers_number.number.catalan.extractors import CatalanNumberExtractor
from recognizers_number_with_unit.number_with_unit.constants import Constants
from recognizers_number_with_unit.number_with_unit.extractors import NumberWithUnitExtractorConfiguration
from recognizers_number_with_unit.resources.catalan_numeric_with_unit import CatalanNumericWithUnit
from recognizers_number_with_unit.resources.base_units import BaseUnits


# pylint: disable=abstract-method
class CatalanNumberWithUnitExtractorConfiguration(NumberWithUnitExtractorConfiguration):
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
        return CatalanNumericWithUnit.ConnectorToken

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
            culture_info = CultureInfo(Culture.Catalan)
        super().__init__(culture_info)
        self._unit_num_extractor = CatalanNumberExtractor(NumberMode.Unit)
        self._build_prefix = CatalanNumericWithUnit.BuildPrefix
        self._build_suffix = CatalanNumericWithUnit.BuildSuffix
        self._compound_unit_connector_regex = RegExpUtility.get_safe_reg_exp(
            CatalanNumericWithUnit.CompoundUnitConnectorRegex)
        self._pm_non_unit_regex = RegExpUtility.get_safe_reg_exp(
            BaseUnits.PmNonUnitRegex)


# pylint: enable=abstract-method

class CatalanAgeExtractorConfiguration(CatalanNumberWithUnitExtractorConfiguration):
    @property
    def extract_type(self) -> str:
        return Constants.SYS_UNIT_AGE

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
        self._suffix_list = CatalanNumericWithUnit.AgeSuffixList
        self._prefix_list = dict()
        self._ambiguous_unit_list = CatalanNumericWithUnit.AmbiguousAgeUnitList


class CatalanCurrencyExtractorConfiguration(CatalanNumberWithUnitExtractorConfiguration):
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
        self._suffix_list = CatalanNumericWithUnit.CurrencySuffixList
        self._prefix_list = CatalanNumericWithUnit.CurrencyPrefixList
        self._ambiguous_unit_list = CatalanNumericWithUnit.AmbiguousCurrencyUnitList


class CatalanDimensionExtractorConfiguration(CatalanNumberWithUnitExtractorConfiguration):
    @property
    def extract_type(self) -> str:
        return Constants.SYS_UNIT_DIMENSION

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

        self._suffix_list = {
            **CatalanNumericWithUnit.InformationSuffixList,
            **CatalanNumericWithUnit.AreaSuffixList,
            **CatalanNumericWithUnit.LengthSuffixList,
            **CatalanNumericWithUnit.SpeedSuffixList,
            **CatalanNumericWithUnit.VolumeSuffixList,
            **CatalanNumericWithUnit.WeightSuffixList
        }

        self._prefix_list = dict()
        self._ambiguous_unit_list = CatalanNumericWithUnit.AmbiguousDimensionUnitList +\
            CatalanNumericWithUnit.AmbiguousAngleUnitList +\
            CatalanNumericWithUnit.AmbiguousLengthUnitList +\
            CatalanNumericWithUnit.AmbiguousSpeedUnitList +\
            CatalanNumericWithUnit.AmbiguousWeightUnitList


class CatalanTemperatureExtractorConfiguration(CatalanNumberWithUnitExtractorConfiguration):
    @property
    def extract_type(self) -> str:
        return Constants.SYS_UNIT_TEMPERATURE

    @property
    def suffix_list(self) -> Dict[str, str]:
        return self._suffix_list

    @property
    def prefix_list(self) -> Dict[str, str]:
        return self._prefix_list

    @property
    def ambiguous_unit_list(self) -> List[str]:
        return self._ambiguous_unit_list

    @property
    def ambiguous_unit_number_multiplier_regex(self) -> Pattern:
        return self._ambiguous_unit_number_multiplier_regex

    def __init__(self, culture_info: CultureInfo = None):
        super().__init__(culture_info)
        self._suffix_list = CatalanNumericWithUnit.TemperatureSuffixList
        self._prefix_list = dict()
        self._ambiguous_unit_list = []
        self._ambiguous_unit_number_multiplier_regex = RegExpUtility.get_safe_reg_exp(
            BaseUnits.AmbiguousUnitNumberMultiplierRegex)
