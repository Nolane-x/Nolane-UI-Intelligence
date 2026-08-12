"""Deterministic product-closure checks.

These checks intentionally validate referential and evidence structure. They do
not infer that a design is usable or good merely because a graph is closed.
"""
from __future__ import annotations

from collections import defaultdict, deque
from typing import Any


def _records(record: dict[str, Any], key: str, errors: list[str]) -> list[dict[str, Any]]:
    value = record.get(key)
    if not isinstance(value, list):
        errors.append(f"functional closure requires {key} list")
        return []
    out: list[dict[str, Any]] = []
    for index, item in enumerate(value):
        if not isinstance(item, dict):
            errors.append(f"{key}[{index}] must be an object")
        else:
            out.append(item)
    return out


def _index(items: list[dict[str, Any]], kind: str, errors: list[str]) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    for item in items:
        iid = item.get("id")
        if not isinstance(iid, str) or not iid.strip():
            errors.append(f"{kind} requires non-empty id")
            continue
        if iid in out:
            errors.append(f"duplicate {kind} id {iid}")
        out[iid] = item
    return out


def validate_functional_closure(record: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    if not isinstance(record, dict):
        return {"valid": False, "errors": ["functional closure record must be an object"]}

    capabilities = _index(_records(record, "capabilities", errors), "capability", errors)
    surfaces = _index(_records(record, "surfaces", errors), "surface", errors)
    actions = _index(_records(record, "actions", errors), "action", errors)
    bindings = _index(_records(record, "bindings", errors), "binding", errors)
    routes = _records(record, "routes", errors)
    scenarios = _index(_records(record, "scenarios", errors), "scenario", errors)

    required_capabilities = {cid for cid, cap in capabilities.items() if cap.get("required", True)}

    # Capability ownership and representation.
    for cid, cap in capabilities.items():
        surface_ids = cap.get("surface_ids", [])
        action_ids = cap.get("action_ids", [])
        if cid in required_capabilities and (not isinstance(surface_ids, list) or not surface_ids):
            errors.append(f"required capability {cid} has no surface representation")
        if cid in required_capabilities and (not isinstance(action_ids, list) or not action_ids):
            errors.append(f"required capability {cid} has no action representation")
        for sid in surface_ids if isinstance(surface_ids, list) else []:
            if sid not in surfaces:
                errors.append(f"capability {cid} references unknown surface {sid}")
        for aid in action_ids if isinstance(action_ids, list) else []:
            if aid not in actions:
                errors.append(f"capability {cid} references unknown action {aid}")

    # Actions and recovery obligations.
    for aid, action in actions.items():
        cid = action.get("capability_id")
        if cid not in capabilities:
            errors.append(f"action {aid} references unknown capability {cid}")
        destination = action.get("destination_id")
        if destination is not None and destination not in surfaces:
            errors.append(f"action {aid} references unknown destination {destination}")
        if action.get("risk") in {"async", "destructive", "permission", "transaction"}:
            if not isinstance(action.get("recovery"), str) or not action.get("recovery", "").strip():
                errors.append(f"action {aid} with risk {action.get('risk')} requires recovery")

    # Binding integrity and semantic collision detection.
    action_bindings: dict[str, list[dict[str, Any]]] = defaultdict(list)
    label_semantics: dict[tuple[str, str], set[str]] = defaultdict(set)
    for bid, binding in bindings.items():
        aid = binding.get("action_id")
        sid = binding.get("surface_id")
        if aid not in actions:
            errors.append(f"binding {bid} references unknown action {aid}")
        else:
            action_bindings[aid].append(binding)
        if sid not in surfaces:
            errors.append(f"binding {bid} references unknown surface {sid}")
        modalities = binding.get("modalities")
        if not isinstance(modalities, list) or not modalities:
            errors.append(f"binding {bid} requires at least one modality")
        discoverability = binding.get("discoverability")
        if discoverability not in {"visible", "menu", "context", "palette", "shortcut", "gesture", "programmatic"}:
            errors.append(f"binding {bid} has invalid discoverability {discoverability}")
        label = binding.get("label")
        if isinstance(label, str) and label.strip() and isinstance(sid, str) and isinstance(aid, str):
            label_semantics[(sid, " ".join(label.lower().split()))].add(aid)
    for (sid, label), aids in label_semantics.items():
        if len(aids) > 1:
            errors.append(f"semantic label collision on surface {sid}: {label!r} maps to {sorted(aids)}")
    for aid in actions:
        if not action_bindings.get(aid):
            errors.append(f"action {aid} has no UI binding")

    # Reachability. A deep-link string is not a graph edge and cannot rescue an
    # otherwise orphan destination.
    adjacency: dict[str, set[str]] = defaultdict(set)
    for index, route in enumerate(routes):
        src, dst, aid = route.get("from"), route.get("to"), route.get("action_id")
        if src not in surfaces:
            errors.append(f"route {index} references unknown source surface {src}")
            continue
        if dst not in surfaces:
            errors.append(f"route {index} references unknown destination surface {dst}")
            continue
        if aid not in actions:
            errors.append(f"route {index} references unknown action {aid}")
            continue
        if route.get("intentional") is not True:
            errors.append(f"route {src}->{dst} must explicitly be intentional")
        adjacency[src].add(dst)

    entries = [sid for sid, surface in surfaces.items() if surface.get("entry") is True]
    if not entries:
        errors.append("functional closure requires at least one entry surface")
    reachable = set(entries)
    queue = deque(entries)
    while queue:
        src = queue.popleft()
        for dst in adjacency.get(src, ()):
            if dst not in reachable:
                reachable.add(dst)
                queue.append(dst)
    needed_surfaces = {
        sid
        for cid in required_capabilities
        for sid in capabilities.get(cid, {}).get("surface_ids", [])
        if isinstance(sid, str)
    }
    for sid in sorted(needed_surfaces - reachable):
        errors.append(f"required surface {sid} is unreachable from every entry surface")

    # Scenario coverage is independent of static reachability: the product must
    # demonstrate that required capabilities participate in at least one user path.
    scenario_caps: set[str] = set()
    for scid, scenario in scenarios.items():
        start = scenario.get("start_surface")
        if start not in surfaces:
            errors.append(f"scenario {scid} has unknown start surface {start}")
        cap_ids = scenario.get("capability_ids")
        if not isinstance(cap_ids, list) or not cap_ids:
            errors.append(f"scenario {scid} requires capability_ids")
            cap_ids = []
        for cid in cap_ids:
            if cid not in capabilities:
                errors.append(f"scenario {scid} references unknown capability {cid}")
            else:
                scenario_caps.add(cid)
        path_actions = scenario.get("path_actions")
        if not isinstance(path_actions, list) or not path_actions:
            errors.append(f"scenario {scid} requires path_actions")
        else:
            for aid in path_actions:
                if aid not in actions:
                    errors.append(f"scenario {scid} references unknown action {aid}")
    for cid in sorted(required_capabilities - scenario_caps):
        errors.append(f"required capability {cid} has no scenario coverage")

    if record.get("status") == "PASS" and errors:
        errors.append("functional closure status cannot be PASS while closure errors exist")
    if record.get("status") not in {"PASS", "FAIL", "UNKNOWN"}:
        errors.append("functional closure status must be PASS, FAIL, or UNKNOWN")

    return {
        "valid": not errors,
        "errors": errors,
        "required_capability_count": len(required_capabilities),
        "surface_count": len(surfaces),
        "action_count": len(actions),
        "binding_count": len(bindings),
        "reachable_surfaces": sorted(reachable),
    }


def validate_ui_specification(spec: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    screens = spec.get("screens") if isinstance(spec, dict) else None
    if not isinstance(screens, list) or not screens:
        return {"valid": False, "errors": ["ui specification requires non-empty screens"], "missing_actions": []}
    required_actions = set(spec.get("required_action_ids", []))
    represented: set[str] = set()
    seen_screens: set[str] = set()
    for screen in screens:
        if not isinstance(screen, dict):
            errors.append("ui specification screen must be an object")
            continue
        sid = screen.get("id")
        if not isinstance(sid, str) or not sid:
            errors.append("ui specification screen requires id")
            continue
        if sid in seen_screens:
            errors.append(f"duplicate ui specification screen {sid}")
        seen_screens.add(sid)
        states = screen.get("states")
        if not isinstance(states, list) or not states:
            errors.append(f"screen {sid} requires states")
        if not isinstance(screen.get("responsive_behavior"), str) or not screen.get("responsive_behavior", "").strip():
            errors.append(f"screen {sid} requires responsive_behavior")
        controls = screen.get("controls")
        if not isinstance(controls, list):
            errors.append(f"screen {sid} requires controls list")
            controls = []
        for control in controls:
            if not isinstance(control, dict):
                errors.append(f"screen {sid} contains non-object control")
                continue
            for field in ("id", "action_id", "label", "semantic_role", "focus_behavior", "accessibility_name"):
                if not isinstance(control.get(field), str) or not control.get(field, "").strip():
                    errors.append(f"screen {sid} control requires {field}")
            if isinstance(control.get("action_id"), str):
                represented.add(control["action_id"])
    missing = sorted(required_actions - represented)
    errors.extend(f"required action {aid} has no implementation-spec control" for aid in missing)
    return {"valid": not errors, "errors": errors, "missing_actions": missing, "screen_count": len(seen_screens)}


def validate_runtime_behavior_ledger(ledger: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    if not isinstance(ledger, dict):
        return {"valid": False, "errors": ["runtime behavior ledger must be an object"], "failed_actions": [], "missing_actions": []}
    required = set(ledger.get("required_action_ids", []))
    probes = ledger.get("probes")
    if not isinstance(probes, list):
        probes = []
        errors.append("runtime behavior ledger requires probes")
    passed: set[str] = set()
    failed: set[str] = set()
    for probe in probes:
        if not isinstance(probe, dict):
            errors.append("runtime probe must be an object")
            continue
        aid = probe.get("action_id")
        if not isinstance(aid, str) or not aid:
            errors.append("runtime probe requires action_id")
            continue
        if probe.get("status") == "PASS":
            passed.add(aid)
        elif probe.get("status") in {"FAIL", "UNKNOWN"}:
            failed.add(aid)
        else:
            errors.append(f"runtime probe {aid} has invalid status")
        if not isinstance(probe.get("modalities"), list) or not probe.get("modalities"):
            errors.append(f"runtime probe {aid} requires modalities")
        if not isinstance(probe.get("evidence"), str) or not probe.get("evidence", "").strip():
            errors.append(f"runtime probe {aid} requires evidence")
    missing = sorted(required - passed - failed)
    failed_required = sorted(required & failed)
    errors.extend(f"required action {aid} has no runtime probe" for aid in missing)
    errors.extend(f"required action {aid} failed runtime verification" for aid in failed_required)
    return {"valid": not errors, "errors": errors, "failed_actions": failed_required, "missing_actions": missing}


__all__ = ["validate_functional_closure", "validate_ui_specification", "validate_runtime_behavior_ledger"]
