#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from ...resources.italian_date_time import ItalianDateTime
from ..base_date import DateTimeUtilityConfiguration


class ItalianDateTimeUtilityConfiguration(DateTimeUtilityConfiguration):

    def __init__(self):
        super().__init__(ItalianDateTime())
