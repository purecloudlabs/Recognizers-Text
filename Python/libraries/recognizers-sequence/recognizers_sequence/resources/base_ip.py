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


class BaseIp:
    Ipv4Regex = f'\\b(1\\d{{2}}|2[0-4]\\d|25[0-5]|0?[1-9]\\d|0{{0,2}}\\d)((\\.(1\\d{{2}}|2[0-4]\\d|25[0-5]|0?[1-9]\\d|0{{0,2}}\\d)){{3}})\\b'
    BasicIpv6Element = f'([\\da-fA-F]{{1,4}})'
    BasicIpv6Regex = f'(({BasicIpv6Element}:){{7}}{BasicIpv6Element})'
    Ipv6EllipsisRegex1 = f'(:(:{BasicIpv6Element}){{1,7}})'
    Ipv6EllipsisRegex2 = f'(({BasicIpv6Element}:){{1}}((:{BasicIpv6Element}){{1,6}}))'
    Ipv6EllipsisRegex3 = f'(({BasicIpv6Element}:){{2}}((:{BasicIpv6Element}){{1,5}}))'
    Ipv6EllipsisRegex4 = f'(({BasicIpv6Element}:){{3}}((:{BasicIpv6Element}){{1,4}}))'
    Ipv6EllipsisRegex5 = f'(({BasicIpv6Element}:){{4}}((:{BasicIpv6Element}){{1,3}}))'
    Ipv6EllipsisRegex6 = f'(({BasicIpv6Element}:){{5}}((:{BasicIpv6Element}){{1,2}}))'
    Ipv6EllipsisRegex7 = f'(({BasicIpv6Element}:){{6}}((:{BasicIpv6Element}){{1}}))'
    Ipv6EllipsisRegex8 = f'(({BasicIpv6Element}:){{7}}(:))'
    Ipv6EllipsisRegexOther = f'\\B::\\B|\\B:(:{BasicIpv6Element}){{1,7}}\\b|\\b({BasicIpv6Element}:){{1,7}}:\\B'
    MergedIpv6Regex = f'({BasicIpv6Regex}|{Ipv6EllipsisRegex1}|{Ipv6EllipsisRegex2}|{Ipv6EllipsisRegex3}|{Ipv6EllipsisRegex4}|{Ipv6EllipsisRegex5}|{Ipv6EllipsisRegex6}|{Ipv6EllipsisRegex7}|{Ipv6EllipsisRegex8})'
    Ipv6Regex = f'(\\b{MergedIpv6Regex}\\b)|({Ipv6EllipsisRegexOther})'


# pylint: enable=line-too-long
