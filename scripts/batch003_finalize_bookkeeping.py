from __future__ import annotations

import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def replace_exact(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    if old not in text:
        raise SystemExit(f"expected text missing in {path.relative_to(ROOT)}: {old[:100]!r}")
    path.write_text(text.replace(old, new), encoding="utf-8")


# Historical batch tests preserve their own baseline, while the newest batch owns exact count.
test002 = ROOT / "tests" / "test_ui_industry_batch_002.py"
replace_exact(
    test002,
    "    def test_final_graph_count_is_exactly_374(self):\n        self.assertEqual(374, len(self.graph_skills))",
    "    def test_graph_preserves_batch_002_374_node_baseline(self):\n        self.assertGreaterEqual(len(self.graph_skills), 374)",
)

# English README.
readme = ROOT / "README.md"
replace_exact(readme, "`374 canonical skills`", "`474 canonical skills`")
replace_exact(readme, "## 374 canonical design faculties", "## 474 canonical design faculties")
replace_exact(readme, "NUI currently preserves **374 canonical skills**.", "NUI currently preserves **474 canonical skills**.")
replace_exact(readme, "skills/                         374 canonical faculties", "skills/                         474 canonical faculties")
replace_exact(
    readme,
    "Batch 002 adds 100 more independently authored specialists across high-friction input, navigation/findability, feedback/recovery, messaging/collaboration, onboarding, commerce lifecycle, content publishing, developer operations, and trust/account lifecycle. See [`docs/research/UI-INDUSTRY-1000-BATCH-001.md`](docs/research/UI-INDUSTRY-1000-BATCH-001.md) and [`docs/research/UI-INDUSTRY-1000-BATCH-002.md`](docs/research/UI-INDUSTRY-1000-BATCH-002.md) for exact inventories, ownership, provenance and non-generation constraints.",
    "Batch 002 adds 100 more independently authored specialists across high-friction input, navigation/findability, feedback/recovery, messaging/collaboration, onboarding, commerce lifecycle, content publishing, developer operations, and trust/account lifecycle. Batch 003 adds another 100 independently authored specialists across accessibility mechanics, globalization and locale mechanics, media playback, file transfer/storage, and device/physical-world integration. See [`docs/research/UI-INDUSTRY-1000-BATCH-001.md`](docs/research/UI-INDUSTRY-1000-BATCH-001.md), [`docs/research/UI-INDUSTRY-1000-BATCH-002.md`](docs/research/UI-INDUSTRY-1000-BATCH-002.md), and [`docs/research/UI-INDUSTRY-1000-BATCH-003.md`](docs/research/UI-INDUSTRY-1000-BATCH-003.md) for exact inventories, ownership, provenance and non-generation constraints.",
)

# Vietnamese README.
readme_vn = ROOT / "README-VN.md"
replace_exact(readme_vn, "`374 skill chuẩn`", "`474 skill chuẩn`")
replace_exact(readme_vn, "Agent không tải toàn bộ 374 skill.", "Agent không tải toàn bộ 474 skill.")
replace_exact(readme_vn, "## 374 design faculties chuẩn", "## 474 design faculties chuẩn")
replace_exact(readme_vn, "NUI hiện giữ **374 canonical skills**.", "NUI hiện giữ **474 canonical skills**.")
replace_exact(readme_vn, "skills/                         374 canonical faculties", "skills/                         474 canonical faculties")
replace_exact(
    readme_vn,
    "Batch 002 bổ sung thêm 100 specialist được viết độc lập về input có ma sát cao, navigation/findability, feedback/recovery, messaging/collaboration, onboarding, commerce lifecycle, content publishing, developer operations và trust/account lifecycle. Xem [`docs/research/UI-INDUSTRY-1000-BATCH-001.md`](docs/research/UI-INDUSTRY-1000-BATCH-001.md) và [`docs/research/UI-INDUSTRY-1000-BATCH-002.md`](docs/research/UI-INDUSTRY-1000-BATCH-002.md) để xem exact inventory, ownership, provenance và các ràng buộc chống sinh lặp.",
    "Batch 002 bổ sung thêm 100 specialist được viết độc lập về input có ma sát cao, navigation/findability, feedback/recovery, messaging/collaboration, onboarding, commerce lifecycle, content publishing, developer operations và trust/account lifecycle. Batch 003 bổ sung thêm 100 specialist được viết độc lập về accessibility mechanics, globalization/locale mechanics, media playback, file transfer/storage và device/physical-world integration. Xem [`docs/research/UI-INDUSTRY-1000-BATCH-001.md`](docs/research/UI-INDUSTRY-1000-BATCH-001.md), [`docs/research/UI-INDUSTRY-1000-BATCH-002.md`](docs/research/UI-INDUSTRY-1000-BATCH-002.md) và [`docs/research/UI-INDUSTRY-1000-BATCH-003.md`](docs/research/UI-INDUSTRY-1000-BATCH-003.md) để xem exact inventory, ownership, provenance và các ràng buộc chống sinh lặp.",
)

# Chinese README.
readme_cn = ROOT / "README-CN.md"
replace_exact(readme_cn, "`374 个 canonical skills`", "`474 个 canonical skills`")
replace_exact(readme_cn, "Agent 不应该一次性加载 374 个 skill。", "Agent 不应该一次性加载 474 个 skill。")
replace_exact(readme_cn, "## 374 个 canonical design faculties", "## 474 个 canonical design faculties")
replace_exact(readme_cn, "NUI 当前保持 **374 个 canonical skills**。", "NUI 当前保持 **474 个 canonical skills**。")
replace_exact(readme_cn, "skills/                         374 canonical faculties", "skills/                         474 canonical faculties")
replace_exact(
    readme_cn,
    "Batch 002 再增加 100 个独立编写的 specialist，覆盖高摩擦输入、navigation/findability、feedback/recovery、messaging/collaboration、onboarding、commerce lifecycle、content publishing、developer operations 以及 trust/account lifecycle。完整 inventory、ownership、provenance 与 anti-generation 约束见 [`docs/research/UI-INDUSTRY-1000-BATCH-001.md`](docs/research/UI-INDUSTRY-1000-BATCH-001.md) 和 [`docs/research/UI-INDUSTRY-1000-BATCH-002.md`](docs/research/UI-INDUSTRY-1000-BATCH-002.md)。",
    "Batch 002 再增加 100 个独立编写的 specialist，覆盖高摩擦输入、navigation/findability、feedback/recovery、messaging/collaboration、onboarding、commerce lifecycle、content publishing、developer operations 以及 trust/account lifecycle。Batch 003 再增加 100 个独立编写的 specialist，覆盖 accessibility mechanics、globalization/locale mechanics、media playback、file transfer/storage 与 device/physical-world integration。完整 inventory、ownership、provenance 与 anti-generation 约束见 [`docs/research/UI-INDUSTRY-1000-BATCH-001.md`](docs/research/UI-INDUSTRY-1000-BATCH-001.md)、[`docs/research/UI-INDUSTRY-1000-BATCH-002.md`](docs/research/UI-INDUSTRY-1000-BATCH-002.md) 和 [`docs/research/UI-INDUSTRY-1000-BATCH-003.md`](docs/research/UI-INDUSTRY-1000-BATCH-003.md)。",
)

# Repository policy.
agents = ROOT / "AGENTS.md"
replace_exact(
    agents,
    "34. The canonical graph currently contains **374 canonical skills**: the historical 174-skill baseline plus 200 independently owned UI-industry specialists across Batch 001 and Batch 002. Skill count remains descriptive, not a progress target; further expansion is allowed only for genuinely distinct decision/failure ownership.",
    "34. The canonical graph currently contains **474 canonical skills**: the historical 174-skill baseline plus 300 independently owned UI-industry specialists across Batch 001, Batch 002, and Batch 003. Skill count remains descriptive, not a progress target; further expansion is allowed only for genuinely distinct decision/failure ownership.",
)

# Deterministic provenance ledger from the already-locked acceptance metadata.
contract = runpy.run_path(str(ROOT / "tests" / "test_ui_industry_batch_003.py"))
batch = contract["BATCH_003"]
if len(batch) != 100:
    raise SystemExit(f"Batch 003 contract expected 100 entries, found {len(batch)}")

court_ranges = [
    (1, 20, "Accessibility mechanics"),
    (21, 40, "Globalization and locale mechanics"),
    (41, 60, "Media playback"),
    (61, 80, "File transfer and storage"),
    (81, 100, "Device and physical-world integration"),
]

lines = [
    "# UI Industry 1000 — Batch 003 Provenance and Ownership Record",
    "",
    "## Scope",
    "",
    "Batch 003 adds exactly 100 canonical specialist faculties to the 374-node Batch 002 graph, producing a 474-node canonical graph. The historical 174-skill baseline and all 200 Batch 001/002 specialists remain part of the same routed graph.",
    "",
    "This is a structural authorship and ownership record. It does **not** claim that adding these skills empirically improves model output; NUI V10 empirical claims remain bounded by real-model evidence.",
    "",
    "## Authorship and automation boundary",
    "",
    "All 100 Batch 003 `SKILL.md` bodies were authored individually. No loop, macro, template expander, bulk prose transformer, cloned body, or programmatic prompt-to-skill generator produced the skill prose. Shared headings are repository schema only; each skill owns a different decision boundary, failure topology, falsification/recovery court, and output contract.",
    "",
    "Temporary scripts are allowed only for deterministic graph/test/docs bookkeeping. `batch003_graph_integrate.py` reads the already-locked acceptance metadata and updates only `skills/skill-graph.json`; `batch003_finalize_bookkeeping.py` migrates counts/provenance/test bookkeeping. Both are excluded from the final product tree.",
    "",
    "## Decision courts",
    "",
]
for start, end, label in court_ranges:
    lines.append(f"- **{label}:** skills {start}–{end}.")

lines += [
    "",
    "## Exact inventory and canonical ownership",
    "",
    "| # | Skill | Family | Parent | Output |",
    "|---:|---|---|---|---|",
]
for index, (slug, family, parent, output) in enumerate(batch, 1):
    lines.append(f"| {index} | `{slug}` | `{family}` | `{parent}` | `{output}` |")

lines += [
    "",
    "## Anti-overlap admission rule",
    "",
    "A candidate is admitted only when removing it and routing solely to its parent leaves a material decision or failure class underspecified. Existing broad owners are not recreated. Examples intentionally excluded as duplicate parents include generic file upload, accessible drag-and-drop, haptics/multisensory feedback, embedded kiosk interfaces, broad screen-reader accessibility, and broad localization.",
    "",
    "Batch 003 therefore introduces narrow runtime/state ownership such as resumable uploads rather than another uploader, live-region announcement policy rather than another screen-reader owner, and device pairing/discovery protocols rather than another generic hardware surface.",
    "",
    "## Structural gates",
    "",
    "The Batch 003 acceptance suite requires exactly 100 unique slugs and outputs, exact family/parent/output metadata, valid root reachability without cycles, final graph count 474, skill frontmatter identity, behavioral-depth sections, minimum body depth, no exact normalized duplicate bodies, and no pair whose normalized body similarity reaches the trivial-rename threshold.",
    "",
    "Full repository completion still requires the canonical read-only Verify NUI workflow, all historical tests, release-packet generation, repository validation, clean final changed-files review, and an exact-head successful CI run.",
    "",
]
(ROOT / "docs" / "research" / "UI-INDUSTRY-1000-BATCH-003.md").write_text("\n".join(lines), encoding="utf-8")

print("Batch 003 deterministic bookkeeping finalized")
