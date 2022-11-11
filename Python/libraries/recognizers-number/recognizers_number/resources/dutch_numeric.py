# ------------------------------------------------------------------------------
# <auto-generated>
#     This code was generated by a tool.
#     Changes to this file may cause incorrect behavior and will be lost if
#     the code is regenerated.
# </auto-generated>
#
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# ------------------------------------------------------------------------------

from .base_numbers import BaseNumbers
# pylint: disable=line-too-long


class DutchNumeric:
    LangMarker = 'Dut'
    CompoundNumberLanguage = True
    MultiDecimalSeparatorCulture = False
    DigitsNumberRegex = f'-?(\\d+|\\d{{1,3}}(\\.\\d{{3}})*)'
    RoundNumberIntegerRegex = f'(honderd|duizend|miljoen|miljard|biljoen)'
    ZeroToNineIntegerRegex = f'(((een)(?!\\s+((honderdste|duizendste|miljoenste|miljardste|biljoenste)|(nulde|eende|eerste|tweede|derde|vierde|vijfd(e|en)|zesde|zevende|achtst(e|en)|negende|tiend(e|en)|elfde|twaalfde|dertiende|veertiende|vijftiende|zestiende|zeventiende|achttiende|negentiende|twintigste|dertigste|veertigste|vijftigste|zestigste|zeventigste|tachtigste|negentigste))))|(één|drie|zeven|acht|vier|vijf|nul|negen|twee|zes))'
    TwoToNineIntegerRegex = f'(drie|zeven|acht|vier|vijf|negen|twee|zes)'
    NegativeNumberTermsRegex = f'(?<negTerm>(min|negatief)\\s+)'
    NegativeNumberSignRegex = f'^{NegativeNumberTermsRegex}.*'
    AnIntRegex = f'(een|één)(?=\\s)'
    TenToNineteenIntegerRegex = f'(zeventien|dertien|veertien|achttien|negentien|vijftien|zestien|elf|twaalf|tien)'
    TensNumberIntegerRegex = f'(zeventig|twintig|dertig|tachtig|negentig|veertig|vijftig|zestig)'
    SeparaIntRegex = f'((({TenToNineteenIntegerRegex}|({ZeroToNineIntegerRegex}(en|ën){TensNumberIntegerRegex})|{TensNumberIntegerRegex}|{ZeroToNineIntegerRegex}|{RoundNumberIntegerRegex})(\\s*{RoundNumberIntegerRegex})*))|{RoundNumberIntegerRegex}|(({AnIntRegex}(\\s*{RoundNumberIntegerRegex})+))'
    AllIntRegex = f'(((({TenToNineteenIntegerRegex}|({ZeroToNineIntegerRegex}(en|ën){TensNumberIntegerRegex})|{TensNumberIntegerRegex}|({ZeroToNineIntegerRegex}|{AnIntRegex}))?(\\s*{RoundNumberIntegerRegex}))\\s*((en|ën)\\s*)?)*{SeparaIntRegex})'
    PlaceHolderPureNumber = f'\\b'
    PlaceHolderDefault = f'\\D|\\b'

    def NumbersWithPlaceHolder(placeholder):
        return f'(((?<!\\d+\\s*)-\\s*)|(?<=\\b))\\d+(?!(\\,\\d+[a-zA-Z]))(?={placeholder})'
    NumbersWithSuffix = f'(((?<!\\d+\\s*)-\\s*)|(?<=\\b))\\d+\\s*{BaseNumbers.NumberMultiplierRegex}(?=\\b)'
    RoundNumberIntegerRegexWithLocks = f'(?<=\\b)\\d+\\s*{RoundNumberIntegerRegex}(?=\\b)'
    NumbersWithDozenSuffix = f'(((?<!\\d+\\s*)-\\s*)|(?<=\\b))\\d+\\s+dozijn(en)?(?=\\b)'
    AllIntRegexWithLocks = f'((?<=\\b){AllIntRegex}(?=\\b))'
    GrossRegex = f'(een\\s+)?gros'
    AllIntRegexWithDozenSuffixLocks = f'(?<=\\b)(((een\\s+)?half\\s+dozijn)|({AllIntRegex}\\s+dozijn(en)?)|{GrossRegex})(?=\\b)'
    RoundNumberOrdinalRegex = f'(honderdste|duizendste|miljoenste|miljardste|biljoenste)'
    BasicOrdinalRegex = f'(nulde|eende|eerste|tweede|derde|vierde|vijfd(e|en)|zesde|zevende|achtst(e|en)|negende|tiend(e|en)|elfde|twaalfde|dertiende|veertiende|vijftiende|zestiende|zeventiende|achttiende|negentiende|twintigste|vijfentwintigste|vijventwintigste|dertigste|veertigste|vijftigste|zestigste|zeventigste|tachtigste|negentigste)'
    RelativeOrdinalRegex = f'(?<relativeOrdinal>volgende|vorige?|huidige|laatste?|(de\\s+op\\s+één\\s+na\\s+|de\\s+een\\s+voor\\s+de\\s+|die\\s+voor\\s+de\\s+|twee\\s+na\\s+|voor)laatste)'
    SuffixBasicOrdinalRegex = f'(((({ZeroToNineIntegerRegex}{RoundNumberIntegerRegex})|({RoundNumberIntegerRegex}{ZeroToNineIntegerRegex})|{TensNumberIntegerRegex}|{ZeroToNineIntegerRegex}|{RoundNumberIntegerRegex})\\s*)*((en|ën)\\s*)*{BasicOrdinalRegex})'
    SuffixRoundNumberOrdinalRegex = f'(({AllIntRegex}\\s*){RoundNumberOrdinalRegex})'
    AllOrdinalNumberRegex = f'(?:{SuffixBasicOrdinalRegex}|{SuffixRoundNumberOrdinalRegex})'
    AllOrdinalRegex = f'(?:{AllOrdinalNumberRegex}|{RelativeOrdinalRegex})'
    OrdinalSuffixRegex = f'(?<=\\b)((\\d+\\s*e)|[18]\\s*ste|[092-7]\\s*de|([0-9]*1[0-9]\\s*de)|([0-9]*[2-9][0-9]\\s*ste)|([0-9]*[0]([18]\\s*ste|[092-7]\\s*de)))(?=\\b)'
    OrdinalNumericRegex = f'(?<=\\b)(\\d{{1,3}}(\\s*.\\s*\\d{{3}})*\\s*e)(?=\\b)'
    OrdinalRoundNumberRegex = f'(?<!(één|een)\\s+){RoundNumberOrdinalRegex}'
    OrdinalDutchRegex = f'(?<=\\b){AllOrdinalRegex}(?=\\b)'
    FractionNotationWithSpacesRegex = f'(((?<=\\W|^)-\\s*)|(?<=\\b))\\d+\\s+\\d+[/]\\d+(?=(\\b[^/]|$))'
    FractionNotationRegex = f'{BaseNumbers.FractionNotationRegex}'
    FractionUnitsRegex = f'((?<onehalf>anderhalve|anderhalf)|(?<quarter>driekwart)|half|halve|helft|kwart)'
    FractionHalfRegex = f'([eë]nhalf|[eë]nhalve|ëneenhal(f|ve))$'
    OneHalfTokens = [r'een', r'half']
    FractionMultiplierRegex = f'(?<fracMultiplier>((\\s+en\\s+)?(anderhalve|anderhalf|driekwart)|\\s+en\\s+(een|{TwoToNineIntegerRegex})\\s+(half|derde|kwart|vierde|vijfd(e|en)|zesde|zevende|achtst(e|en)|negende|tiend(e|en))))'
    RoundMultiplierWithFraction = f'(?<=(?<!{RoundNumberIntegerRegex}){FractionMultiplierRegex}\\s+)?(?<multiplier>(miljoen|miljard|biljoen))(?={FractionMultiplierRegex}?$)'
    RoundMultiplierRegex = f'\\b\\s*(van\\s+)?({RoundMultiplierWithFraction}|(?<multiplier>(honderd|duizend))$)'
    FractionNounRegex = f'(?<=\\b)(({AllIntRegex}\\s+(en\\s+)?)?(({AllIntRegex})(\\s+|\\s*-\\s*|\\s*/\\s*)((({AllOrdinalNumberRegex})|({RoundNumberOrdinalRegex}))n?|halven|vierdes|kwart)|(een\\s+(half|kwart)\\s+){RoundNumberIntegerRegex}|{FractionUnitsRegex}(\\s+{RoundNumberIntegerRegex})?))(?=\\b)'
    FractionNounWithArticleRegex = f'(?<=\\b)((({AllIntRegex}|{RoundNumberIntegerRegexWithLocks})\\s+(en\\s)?)?(een)(\\s+|\\s*-\\s*|\\s*/\\s*)(({AllOrdinalNumberRegex})|({RoundNumberOrdinalRegex})|({FractionUnitsRegex}))|{AllIntRegex}[eë]n(eenhalf|half|halve|helft|kwart))(?=\\b)'
    FractionPrepositionRegex = f'(?<!{BaseNumbers.CommonCurrencySymbol}\\s*)(?<=\\b)(?<numerator>({AllIntRegex})|((?<!,)\\d+))\\s+(op|op\\s+de|van\\s+de|uit|uit\\s+de)\\s+(?<denominator>({AllIntRegex})|(\\d+)(?!,))(?=\\b)'
    FractionPrepositionWithinPercentModeRegex = f'(?<!{BaseNumbers.CommonCurrencySymbol}\\s*)(?<=\\b)(?<numerator>({AllIntRegex})|((?<!,)\\d+))\\s+over\\s+(?<denominator>({AllIntRegex})|(\\d+)(?!,))(?=\\b)'
    AllPointRegex = f'((\\s+{ZeroToNineIntegerRegex})+|(\\s+{SeparaIntRegex}))'
    AllFloatRegex = f'{AllIntRegex}(\\s+komma){AllPointRegex}'
    DoubleWithMultiplierRegex = f'(((?<!\\d+\\s*)-\\s*)|((?<=\\b)(?<!\\d+,)))\\d+,\\d+\\s*{BaseNumbers.NumberMultiplierRegex}(?=\\b)'
    DoubleExponentialNotationRegex = f'(((?<!\\d+\\s*)-\\s*)|((?<=\\b)(?<!\\d+,)))(\\d+(,\\d+)?)e([+-]*[1-9]\\d*)(?=\\b)'
    DoubleCaretExponentialNotationRegex = f'(((?<!\\d+\\s*)-\\s*)|((?<=\\b)(?<!\\d+,)))(\\d+(,\\d+)?)\\^([+-]*[1-9]\\d*)(?=\\b)'

    def DoubleDecimalPointRegex(placeholder):
        return f'(((?<!\\d+\\s*)-\\s*)|((?<=\\b)(?<!\\d+,)))\\d+,\\d+(?!(,\\d+))(?={placeholder})'

    def DoubleWithoutIntegralRegex(placeholder):
        return f'(?<=\\s|^)(?<!(\\d+)),\\d+(?!(,\\d+))(?={placeholder})'
    DoubleWithRoundNumber = f'(((?<!\\d+\\s*)-\\s*)|((?<=\\b)(?<!\\d+,)))\\d+,\\d+\\s+{RoundNumberIntegerRegex}(?=\\b)'
    DoubleAllFloatRegex = f'((?<=\\b){AllFloatRegex}(?=\\b))'
    NumberWithSuffixPercentage = f'(?<!%)({BaseNumbers.NumberReplaceToken})(\\s*)(%(?!{BaseNumbers.NumberReplaceToken})|(procent|percentage|percent)\\b)'
    FractionNumberWithSuffixPercentage = f'(({BaseNumbers.FractionNumberReplaceToken})\\s+van)'
    NumberWithPrefixPercentage = f'(percentage van)(\\s*)({BaseNumbers.NumberReplaceToken})'
    NumberWithPrepositionPercentage = f'({BaseNumbers.NumberReplaceToken})\\s*(uit|in|van|van\\s+de)\\s*({BaseNumbers.NumberReplaceToken})'
    TillRegex = f'(tot|--|-|—|——|~)'
    IncludeTillRegex = f'(tot en met)'
    MoreRegex = f'((groter|hoger|meer)((\\s+is)?(\\s+dan|\\s+als))?|boven|over|>)'
    LessRegex = f'((minder|lager|kleiner)(\\s+dan|\\s+als)?|beneden|onder|<)'
    EqualRegex = f'(gelijk(\\s+(aan|tot|als|dan))?|(?<!<|>)=)'
    MoreOrEqualPrefix = f'((niet\\s+{LessRegex})|(tenminste|op zijn minst|minstens))'
    MoreOrEqual = f'(({MoreRegex}\\s+of\\s+{EqualRegex})|({EqualRegex}\\s+of\\s+{MoreRegex})|{MoreOrEqualPrefix}(\\s+(of)?\\s+{EqualRegex})?|niet\\s+{LessRegex}|>\\s*=)'
    MoreOrEqualSuffix = f'((en|of)\\s+(meer|groter|hoger|grotere)((?!\\s+(dan|als))|(\\s+(dan|als)(?!(\\s*\\d+)))))'
    LessOrEqualPrefix = f'((niet\\s+{MoreRegex})|(hooguit|op zijn hoogst|op zijn meest))'
    LessOrEqual = f'(({LessRegex}\\s+of\\s+{EqualRegex})|({EqualRegex}\\s+of\\s+{LessRegex})|maximum|niet\\s+{MoreRegex}|<\\s*=)'
    LessOrEqualSuffix = f'((en|of)\\s+(minder|lager|kleiner)((?!\\s+(dan|als))|(\\s+(dan|als)(?!(\\s*\\d+)))))'
    NumberSplitMark = f'(?![,.](?!\\d+))'
    MoreRegexNoNumberSucceed = f'((groter|hoger|meer)((?!\\s+dan)|\\s+(dan(?!(\\s*\\d+))))|(boven|over)(?!(\\s*\\d+)))'
    LessRegexNoNumberSucceed = f'((minder|lager|kleiner)((?!\\s+dan)|\\s+(dan(?!(\\s*\\d+))))|(beneden|onder)(?!(\\s*\\d+)))'
    EqualRegexNoNumberSucceed = f'(gelijk((?!\\s+(aan|tot))|(\\s+(aan|tot)(?!(\\s*\\d+))))|evenveel(?!(\\s*\\d+)))'
    OneNumberRangeMoreRegex1 = f'({MoreOrEqual}|{MoreRegex})\\s*(de\\s+)?(?<number1>({NumberSplitMark}.)+)'
    OneNumberRangeMoreRegex2 = f'(?<number1>({NumberSplitMark}.)+)\\s*{MoreOrEqualSuffix}'
    OneNumberRangeMoreSeparateRegex = f'({EqualRegex}\\s+(?<number1>({NumberSplitMark}.)+)(\\s+of\\s+){MoreRegexNoNumberSucceed})|({MoreRegex}\\s+(?<number1>({NumberSplitMark}.)+)(\\s+of\\s+){EqualRegexNoNumberSucceed})'
    OneNumberRangeLessRegex1 = f'({LessOrEqual}|{LessRegex})\\s*(de\\s+)?(?<number2>({NumberSplitMark}.)+)'
    OneNumberRangeLessRegex2 = f'(?<number2>({NumberSplitMark}.)+)\\s*{LessOrEqualSuffix}'
    OneNumberRangeLessSeparateRegex = f'({EqualRegex}\\s+(?<number1>({NumberSplitMark}.)+)(\\s+of\\s+){LessRegexNoNumberSucceed})|({LessRegex}\\s+(?<number1>({NumberSplitMark}.)+)(\\s+of\\s+){EqualRegexNoNumberSucceed})'
    OneNumberRangeEqualRegex = f'{EqualRegex}\\s*(de\\s+)?(?<number1>({NumberSplitMark}.)+)'
    TwoNumberRangeRegex1 = f'tussen\\s*(de\\s+)?(?<number1>({NumberSplitMark}.)+)\\s+en\\s+(de\\s+)?(?<number2>({NumberSplitMark}.)+)'
    TwoNumberRangeRegex2 = f'({OneNumberRangeMoreRegex1}|{OneNumberRangeMoreRegex2})\\s*(en|(,\\s*)?maar|,)\\s*({OneNumberRangeLessRegex1}|{OneNumberRangeLessRegex2})'
    TwoNumberRangeRegex3 = f'({OneNumberRangeLessRegex1}|{OneNumberRangeLessRegex2})\\s*(en|maar|,)\\s*({OneNumberRangeMoreRegex1}|{OneNumberRangeMoreRegex2})'
    TwoNumberRangeRegex4 = f'(van\\s+)?(?<number1>({AllIntRegex}|{AllFloatRegex}|{AllOrdinalRegex}|{DigitsNumberRegex}))\\s*{TillRegex}\\s*(de\\s+)?(?<number2>({AllIntRegex}|{AllFloatRegex}|{AllOrdinalRegex}|{DigitsNumberRegex}))'
    TwoNumberRangeRegex5 = f'(van\\s+)?(?<number1>({AllIntRegex}|{AllFloatRegex}|{AllOrdinalRegex}|{DigitsNumberRegex}))\\s*{IncludeTillRegex}\\s*(de\\s+)?(?<number2>({AllIntRegex}|{AllFloatRegex}|{AllOrdinalRegex}|{DigitsNumberRegex}))'
    AmbiguousFractionConnectorsRegex = f'^[.]'
    DecimalSeparatorChar = ','
    FractionMarkerToken = 'van de'
    NonDecimalSeparatorChar = '.'
    HalfADozenText = 'zes'
    WordSeparatorToken = 'en'
    WrittenDecimalSeparatorTexts = [r'komma']
    WrittenGroupSeparatorTexts = [r'punt']
    WrittenIntegerSeparatorTexts = [r'en', r'ën']
    WrittenFractionSeparatorTexts = [r'uit', r'van de', r'op de', r'en']
    HalfADozenRegex = f'(een\\s+)?half\\s+dozijn'
    DigitalNumberRegex = f'((?<=\\b)(honderd|duizend|miljoen|miljard|biljoen|dozijn?)(?=\\b))|((?<=(\\d|\\b)){BaseNumbers.MultiplierLookupRegex}(?=\\b))'
    CardinalNumberMap = dict([("nul", 0),
                              ("een", 1),
                              ("één", 1),
                              ("twee", 2),
                              ("drie", 3),
                              ("vier", 4),
                              ("vijf", 5),
                              ("zes", 6),
                              ("zeven", 7),
                              ("acht", 8),
                              ("negen", 9),
                              ("tien", 10),
                              ("elf", 11),
                              ("twaalf", 12),
                              ("dozijn", 12),
                              ("dertien", 13),
                              ("veertien", 14),
                              ("vijftien", 15),
                              ("zestien", 16),
                              ("zeventien", 17),
                              ("achttien", 18),
                              ("negentien", 19),
                              ("twintig", 20),
                              ("dertig", 30),
                              ("veertig", 40),
                              ("vijftig", 50),
                              ("zestig", 60),
                              ("zeventig", 70),
                              ("tachtig", 80),
                              ("negentig", 90),
                              ("honderd", 100),
                              ("gros", 144),
                              ("duizend", 1000),
                              ("miljoen", 1000000),
                              ("miljard", 1000000000),
                              ("biljoen", 1000000000000)])
    OrdinalNumberMap = dict([("nulde", 0),
                             ("eerste", 1),
                             ("eende", 1),
                             ("tweede", 2),
                             ("secundair", 2),
                             ("half", 2),
                             ("halve", 2),
                             ("helft", 2),
                             ("derde", 3),
                             ("vierde", 4),
                             ("kwart", 4),
                             ("vijfde", 5),
                             ("vijfden", 5),
                             ("zesde", 6),
                             ("zevende", 7),
                             ("achtste", 8),
                             ("achtsten", 8),
                             ("negende", 9),
                             ("tiende", 10),
                             ("tienden", 10),
                             ("elfde", 11),
                             ("twaalfde", 12),
                             ("dertiende", 13),
                             ("veertiende", 14),
                             ("vijftiende", 15),
                             ("zestiende", 16),
                             ("zeventiende", 17),
                             ("achttiende", 18),
                             ("negentiende", 19),
                             ("twintigste", 20),
                             ("eenentwintigste", 21),
                             ("vijfentwintigste", 25),
                             ("vijventwintigste", 25),
                             ("dertigste", 30),
                             ("vijfendertigste", 35),
                             ("veertigste", 40),
                             ("vijfenveertigste", 45),
                             ("vijftigste", 50),
                             ("vijfenvijftigste", 55),
                             ("zestigste", 60),
                             ("vijfenzestigste", 65),
                             ("zeventigste", 70),
                             ("vijfenzeventigste", 75),
                             ("tachtigste", 80),
                             ("vijfentachtigste", 85),
                             ("negentigste", 90),
                             ("vijfennegentigste", 95),
                             ("honderdste", 100),
                             ("duizendste", 1000),
                             ("miljoenste", 1000000),
                             ("miljardste", 1000000000),
                             ("biljoenste", 1000000000000),
                             ("biljardste", 1000000000000000),
                             ("triljoenste", 1000000000000000000)])
    RoundNumberMap = dict([("honderd", 100),
                           ("duizend", 1000),
                           ("miljoen", 1000000),
                           ("miljard", 1000000000),
                           ("biljoen", 1000000000000),
                           ("biljard", 1000000000000000),
                           ("triljard", 1000000000000000000),
                           ("honderdste", 100),
                           ("duizendste", 1000),
                           ("miljoenste", 1000000),
                           ("miljardste", 1000000000),
                           ("biljoenste", 1000000000000),
                           ("biljardste", 1000000000000000),
                           ("triljoenste", 1000000000000000000),
                           ("honderdsten", 100),
                           ("duizendsten", 1000),
                           ("miljoensten", 1000000),
                           ("miljardsten", 1000000000),
                           ("biljoensten", 1000000000000),
                           ("dozijn", 12),
                           ("gros", 144),
                           ("k", 1000),
                           ("m", 1000000),
                           ("g", 1000000000),
                           ("b", 1000000000),
                           ("t", 1000000000000)])
    AmbiguityFiltersDict = dict([("^[.]", "")])
    RelativeReferenceOffsetMap = dict([("laatst", "0"),
                                       ("laatste", "0"),
                                       ("volgende", "1"),
                                       ("huidige", "0"),
                                       ("vorige", "-1"),
                                       ("vorig", "-1"),
                                       ("de op één na laatste", "-1"),
                                       ("de een voor de laatste", "-1"),
                                       ("die voor de laatste", "-1"),
                                       ("voorlaatste", "-1"),
                                       ("twee na laatste", "-2")])
    RelativeReferenceRelativeToMap = dict([("laatst", "end"),
                                           ("laatste", "end"),
                                           ("volgende", "current"),
                                           ("huidige", "current"),
                                           ("vorige", "current"),
                                           ("vorig", "current"),
                                           ("de op één na laatste", "end"),
                                           ("de een voor de laatste", "end"),
                                           ("die voor de laatste", "end"),
                                           ("voorlaatste", "end"),
                                           ("twee na laatste", "end")])
# pylint: enable=line-too-long
