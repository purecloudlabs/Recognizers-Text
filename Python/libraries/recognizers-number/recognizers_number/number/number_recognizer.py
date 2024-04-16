#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from enum import IntFlag
from typing import List

from recognizers_number.number.arabic.extractors import ArabicOrdinalExtractor, \
    ArabicNumberExtractor, ArabicMergedNumberExtractor
from recognizers_number.number.arabic.parsers import ArabicNumberParserConfiguration
from recognizers_text import Culture, Recognizer, Model
from recognizers_number.culture import CultureInfo
from recognizers_number.number.models import NumberMode, NumberModel, OrdinalModel, ModelResult
from recognizers_number.number.parser_factory import ParserType, AgnosticNumberParserFactory
from recognizers_number.number.english.extractors import EnglishNumberExtractor, EnglishOrdinalExtractor, \
    EnglishMergedNumberExtractor
from recognizers_number.number.english.parsers import EnglishNumberParserConfiguration
from recognizers_number.number.spanish.extractors import SpanishNumberExtractor, SpanishOrdinalExtractor
from recognizers_number.number.chinese.extractors import ChineseNumberExtractor, ChineseOrdinalExtractor
from recognizers_number.number.chinese.parsers import ChineseNumberParserConfiguration
from recognizers_number.number.dutch.extractors import DutchOrdinalExtractor, DutchMergedNumberExtractor
from recognizers_number.number.dutch.parsers import DutchNumberParserConfiguration
from recognizers_number.number.japanese.extractors import JapaneseNumberExtractor, JapaneseOrdinalExtractor
from recognizers_number.number.japanese.parsers import JapaneseNumberParserConfiguration
from recognizers_number.number.spanish.parsers import SpanishNumberParserConfiguration
from recognizers_number.number.portuguese.extractors import PortugueseNumberExtractor, PortugueseOrdinalExtractor
from recognizers_number.number.portuguese.parsers import PortugueseNumberParserConfiguration
from recognizers_number.number.french.extractors import FrenchNumberExtractor, FrenchOrdinalExtractor
from recognizers_number.number.french.parsers import FrenchNumberParserConfiguration
from recognizers_number.number.german.extractors import GermanMergedNumberExtractor, GermanOrdinalExtractor
from recognizers_number.number.german.parsers import GermanNumberParserConfiguration
from recognizers_number.number.italian.extractors import ItalianMergedNumberExtractor, ItalianOrdinalExtractor
from recognizers_number.number.italian.parsers import ItalianNumberParserConfiguration
from recognizers_number.number.catalan.extractors import CatalanNumberExtractor, CatalanOrdinalExtractor
from recognizers_number.number.catalan.parsers import CatalanNumberParserConfiguration


class NumberOptions(IntFlag):
    NONE = 0


class NumberRecognizer(Recognizer[NumberOptions]):
    def __init__(self, target_culture: str = None, options: NumberOptions = NumberOptions.NONE, lazy_initialization: bool = True):
        if options < NumberOptions.NONE or options > NumberOptions.NONE:
            raise ValueError()
        super().__init__(target_culture, options, lazy_initialization)

    def initialize_configuration(self):
        # region English
        self.register_model('NumberModel', Culture.English, lambda options: NumberModel(
            AgnosticNumberParserFactory.get_parser(
                ParserType.NUMBER, EnglishNumberParserConfiguration()),
            EnglishMergedNumberExtractor(NumberMode.PURE_NUMBER)
        ))
        self.register_model('OrdinalModel', Culture.English, lambda options: OrdinalModel(
            AgnosticNumberParserFactory.get_parser(
                ParserType.ORDINAL, EnglishNumberParserConfiguration()),
            EnglishOrdinalExtractor()
        ))
        # endregion

        # region German
        self.register_model('NumberModel', Culture.German, lambda options: NumberModel(
            AgnosticNumberParserFactory.get_parser(
                ParserType.NUMBER, GermanNumberParserConfiguration()),
            GermanMergedNumberExtractor(NumberMode.PURE_NUMBER)
        ))
        self.register_model('OrdinalModel', Culture.German, lambda options: OrdinalModel(
            AgnosticNumberParserFactory.get_parser(
                ParserType.ORDINAL, GermanNumberParserConfiguration()),
            GermanOrdinalExtractor()
        ))
        # endregion

        # region Dutch
        self.register_model('NumberModel', Culture.Dutch, lambda options: NumberModel(
            AgnosticNumberParserFactory.get_parser(
                ParserType.NUMBER, DutchNumberParserConfiguration()),
            DutchMergedNumberExtractor(NumberMode.PURE_NUMBER)
        ))
        self.register_model('OrdinalModel', Culture.Dutch, lambda options: OrdinalModel(
            AgnosticNumberParserFactory.get_parser(
                ParserType.ORDINAL, DutchNumberParserConfiguration()),
            DutchOrdinalExtractor()
        ))
        # endregion

        # region Chinese
        self.register_model('NumberModel', Culture.Chinese, lambda options: NumberModel(
            AgnosticNumberParserFactory.get_parser(
                ParserType.NUMBER, ChineseNumberParserConfiguration()),
            ChineseNumberExtractor()
        ))
        self.register_model('OrdinalModel', Culture.Chinese, lambda options: OrdinalModel(
            AgnosticNumberParserFactory.get_parser(
                ParserType.ORDINAL, ChineseNumberParserConfiguration()),
            ChineseOrdinalExtractor()
        ))
        # endregion

        # region Japanese
        self.register_model('NumberModel', Culture.Japanese, lambda options: NumberModel(
            AgnosticNumberParserFactory.get_parser(
                ParserType.NUMBER, JapaneseNumberParserConfiguration()),
            JapaneseNumberExtractor()
        ))
        self.register_model('OrdinalModel', Culture.Japanese, lambda options: OrdinalModel(
            AgnosticNumberParserFactory.get_parser(
                ParserType.ORDINAL, JapaneseNumberParserConfiguration()),
            JapaneseOrdinalExtractor()
        ))
        # endregion

        # region Spanish
        self.register_model('NumberModel', Culture.Spanish, lambda options: NumberModel(
            AgnosticNumberParserFactory.get_parser(
                ParserType.NUMBER, SpanishNumberParserConfiguration()),
            SpanishNumberExtractor(NumberMode.PURE_NUMBER)
        ))
        self.register_model('OrdinalModel', Culture.Spanish, lambda options: OrdinalModel(
            AgnosticNumberParserFactory.get_parser(
                ParserType.ORDINAL, SpanishNumberParserConfiguration()),
            SpanishOrdinalExtractor()
        ))
        # endregion

        # region Spanish Mexican
        self.register_model('NumberModel', Culture.SpanishMexican, lambda options: NumberModel(
            AgnosticNumberParserFactory.get_parser(
                ParserType.NUMBER, SpanishNumberParserConfiguration(CultureInfo(Culture.SpanishMexican))),
            SpanishNumberExtractor(NumberMode.PURE_NUMBER)
        ))
        self.register_model('OrdinalModel', Culture.SpanishMexican, lambda options: OrdinalModel(
            AgnosticNumberParserFactory.get_parser(
                ParserType.ORDINAL, SpanishNumberParserConfiguration(CultureInfo(Culture.SpanishMexican))),
            SpanishOrdinalExtractor()
        ))
        # endregion

        # region Portuguese
        self.register_model('NumberModel', Culture.Portuguese, lambda options: NumberModel(
            AgnosticNumberParserFactory.get_parser(
                ParserType.NUMBER, PortugueseNumberParserConfiguration()),
            PortugueseNumberExtractor(NumberMode.PURE_NUMBER)
        ))
        self.register_model('OrdinalModel', Culture.Portuguese, lambda options: OrdinalModel(
            AgnosticNumberParserFactory.get_parser(
                ParserType.ORDINAL, PortugueseNumberParserConfiguration()),
            PortugueseOrdinalExtractor()
        ))
        # endregion

        # region French
        self.register_model('NumberModel', Culture.French, lambda options: NumberModel(
            AgnosticNumberParserFactory.get_parser(
                ParserType.NUMBER, FrenchNumberParserConfiguration()),
            FrenchNumberExtractor(NumberMode.PURE_NUMBER)
        ))
        self.register_model('OrdinalModel', Culture.French, lambda options: OrdinalModel(
            AgnosticNumberParserFactory.get_parser(
                ParserType.ORDINAL, FrenchNumberParserConfiguration()),
            FrenchOrdinalExtractor()
        ))
        # endregion

        # region Italian
        self.register_model('NumberModel', Culture.Italian, lambda options: NumberModel(
            AgnosticNumberParserFactory.get_parser(
                ParserType.NUMBER, ItalianNumberParserConfiguration()),
            ItalianMergedNumberExtractor(NumberMode.PURE_NUMBER)
        ))
        self.register_model('OrdinalModel', Culture.Italian, lambda options: OrdinalModel(
            AgnosticNumberParserFactory.get_parser(
                ParserType.ORDINAL, ItalianNumberParserConfiguration()),
            ItalianOrdinalExtractor()
        ))
        # endregion

        # region Catalan
        self.register_model('NumberModel', Culture.Catalan, lambda options: NumberModel(
            AgnosticNumberParserFactory.get_parser(
                ParserType.NUMBER, CatalanNumberParserConfiguration()),
            CatalanNumberExtractor(NumberMode.PURE_NUMBER)
        ))
        self.register_model('OrdinalModel', Culture.Catalan, lambda options: OrdinalModel(
            AgnosticNumberParserFactory.get_parser(
                ParserType.ORDINAL, CatalanNumberParserConfiguration()),
            CatalanOrdinalExtractor()
        ))
        # endregion

        # region Arabic
        self.register_model('NumberModel', Culture.Arabic, lambda options: NumberModel(
            AgnosticNumberParserFactory.get_parser(
                ParserType.NUMBER, ArabicNumberParserConfiguration()),
            ArabicMergedNumberExtractor(NumberMode.PURE_NUMBER)
        ))
        self.register_model('OrdinalModel', Culture.Arabic, lambda options: OrdinalModel(
            AgnosticNumberParserFactory.get_parser(
                ParserType.ORDINAL, ArabicNumberParserConfiguration()),
            ArabicOrdinalExtractor()
        ))
        # endregion


    def get_number_model(self, culture: str = None, fallback_to_default_culture: bool = True) -> Model:
        return self.get_model('NumberModel', culture, fallback_to_default_culture)

    def get_ordinal_model(self, culture: str = None, fallback_to_default_culture: bool = True) -> Model:
        return self.get_model('OrdinalModel', culture, fallback_to_default_culture)


def recognize_number(query: str, culture: str, options: NumberOptions = NumberOptions.NONE, fallback_to_default_culture: bool = True) -> List[ModelResult]:
    recognizer = NumberRecognizer(culture, options)
    model = recognizer.get_number_model(culture, fallback_to_default_culture)
    return model.parse(query)


def recognize_ordinal(query: str, culture: str, options: NumberOptions = NumberOptions.NONE, fallback_to_default_culture: bool = True) -> List[ModelResult]:
    recognizer = NumberRecognizer(culture, options)
    model = recognizer.get_ordinal_model(culture, fallback_to_default_culture)
    return model.parse(query)
