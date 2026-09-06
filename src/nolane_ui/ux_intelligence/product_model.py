"""Evidence-bounded product model contracts for UX Intelligence v3.

This module may normalize explicit discovery evidence, including raw V11 browser
packets, but it never invents user goals, actions, objects, recovery semantics,
or success criteria from browser structure alone.
"""
from __future__ import annotations

from copy import deepcopy
import math
from typing import Any, Iterable

from .provenance import UX_PROVENANCE


MODEL_STATUSES = {"experimental", "active", "deprecated"}
SURFACE_KINDS = {"route", "dialog", "panel", "sheet", "workspace", "native-screen"}
ORIGINS = {"declared", "observed", "inferred"}
COMMITMENT_LEVELS = {"none", "reversible", "state-changing", "destructive", "external-effect"}
RELATIONSHIP_KINDS = {
    "contains",
    "acts-on",
    "navigates-to",
    "transitions-to",
    "preserves",
    "requires",
    "recovers-via",
    "succeeds-with",
}

_REQUIRED_MODEL_FIELDS = (
    "product_id",
    "revision",
    "surfaces",
    "objects",
    "actions",
    "states",
    "relationships",
    "evidence_refs",
    "provenance_ids",
    "status",
)
_REQUIRED_PACKET_FIELDS = (
    "product_id",
    "revision",
    "captures",
    "declared_goals",
    "declared_success_signals",
    "declared_object_hints",
    "provenance_ids",
)
_EVIDENCE_GROUPS = (
    "action_evidence",
    "transition_evidence",
    "object_evidence",
    "state_evidence",
    "success_evidence",
)


def _text(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label} must be a non-empty string")
    return value.strip()


def _mapping(value: Any, label: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise TypeError(f"{label} must be an object")
    return value


def _sequence(value: Any, label: str, *, allow_empty: bool = True) -> tuple[Any, ...]:
    if not isinstance(value, (list, tuple)):
        raise TypeError(f"{label} must be a sequence")
    if not allow_empty and not value:
        raise ValueError(f"{label} must not be empty")
    return tuple(value)


def _strings(value: Any, label: str, *, allow_empty: bool = True) -> tuple[str, ...]:
    values = _sequence(value, label, allow_empty=allow_empty)
    out = []
    for index, item in enumerate(values):
        out.append(_text(item, f"{label}[{index}]"))
    return tuple(out)


def _dedupe_strings(value: Any, label: str, *, allow_empty: bool = True) -> tuple[str, ...]:
    return tuple(sorted(set(_strings(value, label, allow_empty=allow_empty))))


def _confidence(value: Any, label: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(f"{label} must be numeric")
    result = float(value)
    if not math.isfinite(result) or not 0.0 <= result <= 1.0:
        raise ValueError(f"{label} must be finite and within [0, 1]")
    return result


def _known_provenance(provenance_catalog: Iterable[dict[str, Any]]) -> set[str]:
    return {str(record["provenance_id"]) for record in provenance_catalog}


def _validate_provenance_ids(
    values: Any,
    label: str,
    provenance_catalog: Iterable[dict[str, Any]],
) -> tuple[str, ...]:
    ids = _dedupe_strings(values, label)
    unknown = set(ids) - _known_provenance(provenance_catalog)
    if unknown:
        raise ValueError(f"{label} contains unknown provenance ids: {sorted(unknown)}")
    return ids


def _validate_origin_record(
    record: dict[str, Any],
    label: str,
    *,
    allow_declared_without_evidence: bool = True,
) -> None:
    origin = record.get("origin")
    if origin not in ORIGINS:
        raise ValueError(f"{label}.origin must be one of {sorted(ORIGINS)}")
    _confidence(record.get("confidence"), f"{label}.confidence")
    evidence = _strings(record.get("evidence_refs"), f"{label}.evidence_refs")
    if origin in {"observed", "inferred"} and not evidence:
        raise ValueError(f"{label}: {origin} record requires evidence_refs")
    if origin == "declared" and not allow_declared_without_evidence and not evidence:
        raise ValueError(f"{label}: declared record requires evidence_refs")


def _normalize_optional_v11(capture: dict[str, Any]) -> None:
    packet = capture.get("runtime_v11")
    if packet is None:
        return
    from ..runtime_v11.browser import normalize_browser_observation

    capture["runtime_v11"] = normalize_browser_observation(packet)


def validate_ux_discovery_packet(
    packet: dict[str, Any],
    *,
    provenance_catalog: Iterable[dict[str, Any]] = UX_PROVENANCE,
) -> dict[str, Any]:
    if not isinstance(packet, dict):
        raise TypeError("UX discovery packet must be an object")
    missing = [field for field in _REQUIRED_PACKET_FIELDS if field not in packet]
    if missing:
        raise ValueError(f"UX discovery packet missing required fields: {missing}")

    product_id = _text(packet.get("product_id"), "product_id")
    _text(packet.get("revision"), "revision")
    _validate_provenance_ids(packet.get("provenance_ids"), "provenance_ids", provenance_catalog)
    for field in ("declared_goals", "declared_success_signals", "declared_object_hints"):
        _sequence(packet.get(field), field)

    captures = _sequence(packet.get("captures"), "captures")
    seen: set[str] = set()
    for index, raw in enumerate(captures):
        capture = _mapping(raw, f"captures[{index}]")
        capture_id = _text(capture.get("capture_id"), f"captures[{index}].capture_id")
        if capture_id in seen:
            raise ValueError(f"duplicate capture_id {capture_id}")
        seen.add(capture_id)
        _text(capture.get("surface_id"), f"captures[{index}].surface_id")
        _strings(capture.get("evidence_refs"), f"captures[{index}].evidence_refs", allow_empty=False)
        for field in _EVIDENCE_GROUPS:
            values = _sequence(capture.get(field), f"captures[{index}].{field}")
            for item_index, item in enumerate(values):
                record = _mapping(item, f"captures[{index}].{field}[{item_index}]")
                _strings(
                    record.get("evidence_refs"),
                    f"captures[{index}].{field}[{item_index}].evidence_refs",
                    allow_empty=False,
                )
        if "runtime_v11" in capture and not isinstance(capture["runtime_v11"], dict):
            raise TypeError(f"captures[{index}].runtime_v11 must be an object")

    return {"valid": True, "product_id": product_id, "capture_count": len(captures), "errors": []}


def normalize_ux_discovery_packet(
    packet: dict[str, Any],
    *,
    provenance_catalog: Iterable[dict[str, Any]] = UX_PROVENANCE,
) -> dict[str, Any]:
    validate_ux_discovery_packet(packet, provenance_catalog=provenance_catalog)
    out = deepcopy(packet)
    out["provenance_ids"] = _dedupe_strings(out["provenance_ids"], "provenance_ids")
    for field in ("declared_goals", "declared_success_signals", "declared_object_hints"):
        out[field] = tuple(deepcopy(item) for item in out[field])

    captures = []
    for capture in out["captures"]:
        item = deepcopy(capture)
        item["evidence_refs"] = _dedupe_strings(item["evidence_refs"], f"{item['capture_id']}.evidence_refs")
        for field in _EVIDENCE_GROUPS:
            normalized_group = []
            for record in item[field]:
                normalized_record = deepcopy(record)
                normalized_record["evidence_refs"] = _dedupe_strings(
                    normalized_record["evidence_refs"],
                    f"{item['capture_id']}.{field}.evidence_refs",
                    allow_empty=False,
                )
                normalized_group.append(normalized_record)
            item[field] = tuple(normalized_group)
        if "surface_labels" in item:
            item["surface_labels"] = _dedupe_strings(item["surface_labels"], f"{item['capture_id']}.surface_labels")
        _normalize_optional_v11(item)
        captures.append(item)
    out["captures"] = tuple(sorted(captures, key=lambda item: item["capture_id"]))
    return out


def _require_fields(record: dict[str, Any], fields: tuple[str, ...], label: str) -> None:
    missing = [field for field in fields if field not in record]
    if missing:
        raise ValueError(f"{label} missing required fields: {missing}")


def _validate_sorted_unique(records: Any, id_field: str, label: str) -> tuple[dict[str, Any], ...]:
    values = _sequence(records, label)
    ids = []
    out = []
    for index, raw in enumerate(values):
        record = _mapping(raw, f"{label}[{index}]")
        record_id = _text(record.get(id_field), f"{label}[{index}].{id_field}")
        ids.append(record_id)
        out.append(record)
    if len(ids) != len(set(ids)):
        raise ValueError(f"{label} contains duplicate {id_field}")
    if ids != sorted(ids):
        raise ValueError(f"{label} must be sorted by {id_field}")
    return tuple(out)


def validate_ux_product_model(
    model: dict[str, Any],
    *,
    provenance_catalog: Iterable[dict[str, Any]] = UX_PROVENANCE,
) -> dict[str, Any]:
    if not isinstance(model, dict):
        raise TypeError("UX product model must be an object")
    missing = [field for field in _REQUIRED_MODEL_FIELDS if field not in model]
    if missing:
        raise ValueError(f"UX product model missing required fields: {missing}")
    product_id = _text(model.get("product_id"), "product_id")
    _text(model.get("revision"), "revision")
    if model.get("status") not in MODEL_STATUSES:
        raise ValueError(f"unknown product model status {model.get('status')!r}")
    _strings(model.get("evidence_refs"), "evidence_refs")
    _validate_provenance_ids(model.get("provenance_ids"), "provenance_ids", provenance_catalog)

    surfaces = _validate_sorted_unique(model.get("surfaces"), "surface_id", "surfaces")
    objects = _validate_sorted_unique(model.get("objects"), "object_id", "objects")
    actions = _validate_sorted_unique(model.get("actions"), "action_id", "actions")
    states = _validate_sorted_unique(model.get("states"), "state_id", "states")
    relationships = _validate_sorted_unique(model.get("relationships"), "relationship_id", "relationships")
    outcomes = _validate_sorted_unique(model.get("outcomes", ()), "outcome_id", "outcomes")

    surface_ids = {record["surface_id"] for record in surfaces}
    object_ids = {record["object_id"] for record in objects}
    action_ids = {record["action_id"] for record in actions}
    state_ids = {record["state_id"] for record in states}
    outcome_ids = {record["outcome_id"] for record in outcomes}
    all_ids = surface_ids | object_ids | action_ids | state_ids | outcome_ids

    for record in surfaces:
        sid = record["surface_id"]
        _require_fields(
            record,
            ("kind", "locator", "labels", "available_action_ids", "visible_object_ids", "origin", "confidence", "evidence_refs"),
            f"surface {sid}",
        )
        if record["kind"] not in SURFACE_KINDS:
            raise ValueError(f"surface {sid}: unknown kind {record['kind']!r}")
        _text(record["locator"], f"surface {sid}.locator")
        _strings(record["labels"], f"surface {sid}.labels")
        available = _strings(record["available_action_ids"], f"surface {sid}.available_action_ids")
        visible = _strings(record["visible_object_ids"], f"surface {sid}.visible_object_ids")
        if set(available) - action_ids:
            raise ValueError(f"surface {sid}: unresolved action ids {sorted(set(available) - action_ids)}")
        if set(visible) - object_ids:
            raise ValueError(f"surface {sid}: unresolved object ids {sorted(set(visible) - object_ids)}")
        _validate_origin_record(record, f"surface {sid}")

    for record in objects:
        oid = record["object_id"]
        _require_fields(record, ("object_type", "labels", "identity_fields", "state_ids", "origin", "confidence", "evidence_refs"), f"object {oid}")
        _text(record["object_type"], f"object {oid}.object_type")
        _strings(record["labels"], f"object {oid}.labels")
        _strings(record["identity_fields"], f"object {oid}.identity_fields", allow_empty=False)
        object_states = _strings(record["state_ids"], f"object {oid}.state_ids")
        if set(object_states) - state_ids:
            raise ValueError(f"object {oid}: unresolved state ids {sorted(set(object_states) - state_ids)}")
        _validate_origin_record(record, f"object {oid}")

    for record in actions:
        aid = record["action_id"]
        _require_fields(
            record,
            ("label", "action_kind", "source_surface_id", "object_id", "observed_target_surface_ids", "observed_state_changes", "commitment_level", "origin", "confidence", "evidence_refs"),
            f"action {aid}",
        )
        _text(record["label"], f"action {aid}.label")
        _text(record["action_kind"], f"action {aid}.action_kind")
        if record["source_surface_id"] not in surface_ids:
            raise ValueError(f"action {aid}: unresolved source surface {record['source_surface_id']!r}")
        if record["object_id"] not in object_ids:
            raise ValueError(f"action {aid}: unresolved object {record['object_id']!r}")
        targets = _strings(record["observed_target_surface_ids"], f"action {aid}.observed_target_surface_ids")
        if set(targets) - surface_ids:
            raise ValueError(f"action {aid}: unresolved target surfaces {sorted(set(targets) - surface_ids)}")
        _mapping(record["observed_state_changes"], f"action {aid}.observed_state_changes")
        if record["commitment_level"] not in COMMITMENT_LEVELS:
            raise ValueError(f"action {aid}: unknown commitment level {record['commitment_level']!r}")
        _validate_origin_record(record, f"action {aid}")

    for record in states:
        sid = record["state_id"]
        _require_fields(record, ("object_id", "attributes", "origin", "confidence", "evidence_refs"), f"state {sid}")
        if record["object_id"] not in object_ids:
            raise ValueError(f"state {sid}: unresolved object {record['object_id']!r}")
        _mapping(record["attributes"], f"state {sid}.attributes")
        _validate_origin_record(record, f"state {sid}")

    for record in outcomes:
        oid = record["outcome_id"]
        _require_fields(record, ("label", "surface_id", "origin", "confidence", "evidence_refs"), f"outcome {oid}")
        _text(record["label"], f"outcome {oid}.label")
        if record["surface_id"] not in surface_ids:
            raise ValueError(f"outcome {oid}: unresolved surface {record['surface_id']!r}")
        _validate_origin_record(record, f"outcome {oid}")

    for record in relationships:
        rid = record["relationship_id"]
        _require_fields(record, ("source_id", "relation", "target_id", "origin", "confidence", "evidence_refs"), f"relationship {rid}")
        if record["relation"] not in RELATIONSHIP_KINDS:
            raise ValueError(f"relationship {rid}: unknown relation {record['relation']!r}")
        if record["source_id"] not in all_ids:
            raise ValueError(f"relationship {rid}: unresolved source {record['source_id']!r}")
        if record["target_id"] not in all_ids:
            raise ValueError(f"relationship {rid}: unresolved target {record['target_id']!r}")
        _validate_origin_record(record, f"relationship {rid}")

    return {
        "valid": True,
        "product_id": product_id,
        "surface_count": len(surfaces),
        "object_count": len(objects),
        "action_count": len(actions),
        "state_count": len(states),
        "relationship_count": len(relationships),
        "outcome_count": len(outcomes),
        "errors": [],
    }


def normalize_ux_product_model(
    model: dict[str, Any],
    *,
    provenance_catalog: Iterable[dict[str, Any]] = UX_PROVENANCE,
) -> dict[str, Any]:
    validate_ux_product_model(model, provenance_catalog=provenance_catalog)
    out = deepcopy(model)
    out["evidence_refs"] = _dedupe_strings(out["evidence_refs"], "evidence_refs")
    out["provenance_ids"] = _dedupe_strings(out["provenance_ids"], "provenance_ids")
    specs = (
        ("surfaces", "surface_id", ("labels", "available_action_ids", "visible_object_ids")),
        ("objects", "object_id", ("labels", "identity_fields", "state_ids")),
        ("actions", "action_id", ("observed_target_surface_ids",)),
        ("states", "state_id", ()),
        ("relationships", "relationship_id", ()),
        ("outcomes", "outcome_id", ()),
    )
    for field, id_field, tuple_fields in specs:
        if field not in out:
            if field == "outcomes":
                out[field] = ()
            continue
        normalized = []
        for record in out[field]:
            item = deepcopy(record)
            item["evidence_refs"] = _dedupe_strings(item["evidence_refs"], f"{field}.{item[id_field]}.evidence_refs")
            for tuple_field in tuple_fields:
                item[tuple_field] = _dedupe_strings(item[tuple_field], f"{field}.{item[id_field]}.{tuple_field}")
            normalized.append(item)
        out[field] = tuple(sorted(normalized, key=lambda item: item[id_field]))
    return out


def _merge_record(
    store: dict[str, dict[str, Any]],
    key: str,
    record: dict[str, Any],
    *,
    union_fields: tuple[str, ...] = (),
) -> None:
    existing = store.get(key)
    if existing is None:
        store[key] = deepcopy(record)
        return
    for field, value in record.items():
        if field == "evidence_refs":
            existing[field] = tuple(sorted(set(existing[field]) | set(value)))
        elif field in union_fields:
            existing[field] = tuple(sorted(set(existing[field]) | set(value)))
        elif existing.get(field) != value:
            raise ValueError(f"conflicting semantic records for {key}: field {field}")


def build_ux_product_model(
    packet: dict[str, Any],
    *,
    provenance_catalog: Iterable[dict[str, Any]] = UX_PROVENANCE,
) -> dict[str, Any]:
    normalized = normalize_ux_discovery_packet(packet, provenance_catalog=provenance_catalog)
    surfaces: dict[str, dict[str, Any]] = {}
    objects: dict[str, dict[str, Any]] = {}
    actions: dict[str, dict[str, Any]] = {}
    states: dict[str, dict[str, Any]] = {}
    relationships: dict[str, dict[str, Any]] = {}
    outcomes: dict[str, dict[str, Any]] = {}
    all_evidence: set[str] = set()

    for capture in normalized["captures"]:
        surface_id = _text(capture["surface_id"], f"{capture['capture_id']}.surface_id")
        if "surface_kind" not in capture or "surface_locator" not in capture:
            raise ValueError(f"{capture['capture_id']}: model construction requires explicit surface_kind and surface_locator")
        surface_kind = capture["surface_kind"]
        if surface_kind not in SURFACE_KINDS:
            raise ValueError(f"{capture['capture_id']}: unknown surface_kind {surface_kind!r}")
        capture_refs = _dedupe_strings(capture["evidence_refs"], f"{capture['capture_id']}.evidence_refs", allow_empty=False)
        all_evidence.update(capture_refs)
        surface = {
            "surface_id": surface_id,
            "kind": surface_kind,
            "locator": _text(capture["surface_locator"], f"{capture['capture_id']}.surface_locator"),
            "labels": _dedupe_strings(capture.get("surface_labels", ()), f"{capture['capture_id']}.surface_labels"),
            "available_action_ids": tuple(sorted(record["action_id"] for record in capture["action_evidence"])),
            "visible_object_ids": tuple(sorted(record["object_id"] for record in capture["object_evidence"])),
            "origin": "observed",
            "confidence": 1.0,
            "evidence_refs": capture_refs,
        }
        _merge_record(surfaces, surface_id, surface, union_fields=("labels", "available_action_ids", "visible_object_ids"))

        for raw in capture["object_evidence"]:
            object_id = _text(raw.get("object_id"), f"{capture['capture_id']}.object_evidence.object_id")
            record = {
                "object_id": object_id,
                "object_type": _text(raw.get("object_type"), f"object {object_id}.object_type"),
                "labels": _dedupe_strings(raw.get("labels", ()), f"object {object_id}.labels"),
                "identity_fields": _dedupe_strings(raw.get("identity_fields"), f"object {object_id}.identity_fields", allow_empty=False),
                "state_ids": _dedupe_strings(raw.get("state_ids", ()), f"object {object_id}.state_ids"),
                "origin": "observed",
                "confidence": 1.0,
                "evidence_refs": _dedupe_strings(raw["evidence_refs"], f"object {object_id}.evidence_refs", allow_empty=False),
            }
            all_evidence.update(record["evidence_refs"])
            _merge_record(objects, object_id, record, union_fields=("labels", "identity_fields", "state_ids"))

        for raw in capture["action_evidence"]:
            action_id = _text(raw.get("action_id"), f"{capture['capture_id']}.action_evidence.action_id")
            record = {
                "action_id": action_id,
                "label": _text(raw.get("label"), f"action {action_id}.label"),
                "action_kind": _text(raw.get("action_kind"), f"action {action_id}.action_kind"),
                "source_surface_id": surface_id,
                "object_id": _text(raw.get("object_id"), f"action {action_id}.object_id"),
                "observed_target_surface_ids": _dedupe_strings(raw.get("target_surface_ids", ()), f"action {action_id}.target_surface_ids"),
                "observed_state_changes": deepcopy(_mapping(raw.get("state_changes", {}), f"action {action_id}.state_changes")),
                "commitment_level": raw.get("commitment_level"),
                "origin": "observed",
                "confidence": 1.0,
                "evidence_refs": _dedupe_strings(raw["evidence_refs"], f"action {action_id}.evidence_refs", allow_empty=False),
            }
            if record["commitment_level"] not in COMMITMENT_LEVELS:
                raise ValueError(f"action {action_id}: unknown commitment level {record['commitment_level']!r}")
            all_evidence.update(record["evidence_refs"])
            _merge_record(actions, action_id, record, union_fields=("observed_target_surface_ids",))

        for raw in capture["state_evidence"]:
            state_id = _text(raw.get("state_id"), f"{capture['capture_id']}.state_evidence.state_id")
            record = {
                "state_id": state_id,
                "object_id": _text(raw.get("object_id"), f"state {state_id}.object_id"),
                "attributes": deepcopy(_mapping(raw.get("attributes"), f"state {state_id}.attributes")),
                "origin": "observed",
                "confidence": 1.0,
                "evidence_refs": _dedupe_strings(raw["evidence_refs"], f"state {state_id}.evidence_refs", allow_empty=False),
            }
            all_evidence.update(record["evidence_refs"])
            _merge_record(states, state_id, record)

        for raw in capture["transition_evidence"]:
            relationship_id = _text(raw.get("transition_id"), f"{capture['capture_id']}.transition_evidence.transition_id")
            record = {
                "relationship_id": relationship_id,
                "source_id": _text(raw.get("source_id"), f"relationship {relationship_id}.source_id"),
                "relation": raw.get("relation"),
                "target_id": _text(raw.get("target_id"), f"relationship {relationship_id}.target_id"),
                "origin": "observed",
                "confidence": 1.0,
                "evidence_refs": _dedupe_strings(raw["evidence_refs"], f"relationship {relationship_id}.evidence_refs", allow_empty=False),
            }
            if record["relation"] not in RELATIONSHIP_KINDS:
                raise ValueError(f"relationship {relationship_id}: unknown relation {record['relation']!r}")
            all_evidence.update(record["evidence_refs"])
            _merge_record(relationships, relationship_id, record)

        for raw in capture["success_evidence"]:
            outcome_id = _text(raw.get("outcome_id"), f"{capture['capture_id']}.success_evidence.outcome_id")
            record = {
                "outcome_id": outcome_id,
                "label": _text(raw.get("label"), f"outcome {outcome_id}.label"),
                "surface_id": _text(raw.get("surface_id"), f"outcome {outcome_id}.surface_id"),
                "origin": "observed",
                "confidence": 1.0,
                "evidence_refs": _dedupe_strings(raw["evidence_refs"], f"outcome {outcome_id}.evidence_refs", allow_empty=False),
            }
            all_evidence.update(record["evidence_refs"])
            _merge_record(outcomes, outcome_id, record)

    model = {
        "product_id": normalized["product_id"],
        "revision": normalized["revision"],
        "surfaces": tuple(sorted(surfaces.values(), key=lambda item: item["surface_id"])),
        "objects": tuple(sorted(objects.values(), key=lambda item: item["object_id"])),
        "actions": tuple(sorted(actions.values(), key=lambda item: item["action_id"])),
        "states": tuple(sorted(states.values(), key=lambda item: item["state_id"])),
        "relationships": tuple(sorted(relationships.values(), key=lambda item: item["relationship_id"])),
        "outcomes": tuple(sorted(outcomes.values(), key=lambda item: item["outcome_id"])),
        "evidence_refs": tuple(sorted(all_evidence)),
        "provenance_ids": normalized["provenance_ids"],
        "status": "active",
    }
    validate_ux_product_model(model, provenance_catalog=provenance_catalog)
    return normalize_ux_product_model(model, provenance_catalog=provenance_catalog)


__all__ = [
    "COMMITMENT_LEVELS",
    "MODEL_STATUSES",
    "ORIGINS",
    "RELATIONSHIP_KINDS",
    "SURFACE_KINDS",
    "build_ux_product_model",
    "normalize_ux_discovery_packet",
    "normalize_ux_product_model",
    "validate_ux_discovery_packet",
    "validate_ux_product_model",
]
