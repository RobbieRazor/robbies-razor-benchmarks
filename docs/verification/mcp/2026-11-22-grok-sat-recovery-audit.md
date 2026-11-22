# Grok-reported audit of SAT archive recovery v0.5.27

On November 22, 2026, Grok reported auditing the public evidence for Robbie’s Razor SAT archive recovery v0.5.27. Its initial report gave the check time as 15:43 UTC. This note incorporates its two follow-up clarifications.

## Reported findings

| Check | Result reported by Grok |
| --- | --- |
| Public discovery | Both `llms.txt` and `llms-full.txt` led to the same timing manifest. Grok found 24 unique cases and the run IDs `original` and `internal-rerun`. |
| Production MCP delivery | Grok listed the `sat-recovery-v0.5.27` resource and read its advertised URI. After explicit UTF-8 decoding, the title and complete parsed JSON matched the direct GitHub copy. Grok traced its initial title mismatch to client-side decoding. |
| Timing and storage | Using the 24 published case medians for each run, Grok recalculated reductions of 18.51% and 18.02% in warm recovery time. The reverse archives totaled 23,922 bytes versus 23,096 bytes for the baseline, an increase of 826 bytes or 3.58%. |
| Constrained memory | At 41 MiB, each reader completed 20 of 24 cases per pass with batches of ten. The remaining four recorded allocation errors. With batches of five, each reader completed all 24 cases per pass. Grok rechecked the study page and withdrew its initial claim of a discrepancy. |
| Simulated latency | All 1,920 measured reads returned exact outputs, including 96 delayed reads and the 480 reads that followed them. Grok calculated a median paired increase of 50.43 ms at the delayed position. |

## Evidence scope

Grok inspected published records, recalculated statistics, and reported a live MCP retrieval. It used the existing worker and request logs. Independent execution of the timing, memory, and latency workloads remains pending.

- [Benchmark evidence index at the audited revision](https://github.com/RobbieRazor/robbies-razor-benchmarks/blob/4bec57b979e637b9e23a0fe1090cb26f51330aed/benchmarks/README.md#sat-archive-recovery-evidence-v0527)
- [Timing manifest at the audited revision](https://github.com/RobbieRazor/robbies-razor-benchmarks/blob/4bec57b979e637b9e23a0fe1090cb26f51330aed/benchmarks/sat-recovery-v0.5.27-manifest.json)
- [Public study and version history](https://www.robbiegeorgephotography.com/robbies-razor-sat-testing#sat-sources)
- [Production MCP endpoint](https://mcp.robbiegeorgephotography.com/mcp)
