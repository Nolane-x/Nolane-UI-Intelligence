<div align="center">

# Nolane UI Intelligence

### 面向 AI Agent 的设计认知与验证系统

**AI 已经可以在几秒钟内生成界面。NUI 想解决的是更难的一层：让 AI 理解这个界面为什么存在、什么绝不能丢失、它应该呈现怎样的体验，以及在宣称“设计完成”之前究竟需要什么证据。**

[English](README.md) · [Tiếng Việt](README-VN.md) · [简体中文](README-CN.md)

`v0.10.0` · `174 个 canonical skills` · `证据门控` · `跨平台` · `MIT`

</div>

---

## 今天真正困难的，已经不是“AI 能不能写 UI”

现代模型可以快速生成页面、Dashboard、应用、组件、动画，甚至完整前端。

真正困难的是 **代码出现之前和之后发生的事情**：

- 模型真的理解产品了吗，还是把需求压进了一个熟悉模板？
- 那些不适合做 Demo、却决定产品是否完整的能力有没有被悄悄删掉？
- 专业工具有没有再次变成一堆巨大卡片？
- “高级感”是不是又被简化成深色背景、Blur、Glass 和 Gradient？
- Mobile 是真正重构过的信息与操作结构，还是 Desktop 的纵向堆叠？
- Motion 在解释状态和因果，还是只是在制造动效？
- Accessibility、权限、恢复、信任与平台行为有没有在视觉优化之后继续成立？
- Critic 真的看过最终 Render，还是只是复述设计理由？
- 当系统声称“这个 skill 让模型设计得更好”时，**证据在哪里？**

**Nolane UI Intelligence（NUI）** 就是为这一层而设计的。

它不是组件库，不是视觉风格包，也不是一个超长的“帮我做得更漂亮”Prompt。NUI 是一套 **供 AI Agent 使用的结构化 Design Intelligence System**：由专业 decision owners、路由规则、evidence contracts、独立 critics、研究 provenance、确定性 validators，以及 V10 的实验评估机制共同组成。

它试图完成一件很难、但可以清楚描述的事情：

> **把 UI 生成从一次性模仿，变成产品理解、设计分歧、实现、真实渲染审查、恢复与证据约束发布的完整过程。**

---

## NUI 如何改变 Agent 的设计流程

没有设计认知层时，Agent 很容易形成这样的循环：

`需求 → 熟悉模板 → 写代码 → “看起来不错” → 完成`

NUI 使用一条可观察的生命周期替代它：

```text
INTAKE
  ↓
CONTRACTED
  ↓
ROUTED
  ↓
DISCOVERED
  ↓
ARCHITECTED
  ↓
DIVERGED
  ↓
DESIGN_SELECTED
  ↓
SYSTEMIZED
  ↓
SPECIFIED
  ↓
IMPLEMENTABLE
  ↓
RENDERED
  ↓
CRITIQUED
  ↓
VERIFIED
  ↓
RELEASED
```

任何未解决的 obligation、过期 source、遗漏 capability、错误的视觉方向、runtime defect 或越界 claim，都可以把系统送回 `RECOVERY`，或者停在 `BLOCKED`。

这里最重要的不是流程图本身，而是**不同阶段拥有不同的判断权**。

Product intent 不能过早退化成 layout。Aesthetic exploration 不能在第一个流行方案上停止。Compile success 不能替代 visual verification。生成者不能悄悄成为自己作品的唯一裁判。

---

## 174 个 Skills，但只有一个 Canonical Graph

当前 NUI 保留 **174 个 canonical skills**。

这个数字不是 KPI，也不是建议一次性塞进 Context 的 Prompt 数量。`routing-ui-work` 会根据真实任务，只激活 **最小但充分的 skill graph**。

Marketing Site、视频编辑器、金融控制台、医疗系统、TV UI、AAC 沟通界面、AI Agent Workspace 和 Flight Deck，本来就不应该使用完全相同的设计上下文。

NUI 的能力范围包括但不限于：

- Product intent、capability modeling、scope 与 product completeness；
- 用户、任务、expertise、error cost 与 human factors；
- Information architecture、navigation 与 settings architecture；
- Interaction、state、form、search、table 与高密度工作流；
- Web、mobile、desktop、foldable、TV、wearable、automotive、XR、terminal、kiosk 等平台；
- Keyboard、pointer、touch、pen、remote、voice、gaze、haptics 与 alternative input；
- Accessibility、cognitive access、low vision、screen reader、reduced motion、AAC 与 accessible media；
- Human-AI interaction、uncertainty、agent autonomy、generative UI 与 multi-agent surfaces；
- Authentication、permission、privacy、finance、medical 与高后果界面；
- Typography、color、spacing、composition、material、imagery、motion 与 visual hierarchy；
- Editor/canvas、professional workspace、command systems 与 rich interaction；
- Design token、component architecture、design system 与 implementation fidelity；
- Source authority、repository archaeology、外部 UI ecosystem 与 integration audit；
- 独立的 visual、UX、accessibility、safety、platform、resilience 与 fidelity critics。

一个新 skill 只有在它拥有真正独立的 **decision boundary 或 failure class** 时才值得加入。NUI 后续版本刻意优先深化已有 owner，而不是通过复制近似 skill 来膨胀数量。

---

## Flagship Visual Intelligence：美感不是一个 PASS 按钮

NUI 把视觉野心当作真实 contract，而不是一句形容词。

对于 `flagship`、`exceptional` 或 `experiential` 级别的工作，一个漂亮 Hero Screenshot 远远不够。系统需要看到：视觉方向确实经历过探索、分歧、选择和压力测试。

### 至少三个真正不同的方向

候选方案必须在 **composition、typography、material language、signature mechanism** 等核心机制上产生明显差异。换一套颜色不能算第二个方向。

### Generic-transfer resistance

隐藏品牌名和 Logo。如果同一个 authored shell 可以几乎无损地套到十几个无关 SaaS 上，那么产品 identity 仍然是 generic 的。

### Attention architecture

界面要明确用户首先、其次、第三应该看到什么。所有区域都“很精致、很抢眼”，通常意味着 hierarchy 根本没有建立起来。

### Domain-native signature

真正值得记住的设计，应该从产品对象、工作流、数据、工具、交互或领域本身长出来，而不是依赖无意义的发光球体和装饰几何。

### Responsive art direction

Mobile 不等于把 Desktop 卡片竖起来。当任务结构改变时，composition 也应该重写，而不仅是缩小。

### Closed critique cycles

重要 visual finding 必须经过 **修复 → 重新 Render → 在明确 evidence 中再次观察**。只写一段正确的 critique 但不改变设计，不算闭环。

因此 NUI 不提供一个万能的“Beauty Score”。Taste 是比较性的、上下文相关的，并且必须落在可观察 evidence 上。Product truth、accessibility 和 interaction correctness 仍然是不可被视觉分数抵消的 hard boundaries。

---

## Product Completeness 先于 Screen Completeness

一个 UI 可以内部逻辑完整，却仍然代表一个**从最初建模阶段就被缩小过头的产品**。

NUI 因此把 **discovery breadth** 与 **implementation commitment** 分开。对于高 ambition 产品，在压缩成 routes 和 screens 之前，合理的 capability families 需要先被发现，并明确归类为：

`REQUIRED · EXPECTED · OPTIONAL · EXCLUDED · UNKNOWN`

这样，一个号称“完整平台”的产品就不能因为模型最先想到 Dashboard、Items、Settings，就悄悄停在这三个页面。

但广泛 discovery 也不意味着所有小工具都要被强行企业化。Scope 仍然要由 actor、outcome、lifecycle、consequence 与产品 ambition 决定。

对于 editor 和 professional tools，NUI 还会进一步检查 workspace region、selection、inspector、command、history、asset/resource、status、import/export、collaboration 与 persistence。**完整性意味着能力真实存在并且可达，而不是把所有按钮同时摆在屏幕上。**

---

## 可以学习优秀产品，但不把自己变成复制机器

NUI 可以参考平台规范、Design Systems、Component Libraries、Research、成熟产品和外部工具链，但它明确区分：

**能访问某个 Source ≠ 这个 Source 对所有设计决策都有 Authority。**

一个项目很知名、GitHub Stars 很高、视觉很漂亮、有 MCP、有 Agent Docs，都不能自动获得全局设计权。

NUI 按 decision dimension 分配 authority。Platform guide 可以主导 platform conventions；headless primitive 可以提供 semantic/state mechanics；motion engine 可以负责 interpolation mechanics；优秀视觉产品可以提高 composition 的参考标准。但这些 source 不能越界替代 product strategy、local accessibility proof 或产品自身 visual identity。

核心 transfer 原则是：

> **迁移机制，而不是复制 Trade Dress。**

任何重要的外部影响，都应该记录 provenance、source role、license posture、transfer boundary、contraindication 与 local verification。只读 README 就把模式带进 production，不被视为 deep research。

---

## V10：从“看起来很聪明的规则”走向可证伪的设计智能

V10 是 NUI 非常关键的一次变化：

**一个 skill 不再因为文字写得长、逻辑听起来漂亮，就被视为“有深度”。它必须能够改变行为，而且系统必须能够发现它没有产生预期效果的情况。**

V10 的评估层目前包含：

- **13 个可证伪 behavioral hypotheses**；
- **48 个原创 benchmark tasks**，覆盖 **12 个 task families**；
- public generation 与 hidden evaluator 的隔离；
- 面向 transfer 的 holdout tasks；
- targeted semantic mutations、ablations 与 placebo controls；
- blinded pairwise judging；
- provider、model family、model、snapshot、runtime 与 artifact 级 run provenance；
- canonical SHA-256 experimental identity；
- matched-pair aggregation 与 uncertainty-aware statistics；
- hard-blocker regression gates；
- 有边界的 claim promotion：`STRUCTURAL_ONLY`、`EMPIRICAL_LOCAL`、`EMPIRICAL_TRANSFER` 或 `REJECTED`。

最重要的区分是：

```text
一个 artifact 很优秀 ≠ 已经证明 NUI 导致了这个提升
```

优秀 UI 能证明这个 UI 本身优秀，却不能自动证明某一个 NUI skill 让模型能力提升。

如果要做 efficacy claim，V10 要求更完整的 evidence lineage：真实且通过验证的 runs、matched treatment pairs、blind judgments、bundle digests、targeted ablations，以及有边界的统计证据。一个 JSON 字段 `real_model_runs: true` 没有权力自己把 claim 升级。

### 当前 Claim Ceiling

仓库的普通 CI 和内置 structural fixtures 当前验证的是 **NUI 的评估框架与结构约束**，并不自动证明“所有模型用了 NUI 都会设计得更好”。

因此默认 claim ceiling 仍然是：

**`STRUCTURAL_ONLY`**

只有真实 provider/model run bundle 通过 V10 的完整 gate 后，才有资格提升为 `EMPIRICAL_LOCAL` 或 `EMPIRICAL_TRANSFER`。

这不是保守营销，而是项目刻意拒绝用 synthetic benchmark 给自己制造科学感。

---

## NUI 不是什么

NUI 不是：

- UI component kit；
- Figma 替代品；
- Palette / Font / Template 合集；
- 应该粘贴进每个对话的 Mega Prompt；
- 可以计算“客观美感”的 Oracle；
- 自动保证每个 AI UI 都 accessible、安全、production-ready 的证书；
- 用来复制 Apple、Linear、Stripe、Notion、Canva、VS Code 等产品的工具；
- 把单一 Benchmark Score 包装成 Design Intelligence 的系统。

NUI 更接近一层关于 **reasoning、routing、design decisions、criticism、evidence 与 recovery** 的基础设施。

---

## Repository 结构

```text
Nolane-UI-Intelligence/
├── skills/                 # canonical design cognition graph
│   └── skill-graph.json    # ownership / parent / output
├── knowledge/              # authority、research、design 与 evidence memory
├── benchmarks/v10/         # public tasks、hidden evaluator data、mutations
├── evals/                  # adversarial / behavioral pressure tests
├── schemas/                # typed evidence contracts
├── src/nolane_ui/          # deterministic validators & reasoning kernels
├── scripts/                # validation / release / V10 empirical tooling
├── adapters/               # Agent 与 runtime capability mappings
├── docs/                   # architecture / research / run protocols
└── tests/                  # behavior / repository / mutation / claim gates
```

所有 material UI/UX 工作的 canonical entry point 是：

`skills/using-nolane-ui/SKILL.md`

它会把任务交给 `nolane-ui`，再由 `routing-ui-work` 选择真正需要的 faculties。**不要把 174 个 skills 一次性全部塞进 Context。** Progressive disclosure 本身就是 NUI 架构的一部分。

---

## Quick Start

验证 repository：

```bash
PYTHONPATH=src python scripts/nui-validate .
```

运行完整 test suite：

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

开始 V10 controlled evaluation：

```bash
python scripts/nui-v10-build-run-matrix examples/v10/experiment.example.json
python scripts/nui-v10-validate-run-bundle <manifest.json> <runs.jsonl>
python scripts/nui-v10-aggregate <runs.jsonl>
```

在解释任何 efficacy result 之前，请先阅读 `docs/V10-EMPIRICAL-RUN-PROTOCOL.md`。

---

## NUI 的十条核心原则

1. **Product truth 优先于 visual polish。**
2. **第一个合理 UI 是 hypothesis，不是答案。**
3. **高视觉 ambition 必须先 divergence，再 refinement。**
4. **熟悉的交互可以和独特的视觉 identity 共存。**
5. **缺失 evidence 必须保持 `UNKNOWN/BLOCKED`，不能变成 `PASS`。**
6. **Generator 不能静默地成为自己的最终裁判。**
7. **用户看到的是 Render，不是 Source Code。**
8. **Authority 属于具体 decision dimension，而不是属于名气。**
9. **Skill 的深度来自它能改变决策、捕获 failure，而不是文字长度。**
10. **关于“提升”的 claim 必须来自 controlled evidence，而不是 confidence。**

---

## Research 与 Provenance

NUI 会从平台指导、Accessibility Standards、Human Factors、成熟 Design Systems、Implementation Ecosystems 以及 Agent Design Research 中提取机制，但始终保留 source role 与 reuse boundary。

详细 provenance 位于 `docs/research/SOURCES.md`，机器可读 source ledgers 位于 `knowledge/`。

项目不会批量复制第三方 skill prose、专有设计数据库，也不会把其他产品可识别的 visual trade dress 直接变成模板。高 drift source 在发生变化时可以重新打开 research wave。

---

## 为什么做这个项目？

AI-generated software 的未来，不会只属于“最会写 JSX 的模型”。

同样重要的是围绕模型的**认知环境**：它能否保护 product truth、暴露缺失 assumption、在正确时间调用正确专业知识、抵抗 generic attractors、理解风险、比较真正不同的方案、观察真实 Render、进行独立批评、从失败中恢复，并且知道什么时候证据还不足以宣称胜利。

**Nolane UI Intelligence 尝试构建的，就是这一层。**

它不是一个更漂亮的 Prompt。

而是一种让 AI 更严谨地学习“如何设计”的方式。

---

## License

MIT。详情见 `LICENSE`。
