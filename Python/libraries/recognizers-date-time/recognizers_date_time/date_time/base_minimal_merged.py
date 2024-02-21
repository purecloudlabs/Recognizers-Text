from abc import abstractmethod, ABC
from typing import List, Pattern
from datetime import datetime

from recognizers_text.extractor import Extractor, ExtractResult
from .extractors import DateTimeExtractor
from .base_date import BaseDateParser
from .base_time import BaseTimeParser
from .utilities import DateTimeOptions
from recognizers_date_time.date_time.base_merged import BaseMergedExtractor, BaseMergedParser


class MinimalMergedExtractorConfiguration:
    @property
    @abstractmethod
    def ambiguous_range_modifier_prefix(self) -> Pattern:
        raise NotImplementedError

    @property
    @abstractmethod
    def number_ending_pattern(self) -> Pattern:
        raise NotImplementedError

    @property
    @abstractmethod
    def date_extractor(self) -> DateTimeExtractor:
        raise NotImplementedError

    @property
    @abstractmethod
    def time_extractor(self) -> DateTimeExtractor:
        raise NotImplementedError

    @property
    @abstractmethod
    def date_time_extractor(self) -> DateTimeExtractor:
        raise NotImplementedError

    @property
    @abstractmethod
    def integer_extractor(self) -> Extractor:
        raise NotImplementedError

    @property
    @abstractmethod
    def equal_regex(self) -> Pattern:
        raise NotImplementedError

    @property
    @abstractmethod
    def check_both_before_after(self):
        raise NotImplementedError


class MinimalMergedExtractor(BaseMergedExtractor):

    def __init__(self, config: MinimalMergedExtractorConfiguration, options: DateTimeOptions):
        super().__init__(config, options)

    def extract(self, source: str, reference: datetime = None) -> List[ExtractResult]:
        if reference is None:
            reference = datetime.now()

        result: List[ExtractResult] = list()

        # The order is important, since there can be conflicts in merging
        result = self.add_to(
            result, self.config.date_extractor.extract(source, reference), source)
        result = self.add_to(
            result, self.config.time_extractor.extract(source, reference), source)
        result = self.add_to(
            result, self.config.date_time_extractor.extract(source, reference), source)

        # this should be at the end since if need the extractor to determine the previous text contains time or not
        result = self.add_to(
            result, self.number_ending_regex_match(source, result), source)

        result = sorted(result, key=lambda x: x.start)

        return result


class MinimalMergedParserConfiguration(ABC):
    @property
    @abstractmethod
    def before_regex(self) -> Pattern:
        raise NotImplementedError

    @property
    @abstractmethod
    def after_regex(self) -> Pattern:
        raise NotImplementedError

    @property
    @abstractmethod
    def since_regex(self) -> Pattern:
        raise NotImplementedError

    @property
    @abstractmethod
    def around_regex(self) -> Pattern:
        raise NotImplementedError

    @property
    @abstractmethod
    def equal_regex(self) -> Pattern:
        raise NotImplementedError

    @property
    @abstractmethod
    def year_regex(self) -> Pattern:
        raise NotImplementedError

    @property
    @abstractmethod
    def suffix_after(self) -> Pattern:
        raise NotImplementedError

    @property
    @abstractmethod
    def date_parser(self) -> BaseDateParser:
        raise NotImplementedError

    @property
    @abstractmethod
    def time_parser(self) -> BaseTimeParser:
        raise NotImplementedError

    @property
    @abstractmethod
    def date_time_parser(self) -> BaseTimeParser:
        raise NotImplementedError


class MinimalMergedParser(BaseMergedParser):

    def __init__(self, config: MinimalMergedParserConfiguration, options: DateTimeOptions):
        super().__init__(config, options)
