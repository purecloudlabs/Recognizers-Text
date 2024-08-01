from recognizers_date_time.date_time.utilities import DateTimeUtilityConfiguration
from recognizers_date_time.resources.catalan_date_time import CatalanDateTime


class CatalanDateTimeUtilityConfiguration(DateTimeUtilityConfiguration):

    def __init__(self):
        super().__init__(CatalanDateTime())
