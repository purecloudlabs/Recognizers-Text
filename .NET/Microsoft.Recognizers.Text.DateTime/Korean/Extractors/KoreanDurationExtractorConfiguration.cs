﻿using System.Collections.Generic;
using System.Collections.Immutable;
using System.Globalization;
using System.Linq;
using System.Text.RegularExpressions;

using Microsoft.Recognizers.Definitions.Korean;
using Microsoft.Recognizers.Text.NumberWithUnit;
using Microsoft.Recognizers.Text.NumberWithUnit.Korean;

namespace Microsoft.Recognizers.Text.DateTime.Korean
{

    public class KoreanDurationExtractorConfiguration : BaseDateTimeOptionsConfiguration, ICJKDurationExtractorConfiguration
    {

        public static readonly Regex YearRegex = new Regex(DateTimeDefinitions.DurationYearRegex, RegexFlags);

        public static readonly Regex DurationUnitRegex = new Regex(DateTimeDefinitions.DurationUnitRegex, RegexFlags);

        public static readonly Regex DurationConnectorRegex = new Regex(DateTimeDefinitions.DurationConnectorRegex, RegexFlags);

        private const RegexOptions RegexFlags = RegexOptions.Singleline | RegexOptions.ExplicitCapture;

        private readonly bool merge;

        public KoreanDurationExtractorConfiguration(IDateTimeOptionsConfiguration config, bool merge = true)
            : base(config)
        {
            this.merge = merge;

            InternalExtractor = new NumberWithUnitExtractor(new DurationExtractorConfiguration());

            UnitMap = DateTimeDefinitions.ParserConfigurationUnitMap.ToDictionary(k => k.Key, k => k.Value.Substring(0, 1) + k.Value.Substring(1).ToLower());
            UnitValueMap = DateTimeDefinitions.DurationUnitValueMap;
        }

        public IExtractor InternalExtractor { get; }

        public Dictionary<string, string> UnitMap { get; }

        public Dictionary<string, long> UnitValueMap { get; }

        Regex ICJKDurationExtractorConfiguration.DurationUnitRegex => DurationUnitRegex;

        Regex ICJKDurationExtractorConfiguration.DurationConnectorRegex => DurationConnectorRegex;

        Regex ICJKDurationExtractorConfiguration.YearRegex => YearRegex;

        internal class DurationExtractorConfiguration : KoreanNumberWithUnitExtractorConfiguration
        {
            public static readonly ImmutableDictionary<string, string> DurationSuffixList = DateTimeDefinitions.DurationSuffixList.ToImmutableDictionary();

            public DurationExtractorConfiguration()
                : base(new CultureInfo(Text.Culture.Korean))
            {
            }

            public override ImmutableDictionary<string, string> SuffixList => DurationSuffixList;

            public override ImmutableDictionary<string, string> PrefixList => null;

            public override string ExtractType => Constants.SYS_DATETIME_DURATION;

            public override ImmutableList<string> AmbiguousUnitList => DateTimeDefinitions.DurationAmbiguousUnits.ToImmutableList();
        }
    }
}