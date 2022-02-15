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


class SpanishNumeric:
    LangMarker = 'Spa'
    CompoundNumberLanguage = False
    MultiDecimalSeparatorCulture = True
    NonStandardSeparatorVariants = [r'es-mx', r'es-do', r'es-sv', r'es-gt', r'es-hn', r'es-ni', r'es-pa', r'es-pr']
    HundredsNumberIntegerRegex = f'(cuatrocient[ao]s|trescient[ao]s|seiscient[ao]s|setecient[ao]s|ochocient[ao]s|novecient[ao]s|doscient[ao]s|quinient[ao]s|(?<!por\\s+)(cien(to)?))'
    RoundNumberIntegerRegex = f'(mil\\s+millones|mill[oó]n(es)?|mil|bill[oó]n(es)?|trill[oó]n(es)?|cuatrill[oó]n(es)?|quintill[oó]n(es)?|sextill[oó]n(es)?|septill[oó]n(es)?)'
    ZeroToNineIntegerRegex = f'(cuatro|cinco|siete|nueve|cero|tres|seis|ocho|dos|un[ao]?)'
    TwoToNineIntegerRegex = f'(cuatro|cinco|siete|nueve|tres|seis|ocho|dos)'
    TenToNineteenIntegerRegex = f'(diecisiete|diecinueve|diecis[eé]is|dieciocho|catorce|quince|trece|diez|once|doce)'
    TwentiesIntegerRegex = f'(veinti(cuatro|cinco|siete|nueve|tr[eé]s|s[eé]is|ocho|d[oó]s|[uú]n[oa]?)|ventiun[ao]|veinte)'
    TensNumberIntegerRegex = f'(cincuenta|cuarenta|treinta|se[st]enta|ochenta|noventa)'
    NegativeNumberTermsRegex = f'(?<negTerm>(?<!(al|lo)\\s+)menos\\s+)'
    NegativeNumberSignRegex = f'^{NegativeNumberTermsRegex}.*'
    DigitsNumberRegex = f'\\d|\\d{{1,3}}(\\.\\d{{3}})'
    BelowHundredsRegex = f'(({TenToNineteenIntegerRegex}|{TwentiesIntegerRegex}|({TensNumberIntegerRegex}(\\s+y\\s+{ZeroToNineIntegerRegex})?))|{ZeroToNineIntegerRegex})'
    BelowThousandsRegex = f'({HundredsNumberIntegerRegex}(\\s+{BelowHundredsRegex})?|{BelowHundredsRegex})'
    SupportThousandsRegex = f'(({BelowThousandsRegex}|{BelowHundredsRegex})\\s+{RoundNumberIntegerRegex}(\\s+{RoundNumberIntegerRegex})?)'
    SeparaIntRegex = f'({SupportThousandsRegex}(\\s+{SupportThousandsRegex})*(\\s+{BelowThousandsRegex})?|{BelowThousandsRegex})'
    AllIntRegex = f'({SeparaIntRegex}|mil(\\s+{BelowThousandsRegex})?)'
    PlaceHolderPureNumber = f'\\b'
    PlaceHolderDefault = f'\\D|\\b'

    def NumbersWithPlaceHolder(placeholder):
        return f'(((?<!\\d+\\s*)-\\s*)|(?<=\\b))\\d+(?!([\\.,]\\d+[a-zA-Z]))(?={placeholder})'
    NumbersWithSuffix = f'(((?<=\\W|^)-\\s*)|(?<=\\b))\\d+\\s*{BaseNumbers.NumberMultiplierRegex}(?=\\b)'
    RoundNumberIntegerRegexWithLocks = f'(?<=\\b)({DigitsNumberRegex})+\\s+{RoundNumberIntegerRegex}(?=\\b)'
    NumbersWithDozenSuffix = f'(((?<=\\W|^)-\\s*)|(?<=\\b))\\d+\\s+docenas?(?=\\b)'
    AllIntRegexWithLocks = f'((?<=\\b){AllIntRegex}(?=\\b))'
    AllIntRegexWithDozenSuffixLocks = f'(?<=\\b)(((media\\s+)?\\s+docena)|({AllIntRegex}\\s+(y|con)\\s+)?({AllIntRegex}\\s+docenas?))(?=\\b)'
    SimpleRoundOrdinalRegex = f'(mil[eé]simo|millon[eé]sim[oa]|billon[eé]sim[oa]|trillon[eé]sim[oa]|cuatrillon[eé]sim[oa]|quintillon[eé]sim[oa]|sextillon[eé]sim[oa]|septillon[eé]sim[oa])'
    OneToNineOrdinalRegex = f'(primer[oa]?|segund[oa]|tercer[oa]?|cuart[oa]|quint[oa]|sext[oa]|s[eé]ptim[oa]|octav[oa]|noven[oa])'
    TensOrdinalRegex = f'(nonag[eé]sim[oa]|octog[eé]sim[oa]|septuag[eé]sim[oa]|sexag[eé]sim[oa]|quincuag[eé]sim[oa]|cuadrag[eé]sim[oa]|trig[eé]sim[oa]|vig[eé]sim[oa]|d[eé]cim[oa])'
    HundredOrdinalRegex = f'(cent[eé]sim[oa]|ducent[eé]sim[oa]|tricent[eé]sim[oa]|cuadringent[eé]sim[oa]|quingent[eé]sim[oa]|sexcent[eé]sim[oa]|septingent[eé]sim[oa]|octingent[eé]sim[oa]|noningent[eé]sim[oa])'
    SpecialUnderHundredOrdinalRegex = f'(und[eé]cim[oa]|duod[eé]cim[oa]|decimoctav[oa])'
    UnderHundredOrdinalRegex = f'({SpecialUnderHundredOrdinalRegex}|(({TensOrdinalRegex}(\\s)?)?{OneToNineOrdinalRegex})|{TensOrdinalRegex})'
    UnderThousandOrdinalRegex = f'((({HundredOrdinalRegex}(\\s)?)?{UnderHundredOrdinalRegex})|{HundredOrdinalRegex})'
    OverThousandOrdinalRegex = f'(({AllIntRegex})([eé]sim[oa]))'
    RelativeOrdinalRegex = f'(?<relativeOrdinal>(antes\\s+de|anterior\\s+a)(l|\\s+la)\\s+[uú]ltim[ao]|((ante)?pen)?[uú]ltim[ao]s?|pr[oó]xim[ao]s?|anterior(es)?|actual(es)?|siguientes?)'
    ComplexOrdinalRegex = f'(({OverThousandOrdinalRegex}(\\s)?)?{UnderThousandOrdinalRegex}|{OverThousandOrdinalRegex})'
    SufixRoundOrdinalRegex = f'(({AllIntRegex})({SimpleRoundOrdinalRegex}))'
    ComplexRoundOrdinalRegex = f'((({SufixRoundOrdinalRegex}(\\s)?)?{ComplexOrdinalRegex})|{SufixRoundOrdinalRegex})'
    AllOrdinalNumberRegex = f'{ComplexOrdinalRegex}|{SimpleRoundOrdinalRegex}|{ComplexRoundOrdinalRegex}'
    AllOrdinalRegex = f'(?:{AllOrdinalNumberRegex}|{RelativeOrdinalRegex})'
    OrdinalSuffixRegex = f'(?<=\\b)(\\d*((1(er|r[oa])|2d[oa]|3r[oa]|4t[oa]|5t[oa]|6t[oa]|7m[oa]|8v[oa]|9n[oa]|0m[oa]|11[vm][oa]|12[vm][oa])|\\d\\.?[ºª]))(?=\\b)'
    OrdinalNounRegex = f'(?<=\\b){AllOrdinalRegex}(?=\\b)'
    SpecialFractionInteger = f'((({AllIntRegex})i?({ZeroToNineIntegerRegex})|({AllIntRegex}))a?v[oa]s?)'
    FractionNotationRegex = f'{BaseNumbers.FractionNotationRegex}'
    FractionNotationWithSpacesRegex = f'(((?<=\\W|^)-\\s*)|(?<=\\b))\\d+\\s+\\d+[/]\\d+(?=(\\b[^/]|$))'
    FractionMultiplierRegex = f'(?<fracMultiplier>\\s+(y|con)\\s+(medio|(un|{TwoToNineIntegerRegex})\\s+(medio|terci[oa]?|cuart[oa]|quint[oa]|sext[oa]|s[eé]ptim[oa]|octav[oa]|noven[oa]|d[eé]cim[oa])s?))'
    RoundMultiplierWithFraction = f'(?<multiplier>(?:(mil\\s+millones|mill[oó]n(es)?|bill[oó]n(es)?|trill[oó]n(es)?|cuatrill[oó]n(es)?|quintill[oó]n(es)?|sextill[oó]n(es)?|septill[oó]n(es)?)))(?={FractionMultiplierRegex}?$)'
    RoundMultiplierRegex = f'\\b\\s*({RoundMultiplierWithFraction}|(?<multiplier>(mil))$)'
    FractionNounRegex = f'(?<=\\b)({AllIntRegex}\\s+((y|con)\\s+)?)?(({AllIntRegex})(\\s+((y|con)\\s)?)((({AllOrdinalNumberRegex})s?|({SpecialFractionInteger})|({SufixRoundOrdinalRegex})s?)|medi[oa]s?|tercios?)|(medio|un\\s+cuarto\\s+de)\\s+{RoundNumberIntegerRegex})(?=\\b)'
    FractionNounWithArticleRegex = f'(?<=\\b)(({AllIntRegex}|{RoundNumberIntegerRegexWithLocks})\\s+(y\\s+)?)?((un|un[oa])(\\s+)(({AllOrdinalNumberRegex})|({SufixRoundOrdinalRegex}))|(un[ao]?\\s+)?medi[oa]s?)(?=\\b)'
    FractionPrepositionRegex = f'(?<!{BaseNumbers.CommonCurrencySymbol}\\s*)(?<=\\b)(?<numerator>({AllIntRegex})|((?<!\\.)\\d+))\\s+sobre\\s+(?<denominator>({AllIntRegex})|((\\d+)(?!\\.)))(?=\\b)'
    AllPointRegex = f'((\\s+{ZeroToNineIntegerRegex})+|(\\s+{AllIntRegex}))'
    AllFloatRegex = f'{AllIntRegex}(\\s+(coma|con)){AllPointRegex}'

    def DoubleDecimalPointRegex(placeholder):
        return f'(((?<!\\d+\\s*)-\\s*)|((?<=\\b)(?<!\\d+[\\.,])))\\d+[\\.,]\\d+(?!([\\.,]\\d+))(?={placeholder})'

    def DoubleWithoutIntegralRegex(placeholder):
        return f'(?<=\\s|^)(?<!(\\d+))[\\.,]\\d+(?!([\\.,]\\d+))(?={placeholder})'
    DoubleWithMultiplierRegex = f'(((?<!\\d+\\s*)-\\s*)|((?<=\\b)(?<!\\d+\\[\\.,])))\\d+[\\.,]\\d+\\s*{BaseNumbers.NumberMultiplierRegex}(?=\\b)'
    DoubleWithRoundNumber = f'(((?<!\\d+\\s*)-\\s*)|((?<=\\b)(?<!\\d+\\[\\.,])))\\d+[\\.,]\\d+\\s+{RoundNumberIntegerRegex}(?=\\b)'
    DoubleAllFloatRegex = f'((?<=\\b){AllFloatRegex}(?=\\b))'
    DoubleExponentialNotationRegex = f'(((?<!\\d+\\s*)-\\s*)|((?<=\\b)(?<!\\d+[\\.,])))(\\d+([\\.,]\\d+)?)e([+-]*[1-9]\\d*)(?=\\b)'
    DoubleCaretExponentialNotationRegex = f'(((?<!\\d+\\s*)-\\s*)|((?<=\\b)(?<!\\d+[\\.,])))(\\d+([\\.,]\\d+)?)\\^([+-]*[1-9]\\d*)(?=\\b)'
    NumberWithPrefixPercentage = f'(?<!%)({BaseNumbers.NumberReplaceToken})(\\s*)(%(?!{BaseNumbers.NumberReplaceToken})|por\\s+cien(to)?\\b)'
    TillRegex = f'(\\ba\\b|hasta|--|-|—|——|~|–)'
    MoreRegex = f'(más\\s+(alt[oa]s?|grandes)\\s+que|(m[áa]s|mayor(es)?|superior(es)?|por\\s+encima)\\b((\\s+(que|del?|al?))|(?=\\s+o\\b))|(?<!<|=)>)'
    LessRegex = f'((meno(s|r(es)?)|inferior(es)?|por\\s+debajo)((\\s+(que|del?|al?)|(?=\\s+o\\b)))|más\\s+baj[oa]\\s+que|(?<!>|=)<)'
    EqualRegex = f'((igual(es)?|equivalente(s)?|equivalen?)(\\s+(al?|que|del?))?|(?<!<|>)=)'
    MoreOrEqualPrefix = f'((no\\s+{LessRegex})|(por\\s+lo\\s+menos|como\\s+m[íi]nimo|al\\s+menos))'
    MoreOrEqual = f'(({MoreRegex}\\s+(o)?\\s+{EqualRegex})|({EqualRegex}\\s+(o|y)\\s+{MoreRegex})|{MoreOrEqualPrefix}(\\s+(o)\\s+{EqualRegex})?|({EqualRegex}\\s+(o)\\s+)?{MoreOrEqualPrefix}|>\\s*=)'
    MoreOrEqualSuffix = f'((\\b(y|o)\\b\\s+(m[áa]s|mayor(es)?|superior(es)?)((?!\\s+(alt[oa]|baj[oa]|que|del?|al?))|(\\s+(que|del?|al?)(?!(\\s*\\d+)))))|como\\s+m[íi]nimo|por\\s+lo\\s+menos|al\\s+menos)\\b'
    LessOrEqualPrefix = f'((no\\s+{MoreRegex})|(como\\s+(m[aá]ximo|mucho)))'
    LessOrEqual = f'(({LessRegex}\\s+(o)?\\s+{EqualRegex})|({EqualRegex}\\s+(o)?\\s+{LessRegex})|{LessOrEqualPrefix}(\\s+(o)?\\s+{EqualRegex})?|({EqualRegex}\\s+(o)?\\s+)?{LessOrEqualPrefix}|<\\s*=)'
    LessOrEqualSuffix = f'((\\b(y|o)\\b\\s+(meno(s|r(es)?|inferior(es)?))((?!\\s+(alt[oa]|baj[oa]|que|del?|al?))|(\\s+(que|del?|al?)(?!(\\s*\\d+)))))|como\\s+m[áa]ximo)\\b'
    NumberSplitMark = f'(?![,.](?!\\d+))(?!\\s*\\b(((y|e)\\s+)?({LessRegex}|{MoreRegex}|{EqualRegex}|no|de)|pero|o|a)\\b)'
    MoreRegexNoNumberSucceed = f'(\\b(m[áa]s|mayor(es)?|superior(es)?)((?!\\s+(que|del?|al?))|\\s+((que|del?)(?!(\\s*\\d+))))|(por encima)(?!(\\s*\\d+)))\\b'
    LessRegexNoNumberSucceed = f'(\\b(meno(s|r(es)?)|inferior(es)?)((?!\\s+(que|del?|al?))|\\s+((que|del?|al?)(?!(\\s*\\d+))))|(por debajo)(?!(\\s*\\d+)))\\b'
    EqualRegexNoNumberSucceed = f'(\\b(igual(es)?|equivalentes?|equivalen?)((?!\\s+(al?|que|del?))|(\\s+(al?|que|del?)(?!(\\s*\\d+)))))\\b'
    OneNumberRangeMoreRegex1 = f'({MoreOrEqual}|{MoreRegex})\\s*((el|las?|los)\\s+)?(?<number1>({NumberSplitMark}.)+)'
    OneNumberRangeMoreRegex1LB = f'(?<!no\\s+){OneNumberRangeMoreRegex1}'
    OneNumberRangeMoreRegex2 = f'(?<number1>({NumberSplitMark}.)+)\\s*{MoreOrEqualSuffix}'
    OneNumberRangeMoreSeparateRegex = f'({EqualRegex}\\s+(?<number1>({NumberSplitMark}.)+)(\\s+o\\s+){MoreRegexNoNumberSucceed})|({MoreRegex}\\s+(?<number1>({NumberSplitMark}.)+)(\\s+o\\s+){EqualRegexNoNumberSucceed})'
    OneNumberRangeLessRegex1 = f'({LessOrEqual}|{LessRegex})\\s*((el|las?|los)\\s+)?(?<number2>({NumberSplitMark}.)+)'
    OneNumberRangeLessRegex1LB = f'(?<!no\\s+){OneNumberRangeLessRegex1}'
    OneNumberRangeLessRegex2 = f'(?<number2>({NumberSplitMark}.)+)\\s*{LessOrEqualSuffix}'
    OneNumberRangeLessSeparateRegex = f'({EqualRegex}\\s+(?<number1>({NumberSplitMark}.)+)(\\s+o\\s+){LessRegexNoNumberSucceed})|({LessRegex}\\s+(?<number1>({NumberSplitMark}.)+)(\\s+o\\s+){EqualRegexNoNumberSucceed})'
    OneNumberRangeEqualRegex = f'{EqualRegex}\\s*((el|las?|los)\\s+)?(?<number1>({NumberSplitMark}.)+)'
    TwoNumberRangeRegex1 = f'\\bentre\\s*((el|las?|los)\\s+)?(?<number1>({NumberSplitMark}.)+)\\s*y\\s*((el|las?|los)\\s+)?(?<number2>({NumberSplitMark}.)+)'
    TwoNumberRangeRegex2 = f'({OneNumberRangeMoreRegex1}|{OneNumberRangeMoreRegex2})\\s*(\\by\\b|\\be\\b|pero|,)\\s*({OneNumberRangeLessRegex1}|{OneNumberRangeLessRegex2})'
    TwoNumberRangeRegex3 = f'({OneNumberRangeLessRegex1}|{OneNumberRangeLessRegex2})\\s*(\\by\\b|\\be\\b|pero|,)\\s*({OneNumberRangeMoreRegex1}|{OneNumberRangeMoreRegex2})'
    TwoNumberRangeRegex4 = f'(\\bde(sde)?\\s+)?(\\b(el|las?|los)\\s+)?\\b(?!\\s+)(?<number1>({NumberSplitMark}(?!\\b(entre|de(sde)?|es)\\b).)+)\\b\\s*{TillRegex}\\s*((el|las?|los)\\s+)?\\b(?!\\s+)(?<number2>({NumberSplitMark}.)+)\\b'
    AmbiguousFractionConnectorsRegex = f'(\\b(en|de)\\b)'
    DecimalSeparatorChar = ','
    FractionMarkerToken = 'sobre'
    NonDecimalSeparatorChar = '.'
    HalfADozenText = 'seis'
    WordSeparatorToken = 'y'
    WrittenDecimalSeparatorTexts = [r'coma', r'con']
    WrittenGroupSeparatorTexts = [r'punto']
    WrittenIntegerSeparatorTexts = [r'y']
    WrittenFractionSeparatorTexts = [r'con']
    OneHalfTokens = [r'un', r'medio']
    HalfADozenRegex = f'media\\s+docena'
    DigitalNumberRegex = f'((?<=\\b)(mil(l[oó]n(es)?)?|bill[oó]n(es)?|trill[oó]n(es)?|docenas?)(?=\\b))|((?<=(\\d|\\b)){BaseNumbers.MultiplierLookupRegex}(?=\\b))'
    CardinalNumberMap = dict([("cero", 0),
                              ("un", 1),
                              ("una", 1),
                              ("uno", 1),
                              ("dos", 2),
                              ("tres", 3),
                              ("cuatro", 4),
                              ("cinco", 5),
                              ("seis", 6),
                              ("siete", 7),
                              ("ocho", 8),
                              ("nueve", 9),
                              ("diez", 10),
                              ("once", 11),
                              ("doce", 12),
                              ("docena", 12),
                              ("docenas", 12),
                              ("trece", 13),
                              ("catorce", 14),
                              ("quince", 15),
                              ("dieciseis", 16),
                              ("dieciséis", 16),
                              ("diecisiete", 17),
                              ("dieciocho", 18),
                              ("diecinueve", 19),
                              ("veinte", 20),
                              ("ventiuna", 21),
                              ("ventiuno", 21),
                              ("veintiun", 21),
                              ("veintiún", 21),
                              ("veintiuno", 21),
                              ("veintiuna", 21),
                              ("veintidos", 22),
                              ("veintidós", 22),
                              ("veintitres", 23),
                              ("veintitrés", 23),
                              ("veinticuatro", 24),
                              ("veinticinco", 25),
                              ("veintiseis", 26),
                              ("veintiséis", 26),
                              ("veintisiete", 27),
                              ("veintiocho", 28),
                              ("veintinueve", 29),
                              ("treinta", 30),
                              ("cuarenta", 40),
                              ("cincuenta", 50),
                              ("sesenta", 60),
                              ("setenta", 70),
                              ("ochenta", 80),
                              ("noventa", 90),
                              ("cien", 100),
                              ("ciento", 100),
                              ("doscientas", 200),
                              ("doscientos", 200),
                              ("trescientas", 300),
                              ("trescientos", 300),
                              ("cuatrocientas", 400),
                              ("cuatrocientos", 400),
                              ("quinientas", 500),
                              ("quinientos", 500),
                              ("seiscientas", 600),
                              ("seiscientos", 600),
                              ("setecientas", 700),
                              ("setecientos", 700),
                              ("ochocientas", 800),
                              ("ochocientos", 800),
                              ("novecientas", 900),
                              ("novecientos", 900),
                              ("mil", 1000),
                              ("millon", 1000000),
                              ("millón", 1000000),
                              ("millones", 1000000),
                              ("billon", 1000000000000),
                              ("billón", 1000000000000),
                              ("billones", 1000000000000),
                              ("trillon", 1000000000000000000),
                              ("trillón", 1000000000000000000),
                              ("trillones", 1000000000000000000)])
    OrdinalNumberMap = dict([("primero", 1),
                             ("primera", 1),
                             ("primer", 1),
                             ("segundo", 2),
                             ("segunda", 2),
                             ("medio", 2),
                             ("media", 2),
                             ("tercero", 3),
                             ("tercera", 3),
                             ("tercer", 3),
                             ("tercio", 3),
                             ("cuarto", 4),
                             ("cuarta", 4),
                             ("quinto", 5),
                             ("quinta", 5),
                             ("sexto", 6),
                             ("sexta", 6),
                             ("septimo", 7),
                             ("septima", 7),
                             ("séptimo", 7),
                             ("séptima", 7),
                             ("octavo", 8),
                             ("octava", 8),
                             ("noveno", 9),
                             ("novena", 9),
                             ("decimo", 10),
                             ("décimo", 10),
                             ("decima", 10),
                             ("décima", 10),
                             ("undecimo", 11),
                             ("undecima", 11),
                             ("undécimo", 11),
                             ("undécima", 11),
                             ("duodecimo", 12),
                             ("duodecima", 12),
                             ("duodécimo", 12),
                             ("duodécima", 12),
                             ("decimotercero", 13),
                             ("decimotercera", 13),
                             ("decimocuarto", 14),
                             ("decimocuarta", 14),
                             ("decimoquinto", 15),
                             ("decimoquinta", 15),
                             ("decimosexto", 16),
                             ("decimosexta", 16),
                             ("decimoseptimo", 17),
                             ("decimoseptima", 17),
                             ("decimoctavo", 18),
                             ("decimoctava", 18),
                             ("decimonoveno", 19),
                             ("decimonovena", 19),
                             ("vigesimo", 20),
                             ("vigesima", 20),
                             ("vigésimo", 20),
                             ("vigésima", 20),
                             ("trigesimo", 30),
                             ("trigesima", 30),
                             ("trigésimo", 30),
                             ("trigésima", 30),
                             ("cuadragesimo", 40),
                             ("cuadragesima", 40),
                             ("cuadragésimo", 40),
                             ("cuadragésima", 40),
                             ("quincuagesimo", 50),
                             ("quincuagesima", 50),
                             ("quincuagésimo", 50),
                             ("quincuagésima", 50),
                             ("sexagesimo", 60),
                             ("sexagesima", 60),
                             ("sexagésimo", 60),
                             ("sexagésima", 60),
                             ("septuagesimo", 70),
                             ("septuagesima", 70),
                             ("septuagésimo", 70),
                             ("septuagésima", 70),
                             ("octogesimo", 80),
                             ("octogesima", 80),
                             ("octogésimo", 80),
                             ("octogésima", 80),
                             ("nonagesimo", 90),
                             ("nonagesima", 90),
                             ("nonagésimo", 90),
                             ("nonagésima", 90),
                             ("centesimo", 100),
                             ("centesima", 100),
                             ("centésimo", 100),
                             ("centésima", 100),
                             ("ducentesimo", 200),
                             ("ducentesima", 200),
                             ("ducentésimo", 200),
                             ("ducentésima", 200),
                             ("tricentesimo", 300),
                             ("tricentesima", 300),
                             ("tricentésimo", 300),
                             ("tricentésima", 300),
                             ("cuadringentesimo", 400),
                             ("cuadringentesima", 400),
                             ("cuadringentésimo", 400),
                             ("cuadringentésima", 400),
                             ("quingentesimo", 500),
                             ("quingentesima", 500),
                             ("quingentésimo", 500),
                             ("quingentésima", 500),
                             ("sexcentesimo", 600),
                             ("sexcentesima", 600),
                             ("sexcentésimo", 600),
                             ("sexcentésima", 600),
                             ("septingentesimo", 700),
                             ("septingentesima", 700),
                             ("septingentésimo", 700),
                             ("septingentésima", 700),
                             ("octingentesimo", 800),
                             ("octingentesima", 800),
                             ("octingentésimo", 800),
                             ("octingentésima", 800),
                             ("noningentesimo", 900),
                             ("noningentesima", 900),
                             ("noningentésimo", 900),
                             ("noningentésima", 900),
                             ("milesimo", 1000),
                             ("milesima", 1000),
                             ("milésimo", 1000),
                             ("milésima", 1000),
                             ("millonesimo", 1000000),
                             ("millonesima", 1000000),
                             ("millonésimo", 1000000),
                             ("millonésima", 1000000),
                             ("billonesimo", 1000000000000),
                             ("billonesima", 1000000000000),
                             ("billonésimo", 1000000000000),
                             ("billonésima", 1000000000000)])
    PrefixCardinalMap = dict([("dos", 2),
                              ("tres", 3),
                              ("cuatro", 4),
                              ("cinco", 5),
                              ("seis", 6),
                              ("siete", 7),
                              ("ocho", 8),
                              ("nueve", 9),
                              ("diez", 10),
                              ("once", 11),
                              ("doce", 12),
                              ("trece", 13),
                              ("catorce", 14),
                              ("quince", 15),
                              ("dieciseis", 16),
                              ("dieciséis", 16),
                              ("diecisiete", 17),
                              ("dieciocho", 18),
                              ("diecinueve", 19),
                              ("veinte", 20),
                              ("ventiuna", 21),
                              ("veintiun", 21),
                              ("veintiún", 21),
                              ("veintidos", 22),
                              ("veintitres", 23),
                              ("veinticuatro", 24),
                              ("veinticinco", 25),
                              ("veintiseis", 26),
                              ("veintisiete", 27),
                              ("veintiocho", 28),
                              ("veintinueve", 29),
                              ("treinta", 30),
                              ("cuarenta", 40),
                              ("cincuenta", 50),
                              ("sesenta", 60),
                              ("setenta", 70),
                              ("ochenta", 80),
                              ("noventa", 90),
                              ("cien", 100),
                              ("doscientos", 200),
                              ("trescientos", 300),
                              ("cuatrocientos", 400),
                              ("quinientos", 500),
                              ("seiscientos", 600),
                              ("setecientos", 700),
                              ("ochocientos", 800),
                              ("novecientos", 900)])
    SuffixOrdinalMap = dict([("milesimo", 1000),
                             ("millonesimo", 1000000),
                             ("billonesimo", 1000000000000)])
    RoundNumberMap = dict([("mil", 1000),
                           ("milesimo", 1000),
                           ("millon", 1000000),
                           ("millón", 1000000),
                           ("millones", 1000000),
                           ("millonesimo", 1000000),
                           ("billon", 1000000000000),
                           ("billón", 1000000000000),
                           ("billones", 1000000000000),
                           ("billonesimo", 1000000000000),
                           ("trillon", 1000000000000000000),
                           ("trillón", 1000000000000000000),
                           ("trillones", 1000000000000000000),
                           ("trillonesimo", 1000000000000000000),
                           ("docena", 12),
                           ("docenas", 12),
                           ("k", 1000),
                           ("m", 1000000),
                           ("g", 1000000000),
                           ("b", 1000000000),
                           ("t", 1000000000000)])
    AmbiguityFiltersDict = dict([("^[.]", "")])
    RelativeReferenceOffsetMap = dict([("proxima", "1"),
                                       ("proximo", "1"),
                                       ("proximas", "1"),
                                       ("proximos", "1"),
                                       ("próxima", "1"),
                                       ("próximo", "1"),
                                       ("próximas", "1"),
                                       ("próximos", "1"),
                                       ("anterior", "-1"),
                                       ("anteriores", "-1"),
                                       ("actual", "0"),
                                       ("actuales", "0"),
                                       ("siguiente", "1"),
                                       ("siguientes", "1"),
                                       ("ultima", "0"),
                                       ("ultimo", "0"),
                                       ("última", "0"),
                                       ("último", "0"),
                                       ("ultimas", "0"),
                                       ("ultimos", "0"),
                                       ("últimas", "0"),
                                       ("últimos", "0"),
                                       ("penultima", "-1"),
                                       ("penultimo", "-1"),
                                       ("penúltima", "-1"),
                                       ("penúltimo", "-1"),
                                       ("penultimas", "-1"),
                                       ("penultimos", "-1"),
                                       ("penúltimas", "-1"),
                                       ("penúltimos", "-1"),
                                       ("antepenultima", "-2"),
                                       ("antepenultimo", "-2"),
                                       ("antepenúltima", "-2"),
                                       ("antepenúltimo", "-2"),
                                       ("antepenultimas", "-2"),
                                       ("antepenultimos", "-2"),
                                       ("antepenúltimas", "-2"),
                                       ("antepenúltimos", "-2"),
                                       ("antes de la ultima", "-1"),
                                       ("antes del ultimo", "-1"),
                                       ("antes de la última", "-1"),
                                       ("antes del último", "-1"),
                                       ("anterior al ultimo", "-1"),
                                       ("anterior a la ultima", "-1"),
                                       ("anterior al último", "-1"),
                                       ("anterior a la última", "-1")])
    RelativeReferenceRelativeToMap = dict([("proxima", "current"),
                                           ("proximo", "current"),
                                           ("proximas", "current"),
                                           ("proximos", "current"),
                                           ("próxima", "current"),
                                           ("próximo", "current"),
                                           ("próximas", "current"),
                                           ("próximos", "current"),
                                           ("anterior", "current"),
                                           ("anteriores", "current"),
                                           ("actual", "current"),
                                           ("actuales", "current"),
                                           ("siguiente", "current"),
                                           ("siguientes", "current"),
                                           ("ultima", "end"),
                                           ("ultimo", "end"),
                                           ("última", "end"),
                                           ("último", "end"),
                                           ("ultimas", "end"),
                                           ("ultimos", "end"),
                                           ("últimas", "end"),
                                           ("últimos", "end"),
                                           ("penultima", "end"),
                                           ("penultimo", "end"),
                                           ("penúltima", "end"),
                                           ("penúltimo", "end"),
                                           ("penultimas", "end"),
                                           ("penultimos", "end"),
                                           ("penúltimas", "end"),
                                           ("penúltimos", "end"),
                                           ("antepenultima", "end"),
                                           ("antepenultimo", "end"),
                                           ("antepenúltima", "end"),
                                           ("antepenúltimo", "end"),
                                           ("antepenultimas", "end"),
                                           ("antepenultimos", "end"),
                                           ("antepenúltimas", "end"),
                                           ("antepenúltimos", "end"),
                                           ("antes de la ultima", "end"),
                                           ("antes del ultimo", "end"),
                                           ("antes de la última", "end"),
                                           ("antes del último", "end"),
                                           ("anterior al ultimo", "end"),
                                           ("anterior a la ultima", "end"),
                                           ("anterior al último", "end"),
                                           ("anterior a la última", "end")])
# pylint: enable=line-too-long
