from .base_date_time import BaseDateTime
# pylint: disable=line-too-long


class CatalanDateTime:
    LangMarker = 'Cat'
    CheckBothBeforeAfter = False
    TillRegex = f'(?<till>\\bfins\\sa|{BaseDateTime.RangeConnectorSymbolRegex})'
    RangeConnectorRegex = f'(?<and>\\b(i)\\b|{BaseDateTime.RangeConnectorSymbolRegex})'
    # LastNegPrefix = f'(?<!(w(ill|ould|on\\s*\'\\s*t)|m(ay|ight|ust)|sh(all|ould(n\\s*\'\\s*t)?)|c(an(\\s*\'\\s*t|not)?|ould(n\\s*\'\\s*t)?))(\\s+not)?\\s+)'
    # RelativeRegex = f'\\b(?<order>following|next|(up)?coming|this|{LastNegPrefix}last|past|previous|current|the)\\b'
    # StrictRelativeRegex = f'\\b(?<order>following|next|(up)?coming|this|{LastNegPrefix}last|past|previous|current)\\b'
    # UpcomingPrefixRegex = f'((this\\s+)?((up)?coming))'
    # NextPrefixRegex = f'\\b(following|next|{UpcomingPrefixRegex})\\b'
    # AfterNextSuffixRegex = f'\\b(after\\s+(the\\s+)?next)\\b'
    # PastPrefixRegex = f'((this\\s+)?past)\\b'
    # PreviousPrefixRegex = f'({LastNegPrefix}last|previous|{PastPrefixRegex})\\b'
    ThisPrefixRegex = f'(aix[òo]|aquesta)\\b'
    RangePrefixRegex = f'(des de|entre)'
    # CenturySuffixRegex = f'(^century)\\b'
    # ReferencePrefixRegex = f'(that|same)\\b'
    # FutureSuffixRegex = f'\\b((in\\s+the\\s+)?future|hence)\\b'
    # PastSuffixRegex = f'\\b((in\\s+the\\s+)past)\\b'
    DayRegex = f'\\b(?<day>01|02|03|04|05|06|07|08|09|10|11|12|13|14|15|16|17|18|19|1|20|21|22|23|24|25|26|27|28|29|2|30|31|3|4|5|6|7|8|9)(?:\\.[º°])?(?=\\b|t)'
    # ImplicitDayRegex = f'(the\\s*)?(?<day>(?:3[0-1]|[0-2]?\\d)(?:th|nd|rd|st))\\b'
    MonthNumRegex = f'(?<month>1[0-2]|(0)?[1-9])\\b'
    WrittenDayRegex = f'(?<day>un|dos|tres|quatre|cinc|cinc|sis|set|vuit|nou|nou|deu|onze|dotze|dotze|tretze|catorze|quinze|setze|mor disset|mor divuit|dinnou|vint|vint-i-un|vint-i-dos|vint-i-tres|vint-i-quatre|vint-i-cinc|vint-i-sis|vint-i-set|vint-i-vuit|vint-i-nou|trenta|trenta-un)'
    OclockRegex = f'(?<oclock>en\\s+punt(o)?)'
    AmDescRegex = f'({BaseDateTime.BaseAmDescRegex})'
    PmDescRegex = f'({BaseDateTime.BasePmDescRegex})'
    AmPmDescRegex = f'({BaseDateTime.BaseAmPmDescRegex})'
    DescRegex = f'(?<desc>({AmDescRegex}|{PmDescRegex}))'
    OfPrepositionRegex = f'(\\bde\\b)'
    # AfterNextSuffixRegex = f'\\b(despu[eé]s\\s+de\\s+la\\s+pr[oó]xima)\\b'
    # NextSuffixRegex = f'\\b(que\\s+viene|pr[oó]xim[oa]|siguiente)\\b'
    # PreviousSuffixRegex = f'\\b(pasad[ao]|anterior(?!\\s+(al?|del?)\\b))\\b'
    # RelativeSuffixRegex = f'({AfterNextSuffixRegex}|{NextSuffixRegex}|{PreviousSuffixRegex})'
    # RangePrefixRegex = f'((de(l|sde)?|entre)(\\s+la(s)?)?)'
    TwoDigitYearRegex = f'\\b(?<![$])(?<year>([0-9]\\d))(?!(\\s*((\\:\\d)|{AmDescRegex}|{PmDescRegex}|\\.\\d))|\\.?[º°ª])\\b'
    # RelativeRegex = f'(?<order>est[ae]s?|pr[oó]xim[oa]s?|siguiente|(([uú]ltim|pasad)[ao]s?))\\b'
    # StrictRelativeRegex = f'(?<order>est[ae]|pr[oó]xim[oa]|siguiente|(([uú]ltim|pasad)(o|as|os)))\\b'
    WrittenOneToNineRegex = f'(?:u(n)?|dos|tres|quatre|cinc|sis|set|vuit|nou)'
    TwoToNineIntegerRegex = f'(?:tres|set|vuit|quatre|cinc|nou|dos|sis)'
    WrittenElevenToNineteenRegex = f'(?:onze|dotze|tretze|catorze|quinze|setze|disset|divuit|dinou)'
    WrittenTensRegex = f'(?:setanta|vint|trenta|vuitanta|noranta|quaranta|cinquanta|seixanta)'
    WrittenTwentiesRegex = f'(vint(\\s?-\\s?|\\s)i(\\s?-\\s?|\\s)({WrittenOneToNineRegex}))'
    WrittenOneHundredToNineHundredRegex = f'(({TwoToNineIntegerRegex}(\\s?-\\s?|\\s))?cent(s?))'
    WrittenOneToNinetyNineRegex = f'(({WrittenElevenToNineteenRegex}|{WrittenTwentiesRegex}|({WrittenTensRegex}((\\s?-\\s?|\\s)({WrittenOneToNineRegex}))?)|deu|{WrittenOneToNineRegex}))'
    FullTextYearRegex = f'\\b(?<fullyear>((dos\\s+)?mil)(\\s+{WrittenOneHundredToNineHundredRegex})?(\\s+{WrittenOneToNinetyNineRegex})?)'
    YearRegex = f'({BaseDateTime.FourDigitYearRegex}|{FullTextYearRegex})'
    # RelativeMonthRegex = f'(?<relmonth>(de\\s+)?((este|pr[oó]ximo|([uú]ltim(o|as|os)))\\s+mes)|(del\\s+)?(mes\\s+((que\\s+viene)|pasado)))\\b'
    MonthRegex = f'\\b(?<month>gener|febrer|mar[çc]|abril|maig|juny|juliol|agost|setembre|octubre|novembre|desembre)'
    MonthSuffixRegex = f'(?<msuf>((a|de)\\s+)?({MonthRegex}))'
    # DateUnitRegex = f'(?<unit>(año|(?<uoy>semana))(?<plural>s)?|(?<uoy>mes)(?<plural>es)?|(?<uoy>d[ií]a)(?<plural>s)?(?<business>\\s+(h[aá]biles|laborales))?)\\b'
    # PastRegex = f'(?<past>\\b(pasad(a|o)(s)?|[uú]ltim[oa](s)?|anterior(es)?|previo(s)?)\\b)'
    # FutureRegex = f'\\b(siguiente(s)?|pr[oó]xim[oa](s)?)\\b'
    SimpleCasesRegex = f'\\b({RangePrefixRegex}\\s+)?({DayRegex})\\s*{TillRegex}\\s*({DayRegex})\\s+{MonthSuffixRegex}((\\s+|\\s*,\\s*){YearRegex})?\\b'
    MonthFrontSimpleCasesRegex = f'\\b{MonthSuffixRegex}\\s+({RangePrefixRegex}?({DayRegex})\\s*{TillRegex}\\s*({DayRegex})((\\s+|\\s*,\\s*){YearRegex})?\\b'
    MonthFrontBetweenRegex = f'\\b{MonthSuffixRegex}\\s+({RangePrefixRegex}({DayRegex})\\s*{RangeConnectorRegex}\\s*({DayRegex})((\\s+|\\s*,\\s*){YearRegex})?\\b'
    # DayBetweenRegex = f'\\b((entre(\\s+el)?)\\s+)({DayRegex})\\s*{RangeConnectorRegex}\\s*({DayRegex})\\s+{MonthSuffixRegex}((\\s+|\\s*,\\s*)((en|del?)\\s+)?{YearRegex})?\\b'
    # SpecialYearPrefixes = f'((del\\s+)?calend[aá]rio|(?<special>fiscal|escolar))'
    # OneWordPeriodRegex = f'\\b(((((la|el)\\s+)?mes\\s+(({OfPrepositionRegex})\\s+)?)|((pr[oó]xim[oa]?|est[ea]|[uú]ltim[oa]?)\\s+))?({MonthRegex})|((el\\s+)?{RelativeRegex}\\s+)?(({SpecialYearPrefixes}\\s+)año|año\\s+{SpecialYearPrefixes})|(((la|el)\\s+)?((({RelativeRegex}\\s+)({DateUnitRegex}|(fin\\s+de\\s+)?semana|finde)(\\s+{RelativeSuffixRegex})?)|{DateUnitRegex}(\\s+{RelativeSuffixRegex}))|va\\s+de\\s+{DateUnitRegex}|((año|mes)(\\s+(a|hasta)\\s+la\\s+fecha)?|((el\\s+)?fin\\s+de\\s+)?semana|(el\\s+)?finde))\\b)'
    # MonthWithYearRegex = f'\\b((((pr[òo]xima|aquesta|[úu]ltim?)\\s+)?{MonthRegex}|((el\\s+)?(?<cardinal>primero?|1(er|ro)|segundo|2do|tercero?|3(er|ro)|uarto|4to|quinto|5to|sexto|6to|s[eé]ptimo|7mo|octavo|8vo|noveno|9no|d[eé]cimo|10mo|und[eé]cimo|11mo|duod[eé]cimo|12mo|[uú]ltimo)\\s+mes(?=\\s+(del?|en))))((\\s+|(\\s*[,-]\\s*))((de(l|\\s+la)?|en)\\s+)?({YearRegex}|(?<order>pr[oó]ximo(s)?|[uú]ltimo?|este)\\s+año)|\\s+(del?|en)\\s+{TwoDigitYearRegex}))\\b'
    MonthNumWithYearRegex = f'\\b(({YearRegex}(\\s*?)[/\\-\\.~](\\s*?){MonthNumRegex})|({MonthNumRegex}(\\s*?)[/\\-\\.~](\\s*?){YearRegex}))\\b'
    # WeekOfMonthRegex = f'(?<wom>(la\\s+)?(?<cardinal>primera?|1ra|segunda|2da|tercera?|3ra|cuarta|4ta|quinta|5ta|([12345](\\.)?ª)|[uú]ltima)\\s+semana\\s+{MonthSuffixRegex}((\\s+de)?\\s+({BaseDateTime.FourDigitYearRegex}|{RelativeRegex}\\s+año))?)\\b'
    # WeekOfYearRegex = f'(?<woy>(la\\s+)?(?<cardinal>primera?|1ra|segunda|2da|tercera?|3ra|cuarta|4ta|quinta|5ta|[uú]ltima?|([12345]ª))\\s+semana(\\s+(del?|en))?\\s+({YearRegex}|(?<order>pr[oó]ximo|[uú]ltimo|este)\\s+año))'
    OfYearRegex = f'\\b((de?)\\s+({YearRegex}\\s+any))\\b'
    # FirstLastRegex = f'\\b((el|las?|los?)\\s+)?((?<first>primer([ao]s?)?)|(?<last>[uú]ltim[ao]s?))\\b'
    # FollowedDateUnit = f'^\\s*{DateUnitRegex}'
    # NumberCombinedWithDateUnit = f'\\b(?<num>\\d+(\\.\\d*)?){DateUnitRegex}'
    # QuarterTermRegex = f'\\b((?<cardinal>primer|1er|segundo|2do|tercer|3ro|4to|([1234](\\.)?º))\\s+(trimestre|cuarto)|[tq](?<number>[1-4]))\\b'
    # RelativeQuarterTermRegex = f'\\b((?<orderQuarter>{StrictRelativeRegex})\\s+(trimestre|cuarto)|(trimestre|cuarto)\\s+(?<orderQuarter>(actual|pr[oó]ximo|siguiente|pasado|anterior)))\\b'
    # QuarterRegex = f'(el\\s+)?{QuarterTermRegex}((\\s+(del?\\s+)?|\\s*[,-]\\s*)({YearRegex}|(?<order>pr[oó]ximo(s)?|[uú]ltimo?|este)\\s+a[ñn]o|a[ñn]o(\\s+{RelativeSuffixRegex}))|\\s+del\\s+a[ñn]o)?|{RelativeQuarterTermRegex}'
    # QuarterRegexYearFront = f'({YearRegex}|(?<order>pr[oó]ximo(s)?|[uú]ltimo?|este)\\s+a[ñn]o)(?:\\s*-\\s*|\\s+(el\\s+)?)?{QuarterTermRegex}'
    # AllHalfYearRegex = f'\\b(?<cardinal>primer|1er|segundo|2do|[12](\\.)?º)\\s+semestre(\\s+(de\\s+)?({YearRegex}|{RelativeRegex}\\s+año))?\\b'
    # EarlyPrefixRegex = f'\\b(?<EarlyPrefix>(?<RelEarly>m[aá]s\\s+temprano(\\s+(del?|en))?)|((comienzos?|inicios?|principios?|temprano)\\s+({OfPrepositionRegex}(\\s+d[ií]a)?)))(\\s+(el|las?|los?))?\\b'
    # MidPrefixRegex = f'\\b(?<MidPrefix>(media[dn]os\\s+({OfPrepositionRegex})))(\\s+(el|las?|los?))?\\b'
    # LaterPrefixRegex = f'\\b(?<LatePrefix>((fin(al)?(es)?|[uú]ltimos)\\s+({OfPrepositionRegex}))|(?<RelLate>m[aá]s\\s+tarde(\\s+(del?|en))?))(\\s+(el|las?|los?))?\\b'
    # PrefixPeriodRegex = f'({EarlyPrefixRegex}|{MidPrefixRegex}|{LaterPrefixRegex})'
    # PrefixDayRegex = f'\\b((?<EarlyPrefix>(comienzos?|inicios?|principios?|temprano))|(?<MidPrefix>mediados)|(?<LatePrefix>(fin((al)?es)?|m[aá]s\\s+tarde)))(\\s+(en|{OfPrepositionRegex}))?(\\s+([ae]l)(\\s+d[ií]a)?)?$'
    CenturySuffixRegex = f'(^segle)\\b'
    # SeasonRegex = f'\\b(?<season>(([uú]ltim[oa]|est[ea]|el|la|(pr[oó]xim[oa]s?|siguiente)|{PrefixPeriodRegex})\\s+)?(?<seas>primavera|verano|otoño|invierno)((\\s+(del?|en)|\\s*,\\s*)?\\s+({YearRegex}|(?<order>pr[oó]ximo|[uú]ltimo|este)\\s+año))?)\\b'
    # WhichWeekRegex = f'\\b(semana)(\\s*)(?<number>5[0-3]|[1-4]\\d|0?[1-9])(\\s+del?\\s+({YearRegex}|(?<order>pr[oó]ximo|[uú]ltimo|este)\\s+año|año\\s+(?<order>pasado)))?\\b'
    # WeekOfRegex = f'((del?|el|la)\\s+)?(semana)(\\s*)({OfPrepositionRegex}|que\\s+(inicia|comienza)\\s+el|(que\\s+va|a\\s+partir)\\s+del)'
    # MonthOfRegex = f'(mes)(\\s+)({OfPrepositionRegex})'
    RangeUnitRegex = f'\\b(?<unit>anys?|mesos?|setmanes?)\\b'
    BeforeAfterRegex = f'^[.]'
    InConnectorRegex = f'\\b(en)(?=\\s*$)\\b'
    TodayNowRegex = f'\\b(avui|ara)\\b'
    FromRegex = f'((\\bdes?)(\\s*del)?)$'
    BetweenRegex = f'(\\bentre\\s*)'
    WeekDayRegex = f'\\b(?<weekday>(dilluns|dimarts|dimecres|dijous|divendres|dissabte|diumenge))\\b'
    OnRegex = f'\\b(a\\s+)({DayRegex}s?)(?![.,]\\d)\\b'
    RelaxedOnRegex = f'(?<=\\b(a)\\s+)((?<day>10|11|12|13|14|15|16|17|18|19|1st|20|21|22|23|24|25|26|27|28|29|2|30|31|3|4|5|6|7|8|9)s?)(?![.,]\\d)\\b'
    SpecialDayRegex = f'\\b(avui|dem[àa]|ahir)\\b'
    SpecialDayWithNumRegex = f'^[.]'
    FlexibleDayRegex = f'(?<DayOfMonth>([a-z]+\\s)?({WrittenDayRegex}|{DayRegex}))'
    # ForTheRegex = f'\\b((((?<=para\\s+el\\s+){FlexibleDayRegex})|((?<!(\\b{MonthRegex},?|\\bpara)\\s+(el\\s+)|{WeekDayRegex}\\s+(el\\s+)?)((?<=(e[ln]\\s+))|(\\be[ln]\\s+d[ií]a\\s+)){FlexibleDayRegex}))(?<end>\\s*(,|\\.(?![º°ª])|!|\\?|-|$))(?!\\d))'
    WeekDayAndDayOfMonthRegex = f'\\b{WeekDayRegex}\\s+((el\\s+(d[ií]a\\s+)?){FlexibleDayRegex})\\b'
    WeekDayAndDayRegex = f'\\b{WeekDayRegex}\\s+({DayRegex}|{WrittenDayRegex})(?!([-:/]|\\.\\d|(\\s+({AmDescRegex}|{PmDescRegex}|{OclockRegex}))))\\b'
    # WeekDayOfMonthRegex = f'(?<wom>(el\\s+)?(?<cardinal>primera?|1era?|segund[ao]|2d[ao]|tercera?|3era?|cuart[ao]|4t[ao]|quint[ao]|5t[ao]|((1|2|3|4|5)(\\.)?[ºª])|[uú]ltim[ao])\\s+(semana\\s+{MonthSuffixRegex}\\s+el\\s+{WeekDayRegex}|{WeekDayRegex}\\s+{MonthSuffixRegex}))'
    RelativeWeekDayRegex = f'^[.]'
    AmbiguousRangeModifierPrefix = f'^[.]'
    NumberEndingPattern = f'^[.]'
    DateTokenPrefix = 'a '
    TimeTokenPrefix = 'a les '
    TokenBeforeDate = 'el '
    TokenBeforeTime = 'a les '
    HalfTokenRegex = f'^((i\\s+)?mitjana)'
    QuarterTokenRegex = f'^((i\\s+)?quart|(?<neg>menys\\s+quart))'
    PastTokenRegex = f'\\b((passades|passats)(\\s+(de\\s+)?les)?)$'
    ToTokenRegex = f'\\b((per|abans)(\\s+(de\\s+)?les?)|(?<neg>^menys))$'
    SpecialDateRegex = f'(?<=\\b(a)\\s+el\\s+){DayRegex}\\b'
    OfMonthRegex = f'^\\s*((d[ií]a\\s+)?d[e\']\\s?)?{MonthSuffixRegex}'
    MonthEndRegex = f'({MonthRegex}\\s*(el)?\\s*$)'
    WeekDayEnd = f'{WeekDayRegex}\\s*,?\\s*$'
    WeekDayStart = f'^\\b$'
    DateYearRegex = f'(?<year>{YearRegex}|(?<!,\\s?){TwoDigitYearRegex}|{TwoDigitYearRegex}(?=(\\.(?!\\d)|[?!;]|$)))'
    DateExtractor1 = f'\\b({WeekDayRegex}(\\s+|\\s*,\\s*))?(?<!\\d[.,]){DayRegex}((\\s*(d[e\'])|[/\\\\\\.\\-])\\s*)?{MonthRegex}\\b'
    DateExtractor2 = f'\\b((el\\s+d[ií]a|{WeekDayRegex})(\\s+|\\s*,\\s*))?(?<!\\d[.,])(({DayRegex}((\\s+(d[e\']\\s?)?|\\s*[.,/-]\\s*){MonthRegex}((\\s+(del?\\s+)?|\\s*[.,/-]\\s*){DateYearRegex}\\b)?|\\s+(d[e\']\\s?){MonthNumRegex}\\s+(del?\\s+{DateYearRegex}\\b)))|{BaseDateTime.FourDigitYearRegex}\\s*[.,/-]?\\s*(el\\s+d[ií]a\\s+)?{DayRegex}(\\s+(d[e\']\\s+)?|\\s*[.,/-]\\s*){MonthRegex})'
    DateExtractor3 = f'\\b({WeekDayRegex}(\\s+|\\s*,\\s*))?{MonthRegex}(\\s*[.,/-]?\\s*)(el\\s+d[ií]a\\s+)?{DayRegex}(?!\\s*\\-\\s*\\d{{2}}\\b)((\\s+(del?\\s+)?|\\s*[.,/-]\\s*){DateYearRegex})?\\b'
    DateExtractor4 = f'\\b(?<!\\d[.,]){MonthNumRegex}\\s*[/\\\\\\-]\\s*{DayRegex}\\s*[/\\\\\\-]\\s*{DateYearRegex}(?!\\s*[/\\\\\\-\\.]\\s*\\d+)'
    DateExtractor5 = f'\\b(?<!\\d[.,]){DayRegex}\\s*[/\\\\\\-\\.]\\s*({MonthNumRegex}|{MonthRegex})\\s*[/\\\\\\-\\.]\\s*{DateYearRegex}(?!\\s*[/\\\\\\.]\\s*\\d+)'
    DateExtractor6 = f'(?<=\\b(en|el)\\s+){MonthNumRegex}[\\-\\.]{DayRegex}{BaseDateTime.CheckDecimalRegex}\\b(?!\\s*[/\\\\\\.]\\s*\\d+)'
    DateExtractor7 = f'\\b(?<!\\d[.,]){MonthNumRegex}\\s*/\\s*{DayRegex}((\\s+|\\s*,\\s*|\\s+d[e\']\\s?){DateYearRegex})?\\b{BaseDateTime.CheckDecimalRegex}(?!\\s*[/\\\\\\.]\\s*\\d+)'
    DateExtractor8 = f'(?<=\\b(en|el)\\s+){DayRegex}[\\\\\\-]{MonthNumRegex}{BaseDateTime.CheckDecimalRegex}\\b(?!\\s*[/\\\\\\.]\\s*\\d+)'
    DateExtractor9 = f'\\b({WeekDayRegex}\\s+)?(?<!\\d[.,]){DayRegex}\\s*(/|\\bde(l?)\\b)\\s*{MonthNumRegex}((\\s+|\\s*,\\s*|\\s+d[e\']\\s?){DateYearRegex})?\\b{BaseDateTime.CheckDecimalRegex}(?!\\s*[/\\\\\\.]\\s*\\d+)'
    DateExtractor10 = f'\\b(?<!\\d[.,])(({YearRegex}\\s*[/\\\\\\-\\.]\\s*({MonthNumRegex}|{MonthRegex})\\s*[/\\\\\\-\\.]\\s*{DayRegex}(?!\\s*[/\\\\\\-\\.]\\s*\\d+))|({MonthRegex}\\s*[/\\\\\\-\\.]\\s*{BaseDateTime.FourDigitYearRegex}\\s*[/\\\\\\-\\.]\\s*{DayRegex})|({DayRegex}\\s*[/\\\\\\-\\.]\\s*{BaseDateTime.FourDigitYearRegex}\\s*[/\\\\\\-\\.]\\s*{MonthRegex}))'

    HourRegex = f'\\b(?<!\\d[,.])(?<hour>2[0-4]|[0-1]?\\d)'
    HourNumRegex = f'\\b(?<hournum>zero|una|dues|tres|quatre|cinc|sis|set|vuit|nou|deu|deu|onze|dotze)\\b'
    MinuteNumRegex = f'(?<minnum>u(n)?|dos|tres|quatre|cinc|sis|set|vuit|nou|deu|onze|dotze|tretze|catorze|quinze|setze|disset|divuit|dinou|vint|trenta|quaranta|cinquanta)'
    DeltaMinuteNumRegex = f'(?<deltaminnum>u(n)?|dos|tres|quatre|cinc|sis|set|vuit|nou|deu|onze|dotze|tretze|catorze|quinze|setze|disset|divuit|dinou|vint|trenta|quaranta|cinquanta)'
    PmRegex = f'(?<pm>((de|a)\\s+la)\\s+(tarda|nit))'
    AmRegex = f'(?<am>((de|a)\\s+la)|(al)\\s+(matí|matinada))'
    AmTimeRegex = f'(?<am>(aquesta|(de|a)\\s+la)|(aquest)\\s+(matí|matinada))'
    PmTimeRegex = f'(?<pm>(aquesta|(de|a)\\s+la)\\s+(tarda|nit))'
    NightTimeRegex = f'(nit)'
    LastNightTimeRegex = f'(ahir a la nit)'
    NowTimeRegex = f'(ara|mateix|moment)'
    RecentlyTimeRegex = f'(ment)'
    # AsapTimeRegex = f'(posible|pueda[ns]?|podamos)'
    LessThanOneHour = f'(?<lth>((\\s+i\\s+)?quart|(\\s*)menys quart|(\\s+i\\s+)mitjana|{BaseDateTime.DeltaMinuteRegex}(\\s+(minuts?|mins?))|{DeltaMinuteNumRegex}(\\s+(minuts?|mins?))))'
    TensTimeRegex = f'(?<tens>deu|vint|trenta|quaranta|cinquanta)'
    WrittenTimeRegex = f'(?<writtentime>{HourNumRegex}\\s*((i|(?<prefix>menys))\\s+)?(({TensTimeRegex}(\\s*i\\s+)?)?{MinuteNumRegex}))'
    TimePrefix = f'(?<prefix>{LessThanOneHour}(\\s+(passades)\\s+(de\\s+les|les)?|\\s+(per\\s+a|abans\\s+de)?\\s+(les?))?)'
    TimeSuffix = f'(?<suffix>({LessThanOneHour}\\s+)?({AmRegex}|{PmRegex}|{OclockRegex}))'
    GeneralDescRegex = f'({DescRegex}|(?<suffix>{AmRegex}|{PmRegex}))'
    BasicTime = f'(?<basictime>{WrittenTimeRegex}|{HourNumRegex}|{BaseDateTime.HourRegex}:{BaseDateTime.MinuteRegex}(:{BaseDateTime.SecondRegex})?|{BaseDateTime.HourRegex})'
    MidTimeRegex = f'(?<mid>((?<midnight>mitja\\s*nit)|(?<midearlymorning>mitja\\s*matinada)|(?<midmorning>mig\\s*matí)|(?<midafternoon>mitja\\s*tarda)|(?<midday>mig\\s*dia)))'
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

    # PrepositionRegex = f'(?<prep>^(,\\s*)?(a(l)?|en|de(l)?)?(\\s*(la(s)?|el|los))?$)'
    # LaterEarlyRegex = f'((?<early>temprano)|(?<late>fin(al)?(\\s+de)?|m[aá]s\\s+tarde))'
    # NowRegex = f'\\b(?<now>(justo\\s+)?ahora(\\s+mismo)?|en\\s+este\\s+momento|tan\\s+pronto\\s+como\\s+sea\\s+posible|tan\\s+pronto\\s+como\\s+(pueda|puedas|podamos|puedan)|lo\\s+m[aá]s\\s+pronto\\s+posible|recientemente|previamente|este entonces)\\b'
    # SuffixRegex = f'^\\s*(((y|a|en|por)\\s+la|al)\\s+)?(mañana|madrugada|medio\\s*d[ií]a|(?<!(m[áa]s\\s+))tarde|noche)\\b'
    # TimeOfDayRegex = f'\\b((?<timeOfDay>(({LaterEarlyRegex}\\s+)((del?|en|por)(\\s+(el|los?|las?))?\\s+)?)?(mañana|madrugada|pasado\\s+(el\\s+)?medio\\s?d[ií]a|(?<!((m[áa]s|tan)\\s+))tarde|noche))|(en|por)\\s+las?\\s+mañana)\\b'
    # SpecificTimeOfDayRegex = f'\\b(((((a\\s+)?la|esta|siguiente|pr[oó]xim[oa]|[uú]ltim[oa])\\s+)?{TimeOfDayRegex})|anoche)\\b'
    # TimeOfTodayAfterRegex = f'^\\s*(,\\s*)?(en|de(l)?\\s+)?{SpecificTimeOfDayRegex}'
    # TimeOfTodayBeforeRegex = f'({SpecificTimeOfDayRegex}(\\s*,)?(\\s+(((cerca|alrededor)?\\s*(de|a)\\s+)la(s)?|para))?\\s*$)'
    # NonTimeContextTokens = f'(edificio)'
    # SimpleTimeOfTodayAfterRegex = f'(?<!{NonTimeContextTokens}\\s*)\\b({HourNumRegex}|{BaseDateTime.HourRegex})\\s*(,\\s*)?((en|de(l)?)?\\s+)?{SpecificTimeOfDayRegex}\\b'
    # SimpleTimeOfTodayBeforeRegex = f'({SpecificTimeOfDayRegex}(\\s*,)?(\\s+(((cerca|alrededor)?\\s*(de|a)\\s+)la(s)?|para))?\\s*({HourNumRegex}|{BaseDateTime.HourRegex}))\\b'
    # SpecificEndOfRegex = f'((a|e)l\\s+)?fin(alizar|al)?(\\s+(el|de(l)?)(\\s+d[ií]a)?(\\s+de)?)?\\s*$'
    # UnspecificEndOfRegex = f'\\b([ae]l\\s+)?(fin(al)?\\s+del?\\s+d[ií]a)\\b'
    # UnspecificEndOfRangeRegex = f'^[.]'
    # DateTimeTimeOfDayRegex = f'\\b(?<timeOfDay>mañana|madrugada|(?<pm>pasado\\s+(el\\s+)?medio\\s?d[ií]a|tarde|noche))\\b'
    # PeriodTimeOfDayRegex = f'\\b((en\\s+(el|la|lo)?\\s+)?({LaterEarlyRegex}\\s+)?(est[ae]\\s+)?{DateTimeTimeOfDayRegex})\\b'
    # PeriodSpecificTimeOfDayRegex = f'\\b(({LaterEarlyRegex}\\s+)?est[ae]\\s+{DateTimeTimeOfDayRegex}|({StrictRelativeRegex}\\s+{PeriodTimeOfDayRegex})|anoche)\\b'
    # UnitRegex = f'(?<unit>años?|(bi|tri|cuatri|se)mestre|mes(es)?|semanas?|fin(es)?\\s+de\\s+semana|finde|d[ií]as?|horas?|hra?s?|hs?|minutos?|mins?|segundos?|segs?|noches?)\\b'
    # ConnectorRegex = f'^(,|t|(para|y|a|en|por) las?|(\\s*,\\s*)?((cerca|alrededor)\\s+)?(de\\s+las?|del))$'
    # TimeHourNumRegex = f'(?<hour>veint(i(uno|dos|tres|cuatro)|e)|cero|uno|dos|tres|cuatro|cinco|seis|siete|ocho|nueve|diez|once|doce|trece|catorce|quince|dieci(s([eé])is|siete|ocho|nueve))'
    # PureNumFromTo = f'((\\b(desde|de)\\s+(la(s)?\\s+)?)?({BaseDateTime.HourRegex}|{TimeHourNumRegex})(?!\\s+al?\\b)(\\s*(?<leftDesc>{DescRegex}))?|(\\b(desde|de)\\s+(la(s)?\\s+)?)({BaseDateTime.HourRegex}|{TimeHourNumRegex})(\\s*(?<leftDesc>{DescRegex}))?)\\s*{TillRegex}\\s*({BaseDateTime.HourRegex}|{TimeHourNumRegex})\\s*(?<rightDesc>{PmRegex}|{AmRegex}|{DescRegex})?'
    # PureNumBetweenAnd = f'(\\bentre\\s+(la(s)?\\s+)?)(({BaseDateTime.TwoDigitHourRegex}{BaseDateTime.TwoDigitMinuteRegex})|{BaseDateTime.HourRegex}|{TimeHourNumRegex})(\\s*(?<leftDesc>{DescRegex}))?\\s*{RangeConnectorRegex}\\s*(({BaseDateTime.TwoDigitHourRegex}{BaseDateTime.TwoDigitMinuteRegex})|{BaseDateTime.HourRegex}|{TimeHourNumRegex})\\s*(?<rightDesc>{PmRegex}|{AmRegex}|{DescRegex})?'
    # SpecificTimeFromTo = f'({RangePrefixRegex}\\s+)?(?<time1>(({TimeRegex2}|{TimeRegexWithDotConnector}(\\s*{DescRegex})?)|({BaseDateTime.HourRegex}|{TimeHourNumRegex})(\\s*(?<leftDesc>{DescRegex}))?))\\s*{TillRegex}\\s*(?<time2>(({TimeRegex2}|{TimeRegexWithDotConnector}(\\s*{DescRegex})?)|({BaseDateTime.HourRegex}|{TimeHourNumRegex})(\\s*(?<rightDesc>{DescRegex}))?))'
    # SpecificTimeBetweenAnd = f'({BetweenRegex}\\s+)(?<time1>(({TimeRegex1}|{TimeRegex2}|{TimeRegexWithDotConnector}(\\s*{DescRegex})?)|({BaseDateTime.HourRegex}|{TimeHourNumRegex})(\\s*(?<leftDesc>{DescRegex}))?))\\s*{RangeConnectorRegex}\\s*(?<time2>(({TimeRegex1}|{TimeRegex2}|{TimeRegexWithDotConnector}(\\s*{DescRegex})?)|({BaseDateTime.HourRegex}|{TimeHourNumRegex})(\\s*(?<rightDesc>{DescRegex}))?))'
    # TimeUnitRegex = f'([^A-Za-z]{{1,}}|\\b)(?<unit>(hora|minuto|min|segundo|se[cg])(?<plural>s)?|h)\\b'
    # TimeFollowedUnit = f'^\\s*{TimeUnitRegex}'
    # TimeNumberCombinedWithUnit = f'\\b(?<num>\\d+(\\,\\d*)?)\\s*{TimeUnitRegex}'
    # DateTimePeriodNumberCombinedWithUnit = f'\\b(?<num>\\d+(\\.\\d*)?)\\s*{TimeUnitRegex}'
    # PeriodTimeOfDayWithDateRegex = f'\\b(((y|a|en|por)\\s+(la\\s+)?|al\\s+)?((((?<early>primeras\\s+horas\\s+)|(?<late>(últimas|altas)\\s+horas\\s+))(de\\s+la\\s+)?|{LaterEarlyRegex}\\s+(est[ae]\\s+)?)?(?<timeOfDay>(mañana|madrugada|pasado\\s+(el\\s+)?medio\\s?d[ií]a|(?<!(m[áa]s\\s+))tarde|noche|anoche))))(\\s+(del|de))?\\b'
    # RelativeTimeUnitRegex = f'({PastRegex}|{FutureRegex})\\s+{TimeUnitRegex}'
    # LessThanRegex = f'\\b(dentro\\s+de\\s+menos\\s+de)\\b'
    # MoreThanRegex = f'\\b(durante\\s+(m[áa]s\\s+)?de)\\b'
    # SuffixAndRegex = f'(?<suffix>\\s*(y)\\s+((un[ao]?)\\s+)?(?<suffix_num>media|cuarto))'
    # FollowedUnit = f'^\\s*{UnitRegex}'
    # DurationNumberCombinedWithUnit = f'\\b(?<num>\\d+(\\,\\d*)?){UnitRegex}'
    # AnUnitRegex = f'\\b(una?|otr[ao])\\s+{UnitRegex}'
    # DuringRegex = f'^[.]'
    # AllRegex = f'\\b(?<all>tod[oa]?\\s+(el|la)\\s+(?<unit>año|mes|semana|d[ií]a)|((una?|el|la)\\s+)?(?<unit>año|mes|semana|d[ií]a)\\s+enter[ao])\\b'
    # HalfRegex = f'\\b(?<half>medi[oa]\\s+(?<unit>ano|mes|semana|d[íi]a|hora))\\b'
    # ConjunctionRegex = f'^[.]'
    # InexactNumberRegex = f'\\b(pocos?|algo|vari[ao]s|algun[ao]s|un[ao]s)\\b'
    # InexactNumberUnitRegex = f'({InexactNumberRegex})\\s+{UnitRegex}'
    # HolidayRegex1 = f'\\b(?<holiday>viernes\\s+(santo|negro)|mi[eé]rcoles de ceniza|martes de carnaval|d[ií]a (de|de los) presidentes?|clebraci[oó]n de mao|año nuevo chino|año nuevo|noche vieja|(festividad de )?los mayos|d[ií]a de los inocentes|navidad|noche buena|d[ií]a de acci[oó]n de gracias|acci[oó]n de gracias|yuandan|halloween|noches de brujas|pascuas)(\\s+(del?\\s+)?({YearRegex}|(?<order>(pr[oó]xim[oa]?|est[ea]|[uú]ltim[oa]?|en))\\s+año))?\\b'
    # HolidayRegex2 = f'\\b(?<holiday>(d[ií]a( del?( la)?)? )?(martin luther king|todos los santos|tierra|blanco|san patricio|san valent[ií]n|san jorge|cinco de mayo|independencia|raza|trabajador))(\\s+(del?\\s+)?({YearRegex}|(?<order>(pr[oó]xim[oa]?|est[ea]|[uú]ltim[oa]?|en))\\s+año))?\\b'
    # HolidayRegex3 = f'\\b(?<holiday>(d[ií]a( internacional)?( del?( l[ao]s?)?)? )(trabajador(es)?|madres?|padres?|[aá]rbol|mujer(es)?|solteros?|niños?|marmota|san valent[ií]n|maestro))(\\s+(del?\\s+)?({YearRegex}|(?<order>(pr[oó]xim[oa]?|est[ea]|[uú]ltim[oa]?|en))\\s+año))?\\b'
    # BeforeRegex = f'(\\b((ante(s|rior)|m[aá]s\\s+temprano|no\\s+m[aá]s\\s+tard(e|ar)|hasta|(?<include>tan\\s+tarde\\s+como))(\\s+(del?|a|que)(\\s+(el|las?|los?))?)?)|(?<!\\w|>)((?<include><\\s*=)|<))'
    # AfterRegex = f'((\\b(despu[eé]s|(año\\s+)?posterior|m[aá]s\\s+tarde|a\\s+primeros)(\\s*(del?|en|a)(\\s+(el|las?|los?))?)?|(empi?en?zando|comenzando)(\\s+(el|las?|los?))?)\\b|(?<!\\w|<)((?<include>>\\s*=)|>))'
    # SinceRegex = f'\\b(((cualquier\\s+tiempo\\s+)?(desde|a\\s+partir\\s+del?)|tan\\s+(temprano|pronto)\\s+como(\\s+(de|a))?)(\\s+(el|las?|los?))?)\\b'
    # SinceRegexExp = f'({SinceRegex}|\\bde\\b)'
    # AroundRegex = f'(?:\\b(?:cerca|alrededor|aproximadamente)(\\s+(de\\s+(las?|el)|del?))?\\s*\\b)'
    # PeriodicRegex = f'\\b(?<periodic>a\\s*diario|diaria(s|mente)|(bi|tri)?(semanal|quincenal|mensual|(se|tri)mestral|anual)(es|mente)?)\\b'
    # EachExpression = f'\\b(cada|tod[oa]s\\s*(l[oa]s)?)\\b\\s*(?!\\s*l[oa]\\b)'
    # EachUnitRegex = f'(?<each>({EachExpression})\\s*({UnitRegex}|(?<specialUnit>fin(es)?\\s+de\\s+semana|finde)\\b))'
    # EachPrefixRegex = f'(?<each>({EachExpression})\\s*$)'
    # EachDayRegex = f'\\s*({EachExpression})\\s*d[ií]as\\s*\\b'
    # BeforeEachDayRegex = f'({EachExpression})\\s*d[ií]as(\\s+a\\s+las?)?\\s*\\b'
    # SetEachRegex = f'(?<each>({EachExpression})\\s*)'
    # LaterEarlyPeriodRegex = f'\\b(({PrefixPeriodRegex})\\s+(?<suffix>{OneWordPeriodRegex}|(?<FourDigitYear>{BaseDateTime.FourDigitYearRegex}))|({UnspecificEndOfRangeRegex}))\\b'
    # RelativeWeekRegex = f'(((la|el)\\s+)?(((est[ae]|pr[oó]xim[oa]|[uú]ltim(o|as|os))\\s+semanas?)|(semanas?\\s+(que\\s+viene|pasad[oa]))))'
    # WeekWithWeekDayRangeRegex = f'\\b((({RelativeWeekRegex})((\\s+entre\\s+{WeekDayRegex}\\s+y\\s+{WeekDayRegex})|(\\s+de\\s+{WeekDayRegex}\\s+a\\s+{WeekDayRegex})))|((entre\\s+{WeekDayRegex}\\s+y\\s+{WeekDayRegex})|(de\\s+{WeekDayRegex}\\s+a\\s+{WeekDayRegex})){OfPrepositionRegex}\\s+{RelativeWeekRegex})\\b'
    # GeneralEndingRegex = f'^\\s*((\\.,)|\\.|,|!|\\?)?\\s*$'
    # MiddlePauseRegex = f'^[.]'
    # PrefixArticleRegex = f'\\b(e[ln]\\s+(d[ií]a\\s+)?)'
    # OrRegex = f'^[.]'
    # SpecialYearTermsRegex = f'\\b(({SpecialYearPrefixes}\\s+años?\\s+|años?\\s+({SpecialYearPrefixes}\\s+)?)(de\\s+)?)'
    # YearPlusNumberRegex = f'\\b({SpecialYearTermsRegex}((?<year>(\\d{{2,4}}))|{FullTextYearRegex}))\\b'
    # NumberAsTimeRegex = f'\\b({WrittenTimeRegex}|{HourRegex}(?<desc>\\s*h(oras)?)?)\\b'
    # TimeBeforeAfterRegex = f'\\b((?<=\\b(antes|no\\s+m[aá]s\\s+tard(e|ar)\\s+(de|a\\s+las?)|por| después)\\s+)({WrittenTimeRegex}|{HourNumRegex}|{BaseDateTime.HourRegex}|{MidTimeRegex}))\\b'
    # DateNumberConnectorRegex = f'^\\s*(?<connector>a\\s+las)\\s*$'
    # CenturyRegex = f'^[.]'
    # DecadeRegex = f'(?<decade>diez|veinte|treinta|cuarenta|cincuenta|se[st]enta|ochenta|noventa)'
    # DecadeWithCenturyRegex = f'(los\\s+)?((((d[ée]cada(\\s+de)?)\\s+)(((?<century>\\d|1\\d|2\\d)?(?<decade>\\d0))))|a[ñn]os\\s+((((dos\\s+)?mil\\s+)?({WrittenOneHundredToNineHundredRegex}\\s+)?{DecadeRegex})|((dos\\s+)?mil\\s+)?({WrittenOneHundredToNineHundredRegex})(\\s+{DecadeRegex}?)|((dos\\s+)?mil)(\\s+{WrittenOneHundredToNineHundredRegex}\\s+)?{DecadeRegex}?))'
    # RelativeDecadeRegex = f'\\b(((el|las?)\\s+)?{RelativeRegex}\\s+((?<number>[\\w,]+)\\s+)?(d[eé]cada|decenio)s?)\\b'
    # ComplexDatePeriodRegex = f'(?:((de(sde)?)\\s+)?(?<start>.+)\\s*({StrictTillRegex})\\s*(?<end>.+)|((entre)\\s+)(?<start>.+)\\s*({RangeConnectorRegex})\\s*(?<end>.+))'
    # AmbiguousPointRangeRegex = f'^(mar\\.?)$'
    # YearSuffix = f'((,|\\sdel?)?\\s*({YearRegex}|{FullTextYearRegex}))'
    # SinceYearSuffixRegex = f'(^\\s*{SinceRegex}(\\s*(el\\s+)?año\\s*)?{YearSuffix})'
    # AgoRegex = f'\\b(antes\\s+de\\s+(?<day>hoy|ayer|mañana)|antes|hace)\\b'
    # LaterRegex = f'\\b(despu[eé]s(?!\\s+de\\b)|desde\\s+ahora|(a\\s+partir|despu[eé]s)\\s+de\\s+(ahora|(?<day>hoy|ayer|mañana)))\\b'
    # Tomorrow = 'mañana'
    # UnitMap = dict([("años", "Y"),
    #                 ("año", "Y"),
    #                 ("meses", "MON"),
    #                 ("mes", "MON"),
    #                 ("trimestre", "3MON"),
    #                 ("trimestres", "3MON"),
    #                 ("cuatrimestre", "4MON"),
    #                 ("cuatrimestres", "4MON"),
    #                 ("semestre", "6MON"),
    #                 ("semestres", "6MON"),
    #                 ("bimestre", "2MON"),
    #                 ("bimestres", "2MON"),
    #                 ("semanas", "W"),
    #                 ("semana", "W"),
    #                 ("fin de semana", "WE"),
    #                 ("fines de semana", "WE"),
    #                 ("finde", "WE"),
    #                 ("dias", "D"),
    #                 ("dia", "D"),
    #                 ("días", "D"),
    #                 ("día", "D"),
    #                 ("jornada", "D"),
    #                 ("noche", "D"),
    #                 ("noches", "D"),
    #                 ("horas", "H"),
    #                 ("hora", "H"),
    #                 ("hrs", "H"),
    #                 ("hras", "H"),
    #                 ("hra", "H"),
    #                 ("hr", "H"),
    #                 ("h", "H"),
    #                 ("minutos", "M"),
    #                 ("minuto", "M"),
    #                 ("mins", "M"),
    #                 ("min", "M"),
    #                 ("segundos", "S"),
    #                 ("segundo", "S"),
    #                 ("segs", "S"),
    #                 ("seg", "S")])
    # UnitValueMap = dict([("años", 31536000),
    #                      ("año", 31536000),
    #                      ("meses", 2592000),
    #                      ("mes", 2592000),
    #                      ("semanas", 604800),
    #                      ("semana", 604800),
    #                      ("fin de semana", 172800),
    #                      ("fines de semana", 172800),
    #                      ("finde", 172800),
    #                      ("dias", 86400),
    #                      ("dia", 86400),
    #                      ("días", 86400),
    #                      ("día", 86400),
    #                      ("noche", 86400),
    #                      ("noches", 86400),
    #                      ("horas", 3600),
    #                      ("hora", 3600),
    #                      ("hrs", 3600),
    #                      ("hras", 3600),
    #                      ("hra", 3600),
    #                      ("hr", 3600),
    #                      ("h", 3600),
    #                      ("minutos", 60),
    #                      ("minuto", 60),
    #                      ("mins", 60),
    #                      ("min", 60),
    #                      ("segundos", 1),
    #                      ("segundo", 1),
    #                      ("segs", 1),
    #                      ("seg", 1)])
    # SpecialYearPrefixesMap = dict([("fiscal", "FY"),
    #                                ("escolar", "SY")])
    # SeasonMap = dict([("primavera", "SP"),
    #                   ("verano", "SU"),
    #                   ("otoño", "FA"),
    #                   ("invierno", "WI")])
    # SeasonValueMap = dict([("SP", 3),
    #                        ("SU", 6),
    #                        ("FA", 9),
    #                        ("WI", 12)])
    # CardinalMap = dict([("primer", 1),
    #                     ("primero", 1),
    #                     ("primera", 1),
    #                     ("1er", 1),
    #                     ("1ro", 1),
    #                     ("1ra", 1),
    #                     ("1.º", 1),
    #                     ("1º", 1),
    #                     ("1ª", 1),
    #                     ("segundo", 2),
    #                     ("segunda", 2),
    #                     ("2do", 2),
    #                     ("2da", 2),
    #                     ("2.º", 2),
    #                     ("2º", 2),
    #                     ("2ª", 2),
    #                     ("tercer", 3),
    #                     ("tercero", 3),
    #                     ("tercera", 3),
    #                     ("3er", 3),
    #                     ("3ro", 3),
    #                     ("3ra", 3),
    #                     ("3.º", 3),
    #                     ("3º", 3),
    #                     ("3ª", 3),
    #                     ("cuarto", 4),
    #                     ("cuarta", 4),
    #                     ("4to", 4),
    #                     ("4ta", 4),
    #                     ("4.º", 4),
    #                     ("4º", 4),
    #                     ("4ª", 4),
    #                     ("quinto", 5),
    #                     ("quinta", 5),
    #                     ("5to", 5),
    #                     ("5ta", 5),
    #                     ("5.º", 5),
    #                     ("5º", 5),
    #                     ("5ª", 5),
    #                     ("sexto", 6),
    #                     ("sexta", 6),
    #                     ("6to", 6),
    #                     ("6ta", 6),
    #                     ("septimo", 7),
    #                     ("séptimo", 7),
    #                     ("septima", 7),
    #                     ("séptima", 7),
    #                     ("7mo", 7),
    #                     ("7ma", 7),
    #                     ("octavo", 8),
    #                     ("octava", 8),
    #                     ("8vo", 8),
    #                     ("8va", 8),
    #                     ("noveno", 9),
    #                     ("novena", 9),
    #                     ("9no", 9),
    #                     ("9na", 9),
    #                     ("decimo", 10),
    #                     ("décimo", 10),
    #                     ("decima", 10),
    #                     ("décima", 10),
    #                     ("10mo", 10),
    #                     ("10ma", 10),
    #                     ("undecimo", 11),
    #                     ("undécimo", 11),
    #                     ("undecima", 11),
    #                     ("undécima", 11),
    #                     ("11mo", 11),
    #                     ("11ma", 11),
    #                     ("duodecimo", 12),
    #                     ("duodécimo", 12),
    #                     ("duodecima", 12),
    #                     ("duodécima", 12),
    #                     ("12mo", 12),
    #                     ("12ma", 12)])
    DayOfWeek = dict([("dilluns", 1),
                      ("dimarts", 2),
                      ("dimecres", 3),
                      ("dijous", 4),
                      ("divendres", 5),
                      ("dissabte", 6),
                      ("diumenge", 0),
                      # ("dom", 0),
                      # ("lun", 1),
                      # ("mar", 2),
                      # ("mie", 3),
                      # ("mié", 3),
                      # ("jue", 4),
                      # ("vie", 5),
                      # ("sab", 6),
                      # ("sáb", 6),
                      # ("dom.", 0),
                      # ("lun.", 1),
                      # ("mar.", 2),x
                      # ("mie.", 3),
                      # ("mié.", 3),
                      # ("jue.", 4),
                      # ("vie.", 5),
                      # ("sab.", 6),
                      # ("sáb.", 6),
                      # ("do", 0),
                      # ("lu", 1),
                      # ("ma", 2),
                      # ("mi", 3),
                      # ("ju", 4),
                      # ("vi", 5),
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
                        # ("ene", 1),
                        # ("feb", 2),
                        # ("mar", 3),
                        # ("abr", 4),
                        # ("may", 5),
                        # ("jun", 6),
                        # ("jul", 7),
                        # ("ago", 8),
                        # ("sept", 9),
                        # ("sep", 9),
                        # ("set", 9),
                        # ("oct", 10),
                        # ("nov", 11),
                        # ("dic", 12),
                        # ("ene.", 1),
                        # ("feb.", 2),
                        # ("mar.", 3),
                        # ("abr.", 4),
                        # ("may.", 5),
                        # ("jun.", 6),
                        # ("jul.", 7),
                        # ("ago.", 8),
                        # ("sept.", 9),
                        # ("sep.", 9),
                        # ("set.", 9),
                        # ("oct.", 10),
                        # ("nov.", 11),
                        # ("dic.", 12),
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
                        ("09", 9)])
    Numbers = dict([("zero", 0),
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
    # HolidayNames = dict([("padres", ["diadelpadre"]),
    #                      ("madres", ["diadelamadre"]),
    #                      ("acciondegracias", ["diadegracias", "diadeacciondegracias", "acciondegracias"]),
    #                      ("trabajador", ["diadeltrabajador", "diadelostrabajadores", "diainternacionaldeltrabajador",
    #                                      "diainternacionaldelostrabajadores"]),
    #                      ("delaraza", ["diadelaraza", "diadeladiversidadcultural"]),
    #                      ("memoria", ["diadelamemoria"]),
    #                      ("pascuas", ["diadepascuas", "pascuas"]),
    #                      ("navidad", ["navidad", "diadenavidad"]),
    #                      ("nochebuena", ["diadenochebuena", "nochebuena"]),
    #                      ("añonuevo", ["a\u00f1onuevo", "diadea\u00f1onuevo"]),
    #                      ("nochevieja", ["nochevieja", "diadenochevieja"]),
    #                      ("yuandan", ["yuandan"]),
    #                      ("earthday", ["diadelatierra"]),
    #                      ("maestro", ["diadelmaestro"]),
    #                      ("todoslossantos", ["todoslossantos"]),
    #                      ("niño", ["diadelni\u00f1o"]),
    #                      ("mujer", ["diadelamujer"]),
    #                      ("independencia", ["diadelaindependencia", "diadeindependencia", "independencia"]),
    #                      ("blackfriday", ["viernesnegro"]),
    #                      ("goodfriday", ["viernessanto"]),
    #                      ("stpatrickday", ["sanpatricio", "diadesanpatricio"]),
    #                      ("valentinesday", ["sanvalentin", "diadesanvalentin"])])
    # VariableHolidaysTimexDictionary = dict([("padres", "-06-WXX-7-3"),
    #                                         ("madres", "-05-WXX-7-2"),
    #                                         ("acciondegracias", "-11-WXX-4-4"),
    #                                         ("delaraza", "-10-WXX-1-2"),
    #                                         ("memoria", "-03-WXX-2-4")])
    # DoubleNumbers = dict([("mitad", 0.5),
    #                       ("cuarto", 0.25)])
    # UpcomingPrefixRegex = f'((este\\s+))'
    # NextPrefixRegex = f'\\b({UpcomingPrefixRegex}?pr[oó]xim[oa]s?|siguiente|que\\s+viene)\\b'
    # PastPrefixRegex = f'((este\\s+))'
    # PreviousPrefixRegex = f'\\b({PastPrefixRegex}?pasad[oa]s?(?!(\\s+el)?\\s+medio\\s*d[ií]a)|[uú]ltim[oa]s?|anterior)\\b'
    # ThisPrefixRegex = f'(est?[ea]|actual)\\b'
    # PrefixWeekDayRegex = f'(\\s*((,?\\s*el)|[-—–]))'
    # ThisRegex = f'\\b((est[ae]\\s*)(semana{PrefixWeekDayRegex}?)?\\s*{WeekDayRegex})|({WeekDayRegex}\\s*((de\\s+)?esta\\s+semana))\\b'
    # LastDateRegex = f'\\b(({PreviousPrefixRegex}\\s+(semana{PrefixWeekDayRegex}?)?|(la\\s+)?semana\\s+{PreviousPrefixRegex}{PrefixWeekDayRegex})\\s*{WeekDayRegex})|(este\\s+)?({WeekDayRegex}\\s+([uú]ltimo|pasado|anterior))|({WeekDayRegex}(\\s+((de\\s+)?((esta|la)\\s+([uú]ltima\\s+)?semana)|(de\\s+)?(la\\s+)?semana\\s+(pasada|anterior))))\\b'
    # NextDateRegex = f'\\b((({NextPrefixRegex}\\s+)(semana{PrefixWeekDayRegex}?)?|(la\\s+)?semana\\s+{NextPrefixRegex}{PrefixWeekDayRegex})\\s*{WeekDayRegex})|(este\\s+)?({WeekDayRegex}\\s+(pr[oó]ximo|siguiente|que\\s+viene))|({WeekDayRegex}(\\s+(de\\s+)?(la\\s+)?((pr[oó]xima|siguiente)\\s+semana|semana\\s+(pr[oó]xima|siguiente))))\\b'
    # RelativeDayRegex = f'(?<relday>((este|pr[oó]ximo|([uú]ltim(o|as|os)))\\s+días)|(días\\s+((que\\s+viene)|pasado)))\\b'
    # RestOfDateRegex = f'\\bresto\\s+((del|de)\\s+)?((la|el|est?[ae])\\s+)?(?<duration>semana|mes|año|decada)(\\s+actual)?\\b'
    # WithinNextPrefixRegex = f'\\b(dentro\\s+de((\\s+(el|l[ao]s?))?\\s+(?<next>{NextPrefixRegex}))?)(?=\\s*$)\\b'
    # DurationUnitRegex = f'(?<unit>{DateUnitRegex}|horas?|hra?s?|hs?|minutos?|mins?|segundos?|segs?|noches?)\\b'
    # DurationConnectorRegex = f'^\\s*(?<connector>\\s+|y|,)\\s*$'
    # RelativeDurationUnitRegex = f'(?:(?<=({NextPrefixRegex}|{PreviousPrefixRegex}|{ThisPrefixRegex})\\s+)({DurationUnitRegex}))'
    # ReferencePrefixRegex = f'(mism[ao]|aquel|est?e)\\b'
    # ReferenceDatePeriodRegex = f'\\b{ReferencePrefixRegex}\\s+({DateUnitRegex}|fin\\s+de\\s+semana)\\b'
    # FromToRegex = f'\\b(from).+(to)\\b.+'
    # SingleAmbiguousMonthRegex = f'^(the\\s+)?(may|march)$'
    # UnspecificDatePeriodRegex = f'^[\\.]'
    # PrepositionSuffixRegex = f'\\b(en|el|la|cerca|alrededor|desde|durante|hasta|hacia)$'
    # RestOfDateTimeRegex = f'\\bresto\\s+((del?)\\s+)?((la|el|est[ae])\\s+)?(?<unit>(día|jornada))(\\s+de\\s+hoy)?\\b'
    # SetWeekDayRegex = f'^[\\.]'
    # NightRegex = f'\\b(medionoche|noche)\\b'
    # CommonDatePrefixRegex = f'^[\\.]'
    # SuffixAfterRegex = f'\\b((a\\s+)?(o|y)\\s+(arriba|despu[eé]s|posterior|mayor|m[aá]s\\s+tarde)(?!\\s+(que|de)))\\b'
    # YearPeriodRegex = f'((((de(sde)?|durante|en)\\s+)?{YearRegex}\\s*({TillRegex})\\s*{YearRegex})|(((entre)\\s+){YearRegex}\\s*({RangeConnectorRegex})\\s*{YearRegex}))'
    # FutureSuffixRegex = f'\\b(siguiente(s)?|pr[oó]xim[oa](s)?|(en\\s+el\\s+)?futuro)\\b'
    # PastSuffixRegex = f'^\\b$'
    # ModPrefixRegex = f'\\b({RelativeRegex}|{AroundRegex}|{BeforeRegex}|{AfterRegex}|{SinceRegex})\\b'
    # ModSuffixRegex = f'\\b({AgoRegex}|{LaterRegex}|{BeforeAfterRegex}|{FutureSuffixRegex}|{PastSuffixRegex})\\b'
    # WrittenDecades = dict([("", 0)])
    # SpecialDecadeCases = dict([("", 0)])
    DefaultLanguageFallback = 'DMY'
    # DurationDateRestrictions = [r'hoy']
    # AmbiguityFiltersDict = dict([("^\\d{4}$", "(\\d\\.\\d{4}|\\d{4}\\.\\d)"),
    #                              ("^(este\\s+)?mi(\\s+([uú]ltimo|pasado|anterior|pr[oó]ximo|siguiente|que\\s+viene))?$",
    #                               "\\b(este\\s+)?mi(\\s+([uú]ltimo|pasado|anterior|pr[oó]ximo|siguiente|que\\s+viene))?\\b"),
    #                              ("^a[nñ]o$", "(?<!el\\s+)a[nñ]o"),
    #                              ("^semana$", "(?<!la\\s+)semana"),
    #                              ("^mes$", "(?<!el\\s+)mes"),
    #                              ("^(abr|ago|dic|feb|ene|ju[ln]|mar|may|nov|oct|sep?t|sep)$",
    #                               "([$%£&!?@#])(abr|ago|dic|feb|ene|ju[ln]|mar|may|nov|oct|sep?t|sep)|(abr|ago|dic|feb|ene|ju[ln]|mar|may|nov|oct|sep?t|sep)([$%£&@#])"),
    #                              ("^\\d{1,4}-\\d{1,4}$", "\\d{1,4}-\\d{1,4}-\\d|\\d-\\d{1,4}-\\d{1,4}"),
    #                              ("^\\d{1,4}-\\d{1,4}-\\d{1,4}$",
    #                               "\\d{1,4}-\\d{1,4}-\\d{1,4}-\\d|\\d-\\d{1,4}-\\d{1,4}-\\d{1,4}")])
    # EarlyMorningStartEndRegex = f'(^(madrugada)|(madrugada)$)'
    # MorningStartEndRegex = f'(^((la\\s+)?mañana))|(((la\\s+)?mañana)$)'
    # AfternoonStartEndRegex = f'(^(pasado\\s+(el\\s+)?medio\\s*dia))|((pasado\\s+(el\\s+)?medio\\s*dia)$)'
    # EveningStartEndRegex = f'(^(tarde))|((tarde)$)'
    # NightStartEndRegex = f'(^(noche)|(noche)$)'
    # EarlyMorningTermList = [r'madrugada']
    # MorningTermList = [r'mañana', r'la mañana']
    # AfternoonTermList = [r'pasado mediodia', r'pasado el mediodia', r'pasado mediodía', r'pasado el mediodía',
    #                      r'pasado medio dia', r'pasado el medio dia', r'pasado medio día', r'pasado el medio día']
    # EveningTermList = [r'tarde']
    # NightTermList = [r'noche']
    # SameDayTerms = [r'hoy', r'el dia']
    # PlusOneDayTerms = [r'mañana', r'dia siguiente', r'el dia de mañana', r'proximo dia']
    # MinusOneDayTerms = [r'ayer', r'ultimo dia', r'dia anterior']
    # PlusTwoDayTerms = [r'pasado mañana', r'dia despues de mañana']
    # MinusTwoDayTerms = [r'anteayer', r'dia antes de ayer']
    # MonthTerms = [r'mes', r'meses']
    # MonthToDateTerms = [r'mes a la fecha', r'mes hasta la fecha']
    # WeekendTerms = [r'finde', r'fin de semana', r'fines de semana']
    # WeekTerms = [r'semana']
    # FortnightTerms = [r'quincena', r'la quincena']
    # YearTerms = [r'año', r'años']
    # YearToDateTerms = [r'año a la fecha', r'año hasta la fecha']
    # SpecialCharactersEquivalent = dict([("á", "a"),
    #                                     ("é", "e"),
    #                                     ("í", "i"),
    #                                     ("ó", "o"),
    #                                     ("ú", "u")])
    # DoubleMultiplierRegex = f'^(bi)(-|\\s)?'
    # DayTypeRegex = f'(d[ií]as?|diari(o|as|amente))$'
    # WeekTypeRegex = f'(semanas?|semanalmente)$'
    # BiWeekTypeRegex = f'(quincenalmente)$'
    # WeekendTypeRegex = f'(fin(es)?\\s+de\\s+semana|finde)$'
    # MonthTypeRegex = f'(mes(es)?|mensual(es|mente)?)$'
    # QuarterTypeRegex = f'(trimestral(es|mente)?)$'
    # SemiAnnualTypeRegex = f'(semestral(es|mente)?)$'
    # YearTypeRegex = f'(años?|anual(mente)?)$'
# pylint: enable=line-too-long
