"""Revision-bound evidence fingerprints for NUI V11 runtime intelligence."""
from __future__ import annotations

import hashlib
import re
from pathlib import Path
from typing import Any

_SHA256 = re.compile(r"^sha256:[0-9a-f]{64}$")


def _text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def sha256_text(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError("sha256_text requires str")
    return "sha256:" + hashlib.sha256(text.encode("utf-8")).hexdigest()


def sha256_file(path: Path | str) -> str:
    target = Path(path)
    digest = hashlib.sha256()
    with target.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return "sha256:" + digest.hexdigest()


def validate_evidence_binding(record: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    if not isinstance(record, dict):
        return {"valid": False, "errors": ["runtime evidence binding must be an object"]}
    if record.get("version") != 11:
        errors.append("runtime evidence binding must declare version 11")
    for field in ("evidence_id", "revision"):
        if not _text(record.get(field)):
            errors.append(f"runtime evidence binding requires {field}")
    digests = record.get("source_digests")
    if not isinstance(digests, dict) or not digests:
        errors.append("runtime evidence binding requires non-empty source_digests")
    else:
        for path, digest in digests.items():
            if not _text(path):
                errors.append("runtime evidence source path must be non-empty")
            if not isinstance(digest, str) or not _SHA256.match(digest):
                errors.append(f"runtime evidence digest for {path!r} must be sha256:<64 hex>")
    artifacts = record.get("artifacts")
    if not isinstance(artifacts, list) or not artifacts:
        errors.append("runtime evidence binding requires non-empty artifacts")
    elif any(not _text(item) for item in artifacts):
        errors.append("runtime evidence artifacts must be non-empty strings")
    return {"valid": not errors, "errors": errors}


def build_evidence_binding(
    *,
    evidence_id: str,
    revision: str,
    source_digests: dict[str, str],
    artifacts: list[str],
) -> dict[str, Any]:
    record = {
        "version": 11,
        "evidence_id": evidence_id,
        "revision": revision,
        "source_digests": dict(sorted(source_digests.items())),
        "artifacts": list(artifacts),
    }
    result = validate_evidence_binding(record)
    if not result["valid"]:
        raise ValueError("invalid runtime evidence binding: " + "; ".join(result["errors"]))
    return record


def assess_evidence_staleness(
    binding: dict[str, Any],
    current_digests: dict[str, str],
) -> dict[str, Any]:
    validation = validate_evidence_binding(binding)
    if not validation["valid"]:
        raise ValueError("invalid runtime evidence binding: " + "; ".join(validation["errors"]))
    if not isinstance(current_digests, dict):
        raise TypeError("current_digests must be a dict")

    changed: list[str] = []
    missing: list[str] = []
    for path, bound_digest in binding["source_digests"].items():
        current = current_digests.get(path)
        if current is None:
            missing.append(path)
        elif current != bound_digest:
            changed.append(path)

    if changed:
        status = "STALE"
    elif missing:
        status = "UNKNOWN"
    else:
        status = "CURRENT"
    return {
        "status": status,
        "evidence_id": binding["evidence_id"],
        "bound_revision": binding["revision"],
        "changed_paths": sorted(changed),
        "missing_paths": sorted(missing),
        "scope_paths": sorted(binding["source_digests"]),
        "unrelated_current_paths": sorted(set(current_digests) - set(binding["source_digests"])),
    }


__all__ = [
    "assess_evidence_staleness",
    "build_evidence_binding",
    "sha256_file",
    "sha256_text",
    "validate_evidence_binding",
]
