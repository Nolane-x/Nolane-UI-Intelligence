---
name: designing-aac-communication-interfaces
description: Use when an interface supports augmentative and alternative communication, symbol-based language, speech-generating communication, partner-assisted interaction, scanning, or personalized non-vocal communication.
---

# Designing AAC Communication Interfaces

## Overview
AAC is a communication system, not a simplified icon theme. A user may depend on it to express needs, opinions, humor, consent, refusal, identity, urgency, and complex language. Interface choices affect communication rate, motor effort, linguistic growth, privacy, and whether a person can say what they intend rather than only what the software predicted. The design goal is therefore expressive agency and continuity across access methods, vocabulary, symbols, devices, and communication partners.

## Parent Contract
**Required parent:** `designing-accessible-interfaces`.

Consume root accessibility obligations plus the user’s communication goals, known symbol or language system, literacy, motor/access method, sensory needs, communication partners, environments, and device constraints. Never infer that non-speaking means low comprehension. If the user’s established AAC vocabulary or access pattern is unknown, preserve configurability and seek representative evidence rather than replacing it with a generic “easy” board.

## Decision Model
### 1. Start from communicative intent
Model the intents the person must be able to express: request, reject, ask, answer, comment, repair misunderstanding, initiate topic, socialize, disclose pain or danger, consent, and compose novel language. Do not optimize only for common caretaker requests. Ensure the interface supports both quick high-frequency communication and generative expression beyond prewritten phrases.

### 2. Preserve vocabulary and motor consistency
Distinguish core vocabulary, fringe/domain vocabulary, grammatical functions, quick phrases, names, and context-specific words. Stable locations can reduce search and motor-planning cost, so adaptation or prediction must not continuously reorder the entire language surface. Personalization may change available vocabulary, but the user should retain control over learned organization and be able to recover previous layouts.

### 3. Treat symbols as semantic mappings, not decoration
Different AAC symbol sets are not automatically interchangeable. Record concept meaning separately from a rendered symbol so an interface can map to the user’s familiar system when standards and tooling allow. Text labels, symbols, morphology, tense, plurality, cultural meaning, and language order can interact. Do not assume one pictogram is universally understood.

### 4. Design for the actual access method
Support the person’s selected method: direct touch, eye gaze, switch scanning, keyboard, pointer, head tracking, partner-assisted scanning, or combinations. Specify target geometry, dwell or activation behavior, scanning order, focus visibility, accidental-activation recovery, fatigue, and rate. Route each relevant modality faculty rather than making AAC itself responsible for hardware-specific mechanics.

### 5. Protect communication ownership
Prediction, AI completion, and partner assistance may accelerate communication, but generated words must never silently become the user’s statement. Make suggestions distinguishable from committed speech. Provide edit, undo, stop-speech, message history controls, and privacy options for sensitive vocabulary. A communication partner should not gain hidden control over what the user can say.

### 6. Preserve continuity across devices and outages
Users may move between dedicated devices, phones, tablets, web interfaces, and shared environments. Define portability of vocabulary, symbol mappings, preferences, access settings, pronunciations, and backups. Degraded or offline states must preserve essential communication; network loss cannot turn a core communication channel into an empty spinner.

## Evidence
ISO/IEC TS 20071-40:2026 provides current introductory guidance and a framework for AAC in ICT, emphasizing consistency across devices. W3C’s AAC Symbol Registry and WAI-Adapt Symbols work provide semantic mappings intended to support familiar symbol sets and personalized transformations; their status must be recorded accurately rather than assumed fully normative for every platform. Evidence should also include observation with AAC users, established communication vocabularies, access-method trials, communication-rate/error measures, fatigue, partner feedback, and language-specific validation. Clinical or educational decisions remain outside the authority of a UI skill unless qualified domain evidence is supplied.

## Output Contract
Produce an `aac-communication-contract` containing: communication goals; language and symbol system; concept-to-symbol strategy; core/fringe vocabulary architecture; layout stability rules; composition and novel-language path; prediction and AI authorship boundaries; selected access methods and delegated modality contracts; scanning/dwell/target behavior where applicable; communication-partner roles; speech output and stop controls; sensitive-message privacy; offline/degraded essentials; cross-device portability; backup/recovery; localization/morphology concerns; representative user validation; and unresolved communication risks.

## Failure Traps
- Treating AAC as “large buttons with icons.”
- Assuming a non-speaking user has limited comprehension or should receive childlike language.
- Reordering learned vocabulary on every prediction cycle and destroying motor planning.
- Substituting one symbol set for another because the pictures look equivalent to the designer.
- Making AI suggestions speak automatically as if the user authored them.
- Optimizing only for requests such as food or help while omitting refusal, opinion, humor, questions, privacy, and novel expression.
- Designing only for touch when the actual access method is gaze, switch scanning, head tracking, or partner-assisted interaction.
- Requiring a network connection for essential communication.
- Giving caregivers or administrators invisible veto power over ordinary self-expression.

The interface succeeds when the person can communicate with their own language, access method, timing, identity, and authority—not merely operate the software.

## V6 AAC Communication Protocol
Set a **communication-rate budget** for common needs, urgent messages, conversation repair, and novel composition; optimizing visual neatness at the cost of excessive selections is unacceptable. Build **vocabulary access topology** around stable motor/cognitive location, categories, recency, prediction, and personalized words without constantly rearranging core targets.

Support a **partner-assisted path** for users who communicate with trusted partners while preserving direct user agency. Protect **motor-planning consistency** across updates, themes, orientation, and vocabulary growth. Treat authored messages as personal expression under **message-ownership privacy**: prediction/training/history must not expose or silently repurpose intimate communication.

### Falsification
Measure selections/time for high-frequency and emergency messages, switch device/profile, and add vocabulary. If core words move unpredictably or privacy/agency is lost, the layout fails.

### Recovery
Restore stable access paths, reduce steps, provide alternate scanning/direct-selection modes, and preserve user-controlled vocabulary/history boundaries.
