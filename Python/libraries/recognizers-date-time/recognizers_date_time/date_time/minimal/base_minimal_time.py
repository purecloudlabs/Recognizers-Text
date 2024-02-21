from typing import List
from datetime import datetime

from recognizers_text.extractor import ExtractResult
from recognizers_date_time.date_time.base_time import BaseTimeExtractor, BaseTimeParser, TimeExtractorConfiguration, \
    TimeParserConfiguration
from recognizers_date_time.date_time.constants import Constants
from recognizers_date_time.date_time.utilities import DateTimeOptions, merge_all_tokens, TimeZoneUtility


class BaseMinimalTimeExtractor(BaseTimeExtractor):
    @property
    def extractor_type_name(self) -> str:
        return Constants.SYS_DATETIME_TIME

    def __init__(self, config: TimeExtractorConfiguration):
        super().__init__(config)

    def extract(self, source: str, reference: datetime = None) -> List[ExtractResult]:

        if reference is None:
            reference = datetime.now()

        tokens = self.basic_regex_match(source)

        result = merge_all_tokens(tokens, source, self.extractor_type_name)

        if (self.config.options & DateTimeOptions.ENABLE_PREVIEW) != 0:
            result = TimeZoneUtility().merge_time_zones(
                result,
                self.config.time_zone_extractor.extract(source, reference),
                source
            )

        return result


class BaseMinimalTimeParser(BaseTimeParser):

    def __init__(self, config: TimeParserConfiguration):
        super().__init__(config)
        self.config = config
