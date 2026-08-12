---
name: translating-standards-into-obligations
description: Use when a UI task is governed by accessibility, safety, security, regulatory, platform, or organizational standards that must become scoped design and verification requirements.
---

# Translating Standards into Obligations

## Overview
A standard is useful to an agent only when its applicability, requirement strength, test method, and evidence boundary are explicit. This skill turns authoritative guidance into obligations without pretending that prose interpretation equals legal or formal conformance certification.

## Parent Contract
**Required parent:** `calibrating-ui-authority`.

Consume an `authority-resolution` identifying applicable sources and status. If jurisdiction, product classification, platform, or standard version is unknown and materially changes applicability, output a blocking applicability question or bounded alternative sets rather than guessing.

## Decision Model
Extract the smallest actionable obligation that preserves the source intent. Separate normative requirement from informative guidance. Capture: subject, trigger condition, required outcome, exceptions, evidence method, and authority reference. Avoid copying source sentences when a precise synthesis is possible.

Then map obligations to lifecycle stages. Some constraints belong at architecture time — error prevention, alternative input paths, medical critical-task flow. Others belong at component time — target geometry, focus semantics, accessible names. Others require runtime or human evidence — screen-reader behavior, driving-distraction validation, cognitive usability, high-stakes use testing.

Do not convert every guideline into an unconditional rule. A dragging alternative applies when drag operates functionality; automotive restrictions depend on driving context; WCAG 3 draft outcomes may guide exploration but cannot be represented as current WCAG 2.2 conformance. When a standard defers to domain expertise or formal validation, preserve that dependency.

## Evidence
Every obligation stores source id/version/status, applicability rationale, testability class (`deterministic`, `runtime`, `human-evaluation`, `domain-validation`), evidence owner, and consequence of failure. If the source text is inaccessible or paywalled, record only verified metadata and require the licensed standard for clause-level compliance work.

## Output Contract
Return a `standard-obligation-set` with `scope`, `authority_refs[]`, `applicability_assumptions[]`, `obligations[] {id, requirement_strength, trigger, outcome, exceptions, lifecycle_stage, evidence_method, failure_severity}`, `informative_guidance[]`, `unverified_or_external_requirements[]`, and `conformance_claim_limit`.

## Failure Traps
- Quoting a standard without turning it into a testable outcome.
- Treating informative examples as normative requirements.
- Silently promoting a draft to a released standard.
- Claiming legal, medical, accessibility, or safety certification from agent review alone.
- Removing documented exceptions and thereby making the rule incorrect.
- Using platform guidance to weaken a higher-order requirement.
- Declaring PASS when the required evidence method was never executed.

The obligation is complete only when another agent can tell exactly what must be true, why, and what evidence would falsify it.