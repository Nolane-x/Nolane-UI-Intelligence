from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def replace_once(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{path.name}: expected exactly one match for {old!r}, found {count}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


vn = ROOT / "README-VN.md"
replace_once(vn, "`v0.10.0` · `274 skill chuẩn`", "`v0.10.0` · `374 skill chuẩn`")
replace_once(vn, "Agent không tải toàn bộ 274 skill.", "Agent không tải toàn bộ 374 skill.")
replace_once(vn, "## 274 design faculties chuẩn", "## 374 design faculties chuẩn")
replace_once(vn, "NUI hiện giữ **274 canonical skills**.", "NUI hiện giữ **374 canonical skills**.")
replace_once(
    vn,
    "Batch 001 bổ sung 100 specialist được viết độc lập về motion, rich controls, direct manipulation, spreadsheet/data, enterprise workflow, billing, scheduling, geospatial và historical state. Xem [`docs/research/UI-INDUSTRY-1000-BATCH-001.md`](docs/research/UI-INDUSTRY-1000-BATCH-001.md) để xem exact inventory, provenance và các ràng buộc chống sinh lặp.",
    "Batch 001 bổ sung 100 specialist được viết độc lập về motion, rich controls, direct manipulation, spreadsheet/data, enterprise workflow, billing, scheduling, geospatial và historical state. Batch 002 bổ sung thêm 100 specialist được viết độc lập về input có ma sát cao, navigation/findability, feedback/recovery, messaging/collaboration, onboarding, commerce lifecycle, content publishing, developer operations và trust/account lifecycle. Xem [`docs/research/UI-INDUSTRY-1000-BATCH-001.md`](docs/research/UI-INDUSTRY-1000-BATCH-001.md) và [`docs/research/UI-INDUSTRY-1000-BATCH-002.md`](docs/research/UI-INDUSTRY-1000-BATCH-002.md) để xem exact inventory, ownership, provenance và các ràng buộc chống sinh lặp."
)
replace_once(vn, "skills/                         274 canonical faculties", "skills/                         374 canonical faculties")

cn = ROOT / "README-CN.md"
replace_once(cn, "`v0.10.0` · `274 个 canonical skills`", "`v0.10.0` · `374 个 canonical skills`")
replace_once(cn, "Agent 不应该一次性加载 274 个 skill。", "Agent 不应该一次性加载 374 个 skill。")
replace_once(cn, "## 274 个 canonical design faculties", "## 374 个 canonical design faculties")
replace_once(cn, "NUI 当前保持 **274 个 canonical skills**。", "NUI 当前保持 **374 个 canonical skills**。")
replace_once(
    cn,
    "Batch 001 增加了 100 个独立编写的 specialist，覆盖 motion、rich controls、direct manipulation、spreadsheet/data、enterprise workflow、billing、scheduling、geospatial 和 historical state。完整 inventory、provenance 与 anti-generation 约束见 [`docs/research/UI-INDUSTRY-1000-BATCH-001.md`](docs/research/UI-INDUSTRY-1000-BATCH-001.md)。",
    "Batch 001 增加了 100 个独立编写的 specialist，覆盖 motion、rich controls、direct manipulation、spreadsheet/data、enterprise workflow、billing、scheduling、geospatial 和 historical state。Batch 002 再增加 100 个独立编写的 specialist，覆盖高摩擦输入、navigation/findability、feedback/recovery、messaging/collaboration、onboarding、commerce lifecycle、content publishing、developer operations 以及 trust/account lifecycle。完整 inventory、ownership、provenance 与 anti-generation 约束见 [`docs/research/UI-INDUSTRY-1000-BATCH-001.md`](docs/research/UI-INDUSTRY-1000-BATCH-001.md) 和 [`docs/research/UI-INDUSTRY-1000-BATCH-002.md`](docs/research/UI-INDUSTRY-1000-BATCH-002.md)。"
)
replace_once(cn, "skills/                         274 canonical faculties", "skills/                         374 canonical faculties")

agents = ROOT / "AGENTS.md"
replace_once(
    agents,
    "34. The canonical graph currently contains **274 canonical skills**: the historical 174-skill baseline plus 100 independently owned UI-industry specialists. Skill count remains descriptive, not a progress target; further expansion is allowed only for genuinely distinct decision/failure ownership.",
    "34. The canonical graph currently contains **374 canonical skills**: the historical 174-skill baseline plus 200 independently owned UI-industry specialists across Batch 001 and Batch 002. Skill count remains descriptive, not a progress target; further expansion is allowed only for genuinely distinct decision/failure ownership."
)

english = (ROOT / "README.md").read_text(encoding="utf-8")
if "`374 canonical skills`" not in english or "## 374 canonical design faculties" not in english:
    raise SystemExit("README.md is not already aligned to 374")

print("Batch 002 documentation finalized: README-VN, README-CN, AGENTS")
