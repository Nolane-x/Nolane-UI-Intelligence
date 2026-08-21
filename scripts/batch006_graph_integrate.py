from __future__ import annotations

import json
import re
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GRAPH = ROOT / "skills" / "skill-graph.json"
TEST = ROOT / "tests" / "test_ui_industry_batch_006.py"
PROVENANCE = ROOT / "docs" / "research" / "UI-INDUSTRY-1000-BATCH-006.md"

ns = runpy.run_path(str(TEST))
records = ns["BATCH_006"]
assert len(records) == 100
assert len({r["slug"] for r in records}) == 100

graph = json.loads(GRAPH.read_text(encoding="utf-8"))
skills = graph["skills"]
prior_count = len(skills)
new_slugs = {r["slug"] for r in records}

if prior_count == 774:
    assert not (new_slugs & set(skills)), sorted(new_slugs & set(skills))
    prior_outputs = {node.get("output") for node in skills.values()}
    for record in records:
        assert record["parent"] in skills, record
        assert record["output"] not in prior_outputs, record
        prior_outputs.add(record["output"])
        skills[record["slug"]] = {
            "family": record["family"],
            "parent": record["parent"],
            "output": record["output"],
        }
elif prior_count == 874:
    for record in records:
        assert skills.get(record["slug"]) == {
            "family": record["family"],
            "parent": record["parent"],
            "output": record["output"],
        }, record["slug"]
else:
    raise AssertionError(f"unexpected graph baseline: {prior_count}")

assert len(skills) == 874
GRAPH.write_text(json.dumps(graph, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def replace_exact(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    count = text.count(old)
    assert count == 1, (path, old, count)
    path.write_text(text.replace(old, new), encoding="utf-8")


replace_exact(ROOT / "README.md", "`774 canonical skills`", "`874 canonical skills`")
replace_exact(ROOT / "README-VN.md", "`774 skill chuẩn`", "`874 skill chuẩn`")
replace_exact(ROOT / "README-CN.md", "`774 个 canonical skills`", "`874 个 canonical skills`")
replace_exact(
    ROOT / "AGENTS.md",
    "The canonical graph currently contains **774 canonical skills**: the historical 174-skill baseline plus 600 independently owned UI-industry specialists across Batch 001, Batch 002, Batch 003, Batch 004 and Batch 005.",
    "The canonical graph currently contains **874 canonical skills**: the historical 174-skill baseline plus 700 independently owned UI-industry specialists across Batch 001, Batch 002, Batch 003, Batch 004, Batch 005 and Batch 006.",
)

clean = ROOT / "tests" / "test_clean_delivery_contract.py"
text = clean.read_text(encoding="utf-8")
old_record = '            ROOT / "docs" / "research" / "UI-INDUSTRY-1000-BATCH-005.md",\n'
assert text.count(old_record) == 1
text = text.replace(old_record, old_record + '            ROOT / "docs" / "research" / "UI-INDUSTRY-1000-BATCH-006.md",\n')
text = text.replace(
    "def test_repository_policy_matches_the_774_node_batch_005_graph(self):",
    "def test_repository_policy_matches_the_874_node_batch_006_graph(self):",
)
text = text.replace('self.assertIn("**774 canonical skills**", agents)', 'self.assertIn("**874 canonical skills**", agents)')
text = text.replace('self.assertIn("600 independently owned UI-industry specialists", agents)', 'self.assertIn("700 independently owned UI-industry specialists", agents)')
clean.write_text(text, encoding="utf-8")

batch005 = ROOT / "tests" / "test_ui_industry_batch_005.py"
text = batch005.read_text(encoding="utf-8")
old = "    def test_final_graph_count_is_exactly_774(self):\n        self.assertEqual(774, len(self.graph_skills))\n"
new = "    def test_batch005_baseline_remains_materialized(self):\n        self.assertGreaterEqual(len(self.graph_skills), 774)\n"
assert text.count(old) == 1
batch005.write_text(text.replace(old, new), encoding="utf-8")

SOURCES = {
    "design-system-governance": (
        "design-tokens/community-group@16c902d9327c18290e956a21130c445f1b88c40f",
        "openui/open-ui@8812cdc228a21f9366a21a07041b451603a3ca26",
        "Token interchange, component-state vocabulary, compatibility and extension mechanism evidence; local NUI semantics remain authoritative.",
    ),
    "adaptive-composition": (
        "adobe/react-spectrum@5d191ab94472daa8fa53d02e3c425639c2f381a7",
        "openui/open-ui@8812cdc228a21f9366a21a07041b451603a3ca26",
        "Adaptive/responsive mechanism evidence; no upstream breakpoint, visual treatment, or component composition is universalized.",
    ),
    "typography-engineering": (
        "adobe/react-spectrum@5d191ab94472daa8fa53d02e3c425639c2f381a7",
        "W3C CSS Fonts/Text specifications (normative web standards, live authority)",
        "Font loading, fallback, metrics, line breaking and runtime text behavior evidence; browser/platform standards outrank library choices.",
    ),
    "agentic-execution": (
        "ag-ui-protocol/ag-ui@87f3986597dcfe1a89a5974eec9d7badb2a5a22b",
        "CopilotKit/CopilotKit and assistant-ui/assistant-ui (mechanism corroboration; exact implementation not adopted)",
        "Event lifecycle, shared-state, tool/HITL and generative-UI mechanism evidence; it does not grant execution authority or certify safety.",
    ),
    "ui-evidence": (
        "storybookjs/storybook@2c9c87e59adbb23bb56ca4f6cf055f536ecea54a",
        "dequelabs/axe-core@4.12.1 release line plus browser/runtime evidence",
        "Isolated-state, interaction, visual-regression and accessibility evidence mechanisms; automated checks cannot certify full UX truth.",
    ),
    "game-ten-foot": (
        "godotengine/godot@9ba32b09e0dfa4a6c1b82312554894615c716cce",
        "Qt/Qt Quick control/focus mechanisms (corroboration)",
        "Directional focus, controller ownership and ten-foot runtime mechanism evidence; game-specific design truth remains product dependent.",
    ),
    "automotive-hmi": (
        "Android Automotive OS UX-restrictions / driver-distraction guidance (platform authority, accessed 2026-08-21)",
        "godotengine/godot@9ba32b09e0dfa4a6c1b82312554894615c716cce for directional-focus mechanism only",
        "Vehicle-state and input mechanism evidence; applicable OEM, market, safety and regulatory authority always outrank these examples.",
    ),
    "multi-surface-continuity": (
        "react-navigation/react-navigation@73f8c2982a8999f1e1dfb1cfbeae9d8dab0c1cc2",
        "expo/expo@5a97a546476fd0bea35227b60297ad472f065168",
        "Session/lifecycle/device mechanism evidence; identity, security, proximity and cross-device truth require local runtime verification.",
    ),
}


def frontmatter_description(text: str) -> str:
    m = re.search(r"^description:\s*(.+)$", text, re.MULTILINE)
    return m.group(1).strip() if m else ""


def section_body(text: str, needle: str) -> str:
    matches = list(re.finditer(r"^##\s+(.+)$", text, re.MULTILINE))
    for i, match in enumerate(matches):
        if needle.lower() in match.group(1).lower():
            start = match.end()
            end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
            return " ".join(text[start:end].strip().split())
    return ""


def first_sentence(text: str, limit: int = 420) -> str:
    text = " ".join(text.split())
    if not text:
        return "Not separately stated; inspect canonical skill body."
    parts = re.split(r"(?<=[.!?])\s+", text, maxsplit=1)
    return parts[0][:limit]


def decision_sentence(text: str) -> str:
    for sentence in re.split(r"(?<=[.!?])\s+", " ".join(text.split())):
        lowered = sentence.lower()
        if "this skill owns" in lowered or ("decision" in lowered and "owns" in lowered) or "owns the decision" in lowered:
            return sentence[:520]
    return first_sentence(section_body(text, "ownership"), 520)


def sibling_sentence(text: str) -> str:
    for needle in ("Sibling", "boundary", "exclusion"):
        body = section_body(text, needle)
        if body:
            return first_sentence(body, 520)
    return "Sibling boundary is defined in the canonical skill body and enforced by the Batch 006 admission court."


def failure_sentence(text: str) -> str:
    body = section_body(text, "Failure")
    if body:
        return first_sentence(body, 520)
    m = re.search(r"([^\n.!?]*Failure[^.!?]*[.!?])", text, re.IGNORECASE)
    return first_sentence(m.group(1) if m else "", 520)


def falsifier_sentence(text: str) -> str:
    body = section_body(text, "Falsif")
    return first_sentence(body, 520)


def delete_sentence(text: str) -> str:
    for needle in ("Delete-the-skill", "delete-the-skill"):
        body = section_body(text, needle)
        if body:
            return first_sentence(body, 520)
    m = re.search(r"([^\n]*Delete-the-skill[^\n]*)", text, re.IGNORECASE)
    return first_sentence(m.group(1) if m else "", 520)


lines = [
    "# UI Industry 1000 — Batch 006 Research, Provenance, and Ownership Ledger",
    "",
    "## Status and non-generation rule",
    "",
    "Batch 006 starts from the 774-node canonical graph and admits exactly 100 independently owned specialists, producing the 874-node graph. The 100 count is a delivery constraint, never a license to create cosmetic siblings.",
    "",
    "Canonical `SKILL.md` prose was authored independently. External systems are mechanism/domain evidence only; no third-party skill prose, demo composition, brand trade dress, or library-specific visual language is copied. Deterministic automation in this batch is limited to graph registration, count bookkeeping, validation, and this provenance index; it does not create or rewrite canonical skill bodies.",
    "",
    "## Snapshot and source-role matrix",
    "",
    "| Court | Primary snapshot / authority | Secondary evidence | Transfer boundary |",
    "|---|---|---|---|",
]
for court, (primary, secondary, role) in SOURCES.items():
    lines.append(f"| {court} | `{primary}` | {secondary} | {role} |")

lines += [
    "",
    "## Admission rules",
    "",
    "Every owner below survived parent/sibling review and the delete-the-skill test. If removing a candidate leaves no material decision or failure class unowned, that candidate is not canonical. Repository popularity is never authority, and source implementation details are not generalized beyond the mechanism they evidence.",
    "",
    "## Exact ownership ledger",
    "",
]

for record in records:
    path = ROOT / "skills" / record["slug"] / "SKILL.md"
    text = path.read_text(encoding="utf-8")
    assert len(text) >= 2800, record["slug"]
    primary, secondary, role = SOURCES[record["court"]]
    lines += [
        f"### `{record['slug']}`",
        f"Parent: `{record['parent']}`",
        f"Trigger: {frontmatter_description(text)}",
        f"Decision owned: {decision_sentence(text)}",
        f"Sibling exclusion: {sibling_sentence(text)}",
        f"Failure class: {failure_sentence(text)}",
        f"Falsifier: {falsifier_sentence(text)}",
        f"Output: `{record['output']}`",
        f"Evidence role: {role} Primary pin: `{primary}`. Secondary: {secondary}.",
        f"Delete-the-skill: {delete_sentence(text)}",
        "",
    ]

PROVENANCE.parent.mkdir(parents=True, exist_ok=True)
PROVENANCE.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")

print("Batch 006 integrated: graph=874, provenance=100, current counts updated")
