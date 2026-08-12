"""Mandatory routing for standardized emerging UI domains in saturation extension two."""
from __future__ import annotations
from typing import Any


def mandatory_standardized_emerging_routes(profile: dict[str, Any]) -> set[str]:
    domains = set(profile.get("specialized_ui_domains", []))
    required: set[str] = set()
    if "affective-adaptive" in domains:
        required |= {
            "designing-affective-adaptive-interfaces",
            "designing-permissions-and-consent",
            "designing-privacy-sensitive-interfaces",
            "critiquing-security-and-privacy",
        }
    if "avatar-embodied" in domains:
        required |= {
            "designing-avatar-embodied-representation",
            "critiquing-security-and-privacy",
            "critiquing-accessibility",
        }
    if "aac-communication" in domains:
        required |= {
            "designing-accessible-interfaces",
            "designing-aac-communication-interfaces",
            "critiquing-accessibility",
        }
    return required
