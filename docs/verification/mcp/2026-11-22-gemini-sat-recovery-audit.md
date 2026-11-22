# Gemini audit of SAT archive recovery v0.5.27

On November 22, 2026, Gemini 3.8 Flash (High) used Antigravity CLI 1.5.14 to inspect the Naturepedia benchmark. The operator supplied the task and withheld the expected numerical results. The published manifest itself contained summary fields for comparison after calculation.

## Discovery and calculation

Gemini reported listing the production MCP resources and reading `sat-recovery-v0.5.27` at its advertised URI. Antigravity saved the JSON response locally. The execution transcript shows Gemini running Python against that saved payload and finding 24 records with 24 distinct case IDs.

For each run, Gemini sorted the 24 case-level timing ratios and averaged the 12th and 13th values, giving each case equal weight.

| Run | 12th value | 13th value | Panel median | Warm recovery time reduction |
| --- | ---: | ---: | ---: | ---: |
| Original | 0.8146077815488953 | 0.8152137029444076 | 0.8149107422466515 | 18.51% |
| Internal rerun | 0.818280456102414 | 0.8212606815431103 | 0.8197705688227621 | 18.02% |

Summing the individual archive sizes yielded 23,096 baseline bytes and 23,922 reverse bytes, an increase of 826 bytes (3.58%).

## Precision correction and scope

The first Python output displayed the middle values correctly to ten decimal places. Gemini’s accompanying prose supplied incorrect trailing digits for three values labeled “exact.” A follow-up Python run printed all four values with `repr()`. The table above records those corrected values. Both panel medians and both rounded reductions were confirmed.

This audit covered MCP resource retrieval and arithmetic over published case records. The memory and latency logs were outside its scope. Independent execution of the original benchmark remains pending.

- [Manifest at the audited revision](https://github.com/RobbieRazor/robbies-razor-benchmarks/blob/4bec57b979e637b9e23a0fe1090cb26f51330aed/benchmarks/sat-recovery-v0.5.27-manifest.json)
- [Earlier Grok audit](./2026-11-22-grok-sat-recovery-audit.md)
- [Public SAT testing study](https://www.robbiegeorgephotography.com/robbies-razor-sat-testing#sat-sources)
