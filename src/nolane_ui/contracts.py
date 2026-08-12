"""Cross-file skill contract integrity for NUI.

The skill graph is the canonical machine-readable contract. Skill prose must
name the same parent and output IDs so routers, agents and validators cannot
silently drift apart.
"""
from __future__ import annotations

import re
from pathlib import Path
from typing import Any

_FRONTMATTER_NAME = re.compile(r"(?m)^name:\s*([^\n]+)\s*$")
_PARENT = re.compile(r"\*\*Required parent:\*\*\s*`([^`]+)`")
_OUTPUT_HEADING = re.compile(r"(?ims)^(##\s+Output[^\n]*\n.*?)(?=^##\s+|\Z)")


def _extract_output_section(text: str) -> str:
    match = _OUTPUT_HEADING.search(text)
    return match.group(1) if match else ""


def validate_skill_contract_integrity(root: Path | str, graph: dict[str, Any]) -> dict[str, Any]:
    root = Path(root)
    errors: list[str] = []
    skills = graph.get("skills", {}) if isinstance(graph, dict) else {}
    checked = 0
    for name, node in skills.items():
        checked += 1
        path = root / "skills" / name / "SKILL.md"
        if not path.is_file():
            errors.append(f"skill {name} missing SKILL.md")
            continue
        text = path.read_text(encoding="utf-8")
        frontmatter_name = _FRONTMATTER_NAME.search(text)
        if not frontmatter_name or frontmatter_name.group(1).strip() != name:
            errors.append(f"skill {name} frontmatter name mismatch")

        parent = node.get("parent")
        parent_match = _PARENT.search(text)
        if parent is None:
            # Roots may omit a parent declaration or explicitly say none.
            pass
        elif not parent_match or parent_match.group(1).strip() != parent:
            errors.append(f"skill {name} parent contract does not match canonical parent {parent}")

        output = node.get("output")
        output_section = _extract_output_section(text)
        if not isinstance(output, str) or not output:
            errors.append(f"skill {name} graph output is invalid")
        elif f"`{output}`" not in output_section:
            errors.append(f"skill {name} output contract does not name canonical output {output}")

    return {"valid": not errors, "errors": errors, "checked": checked}


__all__ = ["validate_skill_contract_integrity"]
