from recognizers_date_time.resources.arabic_date_time import ArabicDateTime
from recognizers_date_time.date_time.base_date import DateTimeUtilityConfiguration


class ArabicDateTimeUtilityConfiguration(DateTimeUtilityConfiguration):

    def __init__(self):
        super().__init__(ArabicDateTime())
