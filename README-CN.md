<div align="center">

# Nolane UI Intelligence

### 面向 AI Agent 的设计认知、产品完整性、视觉品质与证据门控验证系统

**AI 已经能在几秒钟内生成界面。NUI 想做的是让它在交付之前，先像一支真正的产品与设计团队那样思考。**

[English](README.md) · [Tiếng Việt](README-VN.md) · [简体中文](README-CN.md)

`v0.10.0` · `874 个 canonical skills` · `9 个 Agent projection` · `MCP + CLI` · `证据门控` · `MIT`

</div>

---

## 项目简介

**Nolane UI Intelligence（NUI）** 是一个面向 AI coding agent 的开源设计认知与 UI/UX 验证系统。它不是把几十条“最佳实践”塞进一个提示词，而是通过可路由的专业 skill graph，让 Agent 在产品建模、信息架构、交互、视觉方向、字体、动效、可访问性、平台行为、认证、设置系统、专业工作区、产品完整性、真实渲染批评、design-to-code fidelity 与 empirical evaluation 等不同问题上调用不同 owner。

NUI **不是**组件库、风格预设、mega-prompt、截图复刻工具，也不是一个所谓的“绝对美感分数”。它试图让设计决策变得**可解释、可路由、可反驳、可验证，并且让发布声明受到真实证据约束**。

### Topics / Tags

`ai-agents` · `agent-skills` · `ui-ux` · `design-intelligence` · `design-system` · `frontend` · `codex` · `claude-code` · `gemini-cli` · `opencode` · `cursor` · `vscode` · `mcp` · `accessibility` · `human-computer-interaction` · `ai-coding`

---

# 在你的 AI Agent 中使用 NUI

NUI 现在可以通过同一套 canonical cognition graph 服务于 **Codex、Claude Code、Google Antigravity、Gemini CLI、OpenCode、Cursor、VS Code/Copilot-compatible Agent、任意 MCP Host，以及拥有 shell/CLI 的通用 Agent**。

它的原则不是为每个厂商复制一份数百个 skill 的巨大 prompt，而是：

```text
一套 canonical NUI cognition graph
              ↓
       很薄的 host projection
              ↓
Codex / Claude / Gemini / OpenCode / Cursor / VS Code / MCP / CLI
```

## 快速开始

```bash
git clone https://github.com/Nolane-x/Nolane-UI-Intelligence.git
cd Nolane-UI-Intelligence
```

查看某个 Agent 的 NUI 集成计划：

```bash
python scripts/nui-agent-export --agent openai-codex
```

目前仓库中具有真实 executable projection 的 adapter ID：

```text
openai-codex
claude-code
google-antigravity
gemini-cli
opencode
cursor-compatible
vscode-agent-compatible
generic-mcp
generic-cli
```

### Agent 支持矩阵

| Agent / Host | 推荐接入方式 | NUI 入口 |
|---|---|---|
| **Codex** | Agent Skills bridge + repository policy | `.agents/skills/nolane-ui/SKILL.md` + `python scripts/nui-agent-export --agent openai-codex` |
| **Claude Code** | Native project skill bridge | `.claude/skills/nolane-ui/SKILL.md` + `python scripts/nui-agent-export --agent claude-code` |
| **Google Antigravity** | Agent Skills bridge 或 MCP | `python scripts/nui-agent-export --agent google-antigravity` |
| **Gemini CLI** | CLI/MCP projection | `python scripts/nui-agent-export --agent gemini-cli` |
| **OpenCode** | CLI/MCP projection | `python scripts/nui-agent-export --agent opencode` |
| **Cursor** | Repository guidance + MCP/CLI | `python scripts/nui-agent-export --agent cursor-compatible` |
| **VS Code / Copilot-compatible Agent** | Repository guidance + MCP/CLI | `python scripts/nui-agent-export --agent vscode-agent-compatible` |
| **任意 MCP Host** | 本地 NUI MCP sidecar | `python scripts/nui-mcp-server` |
| **任意 Shell Agent** | Canonical skill + CLI | `python scripts/nui-agent-export --agent generic-cli` |

## 把 NUI 放进你自己的项目

不需要把数百个 skill 复制进一个巨型 system prompt。可以把 NUI 作为 sidecar 放在项目里：

```bash
git clone --depth 1 https://github.com/Nolane-x/Nolane-UI-Intelligence.git .nui
```

然后查看对应 projection：

```bash
python .nui/scripts/nui-agent-export --agent claude-code --root .nui
```

或者直接启动本地 MCP sidecar：

```bash
python .nui/scripts/nui-mcp-server --root .nui
```

请使用你的 Agent Host **当前版本的 MCP / project configuration 语法**注册这条命令。NUI 故意不把厂商配置格式写死进 cognition graph，因为 Codex、Claude、Gemini、编辑器 Agent 的接入语法可能比设计知识本身变化得更快。

> **权限边界：** Host 始终拥有最终权限控制。NUI 不会自行扩大 shell、filesystem、network、browser、image 或 MCP 权限。

完整的逐 Agent 接入指南：**[`docs/AGENT-INTEGRATION.md`](docs/AGENT-INTEGRATION.md)**。

---

## 为什么需要 NUI？

现在真正困难的已经不是“AI 能不能写 JSX / CSS”。

更常见的问题是：AI 可以生成技术上成立的界面，但它的**产品思考范围太小**。

例如：

- 一个销售管理平台只生成 Dashboard + Products + Orders；
- 一个专业编辑器有 canvas，却没有 inspector、history、asset workflow、command model 和 workspace persistence；
- 有登录，但没有 recovery、session/device、account lifecycle；
- Settings 只有几个 toggle，没有 scope、inheritance、search、reset 与 policy；
- desktop 很漂亮，但 mobile 只是把 desktop 压窄；
- 所有区域都变成圆角卡片，因为这是模型最容易生成的结构；
- 一个默认 scrollbar、select、date input 突然出现在精致界面中，破坏整个产品语言；
- 动效存在只是因为“高级产品应该有 animation”；
- Agent 看了一张自己生成的截图，就给自己判定“完成”。

NUI 把这些问题视为**设计认知失败**，而不仅仅是 CSS 小问题。

---

## NUI 的工作方式

与其给 Agent 一句：

```text
Make a beautiful modern premium UI.
```

NUI 更接近下面的生命周期：

```text
product truth
→ user / task / risk contract
→ capability discovery
→ specialist routing
→ information & interaction architecture
→ divergent visual directions
→ design system
→ implementation
→ real render
→ independent critique
→ repair / re-render
→ verification
→ bounded release claim
```

Agent 不应该一次性加载 774 个 skill。Router 会根据当前任务选择**最小但足够的 owner graph**。

---

## 774 个 canonical design faculties

NUI 当前保持 **774 个 canonical skills**。这个数字只是当前系统规模，不是制造重复 expert 的 KPI。长期 UI-industry roadmap 会继续朝约 1,000 个 canonical faculties 扩展，但每个新增 skill 仍必须拥有独立的 decision ownership，并保持最小充分路由。

只有当某个 skill 真正拥有独立的 decision class 或 failure class 时，它才应该存在。NUI 有意避免不断新增名称不同、职责重叠的“专家”。Batch 001 增加了 100 个独立编写的 specialist，覆盖 motion、rich controls、direct manipulation、spreadsheet/data、enterprise workflow、billing、scheduling、geospatial 和 historical state。Batch 002 再增加 100 个独立编写的 specialist，覆盖高摩擦输入、navigation/findability、feedback/recovery、messaging/collaboration、onboarding、commerce lifecycle、content publishing、developer operations 以及 trust/account lifecycle。Batch 003 再增加 100 个独立 specialist，覆盖 accessibility mechanics、globalization/locale、media playback、file/storage workflow 与 device/physical-world integration。Batch 004 再增加 200 个独立 specialist，覆盖 diagramming、project operations、incident response、software delivery、scientific instrumentation、3D/CAD、nonlinear media editing、digital learning、financial operations 与 security operations。Batch 005 再增加 100 个独立编写的 specialist，覆盖 mobile-native application shell、visual application builder、business intelligence、clinical care、public service、marketplace operations、realtime communications、spatial/XR、recommendation/personalization 与 design-to-code handoff。Batch 001–005 research record 保存完整 inventory、ownership、provenance 与 anti-generation 约束。

覆盖范围包括：

- product intent、user、job 与 capability modeling；
- information architecture 与 settings architecture；
- interaction states、rich components、direct manipulation；
- typography、color、spacing、surface、icon、visual hierarchy；
- semantic motion 与 reduced-motion equivalence；
- responsive、mobile、desktop、TV、XR、automotive、wearables；
- keyboard、touch、pen、remote、voice、gaze 等输入方式；
- accessibility、cognitive accessibility、screen reader、low vision、AAC；
- authentication、trust、privacy、financial、medical 等高影响领域；
- human-AI interaction、uncertainty、provenance、streaming、autonomous action；
- editor/canvas workspace 与 professional desktop workspace；
- external-source research 与 authority routing；
- visual media sourcing / authoring / integration；
- product closure 与 route/action reachability；
- rendered critique、adequacy critic、release verification；
- mutation、ablation 与 empirical evaluation。

Canonical bootstrap：

```text
skills/using-nolane-ui/SKILL.md
```

Canonical graph：

```text
skills/skill-graph.json
```

---

## Product Completeness：先想宽，再决定删什么

NUI 的一个核心原则：

> **先探索足够宽的产品能力空间，再有理由地缩小范围。**

Capability 会被明确 disposition 为：

```text
REQUIRED
EXPECTED
OPTIONAL
EXCLUDED
UNKNOWN
```

因此，“完整的销售管理平台”不能因为模型最先想到四个页面，就把那四个页面当成全部产品。Agent 应该主动考虑 account/workspace、role/permission、catalog/SKU、inventory、order lifecycle、fulfillment、returns/refunds、customer、payment、reporting、search、notification、import/export、integration、settings、audit/history、recovery 等合理能力。

但“考虑”并不等于全部强制实现。NUI 追求的是 **intentional scope**，而不是把所有应用都膨胀成 enterprise monster。

---

## 专业工具需要真正的 Instrument Architecture

对于 IDE、设计工具、视频/图像编辑器、运营工作台等产品，NUI 不把“功能多”理解成“按钮多”。它会分析类似下面的结构：

```text
workspace shell
→ modes / tools
→ selection model
→ primary work surface
→ context inspector
→ hierarchy / layers
→ assets / resources
→ command / search
→ history / undo / redo
→ import / export
→ collaboration
→ status / progress
→ persistence
```

完整性与 progressive disclosure 并不冲突。Command palette、keyboard path、contextual controls 和 density strategy 都属于设计本身。

---

## Flagship Visual Intelligence

对于 `flagship`、`exceptional`、`experiential` 级别的任务，NUI 不接受“premium / clean / modern”这种形容词堆叠作为视觉方向证据。

Agent 必须建立 visual thesis，并在收敛前探索真正不同的候选方向，例如在以下轴上产生实质差异：

- composition；
- type system；
- material system；
- signature mechanism。

之后才进入 attention hierarchy、typography、density/composition rhythm、color/material causality、motion、domain-native signature、reference frontier、generic-transfer resistance、responsive re-authoring 与 closed critique cycle。

NUI 不声称能数学证明“美”。它要做的是让一个“这是旗舰级设计”的声明**可以被证据推翻**。

---

## 先 Render，再批评用户真正看到的东西

NUI 区分 source/spec 与最终渲染结果：

```text
render
→ screenshot / runtime observation
→ hierarchy critique
→ typography / spacing / density critique
→ browser/platform residue audit
→ responsive critique
→ correction
→ re-render
→ A/B
```

这样可以捕捉只看代码看不到的问题：文字换行、意外 scrollbar、原生控件残留、optical alignment、媒体裁切、拥挤的 mobile state、不一致的 material，以及违背交互因果关系的 motion。

---

## 不让“老式默认控件”破坏高级界面

NUI 的 default-chrome audit 不只检查 scrollbar，还包括：

```text
scrollbar
select
file input
date/time input
number/range
focus / selection / caret
resize handle
drag ghost
native validation
context menu
tooltip / popover
cursor
overscroll
```

规则不是“全部自定义”。平台原生控件完全可能是正确选择。真正的问题是**无意的 residue、不一致，或者为了视觉而破坏 usability/accessibility 的自定义**。

---

## 学习 Reference，而不是复制产品

NUI 把优秀产品、design system、研究资料、UI library 当成**机制来源**，而不是视觉复刻目标。

```text
need
→ inspect current source
→ identify authority role
→ extract mechanism
→ define transfer boundary
→ adapt to product truth
→ verify local runtime
```

一个 reference 可以教会 Agent density zoning、typographic contrast、command architecture、motion continuity、material layering 或数据表达方式，但不会自动获得复制其品牌 trade dress 的权力。

---

## V10 — Behavioral Design Intelligence & Empirical Proof

V10 在“系统结构是否足够深”之外再问一层：

> **使用 NUI，是否真的会让 AI Agent 的行为朝预期方向改变？**

当前 V10 evaluation plane 包括：

- **13 个 falsifiable behavioral hypotheses**；
- **48 个 benchmark tasks / 12 个 task families**；
- public-generation 与 evaluator-hidden boundary；
- mutation、targeted ablation、placebo control；
- model/runtime/prompt/tool-budget provenance；
- blind pairwise judging；
- matched comparison units；
- exact statistical gates；
- bounded claim promotion。

NUI 不把所有维度压成一个“总分”。Product completeness 可能提升，而其他维度没有提升——这种 trade-off 应该被保留下来。

普通 repository CI 目前仍然只有 **structural evidence ceiling**。Synthetic fixture 不会被包装成“已经证明 NUI 在所有真实模型上更强”。

---

## NUI 不是什么

NUI 不是：

- React component library；
- Tailwind preset；
- Figma kit；
- 一个万能 system prompt；
- trendy screenshot 收藏；
- 自动 accessibility certification；
- 绝对 beauty-score 函数；
- 复制 Apple、Linear、Stripe、Canva、CapCut、VS Code 的许可；
- “只要安装就能保证所有 AI 输出都是顶级设计”的承诺。

NUI 是一次构建 **AI Agent Design Cognition Layer** 的尝试，并且让这个认知层能够被路由、观察、批评和测试。

---

## Repository Map

```text
skills/                         374 canonical faculties
skills/skill-graph.json        routing / ownership graph
knowledge/                     authority, ontology, benchmark, evidence
schemas/                       typed evidence contracts
src/nolane_ui/                 deterministic kernels
evals/                         adversarial / behavioral fixtures
benchmarks/v10/                V10 benchmark corpus
.agents/skills/nolane-ui/      Codex / Agent Skills bridge
.claude/skills/nolane-ui/      Claude Code bridge
scripts/nui-agent-export       agent projection CLI
scripts/nui-mcp-server         local MCP entry point
docs/AGENT-INTEGRATION.md      完整 Agent 接入指南
```

---

## 验证仓库

```bash
python -m unittest discover -s tests -v
python scripts/nui-validate .
```

Repository validator 证明当前 revision 的 structural / evidence-contract invariants。它不会自动证明未来每个 UI 都美观、可用、可访问、合法或 empirically superior。

---

## License

MIT。见 [`LICENSE`](LICENSE)。

---

<div align="center">

### AI 已经学会生成 UI。
### Nolane UI Intelligence 想让它进一步学会 **设计、观察并证明自己的 UI**。

**开始：** [`skills/using-nolane-ui/SKILL.md`](skills/using-nolane-ui/SKILL.md) · **接入 AI Agent：** [`docs/AGENT-INTEGRATION.md`](docs/AGENT-INTEGRATION.md)

</div>