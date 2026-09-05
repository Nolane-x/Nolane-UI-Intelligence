"""Capability profiles shared by authored V13 rule shards.

These helpers only expand evidence capability metadata; they do not generate
rule prose, identifiers, failure modes, repairs, or verification contracts.
"""
from __future__ import annotations


def convergence_caps(**overrides: str) -> dict[str, str]:
    values = {
        "static": "PARTIAL",
        "dom": "PARTIAL",
        "computed-style": "PARTIAL",
        "browser-runtime": "PARTIAL",
        "interaction": "PARTIAL",
        "accessibility-tree": "UNSUPPORTED",
        "visual-render": "REQUIRED",
        "semantic-product": "REQUIRED",
        "cross-generation": "PARTIAL",
        "human-review": "REQUIRED",
    }
    values.update(overrides)
    return values


def interaction_caps(**overrides: str) -> dict[str, str]:
    values = {
        "static": "PARTIAL", "dom": "PARTIAL", "computed-style": "PARTIAL",
        "browser-runtime": "PARTIAL", "interaction": "REQUIRED", "accessibility-tree": "PARTIAL",
        "visual-render": "PARTIAL", "semantic-product": "REQUIRED", "cross-generation": "UNSUPPORTED",
        "human-review": "PARTIAL",
    }
    values.update(overrides)
    return values


__all__ = ["convergence_caps", "interaction_caps"]
