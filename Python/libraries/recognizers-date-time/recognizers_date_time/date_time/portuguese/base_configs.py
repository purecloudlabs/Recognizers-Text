#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from recognizers_date_time.date_time.base_date import DateTimeUtilityConfiguration
from recognizers_date_time.resources.portuguese_date_time import PortugueseDateTime


class PortugueseDateTimeUtilityConfiguration(DateTimeUtilityConfiguration):

    def __init__(self):
        super().__init__(PortugueseDateTime())
