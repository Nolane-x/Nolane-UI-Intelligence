from __future__ import annotations

import json
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GRAPH_PATH = ROOT / "skills" / "skill-graph.json"
TEST_PATH = ROOT / "tests" / "test_ui_industry_batch_003.py"

# Deterministic graph bookkeeping only. This script never reads, creates, or rewrites SKILL.md prose.
contract = runpy.run_path(str(TEST_PATH))
batch = contract["BATCH_003"]

graph = json.loads(GRAPH_PATH.read_text(encoding="utf-8"))
skills = graph["skills"]

if len(skills) == 474 and all(slug in skills for slug, _, _, _ in batch):
    print("Batch 003 graph already integrated")
    raise SystemExit(0)

if len(skills) != 374:
    raise SystemExit(f"expected 374-node pre-Batch-003 graph, found {len(skills)}")

batch_slugs = {slug for slug, _, _, _ in batch}
if len(batch) != 100 or len(batch_slugs) != 100:
    raise SystemExit("Batch 003 contract is not exactly 100 unique skills")

existing_outputs = {node.get("output") for node in skills.values() if isinstance(node, dict)}
new_outputs = {output for _, _, _, output in batch}
if len(new_outputs) != 100 or existing_outputs & new_outputs:
    raise SystemExit("Batch 003 outputs are not unique against the existing graph")

for slug, family, parent, output in batch:
    if slug in skills:
        raise SystemExit(f"Batch 003 slug already exists: {slug}")
    if parent not in skills:
        raise SystemExit(f"parent must exist before child insertion: {slug} -> {parent}")
    skills[slug] = {"family": family, "parent": parent, "output": output}

if len(skills) != 474:
    raise SystemExit(f"expected 474 nodes after integration, found {len(skills)}")

GRAPH_PATH.write_text(json.dumps(graph, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print("Integrated exactly 100 Batch 003 nodes; graph count = 474")
