"""Mandatory routing for cross-device and accessibility-media decision classes."""
from __future__ import annotations
from typing import Any


def mandatory_third_extension_routes(profile: dict[str, Any]) -> set[str]:
    domains = set(profile.get("specialized_ui_domains", []))
    required: set[str] = set()
    if "cross-device-action-equivalence" in domains:
        required |= {
            "designing-cross-device-action-equivalence",
            "adapting-platform-conventions",
            "critiquing-input-modality",
        }
    if "accessibility-settings" in domains:
        required |= {
            "designing-accessible-interfaces",
            "designing-accessibility-settings-and-profiles",
            "critiquing-accessibility",
        }
    if "accessible-media" in domains:
        required |= {
            "designing-accessible-interfaces",
            "designing-accessible-media-alternatives",
            "critiquing-accessibility",
        }
    if "sign-language-presentation" in domains:
        required |= {
            "designing-accessible-interfaces",
            "designing-accessible-media-alternatives",
            "designing-sign-language-presentation",
            "critiquing-accessibility",
        }
    return required
