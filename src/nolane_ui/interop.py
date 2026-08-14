"""NUI v8 portable agent interoperability and external-skill trust invariants."""
from __future__ import annotations

import re
from pathlib import Path
from typing import Any

_SHA40 = re.compile(r"^[0-9a-f]{40}$", re.I)
_SHA256 = re.compile(r"^sha256:[0-9a-f]{64}$", re.I)
_ALLOWED_ADOPTION = {"mechanism-summary-only", "reference-only", "vendored-reviewed", "local-rewrite"}


def validate_agent_interop_registry(record: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    if not isinstance(record, dict):
        return {"valid": False, "errors": ["agent interoperability registry must be an object"]}
    if record.get("version") != 8:
        errors.append("agent interoperability registry must declare version 8")
    adapters = record.get("adapters")
    if not isinstance(adapters, list) or not adapters:
        return {"valid": False, "errors": errors + ["agent interoperability registry requires adapters[]"]}
    ids: set[str] = set()
    for idx, item in enumerate(adapters):
        if not isinstance(item, dict):
            errors.append(f"adapter[{idx}] must be an object")
            continue
        aid = str(item.get("id", "")).strip()
        if not aid:
            errors.append(f"adapter[{idx}] requires id")
            continue
        if aid in ids:
            errors.append(f"duplicate agent adapter id {aid}")
        ids.add(aid)
        if not item.get("surface"):
            errors.append(f"adapter {aid} requires surface")
        roots = item.get("skill_roots", [])
        if roots is not None and not isinstance(roots, list):
            errors.append(f"adapter {aid} skill_roots must be a list")
        if not item.get("evidence"):
            errors.append(f"adapter {aid} requires current primary-source evidence")
        if not item.get("permission_boundary"):
            errors.append(f"adapter {aid} requires permission_boundary")
        if item.get("authority_escalation") is not False:
            errors.append(f"adapter {aid} must set authority_escalation=false")
    required = {"openai-codex", "claude-code", "google-antigravity", "generic-mcp", "generic-cli"}
    missing = sorted(required - ids)
    if missing:
        errors.append(f"agent interoperability registry missing required adapters {missing}")
    return {"valid": not errors, "errors": errors, "adapter_count": len(ids)}


def validate_external_skill_trust(record: dict[str, Any]) -> dict[str, Any]:
    """Treat third-party agent skills as untrusted supply-chain input until reviewed."""
    errors: list[str] = []
    if not isinstance(record, dict):
        return {"valid": False, "errors": ["external skill trust record must be an object"]}
    revision = str(record.get("revision", ""))
    if not _SHA40.match(revision):
        errors.append("external skill requires immutable revision pinned to a 40-character commit SHA")
    license_id = str(record.get("license", "")).strip()
    if not license_id or license_id.lower() in {"unknown", "none", "unverified"}:
        errors.append("external skill requires verified license before adoption")
    if not record.get("license_evidence"):
        errors.append("external skill requires license evidence bound to the reviewed snapshot")
    if not record.get("source") or not record.get("skill_path"):
        errors.append("external skill requires source and skill_path provenance")
    content_hash = str(record.get("content_hash", ""))
    if not _SHA256.match(content_hash):
        errors.append("external skill requires sha256 content hash")
    requested = record.get("requested_capabilities", [])
    reviewed = record.get("reviewed_capabilities", [])
    if not isinstance(requested, list) or not isinstance(reviewed, list):
        errors.append("external skill capabilities must be lists")
        requested, reviewed = [], []
    if set(requested) - set(reviewed):
        errors.append("requested capabilities exceed reviewed capabilities")
    broad = [cap for cap in requested if isinstance(cap, str) and (cap.endswith(":*") or cap in {"network", "shell", "filesystem:*"})]
    if broad:
        errors.append(f"unbounded external skill capabilities are forbidden: {broad}")
    executables = record.get("executable_files", [])
    if not isinstance(executables, list):
        errors.append("executable_files must be a list")
    elif executables and not record.get("executable_review"):
        errors.append("executable external skill files require explicit executable_review")
    boundary = str(record.get("instruction_data_boundary", "")).lower()
    if "advisory data" not in boundary or "locally adopted" not in boundary:
        errors.append("instruction/data boundary must state external instructions are advisory data until locally adopted")
    adoption = record.get("adoption_mode")
    if adoption not in _ALLOWED_ADOPTION:
        errors.append(f"external skill requires bounded adoption_mode from {sorted(_ALLOWED_ADOPTION)}")
    if not record.get("reviewer"):
        errors.append("external skill requires reviewer")
    return {"valid": not errors, "errors": errors}


def build_agent_install_plan(agent_id: str, root: Path | str) -> dict[str, Any]:
    root = Path(root)
    adapters = {
        "openai-codex": [".agents/skills/nolane-ui/SKILL.md", "AGENTS.md"],
        "claude-code": [".claude/skills/nolane-ui/SKILL.md", "AGENTS.md"],
        "google-antigravity": [".agents/skills/nolane-ui/SKILL.md", "AGENTS.md"],
        "generic-mcp": ["scripts/nui-mcp-server"],
        "generic-cli": ["scripts/nui-agent-export", "scripts/nui-validate"],
    }
    if agent_id not in adapters:
        raise ValueError(f"unsupported agent adapter: {agent_id}")
    files = [p for p in adapters[agent_id] if (root / p).exists()]
    files = adapters[agent_id] if agent_id in {"openai-codex", "claude-code", "google-antigravity"} else files
    return {
        "agent_id": agent_id,
        "canonical_skill": "skills/using-nolane-ui/SKILL.md",
        "project_files": files,
        "mcp": {"supported": True, "command": "python scripts/nui-mcp-server", "transport": "stdio-or-host-configured"},
        "cli": {"supported": True, "command": f"python scripts/nui-agent-export --agent {agent_id}"},
        "permission_boundary": "host permissions remain authoritative; the adapter never expands shell, network, filesystem, browser, MCP or image capabilities",
        "copy_policy": "bridge files point to canonical NUI contracts; do not duplicate the canonical skill body",
    }
