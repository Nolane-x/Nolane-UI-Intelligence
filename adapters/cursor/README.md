# Cursor adapter

Use NUI to constrain design reasoning and review while Cursor provides repository context, editing, terminal, and optional browser/MCP capabilities.

## Integration
Keep the universal skills accessible to the agent and add a project rule that material UI work starts with `using-nolane-ui`. Do not paste the entire skill graph into a single rule file; progressive disclosure is part of NUI's design.

## Capability binding
Verify which agent/browser/MCP features the current Cursor version exposes before claiming them. Map local component libraries through actual repository inspection or a configured registry/MCP; never assume shadcn/Storybook/Figma just because the project is frontend.

## Review
Use a fresh agent/review context for critic lenses when available. If the same context must review its own work, explicitly reload the accepted design contract and critic skill and report the weaker independence.

## Fidelity
Strict visual claims require inspectable rendered captures. A diff of CSS/JSX is useful diagnostic evidence but cannot be the sole fidelity oracle.
