# OSR Boundary Checklist  
(Oversight Saturation Ratio Diagnostic)

## Authority & Scope Notice (Required)

This document is diagnostic only.

It does **not** define canonical theory, governance authority, or evaluation contracts.

Canonical definitions reside exclusively in:

- MRD §11.4.5 — Energetic Recursion Ceiling  
- MRD §11.4.6 — Stabilization Bandwidth Constraint  
- MRD §11.10A–B — Sovereign Recursion Doctrine  

This checklist operationalizes OSR (Oversight Saturation Ratio) as a structural stability diagnostic.

It does not license, approve, or restrict any system.

---

# 1. Core Definition

Oversight Saturation Ratio:

\[
OSR = \frac{R \cdot C}{S}
\]

Where:

- **R** — recursive transition rate  
- **C** — correction demand per transition  
- **S** — stabilization bandwidth  

Interpretation:

- **OSR < 1** → Stable regime  
- **OSR ≈ 1** → Boundary regime (stability minimum)  
- **OSR > 1** → Oversight saturation (runaway recursion risk)

---

# 2. Pre-Flight Boundary Check (Before Deployment)

Before integrating a system into a high-stakes loop:

### ✔ Define R explicitly
- What counts as a recursive transition?
- Are you counting structural updates (not tokens)?
- Is transition logging enabled?

### ✔ Estimate C realistically
- Review burden per transition (human or automated)
- Trace depth / tool-call density
- Historical correction rate
- Opacity level (Ω), autonomy (A), coupling density (D)

### ✔ Measure S honestly
- Available reviewer bandwidth per unit time
- Automated validation throughput
- Real bottlenecks (not theoretical capacity)

### ✔ Compute OSR
- Use real measured values
- Do not use optimistic capacity assumptions

---

# 3. Early Warning Signals (OSR Approaching 1)

If OSR trends toward 1, look for:

- Increasing rollback frequency
- Review backlog accumulation
- Escalating trace depth
- Growing tool-call cascades
- Human reviewers deferring or batching corrections
- “Temporary override” policies becoming permanent

These indicate stabilization bandwidth saturation.

---

# 4. Intervention Options (Razor-Aligned)

If OSR ≥ 1, act structurally.

## Reduce C (Preferred)

- Increase inspectability (provenance, structured outputs)
- Reduce autonomy thresholds
- Modularize components to reduce coupling density
- Add circuit breakers to limit cascade

## Reduce R (Situational)

- Rate-limit recursion in high-risk domains
- Increase commit thresholds
- Require verification before state persistence

## Increase S (Institutional)

- Add reviewer capacity
- Shift validation earlier in pipeline
- Automate deterministic checks
- Reduce reviewer context switching

---

# 5. Dual-Ceiling Awareness

OSR addresses the governance ceiling.

Systems must also satisfy the energetic ceiling:

\[
R \le \frac{E}{JCT}
\]

Stability requires:

\[
R \le \min\left(\frac{E}{JCT}, \frac{S}{C}\right)
\]

Ignoring either ceiling produces structural instability.

---

# 6. Red Flags (Architecture-Level)

The following patterns frequently precede runaway recursion:

- High autonomy + high opacity
- Dense inter-component coupling
- Rapid expansion of recursive depth without compression gain
- External veto layers causing recursive shear
- “Just add oversight” instead of reducing C structurally

---

# 7. Reporting Template (Recommended)

When auditing a system, record:

- Transition definition:
- Time window:
- Measured R:
- Proxy C definition:
- Measured S:
- OSR value (or range):
- Primary instability indicator:
- Structural intervention applied:
- Post-intervention OSR:

---

# 8. Non-Normative Closing Note

OSR is not a moral judgment.

It is a structural diagnostic derived from bounded recursive constraint theory.

The objective is neither acceleration nor restriction.

The objective is stable recursion under constraint.
