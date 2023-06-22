import calendar
from datetime import datetime, timedelta
from abc import abstractmethod

from datedelta import datedelta
from regex import regex

from ..utilities import Token
from typing import List, Pattern, Dict, Optional

from recognizers_number import Constants as Num_Constants
from recognizers_date_time import Constants as Date_Constants
from recognizers_date_time import DateTimeOptionsConfiguration, DateTimeExtractor, DateTimeParser, \
    ExtractResultExtension, merge_all_tokens, BaseDateExtractor, BaseDateParser, \
    CJKCommonDateTimeParserConfiguration, DateTimeUtilityConfiguration, DateUtils, DateTimeParseResult, \
    TimeTypeConstants, DateTimeFormatUtil, DateTimeResolutionResult, DateTimeOptions, DurationParsingUtil, DayOfWeek
from recognizers_text import ExtractResult, RegExpUtility, MetaData


class CJKDateExtractorConfiguration(DateTimeOptionsConfiguration):

    @property
    @abstractmethod
    def date_regex_list(self) -> List[Pattern]:
        raise NotImplementedError

    @property
    @abstractmethod
    def implicit_date_list(self) -> List[Pattern]:
        raise NotImplementedError

    @property
    @abstractmethod
    def datetime_period_unit_regex(self) -> Pattern:
        raise NotImplementedError

    @property
    @abstractmethod
    def before_regex(self) -> Pattern:
        raise NotImplementedError

    @property
    @abstractmethod
    def after_regex(self) -> Pattern:
        raise NotImplementedError

    @property
    @abstractmethod
    def week_day_start_end(self) -> Pattern:
        raise NotImplementedError

    @property
    @abstractmethod
    def range_connector_symbol_regex(self) -> Pattern:
        raise NotImplementedError

    @property
    @abstractmethod
    def duration_extractor(self) -> DateTimeExtractor:
        raise NotImplementedError

    @property
    @abstractmethod
    def ambiguity_date_time_filters(self) -> Dict[Pattern, Pattern]:
        raise NotImplementedError


class BaseCJKDateExtractor(DateTimeExtractor):
    @property
    def extractor_type_name(self) -> str:
        return Date_Constants.SYS_DATETIME_TIME

    def __init__(self, config: CJKDateExtractorConfiguration):
        self.config = config

    def extract(self, source: str, reference: datetime = None) -> List[ExtractResult]:
        if reference is None:
            reference = datetime.now()
        tokens = []
        tokens.extend(self.basic_regex_match(source))
        tokens.extend(self.implicit_date(source))
        tokens.extend(self.duration_with_ago_and_later(source, reference))
        result = merge_all_tokens(tokens, source, self.extractor_type_name)

        result = ExtractResultExtension.filter_ambiguity(result, source, self.config.ambiguity_date_time_filters)

        return result

    def basic_regex_match(self, source: str) -> List[Token]:
        ret: List[Token] = list()

        for regexp in self.config.date_regex_list:

            matches = list(regexp.finditer(source))
            if matches:
                for match in matches:

                    # some match might be part of the date range entity, and might be split in a wrong way
                    if BaseDateExtractor.validate_match(match, source):
                        ret.append(Token(match.index, source.index(match.group()) + match.end() - match.start()))

        return ret

    def implicit_date(self, source: str) -> List[Token]:
        ret: List[Token] = list()

        for regexp in self.config.implicit_date_list:

            matches = list(regexp.finditer(source))
            if matches:
                for match in matches:
                    ret.append(Token(match.index, source.index(match.group()) + match.end() - match.start()))

        return ret

    # process case like "三天前" "两个月前"
    def duration_with_ago_and_later(self, source: str, reference: datetime) -> List[Token]:
        ret: List[Token] = list()
        duration_extracted_results = self.config.duration_extractor.extract(source, reference)

        for extracted_result in duration_extracted_results:

            # Only handles date durations here
            # Cases with dateTime durations will be handled in DateTime Extractor
            if self.config.datetime_period_unit_regex.search(extracted_result.text):
                continue

            pos = extracted_result.start + len(extracted_result)

            if pos < len(source):
                suffix = source[pos:]
                match = self.config.before_regex.search(suffix)

                if not match:
                    match = self.config.after_regex.search(suffix)

                if match and suffix.strip().endswith(match.group()):
                    meta_data = MetaData()
                    meta_data.is_duration_date_with_weekday = True
                    ret.append(Token(extracted_result.start, pos + match.index, meta_data))

        ret.extend(self.extend_with_week_day(ret, source))

        return ret

    def extend_with_week_day(self, ret: List[Token], source: str):
        new_ret: List[Token] = list()

        for er in ret:
            before_str = source[0: er.start]
            after_str = source[er.end:]

            before_match = self.config.week_day_start_end.search(before_str)
            after_match = self.config.week_day_start_end.search(after_str)

            if before_match or after_match:
                start = before_match.index if before_match else er.start
                end = after_match.index if after_match else er.end

                meta_data = MetaData()
                meta_data.is_duration_date_with_weekday = True
                ret.append(Token(start, end, meta_data))

        return new_ret


class CJKDateParserConfiguration(CJKCommonDateTimeParserConfiguration):

    def __init__(self, options=DateTimeOptions.NONE, dmy_date_format=False):
        super().__init__(options, dmy_date_format)

    @property
    @abstractmethod
    def cardinal_extractor(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def integer_extractor(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def ordinal_extractor(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def number_parser(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def date_extractor(self) -> DateTimeExtractor:
        raise NotImplementedError

    @property
    @abstractmethod
    def time_extractor(self) -> DateTimeExtractor:
        raise NotImplementedError

    @property
    @abstractmethod
    def date_time_extractor(self) -> DateTimeExtractor:
        raise NotImplementedError

    @property
    @abstractmethod
    def duration_extractor(self) -> DateTimeExtractor:
        raise NotImplementedError

    @property
    @abstractmethod
    def date_period_extractor(self) -> DateTimeExtractor:
        raise NotImplementedError

    @property
    @abstractmethod
    def time_period_extractor(self) -> DateTimeExtractor:
        raise NotImplementedError

    @property
    @abstractmethod
    def date_time_period_extractor(self) -> DateTimeExtractor:
        raise NotImplementedError

    @property
    @abstractmethod
    def set_extractor(self) -> DateTimeExtractor:
        raise NotImplementedError

    @property
    @abstractmethod
    def holiday_extractor(self) -> DateTimeExtractor:
        raise NotImplementedError

    @property
    @abstractmethod
    def date_parser(self) -> BaseDateParser:
        raise NotImplementedError

    @property
    @abstractmethod
    def time_parser(self) -> DateTimeParser:
        raise NotImplementedError

    @property
    @abstractmethod
    def date_time_parser(self) -> DateTimeParser:
        raise NotImplementedError

    @property
    @abstractmethod
    def duration_parser(self) -> DateTimeParser:
        raise NotImplementedError

    @property
    @abstractmethod
    def date_period_parser(self) -> DateTimeParser:
        raise NotImplementedError

    @property
    @abstractmethod
    def time_period_parser(self) -> DateTimeParser:
        raise NotImplementedError

    @property
    @abstractmethod
    def date_time_period_parser(self) -> DateTimeParser:
        raise NotImplementedError

    @property
    @abstractmethod
    def set_parser(self) -> DateTimeParser:
        raise NotImplementedError

    @property
    @abstractmethod
    def holiday_parser(self) -> DateTimeParser:
        raise NotImplementedError

    @property
    @abstractmethod
    def date_time_alt_parser(self) -> DateTimeParser:
        raise NotImplementedError

    @property
    @abstractmethod
    def time_zone_parser(self) -> DateTimeParser:
        raise NotImplementedError

    @property
    @abstractmethod
    def month_of_year(self) -> Dict[str, int]:
        raise NotImplementedError

    @property
    @abstractmethod
    def numbers(self) -> Dict[str, int]:
        raise NotImplementedError

    @property
    @abstractmethod
    def double_numbers(self) -> Dict[str, int]:
        raise NotImplementedError

    @property
    @abstractmethod
    def unit_value_map(self) -> Dict[str, int]:
        raise NotImplementedError

    @property
    @abstractmethod
    def season_map(self) -> Dict[str, str]:
        raise NotImplementedError

    @property
    @abstractmethod
    def special_year_prefixes_map(self) -> Dict[str, str]:
        raise NotImplementedError

    @property
    @abstractmethod
    def unit_map(self) -> Dict[str, str]:
        raise NotImplementedError

    @property
    @abstractmethod
    def cardinal_map(self) -> Dict[str, int]:
        raise NotImplementedError

    @property
    @abstractmethod
    def day_of_month(self) -> Dict[str, int]:
        return NotImplementedError

    @property
    @abstractmethod
    def day_of_week(self) -> Dict[str, int]:
        raise NotImplementedError

    @property
    @abstractmethod
    def written_decades(self) -> Dict[str, int]:
        raise NotImplementedError

    @property
    @abstractmethod
    def special_decade_cases(self) -> Dict[str, int]:
        raise NotImplementedError

    @property
    @abstractmethod
    def special_date(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def utility_configuration(self) -> DateTimeUtilityConfiguration:
        raise NotImplementedError

    @property
    @abstractmethod
    def date_regex_list(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def next_re(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def last_re(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def special_day_regex(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def get_swift_day(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def duration_relative_duration_unit_regex(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def special_day_with_num_regex(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def week_day_and_day_regex(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def next_regex(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def this_regex(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def last_regex(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def week_day_regex(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def month_max_days(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def week_day_of_month_regex(self):
        raise NotImplementedError

    @abstractmethod
    def is_cardinal_last(self, source: str) -> bool:
        raise NotImplementedError

    @abstractmethod
    def next_month_regex(self, source: str) -> bool:
        raise NotImplementedError

    @abstractmethod
    def get_swift_month(self, trimmed_source) -> int:
        raise NotImplementedError

    @property
    @abstractmethod
    def lunar_regex(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def unit_regex(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def before_regex(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def after_regex(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def dynasty_year_regex(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def dynasty_start_year(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def dynasty_year_map(self):
        raise NotImplementedError


class BaseCJKDateParser(DateTimeParser):

    def __init__(self, config: CJKDateParserConfiguration):
        self.config = config

    @property
    def no_date(self):
        return DateUtils.safe_create_from_value(DateUtils.min_value, 0, 0, 0)

    @property
    def parser_type_name(self) -> str:
        return Date_Constants.SYS_DATETIME_TIME

    def parse(self, source: ExtractResult, reference: datetime = None) -> Optional[DateTimeParseResult]:
        from ..utilities import DateTimeFormatUtil
        if reference is None:
            reference = datetime.now()

        result_value = DateTimeParseResult()

        if source.type is self.parser_type_name:
            source_text = source.text.lower()

            result_value = self.inner_parser(source_text, reference)

        result = DateTimeParseResult(source)
        result.value = result_value
        result.timex_str = result_value.timex if result_value is not None else ''
        result.resolution_str = ''

        return result

    def filter_results(self, query: str, candidate_results: List[DateTimeParseResult]):
        return candidate_results

    def inner_parser(self, source_text: ExtractResult, reference: datetime):
        inner_result = self.parse_basic_regex_match(source_text, reference)

        if not inner_result.success:
            inner_result = self.parse_weekday_of_month(
                source_text, reference)

        if not inner_result.success:
            inner_result = self.parse_implicit_date(source_text, reference)

        if not inner_result.success:
            inner_result = self.parser_duration_with_ago_and_later(
                source_text, reference)

        if inner_result.success:
            inner_result.future_resolution: Dict[str, str] = dict()
            inner_result.future_resolution[TimeTypeConstants.DATE] = DateTimeFormatUtil.format_date(
                inner_result.future_value)
            inner_result.past_resolution: Dict[str, str] = dict()
            inner_result.past_resolution[TimeTypeConstants.DATE] = DateTimeFormatUtil.format_date(
                inner_result.past_value)
            inner_result.is_lunar = self.is_lunar_calendar(source_text)

            result_value = inner_result

        return result_value

    # parse basic patterns in DateRegexList
    def parse_basic_regex_match(self, source_text, reference):
        ret = DateTimeResolutionResult()

        for regexp in self.config.date_regex_list:
            match = regex.search(regexp, source_text)

            if match:
                ret = self.match_to_date(match, reference)

        return ret

    # match several other cases
    # including '今天', '后天', '十三日'
    def parse_implicit_date(self, source_text, reference):
        ret = DateTimeResolutionResult()

        # handle "十二日" "明年这个月三日" "本月十一日"

        match = regex.search(self.config.special_date, source_text)

        if match:
            year_str = match.group(Date_Constants.YEAR_GROUP_NAME)
            month_str = match.group(Date_Constants.MONTH_GROUP_NAME)
            day_str = match.group(Date_Constants.DAY_GROUP_NAME)

            month = reference.month
            year = reference.year
            day = self.config.day_of_month[day_str]

            has_year = False
            has_month = False

            if not month_str:
                has_month = True
                has_year = True

                if regex.search(self.config.next_re, month_str):
                    month += 1
                    if month == (Date_Constants.MAX_MONTH + 1):
                        month = Date_Constants.MIN_MONTH
                        year += 1
                elif regex.search(self.config.last_re, month_str):
                    month -= 1
                    if month == (Date_Constants.MIN_MONTH + 1):
                        month = Date_Constants.MAX_MONTH
                        year -= 1

                if year_str:
                    has_year = True
                    if regex.search(self.config.next_re, year_str):
                        year += 1
                    elif regex.search(self.config.last_re, year_str):
                        year -= 1

            ret.timex = DateTimeFormatUtil.luis_date(year if has_year else -1, month if has_month else -1, day)

            future_date: datetime
            past_date: datetime

            if day > self.get_month_max_day(year, month):
                future_month = month + 1
                past_month = month - 1
                future_year = year
                past_year = year

                if future_month == (Date_Constants.MAX_MONTH + 1):
                    future_month = Date_Constants.MAX_MONTH
                    future_year = year + 1

                if past_month == (Date_Constants.MIN_MONTH - 1):
                    past_month = Date_Constants.MAX_MONTH
                    past_year = year - 1

                is_future_valid = DateUtils.is_valid_date(future_year, future_month, day)
                is_past_valid = DateUtils.is_valid_date(past_year, past_month, day)

                if is_future_valid and is_past_valid:
                    future_date = DateUtils.safe_create_from_value(DateUtils.min_value, future_year, future_month, day)
                    past_date = DateUtils.safe_create_from_value(DateUtils.min_value, past_year, past_month, day)
                elif is_future_valid and not is_past_valid:
                    future_date = DateUtils.safe_create_from_value(DateUtils.min_value, future_year, future_month, day)
                    past_date = future_date
                elif not is_future_valid and not is_past_valid:
                    future_date = DateUtils.safe_create_from_value(DateUtils.min_value, future_year, future_month, day)
                    past_date = future_date
                else:
                    # Fall back to normal cases, might lead to resolution failure
                    future_date = DateUtils.safe_create_from_value(DateUtils.min_value, year, month, day)
                    past_date = future_date
            else:
                future_date = DateUtils.safe_create_from_value(DateUtils.min_value, year, month, day)
                past_date = future_date

                if not has_month:
                    if future_date < reference:
                        if DateUtils.is_valid_date(year, month + 1, day):
                            future_date += datedelta(months=1)
                    if past_date >= reference:
                        if DateUtils.is_valid_date(year, month - 1, day):
                            past_date -= datedelta(months=1)
                        elif DateUtils.is_Feb_29th(year, month, day):
                            past_date -= datedelta(months=2)
                elif not has_year:
                    if future_date < reference:
                        if DateUtils.is_valid_date(year + 1, month, day):
                            future_date += datedelta(years=1)
                    if past_date >= reference:
                        if DateUtils.is_valid_date(year - 1, month, day):
                            past_date -= datedelta(years=1)

            ret.future_value = future_date
            ret.past_value = past_date
            ret.success = True

            return ret

        # handle cases like "昨日", "明日", "大后天"
        match = regex.search(self.config.special_day_regex, source_text)

        if match:
            value = self.config.get_swift_day(match.group())
            ret.timex = DateTimeFormatUtil.luis_date(value)
            ret.future_value = DateUtils.safe_create_from_value(DateUtils.min_value, value.year, value.month, value.day)
            ret.success = True

            return ret

        # Handle "今から2日曜日" (2 Sundays from now)
        exact_match = regex.fullmatch(self.config.special_day_with_num_regex, source_text)

        if exact_match:
            num_ers = self.config.integer_extractor.extract(source_text)
            weekday_str = self.config.get_swift_day(exact_match.group(Date_Constants.DAY_GROUP_NAME))

            if not num_ers or not num_ers[0].text:
                return ret

            num = int(self.config.number_parser.parse(num_ers[0]).value)
            value = reference

            # Check whether the determined day of this week has passed.
            if value.isoweekday() > self.config.day_of_week.get(weekday_str):
                num -= 1

            while num > 0:
                value = DateUtils.next(value, self.config.day_of_week.get(weekday_str))
                num -= 1

            ret.timex = DateTimeFormatUtil.luis_date_from_datetime(value)
            ret.future_value = DateUtils.safe_create_from_min_value(value.year, value.month, value.day)
            ret.past_value = ret.future_value
            ret.success = True

            return ret

        # handle "明日から3週間" (3 weeks from tomorrow)
        duration_extracted_results = self.config.duration_extractor.extract(source_text, reference)
        unit_match = regex.search(self.config.duration_relative_duration_unit_regex, source_text)
        is_within = RegExpUtility.get_group(regex.search(self.config.duration_relative_duration_unit_regex,
                                                         source_text), Date_Constants.WITHIN_GROUP_NAME)

        if (exact_match or is_within) and unit_match and duration_extracted_results \
                and not RegExpUtility.get_group(unit_match, Date_Constants.FEW_GROUP_NAME):
            pr = self.config.duration_parser.parse(duration_extracted_results[0], reference)
            day_str = RegExpUtility.get_group(unit_match, Date_Constants.LATER_GROUP_NAME)
            future = True
            swift = 0

            if pr:
                if day_str:
                    swift = self.config.get_swift_day(day_str)

                result_date_time = DurationParsingUtil.shift_date_time(pr.timex_str,
                                                                       (reference + datedelta(days=swift)),
                                                                       future)
                ret.timex = DateTimeFormatUtil.luis_date_from_datetime(result_date_time)
                ret.future_value = result_date_time
                ret.past_value = result_date_time
                ret.success = True
                return ret

        if not ret.success:
            ret = self.match_weekday_and_day(source_text, reference)

        if not ret.success:
            ret = self.match_this_weekday(source_text, reference)

        if not ret.success:
            ret = self.match_next_weekday(source_text, reference)

        if not ret.success:
            ret = self.match_last_weekday(source_text, reference)

        if not ret.success:
            ret = self.match_weekday_alone(source_text, reference)

        return ret

    # Handling cases like 'Monday 21', which both 'Monday' and '21' refer to the same date.
    # The year of expected date can be different to the year of referenceDate.
    def match_weekday_and_day(self, source_text, reference):
        result_value = DateTimeParseResult()

        match = regex.search(self.config.week_day_and_day_regex, source_text)

        if match:
            month = reference.month
            year = reference.year

            # Create a extract result which content ordinal string of text
            er = ExtractResult()
            er.text = RegExpUtility.get_group(match, Date_Constants.DAY_GROUP_NAME)
            er.start = match.string.index(RegExpUtility.get_group(match, Date_Constants.DAY_GROUP_NAME))
            er.length = len(RegExpUtility.get_group(match, Date_Constants.DAY_GROUP_NAME))

            day = self.convert_cjk_to_num(er.text)

            # Firstly, find a latest date with the "day" as pivotDate. Secondly, if the pivotDate equals the
            # referenced date, in other word, the day of the referenced date is exactly the "day". In this way,
            # check if the pivotDate is the weekday. If so, then the futureDate and the previousDate are the same
            # date (referenced date). Otherwise, increase the pivotDate month by month to find the latest futureDate
            # and decrease the pivotDate month by month to the latest previousDate. Notice: if the "day" is larger
            # than 28, some months should be ignored in the increase or decrease procedure.

            pivot_date = datetime(year, month, day)
            days_in_month = calendar.monthrange(year, month)[1]
            if days_in_month >= day:
                pivot_date = DateUtils.safe_create_from_min_value(year, month, day)
            else:
                # Add 1 month is enough, since 1, 3, 5, 7, 8, 10, 12 months has 31 days
                pivot_date = datetime(year, month, day) + datedelta(months=1)
                pivot_date = DateUtils.safe_create_from_min_value(pivot_date.year, pivot_date.month, pivot_date.day)

            num_week_day_int = pivot_date.isoweekday()
            extracted_week_day_str = match.group(Date_Constants.WEEKDAY_GROUP_NAME)
            week_day = self.config.day_of_week.get(extracted_week_day_str)

            if pivot_date != DateUtils.min_value:
                if day == reference.day and num_week_day_int == week_day:
                    # The referenceDate is the weekday and with the "day".
                    result_value.future_value = datetime(year, month, day)
                    result_value.past_value = datetime(year, month, day)
                    result_value.timex = DateTimeFormatUtil.luis_date(year, month, day)
                else:
                    future_date = pivot_date
                    past_date = pivot_date

                    while future_date.isoweekday() != week_day or future_date.day != day or future_date < reference:
                        # Increase the futureDate month by month to find the expected date (the "day" is the weekday)
                        # and make sure the futureDate not less than the referenceDate.
                        future_date += datedelta(months=1)
                        tmp_days_in_month = calendar.monthrange(future_date.year, future_date.month)[1]
                        if tmp_days_in_month >= day:
                            # For months like January 31, after add 1 month, February 31 won't be returned,
                            # so the day should be revised ASAP.
                            future_date = DateUtils.safe_create_from_value(DateUtils.min_value, future_date.year,
                                                                           future_date.month, day)

                    result_value.future_value = future_date

                    while past_date.isoweekday() != week_day or past_date.day != day or past_date > reference:
                        # Decrease the pastDate month by month to find the expected date (the "day" is the weekday) and
                        # make sure the pastDate not larger than the referenceDate.
                        past_date += datedelta(months=-1)
                        tmp_days_in_month = calendar.monthrange(past_date.year, future_date.month)[1]
                        if tmp_days_in_month >= day:
                            # For months like March 31, after minus 1 month, February 31
                            # won't be returned, so the day should be revised ASAP.
                            past_date = DateUtils.safe_create_from_value(DateUtils.min_value, past_date.year,
                                                                         past_date.month, day)

                    result_value.past_value = past_date

                    if week_day == 0:
                        week_day = 7

                    result_value.timex = f"XXXX-WXX-{week_day}"

            result_value.success = True

            return result_value

        return result_value

    def match_next_weekday(self, source_text, reference):
        result = DateTimeParseResult()

        match = regex.match(self.config.next_regex, source_text)

        if match:
            weekday_key = match.group(Date_Constants.WEEKDAY_GROUP_NAME)
            value = DateUtils.next(reference, self.config.day_of_week.get(weekday_key))

            result.timex = DateTimeFormatUtil.luis_date_from_datetime(value)
            result.future_value = value
            result.past_value = value
            result.success = True
        return result

    def match_this_weekday(self, source_text, reference):
        result = DateTimeParseResult()

        match = regex.match(self.config.this_regex, source_text)

        if match:
            weekday_key = match.group(Date_Constants.WEEKDAY_GROUP_NAME)
            value = DateUtils.this(reference, self.config.day_of_week.get(weekday_key))

            result.timex = DateTimeFormatUtil.luis_date_from_datetime(value)
            result.future_value = value
            result.past_value = value
            result.success = True

        return result

    def match_last_weekday(self, source_text, reference):
        result = DateTimeParseResult()

        match = regex.match(self.config.last_regex, source_text)

        if match:
            weekday_key = match.group(Date_Constants.WEEKDAY_GROUP_NAME)
            value = DateUtils.last(reference, self.config.day_of_week.get(weekday_key))

            result.timex = DateTimeFormatUtil.luis_date_from_datetime(value)
            result.future_value = value
            result.past_value = value
            result.success = True

        return result

    def match_weekday_alone(self, source_text, reference):
        result = DateTimeParseResult()

        match = regex.match(self.config.week_day_regex, source_text)
        if match:
            weekday_str = match.group(Date_Constants.WEEKDAY_GROUP_NAME)
            weekday = self.config.day_of_week.get(weekday_str)
            value = DateUtils.this(reference, weekday)

            if weekday < int(DayOfWeek.MONDAY):
                weekday = int(DayOfWeek.SUNDAY)

            if weekday < reference.isoweekday():
                value = DateUtils.next(reference, weekday)

            result.timex = 'XXXX-WXX-' + str(weekday)
            future_date = value
            past_date = value

            if future_date < reference:
                future_date += timedelta(weeks=1)

            if past_date >= reference:
                past_date -= timedelta(weeks=1)

            result.future_value = DateUtils.safe_create_from_min_value(future_date.year, future_date.month,
                                                                       future_date.day)
            result.past_value = DateUtils.safe_create_from_min_value(past_date.year, past_date.month, past_date.day)
            result.success = True
            return result

        return 'None'

    def parse_weekday_of_month(self, source_text, reference):
        ret = DateTimeParseResult()
        trimmed_source = source_text.strip()

        match = regex.match(self.config.week_day_of_month_regex, trimmed_source)

        if not match:
            return ret

        cardinal_str = RegExpUtility.get_group(match, Date_Constants.CARDINAL)
        weekday_str = RegExpUtility.get_group(match, Date_Constants.WEEKDAY_GROUP_NAME)
        month_str = RegExpUtility.get_group(match, Date_Constants.MONTH_GROUP_NAME)
        no_year = False

        if self.config.is_cardinal_last(cardinal_str):
            cardinal = 5
        else:
            cardinal = self.config.cardinal_map.get(cardinal_str)

        weekday = self.config.day_of_week.get(weekday_str)
        year = reference.year

        if not month_str:
            swift = self.config.get_swift_month(trimmed_source)
            temp = reference.replace(month=reference.month + swift)
            month = temp.month
            year = temp.year
        else:
            month = self.config.month_of_year.get(month_str)
            no_year = True

        value = self.compute_date(cardinal, weekday, month, year)

        if value.month != month:
            cardinal -= 1
            value = value.replace(day=value.day - 7)

        future_date = value
        past_date = value

        if no_year and future_date < reference:
            future_date = self.compute_date(cardinal, weekday, month, year + 1)

            if future_date.month != month:
                future_date = future_date.replace(day=future_date.day - 7)

        if no_year and past_date >= reference:
            past_date = self.compute_date(cardinal, weekday, month, year - 1)

            if past_date.month != month:
                past_date = past_date.replace(day=past_date.date - 7)

        # here is a very special case, timeX follows future date
        ret.timex = '-'.join(['XXXX', DateTimeFormatUtil.to_str(month, 2),
                              'WXX', str(weekday), '#' + str(cardinal)])
        ret.future_value = future_date
        ret.past_value = past_date
        ret.success = True

        return ret

    # parse a regex match which includes 'day', 'month' and 'year' (optional) group
    def match_to_date(self, match, reference):
        ret = DateTimeParseResult()

        month_str = RegExpUtility.get_group(match, Date_Constants.MONTH_GROUP_NAME)
        day_str = RegExpUtility.get_group(match, Date_Constants.DAY_GROUP_NAME)
        year_str = RegExpUtility.get_group(match, Date_Constants.YEAR_GROUP_NAME)
        year_cjk_str = RegExpUtility.get_group(match, Date_Constants.YEAR_CJK_GROUP_NAME)

        month = day = year = 0

        tmp = self.convert_cjk_year_to_integer(year_cjk_str)

        year = 0 if tmp == -1 else tmp

        if month_str in self.config.month_of_year and day_str in self.config.day_of_month:
            month = self.config.month_of_year.get(month_str)
            day = self.config.day_of_month.get(day_str)

            if year_str:
                year = self.config.date_extractor.get_year_from_text(match)

                if 100 > year >= Date_Constants.MIN_TWO_DIGIT_YEAR_PAST_NUM:
                    year += 1900
                    year += Date_Constants.BASE_YEAR_PAST_CENTURY
                elif 0 <= year < Date_Constants.MAX_TWO_DIGIT_YEAR_FUTURE_NUM:
                    year += Date_Constants.BASE_YEAR_CURRENT_CENTURY

        no_year = False

        if year == 0:
            year = reference.year
            ret.timex = DateTimeFormatUtil.luis_date(-1, month, day)
            no_year = True
        else:
            ret.timex = DateTimeFormatUtil.luis_date(year, month, day)

        future_date, past_date = DateUtils.generate_dates(no_year, reference, year, month, day)

        ret.future_value = future_date
        ret.past_value = past_date
        ret.success = True
        return ret

    def compute_date(self, cardinal, weekday, month, year):
        first_day = datetime(year, month, 1)
        first_weekday = DateUtils.this(first_day, weekday)

        if weekday == 0:
            weekday = int(DayOfWeek.SUNDAY)

        if weekday < first_day.isoweekday():
            first_weekday = DateUtils.next(first_day, weekday)

        first_weekday = first_weekday.replace(
            day=first_weekday.day + (7 * (cardinal - 1)))
        return first_weekday

    def is_lunar_calendar(self, text):
        trimmed_source = text.strip()
        match = regex.match(self.config.lunar_regex, trimmed_source)
        return match

    # Handle cases like "三天前" "Three days ago"
    def parser_duration_with_ago_and_later(self, source_text, reference):
        ret = DateTimeParseResult()
        num_str = ''
        unit_str = ''

        duration_extracted_results = self.config.duration_extractor.extract(source_text, reference).pop()

        if duration_extracted_results:
            match = regex.search(self.config.unit_regex, source_text)

            if match:
                suffix = source_text[duration_extracted_results.start + duration_extracted_results.length:]
                src_unit = RegExpUtility.get_group(match, 'unit')

                number_str = source_text[duration_extracted_results.start:
                                         match.lastindex - duration_extracted_results.start + 1]
                unit_match = regex.search(self.config.duration_relative_duration_unit_regex, source_text)

                few_in_unit_match = RegExpUtility.get_group(unit_match, Date_Constants.FEW_GROUP_NAME)
                # set the inexact number "数" (few) to 3 for now
                number = 3 if number_str == few_in_unit_match else self.convert_cjk_to_num(num_str)

                if not number_str == few_in_unit_match:
                    if suffix == unit_match:
                        pr = self.config.duration_parser.parse(duration_extracted_results[0], reference)
                        is_future = suffix == RegExpUtility.get_group(unit_match, Date_Constants.LATER_GROUP_NAME)
                        swift = 0

                        if pr:
                            result_date_time = DurationParsingUtil.shift_date_time(pr.timex_str,
                                                                                   (reference + datedelta(days=swift)),
                                                                                   is_future)
                            ret.timex = DateTimeFormatUtil.luis_date_from_datetime(result_date_time)
                            ret.future_value = result_date_time
                            ret.past_value = result_date_time
                            ret.success = True
                            return ret

                if src_unit in self.config.unit_map:
                    unit_str = self.config.unit_map[src_unit]
                    unit_type = 'T' if self.config.duration_parser.is_less_than_day(unit_str) else ''
                    ret.timex = f'P{unit_type}{number_str}{unit_str[0]}'

                    date = Date_Constants.INVALID_DATE_STRING

                    before_match = regex.match(self.config.before_regex, suffix)

                    if before_match and suffix.startswith(before_match):
                        date = DurationParsingUtil.shift_date_time(ret.timex, reference, False)

                    after_match = regex.match(self.config.after_regex, suffix)
                    if after_match and suffix.startswith(after_match[0]):
                        date = DurationParsingUtil.shift_date_time(ret.timex, reference, True)

                    if date != Date_Constants.INVALID_DATE_STRING:
                        ret.timex = DateTimeFormatUtil.luis_date_from_datetime(date)
                        ret.future_value = ret.past_value = date
                        ret.success = True
                        return ret

        return ret

    def convert_cjk_to_num(self, num_string):
        num = -1
        er = self.config.integer_extractor.extract(num_string)

        if er:
            if er[0].type == Num_Constants.SYS_NUM_INTEGER:
                num = int(self.config.number_parser.parse(er[0]).value)

        return num

    def convert_cjk_year_to_integer(self, year_cjk_string):
        year = num = 0

        dynasty_year = DateTimeFormatUtil.parse_dynasty_year(year_cjk_string,
                                                             self.config.dynasty_year_regex,
                                                             self.config.dynasty_start_year,
                                                             self.config.dynasty_year_map,
                                                             self.config.integer_extractor,
                                                             self.config.number_parser)
        if dynasty_year > 0:
            return dynasty_year

        er = self.config.integer_extractor.extract(year_cjk_string)

        if er:
            if er[0].type == Num_Constants.SYS_NUM_INTEGER:
                num = self.config.number_parser.parse(er[0])

        if num < 10:
            num = 0
            for year in year_cjk_string:
                num *= 10

                er = self.config.integer_extractor.extract(str(year))

                if er:
                    if er[0].type == Num_Constants.SYS_NUM_INTEGER:
                        num += self.config.number_parser.parse(er[0])

        year = -1 if num < 10 else num

        return year

    def get_month_max_day(self, year, month) -> int:
        max_day = self.config.month_max_days[month - 1]

        if not DateUtils.is_leap_year(year) and month == 2:
            max_day -= 1
        return max_day
