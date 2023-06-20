from typing import Pattern, Tuple
from recognizers_date_time.date_time.utilities import DateTimeResolutionResult, RegExpUtility


def weekday_group_match_tuple(match: Pattern) -> Tuple[str, int]:
    weekday = RegExpUtility.get_group(match, 'weekday')
    d = 1
    tup = (weekday, d)
    return tup


def weekday_group_match_string(match: Pattern) -> str:
    weekday = RegExpUtility.get_group(match, 'weekday')
    return weekday


def resolve_set(result: DateTimeResolutionResult, inner_timex: str) -> DateTimeResolutionResult:
    result.timex = inner_timex
    result.future_value = result.past_value = f"Set: {inner_timex}"
    result.success = True

    return result
