---
name: designing-mobile-app-switcher-privacy
description: Use when sensitive mobile content can appear in operating-system task switcher snapshots, recent-app previews, background thumbnails, screen recording, or transient inactive states.
---

# Designing Mobile App Switcher Privacy

## Parent Contract

**Required parent:** `designing-mobile-native-application-shells`.

This skill owns privacy treatment when the active application becomes visually observable outside its ordinary foreground interaction, especially task/app switcher snapshots. It is not a general screenshot-prevention policy and must not promise protection the operating system cannot enforce.

## Privacy boundary

Classify screens and regions by snapshot sensitivity: public/low-risk, personal, confidential, regulated/high-consequence, or product-specific categories. Decide whether privacy treatment is screen-wide, region-based, state-based or user-configurable. A bank balance, private message preview, patient record and secret token may need different redaction behavior even in the same app.

Understand the platform lifecycle point at which recent-app imagery is captured. Apply protective content early enough to affect the snapshot but not so aggressively that routine transient inactivity causes visible flashes during benign system overlays. If the platform supplies official secure-window or privacy APIs, use them within their documented scope. Do not infer that blocking a screenshot also blocks screen recording, mirroring, accessibility capture, app-switcher previews, or another device's camera.

Redaction should preserve task recognizability where possible. A neutral branded privacy cover can tell the user which app they are returning to; region masking can preserve nonsensitive shell context. However, partial masking is unsafe if sensitive content can appear dynamically in notifications, canvas thumbnails, cached images, overlays or OS-owned previews.

Coordinate with authentication timeout. A private task-switcher snapshot does not mean the underlying session is locked. Conversely, forcing reauthentication on every short inactive transition can be unusable. Define separate policies for visual privacy, session validity and re-entry authentication.

## Evidence

Use OS lifecycle/snapshot documentation, device screenshots of recent-app surfaces, screen-record/mirroring behavior, notification previews, sensitive-data classification and reauthentication policy. Test on representative OS versions because capture timing and secure-window capabilities differ. Record what is proven versus merely intended.

## Failure topology

Failures include applying a blur after the OS has already captured the frame; a privacy overlay that itself contains sensitive cached text; assuming secure-window flags work identically across platforms; showing a blank white rectangle that makes users think the app crashed; revealing another account's previous screen during fast account switching; or conflating screenshot deterrence with comprehensive exfiltration prevention.

A particularly subtle failure is privacy flicker: sensitive content renders for one frame before redaction during resume, making it observable in recordings or to shoulder surfers even though the eventual UI is covered.

## Falsification

Open representative sensitive states, invoke app switcher repeatedly, trigger notification/control-center/system permission overlays, record the screen where allowed, switch accounts, background during loading and resume under slow device conditions. The contract is falsified if any claimed-protected preview contains sensitive pixels/text, if protection appears after capture, if returning briefly exposes stale sensitive content, or if documentation claims defenses beyond demonstrated platform capability.

## Recovery

Move privacy state to the lifecycle boundary rather than individual screens where necessary, clear stale sensitive render caches, gate sensitive restoration behind validated identity, and phrase limitations explicitly. When platform guarantees are weak, reduce what is rendered in vulnerable states rather than promising absolute capture prevention.

## Output contract

Return a `mobile-app-switcher-privacy-contract` containing sensitivity classes, protected states/regions, lifecycle timing, platform capability matrix, redaction presentation, session-versus-visual privacy distinction, account-switch behavior, recording/screenshot claim limits, and device falsification evidence.

## Handoffs

Use privacy-sensitive interface owners for data classification, authentication/session owners for re-entry, notification owners for lock-screen previews, lifecycle restoration for stale render prevention, and platform guidance for actual secure-window/capture capabilities.