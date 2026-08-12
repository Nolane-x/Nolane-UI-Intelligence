---
name: designing-avatar-embodied-representation
description: Use when a product represents a person, organization, character, assistant, agent, or autonomous system through an avatar, embodied persona, virtual body, or persistent visual identity.
---

# Designing Avatar Embodied Representation

## Overview
An avatar is not merely an illustration placed beside a name. It is an identity and agency surface: users infer who or what is present, who controls it, whether it represents a real person, whether its behavior is live or generated, and what social meaning its appearance carries. Avatar design therefore combines representation, disclosure, control, accessibility, social signaling, impersonation risk, and cross-context continuity. A visually convincing avatar that confuses authorship or agency is a failed interface.

## Parent Contract
**Required parent:** `routing-ui-work`.

Consume a `ui-task-profile` describing who or what the avatar represents, who controls its appearance and behavior, whether it is real-time, recorded, scripted, AI-generated, agentic, or mixed, the social setting, identity sensitivity, and the consequences of misattribution. If control or representation ownership is unknown, do not invent a persona; return an identity-boundary gap.

## Decision Model
### 1. Classify represented entity and controller
Distinguish self-representation, another real person, organization, fictional character, service persona, AI assistant, autonomous agent, and shared/group identity. Separately identify the controller: represented person, another human operator, scripted system, generative model, autonomous agent, or hybrid. Representation and control must never be assumed to be the same.

### 2. Define disclosure and attribution
The interface must let a reasonable user tell when an avatar is synthetic, delegated, automated, impersonating with permission, or speaking for a person. Attribution should survive dense feeds, notifications, voice playback, transcripts, compact layouts, and accessibility representations. If agency changes during a session, disclose the transition at the point where user expectations would otherwise be wrong.

### 3. Bound likeness and identity authority
Record who may create, edit, export, clone, animate, or reuse a likeness. Separate cosmetic customization from identity claims. High-fidelity facial, vocal, or body representations need stronger authorization and provenance than abstract icons. Design recovery for stolen likeness, mistaken identity, account takeover, revoked consent, and cross-tenant leakage.

### 4. Design social meaning without forced stereotypes
Appearance, gesture, clothing, body shape, age cues, disability representation, skin tone, cultural markers, and gender expression can communicate identity but can also encode stereotype or exclusion. Provide meaningful user control where self-expression is a product goal, while avoiding defaults that assign identity from inferred demographics. A professional or safety context may appropriately constrain expression, but the reason should come from task and policy rather than designer taste.

### 5. Preserve accessibility beyond the image
Do not encode speaker, presence, status, role, ownership, or emotion solely in visual appearance or animation. Provide programmatic names, role/status text, captions or transcripts for avatar speech, reduced-motion behavior, contrast-safe status cues, and a coherent non-visual representation. For sign-language or communication avatars, accuracy and linguistic evidence outrank aesthetic smoothness.

### 6. Maintain continuity across surfaces
Define which identity attributes persist across web, mobile, XR, notifications, collaboration views, and exports. Scale detail to viewing distance without changing who the avatar appears to be. When a single account can operate multiple personae, prevent context leakage by making the active persona and audience visible before consequential communication.

## Evidence
ISO/IEC 24216-1:2026 provides current published requirements and recommendations for user interfaces using avatars, including categorization plus ethical and usability considerations across entertainment, business, VR, AR, MR, cyber-physical, metaverse, and related systems. Supplement standards with product identity policy, consent records, provenance, impersonation threat analysis, representative usability research, and accessibility testing. For AI-controlled avatars, also require the human-AI and agency evidence owned by the AI faculties rather than using embodiment as a substitute for disclosure.

## Output Contract
Produce an `avatar-representation-contract` containing: represented entity; controller and automation model; identity/provenance source; disclosure rules; likeness permissions; customization boundaries; social-signaling constraints; impersonation and abuse defenses; accessibility representation; speech/caption/transcript behavior; cross-surface continuity; active-persona and audience indicators; revocation/recovery flow; AI/agent handoff conditions; and evidence required before high-fidelity or consequential representation can ship.

## Failure Traps
- Assuming the avatar’s appearance tells users whether it is a human or an AI.
- Letting an AI-controlled avatar speak as a real person without explicit attribution.
- Treating likeness capture as ordinary profile-image upload with no reuse boundary.
- Encoding presence, speaker identity, emotion, or role only through color, animation, or facial expression.
- Inferring ethnicity, gender, disability, age, or personality and applying it as representation without user control.
- Allowing persona switching without showing the active identity and audience.
- Making a photorealistic avatar more authoritative than the evidence behind its claims.
- Designing sign or communication avatars for visual smoothness while ignoring linguistic correctness.
- Reusing an avatar across contexts after consent or authority has been revoked.

The avatar succeeds when it strengthens identity and social comprehension without blurring who is present, who is acting, or who is accountable.
