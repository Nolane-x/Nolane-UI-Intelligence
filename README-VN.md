<div align="center">

# Nolane UI Intelligence

### Nhận thức thiết kế, độ đầy đủ sản phẩm, chất lượng thị giác và kiểm chứng bằng evidence cho AI Agent

**AI có thể tạo giao diện trong vài giây. NUI được xây để buộc AI suy nghĩ như một đội product + design nghiêm túc trước khi dám giao nó cho người dùng.**

[English](README.md) · [Tiếng Việt](README-VN.md) · [简体中文](README-CN.md)

`v0.10.0` · `774 skill chuẩn` · `9 agent projection` · `MCP + CLI` · `evidence-gated` · `MIT`

</div>

---

## Mô tả

**Nolane UI Intelligence (NUI)** là một hệ thống nhận thức thiết kế và kiểm chứng UI/UX mã nguồn mở dành cho AI coding agent. NUI cung cấp cho agent một đồ thị skill được định tuyến theo nhiệm vụ: từ hiểu sản phẩm, người dùng, information architecture, interaction, typography, motion, accessibility, authentication, settings, professional workspace, product completeness cho tới render critique, design-to-code fidelity và empirical evaluation.

NUI **không phải** component library, bộ style preset, mega-prompt, công cụ chép screenshot hay một “điểm đẹp” duy nhất. Mục tiêu của nó là làm cho quyết định thiết kế trở nên **rõ ràng, có owner, có thể phản biện, có thể kiểm chứng và có giới hạn claim**.

### Tags / chủ đề

`ai-agents` · `agent-skills` · `ui-ux` · `design-intelligence` · `design-system` · `frontend` · `codex` · `claude-code` · `gemini-cli` · `opencode` · `cursor` · `vscode` · `mcp` · `accessibility` · `human-computer-interaction` · `ai-coding`

---

# Dùng NUI với AI agent của bạn

NUI được thiết kế để dùng với **Codex, Claude Code, Google Antigravity, Gemini CLI, OpenCode, Cursor, VS Code/Copilot-compatible agents, mọi MCP host và các AI agent có shell/CLI** mà không phải tạo chín bản copy của cùng một bộ skill.

Kiến trúc cốt lõi:

```text
một NUI cognition graph chuẩn
            ↓
      bridge mỏng theo host
            ↓
Codex / Claude / Gemini / OpenCode / Cursor / VS Code / MCP / CLI
```

## Cài nhanh

```bash
git clone https://github.com/Nolane-x/Nolane-UI-Intelligence.git
cd Nolane-UI-Intelligence
```

Xem plan tích hợp dành cho agent của bạn:

```bash
python scripts/nui-agent-export --agent openai-codex
```

Các adapter ID đang được hỗ trợ thật trong repo:

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

### Bảng tích hợp agent

| Agent / host | Cách NUI đề xuất | Đường vào |
|---|---|---|
| **Codex** | Agent Skills bridge + repository policy | `.agents/skills/nolane-ui/SKILL.md` + `python scripts/nui-agent-export --agent openai-codex` |
| **Claude Code** | Project skill bridge | `.claude/skills/nolane-ui/SKILL.md` + `python scripts/nui-agent-export --agent claude-code` |
| **Google Antigravity** | Agent Skills bridge hoặc MCP | `python scripts/nui-agent-export --agent google-antigravity` |
| **Gemini CLI** | CLI/MCP projection | `python scripts/nui-agent-export --agent gemini-cli` |
| **OpenCode** | CLI/MCP projection | `python scripts/nui-agent-export --agent opencode` |
| **Cursor** | Repository guidance + MCP/CLI | `python scripts/nui-agent-export --agent cursor-compatible` |
| **VS Code / Copilot-compatible agent** | Repository guidance + MCP/CLI | `python scripts/nui-agent-export --agent vscode-agent-compatible` |
| **Mọi MCP host** | Local NUI MCP sidecar | `python scripts/nui-mcp-server` |
| **Mọi agent có shell** | Canonical skill + CLI | `python scripts/nui-agent-export --agent generic-cli` |

## Gắn NUI vào một project khác

Không cần chép hàng trăm skill vào prompt. Có thể giữ NUI dưới dạng sidecar trong project:

```bash
git clone --depth 1 https://github.com/Nolane-x/Nolane-UI-Intelligence.git .nui
```

Sau đó xem projection cho agent:

```bash
python .nui/scripts/nui-agent-export --agent claude-code --root .nui
```

hoặc chạy NUI như một MCP sidecar local:

```bash
python .nui/scripts/nui-mcp-server --root .nui
```

Hãy đăng ký command trên bằng **cú pháp MCP/project config hiện tại của host**. NUI cố ý không hard-code config vendor vào cognition graph vì syntax của Codex/Claude/Gemini/editor có thể thay đổi nhanh hơn chính kiến thức thiết kế.

> **Ranh giới quyền:** host vẫn là authority. NUI không tự mở rộng quyền shell, filesystem, network, browser, image hay MCP.

Hướng dẫn đầy đủ theo từng agent nằm ở **[`docs/AGENT-INTEGRATION.md`](docs/AGENT-INTEGRATION.md)**.

---

## Vì sao NUI tồn tại?

Vấn đề khó bây giờ không còn là “AI có viết được JSX/CSS không?”.

Một AI có thể tạo code hợp lệ nhưng vẫn **nghĩ quá gọn**:

- web quản lý bán hàng chỉ có Dashboard + Products + Orders;
- editor có canvas nhưng thiếu inspector, history, asset flow, command system và workspace persistence;
- login có nhưng recovery, device/session, account lifecycle không có;
- Settings chỉ là vài toggle;
- desktop đẹp nhưng mobile chỉ là desktop bị bóp nhỏ;
- mọi vùng đều thành rounded card vì đó là cấu trúc dễ sinh nhất;
- một scrollbar/select/date input mặc định phá hỏng toàn bộ phong cách;
- animation có mặt chỉ vì “premium app thì phải có motion”;
- agent nhìn screenshot do chính nó tạo rồi tự tuyên bố “xong”.

NUI coi những trường hợp đó là **lỗi nhận thức thiết kế**, không đơn thuần là lỗi CSS.

---

## Cách NUI suy nghĩ

Thay vì một prompt như:

```text
Hãy làm UI thật đẹp, hiện đại và premium.
```

NUI đưa agent vào một lifecycle gần với:

```text
product truth
→ user / task / risk contract
→ capability discovery
→ specialist routing
→ information & interaction architecture
→ divergent visual directions
→ design system
→ implementation
→ render thật
→ critique độc lập
→ sửa / render lại
→ verification
→ bounded release claim
```

Agent không tải toàn bộ 774 skill. Router chọn **graph owner nhỏ nhất nhưng đủ** cho nhiệm vụ hiện tại.

---

## 774 design faculties chuẩn

NUI hiện giữ **774 canonical skills**. Con số hiện tại chỉ mang tính mô tả, không phải giấy phép để tạo các expert trùng nhau. Roadmap dài hạn hướng tới độ phủ toàn ngành UI ở mức khoảng 1.000 canonical faculties nhưng vẫn giữ decision ownership riêng biệt và routing tối thiểu.

Một skill chỉ nên tồn tại khi nó sở hữu một loại quyết định hoặc failure class riêng. Hệ thống cố tình chống lại việc tạo hàng chục “expert” gần giống nhau. Batch 001 bổ sung 100 specialist được viết độc lập về motion, rich controls, direct manipulation, spreadsheet/data, enterprise workflow, billing, scheduling, geospatial và historical state. Batch 002 bổ sung thêm 100 specialist được viết độc lập về input có ma sát cao, navigation/findability, feedback/recovery, messaging/collaboration, onboarding, commerce lifecycle, content publishing, developer operations và trust/account lifecycle. Batch 003 thêm 100 specialist độc lập về accessibility mechanics, globalization/locale, media playback, file/storage và tích hợp thiết bị/thế giới vật lý. Batch 004 thêm 200 specialist độc lập về diagramming, project operations, incident response, software delivery, scientific instrumentation, 3D/CAD, nonlinear media editing, digital learning, financial operations và security operations. Batch 005 thêm 100 specialist được viết độc lập về mobile-native application shell, visual application builder, business intelligence, clinical care, public service, marketplace operations, realtime communications, spatial/XR, recommendation/personalization và design-to-code handoff. Inventory, ownership, provenance và ràng buộc chống sinh lặp được lưu trong các research record Batch 001–005.

Các nhóm lớn bao gồm:

- product intent, users, jobs, capability modeling;
- information architecture và settings architecture;
- interaction state, rich component, direct manipulation;
- typography, color, spacing, surface, icon, hierarchy;
- semantic motion và reduced-motion equivalence;
- responsive, mobile, desktop, TV, XR, automotive, wearables;
- keyboard, touch, pen, remote, voice, gaze;
- accessibility, cognitive accessibility, screen reader, low vision, AAC;
- authentication, trust, privacy, financial, medical và các domain high-impact;
- human-AI interaction, uncertainty, provenance, streaming, autonomous action;
- editor/canvas workspace, desktop professional workspace;
- external source research và authority routing;
- visual media sourcing/authoring/integration;
- product closure và route/action reachability;
- rendered critique, adequacy critic và release verification;
- mutation, ablation và empirical evaluation.

Bootstrap chuẩn:

```text
skills/using-nolane-ui/SKILL.md
```

Graph chuẩn:

```text
skills/skill-graph.json
```

---

## Product completeness: nghĩ rộng trước, thu gọn sau

Một nguyên tắc quan trọng của NUI:

> **Luôn khám phá phạm vi đủ rộng trước khi quyết định bỏ bớt.**

Capability có thể được disposition thành:

```text
REQUIRED
EXPECTED
OPTIONAL
EXCLUDED
UNKNOWN
```

Vì vậy một “full sales management platform” không được phép dừng ngay ở bốn màn hình đầu tiên chỉ vì AI nghĩ ra chúng trước. Agent phải xem xét những capability hợp lý như account/workspace, roles/permissions, catalog/SKU, inventory, order lifecycle, fulfillment, returns/refunds, customer, payment, reporting, search, notifications, import/export, integrations, settings, audit/history và recovery.

Nhưng “xem xét” **không đồng nghĩa bắt buộc triển khai hết**. NUI tìm kiếm intentional scope, không ép mọi sản phẩm thành enterprise monster.

---

## Professional tool phải có kiến trúc công cụ thật

Đối với IDE, editor, design tool, media tool hoặc operations workspace, NUI suy nghĩ bằng **instrument architecture**:

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

Đầy đủ không có nghĩa hiển thị hết mọi button. Progressive disclosure, command palette, keyboard path, context action và density vẫn phải được thiết kế.

---

## Flagship visual intelligence

Với ambition `flagship`, `exceptional` hoặc `experiential`, NUI không chấp nhận một danh sách tính từ “premium / clean / modern” như art direction.

Agent phải có visual thesis và khám phá các candidate **thật sự khác nhau** về:

- composition;
- type system;
- material system;
- signature mechanism.

Sau đó mới hội tụ và kiểm tra attention hierarchy, typography, density/composition rhythm, color-material causality, motion, product-native signature, reference frontier, generic-transfer resistance, responsive re-authoring và critique loop.

NUI không tuyên bố toán học hóa vẻ đẹp. Nó làm cho **claim về chất lượng cao có thể bị bác bỏ** nếu evidence không đủ.

---

## Render rồi mới được critique

NUI phân biệt thiết kế trên giấy với kết quả người dùng thật sự nhìn thấy:

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

Nhờ vậy agent có thể bắt những lỗi mà đọc source không thấy: text wrapping, scrollbar lạc tông, focus/native chrome, optical alignment, crop, cramped mobile state, material inconsistency và motion sai causality.

---

## Không để “UI mặc định cổ điển” lọt vào một sản phẩm đẹp

NUI audit nhiều default-chrome class, không chỉ scrollbar:

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

Nguyên tắc không phải “custom tất cả”. Native đúng platform có thể là lựa chọn tốt. Lỗi nằm ở **residue vô tình**, inconsistency hoặc custom sai làm mất khả năng sử dụng/accessibility.

---

## Học reference mà không copy

NUI dùng các sản phẩm, design system, research và UI library như nguồn học **mechanism**, không phải mẫu để chép trade dress.

Flow:

```text
need
→ inspect current source
→ identify authority role
→ extract mechanism
→ define transfer boundary
→ adapt to product truth
→ verify local runtime
```

Một reference có thể dạy density zoning, typography contrast, command architecture, motion continuity hay material layering. Nó không tự trở thành quyền để sao chép phong cách nhận diện của sản phẩm đó.

---

## V10 — Behavioral Design Intelligence & Empirical Proof

V10 thêm một câu hỏi khó hơn:

> **NUI có thật sự làm AI thay đổi hành vi theo chiều đúng hay không?**

V10 hiện có:

- **13 falsifiable behavioral hypotheses**;
- **48 benchmark tasks / 12 task families**;
- public-generation và evaluator-hidden boundary;
- mutation, targeted ablation, placebo control;
- provenance cho model/runtime/prompt/tool budget;
- blind pairwise judging;
- matched comparison units;
- exact statistical gates;
- bounded claim promotion.

Không có một “NUI score” duy nhất. Nếu product completeness tăng nhưng một chiều khác không tăng, kết quả phải thể hiện điều đó.

CI repo hiện vẫn giữ **structural evidence ceiling**; NUI không dùng synthetic fixture để tự quảng cáo rằng nó đã được empirical prove trên mọi model.

---

## NUI không phải là gì?

NUI không phải:

- React component library;
- Tailwind preset;
- Figma kit;
- một system prompt duy nhất;
- bộ screenshot trend;
- máy tự cấp chứng chỉ accessibility;
- hàm tính beauty score tuyệt đối;
- giấy phép copy Apple/Linear/Stripe/Canva/CapCut/VS Code;
- bảo đảm mọi output của AI tự động thành tuyệt phẩm.

NUI là một nỗ lực xây **design cognition layer bao quanh AI agent**, sau đó làm lớp nhận thức đó có thể định tuyến, quan sát, phản biện và kiểm thử.

---

## Cấu trúc repo

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
docs/AGENT-INTEGRATION.md      hướng dẫn tích hợp agent đầy đủ
```

---

## Kiểm chứng repository

```bash
python -m unittest discover -s tests -v
python scripts/nui-validate .
```

Validator chứng minh structural/evidence-contract invariants của revision đang kiểm tra. Nó không tự chứng minh mọi UI tương lai sẽ đẹp, usable, accessible, lawful hay empirically superior.

---

## License

MIT. Xem [`LICENSE`](LICENSE).

---

<div align="center">

### AI đã biết sinh UI.
### Nolane UI Intelligence cố gắng dạy nó **thiết kế, quan sát và chứng minh** UI đó.

**Bắt đầu:** [`skills/using-nolane-ui/SKILL.md`](skills/using-nolane-ui/SKILL.md) · **Cài cho AI agent:** [`docs/AGENT-INTEGRATION.md`](docs/AGENT-INTEGRATION.md)

</div>