"""Mandatory routing for emerging UI domains discovered by adversarial research."""
from __future__ import annotations

from typing import Any


def mandatory_emerging_routes(profile: dict[str, Any]) -> set[str]:
    surfaces = set(profile.get("platform_surfaces", []))
    modalities = set(profile.get("input_modalities", []))
    required: set[str] = set()
    if "robotics-teleoperation" in surfaces:
        required |= {"designing-robotic-teleoperation-interfaces", "engineering-human-factors", "critiquing-human-factors-and-safety", "critiquing-input-modality"}
    if "ambient-context-aware" in surfaces:
        required |= {"designing-ambient-context-aware-interfaces", "designing-privacy-sensitive-interfaces", "critiquing-ai-trust-and-agency", "critiquing-security-and-privacy"}
    if "supervisory-control-room" in surfaces:
        required |= {"designing-supervisory-control-room-hmi", "engineering-human-factors", "critiquing-human-factors-and-safety", "critiquing-cognitive-load"}
    if "neuroinput" in modalities:
        required |= {"designing-brain-computer-interface-ux", "engineering-human-factors", "critiquing-input-modality"}
    return required
