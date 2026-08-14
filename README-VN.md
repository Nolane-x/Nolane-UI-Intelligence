<div align="center">

# Nolane UI Intelligence

### Hệ thống nhận thức thiết kế và kiểm chứng UI dành cho AI Agent

**AI có thể dựng một giao diện trong vài giây. NUI được tạo ra để khiến AI hiểu vì sao giao diện đó phải tồn tại, điều gì không được phép đánh mất, nó nên tạo cảm giác gì — và cần bằng chứng nào trước khi dám gọi nó là tốt.**

[English](README.md) · [Tiếng Việt](README-VN.md) · [简体中文](README-CN.md)

`v0.10.0` · `174 skill chuẩn` · `evidence-gated` · `đa nền tảng` · `MIT`

</div>

---

## Bài toán bây giờ không còn là “AI có viết được UI hay không”

AI hiện đại có thể tạo page, dashboard, app, component, animation, thậm chí cả một frontend hoàn chỉnh với tốc độ đáng kinh ngạc.

Nhưng phần khó nhất lại nằm ở **trước và sau lúc code được sinh ra**.

AI có thực sự hiểu sản phẩm, hay chỉ ép yêu cầu vào một mẫu giao diện quen thuộc? Những capability quan trọng có bị mất vì chúng không “đẹp để demo” không? Một công cụ chuyên nghiệp có bị biến thành vài card khổng lồ? “Premium” có lại đồng nghĩa với nền tối + blur + gradient? Mobile có chỉ là desktop bị ép nhỏ? Motion có đang truyền đạt quan hệ và trạng thái, hay chỉ chuyển động cho vui? Accessibility, permission, recovery, trust và platform behavior có sống sót sau khi thiết kế trở nên đẹp hơn không?

Và còn một câu hỏi khó hơn:

> Khi một hệ thống tuyên bố “skill này giúp AI thiết kế tốt hơn”, **bằng chứng nào chứng minh điều đó?**

**Nolane UI Intelligence (NUI)** được xây dựng cho chính tầng vấn đề này.

NUI không phải UI kit. Không phải kho theme. Không phải một mega-prompt kiểu “hãy làm giao diện cực đẹp”. NUI là một **hệ thống design intelligence có cấu trúc dành cho AI Agent**: gồm graph các decision owner chuyên biệt, router, evidence contract, critic độc lập, provenance nghiên cứu, validator deterministic và bộ máy thực nghiệm để kiểm soát claim.

Mục tiêu của NUI có thể tóm lại trong một câu:

> **Biến việc tạo UI từ một cú bắt chước một lần thành một quy trình có kỷ luật: hiểu sản phẩm → khám phá → phân kỳ → thiết kế → triển khai → quan sát render thật → phản biện → sửa → kiểm chứng → mới được release.**

---

## NUI thay đổi cách AI thiết kế như thế nào?

Một agent không có tầng design cognition rất dễ rơi vào vòng lặp:

`prompt → pattern quen thuộc → code → “trông ổn” → xong`

NUI thay nó bằng lifecycle có trạng thái rõ ràng:

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

Nếu obligation thất bại, source bị stale, capability bị thiếu, thiết kế mắc trong một visual basin yếu, runtime có lỗi, hoặc claim vượt quá evidence, hệ thống có thể quay về `RECOVERY` hoặc dừng ở `BLOCKED`.

Điểm cốt lõi là: **mỗi giai đoạn được phép trả lời một loại câu hỏi khác nhau**.

Product intent không được phép biến thành layout quá sớm. Visual direction không được phép khóa vào phương án thời thượng đầu tiên. Compile thành công không được phép đóng vai bằng chứng thẩm mỹ. Một generator không được tự vừa tạo vừa lặng lẽ chứng nhận chính sản phẩm của nó.

---

## 174 skill — nhưng chỉ có một hệ thống

NUI hiện có **174 canonical skills**.

174 không phải con số để khoe và càng không phải số lượng context phải nạp vào mỗi task. Router `routing-ui-work` chỉ chọn **graph nhỏ nhất nhưng đủ** cho bài toán hiện tại.

Một landing page, một video editor, một financial console, một hệ thống y tế, một giao diện TV, một ứng dụng AAC, một workspace AI agent và một flight deck không thể bị suy nghĩ bằng cùng một bộ context.

Graph của NUI bao phủ nhiều tầng khác nhau, trong đó có:

- product intent, capability, product scope và completeness;
- user/task model, expertise, error cost và human factors;
- information architecture, navigation và settings architecture;
- interaction, state, form, search, table và data-dense workflow;
- web, mobile, desktop, foldable, TV, wearable, automotive, XR, terminal, kiosk và các surface chuyên biệt;
- keyboard, pointer, touch, pen, remote, voice, gaze, haptic và alternative input;
- accessibility, cognitive access, low vision, screen reader, reduced motion, AAC và accessible media;
- human-AI interaction, uncertainty, agent autonomy, generative UI và multi-agent surface;
- authentication, permissions, privacy, finance, medical và high-consequence UX;
- typography, color, spacing, composition, material, imagery, motion và visual hierarchy;
- editor/canvas, professional workspace, command system và rich interaction;
- design token, component architecture, design system và implementation fidelity;
- source authority, repository archaeology, external library và integration audit;
- các critic độc lập cho visual, UX, accessibility, safety, platform, resilience và fidelity.

Một skill mới chỉ đáng tồn tại khi nó sở hữu **một decision boundary hoặc failure class thực sự khác biệt**. NUI các đời sau cố tình ưu tiên đào sâu owner cũ thay vì sinh thêm skill gần giống nhau chỉ để tăng số lượng.

---

## Flagship Visual Intelligence: “đẹp” không phải một checkbox

NUI coi mức độ tham vọng thẩm mỹ là một contract thật.

Với `flagship`, `exceptional` hoặc `experiential`, một screenshot bóng bẩy là chưa đủ. AI phải chứng minh rằng visual direction đã được khám phá, phân kỳ và stress-test chứ không phải tình cờ rơi vào một mẫu đẹp quen thuộc.

### Ba hướng phải thực sự khác nhau

Ít nhất ba candidate phải khác đáng kể ở **composition, typography, material language và signature mechanism**. Đổi màu một layout không được tính là divergence.

### Generic-transfer test

Ẩn logo và tên sản phẩm. Nếu cùng một shell đó có thể gắn vào hàng chục SaaS không liên quan mà gần như không mất ý nghĩa, identity layer vẫn còn generic.

### Attention architecture

Thiết kế phải cho thấy mắt người nên hiểu gì thứ nhất, thứ hai, thứ ba. “Mọi thứ đều đẹp và đều nổi” thường có nghĩa là hierarchy đã thất bại.

### Domain-native signature

Memorability nên được sinh ra từ chính subject, workflow, dữ liệu, công cụ hoặc interaction của sản phẩm — không phải vài hình cầu phát sáng vô nghĩa đặt phía sau content.

### Responsive art direction

Mobile không phải desktop xếp dọc. Khi cấu trúc nhiệm vụ thay đổi, composition phải được re-author chứ không chỉ co nhỏ.

### Closed critique loop

Một finding quan trọng phải được **sửa rồi quan sát lại trong một render cụ thể**. Critique chỉ nói đúng mà không làm evidence thay đổi thì chưa đóng vòng lặp.

NUI vì vậy không sử dụng một “beauty score” toàn năng. Taste phải được so sánh theo ngữ cảnh và có bằng chứng. Product truth, accessibility và interaction correctness vẫn là hard boundary ngay cả khi một phương án khác trông “wow” hơn trong một bài preference test nông.

---

## Product completeness phải đi trước screen completeness

Một UI có thể cực kỳ logic bên trong chính nó nhưng vẫn đại diện cho **một sản phẩm bị cắt cụt ngay từ lúc model hóa**.

Vì vậy NUI tách **discovery breadth** khỏi **implementation commitment**. Trước khi một sản phẩm tham vọng bị nén thành route và screen, các capability family hợp lý phải được phát hiện và gán disposition rõ ràng:

`REQUIRED · EXPECTED · OPTIONAL · EXCLUDED · UNKNOWN`

Điều này ngăn một “full platform” vô tình biến thành Dashboard + Items + Settings chỉ vì đó là ba thứ đầu tiên AI nghĩ tới.

Nhưng broad discovery cũng không phải giấy phép biến mọi tool nhỏ thành enterprise suite. Scope vẫn phải đi theo actor, outcome, lifecycle, consequence và ambition thực tế.

Với editor và professional tool, NUI còn ép kiểm tra workspace region, selection, inspector, command, history, asset/resource, status, import/export, collaboration và persistence. **Completeness là capability có thật và reachable**, không phải việc bày toàn bộ control lên màn hình.

---

## Học từ hệ sinh thái UI mà không biến thành máy sao chép

NUI có thể học từ platform guideline, design system, component library, paper, production product và toolchain ngoài repo — nhưng nó tách rõ **khả năng truy cập source** khỏi **quyền lực của source**.

Một source nổi tiếng, đẹp, nhiều sao GitHub, có MCP hay có agent docs không vì thế mà trở thành authority cho mọi quyết định.

NUI chia authority theo dimension. Platform guide có thể là authority của platform convention. Headless primitive có thể mạnh về semantics và state. Motion engine có thể mạnh về interpolation. Một sản phẩm đẳng cấp có thể nâng chuẩn composition. Nhưng không source nào tự động được quyền quyết định product strategy, accessibility hay visual identity ở ngoài phạm vi của nó.

Nguyên tắc transfer là:

> **Học mechanism, không copy trade dress.**

Material influence từ source ngoài phải giữ provenance, source role, licensing posture, transfer boundary, contraindication và local verification. Đọc mỗi README rồi đem pattern vào production không được coi là deep research.

---

## V10: từ “skill nghe có vẻ thông minh” sang design intelligence có thể bị bác bỏ

V10 thay đổi một điều rất quan trọng:

**Một skill không còn được xem là sâu chỉ vì nó được viết dài, logic và thuyết phục. Nó phải có khả năng làm hành vi thay đổi — và hệ thống phải có cách phát hiện khi nó không làm được điều đó.**

Evaluation layer của V10 hiện có:

- **13 behavioral hypothesis có thể falsify**;
- **48 benchmark task gốc**, chia thành **12 task family**;
- boundary giữa public generation và hidden evaluator;
- holdout task cho transfer-sensitive evaluation;
- semantic mutation, targeted ablation và placebo control;
- blinded pairwise judging;
- run provenance gồm provider, model family, model, snapshot, runtime và artifact digest;
- canonical SHA-256 cho experimental identity;
- matched-pair aggregation và uncertainty-aware statistics;
- hard-blocker regression gate;
- claim promotion có giới hạn: `STRUCTURAL_ONLY`, `EMPIRICAL_LOCAL`, `EMPIRICAL_TRANSFER`, hoặc `REJECTED`.

Phân biệt quan trọng nhất là:

```text
artifact đẹp ≠ bằng chứng rằng NUI là nguyên nhân khiến artifact tốt hơn
```

Một UI xuất sắc chứng minh UI đó xuất sắc. Nó chưa tự động chứng minh một skill cụ thể đã cải thiện model.

Muốn claim efficacy, V10 đòi evidence lineage mạnh hơn: real validated runs, matched treatment pairs, blind judgment, bundle digest, targeted ablation và thống kê có giới hạn. Chỉ ghi `real_model_runs: true` trong JSON không có quyền nâng claim.

### Claim ceiling hiện tại

CI thông thường và fixture đi kèm repository hiện đang chứng minh **evaluation framework và structural invariants**, chứ chưa chứng minh một tuyên bố phổ quát kiểu “NUI làm mọi model thiết kế đẹp hơn”.

Vì vậy default claim ceiling vẫn là:

**`STRUCTURAL_ONLY`**

Muốn lên `EMPIRICAL_LOCAL` hay `EMPIRICAL_TRANSFER`, phải chạy real provider/model bundle và vượt đúng gate V10.

Đây không phải sự yếu đi của project. Đây là việc project **từ chối tự lừa mình bằng benchmark synthetic**.

---

## NUI không phải là gì?

NUI không phải:

- UI component kit;
- bản thay thế Figma;
- kho palette/font/template đẹp;
- một mega-prompt để dán vào mọi cuộc hội thoại;
- oracle có thể tính “độ đẹp khách quan”;
- giấy chứng nhận rằng mọi UI do AI sinh ra đều accessible, safe hoặc production-ready;
- công cụ để copy Apple, Linear, Stripe, Notion, Canva, VS Code hay bất kỳ sản phẩm nào khác;
- một benchmark score được gọi nhầm là design intelligence.

NUI là infrastructure cho **reasoning, routing, design decision, criticism, evidence và recovery**.

---

## Kiến trúc repository

```text
Nolane-UI-Intelligence/
├── skills/                 # canonical design cognition graph
│   └── skill-graph.json    # ownership, parent và output
├── knowledge/              # authority, research, design & evidence memory
├── benchmarks/v10/         # public tasks, hidden evaluator data, mutations
├── evals/                  # adversarial / behavioral pressure tests
├── schemas/                # typed evidence contracts
├── src/nolane_ui/          # deterministic validators & reasoning kernels
├── scripts/                # validation, release, empirical tooling
├── adapters/               # mapping cho agent/runtime
├── docs/                   # architecture, research, run protocol
└── tests/                  # behavioral, repository, mutation, claim gates
```

Entry point chuẩn cho material UI/UX task:

`skills/using-nolane-ui/SKILL.md`

Bootstrap này giao task cho `nolane-ui`, sau đó `routing-ui-work` chọn những faculty thực sự cần. **Không nạp cả 174 skill vào một context.** Progressive disclosure là một phần của kiến trúc, không phải tối ưu phụ.

---

## Chạy thử

Kiểm tra repository:

```bash
PYTHONPATH=src python scripts/nui-validate .
```

Chạy toàn bộ test suite:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

Bắt đầu với V10 controlled evaluation:

```bash
python scripts/nui-v10-build-run-matrix examples/v10/experiment.example.json
python scripts/nui-v10-validate-run-bundle <manifest.json> <runs.jsonl>
python scripts/nui-v10-aggregate <runs.jsonl>
```

Trước khi diễn giải bất kỳ efficacy result nào, đọc `docs/V10-EMPIRICAL-RUN-PROTOCOL.md`.

---

## 10 nguyên tắc thể hiện tinh thần của NUI

1. **Product truth đứng trước visual polish.**
2. **UI hợp lý đầu tiên chỉ là hypothesis, không phải đáp án.**
3. **Ambition cao phải divergence trước khi refinement.**
4. **Interaction quen thuộc vẫn có thể sống cùng identity khác biệt.**
5. **Thiếu evidence là `UNKNOWN/BLOCKED`, không phải `PASS`.**
6. **Generator không được lặng lẽ tự chứng nhận chính sản phẩm nó tạo.**
7. **Pixel cuối cùng người dùng nhìn thấy quan trọng; source code chưa phải interface cuối.**
8. **Authority là theo decision dimension, không phải theo độ nổi tiếng.**
9. **Skill sâu vì nó đổi quyết định và bắt được failure — không phải vì nó nhiều chữ.**
10. **Claim cải thiện phải có controlled evidence, không phải confidence.**

---

## Research & provenance

NUI tổng hợp mechanism từ platform guidance, accessibility standard, human-factors research, design system, implementation ecosystem và agent-design research nhưng luôn giữ source role và reuse boundary.

Provenance chi tiết nằm ở `docs/research/SOURCES.md` và các machine-readable ledger trong `knowledge/`.

Project chủ động không bulk-copy skill prose của bên thứ ba, không nhập proprietary design database, và không biến visual identity của sản phẩm khác thành template của mình. Source có độ drift cao có thể mở lại research wave khi guidance thay đổi.

---

## Vì sao dự án này tồn tại?

Tương lai của AI-generated software sẽ không chỉ thuộc về model viết được nhiều JSX nhất.

Nó còn phụ thuộc vào **môi trường nhận thức bao quanh model**: môi trường giữ product truth không bị rơi mất, phát hiện assumption còn thiếu, gọi đúng chuyên môn đúng lúc, chống generic attractor, hiểu risk, tạo phương án khác nhau, quan sát render thật, tự phản biện độc lập, quay lại sửa khi sai — và biết khi nào evidence vẫn chưa đủ để tuyên bố chiến thắng.

**Nolane UI Intelligence là một nỗ lực xây dựng chính tầng thiết kế đó.**

Không phải một prompt đẹp hơn.

Mà là một cách nghiêm túc hơn để AI học cách thiết kế.

---

## License

MIT. Xem `LICENSE` để biết chi tiết.
