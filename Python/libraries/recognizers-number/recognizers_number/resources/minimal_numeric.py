# pylint: disable=line-too-long


class MinimalNumeric:
    LangMarker = 'min'
    NumberReplaceToken = '@builtin.num'
    FractionNumberReplaceToken = '@builtin.num.fraction'

    def IntegerRegexDefinition(placeholder, thousandsmark):
        return f'(((?<!\\d+\\s*)-\\s*)|((?<=\\b)(?<!\\d+[\\.,])))\\d{{1,3}}({thousandsmark}\\d{{3}})+(?={placeholder})'
    FractionNotationRegex = f'((((?<=\\W|^)-\\s*)|(?<![/-])(?<=\\b))\\d+[/]\\d+(?=(\\b[^/]|$))|[\\u00BC-\\u00BE\\u2150-\\u215E])'

    def DoubleRegexDefinition(placeholder, thousandsmark, decimalmark):
        return f'(((?<!\\d+\\s*)-\\s*)|((?<=\\b)(?<!\\d+[\\.,])))\\d{{1,3}}(({thousandsmark}\\d{{3}})+{decimalmark}|({decimalmark}\\d{{3}})+{thousandsmark})\\d+(?={placeholder})'
    PlaceHolderDefault = '(?=\\D)|\\b'
    PlaceHolderMixed = '\\D|\\b'
    CaseSensitiveTerms = f'(?<=(\\s|\\d))(kB|K[Bb]?|M[BbM]?|G[Bb]?|B)\\b'
    NumberMultiplierRegex = f'(K|k|MM?|mil|G|T|B|b)'
    MultiplierLookupRegex = f'(k|m(il|m)?|t|g|b)'
    CurrencyRegex = f'(((?<=\\W|^)-\\s*)|(?<=\\b))\\d+\\s*(b|m|t|g)(?=\\b)'
    CommonCurrencySymbol = f'(¥|\\$|€|£|₩)'

    PlaceHolderPureNumber = f'\\b'
    def NumbersWithPlaceHolder(placeholder):
        return f'(((?<!(\\d+(\\s*(K|k|MM?|mil|G|T|B|b))?\\s*|\\p{{L}}))-\\s*)|(?<={placeholder}))\\d+(?!([\\.,]\\d+[a-zA-Z]))(?={placeholder})'
    IndianNumberingSystemRegex = f'(?<=\\b)((?:\\d{{1,2}},(?:\\d{{2}},)*\\d{{3}})(?=\\b))'
    NumbersWithSuffix = f'(((?<!\\d+(\\s*{NumberMultiplierRegex})?\\s*)-\\s*)|(?<=\\b))\\d+\\s*{NumberMultiplierRegex}(?=\\b)'
    FractionNotationWithSpacesRegex = f'(((?<=\\W|^)-\\s*)|(?<=\\b))\\d+\\s+\\d+[/]\\d+(?=(\\b[^/]|$))'
    DoubleWithMultiplierRegex = f'(((?<!\\d+(\\s*{NumberMultiplierRegex})?\\s*)-\\s*)|((?<=\\b)(?<!\\d+[\\.,])))(\\d{{1,3}}(,\\d{{3}})+(\\.\\d+)?|\\d+[\\.,]\\d+)\\s*{NumberMultiplierRegex}(?=\\b)'
    DoubleExponentialNotationRegex = f'(((?<!\\d+(\\s*{NumberMultiplierRegex})?\\s*)-\\s*)|((?<=\\b)(?<!\\d+[\\.,])))(\\d+([\\.,]\\d+)?)(e|x10\\^)([+-]*[1-9]\\d*)(?=\\b)'
    DoubleCaretExponentialNotationRegex = f'(((?<!\\d+(\\s*{NumberMultiplierRegex})?\\s*)-\\s*)|((?<=\\b)(?<!\\d+[\\.,])))(\\d+([\\.,]\\d+)?)\\^([+-]*[1-9]\\d*)(?=\\b)'
    def DoubleDecimalPointRegex(placeholder):
        return f'(((?<!(\\d+(\\s*(K|k|MM?|mil|G|T|B|b))?\\s*|\\p{{L}}))-\\s*)|((?<={placeholder})(?<!\\d+[\\.,])))(\\d{{1,3}}(,\\d{{3}})+(\\.\\d+)?|\\d+[\\.,]\\d+)(?!([\\.,]\\d+))(?={placeholder})'
    DoubleIndianDecimalPointRegex = f'(?<=\\b)((?:\\d{{1,2}},(?:\\d{{2}},)*\\d{{3}})(?:\\.\\d{{2}})(?=\\b))'

    def DoubleWithoutIntegralRegex(placeholder):
        return f'(?<=\\s|^)(?<!(\\d+))[\\.,]\\d+(?!([\\.,]\\d+))(?={placeholder})'

    DecimalSeparatorChar = '.'
    NonDecimalSeparatorChar = ','
    NegativeNumberSignRegex = f'^(^[.]\\s+).*'
# pylint: enable=line-too-long
