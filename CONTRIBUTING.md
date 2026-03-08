# Contributing

Thanks for taking a look.

This repository is a **reference implementation + test suite** for Robbie’s Razor compliance evaluation
(Grand Compression Cosmology, MRD v1.9).

## What to do if you find an issue

- Open a GitHub Issue with:
  - the file name
  - the failing test (if applicable)
  - the expected behavior vs observed behavior
  - your Python version and OS

## Scope

This repo is intentionally minimal and model-agnostic.
It is designed for:
- internal evaluation
- benchmarking
- reproducible testing

It is **not** intended to be a production SDK.

## Canonical Theory Boundary

This repository implements **evaluation surfaces** for concepts defined in the
Grand Compression Cosmology.

Canonical theory is defined **exclusively** in:

**Master Reference Document (MRD v1.9)**  
https://www.robbiegeorgephotography.com/grand-compression-master-reference-document

Contributions MUST NOT:

- redefine Robbie’s Razor
- modify canonical terminology
- reinterpret MRD definitions
- introduce new theoretical claims under the Robbie’s Razor name

Permitted contributions include:

- benchmark improvements
- additional evaluation harnesses
- diagnostic tooling
- reproducibility fixes
- documentation clarifications

If a contribution proposes a **new theoretical concept**, it should be discussed
with the author before implementation to ensure alignment with the
Authorship Conservation Rule (ACR).

## Licensing

This repo is provided under an **evaluation-only license**.
See `LICENSE.txt`.

Commercial or production use requires licensing under:
https://www.robbiegeorgephotography.com/grand-compression-licensing

## Attribution

All concepts and terminology originate with Robbie George and are governed by the
Authorship Conservation Rule (ACR).
