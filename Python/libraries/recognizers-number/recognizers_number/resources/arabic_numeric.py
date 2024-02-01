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


class ArabicNumeric:
    LangMarker = 'Ara'
    CompoundNumberLanguage = False
    MultiDecimalSeparatorCulture = True
    RoundNumberIntegerRegex = f'(?:الفا|أحد عشر|ألفاً|الاف|الدستات|الاثنين|الاثنان|الصفر|التريليون|المليار|وتسعمائة|وثمانمائة|وسبعمائة|وستمائة|وخمسمائة|وأربعمائة|أربعمائة|وثلاثمائة|ومائتان|وثلاثون|اثنى عشر|إحدى عشر|ألفان|ثمانمائة|ثلاثمائة|ومائة|المليون|مليونًا|مائتان|مائة|مائتين|ثلاثمائه|أربعة مئة|خمسمائة|ستمائة|سبعمائة|ثمان مائة|تسعمائة|تريليون|ترليون|آلاف|تريليونين|تريليونات|مليار|ملياري|مليارات|مليون|مليونان|ملايين|ألف|مليونين|ألفين|مئة|الف|ومائتين|الفين|بألفي|بألفين|مئتان|الآف)'
    ZeroToNineIntegerRegex = f'(وخمسة|و خمسة|بإثنان|وواحد|و واحد|واحد|وأربعة|و أربعة|واثنان|اثنان|إثنان|وثلاثة|و ثلاثة|ثلاثة|واربعة|أربع|أربعة|خمسة|وستة|و ستة|بستة|ستة|وسبعة|و سبعة|سبعة|وثمانية|و ثمانية|ثمانية|ثمانٍ|وتسعة|و تسعة|تسع|أحد|اثني|إثني|ثلاث|صفر|سبع|ست|اربع|أربع|السادس|الثامنة|تسعة|اثنين|واحدُ|وإثنين|وواحدُ|الواحد:?)'
    TwoToNineIntegerRegex = f'(?:ثلاث|ثلاثة|سبعة|ثمان|ثمانية|أربع|أربعة|خمسة|تسعة|اثنان|اثنتان|اثنين|اثتنين|اثنتان|إثنان|إثنتان|إثنين|إثتنين|إثنتان|ست|بستة|ستة)'
    NegativeNumberTermsRegex = f'(?<negTerm>(سالب|ناقص)(\\s+)?)'
    NegativeNumberSignRegex = f'^{NegativeNumberTermsRegex}.*'
    AnIntRegex = f'(واحد|أحد)(?=\\s)'
    TenToNineteenIntegerRegex = f'(?:((ثلاث|ثلاثة|سبعة|ثمان|ثمانية|أربع|أربعة|خمسة|تسعة|اثنان|اثنان|اثنين|اثتنين|اثنتان|إثنان|إثنتان|إثنين|إثتنين|إثنتان|ستة|أحد|أربعة|إثني|اثني)\\s(عشر|عشرة)))'
    TensNumberIntegerRegex = f'(عشرة|عشرون|ثلاثون|أربعون|خمسون|ستون|سبعون|ثمانون|تسعين|وعشرين|و عشرين|وثلاثين|و ثلاثين|وأربعين|و أربعين|وخمسين|و خمسين|وستين|وستين|وسبعين|و سبعين|وثمانين|و ثمانين|وتسعين|وتسعين|وعشرون|ثلاثون|وأربعون|و أربعون|وخمسون|و خمسون|وستون|و ستون|وسبعون|و سبعون|وثمانون|و ثمانون|وتسعون|و تسعون|عشرين|ثلاثين|أربعين|خمسين|ستين|سبعين|ثمانين|تسعون|العشرون:?)'
    SeparaIntRegex = f'(?:((({RoundNumberIntegerRegex}\\s{RoundNumberIntegerRegex})|{TenToNineteenIntegerRegex}|({ZeroToNineIntegerRegex}(((و)?)\\s+(و)?|\\s*-\\s*){TensNumberIntegerRegex})|{TensNumberIntegerRegex}|{ZeroToNineIntegerRegex}|{RoundNumberIntegerRegex})(\\s+{RoundNumberIntegerRegex})*))|(((\\s+{RoundNumberIntegerRegex})+))'
    AllIntRegex = f'(?:({SeparaIntRegex})((\\s+(و)?)({SeparaIntRegex})(\\s+{RoundNumberIntegerRegex})?)*|((({TenToNineteenIntegerRegex}|({TensNumberIntegerRegex}(\\s+(و)?|\\s*-\\s*){ZeroToNineIntegerRegex})|{TensNumberIntegerRegex}|{ZeroToNineIntegerRegex})?(\\s+{RoundNumberIntegerRegex})+)\\s+(و)?)*{SeparaIntRegex})'
    PlaceHolderPureNumber = f'\\b'
    PlaceHolderDefault = f'\\D|\\b'

    def NumbersWithPlaceHolder(placeholder):
        return f'(((?<!\\d+\\s*)([-]\\s*)?)|(?<=\\b))\\d+(?!([\\.،,]\\d+[\\u0621-\\u064A]))(?={placeholder})'
    NumbersWithSuffix = f'(((?<!\\d+\\s*)([-]\\s*)?)|(?<=\\b))\\d+\\s*{BaseNumbers.NumberMultiplierRegex}(?=\\b)'
    RoundNumberIntegerRegexWithLocks = f'(?<=\\b)(\\d+\\s*({RoundNumberIntegerRegex})(\\s|و\\s|\\sو))?\\d+(\\s|و\\s|\\sو)+{RoundNumberIntegerRegex}((\\s*و\\s*)+\\d+)?(?=\\b)'
    NumbersWithDozenSuffix = f'(((?<!\\d+\\s*)([-]\\s*)?)|(?<=\\b))(\\d+\\s+)?(دستة|دستات|دست|دزينة|دزينات|دزينتين)(?=\\b)'
    AllIntRegexWithLocks = f'((?<=\\b){AllIntRegex}(?=\\b))'
    AllIntRegexWithDozenSuffixLocks = f'(?<=\\b)(((نصف\\s+)(دزينة|دستة|دستات|دست|دزينات|دزينتين))|({AllIntRegex}(و)?\\s+((و)?))(دزينة|دستة|دستات|دست|دزينات|دزينتين))(?=\\b)'
    RoundNumberOrdinalRegex = f'(?:((من|على)\\s+)({RoundNumberIntegerRegex}))'
    NumberOrdinalRegex = f'(اخماس|ثلثان|واحد جزء من|أجزاء من|المئتيان|مائتي|الحاديه عشر|سابعًا|خامسا|ثانيا|أول|الأول|الثاني|الثالث|الرابع|الخامس|السابع|الثامن|التاسع|الأولى|الثانية|الثالثة|الرابعة|الخامسة|السادسة|السابعة|التاسعة|السادس عشر|السابعة عشرة|السادسة عشرة|الثالثة عشرة|الحادية عشرة|السابع عشر|سادس عشر|الخامس عشر|الحادية عَشْرةَ|الثانيَ عَشَر|الثانيةَ عَشْرةَ|الثالثَ عَشَرَ|الثالثةَ عَشْرةَ|الرابعَ عَشَرَ|الرابعةَ عَشْرةَ|الخامِسَ عَشَرَ|الخامسةَ عَشْرةَ|السادِسَ عَشَرَ|السادسةَ عَشْرةَ|السابعَ عَشَرَ|السابعةَ عَشْرةَ|الثامنَ عَشَرَ|الثامنةَ عَشْرةَ|التاسعَ عَشَرَ|التاسعةَ عَشْرةَ|الحادِيَ عَشَرَ|الحادي عشر|الثاني عشر|الثالث عشر|الرابع عشر|الثامن عشر|التاسع عشر|الثانية عشرة|الرابعة عشرة|الخامسة عشرة|الثامنة عشرة|التاسعة عشرة|العاشر|العاشرة|عشرون|العشرين|الثلاثين|الثلاثون|الرابعة والأربعون|الرابع والأربعون|خمسون|الخمسون|الستين|ستون|والستين|سبعون|السبعون|والسبعون|ثامن عشر|الثامن عشر|الرابع والأربعين|الثامنة والثمانون|الثامن|والثمانين|وثلثان|ثمن|أثمان|التاسع والتسعون|التاسعة والتسعون|اثمان|خمس|أخماس|وثلاثون|ثلثان|الأخماس|اخماس|ثلثان|واحد جزء من|العشرون|التريليون|الواحد والعشرون|العشرين|الحادي والعشرين|الثاني والعشرين|الثالث والعشرين|الرابع والعشرين|الخامس والعشرين|السادس والعشرين|السابع والعشرين|الثامن والعشرين|التاسع والعشرين|الثلاثين|الحادي والثلاثين|الخامسة والعشرون:?)'
    RelativeOrdinalRegex = f'(?<relativeOrdinal>(الواحد\\s)?((السابق|السابقة|الثانية الى|((الذي)\\s*(قبل|قبلا)\\s*)?(الأخير)|قبل|بعد|سبق|سبقت|التالي|الحالي|الذي|اخر)(\\s))?((تالي|الحالي|السابقة|سابق|قادم|التالي|((الذي)\\s*(قبل|قبلا)\\s*)?(الأخير)|آخر|أخير|حالي|اخر|الاخير|الأولى)(ة)?)|(الاخر|الاول|الأول|اول|الأولى|((الذي)\\s*(قبل|قبلا)\\s*)?(الأخير)|السابق|التالي|أخر))'
    BasicOrdinalRegex = f'({NumberOrdinalRegex}|{RelativeOrdinalRegex})'
    SuffixBasicOrdinalRegex = f'(?:(((({TensNumberIntegerRegex}(\\s+(و)?|\\s*){ZeroToNineIntegerRegex})|{TensNumberIntegerRegex}|{ZeroToNineIntegerRegex}|({RoundNumberIntegerRegex}|المئة(\\s+(و)?)))((\\s+{RoundNumberIntegerRegex}|المئة)+|({BasicOrdinalRegex})))\\s+(و)?)*({TensNumberIntegerRegex}(\\s+|\\s*))?{BasicOrdinalRegex}|({TensNumberIntegerRegex}))'
    SuffixRoundNumberOrdinalRegex = f'(?:({AllIntRegex}\\s+){RoundNumberOrdinalRegex})'
    AllOrdinalRegex = f'(?:{SuffixBasicOrdinalRegex}|{SuffixRoundNumberOrdinalRegex})'
    OrdinalNumericRegex = f'(?<=\\b)(?:\\d{{1,3}}(\\s*,\\s*\\d{{3}})*\\s*th)(?=\\b)'
    OrdinalRoundNumberRegex = f'({RoundNumberOrdinalRegex})'
    OrdinalEnglishRegex = f'(?<=\\b){AllOrdinalRegex}(?=\\b)'
    FractionNotationWithSpacesRegex = f'(((?<={{?[\\u0600-\\u06ff]}}|^)-\\s*)|(?<=\\b))\\d+\\s+\\d+[/]\\d+(?=(\\b[^/]|$))'
    FractionNotationWithSpacesRegex2 = f'(((?<={{?[\\u0600-\\u06ff]}}|^)-\\s*)|(?<![/-])(?<=\\b))\\d+[/]\\d+(?=(\\b[^/]|$))(\\s*\\d+)'
    FractionNotationRegex = f'(((?<={{?[\\u0600-\\u06ff]}}|^)-\\s*)|(?<![/-])(?<=\\b))\\d+[/]\\d+(?=(\\b[^/]|$))'
    ArabicBuiltInFraction = f'(ثلثان|ربع|خمس|عشرونات|ثلاثون|خُمسَين:?)'
    FractionOrdinalPrefix = f'(الوزن|المحتوى:?)'
    FractionNounRegex = f'(?<=\\b){ArabicBuiltInFraction}|{AllIntRegex}\\s(و\\s|و){ArabicBuiltInFraction}|(({AllIntRegex}\\s(و\\s|و)?)?({AllIntRegex})(\\s+|\\s*)(({AllOrdinalRegex})|({RoundNumberOrdinalRegex})|أرباع|وربع|ارباع|واحد وربع|نصف|ربع|أنصاف|ربعين|أرباع|ارباع))(?=\\b)'
    FractionNounWithArticleRegex = f'(?<=\\b)((({AllIntRegex}(\\s|(\\s*-\\s*)|و\\s+)?)(({AllOrdinalRegex})|{NumberOrdinalRegex}|نصف|وربع|ربع|ونصف))|(الربع|النصف|نصف|))(?=\\b)'
    FractionPrepositionRegex = f'(?<!{BaseNumbers.CommonCurrencySymbol}\\s*)(?<=\\b)(?<numerator>({AllIntRegex})|((?<![\\.,])\\d+))\\s+(فوق|على|في|جزء|من|أجزاء من|اجزاء من|جزء من)\\s+(?<denominator>({AllIntRegex})|(\\d+)(?![\\.,]))(?=\\b)'
    FractionPrepositionWithinPercentModeRegex = f'(?<!{BaseNumbers.CommonCurrencySymbol}\\s*)(?<=\\b)(?<numerator>({AllIntRegex})|((?<![\\.,])\\d+))\\s+على\\s+(?<denominator>({AllIntRegex})|(\\d+)(?![\\.,]))(?=\\b)'
    FractionWithOrdinalPrefix = f'({AllOrdinalRegex})(?=\\s*({FractionOrdinalPrefix}))'
    FractionWithPartOfPrefix = f'((جزء من)\\s+)({AllIntRegexWithLocks})'
    AllPointRegex = f'((\\s+{ZeroToNineIntegerRegex})+|(\\s+{SeparaIntRegex}))'
    AllFloatRegex = f'{AllIntRegex}(\\s+(نقطة|جزء|جزء من)){AllPointRegex}'
    DoubleWithMultiplierRegex = f'(((?<!\\d+\\s*)([-]\\s*)?)|((?<=\\b)(?<!\\d+[\\.,])))\\d+\\u202A?[\\.,]\\u202A?\\d+\\s*{BaseNumbers.NumberMultiplierRegex}(?=\\b)'
    DoubleExponentialNotationRegex = f'(((?<!\\d+\\s*)([-]\\s*)?)|((?<=\\b)(?<!\\d+[\\.,])))(\\d+(\\u202A?[\\.,]\\u202A?\\d+)?)e([+-]*[\\u0660-\\u0669]\\d*)(?=\\b)'
    DoubleCaretExponentialNotationRegex = f'(((?<!\\d+\\s*)([-]\\s*)?)|((?<=\\b)(?<!\\d+[\\.,])))(\\d+(\\u202A?[\\.,]\\u202A?\\d+)?)[+-]*\\^([+-]*[\\u0660-\\u0669]([\\.,])?\\d*)(?=\\b)'

    def DoubleDecimalPointRegex(placeholder):
        return f'(((?<!\\d+\\s*)([-]\\s*)?)|((?<=\\b)(?<!\\d+[\\.,])))((?<!\\d.)(\\d+\\u202A?[\\.,]\\u202A?\\d+))(?!([\\.,]\\d+))(?={placeholder})'

    def DoubleWithoutIntegralRegex(placeholder):
        return f'(?<=\\s|^)(?<!(\\d+))\\u202A?[\\.,]\\u202A?\\d+(?!([\\.,]\\d+))(?={placeholder})'
    DoubleWithRoundNumber = f'(((?<!\\d+\\s*)([-]\\s*)?)|((?<=\\b)(?<!\\d+[\\.,])))\\d+\\u202A?[\\.,]\\u202A?\\d+\\s+{RoundNumberIntegerRegex}(?=\\b)'

    def DoubleWithThousandMarkRegex(placeholder):
        return f'(((?<!\\d+\\s*)-\\s*)|((?<=\\b)(?<!\\d+\\.|\\d+,)))\\d{{1,3}}(\\u202A?[،]\\u202A?\\d{{3}})+\\u202A?[\\.,]\\u202A?\\d+(?={placeholder})'
    DoubleAllFloatRegex = f'((?<=\\b){AllFloatRegex}(?=\\b))'
    ConnectorRegex = f'(?<spacer>و)'
    NumberWithSuffixPercentage = f'((?<!(٪|%))({BaseNumbers.NumberReplaceToken})(\\s*)((٪|%)(?!{BaseNumbers.NumberReplaceToken})|(بالمائة|في المئة|بالمئة)))'
    FractionNumberWithSuffixPercentage = f'(({BaseNumbers.FractionNumberReplaceToken})\\s+(من|في المئة))'
    NumberWithPrefixPercentage = f'(نسبة|بالمائة)(\\s*)({BaseNumbers.NumberReplaceToken})'
    NumberWithPrepositionPercentage = f'({BaseNumbers.NumberReplaceToken})\\s*(في|خارج\\s+من)\\s*({BaseNumbers.NumberReplaceToken})'
    TillRegex = f'(الى|إلى|خلال|--|-|—|——|~|–)'
    MoreRegex = f'(?:(اكثر|فوق|أكبر|أعظم|أطول|يتجاوز|تفوق|أعلى|أكثر)|(?<!<|=)>)'
    LessRegex = f'(?:(أقل|اقل|اصغر|أصغر|أخفض|ادنى)(\\s*من)?|تحت|(?<!>|=)<)'
    EqualRegex = f'(يساوي|(?<!<|>)=)'
    MoreOrEqualPrefix = f'(((ليس|لا)\\s+{LessRegex})|(على\\s+الأقل))'
    MoreOrEqual = f'(?:(({MoreRegex}(\\s+من)?)\\s+(أو|او)?\\s+{EqualRegex})|(({MoreOrEqualPrefix}|(تفوق))(\\s+(أو|او)?\\s+{EqualRegex})?)|(({EqualRegex}\\s+(أو|او)?\\s+)?({MoreOrEqualPrefix}|تفوق))|>\\s*=)'
    MoreOrEqualSuffix = f'((أو|او)\\s+(((أكبر|أعظم|أطول|فوق|اكثر|اكثر|اكبر|أكثر)((?!\\s+من)|(\\s+من(?!(\\s*\\d+)))))|((فوق|أكبر|أطول|اكثر)(?!\\s+من))))'
    LessOrEqualPrefix = f'((ليس\\s+{MoreRegex})|(at\\s+most)|(بحد أقصى)|(يصل الى))'
    LessOrEqual = f'(((لا\\s*)?{LessRegex}\\s+(أو|او)?\\s+{EqualRegex})|({EqualRegex}\\s+(أو|او)?\\s+(((أقل|اقل|أدنى|اصغر|أصغر|ادنى)(\\s+من))|تحت|(?<!>|=)<))|({LessOrEqualPrefix}(\\s+(أو|او)?\\s+{EqualRegex})?)|(({EqualRegex}\\s+(أو|او)?\\s+)?{LessOrEqualPrefix})|<\\s*=)'
    LessOrEqualSuffix = f'((أ|ا)?و\\s+(أقل)((?!\\s+من)|(\\s+من(?!(\\s*\\d+)))))'
    NumberSplitMark = f'(?![.،](?!\\d+))'
    MoreRegexNoNumberSucceed = f'((أكبر|أعظم|أطول|فوق|اكثر)((?!\\s+من)|\\s+(من(?!(\\s*\\d+))))|(فوق|أكبر|أعظم)(?!(\\s*\\d+)))'
    LessRegexNoNumberSucceed = f'((أقل|أصغر)((?!\\s+من)|\\s+(من(?!(\\s*\\d+))))|(تحت|اقل|أقل|أصغر)(?!((\\s*\\d+)|\\s*من)))'
    EqualRegexNoNumberSucceed = f'((يساوي)(?!(\\s*\\d+)))'
    OneNumberRangeMoreRegex1 = f'({MoreOrEqual})\\s*(ال)?(?<number1>({NumberSplitMark}.)+)|({EqualRegex}\\s*(أو|او)?\\s+({MoreRegex}))(\\s+(من))\\s*(?<number1>({NumberSplitMark}.)+)|({EqualRegex}\\s+(أو|او)?\\s+({MoreRegex}))\\s*(?<number1>({NumberSplitMark}.)+)|({MoreRegex})(\\s+(من))\\s*(?<number1>({NumberSplitMark}.)+)|({MoreRegex})\\s*(?<number1>({NumberSplitMark}.)+)'
    OneNumberRangeMoreRegex3 = f'(?<number1>({NumberSplitMark}.)+)\\s*(و|أو)\\s*({MoreRegex})'
    OneNumberRangeMoreRegex2 = f'(?<number1>({NumberSplitMark}.)+)\\s*{MoreOrEqualSuffix}'
    OneNumberRangeMoreSeparateRegex = f'({MoreRegex}\\s*(من)\\s+(?<number1>({NumberSplitMark}.)+)\\s+(أو|او)\\s+{EqualRegexNoNumberSucceed})|({EqualRegex}\\s+(?<number1>({NumberSplitMark}.)+)(\\s+(أو|او)\\s+){MoreRegexNoNumberSucceed})|({MoreRegex}\\s+(?<number1>({NumberSplitMark}.)+)(\\s+(أو|او)\\s+){EqualRegexNoNumberSucceed})'
    OneNumberRangeLessRegex1 = f'(({LessOrEqual})\\s*(ال)?(?<number2>({NumberSplitMark}.)+))|(لا\\s*)?((((أقل|اقل|أدنى|اصغر|أصغر|ادنى)(\\s+من))|تحت|(?<!>|=)<))\\s*(ال)?(?<number2>({NumberSplitMark}.)+)|(لا\\s*)?(({LessRegex})\\s*(ال)?(?<number2>({NumberSplitMark}.)+))'
    OneNumberRangeLessRegex2 = f'(?<number2>({NumberSplitMark}.)+)\\s*{LessOrEqualSuffix}'
    OneNumberRangeLessSeparateRegex = f'({EqualRegex}\\s+(?<number1>({NumberSplitMark}.)+)\\s*(أو|او)\\s+{LessRegexNoNumberSucceed})|(((((أقل|اقل|أدنى|اصغر|أصغر|ادنى)(\\s+من))|تحت|(?<!>|=)<))\\s+(?<number1>({NumberSplitMark}.)+)(\\s+(أو|او)\\s+){EqualRegexNoNumberSucceed})'
    OneNumberRangeEqualRegex = f'{EqualRegex}\\s*(ال)?(?<number1>({NumberSplitMark}.)+)'
    TwoNumberRangeRegex1 = f'بين\\s*(ال)?(?<number1>({NumberSplitMark}.)+)\\s*و\\s*(ال)?(?<number2>({NumberSplitMark}.)+)'
    TwoNumberRangeRegex2 = f'({OneNumberRangeMoreRegex1}|{OneNumberRangeMoreRegex2})\\s*(،)?\\s*((أ|ا)?و|لكن|,)\\s*({OneNumberRangeLessRegex1}|{OneNumberRangeLessRegex2})'
    TwoNumberRangeRegex3 = f'({OneNumberRangeLessRegex1}|{OneNumberRangeLessRegex2})\\s*(،)?\\s*((أ|ا)?و|لكن|,)\\s*({OneNumberRangeMoreRegex1}|{OneNumberRangeMoreRegex2})'
    TwoNumberRangeRegex4 = f'((من\\s)(?<number1>({NumberSplitMark}(?!\\bمن\\b).)+)\\s*{TillRegex}\\s*(ال\\s+)?(?<number2>({NumberSplitMark}.)+))|((من\\s)?(?<number1>({NumberSplitMark}(?!\\bمن\\b).)+)\\s*{TillRegex}\\s*(ال\\s+)?(?<number2>({NumberSplitMark}.)+))'
    AmbiguousFractionConnectorsRegex = f'(\\bمن|بين|من|بين\\b)'
    DecimalSeparatorChar = '.'
    FractionMarkerToken = 'أكثر'
    NonDecimalSeparatorChar = ','
    HalfADozenText = 'ستة'
    WordSeparatorToken = 'و'
    WrittenDecimalSeparatorTexts = [r'نقطة | فاصلة']
    WrittenGroupSeparatorTexts = [r'punto']
    WrittenIntegerSeparatorTexts = [r'و']
    WrittenFractionSeparatorTexts = [r'و']
    HalfADozenRegex = f'نصف?\\sدستة'
    DigitalNumberRegex = f'((?<=\\b)(مائة|مائتان|دست|دستات|ألف|ألفين|مائتين|ألفين|ثلاثمائة|أربعمائة|خمسمائة|ستمائة|سبعمائة|تسعمائة|ثمانمائة|مليون|آلاف|مليار|ترليون)(?=\\b))|((?<=(\\d|\\b)){BaseNumbers.MultiplierLookupRegex}(?=\\b))'
    CardinalNumberMap = dict([("واحد", 1),
                              ("صفر", 0),
                              ("اثنان", 2),
                              ("اثنين", 2),
                              ("ثلاث", 3),
                              ("ثلاثة", 3),
                              ("أربعة", 4),
                              ("خمسة", 5),
                              ("ستة", 6),
                              ("بستة", 6),
                              ("سبعة", 7),
                              ("ثمانية", 8),
                              ("تسعة", 9),
                              ("عشرة", 10),
                              ("إحدى عشر", 11),
                              ("أحد عشر", 11),
                              ("اثنى عشر", 12),
                              ("اثني عشر", 12),
                              ("دستة", 12),
                              ("دستات", 12),
                              ("ثلاثة عشر", 13),
                              ("أربعة عشر", 14),
                              ("خمسة عشر", 15),
                              ("ستة عشر", 16),
                              ("سبعة عشر", 17),
                              ("ثمانية عشر", 18),
                              ("تسعة عشر", 19),
                              ("عشرون", 20),
                              ("عشرين", 20),
                              ("وعشرون", 20),
                              ("ثلاثون", 30),
                              ("ثلاثين", 30),
                              ("وثلاثون", 30),
                              ("أربعون", 40),
                              ("أربعين", 40),
                              ("وأربعون", 40),
                              ("خمسون", 50),
                              ("وخمسون", 50),
                              ("ستون", 60),
                              ("ستين", 60),
                              ("وستون", 60),
                              ("سبعون", 70),
                              ("وسبعون", 70),
                              ("ثمانون", 80),
                              ("وثمانون", 80),
                              ("تسعون", 90),
                              ("تسعين", 90),
                              ("وتسعون", 90),
                              ("مائة", 100),
                              ("مئة", 100),
                              ("ومائة", 100),
                              ("مائتان", 200),
                              ("مئتان", 200),
                              ("ومائتان", 200),
                              ("مائتين", 200),
                              ("ومائتين", 200),
                              ("ثلاثمائة", 300),
                              ("ثلاثمائه", 300),
                              ("وثلاثمائة", 300),
                              ("أربعمائة", 400),
                              ("أربعة مئة", 400),
                              ("وأربعمائة", 400),
                              ("خمسمائة", 500),
                              ("وخمسمائة", 500),
                              ("ستمائة", 600),
                              ("وستمائة", 600),
                              ("سبعمائة", 700),
                              ("وسبعمائة", 700),
                              ("ثمانمائة", 800),
                              ("وثمانمائة", 800),
                              ("تسعمائة", 900),
                              ("وتسعمائة", 900),
                              ("ألف", 1000),
                              ("آلاف", 1000),
                              ("الآف", 1000),
                              ("الاف", 1000),
                              ("ألفاً", 1000),
                              ("الفا", 1000),
                              ("الف", 1000),
                              ("ألفين", 2000),
                              ("بألفي", 2000),
                              ("ألفان", 2000),
                              ("المليون", 1000000),
                              ("مليون", 1000000),
                              ("مليونًا", 1000000),
                              ("مليار", 1000000000),
                              ("المليار", 1000000000),
                              ("تريليون", 1000000000000),
                              ("التريليون", 1000000000000),
                              ("الواحد", 1),
                              ("الصفر", 0),
                              ("الاثنان", 2),
                              ("الاثنين", 2),
                              ("الثلاثة", 3),
                              ("الأربعة", 4),
                              ("الخمسة", 5),
                              ("الستة", 6),
                              ("السبعة", 7),
                              ("الثمانية", 8),
                              ("التسعة", 9),
                              ("العشرة", 10),
                              ("الإحدى عشر", 11),
                              ("الاثنى عشر", 12),
                              ("الدستة", 12),
                              ("الدستات", 12),
                              ("الثلاثة عشر", 13),
                              ("الأربعة عشر", 14),
                              ("الخمسة عشر", 15),
                              ("الستة عشر", 16),
                              ("السبعة عشر", 17),
                              ("الثمانية عشر", 18),
                              ("التسعة عشر", 19),
                              ("العشرون", 20),
                              ("الثلاثون", 30),
                              ("الأربعون", 40),
                              ("الخمسون", 50),
                              ("الستون", 60),
                              ("السبعون", 70),
                              ("الثمانون", 80),
                              ("التسعون", 90),
                              ("المائة", 100),
                              ("المائتين", 200),
                              ("المائتان", 200),
                              ("الثلاثمائة", 300),
                              ("الأربعمائة", 400),
                              ("الخمسمائة", 500),
                              ("الستمائة", 600),
                              ("السبعمائة", 700),
                              ("الثمانمائة", 800),
                              ("التسعمائة", 900),
                              ("الألف", 1000),
                              ("الآلاف", 1000),
                              ("الألفين", 2000)])
    OrdinalNumberMap = dict([("أول", 1),
                             ("أولى", 1),
                             ("الأول", 1),
                             ("الأولى", 1),
                             ("ثاني", 2),
                             ("ثانية", 2),
                             ("الثاني", 2),
                             ("الثانية", 2),
                             ("ثان", 2),
                             ("النصف", 2),
                             ("نصف", 2),
                             ("ثلث", 3),
                             ("الثالث", 3),
                             ("الثالثة", 3),
                             ("ثالث", 3),
                             ("ثالثة", 3),
                             ("الربع", 4),
                             ("ربع", 4),
                             ("الرابع", 4),
                             ("الرابعة", 4),
                             ("رابع", 4),
                             ("رابعة", 4),
                             ("خمس", 5),
                             ("الخامس", 5),
                             ("الخامسة", 5),
                             ("خامس", 5),
                             ("خامسة", 5),
                             ("سدس", 6),
                             ("السادس", 6),
                             ("السادسة", 6),
                             ("سادس", 6),
                             ("سادسة", 6),
                             ("سبع", 7),
                             ("السابع", 7),
                             ("السابعة", 7),
                             ("سابع", 7),
                             ("سابعة", 7),
                             ("ثمن", 8),
                             ("الثامن", 8),
                             ("الثامنة", 8),
                             ("ثامن", 8),
                             ("ثامنة", 8),
                             ("تسع", 9),
                             ("التاسع", 9),
                             ("تاسع", 9),
                             ("تاسعة", 9),
                             ("التاسعة", 10),
                             ("واحد من عشرة", 10),
                             ("العاشر", 10),
                             ("واحد من إحدى عشر", 11),
                             ("الحادية عشرة", 11),
                             ("الحادي عشر", 11),
                             ("واحد من إثنى عشر", 12),
                             ("الثانية عشرة", 12),
                             ("الثاني عشر", 12),
                             ("واحد من ثلاثة عشر", 13),
                             ("الثالثة عشرة", 13),
                             ("الثالث عشر", 13),
                             ("واحد من أربعة عشر", 14),
                             ("الرابعة عشرة", 14),
                             ("الرابع عشر", 14),
                             ("واحد من خمسة عشر", 15),
                             ("الخامسة عشرة", 15),
                             ("الخامس عشر", 15),
                             ("واحد من ستة عشر", 16),
                             ("السادسة عشرة", 16),
                             ("السادس عشر", 16),
                             ("واحد من سبعة عشر", 17),
                             ("السابعة عشرة", 17),
                             ("السابع عشر", 17),
                             ("واحد من ثمانية عشر", 18),
                             ("الثامنة عشرة", 18),
                             ("الثامن عشر", 18),
                             ("واحد من تسعة عشر", 19),
                             ("التاسع عشر", 19),
                             ("واحد من عشرين", 20),
                             ("العشرون", 20),
                             ("العشرين", 20),
                             ("الحادي والعشرين", 21),
                             ("الثاني والعشرين", 22),
                             ("الثالث والعشرين", 23),
                             ("الرابع والعشرين", 24),
                             ("الخامس والعشرين", 25),
                             ("السادس والعشرين", 26),
                             ("السابع والعشرين", 27),
                             ("الثامن والعشرين", 28),
                             ("التاسع والعشرين", 29),
                             ("واحد من ثلاثين", 30),
                             ("الثلاثون", 30),
                             ("الثلاثين", 30),
                             ("الحادي والثلاثين", 31),
                             ("واحد من أربعين", 40),
                             ("الأربعون", 40),
                             ("الأربعين", 40),
                             ("واحد من خمسين", 50),
                             ("الخمسون", 50),
                             ("الخمسين", 50),
                             ("واحد من ستين", 60),
                             ("الستون", 60),
                             ("الستين", 60),
                             ("واحد من سبعين", 70),
                             ("السبعون", 70),
                             ("السبعين", 70),
                             ("واحد من ثمانين", 80),
                             ("الثمانون", 80),
                             ("الثمانين", 80),
                             ("واحد من تسعين", 90),
                             ("التسعون", 90),
                             ("التسعين", 90),
                             ("واحد من مائة", 100),
                             ("المائة", 100),
                             ("المائتان", 200),
                             ("المائتين", 200),
                             ("الثلاثمائة", 300),
                             ("الأربعمائة", 400),
                             ("الخمسمائة", 500),
                             ("الستمائة", 600),
                             ("السبعمائة", 700),
                             ("الثمانمائة", 800),
                             ("التسعمائة", 100),
                             ("الألف", 1000),
                             ("واحد من ألف", 1000),
                             ("واحد من مليون", 1000000),
                             ("المليون", 1000000),
                             ("واحد من مليار", 1000000000),
                             ("المليار", 1000000000),
                             ("واحد من تريليون", 1000000000000),
                             ("التريليون", 1000000000000),
                             ("أوائل", 1),
                             ("أنصاف", 2),
                             ("أثلاث", 3),
                             ("أرباع", 4),
                             ("أخماس", 5),
                             ("أسداس", 6),
                             ("أسباع", 7),
                             ("أثمان", 8),
                             ("أتساع", 9),
                             ("أعشار", 10),
                             ("عشرينات", 20),
                             ("ثلاثينات", 30),
                             ("أربعينات", 40),
                             ("خمسينات", 50),
                             ("ستينات", 60),
                             ("سبعينات", 70),
                             ("ثمانينات", 80),
                             ("تسعينات", 90),
                             ("مئات", 100),
                             ("ألوف", 1000),
                             ("ملايين", 1000000),
                             ("مليارات", 1000000000),
                             ("تريليون", 1000000000000)])
    RoundNumberMap = dict([("ترليون", 1000000000000),
                           ("مائة", 100),
                           ("مئة", 100),
                           ("ألف", 1000),
                           ("آلاف", 1000),
                           ("الآف", 1000),
                           ("الاف", 1000),
                           ("ألفاً", 1000),
                           ("الفا", 1000),
                           ("الف", 1000),
                           ("مليون", 1000000),
                           ("مليار", 1000000000),
                           ("تريليون", 1000000000000),
                           ("مائتين", 200),
                           ("مائتان", 200),
                           ("ثلاثمائة", 300),
                           ("أربعمائة", 400),
                           ("خمسمائة", 500),
                           ("ستمائة", 600),
                           ("سبعمائة", 700),
                           ("ثمانمائة", 800),
                           ("تسعمائة", 900),
                           ("ألفين", 2000),
                           ("دستة", 12),
                           ("دستات", 12),
                           ("المائة", 100),
                           ("الألف", 1000),
                           ("المليون", 1000000),
                           ("المليار", 1000000000),
                           ("التريليون", 1000000000000),
                           ("المائتين", 200),
                           ("المائتان", 200),
                           ("الثلاثمائة", 300),
                           ("الأربعمائة", 400),
                           ("الخمسمائة", 500),
                           ("الستمائة", 600),
                           ("السبعمائة", 700),
                           ("الثمانمائة", 800),
                           ("التسعمائة", 900),
                           ("الألفين", 2000),
                           ("الدستة", 12),
                           ("الدستات", 12)])
    AmbiguityFiltersDict = dict([("\\bواحد\\b", "\\b(الذي|هذا|ذلك|ذاك|أي)\\s+(واحد)\\b")])
    RelativeReferenceOffsetMap = dict([("الاخر", "0"),
                                       ("آخر", "0"),
                                       ("اخر", "0"),
                                       ("الأخيرة", "0"),
                                       ("الأخير", "0"),
                                       ("سبقت الأخيرة", "-1"),
                                       ("سبقت الأخير", "-1"),
                                       ("قبل الأخير", "-1"),
                                       ("قبل الأخيرة", "-1"),
                                       ("القبل الأخير", "-1"),
                                       ("قبلا الأخي", "-1"),
                                       ("التالي", "1"),
                                       ("بعد التالي", "2"),
                                       ("قادم", "1"),
                                       ("قادمة", "1"),
                                       ("القادم", "1"),
                                       ("القادمة", "1"),
                                       ("السابقة", "-1"),
                                       ("الحالي", "0"),
                                       ("الحالية", "0"),
                                       ("قبل الاخير", "-1"),
                                       ("الواحد قبل الاخير", "-1"),
                                       ("الثانية الى الاخير", "-1"),
                                       ("الذي قبلا الأخير", "-1"),
                                       ("الذي قبل الأخير", "-1"),
                                       ("الذي قبلا الأخي", "-1"),
                                       ("السابق", "-1"),
                                       ("أخر", "0"),
                                       ("الاخير", "0"),
                                       ("اول", "1"),
                                       ("الاول", "1"),
                                       ("التالية", "-1")])
    RelativeReferenceRelativeToMap = dict([("اول", "current"),
                                           ("التالية", "current"),
                                           ("الاول", "current"),
                                           ("الاخر", "end"),
                                           ("الاخير", "end"),
                                           ("أخر", "end"),
                                           ("آخر", "end"),
                                           ("اخر", "end"),
                                           ("الأخيرة", "end"),
                                           ("الأخير", "end"),
                                           ("سبقت الأخيرة", "current"),
                                           ("سبقت الأخير", "current"),
                                           ("قبل الأخير", "end"),
                                           ("قبل الأخيرة", "current"),
                                           ("القبل الأخير", "current"),
                                           ("الذي قبلا الأخي", "end"),
                                           ("التالي", "current"),
                                           ("بعد التالي", "current"),
                                           ("قادم", "current"),
                                           ("قادمة", "current"),
                                           ("القادم", "current"),
                                           ("القادمة", "current"),
                                           ("السابقة", "current"),
                                           ("الحالي", "current"),
                                           ("قبلا الأخي", "current"),
                                           ("الحالية", "end"),
                                           ("قبل الاخير", "end"),
                                           ("الواحد قبل الاخير", "end"),
                                           ("الذي قبل الأخير", "end"),
                                           ("الذي قبلا الأخير", "end"),
                                           ("الثانية الى الاخير", "end"),
                                           ("السابق", "current")])
# pylint: enable=line-too-long
