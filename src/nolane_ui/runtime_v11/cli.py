"""CLI entry point for the NUI V11 deterministic runtime detector."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Sequence

from .adjudication import adjudicate_findings
from .detector import scan_path
from .registry import load_rule_registry

DEFAULT_ROOT = Path(__file__).resolve().parents[3]


def _load_json_object(path: str | None, label: str) -> dict[str, Any] | None:
    if path is None:
        return None
    target = Path(path)
    try:
        value = json.loads(target.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValueError(f"{label} file does not exist: {target}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"{label} file is invalid JSON: {target}: {exc}") from exc
    if not isinstance(value, dict):
        raise ValueError(f"{label} file must contain a JSON object: {target}")
    return value


def _emit(payload: dict[str, Any]) -> None:
    print(json.dumps(payload, indent=2, ensure_ascii=False, sort_keys=True))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Run NUI V11 deterministic UI runtime/source observations"
    )
    parser.add_argument("target", help="UI source file or directory to scan")
    parser.add_argument("--root", default=str(DEFAULT_ROOT), help="NUI root containing the V11 rule registry")
    parser.add_argument("--tier", choices=("edit", "session", "release"), default="session")
    parser.add_argument("--context", help="Optional JSON task/design context used for contextual adjudication")
    parser.add_argument("--exceptions", help="Optional JSON file with {\"exceptions\": [...]} narrow reviewed exceptions")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(list(argv) if argv is not None else None)
    try:
        root = Path(args.root).resolve()
        registry = load_rule_registry(root)
        context = _load_json_object(args.context, "runtime context")
        exceptions_record = _load_json_object(args.exceptions, "runtime exceptions")
        exceptions: list[dict[str, Any]] | None = None
        if exceptions_record is not None:
            value = exceptions_record.get("exceptions")
            if not isinstance(value, list):
                raise ValueError("runtime exceptions file requires exceptions[]")
            if any(not isinstance(item, dict) for item in value):
                raise ValueError("runtime exceptions entries must be objects")
            exceptions = [dict(item) for item in value]

        scan = scan_path(args.target, registry, tier=args.tier, context=context)
        adjudicated = adjudicate_findings(
            scan["findings"], registry, context=context, exceptions=exceptions
        )
        payload = {
            "valid": True,
            "target": scan["target"],
            "tier": args.tier,
            "registry_version": registry["version"],
            "scanned_files": scan["scanned_files"],
            "finding_count": len(adjudicated["findings"]),
            "unknown_count": len(adjudicated["unknowns"]),
            "accepted_exception_count": len(adjudicated["accepted_exceptions"]),
            "findings": adjudicated["findings"],
            "unknowns": adjudicated["unknowns"],
            "accepted_exceptions": adjudicated["accepted_exceptions"],
            "exception_errors": adjudicated["exception_errors"],
            "claim_boundary": "A clean deterministic scan is evidence only and does not certify NUI VERIFIED/RELEASED state.",
        }
        _emit(payload)
        return 2 if payload["finding_count"] or payload["unknown_count"] else 0
    except (OSError, ValueError) as exc:
        _emit({"valid": False, "error": str(exc)})
        return 1


__all__ = ["DEFAULT_ROOT", "build_parser", "main"]
