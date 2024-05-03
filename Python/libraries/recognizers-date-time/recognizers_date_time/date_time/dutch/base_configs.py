#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from ...resources.dutch_date_time import DutchDateTime
from ..base_date import DateTimeUtilityConfiguration


class DutchDateTimeUtilityConfiguration(DateTimeUtilityConfiguration):

    def __init__(self):
        super().__init__(DutchDateTime())
