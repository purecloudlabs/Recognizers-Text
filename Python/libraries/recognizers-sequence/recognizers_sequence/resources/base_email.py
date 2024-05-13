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


class BaseEmail:
    EmailRegex = f'(([-a-z0-9_\\+\\.]+)@([-a-z\\d\\.]+)\\.([a-z\\.]{{2,6}}))'
    IPv4Regex = f'(?<ipv4>(\\d{{1,3}}\\.){{3}}\\d{{1,3}})'
    NormalSuffixRegex = f'(([0-9a-z][-]*[0-9a-z]*\\.)+(?<tld>[a-z][\\-a-z]{{0,22}}[a-z]))'
    EmailPrefix = f'(?(\"\")(\"\".+?(?<!\\\\)\"\")|(([0-9a-z]((\\.(?!\\.))|[-!#\\$%&\'\\*\\+/=\\?\\^\\{{\\}}\\|~\\w])*)(?<=[0-9a-z])))'
    EmailSuffix = f'(?(\\[)(\\[{IPv4Regex}\\])|{NormalSuffixRegex})'
    EmailRegex2 = f'(({EmailPrefix})@({EmailSuffix}))'
    RFC5322Regex = f'\\A(?:[a-z0-9!#$%&\'*+/=?^_`{{|}}~-]+(?:\\.[a-z0-9!#$%&\'*+/=?^_`{{|}}~-]+)*|\"\"(?:[\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21\\x23-\\x5b\\x5d-\\x7f]|\\\\[\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])*\"\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){{3}}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21-\\x5a\\x53-\\x7f]|\\\\[\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])+)\\])\\z'


# pylint: enable=line-too-long
