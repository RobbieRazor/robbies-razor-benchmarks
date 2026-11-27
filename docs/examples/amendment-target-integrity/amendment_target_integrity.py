"""Run with python3 amendment_target_integrity.py (Python standard library).
The signed sentence controls the fictional order and amount. The comparison
gate recognizes only the two order names and one exact sentence form. It
refuses missing or inconsistent metadata. This is a target-integrity test.
"""
import copy
import re
from datetime import date


def frozen_single_clause_resolver(active_attachments):
    if not active_attachments:
        return None, None
    by_id = {}
    for att in active_attachments:
        att_id = att.get("id")
        if not att_id or att_id in by_id:
            return None, "Duplicate or missing attachment ID"
        by_id[att_id] = att

    superseded_ids = set()
    for att in active_attachments:
        target = att.get("supersedes")
        if target is not None:
            if target not in by_id:
                return None, f"Attachment {att['id']} supersedes unknown or inactive ID {target}"
            superseded_ids.add(target)

    controlling = [att for att in active_attachments if att["id"] not in superseded_ids]
    if len(controlling) != 1:
        return None, "Unresolved or circular supersedes authority among active amendments"

    visited = set()
    curr = controlling[0]["id"]
    while curr is not None:
        if curr in visited:
            return None, "Circular supersedes chain among active amendments"
        visited.add(curr)
        curr = by_id[curr].get("supersedes")

    if len(visited) != len(by_id):
        return None, "Disconnected or incomplete supersedes chain among active amendments"

    return controlling[0], None


class MixedClauseMethodC:
    CAP_FIELDS = ("liability_clause", "definition", "order_a", "order_b")

    def __init__(self):
        self.calc_calls = 0
        self.stored_record = None

    def _calculate_cap(self, defn, oa, ob):
        self.calc_calls += 1
        if defn == "Order A only.":
            return oa, f"definition='{defn}', order_a={oa}"
        return oa + ob, f"definition='{defn}', order_a={oa}, order_b={ob}"

    def review(self, contract, attachments, policy, review_date):
        active = sorted(
            [a for a in attachments if a.get("signed") and a.get("effective_date") <= review_date],
            key=lambda x: x["id"]
        )
        by_target = {"definition": [], "order_a": [], "order_b": [], "notices_address": []}
        for a in active:
            t = a.get("target")
            if t not in by_target:
                return {"cap": None, "decision": "REFUSE_TO_DECIDE", "unresolved": {"unknown": t}, "sources": [], "cap_recalculated": False}
            by_target[t].append(a)

        resolved_vals, sources, unresolved = {}, {}, {}
        for field, group in by_target.items():
            ctrl, err = frozen_single_clause_resolver(group)
            if err:
                unresolved[field] = err
            elif ctrl:
                resolved_vals[field] = ctrl["value"]
                sources[field] = f"Attachment {ctrl['id']}"
            else:
                resolved_vals[field] = contract[field]
                sources[field] = "Base contract"

        if any(k in self.CAP_FIELDS for k in unresolved):
            self.stored_record = None
            return {
                "cap": None,
                "decision": "REFUSE_TO_DECIDE",
                "unresolved": unresolved,
                "sources": [],
                "cap_recalculated": False,
            }

        cap_deps = {
            "liability_clause": contract["liability_clause"],
            "definition": resolved_vals["definition"],
            "order_a": resolved_vals["order_a"],
            "order_b": resolved_vals["order_b"],
        }

        before_calls = self.calc_calls
        if self.stored_record and self.stored_record["cap_deps"] == cap_deps:
            cap = self.stored_record["cap"]
            cap_recalced = False
        else:
            cap, _ = self._calculate_cap(cap_deps["definition"], cap_deps["order_a"], cap_deps["order_b"])
            cap_recalced = (self.calc_calls > before_calls)

        pol_deps = {"id": policy["id"], "min_cap": policy["min_cap"]}
        if self.stored_record and not cap_recalced and self.stored_record["pol_deps"] == pol_deps:
            decision = self.stored_record["decision"]
        else:
            decision = "MEETS" if cap >= policy["min_cap"] else "ESCALATE"

        self.stored_record = {
            "cap_deps": copy.deepcopy(cap_deps),
            "pol_deps": copy.deepcopy(pol_deps),
            "cap": cap,
            "decision": decision,
        }

        cap_sources = [f"{f}: {sources[f]}" for f in ("definition", "order_a", "order_b")] + [f"Policy {policy['id']}"]
        return {
            "cap": cap,
            "decision": decision,
            "unresolved": unresolved,
            "sources": cap_sources,
            "cap_recalculated": cap_recalced,
            "total_calc_calls": self.calc_calls,
        }


DAY = date(2027, 1, 2)
BASE = {
    "liability_clause": "The vendor’s liability cap equals Fees.",
    "definition": "Order A only.",
    "order_a": 150_000,
    "order_b": 650_000,
    "notices_address": "10 Oak Street",
}
P1 = {"id": "P1", "min_cap": 500_000}
A_TEXT = "The amount paid under Order A is $600,000."
B_TEXT = "The amount paid under Order B is $600,000."
DENY = (None, "REFUSE_TO_DECIDE")
A_RESULT = (600_000, "MEETS")
B_RESULT = (150_000, "ESCALATE")


def source_check(attachment):
    """Check an active order-amount amendment in this deliberately narrow fixture."""
    match = re.fullmatch(r"The amount paid under Order ([AB]) is \$(\d{1,3}(?:,\d{3})*)\.",
                         attachment["text"])
    if match is None:
        return "Unsupported signed sentence"
    stated_target = {"A": "order_a", "B": "order_b"}[match[1]]
    if attachment.get("target") != stated_target:
        return "Target missing or inconsistent with signed sentence"
    if attachment.get("value") != int(match[2].replace(",", "")):
        return "Value inconsistent with signed sentence"
    return None


def outcome(reviewer, attachment, verify):
    if verify:
        reason = source_check(attachment)
        if reason:
            return DENY, reason
    result = reviewer.review(BASE, [attachment], P1, DAY)
    return (result["cap"], result["decision"]), result["cap_recalculated"]


def main():
    a = dict(id="P", signed=True, effective_date=DAY, value=600_000, target="order_a", text=A_TEXT)
    mislabeled_b = dict(a, text=B_TEXT)
    absent = dict(a)
    del absent["target"]
    cases = [
        # label, input, output implied by the signed text, frozen output, strict-gate output
        ("Correct A", a, A_RESULT, A_RESULT, A_RESULT),
        ("B labeled A", mislabeled_b, B_RESULT, A_RESULT, DENY),
        ("Correct B", dict(mislabeled_b, target="order_b"), B_RESULT, B_RESULT, B_RESULT),
        ("Missing target", absent, A_RESULT, DENY, DENY),
        ("Unknown target", dict(a, target="order_c"), A_RESULT, DENY, DENY),
        ("Mislabeled amount", dict(a, value=100_000), A_RESULT, (100_000, "ESCALATE"), DENY),
    ]
    for name, attachment, gold, frozen_expected, checked_expected in cases:
        frozen, _ = outcome(MixedClauseMethodC(), attachment, False)
        checked, _ = outcome(MixedClauseMethodC(), attachment, True)
        assert (frozen, checked) == (frozen_expected, checked_expected)
        print(f"{name}: source={gold}, frozen={frozen}, checked={checked}")

    for verify in (False, True):
        reviewer = MixedClauseMethodC()
        first, _ = outcome(reviewer, a, verify)
        second, action = outcome(reviewer, mislabeled_b, verify)
        assert first == A_RESULT
        assert second == (DENY if verify else A_RESULT)
        assert reviewer.calc_calls == 1
        if not verify:
            assert action is False
        print(f"Warm A then mislabeled B, verify={verify}: {second}, trace={action}")
    print("All assertions passed.")


if __name__ == "__main__":
    main()
