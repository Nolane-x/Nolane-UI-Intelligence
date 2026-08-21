"""CLI for read-only NUI V11 runtime diagnostics."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Sequence

from .doctor import diagnose_runtime_state

DEFAULT_ROOT = Path(__file__).resolve().parents[3]


def _load_json(path: str | None, label: str) -> Any:
    if path is None:
        return None
    target = Path(path)
    try:
        return json.loads(target.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValueError(f"{label} file does not exist: {target}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"{label} file is invalid JSON: {target}: {exc}") from exc


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Inspect NUI V11 runtime installation, evidence staleness, and capability gaps")
    parser.add_argument("--root", default=str(DEFAULT_ROOT))
    parser.add_argument("--bindings", help="Optional JSON list or {\"bindings\": [...]} runtime evidence bindings")
    parser.add_argument("--digests", help="Optional JSON object mapping source paths to current sha256 digests")
    parser.add_argument("--require-capability", action="append", default=[])
    parser.add_argument("--available-capability", action="append", default=[])
    parser.add_argument("--commit-count", type=int)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(list(argv) if argv is not None else None)
    try:
        bindings_value = _load_json(args.bindings, "bindings")
        if isinstance(bindings_value, dict):
            bindings_value = bindings_value.get("bindings")
        if bindings_value is None:
            bindings: list[dict[str, Any]] = []
        elif isinstance(bindings_value, list) and all(isinstance(item, dict) for item in bindings_value):
            bindings = [dict(item) for item in bindings_value]
        else:
            raise ValueError("bindings file must contain a list or {\"bindings\": [...]} of objects")

        digests_value = _load_json(args.digests, "digests")
        if digests_value is None:
            digests: dict[str, str] = {}
        elif isinstance(digests_value, dict) and all(isinstance(key, str) and isinstance(value, str) for key, value in digests_value.items()):
            digests = dict(digests_value)
        else:
            raise ValueError("digests file must contain an object mapping source paths to digest strings")

        report = diagnose_runtime_state(
            Path(args.root).resolve(),
            evidence_bindings=bindings,
            current_digests=digests,
            required_capabilities=args.require_capability,
            available_capabilities=args.available_capability,
            commit_count=args.commit_count,
        )
        print(json.dumps(report, indent=2, ensure_ascii=False, sort_keys=True))
        return 0 if report["valid"] else 2
    except (OSError, ValueError) as exc:
        print(json.dumps({"valid": False, "error": str(exc)}, indent=2, ensure_ascii=False, sort_keys=True))
        return 1


__all__ = ["build_parser", "main"]
