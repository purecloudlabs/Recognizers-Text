#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from ...resources.german_date_time import GermanDateTime
from ..utilities import DateTimeUtilityConfiguration


class GermanDateTimeUtilityConfiguration(DateTimeUtilityConfiguration):

    def __init__(self):
        super().__init__(GermanDateTime())
