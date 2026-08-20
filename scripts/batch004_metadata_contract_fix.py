from __future__ import annotations

import re
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BATCH_TEST = ROOT / "tests" / "test_ui_industry_batch_004.py"


def normalize_frontmatter_description(text: str, slug: str) -> str:
    match = re.match(r"\A---\n(?P<frontmatter>.*?)\n---\n", text, re.S)
    if not match:
        raise SystemExit(f"{slug}: missing canonical YAML frontmatter")

    frontmatter = match.group("frontmatter")
    description_match = re.search(r"(?m)^description:\s*(?P<description>.+)$", frontmatter)
    if not description_match:
        raise SystemExit(f"{slug}: missing frontmatter description")

    description = description_match.group("description").strip()
    if description.startswith("Use when"):
        return text

    normalized = (
        "Use when this specialist's decision ownership is materially in scope. "
        + description
    )
    if len(normalized) > 500:
        raise SystemExit(
            f"{slug}: normalized description exceeds 500 characters ({len(normalized)})"
        )

    new_frontmatter = (
        frontmatter[: description_match.start("description")]
        + normalized
        + frontmatter[description_match.end("description") :]
    )
    return text[: match.start("frontmatter")] + new_frontmatter + text[match.end("frontmatter") :]


def ensure_parent_contract(text: str, slug: str, parent: str) -> str:
    required_line = f"**Required parent:** `{parent}`."
    if "## Parent Contract" in text:
        if required_line not in text:
            raise SystemExit(
                f"{slug}: existing Parent Contract does not name canonical parent {parent}"
            )
        return text

    heading = re.search(r"(?m)^# .+$", text)
    if not heading:
        raise SystemExit(f"{slug}: missing H1 heading")

    section = (
        "\n\n## Parent Contract\n\n"
        + required_line
        + "\n\nInherit the broader routing and decision boundary from this canonical parent; "
        "this specialist remains accountable only for the narrower ownership, failure topology, "
        "falsification criteria, and output contract defined below."
    )
    return text[: heading.end()] + section + text[heading.end() :]


def main() -> None:
    namespace = runpy.run_path(str(BATCH_TEST))
    records = namespace["BATCH_004"]
    if len(records) != 200:
        raise SystemExit(f"expected 200 Batch 004 records, got {len(records)}")

    changed = 0
    for record in records:
        slug = record["slug"]
        parent = record["parent"]
        path = ROOT / "skills" / slug / "SKILL.md"
        if not path.is_file():
            raise SystemExit(f"{slug}: missing SKILL.md")

        original = path.read_text(encoding="utf-8")
        normalized = normalize_frontmatter_description(original, slug)
        normalized = ensure_parent_contract(normalized, slug, parent)
        if normalized != original:
            path.write_text(normalized, encoding="utf-8")
            changed += 1

    print(f"Batch 004 metadata contracts normalized for {changed} of {len(records)} skills.")


if __name__ == "__main__":
    main()
