#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from typing import Pattern
from recognizers_text.utilities import RegExpUtility
from recognizers_date_time.date_time.base_date import DateTimeUtilityConfiguration
from recognizers_date_time.resources.english_date_time import EnglishDateTime


class EnglishDateTimeUtilityConfiguration(DateTimeUtilityConfiguration):

    def __init__(self):
        super().__init__(EnglishDateTime())