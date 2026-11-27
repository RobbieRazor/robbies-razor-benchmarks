# When One Letter Changes the Approval

An exploratory Robbie’s Razor case study by Robbie George, November 27, 2026.

[Read the illustrated case study on Robbie George Photography](https://www.robbiegeorgephotography.com/robbies-razor-applications#when-one-letter-changes-the-approval)

## The test

A fictional agreement sets its liability cap equal to the amount paid under Order A. The company originally paid $150,000 under that order. Its policy requires a cap of at least $500,000.

In both cases, a database entry assigns a $600,000 amendment to Order A. The signed wording governs. One letter changes between the two inputs.

| Signed wording | Correct cap | Policy result | Database record |
|---|---:|---|---|
| “The amount paid under Order A is $600,000.” | $600,000 | Meets the minimum | Agrees |
| “The amount paid under Order B is $600,000.” | $150,000 | Falls $350,000 short | Conflicts with the signed wording |

## What happened

In two Google Search trials conducted in Safari, the AI answers gave the correct cap and policy result for each case and identified whether the records agreed. These were two observed responses on November 27, 2026.

The original AI-generated Python reviewer read the structured order label and amount. It approved both cases at $600,000. The Order B case produced a false approval even when run first with an empty cache. When the Order A case ran first, the reviewer reused the earlier approval because the database fields appeared identical.

The error began before the decision entered memory. Reuse carried it forward.

## Run the Python comparison

From this directory, run `python3 amendment_target_integrity.py`. The script uses the Python standard library.

The script compares the original reviewer with a version that checks the order and amount in the signed sentence before consulting the cache. For the mislabeled Order B case, the original returns `600000 / MEETS`. The source-checked version returns `None / REFUSE_TO_DECIDE` and identifies the mismatch. A correctly labeled Order B provides a control: both reviewers return `150000 / ESCALATE`.

The script also checks a missing target, an unknown target, an incorrect amount, and reuse after a prior approval. A successful run ends with `All assertions passed.`

## What this illustrates

Robbie’s Razor asks what must survive when information is compressed into a record and reused. Here, the critical relationship is which order the signed amount belongs to. Preserving the dollar amount alone was insufficient.

The source check recognizes the specific sentence form used in this example. The experiment measures decisions on fictional inputs. General contract interpretation, model-wide accuracy, and compute savings remain open questions.
