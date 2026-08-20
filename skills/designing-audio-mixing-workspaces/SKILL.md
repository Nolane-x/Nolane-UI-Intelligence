---
name: designing-audio-mixing-workspaces
description: Use when this specialist's decision ownership is materially in scope. Own audio mixing interfaces across channel/track/bus routing, gain, pan, mute/solo, meters, sends, inserts, automation mode, clipping, loudness, and mix-state provenance.
---
# Designing Audio Mixing Workspaces

## Parent Contract

**Required parent:** `designing-nonlinear-media-editors`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own the mixer as a signal-routing and level-control workspace. Decide channel strips, track/bus/master hierarchy, input/output routing, gain/fader, pan, mute/solo, metering, sends, inserts, clipping, loudness context, and automation mode visibility. Track management owns editorial track structure; this owner owns audible signal flow and mix state.

## Inputs and evidence

Require audio track/channel layout, buses, routing graph, gain/pan ranges, plugins/effects, send topology, metering types, sample rate, loudness targets, automation modes, hardware I/O, and latency. Identify mono/stereo/surround/immersive differences.

## Procedure

Make signal path inspectable from source track through buses to master/output. Channel strips must identify track/bus and current routing. Faders/pan show numeric values and reset reference; meters distinguish peak/RMS/loudness as applicable and retain clip indicators. Solo/mute state needs a global cue when it alters the mix. Sends and inserts expose pre/post-fader and bypass state. Automation mode—read/write/touch/latch/off—must be unmistakable before moving a fader that can write keyframes. Routing changes preview downstream impact and avoid silent feedback loops.

## Failure topology

Failures include fader movement writing automation unexpectedly, hidden solo making mix silent, routing to wrong bus, meters with unknown scale, clipping indicator disappearing too fast, plugin bypass mistaken for removal, and feedback routing accepted silently. Another failure is visual channel order drifting from timeline track identity.

## Falsification

Reject if signal routing cannot be traced; if automation-write mode is hidden; if meter scale/type is unknown; if solo/mute global effect is invisible; if a routing change can create invalid feedback with no detection; if timeline/mixer track identity diverges; or if numeric gain/pan cannot be recovered.

## Output contract

Return an `audio-mixing-workspaces-contract` with: channel/bus/master identity; routing graph; fader/gain/pan; meter type/scale; clip/loudness state; mute/solo; sends/inserts; bypass; automation mode; routing validation; hardware I/O; and mix-state provenance. Include one hidden-solo and one automation-write case.

## Handoffs

Audio automation curves own written envelopes, track management owns editorial tracks, media playback monitors mix output, and render/export queues produce final audio.