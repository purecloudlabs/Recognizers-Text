from .base_numbers import BaseNumbers
# pylint: disable=line-too-long


class CatalanNumeric:
    LangMarker = 'Cat'
    CompoundNumberLanguage = False
    MultiDecimalSeparatorCulture = True
    NonStandardSeparatorVariants = []
    RoundNumberIntegerRegex = f'(?:cents|milers|milions|mil milions|bilió)s?'
    ZeroToNineIntegerRegex = f'(?:tres|set|vuit|quatre|cinc|zero|nou|un|dos|sis)'
    TwoToNineIntegerRegex = f'(?:tres|set|vuit|quatre|cinc|nou|dos|sis)'
    NegativeNumberTermsRegex = f'(?<negTerm>(menys|negatiu)\\s+)'
    NegativeNumberSignRegex = f'^{NegativeNumberTermsRegex}.*'
    TenToNineteenIntegerRegex = f'(?:disset|tretze|catorze|divuit anys|dinou|quinze|setze|onze|dotze|deu)'
    TensNumberIntegerRegex = f'(?:setanta|vint|trenta|vuitanta|noranta|quaranta|cinquanta|seixanta)'

    TwentiesIntegerRegex = f'(vint(\\s?-\\s?|\\s)i(\\s?-\\s?|\\s)(u|{TwoToNineIntegerRegex}))'
    BelowHundredsRegex = f'(({TenToNineteenIntegerRegex}|{TwentiesIntegerRegex}|({TensNumberIntegerRegex}((\\s?-\\s?|\\s)({TwoToNineIntegerRegex}|u))?)|{ZeroToNineIntegerRegex}))'
    HundredsNumberIntegerRegex = f'(({TwoToNineIntegerRegex}(\\s?-\\s?|\\s))?cent(s?))'
    BelowThousandsRegex = f'({HundredsNumberIntegerRegex}(\\s+{BelowHundredsRegex})?|{BelowHundredsRegex})'

    SupportThousandsRegex = f'(({BelowThousandsRegex}|{BelowHundredsRegex})\\s+{RoundNumberIntegerRegex}(\\s+{RoundNumberIntegerRegex})?)'
    SeparaIntRegex = f'({SupportThousandsRegex}(\\s+{SupportThousandsRegex})*(\\s+{BelowThousandsRegex})?|{BelowThousandsRegex})'
    AllIntRegex = f'({SeparaIntRegex}|mil(\\s+{BelowThousandsRegex})?|{RoundNumberIntegerRegex})'

    PlaceHolderPureNumber = f'\\b'
    PlaceHolderDefault = f'(?=\\D)|\\b'
    PlaceHolderMixed = f'\\D|\\b'
    DigitsNumberRegex = f'\\d|\\d{{1,3}}(\\.\\d{{3}})'

    def NumbersWithPlaceHolder(placeholder):
        return f'(((?<!\\d+\\s*)-\\s*)|(?<=\\b))\\d+(?!([\\.,]\\d+[a-zA-Z]))(?={placeholder})'

    NumbersWithSuffix = f'(((?<=\\W|^)-\\s*)|(?<=\\b))\\d+\\s*{BaseNumbers.NumberMultiplierRegex}(?=\\b)'
    RoundNumberIntegerRegexWithLocks = f'(?<=\\b)({DigitsNumberRegex})+\\s+{RoundNumberIntegerRegex}(?=\\b)'
    NumbersWithDozenSuffix = f'(((?<=\\W|^)-\\s*)|(?<=\\b))\\d+\\s+(dotzena)s?(?=\\b)'
    AllIntRegexWithLocks = f'((?<=\\b){AllIntRegex}(?=\\b))'
    # AllIntRegexWithDozenSuffixLocks = f'(?<=\\b)(((half\\s+)?a\\s+dozen)|({AllIntRegex}\\s+(doz(en)?|dz)s?))(?=\\b)'
    RoundNumberOrdinalRegex = f'(?:centèsim|mil·lèssim|milionèsima|mil milions|bilionsè)'
    NumberOrdinalRegex = f'(?:primer|segon[a]?|tercer|quart|cinquè|cinquena|sisè|sisena|setè|setena|vuitè|vuitena|novè|desè|desena|onzè|dotzè|tretzè|catorzè|quinzena|setzè|dissetè|divuitè|dinou|vintè|thirtieth|trent[èe]|cinquantè|seixanta|setanta|vuitanta|noranta)'
    # RelativeOrdinalRegex = f'(?<relativeOrdinal>(next|previous|current)\\s+one|(the\\s+second|next)\\s+to\\s+last|the\\s+one\\s+before\\s+the\\s+last(\\s+one)?|the\\s+last\\s+but\\s+one|(ante)?penultimate|last|next|previous|current)'
    # SuffixBasicOrdinalRegex = f'(?:(((({TensNumberIntegerRegex}(\\s+(and\\s+)?|\\s*-\\s*){ZeroToNineIntegerRegex})|{TensNumberIntegerRegex}|{ZeroToNineIntegerRegex}|{AnIntRegex})(\\s+{RoundNumberIntegerRegex})+)\\s+(and\\s+)?)*({TensNumberIntegerRegex}(\\s+|\\s*-\\s*))?{NumberOrdinalRegex})'
    SuffixRoundNumberOrdinalRegex = f'(?:({AllIntRegex}\\s+){RoundNumberOrdinalRegex})'
    AllOrdinalNumberRegex = f'(?:{SuffixRoundNumberOrdinalRegex})'
    AllOrdinalRegex = f'(?:{AllOrdinalNumberRegex})'
    OrdinalSuffixRegex = f'(?<=\\b)(?:(\\d*(1r|2n|3r|4t|[5-99][èe])))(?=\\b)'
    # OrdinalNumericRegex = f'(?<=\\b)(?:\\d{{1,3}}(\\s*,\\s*\\d{{3}})*\\s*th)(?=\\b)'
    # OrdinalRoundNumberRegex = f'(?<!an?\\s+){RoundNumberOrdinalRegex}'
    # OrdinalEnglishRegex = f'(?<=\\b){AllOrdinalRegex}(?=\\b)'
    # FractionNotationWithSpacesRegex = f'(((?<=\\W|^)-\\s*)|(?<=\\b))\\d+\\s+\\d+[/]\\d+(?=(\\b[^/]|$))'
    # FractionNotationRegex = f'{BaseNumbers.FractionNotationRegex}'
    # FractionMultiplierRegex = f'(?<fracMultiplier>\\s+and\\s+(a|one|{TwoToNineIntegerRegex})\\s+(half|quarter|third|fourth|fifth|sixth|seventh|eighth|nine?th|tenth)s?)'
    # RoundMultiplierWithFraction = f'(?<=(?<!{RoundNumberIntegerRegex}){FractionMultiplierRegex}\\s+)?(?<multiplier>(?:million|mln|billion|bln|trillion|tln)s?)(?={FractionMultiplierRegex}?$)'
    # RoundMultiplierRegex = f'\\b\\s*((of\\s+)?a\\s+)?({RoundMultiplierWithFraction}|(?<multiplier>(?:hundred|thousand|lakh|crore)s?)$)'
    # FractionNounRegex = f'(?<=\\b)({AllIntRegex}\\s+(and\\s+)?)?(({AllIntRegex})(\\s+|\\s*-\\s*)((({AllOrdinalNumberRegex})|({RoundNumberOrdinalRegex}))s|halves|quarters)((\\s+of\\s+a)?\\s+{RoundNumberIntegerRegex})?|(half(\\s+a)?|quarter(\\s+of\\s+a)?)\\s+{RoundNumberIntegerRegex})(?=\\b)'
    # FractionNounWithArticleRegex = f'(?<=\\b)(((({AllIntRegex}|{RoundNumberIntegerRegexWithLocks})\\s+(and\\s+)?)?(an?|one)(\\s+|\\s*-\\s*)(?!\\bfirst\\b|\\bsecond\\b)(({AllOrdinalNumberRegex})|({RoundNumberOrdinalRegex})|(half|quarter)(((\\s+of)?\\s+a)?\\s+{RoundNumberIntegerRegex})?))|(half))(?=\\b)'
    # FractionPrepositionRegex = f'(?<!{BaseNumbers.CommonCurrencySymbol}\\s*)(?<=\\b)(?<numerator>({AllIntRegex})|((?<![\\.,])\\d+))\\s+(over|(?<ambiguousSeparator>in|out\\s+of))\\s+(?<denominator>({AllIntRegex})|(\\d+)(?![\\.,]))(?=\\b)'
    # FractionPrepositionWithinPercentModeRegex = f'(?<!{BaseNumbers.CommonCurrencySymbol}\\s*)(?<=\\b)(?<numerator>({AllIntRegex})|((?<![\\.,])\\d+))\\s+over\\s+(?<denominator>({AllIntRegex})|(\\d+)(?![\\.,]))(?=\\b)'
    AllPointRegex = f'((\\s+{ZeroToNineIntegerRegex})+|(\\s+{SeparaIntRegex}))'
    AllFloatRegex = f'{AllIntRegex}(\\s+coma){AllPointRegex}'

    def DoubleDecimalPointRegex(placeholder):
        return f'(((?<!\\d+\\s*)-\\s*)|((?<=\\b)(?<!\\d+[\\.,])))\\d+[\\.,]\\d+(?!([\\.,]\\d+))(?={placeholder})'

    def DoubleWithoutIntegralRegex(placeholder):
        return f'(?<=\\s|^)(?<!(\\d+))[\\.,]\\d+(?!([\\.,]\\d+))(?={placeholder})'

    DoubleWithMultiplierRegex = f'(((?<!\\d+\\s*)-\\s*)|((?<=\\b)(?<!\\d+\\[\\.,])))\\d+[\\.,]\\d+\\s*{BaseNumbers.NumberMultiplierRegex}(?=\\b)'
    DoubleWithRoundNumber = f'(((?<!\\d+\\s*)-\\s*)|((?<=\\b)(?<!\\d+\\[\\.,])))\\d+[\\.,]\\d+\\s+{RoundNumberIntegerRegex}(?=\\b)'
    DoubleAllFloatRegex = f'((?<=\\b){AllFloatRegex}(?=\\b))'
    DoubleExponentialNotationRegex = f'(((?<!\\d+\\s*)-\\s*)|((?<=\\b)(?<!\\d+[\\.,])))(\\d+([\\.,]\\d+)?)e([+-]*[1-9]\\d*)(?=\\b)'
    DoubleCaretExponentialNotationRegex = f'(((?<!\\d+\\s*)-\\s*)|((?<=\\b)(?<!\\d+[\\.,])))(\\d+([\\.,]\\d+)?)\\^([+-]*[1-9]\\d*)(?=\\b)'

    # NumberWithSuffixPercentage = f'(?<!%({BaseNumbers.NumberReplaceToken})?)({BaseNumbers.NumberReplaceToken}(\\s*))?(%(?!{BaseNumbers.NumberReplaceToken})|(per\\s*cents?|percentage|cents?)\\b)'
    # FractionNumberWithSuffixPercentage = f'(({BaseNumbers.FractionNumberReplaceToken})\\s+of)'
    # NumberWithPrefixPercentage = f'(per\\s*cents?\\s+of)(\\s*)({BaseNumbers.NumberReplaceToken})'
    # NumberWithPrepositionPercentage = f'({BaseNumbers.NumberReplaceToken})\\s*(in|out\\s+of)\\s*({BaseNumbers.NumberReplaceToken})'
    # TillRegex = f'((?<!\\bequal\\s+)to|through|--|-|—|——|~|–)'
    # MoreRegex = f'(?:(bigger|greater|more|higher|larger)(\\s+than)?|above|over|beyond|exceed(ed|ing)?|surpass(ed|ing)?|(?<!<|=)>)'
    # LessRegex = f'(?:(less|lower|smaller|fewer)(\\s+than)?|below|under|(?<!>|=)<)'
    EqualRegex = f'(igual a)'
    # MoreOrEqualPrefix = f'((no\\s+{LessRegex})|(at\\s+least))'
    # MoreOrEqual = f'(?:({MoreRegex}\\s+(or)?\\s+{EqualRegex})|({EqualRegex}\\s+(or)?\\s+{MoreRegex})|{MoreOrEqualPrefix}(\\s+(or)?\\s+{EqualRegex})?|({EqualRegex}\\s+(or)?\\s+)?{MoreOrEqualPrefix}|>\\s*=|≥)'
    # MoreOrEqualSuffix = f'((and|or)\\s+(((more|greater|higher|larger|bigger)((?!\\s+than)|(\\s+than(?!((\\s+or\\s+equal\\s+to)?\\s*\\d+)))))|((over|above)(?!\\s+than))))'
    # LessOrEqualPrefix = f'((no\\s+{MoreRegex})|(at\\s+most)|(up\\s+to))'
    # LessOrEqual = f'(({LessRegex}\\s+(or)?\\s+{EqualRegex})|({EqualRegex}\\s+(or)?\\s+{LessRegex})|{LessOrEqualPrefix}(\\s+(or)?\\s+{EqualRegex})?|({EqualRegex}\\s+(or)?\\s+)?{LessOrEqualPrefix}|<\\s*=|≤)'
    # LessOrEqualSuffix = f'((and|or)\\s+(less|lower|smaller|fewer)((?!\\s+than)|(\\s+than(?!(\\s*\\d+)))))'
    # NumberSplitMark = f'(?![,.](?!\\d+))(?!\\s*\\b(and\\s+({LessRegex}|{MoreRegex})|but|or|to)\\b)'
    # MoreRegexNoNumberSucceed = f'((bigger|greater|more|higher|larger)((?!\\s+than)|\\s+(than(?!(\\s*\\d+))))|(above|over)(?!(\\s*\\d+)))'
    # LessRegexNoNumberSucceed = f'((less|lower|smaller|fewer)((?!\\s+than)|\\s+(than(?!(\\s*\\d+))))|(below|under)(?!(\\s*\\d+)))'
    # EqualRegexNoNumberSucceed = f'(equal(s|ing)?((?!\\s+(to|than))|(\\s+(to|than)(?!(\\s*\\d+)))))'
    # OneNumberRangeMoreRegex1 = f'({MoreOrEqual}|{MoreRegex})\\s*(the\\s+)?(?<number1>({NumberSplitMark}.)+)'
    # OneNumberRangeMoreRegex1LB = f'(?<!no\\s+){OneNumberRangeMoreRegex1}'
    # OneNumberRangeMoreRegex2 = f'(?<number1>({NumberSplitMark}.)+)\\s*{MoreOrEqualSuffix}'
    # OneNumberRangeMoreSeparateRegex = f'({EqualRegex}\\s+(?<number1>({NumberSplitMark}.)+)(\\s+or\\s+){MoreRegexNoNumberSucceed})|({MoreRegex}\\s+(?<number1>({NumberSplitMark}.)+)(\\s+or\\s+){EqualRegexNoNumberSucceed})'
    # OneNumberRangeLessRegex1 = f'({LessOrEqual}|{LessRegex})\\s*(the\\s+)?(?<number2>({NumberSplitMark}.)+)'
    # OneNumberRangeLessRegex1LB = f'(?<!no\\s+){OneNumberRangeLessRegex1}'
    # OneNumberRangeLessRegex2 = f'(?<number2>({NumberSplitMark}.)+)\\s*{LessOrEqualSuffix}'
    # OneNumberRangeLessSeparateRegex = f'({EqualRegex}\\s+(?<number1>({NumberSplitMark}.)+)(\\s+or\\s+){LessRegexNoNumberSucceed})|({LessRegex}\\s+(?<number1>({NumberSplitMark}.)+)(\\s+or\\s+){EqualRegexNoNumberSucceed})'
    # OneNumberRangeEqualRegex = f'(?<!\\bthan\\s+or\\s+){EqualRegex}\\s*(the\\s+)?(?<number1>({NumberSplitMark}.)+)'
    # TwoNumberRangeRegex1 = f'between\\s*(the\\s+)?(?<number1>({NumberSplitMark}.)+)\\s*and\\s*(the\\s+)?(?<number2>({NumberSplitMark}.)+)'
    # TwoNumberRangeRegex2 = f'({OneNumberRangeMoreRegex1}|{OneNumberRangeMoreRegex2})\\s*(and|but|,)\\s*({OneNumberRangeLessRegex1}|{OneNumberRangeLessRegex2})'
    # TwoNumberRangeRegex3 = f'({OneNumberRangeLessRegex1}|{OneNumberRangeLessRegex2})\\s*(and|but|,)\\s*({OneNumberRangeMoreRegex1}|{OneNumberRangeMoreRegex2})'
    # TwoNumberRangeRegex4 = f'(from\\s+)?(?<number1>({NumberSplitMark}(?!\\bfrom\\b).)+)\\s*{TillRegex}\\s*(the\\s+)?(?<number2>({NumberSplitMark}.)+)'
    AmbiguousFractionConnectorsRegex = f'(\\b(en|a)\\b)'
    DecimalSeparatorChar = ','
    # FractionMarkerToken = 'over'
    NonDecimalSeparatorChar = '.'
    HalfADozenText = 'sis'
    WordSeparatorToken = 'i'
    WrittenDecimalSeparatorTexts = [r'coma']
    WrittenGroupSeparatorTexts = [r'punto']
    WrittenIntegerSeparatorTexts = [r'i']
    HalfADozenRegex = f'mitja\\s+dotzena'
    DigitalNumberRegex = f'((?<=\\b)(cent|milers|mil|milions|mil milions|bili[óo])(?=\\b))|((?<=(\\d|\\b)){BaseNumbers.MultiplierLookupRegex}(?=\\b))'
    CardinalNumberMap = dict([("zero", 0),
                              ("una", 1),
                              ("un", 1),
                              ("u", 1),
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
                              ("dotzena", 12),
                              ("dotzenes", 12),
                              ("tretze", 13),
                              ("catorze", 14),
                              ("quinze", 15),
                              ("setze", 16),
                              ("disset", 17),
                              ("divuit", 18),
                              ("dinnou", 19),
                              ("vint", 20),
                              ("trenta", 30),
                              ("quaranta", 40),
                              ("cinquanta", 50),
                              ("seixanta", 60),
                              ("setanta", 70),
                              ("vuitanta", 80),
                              ("noranta", 90),
                              ("cent", 100),
                              ("dos-cents", 200),
                              ("doscents", 200),
                              ("dos cents", 200),
                              ("tres-cents", 300),
                              ("trescents", 300),
                              ("tres cents", 300),
                              ("quatre-cents", 400),
                              ("quatre cents", 400),
                              ("quatrecents", 400),
                              ("cinc-cents", 500),
                              ("cinc cents", 500),
                              ("cinccents", 500),
                              ("sis-cents", 600),
                              ("sis cents", 600),
                              ("siscents", 600),
                              ("set-cents", 700),
                              ("set cents", 700),
                              ("setcents", 700),
                              ("vuit-cents", 800),
                              ("vuit cents", 800),
                              ("vuitcents", 800),
                              ("nou-cents", 900),
                              ("nou cents", 900),
                              ("noucents", 900),
                              ("mil", 1000),
                              ("milions", 1000000),
                              ("bilió", 1000000000000),
                              ("centenars", 100),
                              ("milers", 1000),
                              ("milers de milions", 1000000000),
                              ("bilions", 1000000000000)])
    OrdinalNumberMap = dict([("primer", 1),
                             ("segon", 2),
                             ("secundari", 2),
                             ("la meitat", 2),
                             ("tercer", 3),
                             ("quart", 4),
                             ("cinquè", 5),
                             ("sisè", 6),
                             ("setè", 7),
                             ("vuitè", 8),
                             ("novè", 9),
                             ("desè", 10),
                             ("onzè", 11),
                             ("dotzè", 12),
                             ("tretzè", 13),
                             ("catorzè", 14),
                             ("quinzè", 15),
                             ("setze", 16),
                             ("disset", 17),
                             ("divuitena", 18),
                             ("dinovena", 19),
                             ("vintè", 20),
                             ("trenta", 30),
                             ("quaranta", 40),
                             ("cinquantè", 50),
                             ("seixanta", 60),
                             ("setanta", 70),
                             ("80è", 80),
                             ("noranta", 90),
                             ("centèsima", 100),
                             ("milè", 1000),
                             ("milionèsima", 1000000),
                             ("bil·lionèsima", 1000000000000)])
    RoundNumberMap = dict([("cent", 100),
                           ("mil", 1000),
                           ("milions", 1000000),
                           ("mln", 1000000),
                           ("mil milions", 1000000000),
                           ("bln", 1000000000),
                           ("bilió", 1000000000000),])
    AmbiguityFiltersDict = dict([("^[.]", "")])
# pylint: enable=line-too-long
