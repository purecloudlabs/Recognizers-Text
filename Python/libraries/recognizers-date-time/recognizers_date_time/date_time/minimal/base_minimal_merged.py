from typing import List
from datetime import datetime

from recognizers_text.extractor import ExtractResult
from recognizers_date_time.date_time.constants import Constants
from recognizers_date_time.date_time.utilities import DateTimeOptions
from recognizers_date_time.date_time.base_minimal_merged import MinimalMergedExtractorConfiguration, \
    MinimalMergedParserConfiguration
from recognizers_date_time.date_time.base_merged import BaseMergedExtractor, BaseMergedParser


class BaseMinimalMergedExtractor(BaseMergedExtractor):
    @property
    def extractor_type_name(self) -> str:
        return Constants.SYS_DATETIME_MERGED

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

        # this should be at the end since if need the extractor to determine the previous text contains time or not
        result = self.add_to(
            result, self.number_ending_regex_match(source, result), source)

        result = sorted(result, key=lambda x: x.start)

        return result


class BaseMinimalMergedParser(BaseMergedParser):
    @property
    def parser_type_name(self) -> str:
        return Constants.SYS_DATETIME_MERGED

    def __init__(self, config: MinimalMergedParserConfiguration, options: DateTimeOptions):
        super().__init__(config, options)

    def parse_result(self, source: ExtractResult, reference: datetime):
        if source.type == Constants.SYS_DATETIME_DATE:
            result = self.config.date_parser.parse(source, reference)
        elif source.type == Constants.SYS_DATETIME_TIME:
            result = self.config.time_parser.parse(source, reference)
        else:
            return None

        return result
