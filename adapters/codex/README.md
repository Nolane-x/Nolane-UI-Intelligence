# Codex adapter

NUI's universal contracts stay unchanged in Codex. Use Codex-native workspace editing, terminal execution, browser inspection, screenshots, and worker capabilities when the current Codex surface exposes them.

## Installation/discovery
Place the NUI skill directories in a location Codex scans for Agent Skills (the cross-runtime `.agents/skills` convention is suitable where supported) or keep this repository in the workspace and reference `skills/using-nolane-ui/SKILL.md` from project instructions.

## Tool binding
- File/read/write → Codex workspace tools.
- Tests/validators → run exact repository/project commands; expected output is never evidence.
- Browser → prefer the browser capability integrated into the current Codex environment. Use Playwright/other automation as a fallback when the native browser is unavailable or insufficient, and record the reason.
- Screenshots → capture the exact state/viewport used by fidelity or critic obligations.
- Visual target workflows → do not require ImageGen universally. A screenshot, Figma frame, accepted mock, existing production UI, or user-approved concept can be authoritative.

## Fidelity discipline
When Codex has both target and rendered screenshot, bind both to `verifying-design-fidelity`. Do not substitute DOM inspection for final visual comparison on strict-fidelity work.

## Critic discipline
Use independent/fresh worker context where Codex exposes it. Generator success, compile success, or browser load success does not replace the NUI critic/gate.
