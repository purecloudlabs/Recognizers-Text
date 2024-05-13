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

# pylint: disable=line-too-long


class EnglishChoice:
    LangMarker = 'Eng'
    TokenizerRegex = f'[^\\w\\d]'
    SkinToneRegex = f'(\\uD83C\\uDFFB|\\uD83C\\uDFFC|\\uD83C\\uDFFD|\\uD83C\\uDFFE|\\uD83C\\uDFFF)'
    TrueRegex = (
        f'\\b(true|yes|yep|yup|yeah|y|sure|ok|agree)\\b|(\\uD83D\\uDC4D|\\uD83D\\uDC4C|\\u0001f44c){SkinToneRegex}?'
    )
    FalseRegex = f'\\b(false|nope|nop|no|not\\s+ok|disagree)\\b|(\\uD83D\\uDC4E|\\u270B|\\uD83D\\uDD90|\\u0001F44E|\\u0001F590){SkinToneRegex}?'


# pylint: enable=line-too-long
