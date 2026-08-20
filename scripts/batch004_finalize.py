from __future__ import annotations

import json
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GRAPH = ROOT / "skills" / "skill-graph.json"
BATCH_TEST = ROOT / "tests" / "test_ui_industry_batch_004.py"
BATCH3_TEST = ROOT / "tests" / "test_ui_industry_batch_003.py"


def replace_exact(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    if old not in text:
        raise SystemExit(f"expected text not found in {path}: {old!r}")
    path.write_text(text.replace(old, new), encoding="utf-8")


namespace = runpy.run_path(str(BATCH_TEST))
records = namespace["BATCH_004"]
if len(records) != 200:
    raise SystemExit(f"expected 200 Batch 004 records, got {len(records)}")

payload = json.loads(GRAPH.read_text(encoding="utf-8"))
skills = payload["skills"]
if len(skills) != 474:
    raise SystemExit(f"Batch 004 stacked base must contain 474 graph nodes, got {len(skills)}")

for record in records:
    slug = record["slug"]
    if slug in skills:
        raise SystemExit(f"Batch 004 graph node already exists: {slug}")
    skills[slug] = {
        "family": record["family"],
        "parent": record["parent"],
        "output": record["output"],
    }

if len(skills) != 674:
    raise SystemExit(f"final graph must contain 674 nodes, got {len(skills)}")
GRAPH.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

replace_exact(
    BATCH3_TEST,
    "    def test_final_graph_count_is_exactly_474(self):\n        self.assertEqual(474, len(self.graph_skills))",
    "    def test_graph_preserves_batch_003_baseline_at_or_above_474(self):\n        self.assertGreaterEqual(len(self.graph_skills), 474)",
)

readme = ROOT / "README.md"
replace_exact(readme, "`374 canonical skills`", "`674 canonical skills`")
replace_exact(readme, "## 374 canonical design faculties", "## 674 canonical design faculties")
replace_exact(readme, "NUI currently preserves **374 canonical skills**.", "NUI currently preserves **674 canonical skills**.")
replace_exact(
    readme,
    "Batch 002 adds 100 more independently authored specialists across high-friction input, navigation/findability, feedback/recovery, messaging/collaboration, onboarding, commerce lifecycle, content publishing, developer operations, and trust/account lifecycle. See [`docs/research/UI-INDUSTRY-1000-BATCH-001.md`](docs/research/UI-INDUSTRY-1000-BATCH-001.md) and [`docs/research/UI-INDUSTRY-1000-BATCH-002.md`](docs/research/UI-INDUSTRY-1000-BATCH-002.md) for exact inventories, ownership, provenance and non-generation constraints.",
    "Batch 002 adds 100 more independently authored specialists across high-friction input, navigation/findability, feedback/recovery, messaging/collaboration, onboarding, commerce lifecycle, content publishing, developer operations, and trust/account lifecycle. Batch 003 contributes another 100 independently authored specialists across accessibility mechanics, globalization/locale behavior, media playback, file/storage workflows and device/physical-world integration. Batch 004 adds 200 independently authored specialists across diagramming, project operations, incident response, software delivery, scientific instrumentation, 3D/CAD, nonlinear media editing, digital learning, financial operations and security operations. See the Batch 001–004 research records for exact inventory, ownership, provenance and non-generation constraints.",
)

vn = ROOT / "README-VN.md"
replace_exact(vn, "`374 skill chuẩn`", "`674 skill chuẩn`")
replace_exact(vn, "Agent không tải toàn bộ 374 skill.", "Agent không tải toàn bộ 674 skill.")
replace_exact(vn, "## 374 design faculties chuẩn", "## 674 design faculties chuẩn")
replace_exact(vn, "NUI hiện giữ **374 canonical skills**.", "NUI hiện giữ **674 canonical skills**.")
replace_exact(
    vn,
    "Batch 002 bổ sung thêm 100 specialist được viết độc lập về input có ma sát cao, navigation/findability, feedback/recovery, messaging/collaboration, onboarding, commerce lifecycle, content publishing, developer operations và trust/account lifecycle. Xem [`docs/research/UI-INDUSTRY-1000-BATCH-001.md`](docs/research/UI-INDUSTRY-1000-BATCH-001.md) và [`docs/research/UI-INDUSTRY-1000-BATCH-002.md`](docs/research/UI-INDUSTRY-1000-BATCH-002.md) để xem exact inventory, ownership, provenance và các ràng buộc chống sinh lặp.",
    "Batch 002 bổ sung thêm 100 specialist được viết độc lập về input có ma sát cao, navigation/findability, feedback/recovery, messaging/collaboration, onboarding, commerce lifecycle, content publishing, developer operations và trust/account lifecycle. Batch 003 thêm 100 specialist độc lập về accessibility mechanics, globalization/locale, media playback, file/storage và tích hợp thiết bị/thế giới vật lý. Batch 004 thêm 200 specialist độc lập về diagramming, project operations, incident response, software delivery, scientific instrumentation, 3D/CAD, nonlinear media editing, digital learning, financial operations và security operations. Inventory, ownership, provenance và ràng buộc chống sinh lặp được lưu trong các research record Batch 001–004.",
)

cn = ROOT / "README-CN.md"
replace_exact(cn, "`374 个 canonical skills`", "`674 个 canonical skills`")
replace_exact(cn, "Agent 不应该一次性加载 374 个 skill。", "Agent 不应该一次性加载 674 个 skill。")
replace_exact(cn, "## 374 个 canonical design faculties", "## 674 个 canonical design faculties")
replace_exact(cn, "NUI 当前保持 **374 个 canonical skills**。", "NUI 当前保持 **674 个 canonical skills**。")
replace_exact(
    cn,
    "Batch 002 再增加 100 个独立编写的 specialist，覆盖高摩擦输入、navigation/findability、feedback/recovery、messaging/collaboration、onboarding、commerce lifecycle、content publishing、developer operations 以及 trust/account lifecycle。完整 inventory、ownership、provenance 与 anti-generation 约束见 [`docs/research/UI-INDUSTRY-1000-BATCH-001.md`](docs/research/UI-INDUSTRY-1000-BATCH-001.md) 和 [`docs/research/UI-INDUSTRY-1000-BATCH-002.md`](docs/research/UI-INDUSTRY-1000-BATCH-002.md)。",
    "Batch 002 再增加 100 个独立编写的 specialist，覆盖高摩擦输入、navigation/findability、feedback/recovery、messaging/collaboration、onboarding、commerce lifecycle、content publishing、developer operations 以及 trust/account lifecycle。Batch 003 再增加 100 个独立 specialist，覆盖 accessibility mechanics、globalization/locale、media playback、file/storage workflow 与 device/physical-world integration。Batch 004 再增加 200 个独立 specialist，覆盖 diagramming、project operations、incident response、software delivery、scientific instrumentation、3D/CAD、nonlinear media editing、digital learning、financial operations 与 security operations。Batch 001–004 research record 保存完整 inventory、ownership、provenance 与 anti-generation 约束。",
)

agents = ROOT / "AGENTS.md"
replace_exact(
    agents,
    "34. The canonical graph currently contains **374 canonical skills**: the historical 174-skill baseline plus 200 independently owned UI-industry specialists across Batch 001 and Batch 002. Skill count remains descriptive, not a progress target; further expansion is allowed only for genuinely distinct decision/failure ownership.",
    "34. The canonical graph currently contains **674 canonical skills**: the historical 174-skill baseline plus 500 independently owned UI-industry specialists across Batch 001, Batch 002, Batch 003 and Batch 004. Skill count remains descriptive, not a progress target; further expansion is allowed only for genuinely distinct decision/failure ownership.",
)

provenance = ROOT / "docs" / "research" / "UI-INDUSTRY-1000-BATCH-004.md"
lines = [
    "# UI Industry 1000 — Batch 004 (200 skills)",
    "",
    "## Scope",
    "",
    "Batch 004 expands the stacked 474-node canonical graph to 674 nodes with 200 specialist faculties. The substantive `SKILL.md` bodies were individually authored; no loop, mass rename, or body template was used to generate their prose. Deterministic code is used only for graph/document bookkeeping after the 200-body inventory was locked in tests.",
    "",
    "The exact pre-authoring inventory is `docs/research/UI-INDUSTRY-1000-BATCH-004-INVENTORY.md`. The acceptance contract is `tests/test_ui_industry_batch_004.py`.",
    "",
    "## Courts",
    "",
    "1. Diagramming and node-graph authoring — 20",
    "2. Project and work management — 20",
    "3. Incident response and reliability operations — 20",
    "4. Software delivery and release engineering — 20",
    "5. Scientific and engineering instrumentation — 20",
    "6. 3D/CAD authoring — 20",
    "7. Nonlinear media editing — 20",
    "8. Digital learning and assessment — 20",
    "9. Financial operations — 20",
    "10. Security operations — 20",
    "",
    "## Admission and anti-generation rule",
    "",
    "A skill is admitted only when it owns a consequential decision/failure class not already owned by its parent or siblings. Shared section headings are repository schema, not a prose-generation template. The acceptance suite rejects missing bodies, bodies below the locked structural floor, missing behavioral sections, metadata drift, output collisions, parent cycles, exact normalized duplicates, trivial-renaming similarity, placeholders, and any final graph count other than 674.",
    "",
    "## Canonical metadata",
    "",
    "| Skill | Court | Family | Parent | Output |",
    "|---|---|---|---|---|",
]
for record in records:
    lines.append(f"| `{record['slug']}` | {record['court']} | `{record['family']}` | `{record['parent']}` | `{record['output']}` |")
lines += [
    "",
    "## Evidence boundary",
    "",
    "Structural verification can prove corpus/graph invariants and anti-duplication gates. It does not by itself prove that any model's aesthetic output improves. Claims of model-quality improvement remain subject to NUI's independent empirical evaluation faculties.",
]
provenance.write_text("\n".join(lines) + "\n", encoding="utf-8")

print("Batch 004 deterministic finalization prepared: 674 graph nodes, docs synchronized, historical Batch 003 count gate migrated.")
