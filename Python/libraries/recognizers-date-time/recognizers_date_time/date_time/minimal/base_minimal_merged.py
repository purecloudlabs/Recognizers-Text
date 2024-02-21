from typing import List, Optional
from datetime import datetime

from recognizers_text.extractor import ExtractResult
from recognizers_date_time.date_time.constants import Constants
from recognizers_date_time.date_time.utilities import DateTimeOptions
from recognizers_date_time.date_time.base_merged import BaseMergedExtractor, BaseMergedParser
from recognizers_date_time.date_time.parsers import DateTimeParseResult


class BaseMinimalMergedExtractor(BaseMergedExtractor):
    @property
    def extractor_type_name(self) -> str:
        return Constants.SYS_DATETIME_MERGED

    def __init__(self, config, options: DateTimeOptions):
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

        result = sorted(result, key=lambda x: x.start)

        return result


class BaseMinimalMergedParser(BaseMergedParser):
    @property
    def parser_type_name(self) -> str:
        return Constants.SYS_DATETIME_MERGED

    def __init__(self, config, options: DateTimeOptions):
        super().__init__(config, options)

    def parse_result(self, source: ExtractResult, reference: datetime):
        if source.type == Constants.SYS_DATETIME_DATE:
            result = self.config.date_parser.parse(source, reference)
        elif source.type == Constants.SYS_DATETIME_TIME:
            result = self.config.time_parser.parse(source, reference)
        else:
            return None

        return result

    def parse(self, source: ExtractResult, reference: datetime = None) -> Optional[DateTimeParseResult]:
        if not reference:
            reference = datetime.now()

        result = self.parse_result(source, reference)
        if not result:
            return None

        if self.options & DateTimeOptions.SPLIT_DATE_AND_TIME and result.value and result.value.sub_date_time_entities:
            result.value = self._date_time_resolution_for_split(result)
        else:
            result = self.set_parse_result(
                result, has_before=False, has_after=False, has_since=False)

        return result
