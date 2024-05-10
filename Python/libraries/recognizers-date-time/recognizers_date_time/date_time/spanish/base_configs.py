#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from recognizers_date_time.date_time.utilities import DateTimeUtilityConfiguration
from recognizers_date_time.resources.spanish_date_time import SpanishDateTime


class SpanishDateTimeUtilityConfiguration(DateTimeUtilityConfiguration):

    def __init__(self):
        super().__init__(SpanishDateTime())
