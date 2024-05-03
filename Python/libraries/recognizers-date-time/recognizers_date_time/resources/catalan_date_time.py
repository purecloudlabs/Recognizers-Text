from .base_date_time import BaseDateTime, BaseDateTimeResource


# pylint: disable=line-too-long


class CatalanDateTime(BaseDateTimeResource):
    LangMarker = 'Cat'
    CheckBothBeforeAfter = False
    TillRegex = f'(?<till>\\bfins\\sa|{BaseDateTime.RangeConnectorSymbolRegex})'
    RangeConnectorRegex = f'(?<and>\\b(i)\\b|{BaseDateTime.RangeConnectorSymbolRegex})'
    ThisPrefixRegex = '(aix[òo]|aquesta)\\b'
    RangePrefixRegex = '(des de|entre)'
    DayRegex = '\\b(?<day>01|02|03|04|05|06|07|08|09|10|11|12|13|14|15|16|17|18|19|1|20|21|22|23|24|25|26|27|28|29|2|30|31|3|4|5|6|7|8|9)(?:\\.[º°])?(?=\\b|t)'
    MonthNumRegex = '(?<month>1[0-2]|(0)?[1-9])\\b'
    WrittenDayRegex = '(?<day>un?|dos|tres|quatre|cinc|sis|set|vuit|nou|deu|onze|dotze|tretze|catorze|quinze|setze|disset|divuit|dinou|vint|vint-i-un?|vint-i-dos|vint-i-tres|vint-i-quatre|vint-i-cinc|vint-i-sis|vint-i-set|vint-i-vuit|vint-i-nou|trenta|trenta-un?)'
    OclockRegex = '(?<oclock>en\\s+punt(o)?)'
    AmDescRegex = f'({BaseDateTime.BaseAmDescRegex})'
    PmDescRegex = f'({BaseDateTime.BasePmDescRegex})'
    AmPmDescRegex = f'({BaseDateTime.BaseAmPmDescRegex})'
    DescRegex = f'(?<desc>({AmDescRegex}|{PmDescRegex}))'
    OfPrepositionRegex = '(\\bde\\b)'
    TwoDigitYearRegex = f'\\b(?<![$])(?<year>([0-9]\\d))(?!(\\s*((\\:\\d)|{AmDescRegex}|{PmDescRegex}|\\.\\d))|\\.?[º°ª])\\b'
    WrittenOneToNineRegex = '(?:u(n)?|dos|tres|quatre|cinc|sis|set|vuit|nou)'
    WrittenOneToTwelveRegex = '(?<month>un?|dos|tres|quatre|cinc|sis|set|vuit|nou|deu|onze|dotze)'
    TwoToNineIntegerRegex = '(?:tres|set|vuit|quatre|cinc|nou|dos|sis)'
    WrittenElevenToNineteenRegex = '(?:onze|dotze|tretze|catorze|quinze|setze|disset|divuit|dinou)'
    WrittenTensRegex = '(?:setanta|vint|trenta|vuitanta|noranta|quaranta|cinquanta|seixanta)'
    WrittenTwentiesRegex = f'(vint(\\s?-\\s?|\\s)i(\\s?-\\s?|\\s)({WrittenOneToNineRegex}))'
    WrittenOneHundredToNineHundredRegex = f'(({TwoToNineIntegerRegex}(\\s?-\\s?|\\s))?cent(s?))'
    WrittenOneToNinetyNineRegex = f'(({WrittenElevenToNineteenRegex}|{WrittenTwentiesRegex}|({WrittenTensRegex}((\\s?-\\s?|\\s)({WrittenOneToNineRegex}))?)|deu|{WrittenOneToNineRegex}))'
    FullTextYearRegex = f'\\b(?<fullyear>((dos\\s+)?mil)(\\s+{WrittenOneHundredToNineHundredRegex})?(\\s+{WrittenOneToNinetyNineRegex})?)'
    YearRegex = f'({BaseDateTime.FourDigitYearRegex}|{FullTextYearRegex})'
    MonthRegex = '\\b(?<month>gener|febrer|mar[çc]|abril|maig|juny|juliol|agost|setembre|octubre|novembre|desembre)'
    MonthSuffixRegex = f'(?<msuf>((a|de)\\s+)?({MonthRegex}))'
    YearSuffix = f'((\\s?(a|del?|(de\\sl\'|del\\s)any)\\s+)?({YearRegex}|{FullTextYearRegex}))'
    SimpleCasesRegex = f'\\b({RangePrefixRegex}\\s+)?({DayRegex}|{WrittenDayRegex})\\s*{TillRegex}\\s*({DayRegex}|{WrittenDayRegex})\\s+{MonthSuffixRegex}((\\s+|\\s*,\\s*){YearRegex})?\\b'
    MonthFrontSimpleCasesRegex = f'\\b{MonthSuffixRegex}\\s+({RangePrefixRegex}?({DayRegex})\\s*{TillRegex}\\s*({DayRegex})((\\s+|\\s*,\\s*){YearRegex})?\\b'
    MonthFrontBetweenRegex = f'\\b{MonthSuffixRegex}\\s+({RangePrefixRegex}({DayRegex})\\s*{RangeConnectorRegex}\\s*({DayRegex})((\\s+|\\s*,\\s*){YearRegex})?\\b'
    MonthNumWithYearRegex = f'\\b(({YearRegex}(\\s*?)[/\\-\\.~](\\s*?){MonthNumRegex})|({MonthNumRegex}(\\s*?)[/\\-\\.~](\\s*?){YearRegex}))\\b'
    OfYearRegex = f'\\b(((de?)\\s+(({YearRegex}\\s+any)))|(de(\\s+l\'|l\\s)any\\s+{YearRegex}))\\b'
    CenturySuffixRegex = '(^segle)\\b'
    RangeUnitRegex = '\\b(?<unit>anys?|mesos?|setmanes?)\\b'
    BeforeAfterRegex = '^[.]'
    LaterRegex = '^[.]'
    AgoRegex = '^[.]'
    WithinNextPrefixRegex = '^[.]'
    CommonDatePrefixRegex = '^[.]'
    DateUnitRegex = '^[.]'
    TimeUnitRegex = '^[.]'
    ForTheRegex = '^[.]'
    RelativeMonthRegex = '^[.]'
    StrictRelativeRegex = '^[.]'
    SinceYearSuffixRegex = '^[.]'
    PrefixArticleRegex = '^[.]'
    MoreThanRegex = '^[.]'
    LessThanRegex = '^[.]'
    MonthEnd = '^[.]'
    OfMonth = '^[.]'
    InConnectorRegex = '\\b(en)(?=\\s*$)\\b'
    TodayNowRegex = '\\b(avui|ara)\\b'
    FromRegex = '((\\bde(s|l)?)(\\s*al?)?)$'
    BetweenRegex = '(\\bentre\\s*)'
    WeekDayRegex = '\\b(?<weekday>(dilluns|dimarts|dimecres|dijous|divendres|dissabte|diumenge))\\b'
    OnRegex = f'(?<=\\bel(\\s+d[ií]a)?\\s+)({DayRegex}s?)(?![.,]\\d)\\b'
    RelaxedOnRegex = '(?<=\\bel(\\s+d[ií]a)?\\s+)((?<day>10|11|12|13|14|15|16|17|18|19|1st|20|21|22|23|24|25|26|27|28|29|2|30|31|3|4|5|6|7|8|9)s?)(?![.,]\\d)\\b'
    SpecialDayRegex = '\\b(avui|dem[àa]|ahir)\\b'
    SpecialDayWithNumRegex = '^[.]'
    FlexibleDayRegex = f'(?<DayOfMonth>([a-z]+\\s)?({WrittenDayRegex}|{DayRegex}))'
    WeekDayAndDayOfMonthRegex = f'\\b{WeekDayRegex}\\s+((el\\s+(d[ií]a\\s+)?){FlexibleDayRegex})\\b'
    WeekDayAndDayRegex = f'\\b{WeekDayRegex}\\s+({DayRegex}|{WrittenDayRegex})(?!([-:/]|\\.\\d|(\\s+({AmDescRegex}|{PmDescRegex}|{OclockRegex}))))\\b'
    RelativeWeekDayRegex = '^[.]'
    AmbiguousRangeModifierPrefix = '^[.]'
    NumberEndingPattern = '^[.]'
    DateTokenPrefix = 'el '
    TimeTokenPrefix = 'a les '
    TokenBeforeDate = 'el '
    TokenBeforeTime = 'a les '
    HalfTokenRegex = '^((i\\s+)?mitja(na)?)'
    QuarterTokenRegex = '^((i\\s+)?quart|(?<neg>menys\\s+quart))'
    PastTokenRegex = '\\b((passades|passats)(\\s+(de\\s+)?les)?)$'
    ToTokenRegex = '\\b((per|abans)(\\s+(de\\s+)?les?)|(?<neg>^menys))$'
    SpecialDateRegex = f'(?<=\\b(a)\\s+el\\s+){DayRegex}\\b'
    OfMonthRegex = f'^\\s*((d[ií]a\\s+)?d[e\']\\s?)?{MonthSuffixRegex}'
    MonthEndRegex = f'({MonthRegex}\\s*(el)?\\s*$)'
    WeekDayEnd = f'{WeekDayRegex}\\s*,?\\s*$'
    WeekDayStart = '^\\b$'
    DateYearRegex = f'(?<year>{YearRegex}|(?<!,\\s?){TwoDigitYearRegex}|{TwoDigitYearRegex}(?=(\\.(?!\\d)|[?!;]|$)))'
    DateExtractor1 = f'\\b({WeekDayRegex}(\\s+|\\s*,\\s*))?(?<!\\d[.,]){DayRegex}((\\s*(d[e\'])|[/\\\\\\.\\-])\\s*)?{MonthRegex}\\b'
    DateExtractor2 = f'\\b((el\\s+d[ií]a|{WeekDayRegex})(\\s+|\\s*,\\s*))?(?<!\\d[.,])((({DayRegex}|{WrittenDayRegex})((\\s+(d(\'|e(l|\\sl\')?)\\s?)?|\\s*[.,/-]\\s*)({MonthRegex}|{MonthNumRegex}|{WrittenOneToTwelveRegex})((\\s+(de(l|l\\sany|\\sl\'any)?\\s+)?|\\s*[.,/-]\\s*){DateYearRegex}\\b)?|\\s+(d[e\']\\s?){MonthNumRegex}\\s+(del?\\s+{DateYearRegex}\\b)))|{BaseDateTime.FourDigitYearRegex}\\s*[.,/-]?\\s*(el\\s+d[ií]a\\s+)?{DayRegex}(\\s+(d[e\']\\s+)?|\\s*[.,/-]\\s*){MonthRegex})'
    DateExtractor3 = f'\\b({WeekDayRegex}(\\s+|\\s*,\\s*))?{MonthRegex}(\\s*[.,/-]?\\s*)(el\\s+d[ií]a\\s+)?{DayRegex}(?!\\s*\\-\\s*\\d{{2}}\\b)((\\s+(del?\\s+)?|\\s*[.,/-]\\s*){DateYearRegex})?\\b'
    DateExtractor4 = f'\\b(?<!\\d[.,]){MonthNumRegex}\\s*[/\\\\\\-]\\s*{DayRegex}\\s*[/\\\\\\-]\\s*{DateYearRegex}(?!\\s*[/\\\\\\-\\.]\\s*\\d+)'
    DateExtractor5 = f'\\b(?<!\\d[.,]){DayRegex}\\s*[/\\\\\\-\\.]\\s*({MonthNumRegex}|{MonthRegex})\\s*[/\\\\\\-\\.]\\s*{DateYearRegex}(?!\\s*[/\\\\\\.]\\s*\\d+)'
    DateExtractor6 = f'(?<=\\b(en|el)\\s+){MonthNumRegex}[\\-\\.]{DayRegex}{BaseDateTime.CheckDecimalRegex}\\b(?!\\s*[/\\\\\\.]\\s*\\d+)'
    DateExtractor7 = f'\\b(?<!\\d[.,]){MonthNumRegex}\\s*/\\s*{DayRegex}((\\s+|\\s*,\\s*|\\s+d[e\']\\s?){DateYearRegex})?\\b{BaseDateTime.CheckDecimalRegex}(?!\\s*[/\\\\\\.]\\s*\\d+)'
    DateExtractor8 = f'(?<=\\b(en|el)\\s+){DayRegex}[\\\\\\-]{MonthNumRegex}{BaseDateTime.CheckDecimalRegex}\\b(?!\\s*[/\\\\\\.]\\s*\\d+)'
    DateExtractor9 = f'\\b({WeekDayRegex}\\s+)?(?<!\\d[.,]){DayRegex}\\s*(/|\\bde(l?|\\sl\')\\b)\\s*{MonthNumRegex}((\\s+|\\s*,\\s*|\\s+d[e\']\\s?){DateYearRegex})?\\b{BaseDateTime.CheckDecimalRegex}(?!\\s*[/\\\\\\.]\\s*\\d+)'
    DateExtractor10 = f'\\b(?<!\\d[.,])(({YearRegex}\\s*[/\\\\\\-\\.]\\s*({MonthNumRegex}|{MonthRegex})\\s*[/\\\\\\-\\.]\\s*{DayRegex}(?!\\s*[/\\\\\\-\\.]\\s*\\d+))|({MonthRegex}\\s*[/\\\\\\-\\.]\\s*{BaseDateTime.FourDigitYearRegex}\\s*[/\\\\\\-\\.]\\s*{DayRegex})|({DayRegex}\\s*[/\\\\\\-\\.]\\s*{BaseDateTime.FourDigitYearRegex}\\s*[/\\\\\\-\\.]\\s*{MonthRegex}))'

    HourRegex = '\\b(?<!\\d[,.])(?<hour>2[0-4]|[0-1]?\\d)'
    HourNumRegex = '\\b(?<hournum>zero|una|dues|tres|quatre|cinc|sis|set|vuit|nou|deu|deu|onze|dotze)\\b'
    MinuteNumRegex = '(?<minnum>u(n)?|dos|tres|quatre|cinc|sis|set|vuit|nou|deu|onze|dotze|tretze|catorze|quinze|setze|disset|divuit|dinou|vint|trenta|quaranta|cinquanta)'
    DeltaMinuteNumRegex = '(?<deltaminnum>u(n)?|dos|tres|quatre|cinc|sis|set|vuit|nou|deu|onze|dotze|tretze|catorze|quinze|setze|disset|divuit|dinou|vint|trenta|quaranta|cinquanta)'
    PmRegex = '(?<pm>((de|a)\\s+la)\\s+(tarda|nit))'
    AmRegex = '(?<am>(((de|a)\\s+la)|al|del)\\s+(matí|matinada))'
    AmTimeRegex = '(?<am>(aquesta|(de|a)\\s+la)|(aquest)\\s+(matí|matinada))'
    PmTimeRegex = '(?<pm>(aquesta|(de|a)\\s+la)\\s+(tarda|nit))'
    NightTimeRegex = '(nit)'
    LastNightTimeRegex = '(ahir a la nit)'
    NowTimeRegex = '(ara|mateix|moment)'
    RecentlyTimeRegex = '(ment)'
    LessThanOneHour = f'(?<lth>((\\s)?(dos|tres)\\squart(s)|((\\s)?(i|un)\\s+)?quart(s)?|(\\s*)menys quart(s)?|(\\s+i\\s+)mitja(na)?|{BaseDateTime.DeltaMinuteRegex}(\\s+(minuts?|mins?))|{DeltaMinuteNumRegex}(\\s+(minuts?|mins?))|([1-3])/(2|4)))'
    TensTimeRegex = '(?<tens>deu|vint|trenta|quaranta|cinquanta)'
    WrittenTimeRegex = f'(?<writtentime>{HourNumRegex}\\s*((i|(?<prefix>menys))\\s+)?(({TensTimeRegex}(\\s*i\\s+)?)?{MinuteNumRegex}))'
    TimePrefix = f'(?<prefix>{LessThanOneHour}(\\s+(passades|de)\\s+(de\\s+les|les)?|\\s+(per\\s+a|abans\\s+de)?\\s+(les?)|\\s+(d\')|\\s+(menys))?)'
    TimeSuffix = f'(?<suffix>({LessThanOneHour}\\s+)?({AmRegex}|{PmRegex}|{OclockRegex}))'
    GeneralDescRegex = f'({DescRegex}|(?<suffix>{AmRegex}|{PmRegex}))'
    BasicTime = f'(?<basictime>{WrittenTimeRegex}|{HourNumRegex}|{BaseDateTime.HourRegex}:{BaseDateTime.MinuteRegex}(:{BaseDateTime.SecondRegex})?|{BaseDateTime.HourRegex})'
    MidTimeRegex = '(?<mid>((?<midnight>mitja\\s*nit)|(?<midearlymorning>mitja\\s*matinada)|(?<midmorning>mig\\s*matí)|(?<midafternoon>mitja\\s*tarda)|(?<midday>mig\\s*dia)))'
    AtRegex = f'\\b((?<=\\b((a)\\s+les?|al)\\s+)(({WrittenTimeRegex}|{HourNumRegex}|{BaseDateTime.HourRegex})\\b?(DescRegex)?|{MidTimeRegex})|{MidTimeRegex})'
    ConnectNumRegex = f'({BaseDateTime.HourRegex}(?<min>[0-5][0-9])\\s*{DescRegex})'
    TimeRegexWithDotConnector = f'({BaseDateTime.HourRegex}\\.{BaseDateTime.MinuteRegex})'
    TimeRegex1 = f'(\\b{TimePrefix}\\s+)?({WrittenTimeRegex}|{HourNumRegex}|{BaseDateTime.HourRegex})\\s*({DescRegex})'
    TimeRegex2 = f'(\\b{TimePrefix}\\s+)?(t)?{BaseDateTime.HourRegex}(\\s*)?:(\\s*)?{BaseDateTime.MinuteRegex}((\\s*)?:(\\s*)?{BaseDateTime.SecondRegex})?(\\s*({DescRegex})|\\b)'
    TimeRegex3 = f'\\b(({TimePrefix}\\s+)?{TimeRegexWithDotConnector}(\\s*({DescRegex}|{TimeSuffix}))|((les\\s+{TimeRegexWithDotConnector})(?!\\s*(per\\s+cent?|%))(\\s*({DescRegex}|{TimeSuffix})|\\b)))'
    TimeRegex4 = f'\\b(({DescRegex}?)|({BasicTime}\\s*)?({GeneralDescRegex}?)){TimePrefix}(\\s*({HourNumRegex}|{BaseDateTime.HourRegex}))?(\\s+{TensTimeRegex}(\\s*(i\\s+)?{MinuteNumRegex})?)?(\\s*({OclockRegex}|{DescRegex})|\\b)'
    TimeRegex5 = f'\\b({TimePrefix}|{BasicTime}{TimePrefix})\\s+(\\s*{DescRegex})?{BasicTime}?\\s*{TimeSuffix}\\b'
    TimeRegex6 = f'({BasicTime}(\\s*{DescRegex})?\\s+{TimeSuffix}\\b)'
    TimeRegex7 = f'\\b{TimeSuffix}\\s+a\\s+les\\s+{BasicTime}((\\s*{DescRegex})|\\b)'
    TimeRegex8 = f'\\b{TimeSuffix}\\s+{BasicTime}((\\s*{DescRegex})|\\b)'
    TimeRegex9 = f'\\b(?<writtentime>{HourNumRegex}\\s+({TensTimeRegex}\\s*)(i\\s+)?{MinuteNumRegex}?)\\b'
    TimeRegex11 = f'\\b({WrittenTimeRegex})(\\s+{DescRegex})?\\b'
    TimeRegex12 = f'(\\b{TimePrefix}\\s+)?{BaseDateTime.HourRegex}(\\s*){BaseDateTime.MinuteRegex}(\\s*{DescRegex})?'
    NowRegex = '\\b(?<now>(just\\s+)?ara(\\s+mateix)?|en\\s+aquest\\s+moment|tan\\s+aviat\\s +com\\s+sigui\\s+possible|tan\\s+aviat\\s+com\\s+(pugui|podes|podem|poden)|el\\s+m[aà]s\\s +aviat\\s+possible|recentment|prèviament|aquest llavors)\\b'
    Tomorrow = 'matí'
    DayOfWeek = dict([("dilluns", 1),
                      ("dimarts", 2),
                      ("dimecres", 3),
                      ("dijous", 4),
                      ("divendres", 5),
                      ("dissabte", 6),
                      ("diumenge", 0),
                      ("sa", 6)])
    MonthOfYear = dict([("gener", 1),
                        ("febrer", 2),
                        ("març", 3),
                        ("marc", 3),
                        ("abril", 4),
                        ("maig", 5),
                        ("juny", 6),
                        ("juliol", 7),
                        ("agost", 8),
                        ("setembre", 9),
                        ("octubre", 10),
                        ("novembre", 11),
                        ("desembre", 12),
                        ("1", 1),
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
                        ("09", 9),
                        ("u", 1),
                        ("un", 1),
                        ("una", 1),
                        ("dos", 2),
                        ("tres", 3),
                        ("trés", 3),
                        ("quatre", 4),
                        ("cinc", 5),
                        ("sis", 6),
                        ("set", 7),
                        ("vuit", 8),
                        ("nou", 9),
                        ("deu", 10),
                        ("onze", 11),
                        ("dotze", 12),
                        ("docena", 12),
                        ("dotzenes", 12),
                        ])
    Numbers = dict([("zero", 0),
                    ("u", 1),
                    ("un", 1),
                    ("una", 1),
                    ("dos", 2),
                    ("dues", 2),
                    ("tres", 3),
                    ("trés", 3),
                    ("quatre", 4),
                    ("cinc", 5),
                    ("sis", 6),
                    ("set", 7),
                    ("vuit", 8),
                    ("nou", 9),
                    ("deu", 10),
                    ("onze", 11),
                    ("dotze", 12),
                    ("docena", 12),
                    ("dotzenes", 12),
                    ("tretze", 13),
                    ("catorze", 14),
                    ("quinze", 15),
                    ("setze", 16),
                    ("disset", 17),
                    ("divuit", 18),
                    ("dinou", 19),
                    ("vint", 20),
                    ("veinti", 20),
                    ("ventiuna", 21),
                    ("ventiuno", 21),
                    ("vint-i-un", 21),
                    ("vint-i-una", 21),
                    ("vint-i-dos", 22),
                    ("vint-i-tres", 23),
                    ("vint-i-quatre", 24),
                    ("vint-i-cinc", 25),
                    ("vint-i-sis", 26),
                    ("vint-sis", 26),
                    ("vint-i-set", 27),
                    ("vint-i-vuit", 28),
                    ("vint-i-nou", 29),
                    ("treinta", 30),
                    ("quaranta", 40),
                    ("cinquanta", 50)])
    DayOfMonth = dict([("u", 1),
                       ("un", 1),
                       ("dos", 2),
                       ("tres", 3),
                       ("quatre", 4),
                       ("cinc", 5),
                       ("sis", 6),
                       ("set", 7),
                       ("vuit", 8),
                       ("nou", 9),
                       ("deu", 10),
                       ("onze", 11),
                       ("dotze", 12),
                       ("tretze", 13),
                       ("catorze", 14),
                       ("quinze", 15),
                       ("setze", 16),
                       ("disset", 17),
                       ("divuit", 18),
                       ("dinou", 19),
                       ("vint", 20),
                       ("vint-i-un", 21),
                       ("vint-i-dos", 22),
                       ("vint-i-tres", 23),
                       ("vint-i-quatre", 24),
                       ("vint-i-cinc", 25),
                       ("vint-i-sis", 26),
                       ("vint-i-set", 27),
                       ("vint-i-vuit", 28),
                       ("vint-i-nou", 29),
                       ("trenta", 30),
                       ("trenta-un", 31)])
    DefaultLanguageFallback = 'DMY'
# pylint: enable=line-too-long
