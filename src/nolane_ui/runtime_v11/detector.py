"""Dependency-free source observation engine for NUI V11.

This module deliberately reports the engine and source evidence it actually used.
It never upgrades text heuristics into AST/browser certainty.
"""
from __future__ import annotations

import hashlib
import re
from pathlib import Path
from typing import Any, Iterable

from .contracts import NUI_FINDING_REQUIRED_FIELDS, SCANNABLE_SUFFIXES
from .registry import validate_rule_registry

_TIER_RANK = {"edit": 0, "session": 1, "release": 2}
_TAG_IMG = re.compile(r"<img\b[^>]*>", re.IGNORECASE | re.DOTALL)
_EMPTY_LINK = re.compile(r"<a\b[^>]*\bhref\s*=\s*([\"'])\s*\1[^>]*>", re.IGNORECASE | re.DOTALL)
_OPACITY_ZERO = re.compile(r"\bopacity\s*:\s*0(?:\s*!important)?\s*[;,}]?", re.IGNORECASE)
_OUTLINE_NONE = re.compile(r"\boutline\s*:\s*(?:none|0(?:px)?)\b", re.IGNORECASE)
_MIN_WIDTH = re.compile(r"\b(?:min-width|minWidth)\s*[:=]\s*['\"]?(\d{3,4})px", re.IGNORECASE)
_HARDCODED_COLOR = re.compile(r"(?<![\w-])#[0-9a-fA-F]{3,8}\b")
_CARD_OPEN = re.compile(
    r"<[^>]+\b(?:class|className)\s*=\s*([\"'])[^\"']*\bcard\b[^\"']*\1[^>]*>",
    re.IGNORECASE,
)
_BACKGROUND_CLIP_TEXT = re.compile(r"(?:-webkit-)?background-clip\s*:\s*text\b", re.IGNORECASE)
_LINEAR_GRADIENT = re.compile(r"linear-gradient\s*\(", re.IGNORECASE)
_CLIP_BLOCK = re.compile(r"\{([^{}]{0,500})\}", re.DOTALL)
_HEIGHT_DECL = re.compile(r"\b(?:height|max-height|maxHeight)\s*[:=]\s*['\"]?[^;,}\n]+", re.IGNORECASE)
_OVERFLOW_HIDDEN = re.compile(r"\boverflow(?:-[xy])?\s*:\s*hidden\b", re.IGNORECASE)

_DOMAIN_IMPACT = {
    "runtime-integrity": "The shipped interface can expose broken, misleading, or unreachable behavior to users.",
    "accessibility-mechanics": "Users relying on non-visual or keyboard interaction may lose information or operability.",
    "layout-integrity": "Content can become clipped, horizontally unreachable, or fragile across supported viewports and content states.",
    "design-system-integrity": "Local implementation can drift from the declared system and make later changes inconsistent or expensive.",
    "genericness": "The result may converge on reusable template habits instead of expressing product-specific hierarchy and intent.",
}

_DOMAIN_REPAIR = {
    "runtime-integrity": "Repair the concrete runtime/source defect and re-observe the affected surface.",
    "accessibility-mechanics": "Route to the existing accessibility/input owner, preserve semantics, and verify the repaired interaction in the relevant modality.",
    "layout-integrity": "Route to the existing layout/responsive owner, remove the brittle constraint or justify it, then verify representative viewports and content states.",
    "design-system-integrity": "Resolve the value against the active token/design authority or record a narrow evidence-backed exception.",
    "genericness": "Send this signal to comparative critique; keep it only when product structure or the committed visual thesis earns the pattern.",
}


def _line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, max(offset, 0)) + 1


def _line_snippet(text: str, offset: int, limit: int = 180) -> str:
    start = text.rfind("\n", 0, max(offset, 0)) + 1
    end = text.find("\n", max(offset, 0))
    if end < 0:
        end = len(text)
    return " ".join(text[start:end].strip().split())[:limit]


def _token_color_owned(context: dict[str, Any] | None) -> bool:
    if not isinstance(context, dict):
        return False
    design_system = context.get("design_system")
    if not isinstance(design_system, dict):
        return False
    axes = design_system.get("token_owned_axes", [])
    return isinstance(axes, list) and "color" in {str(axis).strip().lower() for axis in axes}


def _img_matches(text: str) -> Iterable[tuple[str, int, str]]:
    for match in _TAG_IMG.finditer(text):
        tag = match.group(0)
        src = re.search(r"\bsrc\s*=\s*([\"'])(.*?)\1", tag, re.IGNORECASE | re.DOTALL)
        if src is None or src.group(2).strip().lower() in {"", "placeholder", "about:blank"}:
            yield "runtime.integrity.broken-image-src", match.start(), "markup"
        if re.search(r"\balt\s*=", tag, re.IGNORECASE) is None:
            yield "runtime.accessibility.image-alt-omission", match.start(), "markup"


def _simple_matches(text: str, context: dict[str, Any] | None) -> Iterable[tuple[str, int, str]]:
    for match in _EMPTY_LINK.finditer(text):
        yield "runtime.integrity.empty-navigation-target", match.start(), "markup"
    for match in _OPACITY_ZERO.finditer(text):
        yield "runtime.integrity.hidden-content-default", match.start(), "css"
    for match in _OUTLINE_NONE.finditer(text):
        yield "runtime.accessibility.focus-visibility-suppressed", match.start(), "css"
    for match in _MIN_WIDTH.finditer(text):
        if int(match.group(1)) >= 640:
            yield "runtime.layout.viewport-minimum-width", match.start(), "css"
    if _token_color_owned(context):
        for match in _HARDCODED_COLOR.finditer(text):
            yield "runtime.design-system.hard-coded-color", match.start(), "text"


def _clipping_matches(text: str) -> Iterable[tuple[str, int, str]]:
    for block in _CLIP_BLOCK.finditer(text):
        body = block.group(1)
        if _HEIGHT_DECL.search(body) and _OVERFLOW_HIDDEN.search(body):
            overflow = _OVERFLOW_HIDDEN.search(body)
            assert overflow is not None
            yield "runtime.layout.content-clipping-risk", block.start(1) + overflow.start(), "css"


def _nested_card_matches(text: str) -> Iterable[tuple[str, int, str]]:
    opens = list(_CARD_OPEN.finditer(text))
    for outer_index, outer in enumerate(opens[:-1]):
        for inner in opens[outer_index + 1:]:
            if 0 < inner.start() - outer.end() <= 1600:
                yield "runtime.genericness.repeated-nested-card-shell", inner.start(), "text"
                return


def _gradient_text_matches(text: str) -> Iterable[tuple[str, int, str]]:
    if _LINEAR_GRADIENT.search(text):
        clip = _BACKGROUND_CLIP_TEXT.search(text)
        if clip:
            yield "runtime.genericness.decorative-gradient-text", clip.start(), "css"


def _raw_matches(text: str, context: dict[str, Any] | None) -> list[tuple[str, int, str]]:
    matches: list[tuple[str, int, str]] = []
    matches.extend(_img_matches(text))
    matches.extend(_simple_matches(text, context))
    matches.extend(_clipping_matches(text))
    matches.extend(_nested_card_matches(text))
    matches.extend(_gradient_text_matches(text))
    return matches


def _make_finding(rule: dict[str, Any], path: str, text: str, offset: int, engine: str) -> dict[str, Any]:
    line = _line_number(text, offset)
    snippet = _line_snippet(text, offset)
    rule_id = str(rule["rule_id"])
    digest = hashlib.sha256(f"{path}\n{line}\n{rule_id}\n{snippet}".encode("utf-8")).hexdigest()
    owner_hints = [str(owner) for owner in rule.get("owner_hints", [])]
    owner_suffix = f" Suggested existing owner(s): {', '.join(owner_hints)}." if owner_hints else ""
    domain = str(rule["domain"])
    finding = {
        "finding_id": f"{rule_id}:{digest[:16]}",
        "domain": domain,
        "severity": str(rule["severity"]),
        "evidence": [f"{path}:{line}: {snippet}"],
        "violated_constraint": str(rule["description"]),
        "user_impact": _DOMAIN_IMPACT.get(domain, "The observed condition can undermine the active UI contract."),
        "falsifier": str(rule["falsifier"]),
        "recommended_repair": _DOMAIN_REPAIR.get(domain, "Route the finding to the existing NUI owner and re-observe after repair.") + owner_suffix,
        "status": "open",
        "runtime": {
            "rule_id": rule_id,
            "rule_class": str(rule["class"]),
            "declared_tier": str(rule["tier"]),
            "engine": engine,
            "path": path,
            "line": line,
            "snippet": snippet,
            "observation_digest": f"sha256:{digest}",
        },
    }
    # Keep this assertion close to construction so future finding-schema changes
    # fail in the runtime package rather than leaking malformed evidence.
    missing = [field for field in NUI_FINDING_REQUIRED_FIELDS if field not in finding]
    if missing:
        raise AssertionError(f"runtime finding construction omitted fields: {missing}")
    return finding


def scan_text(
    text: str,
    path: str,
    registry: dict[str, Any],
    *,
    tier: str = "session",
    context: dict[str, Any] | None = None,
) -> list[dict[str, Any]]:
    """Scan one source text and return deterministic NUI-compatible findings."""
    if tier not in _TIER_RANK:
        raise ValueError(f"invalid runtime detector tier: {tier}")
    validation = validate_rule_registry(registry)
    if not validation["valid"]:
        raise ValueError("invalid runtime rule registry: " + "; ".join(validation["errors"]))
    rules = {str(rule["rule_id"]): rule for rule in registry["rules"]}
    max_rank = _TIER_RANK[tier]
    dedup: dict[tuple[str, int], dict[str, Any]] = {}
    for rule_id, offset, engine in _raw_matches(text, context):
        rule = rules.get(rule_id)
        if rule is None:
            continue
        if _TIER_RANK[str(rule["tier"])] > max_rank:
            continue
        line = _line_number(text, offset)
        key = (rule_id, line)
        dedup.setdefault(key, _make_finding(rule, path, text, offset, engine))
    return sorted(dedup.values(), key=lambda item: (item["runtime"]["line"], item["runtime"]["rule_id"]))


def scan_path(
    target: Path | str,
    registry: dict[str, Any],
    *,
    tier: str = "session",
    context: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Scan one file or a bounded directory tree with stable path ordering."""
    target_path = Path(target)
    if not target_path.exists():
        raise ValueError(f"runtime detector target does not exist: {target_path}")
    if target_path.is_file():
        files = [target_path]
    else:
        files = sorted(
            path for path in target_path.rglob("*")
            if path.is_file() and path.suffix.lower() in SCANNABLE_SUFFIXES
            and not any(part in {".git", "node_modules", "dist", "build", ".next", "coverage"} for part in path.parts)
        )
    findings: list[dict[str, Any]] = []
    scanned: list[str] = []
    for path in files:
        if path.suffix.lower() not in SCANNABLE_SUFFIXES:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        display = path.as_posix()
        scanned.append(display)
        findings.extend(scan_text(text, display, registry, tier=tier, context=context))
    findings.sort(key=lambda item: (item["runtime"]["path"], item["runtime"]["line"], item["runtime"]["rule_id"]))
    return {"target": target_path.as_posix(), "tier": tier, "scanned_files": scanned, "findings": findings}


__all__ = ["scan_path", "scan_text"]
