# Governance Ceiling Operationalization (OSR + Dual-Ceiling)

## Authority & Scope Notice (Required)

This document provides **operationalization guidance only** for diagnostic measurement.

It does **not** define canonical theory, terminology, or governance meaning.

Canonical specification lives exclusively in the **Master Reference Document (MRD)**:
- MRD §11.4.5 — Energetic Recursion Ceiling
- MRD §11.4.6 — Stabilization Bandwidth Constraint (Governance Layer)
- MRD §11.10A–B — Sovereign Recursion Doctrine (if present)

This document exists to translate MRD §11.4.6 into measurable proxies suitable for experiments and engineering review.

---

## 1. Definitions (Operational)

From MRD §11.4.6:

- **R** — recursive transition rate (transitions / unit time)  
- **C** — correction demand per transition (correction load / transition)  
- **S** — stabilization bandwidth (correction capacity / unit time)  

Governance ceiling:

\[
R \cdot C \le S
\]

Oversight Saturation Ratio:

\[
OSR = \frac{R \cdot C}{S}
\]

Dual-ceiling safe envelope (with energy ceiling):

\[
R \le \min\left(\frac{E}{JCT}, \frac{S}{C}\right)
\]

---

## 2. What Counts as a “Transition” for R

A “recursive transition” must be counted as a discrete event. Use one of the following operational definitions (choose one per experiment and log it):

**R1 — Accepted State Update (Recommended)**
Count one transition when the system commits a new state that is later reused (e.g., accepted plan revision, accepted constraint set, accepted summary used downstream).

**R2 — Verified Subgoal Completion**
Count one transition per subgoal completion event that passes a verifier / unit test / constraint check.

**R3 — Search-Space Reduction Event**
Count one transition when the system produces an artifact that measurably reduces subsequent search (e.g., cached tool result, deduplicated branch set, compiled policy).

**Rule:** Do not count raw “thought tokens” as transitions. Tokens are cost; transitions are structural.

---

## 3. Measuring R in Practice

Choose a time window Δt (e.g., 60 seconds; or per task).

\[
R = \frac{\#\text{transitions in }\Delta t}{\Delta t}
\]

**Logging requirements:**
- Timestamp each transition.
- Record transition type (R1/R2/R3).
- Record whether the transition was reused later (binary reuse flag is sufficient).

---

## 4. Approximating C (Correction Demand per Transition)

C is a functional:

\[
C = f(\Omega, A, D)
\]

Where:
- **Ω (opacity)**: inspectability deficit
- **A (autonomy)**: degree of independent action
- **D (coupling density)**: component interdependence / cascade potential

In practice, compute a **proxy Ĉ** from measurable signals.

### 4.1 Recommended proxy components

**Trace Burden (TB):**
- tokens in rationale + number of tool calls + number of intermediate artifacts
- (scaled) per transition

**Review Burden (RB):**
- human review time per transition (seconds) OR
- automated review time (verifier runtime) per transition

**Correction Rate (CR):**
- fraction of transitions requiring rework / rollback / patching

### 4.2 Example proxy definition (simple, stable)

Define:

\[
\hat{C} = w_1 \cdot TB + w_2 \cdot RB + w_3 \cdot CR
\]

Where weights \(w_i\) are set once per test suite (they can be 1.0 initially).

**Interpretation:**
- Higher opacity increases TB and RB.
- Higher autonomy increases RB and CR.
- Higher coupling density increases CR and RB via cascade.

---

## 5. Estimating S (Stabilization Bandwidth)

S is the correction capacity per unit time.

Two practical interpretations:

**S1 — Human Stabilization Bandwidth**
\[
S = \frac{\text{available reviewer time in }\Delta t}{\Delta t}
\]
Example: one reviewer available 30 min per hour ⇒ \(S = 0.5\) reviewer-hours/hour.

**S2 — Pipeline Stabilization Bandwidth**
If you use automated checks (unit tests, policy validators, red-team harnesses):
\[
S = \frac{\text{validator throughput in }\Delta t}{\Delta t}
\]
Example: 120 validations/hour.

**Rule:** Choose S units consistent with Ĉ.
- If Ĉ is “seconds of review per transition,” then S should be “seconds of review available per unit time.”

---

## 6. Computing OSR in Experiments

Using the proxies:

\[
\widehat{OSR} = \frac{R \cdot \hat{C}}{S}
\]

Interpretation:
- **OSR < 1**: stabilization capacity exceeds correction demand (stable regime)
- **OSR ≈ 1**: boundary condition (stability minimum regime)
- **OSR > 1**: oversight saturation; runaway recursion risk

---

## 7. How to Reduce OSR (Razor-Aligned Interventions)

You can reduce OSR by acting on **R**, **C**, or **S**.

### 7.1 Reduce C (Preferred; architectural)
- Increase inspectability: provenance, trace compression, modular outputs
- Reduce autonomy: require confirmations at boundary crossings
- Reduce coupling density: isolate subsystems, define interfaces, add circuit breakers

### 7.2 Reduce R (situational)
- Rate-limit recursion in high-risk domains
- Increase reuse thresholds (only commit transitions that will be reused)

### 7.3 Increase S (institutional)
- Add reviewers or shift review earlier (pre-flight checks)
- Automate validations to increase throughput
- Standardize checklists to increase review velocity without losing rigor

---

## 8. Minimal Reporting Template

For each experiment / system:

- Transition definition used (R1/R2/R3):
- Δt window:
- R:
- Ĉ definition and weights:
- S definition:
- OSR (or OSR range over time):
- Primary instability signature if OSR>1:
- Intervention applied (reduce C / reduce R / increase S):
- Post-intervention OSR:

---

## 9. Non-Normative Note

This operationalization does not adjudicate policy outcomes.

It provides a constraint-based diagnostic to prevent:
- runaway acceleration (OSR >> 1)
- paralysis via overcorrection (R artificially suppressed without compression gains)

The goal is stable recursion under bounded constraints, consistent with MRD §11.4.
