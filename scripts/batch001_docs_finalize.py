from pathlib import Path

root = Path(__file__).resolve().parents[1]

agents = root / "AGENTS.md"
agents_text = agents.read_text(encoding="utf-8")
old_count = "Current canonical skill count: 174."
new_count = (
    "Current canonical skill count: 274. The historical 174-skill depth baseline remains protected; "
    "the UI-industry roadmap may grow toward 1,000 only through distinct decision ownership, never duplicate inflation."
)
if agents_text.count(old_count) != 1:
    raise SystemExit(f"AGENTS.md: expected one historical count marker, found {agents_text.count(old_count)}")
agents.write_text(agents_text.replace(old_count, new_count, 1), encoding="utf-8")

sources = root / "docs" / "research" / "SOURCES.md"
sources_text = sources.read_text(encoding="utf-8")
heading = "## UI Industry 1000 — Batch 001"
if heading not in sources_text:
    sources_text += """

## UI Industry 1000 — Batch 001

Batch 001 expands the canonical graph from the historical 174-skill baseline to 274 skills with 100 independently authored specialists. Its exact inventory, ownership boundaries, source posture and anti-generation constraints are recorded in [`UI-INDUSTRY-1000-BATCH-001.md`](UI-INDUSTRY-1000-BATCH-001.md).

The batch continues to use this source ledger's authority order. WCAG/WAI-ARIA APG and authoritative platform guidance constrain semantics and accessibility; mature design systems such as Carbon, Fluent, Spectrum, Material and GOV.UK corroborate component/state practice; OpenDesign, `VoltAgent/awesome-design-md`, `bergside/awesome-design-skills` and similar public corpora are discovery/mechanism sources only. No discovery corpus is promoted into a global aesthetic authority, and no Batch 001 skill body was bulk-copied from those collections.
"""
sources.write_text(sources_text, encoding="utf-8")
