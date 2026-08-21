"""Shared contracts for NUI V11 runtime design intelligence."""
from __future__ import annotations

RULE_CLASSES = frozenset({"mechanical", "contextual", "genericness", "advisory"})
RULE_TIERS = frozenset({"edit", "session", "release"})
RULE_ENGINES = frozenset({"text", "markup", "css", "browser"})
FINDING_SEVERITIES = frozenset({"critical", "major", "moderate", "minor", "observation"})

# Taste-sensitive rules are evidence for criticism. They never earn the right to
# interrupt a write merely by existing in the registry.
EDIT_FORBIDDEN_CLASSES = frozenset({"genericness", "advisory"})

SCANNABLE_SUFFIXES = frozenset({
    ".html", ".htm", ".tsx", ".jsx", ".vue", ".svelte", ".astro",
    ".css", ".scss", ".sass", ".less", ".ts", ".js",
})

NUI_FINDING_REQUIRED_FIELDS = (
    "finding_id",
    "domain",
    "severity",
    "evidence",
    "violated_constraint",
    "user_impact",
    "falsifier",
    "recommended_repair",
    "status",
)

__all__ = [
    "EDIT_FORBIDDEN_CLASSES",
    "FINDING_SEVERITIES",
    "NUI_FINDING_REQUIRED_FIELDS",
    "RULE_CLASSES",
    "RULE_ENGINES",
    "RULE_TIERS",
    "SCANNABLE_SUFFIXES",
]
