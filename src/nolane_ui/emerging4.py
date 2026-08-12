"""Mandatory routing for flight-deck and in-product-assistance decision classes."""
from __future__ import annotations
from typing import Any


def mandatory_fourth_extension_routes(profile: dict[str, Any]) -> set[str]:
    surfaces = set(profile.get("platform_surfaces", []))
    domains = set(profile.get("specialized_ui_domains", []))
    required: set[str] = set()
    if "flight-deck" in surfaces:
        required |= {
            "designing-flight-deck-interfaces",
            "engineering-human-factors",
            "designing-high-stakes-decisions",
            "critiquing-human-factors-and-safety",
        }
    if "in-product-assistance" in domains:
        required |= {
            "designing-in-product-assistance",
            "critiquing-user-experience",
        }
    return required
