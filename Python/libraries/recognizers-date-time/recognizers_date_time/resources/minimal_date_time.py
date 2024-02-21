from .base_date_time import BaseDateTime


# pylint: disable=line-too-long


class MinimalDateTime:
    LangMarker = 'min'
    CheckBothBeforeAfter = False
    DayRegex = f'\\b(?<day>01|02|03|04|05|06|07|08|09|10|11|12|13|14|15|16|17|18|19|1|20|21|22|23|24|25|26|27|28|29|2|30|31|3|4|5|6|7|8|9)(?:\\.[º°])?(?=\\b|t)'
    MonthNumRegex = f'(?<month>1[0-2]|(0)?[1-9])\\b'
    AmDescRegex = f'({BaseDateTime.BaseAmDescRegex})'
    PmDescRegex = f'({BaseDateTime.BasePmDescRegex})'
    AmPmDescRegex = f'({BaseDateTime.BaseAmPmDescRegex})'
    DescRegex = f'(?<desc>({AmDescRegex}|{PmDescRegex}))'
    TwoDigitYearRegex = f'\\b(?<![$])(?<year>([0-9]\\d))(?!(\\s*((\\:\\d)|{AmDescRegex}|{PmDescRegex}|\\.\\d))|\\.?[º°ª])\\b'
    YearRegex = f'({BaseDateTime.FourDigitYearRegex})'
    MonthNumWithYearRegex = f'\\b(({YearRegex}(\\s*?)[/\\-\\.~](\\s*?){MonthNumRegex})|({MonthNumRegex}(\\s*?)[/\\-\\.~](\\s*?){YearRegex}))\\b'
    DateYearRegex = f'(?<year>{YearRegex}|(?<!,\\s?){TwoDigitYearRegex}|{TwoDigitYearRegex}(?=(\\.(?!\\d)|[?!;]|$)))'
    DateExtractor4 = f'\\b{MonthNumRegex}\\s*[/\\\\\\-]\\s*{DayRegex}[\\.]?\\s*[/\\\\\\-]\\s*{DateYearRegex}'
    DateExtractor5 = f'\\b{DayRegex}\\s*[/\\\\\\-\\.]\\s*({MonthNumRegex})\\s*[/\\\\\\-\\.]\\s*{DateYearRegex}(?!\\s*[/\\\\\\-\\.]\\s*\\d+)'
    DateExtractor7S = f'\\b{MonthNumRegex}\\s*/\\s*{DayRegex}(?![%]){BaseDateTime.CheckDecimalRegex}\\b'
    DateExtractor9S = f'\\b{DayRegex}\\s*/\\s*{MonthNumRegex}{BaseDateTime.CheckDecimalRegex}(?![%])\\b'

    HourRegex = f'\\b(?<!\\d[,.])(?<hour>2[0-4]|[0-1]?\\d)'
    BasicTime = f'(?<basictime>{BaseDateTime.HourRegex}:{BaseDateTime.MinuteRegex}(:{BaseDateTime.SecondRegex})?|{BaseDateTime.HourRegex})'
    ConnectNumRegex = f'({BaseDateTime.HourRegex}(?<min>[0-5][0-9])\\s*{DescRegex})'
    TimeRegexWithDotConnector = f'({BaseDateTime.HourRegex}\\.{BaseDateTime.MinuteRegex})'
    TimeRegex1 = f'({BaseDateTime.HourRegex})\\s*({DescRegex})'
    TimeRegex2 = f'(t)?{BaseDateTime.HourRegex}(\\s*)?:(\\s*)?{BaseDateTime.MinuteRegex}((\\s*)?:(\\s*)?{BaseDateTime.SecondRegex})?(\\s*({DescRegex})|\\b)'
    TimeRegex3 = f'\\b({TimeRegexWithDotConnector}(\\s*({DescRegex})))'
    TimeRegex12 = f'{BaseDateTime.HourRegex}(\\s*){BaseDateTime.MinuteRegex}(\\s*{DescRegex})?'

    MonthOfYear = dict([("1", 1),
                        ("2", 2),
                        ("3", 3),
                        ("4", 4),
                        ("5", 5),
                        ("6", 6),
                        ("7", 7),
                        ("8", 8),
                        ("9", 9),
                        ("10", 10),
                        ("11", 11),
                        ("12", 12),
                        ("01", 1),
                        ("02", 2),
                        ("03", 3),
                        ("04", 4),
                        ("05", 5),
                        ("06", 6),
                        ("07", 7),
                        ("08", 8),
                        ("09", 9)
                        ])

    DefaultLanguageFallback = 'DMY'
# pylint: enable=line-too-long
