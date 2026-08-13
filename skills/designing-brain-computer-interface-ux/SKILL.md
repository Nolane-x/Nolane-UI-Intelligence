---
name: designing-brain-computer-interface-ux
description: Use when noninvasive or implanted brain-computer interface signals contribute to selection, communication, control, rehabilitation, adaptive behavior, or other interaction where calibration, noisy intent inference, fatigue, privacy, and safety differ from conventional input.
---

# Designing Brain-Computer Interface UX

## Overview
Neural signal is not direct intention. Treat BCI as an uncertain input channel requiring calibration, feedback, error tolerance, privacy boundaries, and alternative control rather than mapping every classified signal directly to irreversible action.

## Parent Contract
**Required parent:** `routing-ui-work`.

Require BCI technology, user population, medical versus nonmedical context, signal pipeline, classification confidence/calibration, command vocabulary, feedback channels, session setup, fatigue, data storage, safety consequence, and alternative input. Implanted/medical devices require domain regulatory and human-factors processes beyond this skill.

## Decision Model
Separate **signal acquisition**, **system inference**, **candidate intent**, **user confirmation where needed**, and **action**. Expose calibration and signal quality in terms that support task recovery without forcing users to interpret raw neuroscience telemetry. Classifier uncertainty can vary by session, posture, fatigue, electrode placement, medication, environment, and task.

Design command vocabulary around discriminability and consequence. High-frequency low-risk commands may tolerate probabilistic selection with easy correction; destructive, financial, mobility, stimulation, or physical-machine actions need stronger confidence and/or an independent confirmation channel. Avoid requiring sustained concentration beyond realistic fatigue limits.

Feedback closes the loop. Users need timely acknowledgement of detected candidate input and committed action, with a way to cancel false positives. For communication BCIs, preserve text/message editing and correction before sending. For adaptive systems, do not silently infer cognitive/emotional state and change behavior without visible policy and override.

Neural data is extremely sensitive. Minimize storage and exposure, separate signal/derived inference, make research/training reuse explicit, and prevent dashboards from casually revealing health-like interpretations. Use stable metadata/provenance because BCI data standards are actively evolving.

## Evidence
Test calibration drift, false positive/negative, fatigue across session duration, signal loss, alternative input, accidental activation, correction time, privacy/export, accessibility, and realistic user population. Medical/implanted validation follows applicable FDA/standards and clinical evidence; simulator success is not clinical proof.

## Output Contract
Return a `bci-interaction-contract` with `signal_pipeline_summary`, `calibration_model`, `intent_states`, `command_vocabulary[]`, `confidence_and_confirmation_policy`, `feedback_loop`, `false_activation_recovery`, `fatigue_constraints`, `alternative_inputs[]`, `neural_data_privacy`, `medical_regulatory_dependencies[]`, and `bci_tests[]`.

## Failure Traps
- Neural classifier output treated as certain intention.
- Irreversible command executed on one noisy detection.
- Raw “attention score” presented as a meaningful psychological truth without validation.
- Calibration hidden until users think they are failing.
- No conventional fallback when signal quality collapses.
- Neural data reused for model training without clear scope/consent.
- Nonmedical UI skill claiming implanted-device safety or clinical efficacy.

BCI interaction is successful when uncertainty is absorbed by the system instead of transferred as blame or risk to the user.

## V6 BCI Interaction Safety Protocol
Use **signal-confidence gating** before mapping classifier output to action; uncertain neural signals should preview/seek confirmation rather than execute high-consequence operations. Set a **false-activation ceiling** by action class and environment, acknowledging non-stationarity, fatigue, artifacts, and user variability.

Minimize **calibration burden** and show when recalibration is needed without implying user failure. Establish a **neural-data consent boundary** for collection, storage, inference, secondary use, clinical interpretation, and sharing. Always retain an **alternative-input escape** so users can pause/disable BCI, correct errors, or complete essential tasks through another accessible modality where feasible.

### Falsification
Inject noisy signals, fatigue drift, classifier confidence near threshold, and accidental activation during rest. If actions fire without trustworthy intent or users cannot escape the mode, the system fails.

### Recovery
Drop to preview/confirmation, recalibrate, suspend unsafe actions, purge/limit questionable inferred state, and switch to alternate input until signal quality is re-established.
