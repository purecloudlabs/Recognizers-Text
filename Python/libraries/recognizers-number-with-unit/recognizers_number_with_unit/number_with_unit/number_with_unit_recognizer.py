from enum import IntFlag
from typing import List

from recognizers_number.culture import CultureInfo
from recognizers_text import Culture, Recognizer
from recognizers_text.model import Model, ModelResult

from .configs import (
    ArabicCurrencyExtractorConfiguration,
    ArabicCurrencyParserConfiguration,
    CatalanCurrencyExtractorConfiguration,
    CatalanCurrencyParserConfiguration,
    ChineseCurrencyExtractorConfiguration,
    ChineseCurrencyParserConfiguration,
    DutchCurrencyExtractorConfiguration,
    DutchCurrencyParserConfiguration,
    EnglishCurrencyExtractorConfiguration,
    EnglishCurrencyParserConfiguration,
    FrenchCurrencyExtractorConfiguration,
    FrenchCurrencyParserConfiguration,
    GermanCurrencyExtractorConfiguration,
    GermanCurrencyParserConfiguration,
    ItalianCurrencyExtractorConfiguration,
    ItalianCurrencyParserConfiguration,
    JapaneseCurrencyExtractorConfiguration,
    JapaneseCurrencyParserConfiguration,
    PortugueseCurrencyExtractorConfiguration,
    PortugueseCurrencyParserConfiguration,
    SpanishCurrencyExtractorConfiguration,
    SpanishCurrencyParserConfiguration,
)
from .extractors import BaseMergedUnitExtractor, NumberWithUnitExtractor
from .models import CurrencyModel, ExtractorParserModel
from .parsers import BaseMergedUnitParser, NumberWithUnitParser


class NumberWithUnitOptions(IntFlag):
    NONE = 0


class NumberWithUnitRecognizer(Recognizer[NumberWithUnitOptions]):
    def __init__(self, target_culture: str = None,
                 options: NumberWithUnitOptions = NumberWithUnitOptions.NONE,
                 lazy_initialization: bool = True):
        if options < NumberWithUnitOptions.NONE or options > NumberWithUnitOptions.NONE:
            raise ValueError()
        super().__init__(target_culture, options, lazy_initialization)

    def initialize_configuration(self):
        # region English
        self.register_model('CurrencyModel', Culture.English, lambda options: CurrencyModel(
            [ExtractorParserModel(BaseMergedUnitExtractor(EnglishCurrencyExtractorConfiguration(
            )), BaseMergedUnitParser(EnglishCurrencyParserConfiguration()))]
        ))
        # endregion

        # region Chinese
        self.register_model('CurrencyModel', Culture.Chinese, lambda options: CurrencyModel([
            ExtractorParserModel(
                BaseMergedUnitExtractor(
                    ChineseCurrencyExtractorConfiguration()),
                BaseMergedUnitParser(ChineseCurrencyParserConfiguration())),
            ExtractorParserModel(
                NumberWithUnitExtractor(
                    EnglishCurrencyExtractorConfiguration()),
                NumberWithUnitParser(EnglishCurrencyParserConfiguration()))
        ]))
        # endregion

        # region Dutch
        self.register_model('CurrencyModel', Culture.Dutch, lambda options: CurrencyModel(
            [ExtractorParserModel(BaseMergedUnitExtractor(DutchCurrencyExtractorConfiguration(
            )), BaseMergedUnitParser(DutchCurrencyParserConfiguration()))]
        ))
        # endregion

        # region French
        self.register_model('CurrencyModel', Culture.French, lambda options: CurrencyModel(
            [ExtractorParserModel(BaseMergedUnitExtractor(FrenchCurrencyExtractorConfiguration(
            )), BaseMergedUnitParser(FrenchCurrencyParserConfiguration()))]
        ))
        # endregion

        # region Portuguese
        self.register_model('CurrencyModel', Culture.Portuguese, lambda options: CurrencyModel(
            [ExtractorParserModel(BaseMergedUnitExtractor(PortugueseCurrencyExtractorConfiguration(
            )), BaseMergedUnitParser(PortugueseCurrencyParserConfiguration()))]
        ))
        # endregion

        # region Spanish
        self.register_model('CurrencyModel', Culture.Spanish, lambda options: CurrencyModel(
            [ExtractorParserModel(BaseMergedUnitExtractor(SpanishCurrencyExtractorConfiguration(
            )), BaseMergedUnitParser(SpanishCurrencyParserConfiguration()))]
        ))
        # endregion

        # region Spanish Mexican
        self.register_model('CurrencyModel', Culture.SpanishMexican, lambda options: CurrencyModel(
            [ExtractorParserModel(BaseMergedUnitExtractor(SpanishCurrencyExtractorConfiguration(
            )), BaseMergedUnitParser(SpanishCurrencyParserConfiguration(culture_info=CultureInfo(Culture.SpanishMexican))))]
        ))
        # endregion

        # region Italian
        self.register_model('CurrencyModel', Culture.Italian, lambda options: CurrencyModel([
            ExtractorParserModel(
                BaseMergedUnitExtractor(
                    ItalianCurrencyExtractorConfiguration()),
                BaseMergedUnitParser(ItalianCurrencyParserConfiguration()))
        ]))
        # endregion

        # region German
        self.register_model('CurrencyModel', Culture.German, lambda options: CurrencyModel([
            ExtractorParserModel(
                BaseMergedUnitExtractor(
                    GermanCurrencyExtractorConfiguration()),
                BaseMergedUnitParser(GermanCurrencyParserConfiguration()))
        ]))
        # endregion

        # region Japanese
        self.register_model('CurrencyModel', Culture.Japanese, lambda options: CurrencyModel([
            ExtractorParserModel(
                BaseMergedUnitExtractor(
                    JapaneseCurrencyExtractorConfiguration()),
                BaseMergedUnitParser(JapaneseCurrencyParserConfiguration())),
            ExtractorParserModel(
                NumberWithUnitExtractor(
                    EnglishCurrencyExtractorConfiguration()),
                NumberWithUnitParser(EnglishCurrencyParserConfiguration()))
        ]))
        # endregion

        # region Catalan
        self.register_model('CurrencyModel', Culture.Catalan, lambda options: CurrencyModel([
            ExtractorParserModel(
                BaseMergedUnitExtractor(
                    CatalanCurrencyExtractorConfiguration()),
                BaseMergedUnitParser(CatalanCurrencyParserConfiguration()))
        ]))
        # endregion

        # region Arabic
        self.register_model('CurrencyModel', Culture.Arabic, lambda options: CurrencyModel([
            ExtractorParserModel(
                BaseMergedUnitExtractor(
                    ArabicCurrencyExtractorConfiguration()),
                BaseMergedUnitParser(ArabicCurrencyParserConfiguration()))
        ]))
        # endregion

    def get_currency_model(self, culture: str = None, fallback_to_default_culture: bool = True) -> Model:
        return self.get_model('CurrencyModel', culture, fallback_to_default_culture)


def recognize_currency(query: str, culture: str, options: NumberWithUnitOptions = NumberWithUnitOptions.NONE, fallback_to_default_culture: bool = True) -> List[ModelResult]:
    recognizer = NumberWithUnitRecognizer(culture, options)
    model = recognizer.get_currency_model(culture, fallback_to_default_culture)
    return model.parse(query)
