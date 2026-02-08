# Precision-Limit Check (PLC) — Finite Representation Invariant

**Purpose:** Detect *Boundary Avoidance* via **non-functional numeric precision**—computing digits that cannot change any physically meaningful outcome.

**Pitch:** Stop computing digits that don’t move the needle. Adopt the **Finite Representation Invariant**.

---

## 1) Core Logic

If a system’s chosen floating-point precision (e.g., FP64) **exceeds** the task’s physical reconstruction requirement, flag it as **Boundary Avoidance**.

This diagnostic applies to any pipeline where numeric precision is a design choice (simulation, inference, control loops, optimization, rendering, robotics, scientific computing, etc.).

---

## 2) Definitions

Let:

- **R** = scale (typical magnitude) of the quantity being computed (in task units)
- **ε** = reconstruction tolerance (task-required absolute error bound, in same units)
- **required_digits** = minimum decimal digits needed such that truncation/rounding cannot exceed ε at scale R

### Required digits (task-side)
\[
\text{required\_digits} = \lceil \log_{10}(R/\varepsilon) \rceil
\]

### Available digits (representation-side, approximate)
- **BF16** ≈ 2–3 decimal digits
- **FP16** ≈ 3–4 decimal digits
- **FP32** ≈ 7–8 decimal digits
- **FP64** ≈ 15–16 decimal digits

> Note: these are practical engineering approximations for significance (not exponent range).

---

## 3) Decision Rule

Choose a conservative safety margin **m = 2 digits** (default).

- If **available_digits ≥ required_digits + m** → **FLAG: Boundary Avoidance (Over-Precision)**
- If **available_digits < required_digits** → **FLAG: Under-Precision Risk**
- Else → **PASS: Precision matches task**

### Output labels (recommended)
- `PLC_OVER_PRECISION_BOUNDARY_AVOIDANCE`
- `PLC_UNDER_PRECISION_RISK`
- `PLC_PASS`

---

## 4) Why This Matters (Razor Mapping)

Over-precision consumes compute/energy without increasing reconstruction fidelity.

In Robbie’s Razor accounting terms:
- **Compression:** select the minimal sufficient representation
- **Expression:** emit only the digits needed for the task
- **Memory:** preserve the invariant within tolerance
- **Recursion:** repeat without representational inflation

**Over-precision is representational inflation**: it increases overhead without improving meaning.

---

## 5) Examples

### Example A — “Earth-scale, inch-levelA: no reason for FP64”
- R ≈ 4.0e7 meters (Earth circumference scale)
- ε ≈ 0.0254 meters (1 inch)

R/ε ≈ 1.6e9 → required_digits ≈ 10

- FP32 (7–8 digits) may be borderline depending on conditioning
- FP64 (15–16 digits) likely exceeds requirement → **over-precision** unless justified

### Example B — “Engineering tolerance dominates”
If your sensors are noisy at ε = 1e-3 and your state is R = 1e2:
R/ε = 1e5 → required_digits = 5

FP32 is sufficient; FP64 is typically non-functional overhead.

---

## 6) Guardrails (When Higher Precision Is Justified)

PLC flags *over-precision relative to task tolerance*, but higher precision can still be justified when:

- The computation is **ill-conditioned** (cancellation, stiff systems, chaotic sensitivity)
- Intermediate steps require higher precision to prevent error blow-up
- You are estimating derivatives / gradients with tight numerical stability constraints

**Override rule:** If precision is escalated for conditioning reasons, require an explicit annotation:
> “Precision escalation justified by conditioning / stability constraints.”

---

## 7) MRD Cross-Links

- **MRD v1.8 — §11.6A** Boundary Avoidance (representational inflation / non-functional overhead)
- **MRD v1.8 — §1.13** Rotational Reset Symmetry (scaled recursion neutralizes complexity)
- **MRD v1.8 — §1.13 (Addendum)** Finite Representation Invariant (π boundary case)
