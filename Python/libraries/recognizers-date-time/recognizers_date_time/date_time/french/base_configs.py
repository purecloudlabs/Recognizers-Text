#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from ...resources.french_date_time import FrenchDateTime
from ..utilities import DateTimeUtilityConfiguration


class FrenchDateTimeUtilityConfiguration(DateTimeUtilityConfiguration):

    def __init__(self):
        super().__init__(FrenchDateTime())
