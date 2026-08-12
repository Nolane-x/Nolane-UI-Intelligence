---
name: designing-embedded-kiosk-interfaces
description: Use when a UI runs on dedicated, public, industrial, appliance, kiosk, point-of-service, or constrained embedded hardware with fixed devices, unattended sessions, environmental constraints, or strict recovery needs.
---

# Designing Embedded and Kiosk Interfaces

## Overview
Dedicated hardware removes many escape hatches. Design for public misuse, hardware failure, constrained input, session reset, environmental conditions, and recovery without assuming a personal browser, keyboard, or administrator is nearby.

## Parent Contract
**Required parent:** `routing-ui-work`.

Require hardware/display/input capabilities, public versus supervised context, session ownership, network reliability, environment, accessibility, timeout policy, physical peripherals, and failure/reboot constraints. Route safety-critical industrial controls through human factors.

## Decision Model
Define the session lifecycle first: attract/idle, start, identify if needed, task, payment/commit if any, receipt/handoff, completion, privacy clearing, timeout, and recovery. Public sessions must never leak the previous user’s data after completion, timeout, crash, or Back navigation.

Design for the actual hardware: fixed screen size, brightness/glare, gloves, rugged touch, scanner, card reader, printer, keypad, NFC, physical buttons, or no keyboard. Peripheral state is UI state. Show whether a card reader is ready, printer is out of paper, scanner failed, or network is unavailable before asking users to repeat actions blindly.

Offline/degraded behavior needs explicit capability. Queue only operations that are safe to replay; distinguish “not submitted,” “queued,” “accepted,” and “completed.” Payment or identity flows require stronger duplicate-action protection.

Timeouts balance privacy and task duration. Warn before clearing active work, allow extension when safe, and clear sensitive state deterministically. Kiosks need an accessible recovery path that does not expose an admin surface to the public.

## Evidence
Test power/network interruption, peripheral unplug/failure, dirty/coarse touch, timeout at each task stage, session reset, long accessibility interaction, public shoulder-surfing, duplicate taps, reboot recovery, and unattended idle. Hardware-in-loop evidence matters more than desktop emulation for critical device behavior.

## Output Contract
Return an `embedded-kiosk-contract` with `session_lifecycle`, `hardware_inventory[]`, `peripheral_states[]`, `environment_constraints[]`, `offline_capability`, `duplicate_protection`, `timeout_policy`, `privacy_clearing`, `public_vs_admin_boundary`, `recovery_states[]`, and `hardware_tests[]`.

## Failure Traps
- Previous user data remains after timeout.
- Spinner hides whether payment was sent twice.
- Generic “something went wrong” when a specific peripheral is unavailable.
- Tiny touch targets on rugged/gloved hardware.
- No recovery when a receipt printer fails after payment.
- Admin escape gesture discoverable by public users.
- Desktop browser assumptions about keyboard, Back, refresh, or network.

A kiosk is trustworthy when failure leaves the next person in a known, private, recoverable state.