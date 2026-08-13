"""Optional MCP exposure for NUI v8.

The module remains importable without the MCP SDK. When installed with the
``mcp`` extra, :func:`run_server` exposes bounded local read/analysis tools.
It deliberately contains no arbitrary shell executor, remote URL fetcher, or
third-party skill installer; those permissions belong to the host agent.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .interop import build_agent_install_plan
from .validators import validate_repository


def _load(root: Path, relative: str) -> Any:
    return json.loads((root / relative).read_text(encoding="utf-8"))


def get_status(root: Path | str) -> dict[str, Any]:
    root = Path(root).resolve()
    result = validate_repository(root)
    return {"name":"Nolane UI Intelligence","version":_load(root,"nui.config.json").get("version"),"valid":result.get("valid",False),"metrics":result.get("metrics",{}),"errors":result.get("errors",[])[:20],"root":str(root)}


def get_media_sources(root: Path | str) -> dict[str, Any]:
    root = Path(root).resolve(); data=_load(root,"knowledge/visual-media-sources-v8.json")
    return {"version":data.get("version"),"principle":data.get("principle"),"sources":data.get("sources",[])}


def get_creative_tools(root: Path | str) -> dict[str, Any]:
    root = Path(root).resolve(); data=_load(root,"knowledge/creative-toolchain-v8.json")
    return {"version":data.get("version"),"principle":data.get("principle"),"tools":data.get("tools",[])}


def get_skill(root: Path | str, skill_name: str) -> dict[str, Any]:
    root=Path(root).resolve(); graph=_load(root,"skills/skill-graph.json").get("skills",{})
    if skill_name not in graph: raise ValueError(f"unknown canonical NUI skill: {skill_name}")
    path=(root/"skills"/skill_name/"SKILL.md").resolve(); skill_root=(root/"skills").resolve()
    if skill_root not in path.parents: raise ValueError("skill path escaped canonical skill root")
    return {"name":skill_name,"metadata":graph[skill_name],"content":path.read_text(encoding="utf-8")}


def tool_catalog(root: Path | str) -> list[dict[str,str]]:
    _=Path(root)
    return [
        {"name":"nui_status","description":"Validate the local NUI repository and return bounded structural metrics."},
        {"name":"nui_install_plan","description":"Return a permission-preserving adapter plan for a supported agent harness."},
        {"name":"nui_get_skill","description":"Read one canonical NUI skill by exact graph name."},
        {"name":"nui_media_sources","description":"List rights-aware visual-media discovery sources and their caveats."},
        {"name":"nui_creative_tools","description":"List creative production tools by stage authority and policy boundary."},
    ]


def run_server(root: Path | str | None=None) -> None:
    root_path=Path(root).resolve() if root else Path(__file__).resolve().parents[2]
    try:
        from mcp.server.fastmcp import FastMCP  # type: ignore
    except ImportError as exc:
        raise RuntimeError("MCP SDK is optional. Install NUI with the 'mcp' extra: pip install -e '.[mcp]'") from exc
    mcp=FastMCP("nolane-ui-intelligence")
    @mcp.tool()
    def nui_status() -> dict[str,Any]: return get_status(root_path)
    @mcp.tool()
    def nui_install_plan(agent_id: str) -> dict[str,Any]: return build_agent_install_plan(agent_id,root_path)
    @mcp.tool()
    def nui_get_skill(skill_name: str) -> dict[str,Any]: return get_skill(root_path,skill_name)
    @mcp.tool()
    def nui_media_sources() -> dict[str,Any]: return get_media_sources(root_path)
    @mcp.tool()
    def nui_creative_tools() -> dict[str,Any]: return get_creative_tools(root_path)
    mcp.run()
