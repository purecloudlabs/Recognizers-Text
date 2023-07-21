#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.

from typing import List, Dict, Callable
import re
from datetime import datetime

from recognizers_text.utilities import RegExpUtility
from ..utilities import DateUtils
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

    def get_swift_year(self, text: str) -> int:
        trimmed_text = text.strip().lower()
        swift = -10
        if trimmed_text.startswith('next'):
            swift = 1
        if trimmed_text.startswith('last'):
            swift = -1
        if trimmed_text.startswith('this'):
            swift = 0
        return swift

    def sanitize_holiday_token(self, holiday: str) -> str:
        return re.sub('[ \']', '', holiday)

    def __init__(self, config):
        super().__init__()
        self._holiday_regexes = [
            RegExpUtility.get_safe_reg_exp(CatalanDateTime.HolidayRegex)
        ]
        self._holiday_names = CatalanDateTime.HolidayNames

    def _init_holiday_funcs(self) -> Dict[str, Callable[[int], datetime]]:
        local = dict([
            ('maosbirthday', CatalanHolidayParserConfiguration.mao_birthday),
            ('yuandan', CatalanHolidayParserConfiguration.new_year),
            ('teachersday', CatalanHolidayParserConfiguration.teacher_day),
            ('singleday', CatalanHolidayParserConfiguration.singles_day),
            ('allsaintsday', CatalanHolidayParserConfiguration.halloween_day),
            ('youthday', CatalanHolidayParserConfiguration.youth_day),
            ('childrenday', CatalanHolidayParserConfiguration.children_day),
            ('femaleday', CatalanHolidayParserConfiguration.female_day),
            ('treeplantingday', CatalanHolidayParserConfiguration.tree_plant_day),
            ('arborday', CatalanHolidayParserConfiguration.tree_plant_day),
            ('girlsday', CatalanHolidayParserConfiguration.girls_day),
            ('whiteloverday', CatalanHolidayParserConfiguration.white_lover_day),
            ('loverday', CatalanHolidayParserConfiguration.valentines_day),
            ('christmas', CatalanHolidayParserConfiguration.christmas_day),
            ('xmas', CatalanHolidayParserConfiguration.christmas_day),
            ('newyear', CatalanHolidayParserConfiguration.new_year),
            ('newyearday', CatalanHolidayParserConfiguration.new_year),
            ('newyearsday', CatalanHolidayParserConfiguration.new_year),
            ('inaugurationday', CatalanHolidayParserConfiguration.inauguration_day),
            ('groundhougday', CatalanHolidayParserConfiguration.groundhog_day),
            ('valentinesday', CatalanHolidayParserConfiguration.valentines_day),
            ('stpatrickday', CatalanHolidayParserConfiguration.st_patrick_day),
            ('aprilfools', CatalanHolidayParserConfiguration.fool_day),
            ('stgeorgeday', CatalanHolidayParserConfiguration.st_george_day),
            ('mayday', CatalanHolidayParserConfiguration.may_day),
            ('cincodemayoday', CatalanHolidayParserConfiguration.cinco_de_mayo_day),
            ('baptisteday', CatalanHolidayParserConfiguration.baptiste_day),
            ('usindependenceday', CatalanHolidayParserConfiguration.usa_independence_day),
            ('independenceday', CatalanHolidayParserConfiguration.usa_independence_day),
            ('bastilleday', CatalanHolidayParserConfiguration.bastille_day),
            ('halloweenday', CatalanHolidayParserConfiguration.halloween_day),
            ('allhallowday', CatalanHolidayParserConfiguration.all_hallow_day),
            ('allsoulsday', CatalanHolidayParserConfiguration.all_souls_day),
            ('guyfawkesday', CatalanHolidayParserConfiguration.guy_fawkes_day),
            ('veteransday', CatalanHolidayParserConfiguration.veterans_day),
            ('christmaseve', CatalanHolidayParserConfiguration.christmas_eve),
            ('newyeareve', CatalanHolidayParserConfiguration.new_year_eve),
            ('easterday', CatalanHolidayParserConfiguration.easter_day),
            ('juneteenth', CatalanHolidayParserConfiguration.juneteenth),
        ])

        return {**super()._init_holiday_funcs(), **local}

    @staticmethod
    def mao_birthday(year: int) -> datetime:
        return datetime(year, 12, 26)

    @staticmethod
    def new_year(year: int) -> datetime:
        return datetime(year, 1, 1)

    @staticmethod
    def teacher_day(year: int) -> datetime:
        return datetime(year, 9, 10)

    @staticmethod
    def singles_day(year: int) -> datetime:
        return datetime(year, 11, 11)

    @staticmethod
    def halloween_day(year: int) -> datetime:
        return datetime(year, 10, 31)

    @staticmethod
    def youth_day(year: int) -> datetime:
        return datetime(year, 5, 4)

    @staticmethod
    def children_day(year: int) -> datetime:
        return datetime(year, 6, 1)

    @staticmethod
    def female_day(year: int) -> datetime:
        return datetime(year, 3, 8)

    @staticmethod
    def tree_plant_day(year: int) -> datetime:
        return datetime(year, 3, 12)

    @staticmethod
    def girls_day(year: int) -> datetime:
        return datetime(year, 3, 7)

    @staticmethod
    def white_lover_day(year: int) -> datetime:
        return datetime(year, 3, 14)

    @staticmethod
    def valentines_day(year: int) -> datetime:
        return datetime(year, 2, 14)

    @staticmethod
    def christmas_day(year: int) -> datetime:
        return datetime(year, 12, 25)

    @staticmethod
    def inauguration_day(year: int) -> datetime:
        return datetime(year, 1, 20)

    @staticmethod
    def groundhog_day(year: int) -> datetime:
        return datetime(year, 2, 2)

    @staticmethod
    def st_patrick_day(year: int) -> datetime:
        return datetime(year, 3, 17)

    @staticmethod
    def fool_day(year: int) -> datetime:
        return datetime(year, 4, 1)

    @staticmethod
    def st_george_day(year: int) -> datetime:
        return datetime(year, 4, 23)

    @staticmethod
    def may_day(year: int) -> datetime:
        return datetime(year, 5, 1)

    @staticmethod
    def cinco_de_mayo_day(year: int) -> datetime:
        return datetime(year, 5, 5)

    @staticmethod
    def baptiste_day(year: int) -> datetime:
        return datetime(year, 6, 24)

    @staticmethod
    def usa_independence_day(year: int) -> datetime:
        return datetime(year, 7, 4)

    @staticmethod
    def bastille_day(year: int) -> datetime:
        return datetime(year, 7, 14)

    @staticmethod
    def all_hallow_day(year: int) -> datetime:
        return datetime(year, 11, 1)

    @staticmethod
    def all_souls_day(year: int) -> datetime:
        return datetime(year, 11, 2)

    @staticmethod
    def guy_fawkes_day(year: int) -> datetime:
        return datetime(year, 11, 5)

    @staticmethod
    def veterans_day(year: int) -> datetime:
        return datetime(year, 11, 11)

    @staticmethod
    def christmas_eve(year: int) -> datetime:
        return datetime(year, 12, 24)

    @staticmethod
    def new_year_eve(year: int) -> datetime:
        return datetime(year, 12, 31)

    @staticmethod
    def easter_day(year: int) -> datetime:
        return DateUtils.min_value

    @staticmethod
    def juneteenth(year: int) -> datetime:
        return datetime(year, 6, 19)
