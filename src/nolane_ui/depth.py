"""NUI v6 ontology and skill-depth validators."""
from __future__ import annotations
from collections import Counter
from typing import Any

MANDATORY_ONTOLOGY_AXES = {
    "surfaces_platforms", "input_modalities", "product_interface_archetypes",
    "information_data_character", "interaction_mechanics", "visual_media_systems",
    "aesthetic_art_direction_regimes", "design_system_maturity",
    "accessibility_inclusive_contexts", "localization_script_conditions",
    "temporal_network_behavior", "collaboration_social_topology", "ai_agency",
    "trust_risk", "implementation_ecosystem",
}

def _skills_unknown(items: Any, known: set[str]) -> list[str]:
    if not isinstance(items, list): return []
    return sorted(str(x) for x in items if str(x) not in known)

def validate_industry_ontology(ontology: dict[str, Any], known_skills: set[str]) -> dict[str, Any]:
    errors: list[str] = []
    if not isinstance(ontology, dict):
        return {"valid":False,"errors":["industry ontology must be an object"],"axis_count":0,"axis_value_count":0,"interaction_cell_count":0}
    if ontology.get("version") != 6: errors.append("industry ontology version must be 6")
    axes=ontology.get("axes") if isinstance(ontology.get("axes"),dict) else {}
    missing=sorted(MANDATORY_ONTOLOGY_AXES-set(axes))
    for axis in missing: errors.append(f"missing mandatory ontology axis: {axis}")
    axis_values=0
    obligations=ontology.get("axis_obligations") if isinstance(ontology.get("axis_obligations"),dict) else {}
    for axis, values in axes.items():
        if not isinstance(values,list) or not values:
            errors.append(f"ontology axis {axis} requires values"); continue
        if len(values)!=len(set(map(str,values))): errors.append(f"ontology axis {axis} contains duplicate values")
        axis_values += len(values)
        obligation=obligations.get(axis)
        if not isinstance(obligation,dict):
            errors.append(f"ontology axis {axis} requires axis_obligations"); continue
        owners=obligation.get("owner_skills") if isinstance(obligation.get("owner_skills"),list) else []
        verifiers=obligation.get("verifier_skills") if isinstance(obligation.get("verifier_skills"),list) else []
        if not owners: errors.append(f"ontology axis {axis} requires owner_skills")
        if not verifiers: errors.append(f"ontology axis {axis} requires verifier_skills")
        for skill in _skills_unknown(owners+verifiers,known_skills): errors.append(f"ontology axis {axis} references unknown skill: {skill}")
        if set(owners)&set(verifiers): errors.append(f"ontology axis {axis} requires independent owner and verifier skills")
        if not obligation.get("evidence_classes"): errors.append(f"ontology axis {axis} requires evidence_classes")
        if not obligation.get("source_domains"): errors.append(f"ontology axis {axis} requires source_domains")
    cells=ontology.get("interaction_cells") if isinstance(ontology.get("interaction_cells"),list) else []
    seen=set()
    for i,cell in enumerate(cells):
        if not isinstance(cell,dict): errors.append(f"interaction cell {i} must be an object"); continue
        cid=str(cell.get("id",''))
        if not cid: errors.append(f"interaction cell {i} requires id")
        elif cid in seen: errors.append(f"duplicate interaction cell id: {cid}")
        seen.add(cid)
        conditions=cell.get("conditions") if isinstance(cell.get("conditions"),dict) else {}
        if len(conditions)<2: errors.append(f"interaction cell {cid or i} requires at least two crossed axes")
        for axis,value in conditions.items():
            if axis not in axes: errors.append(f"interaction cell {cid or i} uses unknown axis {axis}")
            elif value not in axes[axis]: errors.append(f"interaction cell {cid or i} uses unknown value {axis}={value}")
        owners=cell.get("owner_skills") if isinstance(cell.get("owner_skills"),list) else []
        verifiers=cell.get("verifier_skills") if isinstance(cell.get("verifier_skills"),list) else []
        if not owners: errors.append(f"interaction cell {cid or i} requires owner_skills")
        if not verifiers: errors.append(f"interaction cell {cid or i} requires verifier_skills")
        for skill in _skills_unknown(owners+verifiers,known_skills): errors.append(f"interaction cell {cid or i} references unknown skill: {skill}")
        if set(owners)&set(verifiers): errors.append(f"interaction cell {cid or i} requires independent owner and verifier skills")
        if not cell.get("why_interaction_is_distinct"): errors.append(f"interaction cell {cid or i} requires why_interaction_is_distinct")
        if not cell.get("evidence_required"): errors.append(f"interaction cell {cid or i} requires evidence_required")
    return {"valid":not errors,"errors":errors,"axis_count":len(axes),"axis_value_count":axis_values,"interaction_cell_count":len(cells)}

SKILL_DEPTH_DIMENSIONS = (
    "ownership", "inputs_inherited_obligations", "observation_protocol",
    "branch_logic_tradeoffs", "counterfactual_falsification", "evidence",
    "output_semantics", "failure_topology", "escalation_recovery",
    "downstream_verification",
)


def validate_skill_depth_record(record: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    if not isinstance(record, dict):
        return {"valid": False, "errors": ["skill depth record must be an object"], "missing_dimensions": list(SKILL_DEPTH_DIMENSIONS), "dimension_count": 0}
    if not str(record.get("skill", "")).strip(): errors.append("skill depth record requires skill")
    dims = record.get("dimensions") if isinstance(record.get("dimensions"), dict) else {}
    missing = [d for d in SKILL_DEPTH_DIMENSIONS if d not in dims]
    for d in missing: errors.append(f"skill depth record missing behavioral dimension: {d}")
    for d in SKILL_DEPTH_DIMENSIONS:
        if d not in dims: continue
        item = dims[d]
        if not isinstance(item, dict):
            errors.append(f"skill depth dimension {d} must be an object"); continue
        evidence = str(item.get("evidence", "")).strip()
        decision = str(item.get("decision", "")).strip()
        if not evidence: errors.append(f"skill depth dimension {d} requires concrete evidence")
        if not decision: errors.append(f"skill depth dimension {d} requires a decision consequence")
        if evidence and decision and evidence == decision: errors.append(f"skill depth dimension {d} cannot use the same text as evidence and decision")
    if not str(record.get("evaluator", "")).strip(): errors.append("skill depth record requires evaluator")
    return {"valid": not errors, "errors": errors, "missing_dimensions": missing, "dimension_count": sum(1 for d in SKILL_DEPTH_DIMENSIONS if d in dims)}


def audit_skill_depth(records: list[dict[str, Any]]) -> dict[str, Any]:
    errors: list[str] = []
    warnings: list[str] = []
    results = []
    signature_counts: Counter[tuple[str, ...]] = Counter()
    for record in records if isinstance(records, list) else []:
        result = validate_skill_depth_record(record)
        results.append({"skill": record.get("skill") if isinstance(record, dict) else None, **result})
        if not result["valid"]: errors.extend(f"{record.get('skill','?')}: {e}" for e in result["errors"])
        if isinstance(record, dict) and isinstance(record.get("dimensions"), dict):
            signature = tuple(str(record["dimensions"].get(d, {}).get("evidence", "")).strip().lower() for d in SKILL_DEPTH_DIMENSIONS)
            signature_counts[signature] += 1
    repeated = [count for sig, count in signature_counts.items() if count >= 4 and any(sig)]
    if repeated:
        warnings.append(f"Repeated identical depth evidence signature detected across {max(repeated)} skills; inspect for templated reasoning rather than domain-specific decision procedures.")
    return {"valid": not errors, "errors": errors, "warnings": warnings, "records": results, "record_count": len(results)}
