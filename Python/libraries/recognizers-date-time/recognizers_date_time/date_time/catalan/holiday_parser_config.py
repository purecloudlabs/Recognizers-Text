#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from typing import List, Dict, Callable
from datetime import datetime

from recognizers_text.utilities import RegExpUtility
from ..utilities import DateUtils, HolidayFunctions
from ..base_holiday import BaseHolidayParserConfiguration
from ...resources.catalan_date_time import CatalanDateTime


class CatalanHolidayParserConfiguration(BaseHolidayParserConfiguration):
    @property
    def holiday_names(self) -> Dict[str, List[str]]:
        return self._holiday_names

    @property
    def holiday_regex_list(self) -> List[str]:
        return self._holiday_regexes

    @property
    def holiday_func_dictionary(self) -> Dict[str, Callable[[int], datetime]]:
        return self._holiday_func_dictionary

    def __init__(self, config):
        super().__init__()
        self._holiday_regexes = [
            RegExpUtility.get_safe_reg_exp(CatalanDateTime.HolidayRegex1),
            RegExpUtility.get_safe_reg_exp(CatalanDateTime.HolidayRegex2),
            RegExpUtility.get_safe_reg_exp(CatalanDateTime.HolidayRegex3)
        ]
        self._holiday_names = CatalanDateTime.HolidayNames
        self._variable_holidays_timex_dictionary = CatalanDateTime.VariableHolidaysTimexDictionary

        self.next_prefix_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.NextPrefixRegex)
        self.previous_prefix_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.PreviousPrefixRegex)
        self.this_prefix_regex = RegExpUtility.get_safe_reg_exp(
            CatalanDateTime.ThisPrefixRegex)

    def _init_holiday_funcs(self) -> Dict[str, Callable[[int], datetime]]:
        local = dict([
            ('padres', CatalanHolidayParserConfiguration.fathers_day),
            ('madres', CatalanHolidayParserConfiguration.mothers_day),
            ('acciondegracias', CatalanHolidayParserConfiguration.thanksgiving_day),
            ('trabajador', CatalanHolidayParserConfiguration.international_workers_day),
            ('delaraza', CatalanHolidayParserConfiguration.columbus_day),
            ('memoria', CatalanHolidayParserConfiguration.memorial_day),
            ('pascuas', CatalanHolidayParserConfiguration.easter_day),
            ('navidad', CatalanHolidayParserConfiguration.christmas_day),
            ('nochebuena', CatalanHolidayParserConfiguration.christmas_eve),
            ('añonuevo', CatalanHolidayParserConfiguration.new_year),
            ('nochevieja', CatalanHolidayParserConfiguration.new_year_eve),
            ('yuandan', CatalanHolidayParserConfiguration.new_year),
            ('maestro', CatalanHolidayParserConfiguration.teacher_day),
            ('todoslossantos', CatalanHolidayParserConfiguration.halloween_day),
            ('niño', CatalanHolidayParserConfiguration.children_day),
            ('mujer', CatalanHolidayParserConfiguration.female_day)
        ])

        return {**super()._init_holiday_funcs(), **local}

    @staticmethod
    def new_year(year: int) -> datetime:
        return datetime(year, 1, 1)

    @staticmethod
    def new_year_eve(year: int) -> datetime:
        return datetime(year, 12, 31)

    @staticmethod
    def christmas_day(year: int) -> datetime:
        return datetime(year, 12, 25)

    @staticmethod
    def christmas_eve(year: int) -> datetime:
        return datetime(year, 12, 24)

    @staticmethod
    def female_day(year: int) -> datetime:
        return datetime(year, 3, 8)

    @staticmethod
    def children_day(year: int) -> datetime:
        return datetime(year, 6, 1)

    @staticmethod
    def halloween_day(year: int) -> datetime:
        return datetime(year, 10, 31)

    @staticmethod
    def teacher_day(year: int) -> datetime:
        return datetime(year, 9, 11)

    @staticmethod
    def easter_day(year: int) -> datetime:
        return HolidayFunctions.calculate_holiday_by_easter(year)

    def get_swift_year(self, text: str) -> int:
        trimmed_text = text.strip().lower()
        swift = -10

        if self.next_prefix_regex.search(trimmed_text):
            swift = 1

        if self.previous_prefix_regex.search(trimmed_text):
            swift = -1

        if self.this_prefix_regex.search(trimmed_text):
            swift = 0

        return swift

    def sanitize_holiday_token(self, holiday: str) -> str:
        return holiday.replace(' ', '').replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u')
