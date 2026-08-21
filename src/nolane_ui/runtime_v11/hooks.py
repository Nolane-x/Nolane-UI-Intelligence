"""Provider-neutral hook capability contracts for NUI V11.

This module describes what a host can truthfully expose. It does not install
hooks and it never grants permissions beyond the host's own policy.
"""
from __future__ import annotations

from typing import Any

_NATIVE_CAPABILITIES: dict[str, dict[str, Any]] = {
    "openai-codex": {
        "integration": "native-advisory",
        "events": {"pre_write": False, "post_write": True, "session_stop": True, "release_check": False},
        "can_block_write": False,
        "returns_findings_to_agent": True,
    },
    "claude-code": {
        "integration": "native-advisory",
        "events": {"pre_write": False, "post_write": True, "session_stop": True, "release_check": False},
        "can_block_write": False,
        "returns_findings_to_agent": True,
    },
    "cursor-compatible": {
        "integration": "native-preflight",
        "events": {"pre_write": True, "post_write": False, "session_stop": False, "release_check": False},
        "can_block_write": True,
        "returns_findings_to_agent": True,
    },
}

_MANUAL_IDS = {
    "google-antigravity",
    "gemini-cli",
    "opencode",
    "vscode-agent-compatible",
    "generic-mcp",
    "generic-cli",
}


def build_hook_capability(agent_id: str) -> dict[str, Any]:
    if agent_id in _NATIVE_CAPABILITIES:
        native = _NATIVE_CAPABILITIES[agent_id]
        capability = {
            "agent_id": agent_id,
            "integration": native["integration"],
            "events": dict(native["events"]),
            "can_block_write": bool(native["can_block_write"]),
            "returns_findings_to_agent": bool(native["returns_findings_to_agent"]),
        }
    elif agent_id in _MANUAL_IDS:
        capability = {
            "agent_id": agent_id,
            "integration": "manual",
            "events": {"pre_write": False, "post_write": False, "session_stop": False, "release_check": False},
            "can_block_write": False,
            "returns_findings_to_agent": False,
        }
    else:
        raise ValueError(f"unsupported runtime hook agent: {agent_id}")

    capability.update({
        "detector_command": "python scripts/nui-detect",
        "authority": "evidence-only",
        "permission_escalation": False,
        "edit_tier": "edit",
        "stop_tier": "session" if capability["events"]["session_stop"] else None,
        "release_tier": "release",
        "note": "Host event support is a capability declaration, not design authority. Unsupported events must be invoked manually rather than simulated.",
    })
    return capability


__all__ = ["build_hook_capability"]
