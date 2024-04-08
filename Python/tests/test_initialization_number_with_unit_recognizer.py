#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

import pytest
from recognizers_text import Culture
from recognizers_number_with_unit.number_with_unit import NumberWithUnitRecognizer, NumberWithUnitOptions
from recognizers_number_with_unit.number_with_unit.models import CurrencyModel, AbstractNumberWithUnitModel, ExtractorParserModel
from recognizers_number_with_unit.number_with_unit.extractors import NumberWithUnitExtractor
from recognizers_number_with_unit.number_with_unit.english.extractors import EnglishCurrencyExtractorConfiguration
from recognizers_number_with_unit.number_with_unit.parsers import NumberWithUnitParser
from recognizers_number_with_unit.number_with_unit.english.parsers import EnglishCurrencyParserConfiguration


class TestInitializationNumberWithUnitRecognizer():
    control_model = CurrencyModel(
        [ExtractorParserModel(NumberWithUnitExtractor(EnglishCurrencyExtractorConfiguration(
        )), NumberWithUnitParser(EnglishCurrencyParserConfiguration()))]
    )
    english_culture = Culture.English
    spanish_culture = Culture.Spanish
    invalid_culture = "vo-id"

    def assert_models_equal(
            self, expected: AbstractNumberWithUnitModel, actual: AbstractNumberWithUnitModel):
        assert actual.model_type_name == expected.model_type_name
        assert len(actual.extractor_parser) == len(expected.extractor_parser)

        # deep comparison
        for actual_item, expected_item in zip(
                actual.extractor_parser, expected.extractor_parser):
            assert isinstance(actual_item.parser, type(expected_item.parser))

            # configs
            assert isinstance(
                actual_item.extractor.config, type(
                    expected_item.extractor.config))
            assert isinstance(
                actual_item.parser.config, type(
                    expected_item.parser.config))

    def assert_models_distinct(self, expected, actual):
        assert actual.model_type_name == expected.model_type_name
        assert len(actual.extractor_parser) == len(expected.extractor_parser)

        # deep comparison
        any_config_is_different = False
        for actual_item, expected_item in zip(
                actual.extractor_parser, expected.extractor_parser):
            assert isinstance(actual_item.parser, type(expected_item.parser))

            # configs
            any_config_is_different = any_config_is_different or not isinstance(
                actual_item.extractor.config, type(expected_item.extractor.config))
            any_config_is_different = any_config_is_different or not isinstance(
                actual_item.parser.config, type(expected_item.parser.config))

        assert any_config_is_different

    def test_with_invalid_culture_and_without_fallback_throw_error(self):
        recognizer = NumberWithUnitRecognizer()
        with pytest.raises(ValueError):
            recognizer.get_currency_model(self.invalid_culture, False)

    def test_with_invalid_culture_as_target_and_without_fallback_throw_error(
            self):
        recognizer = NumberWithUnitRecognizer(self.invalid_culture)
        with pytest.raises(ValueError):
            recognizer.get_currency_model(None, False)

    def test_initialization_with_int_option_resolve_options_enum(self):
        recognizer = NumberWithUnitRecognizer(
            self.english_culture, NumberWithUnitOptions.NONE, False)
        assert (recognizer.options &
                NumberWithUnitOptions.NONE) == NumberWithUnitOptions.NONE

    def test_initialization_with_invalid_options_throw_error(self):
        with pytest.raises(ValueError):
            NumberWithUnitRecognizer(self.invalid_culture, -1)


if __name__ == '__main__':
    tests = TestInitializationNumberWithUnitRecognizer()
