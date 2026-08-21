"""Portable NUI agent interoperability and external-skill trust invariants.

NUI keeps one canonical cognition graph and projects it through thin host
surfaces. Host adapters change discovery and invocation only; they never gain
design authority and never expand the host's permissions.
"""
from __future__ import annotations

import re
from pathlib import Path
from typing import Any

_SHA40 = re.compile(r"^[0-9a-f]{40}$", re.I)
_SHA256 = re.compile(r"^sha256:[0-9a-f]{64}$", re.I)
_ALLOWED_ADOPTION = {"mechanism-summary-only", "reference-only", "vendored-reviewed", "local-rewrite"}

SUPPORTED_AGENT_IDS = (
    "openai-codex",
    "claude-code",
    "google-antigravity",
    "gemini-cli",
    "opencode",
    "cursor-compatible",
    "vscode-agent-compatible",
    "generic-mcp",
    "generic-cli",
)

_AGENT_PROJECTIONS: dict[str, dict[str, Any]] = {
    "openai-codex": {
        "surface": "Open Agent Skills bridge + repository policy + optional MCP/CLI",
        "project_files": [".agents/skills/nolane-ui/SKILL.md", "AGENTS.md"],
        "recommended_mode": "project-skill",
        "discovery_note": "Use the repository-local .agents skill bridge, then follow the canonical bootstrap instead of copying 174 skills into Codex instructions.",
    },
    "claude-code": {
        "surface": "Claude project skill bridge + repository policy + optional MCP/CLI",
        "project_files": [".claude/skills/nolane-ui/SKILL.md", "AGENTS.md"],
        "recommended_mode": "project-skill",
        "discovery_note": "Use the repository-local Claude skill bridge; it points to the same canonical NUI bootstrap and graph.",
    },
    "google-antigravity": {
        "surface": "Open Agent Skills compatible workspace bridge + repository policy",
        "project_files": [".agents/skills/nolane-ui/SKILL.md", "AGENTS.md"],
        "recommended_mode": "workspace-skill",
        "discovery_note": "Use the .agents skill bridge when the current Antigravity workspace supports Agent Skills; verify host syntax live because the surface can drift.",
    },
    "gemini-cli": {
        "surface": "repository context + provider-neutral CLI/MCP projection",
        "project_files": ["AGENTS.md", "scripts/nui-agent-export", "scripts/nui-mcp-server"],
        "recommended_mode": "cli-or-mcp",
        "discovery_note": "Keep NUI inside the target repository and connect through the generic CLI/MCP projection; verify the current Gemini CLI project-instruction/MCP syntax before wiring host config.",
    },
    "opencode": {
        "surface": "repository context + provider-neutral CLI/MCP projection",
        "project_files": ["AGENTS.md", "scripts/nui-agent-export", "scripts/nui-mcp-server"],
        "recommended_mode": "cli-or-mcp",
        "discovery_note": "Use the NUI CLI/MCP boundary rather than inventing an OpenCode-specific copy of the skill graph; verify current host configuration live.",
    },
    "cursor-compatible": {
        "surface": "repository instructions + provider-neutral MCP/CLI projection",
        "project_files": ["AGENTS.md", "scripts/nui-agent-export", "scripts/nui-mcp-server"],
        "recommended_mode": "repository-plus-mcp",
        "discovery_note": "Keep the canonical NUI graph in the repository and expose it through the current editor's repository-instruction and/or MCP surface.",
    },
    "vscode-agent-compatible": {
        "surface": "repository instructions + provider-neutral MCP/CLI projection",
        "project_files": ["AGENTS.md", "scripts/nui-agent-export", "scripts/nui-mcp-server"],
        "recommended_mode": "repository-plus-mcp",
        "discovery_note": "Use repository guidance plus the host's current MCP/agent integration; workspace trust and editor permissions remain host-owned.",
    },
    "generic-mcp": {
        "surface": "local Model Context Protocol server",
        "project_files": ["scripts/nui-mcp-server", "skills/using-nolane-ui/SKILL.md"],
        "recommended_mode": "mcp",
        "discovery_note": "Register the local stdio server with any compatible MCP host and let the host own connection approval and permissions.",
    },
    "generic-cli": {
        "surface": "process/CI/shell projection",
        "project_files": ["scripts/nui-agent-export", "scripts/nui-validate", "skills/using-nolane-ui/SKILL.md"],
        "recommended_mode": "cli",
        "discovery_note": "Use the export plan plus the canonical bootstrap from any shell-capable agent or CI harness.",
    },
}


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
    missing = sorted(set(SUPPORTED_AGENT_IDS) - ids)
    extra = sorted(ids - set(SUPPORTED_AGENT_IDS))
    if missing:
        errors.append(f"agent interoperability registry missing supported adapters {missing}")
    if extra:
        errors.append(f"agent interoperability registry declares adapters with no executable projection {extra}")
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
    """Return a thin, executable projection plan for one supported agent host."""
    root = Path(root)
    if agent_id not in _AGENT_PROJECTIONS:
        raise ValueError(f"unsupported agent adapter: {agent_id}; choose one of {', '.join(SUPPORTED_AGENT_IDS)}")

    projection = _AGENT_PROJECTIONS[agent_id]
    declared_files = list(projection["project_files"])
    missing_files = [path for path in declared_files if not (root / path).exists()]
    if missing_files:
        raise ValueError(f"agent adapter {agent_id} references missing repository files: {missing_files}")

    runtime_files = ["scripts/nui-detect", "knowledge/runtime-detector-rules-v11.json"]
    missing_runtime_files = [path for path in runtime_files if not (root / path).exists()]
    if missing_runtime_files:
        raise ValueError(f"agent adapter {agent_id} references missing runtime detection files: {missing_runtime_files}")

    # Local import keeps V8 interoperability validation independent from the
    # V11 runtime package while allowing install plans to expose the new layer.
    from .runtime_v11.hooks import build_hook_capability

    return {
        "agent_id": agent_id,
        "surface": projection["surface"],
        "recommended_mode": projection["recommended_mode"],
        "canonical_skill": "skills/using-nolane-ui/SKILL.md",
        "canonical_graph": "skills/skill-graph.json",
        "project_files": declared_files,
        "bootstrap_instruction": "Read skills/using-nolane-ui/SKILL.md, route through skills/nolane-ui/SKILL.md, and load only the owners triggered by the task profile.",
        "discovery_note": projection["discovery_note"],
        "mcp": {
            "supported": True,
            "command": "python scripts/nui-mcp-server",
            "transport": "stdio-or-host-configured",
            "configuration_boundary": "Use the current host's MCP configuration format; NUI intentionally does not hard-code vendor config syntax that can drift.",
        },
        "cli": {
            "supported": True,
            "command": f"python scripts/nui-agent-export --agent {agent_id}",
            "validate": "python scripts/nui-validate .",
        },
        "runtime_detection": {
            "supported": True,
            "command": "python scripts/nui-detect",
            "project_files": runtime_files,
            "hook_capabilities": build_hook_capability(agent_id),
            "claim_boundary": "evidence-only",
            "configuration_boundary": "Runtime detection uses host-approved file/browser capabilities only; a clean scan never expands NUI completion authority.",
        },
        "permission_boundary": "host permissions remain authoritative; the adapter never expands shell, network, filesystem, browser, MCP or image capabilities",
        "copy_policy": "bridge files point to canonical NUI contracts; do not duplicate the canonical skill body",
    }


__all__ = [
    "SUPPORTED_AGENT_IDS",
    "build_agent_install_plan",
    "validate_agent_interop_registry",
    "validate_external_skill_trust",
]
