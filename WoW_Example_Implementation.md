# Example Implementation: SCA Module 2 (MedComm) Agentic Transformation

> **What this is:** A concrete, stage-by-stage walkthrough of the WoW process applied to a real pilot. Read this to see exactly what each stage looks like in practice.

---

## Context

**Platform:** Scientific Content Automation (SCA) Module 2, informally called MedComm. Generates visual medical communications assets (slides, infographics, posters, emailers) from source documents.

**Current state:**
- 12-stage sequential prompt pipeline (Pre-1 through Stage 13) with 4 sub-stages in Stage 10
- Custom orchestration via Celery tasks (15 concurrent workers, Redis broker, 4-hour task timeout)
- Multi-provider LLM: Gemini 3 Pro + 2.5 Pro (content/layout), Claude Sonnet 3.7 via Bedrock (design/iteration)
- FastAPI backend, React frontend with in-browser JSX/Babel compilation
- PostgreSQL (SQLAlchemy reflection), S3 storage, Playwright screenshots, Adobe PDF generation

**Target state:**
- Agentic platform (Strands framework under evaluation)
- Prompts converted to versioned `skills.md` files
- Complex service logic converted to agent-callable tools
- Eval datasets for every pipeline stage (content + visual)
- Engineer + non-engineer collaboration per WoW process

**Why rearchitect:** Current orchestration pipeline is brittle — bugs are frequent and hard to trace due to complex inter-stage dependencies, custom Celery routing, and tightly coupled prompt logic. Extending to new asset types requires modifying multiple stages. Agentic architecture with clear skill boundaries, tool abstractions, and eval coverage should improve debuggability, quality, and scalability.

---

## STAGE 0: INTAKE & CLASSIFICATION

| # | Action Item | SCA/MedComm Implementation |
|---|-----------|---------------------------|
| 1 | Log the request | "Rearchitect SCA Module 2 with agentic principles to improve quality, debuggability, and scalability across asset types" |
| 2 | Classify engagement type | **Type A — New Product / Major Feature.** Fundamental rearchitecture, not an enhancement. All stages apply (0 through 5). |
| 3 | Assign STO | One person accountable end-to-end — the SA who understands both the current pipeline and the agentic target state |
| 4 | Identify applicable stages | All stages: 0 → 1 → 2 → 3 → 4 → 5. No stages skipped — this is greenfield agentic architecture on an existing domain. |
| 5 | Assign priority | **P2 — Planned Enhancement.** Strategic, not urgent. Timeline: next 2-3 sprints for initial build. |
| 6 | Enter into backlog | Type A, STO named, all stages, P2, estimated 10-12 week pilot |

**Gate 0 Outputs:**

- [x] Type: A (New Product / Major Feature)
- [x] STO: [Named person]
- [x] Stages: 0 → 1 → 2 → 3 → 4 → 5
- [x] Priority: P2
- [x] Backlog: Entered

---

## STAGE 1: REQUIREMENT & SCOPING

| # | Action Item | SCA/MedComm Implementation |
|---|-----------|---------------------------|
| 1 | Intake call (30 min) | Internal call — self-initiated rearchitecture, not client-driven. Attendees: SA + Engineering lead. Confirm: converting existing 12-stage pipeline to agentic system, not building from scratch. |
| 2 | Discovery — map current pipeline | Document all 12+ stages end-to-end with provider, prompt key, input, output, and dependencies for each: |
| | | **Pre-1:** Parse reference asset images (Claude via Bedrock) |
| | | **Stage 1:** Extract all content from source PDFs — text, tables, figures, flowcharts as Mermaid, equations. Per-page output with `=== PAGE n ===` headers. (Gemini 3 Pro) |
| | | **Stage 2:** Generate hierarchical XML outline `<Asset> → <Part> → <Component> → <Sub-Component>` based on asset type, dimensions, topic. Two variants: vertical and horizontal. (Gemini 2.5 Pro) |
| | | **Stage 3:** Flesh out each component with detailed content. Iterates through `<part>` elements, extracts titles to keyed output ("1_Title", "2_Title"). (Gemini 2.5 Pro) |
| | | **Stages 5-8:** Design spec chain — 4 sequential stages using Claude. Stage 5 (spec from images) → Stage 6 (spec refinement) → Stage 7 (design feedback) → Stage 8 (final design parse). Each depends on prior stage + reference images. |
| | | **Stage 9:** Generate design spec from template or images. Template-driven path. |
| | | **Stage 10:** Section-level processing with 4 sub-stages per section — (10.1) section layout generation, (10.2) layout feedback/validation, (10.3) section fit to PDF dimensions via screenshot, (10.4) fit feedback/validation. Template-specific model overrides (az-infographic, slide-deck use Gemini 3 Pro). Playwright screenshots for visual validation. |
| | | **Stage 11:** HTML → PDF conversion. Two paths: SimpleSSRBridge (React/HTML → full HTML, 120s timeout) then Playwright PDF (1280x780 viewport). Adobe PDF Services as enterprise path with credential rotation. |
| | | **Stages 12-13:** Code iteration from user comments. Stage 12 = first pass, Stage 13 = second pass (depends on Stages 1+11). Both use Claude. |
| 3 | Collect inputs and outputs | **Inputs:** Source PDFs (up to 1GB), reference asset images, asset type selection (poster/slide deck/infographic/emailer/microsite), template selection (6 slide-deck variants, poster templates, etc.), topic/description, user comments for iteration. **Outputs:** XML content outline, section content (HTML with citations), design specs, section layouts (HTML/CSS), screenshots (PNG via Playwright), final PDF asset. |
| 4 | Collect good/bad examples | Gather 5+ existing MedComm assets across types: 2 slide decks, 1 infographic, 1 poster, 1 emailer. For each, document: what was good (accurate content, proper layout, correct citations) and what failed (content hallucinations, layout overflow, broken Mermaid diagrams, citation mismatches, wrong asset dimensions). |
| 5 | Define scalability parameters | **Max processing time:** Current 5-8 min end-to-end; target same or better. **Concurrent users:** Currently 15 Celery workers; target 10+ simultaneous projects. **Time to onboard new asset type:** Currently requires new prompts + template overrides (days); target: add skills + template config (hours). **Cost per asset:** Currently $2-5 per asset (multi-model); target same or lower. **Error rate:** Currently frequent orchestration bugs; target < 5% pipeline failures. **Rework rate:** Target < 20% of outputs need human correction. |
| 6 | Plan golden dataset | **Content quality dataset (15-20 rows):** Outline quality (completeness, hierarchy, topic relevance), section content (accuracy, citations, interpretation). **Visual quality dataset (10-15 rows):** Layout quality (no overflow, correct viewport), template compliance, screenshot fidelity. **Edge cases (25-30% of rows):** Complex tables in source PDFs, Mermaid flowcharts, multi-column layouts, very long content exceeding page bounds, OCR-artifact PDFs. |
| 7 | Define scoring dimensions | 1. **Data Accuracy** (PASS/FAIL) — every claim traceable to source, no hallucinated drug names/data. 2. **Content Completeness** (checklist) — all outline sections present, all citations linked. 3. **Visual Quality** (1-5) — layout renders correctly, no overflow/truncation, fonts and colors per template. 4. **Template Compliance** (checklist) — matches selected template structure and asset dimensions. 5. **Source Fidelity** (1-5) — content accurately represents source PDFs, tables and figures correctly interpreted. |
| 8 | Draft requirements document | **Problem:** Current prompt-chain pipeline is brittle and hard to extend. **Solution:** Agentic rearchitecture. **Success criteria:** Content eval >= 85%, visual quality >= 4/5, pipeline failure < 5%, time-to-new-asset-type < 1 day. **Out of scope:** Frontend redesign, auth changes, new asset types (post-pilot), database schema changes. |
| 9 | Internal review (1 hr) | Engineer validates: Is Strands framework viable for this use case? Can Celery infra be replaced incrementally or must it be swapped wholesale? What about Playwright/Adobe/S3 dependencies — do they become tools cleanly? Leadership confirms: capacity for 2-3 sprints of rearchitecture alongside ongoing delivery. |
| 10 | Sign-off | Internal sign-off — SA + Engineering + Leadership agree on rubric, success criteria, and sprint capacity. No external client for this pilot. |

**Gate 1 Outputs:**

- [x] Current pipeline fully documented (12+ stages with providers, prompts, I/O, dependencies)
- [x] Golden dataset plan: 15-20 content rows + 10-15 visual rows + edge cases
- [x] 5 scoring dimensions defined with rubrics
- [x] Scalability parameters quantified (processing time, concurrency, cost, error rate, onboarding time)
- [x] Requirements document drafted and internally reviewed
- [x] Strands framework feasibility assessed
- [x] Risk register initialized

---

## STAGE 2: SOLUTIONING WORKSHOP

| # | Action Item | SCA/MedComm Implementation |
|---|-----------|---------------------------|
| 1 | Send pre-workshop packet | Distribute: (a) Current 12-stage pipeline diagram with LLM providers and dependencies, (b) Strands framework overview + comparison with alternatives, (c) Proposed agent topology draft, (d) Full prompt-to-skill mapping table, (e) Full service-to-tool mapping table, (f) Constraints: must preserve existing API contracts (FastAPI endpoints, S3 structure, DB schema) |
| 2 | Walk the Complexity Ladder | **Current system: Level 2 (Router) + Level 3 (Parallel).** Stage 10 processes sections in parallel; different stages route to different providers (Gemini vs Claude). **Target system: Level 5 (Multi-Agent).** Justification: single agent cannot hold context for 12+ stages spanning content generation, visual design, rendering, and iteration. Specialized agents produce better outputs in their domain. Current pipeline already has natural agent boundaries (content vs design vs rendering vs iteration). **Evidence needed:** Run single-agent vs multi-agent on 10 test inputs during first sprint to validate the split. |
| 3 | Design agent topology | Four specialized agents under one orchestrator: |
| | | **Orchestrator Agent** — Receives user request (asset type, template, topic, sources). Plans execution sequence. Delegates to specialized agents. Manages cross-agent state. Handles error recovery and retries. |
| | | **ContentAgent** (Stages 1-3) — PDF parsing, outline generation, section content fleshing. Owns the content creation lifecycle. |
| | | **DesignAgent** (Stages 5-9) — Design spec generation chain. Produces visual design specifications from reference images and templates. |
| | | **RenderAgent** (Stages 10-11) — Section-level layout, fit, screenshot capture, PDF generation. Handles the 4 sub-stage loop per section. Owns Playwright and Adobe tool interactions. |
| | | **IterationAgent** (Stages 12-13) — Processes user comments/annotations/drawings into code modifications. Produces new asset versions. |
| 4 | Map all prompts to skills.md | Every `PROMPT_STAGE_MAPPING` entry becomes a versioned skill file: |
| | | `skills/sca/image-parsing.md` — Pre-1 (Claude) — Parse reference asset images |
| | | `skills/sca/pdf-extraction.md` — Stage 1 (Gemini 3 Pro) — Extract text, tables, figures, Mermaid, equations from PDFs |
| | | `skills/sca/outline-generation-vertical.md` — Stage 2 variant (Gemini 2.5 Pro) — Vertical XML outline |
| | | `skills/sca/outline-generation-horizontal.md` — Stage 2 variant (Gemini 2.5 Pro) — Horizontal XML outline |
| | | `skills/sca/section-fleshing.md` — Stage 3 (Gemini 2.5 Pro) — Flesh out component content with citations |
| | | `skills/sca/design-spec-s1.md` — Stage 5 (Claude) — Design spec stage 1 from images |
| | | `skills/sca/design-spec-s2.md` — Stage 6 (Claude) — Design spec stage 2 refinement |
| | | `skills/sca/design-feedback.md` — Stage 7 (Claude) — Design feedback and validation |
| | | `skills/sca/final-design-parser.md` — Stage 8 (Claude) — Parse final design specification |
| | | `skills/sca/section-layout.md` — Stage 10.1 (Gemini 2.5/3 Pro) — Generate HTML/CSS layout per section |
| | | `skills/sca/section-layout-feedback.md` — Stage 10.2 (Gemini 2.5 Pro) — Validate and refine layout |
| | | `skills/sca/section-fit.md` — Stage 10.3 (Gemini 2.5 Pro) — Adjust layout to fit PDF page dimensions |
| | | `skills/sca/section-fit-feedback.md` — Stage 10.4 (Gemini 2.5 Pro) — Validate final section fit |
| | | `skills/sca/code-iteration-s1.md` — Stage 12 (Claude) — First-pass code iteration from user feedback |
| | | `skills/sca/code-iteration-s2.md` — Stage 13 (Claude) — Second-pass iteration (depends on Stage 1 + 11 context) |
| | | **Total: 15 skill files.** Each includes: system prompt, user prompt template, model, output format, version metadata. |
| 5 | Map services to tools | Complex service logic becomes agent-callable tools: |
| | | `tools/playwright-screenshot` — Launch headless Chromium, set viewport to asset_dimensions, wait for images/fonts/Canvas/SVG, capture PNG, cleanup local files |
| | | `tools/pdf-generator` — Two paths: Playwright HTML→PDF (1280x780, print_background=True) + Adobe PDF Services with credential rotation (APIKeyManager, multiple client_id/secret pairs) |
| | | `tools/s3-file-manager` — Presigned URL generation (15-min expiry), staging-to-permanent copy, LLM payload storage at `llm-payloads/` prefix |
| | | `tools/llm-queue` — Wraps existing GlobalLLMQueue: 15 concurrent workers, 4 RPS rate limit, 3 retries with exponential backoff, 300s timeout, status tracking (QUEUED→PROCESSING→COMPLETED/FAILED/TIMEOUT) |
| | | `tools/xml-parser` — Parse and serialize the `<Asset>→<Part>→<Component>→<Sub-Component>` XML outline structure, handle recursive nesting and tag balancing |
| | | `tools/section-processor` — Iterate through Stage 3 keyed output, extract titles, produce per-section data structure for Stage 10 processing |
| | | `tools/image-renderer` — Render Mermaid diagrams to images, process figures extracted from PDFs (DPI_SCALE=2.0, CHUNK_SIZE=10) |
| | | `tools/template-resolver` — Resolve template-specific overrides (TEMPLATE_STAGE10_PROMPT_OVERRIDES for az-infographic, az-slide-deck, slide-deck) and asset dimensions |
| | | **Total: 8 tools.** |
| 6 | Define KB requirements | **Structural KBs:** `kb/sca/asset-types.md` (definitions and constraints per asset type — poster, slide deck, infographic, emailer, microsite, custom). `kb/sca/template-catalog.md` (available templates per type with dimensions, color schemes, layout rules, preview references). `kb/sca/xml-outline-schema.md` (the XML structure specification and valid nesting rules). **Conventions KBs:** `kb/sca/medical-writing-conventions.md` (MedComm-specific language — abbreviations, citation format, regulatory language). `kb/sca/design-principles.md` (visual layout rules — spacing, font hierarchy, color usage per brand). **Corrections KBs:** `kb/sca/common-failures.md` (known failure patterns from production bugs — content overflow, citation mismatches, Mermaid rendering issues, and how to avoid them). |
| 7 | Non-functional requirements | **Latency:** End-to-end < 8 min (current: 5-8 min). **Concurrency:** 10+ simultaneous projects. **Cost:** < $5 per asset. **Model tiering:** Gemini 3 Pro for visual tasks (PDF extraction, section layout), Gemini 2.5 Pro for text tasks (outline, content), Claude Sonnet 3.7 for reasoning tasks (design specs, iteration). **Fallback:** Gemini 3 Pro → Gemini 2.5 Pro with 30s/60s delays (preserve current chain). **Infrastructure:** Must work with existing PostgreSQL schema, S3 bucket structure, Redis broker. |
| 8 | Framework decision | Evaluate Strands against criteria: multi-agent with tool use support? Rate-limited LLM queue integration? Celery/Redis compatibility? Handles Stage 10's 4-sub-stage parallel-per-section pattern? Document decision with rationale. If Strands rejected, identify alternative or plan for custom lightweight orchestration. |
| 9 | Risk register | **R1:** Strands may not support all required patterns — Mitigation: evaluate in Sprint 1, fall back to custom orchestration. **R2:** Visual quality eval is subjective — Mitigation: define rubric with measurable criteria (no overflow, correct dimensions, text readability). **R3:** Agentic overhead may increase latency — Mitigation: benchmark early in Sprint 1, optimize agent handoffs. **R4:** 15 skills + 8 tools is a large surface area — Mitigation: build ContentAgent first as pattern validation before expanding. **R5:** Preserving API contracts while swapping orchestration — Mitigation: feature flag to route between old and new pipeline. |

**Gate 2 Outputs:**

- [x] Architecture: Multi-Agent Level 5 — Orchestrator + ContentAgent + DesignAgent + RenderAgent + IterationAgent
- [x] Complexity decision justified: single-agent insufficient for 12+ stages spanning content, design, rendering, iteration
- [x] Skills map: 15 files with owners and effort estimates
- [x] Tools map: 8 tools mapped from current services
- [x] KB requirements: 3 structural + 2 conventions + 1 corrections
- [x] Framework decision documented (Strands or alternative)
- [x] Non-functional requirements defined
- [x] Risk register: 5 identified risks with mitigations
- [x] Timeline: Sprint 1 = ContentAgent, Sprint 2 = DesignAgent + RenderAgent, Sprint 3 = IterationAgent + integration

---

## STAGE 3: BUILD & TEST

| # | Action Item | SCA/MedComm Implementation |
|---|-----------|---------------------------|
| 1 | Repo and branch setup | Create branch: `feature/sca-agentic-rearchitecture`. Enable branch protection on `main`. Configure CODEOWNERS: `/skills/sca/` → SA team, `/tools/` → engineering, `/eval-datasets/sca/` → QC + SA, `/pipeline/` → engineering only. Add PR template with eval result fields. |
| 2 | Role-based permissions | **SAs** create and edit all 15 skill files, all KBs, eval datasets. **Engineers** implement 8 tools, agent framework integration, Orchestrator, API wiring. **QC** builds eval datasets, runs Tier 3 human reviews. SAs use Cursor/Claude Code for skill editing, engineers handle all `.py` files. |
| 3 | Non-engineers onboarded | 30-min guided Git walkthrough for SAs and QC on sandbox repo. Cover: branch creation (`skill/sca-outline-improve`), editing skill files, running local eval, committing, pushing, creating PRs. Mandatory before first contribution. |
| | | |
| | **Sprint 1: ContentAgent (Weeks 4-5)** | |
| 4 | Engineer: ContentAgent skeleton | Implement ContentAgent in chosen framework. Wire up tool integrations: `llm-queue` (wrapping existing GlobalLLMQueue singleton), `xml-parser`, `section-processor`, `image-renderer`. Agent receives: source PDFs + asset type + template + topic. Agent produces: parsed content → XML outline → fleshed section content. |
| 5 | SA: Convert content skills (4 files) | `skills/sca/pdf-extraction.md` — from `pdf_gemini-3-pro-preview` prompt. System prompt + user prompt template + model spec + output format (per-page with `=== PAGE n ===` headers). `skills/sca/outline-generation-vertical.md` + `horizontal.md` — from outline prompts. Include: XML schema specification, asset type constraints, dimension-aware formatting. `skills/sca/section-fleshing.md` — from `flesh_gemini-2.5-pro`. Include: iteration pattern through `<part>` elements, title extraction to keyed output. `skills/sca/image-parsing.md` — from `image_bedrock-sonnet3.7`. |
| 6 | QC + SA: Content eval dataset (15 rows) | **Outline quality (5 rows):** Input: source PDFs + asset type + topic. Expected: well-structured XML matching template schema. Scoring: completeness (all parts present), hierarchy (proper `<Part>→<Component>→<Sub-Component>` nesting), topic relevance. **Section content (7 rows):** Input: outline + source docs. Expected: accurate, cited content per section. Scoring: data accuracy (PASS/FAIL — zero tolerance), completeness, source fidelity. **Edge cases (3 rows):** Complex tables spanning multiple PDF pages, Mermaid flowcharts in source, 50+ page PDFs with OCR artifacts. |
| 7 | Sprint 1 validation | Run ContentAgent on all 15 eval rows. Target: content weighted score >= 0.80, zero data accuracy FAILs. Compare output against current Stage 1-3 pipeline output on same inputs — agentic must match or exceed. |
| | | |
| | **Sprint 2: DesignAgent + RenderAgent (Weeks 6-7)** | |
| 8 | Engineer: DesignAgent | Implement DesignAgent wrapping Stage 5-8 chain. Sequential skill execution: design-spec-s1 → design-spec-s2 → design-feedback → final-design-parser. Each step depends on prior output + reference images from S3. |
| 9 | Engineer: RenderAgent | Implement RenderAgent handling Stage 10's 4-sub-stage pattern. **Per section:** (10.1) section-layout skill → (10.2) layout-feedback skill → screenshot via `playwright-screenshot` tool → (10.3) section-fit skill → (10.4) fit-feedback skill. Handle template-specific model overrides via `template-resolver` tool (az-infographic, az-slide-deck, slide-deck all use Gemini 3 Pro). Wire up `pdf-generator` tool for Stage 11: SimpleSSRBridge (React→HTML, 120s timeout) then Playwright PDF (1280x780 viewport, print_background=True). Adobe path with credential rotation via APIKeyManager. |
| 10 | SA: Convert design + render skills (8 files) | Design skills: `design-spec-s1.md`, `design-spec-s2.md`, `design-feedback.md`, `final-design-parser.md` — all from Claude-based prompts, each referencing image inputs. Render skills: `section-layout.md` (with model variant per template type), `section-layout-feedback.md`, `section-fit.md` (input: screenshot + PDF dimensions), `section-fit-feedback.md`. |
| 11 | QC + SA: Visual eval dataset (10 rows) | **Layout quality (4 rows):** Input: section content + asset dimensions (e.g., 1920x1080 for slides). Expected: properly fitted HTML/CSS. Scoring: no overflow/truncation, correct viewport, text readable, images loaded and positioned. **Template compliance (3 rows):** Input: content + specific template (slide-deck variant, poster, infographic). Expected: output matches template structure and brand rules. **Screenshot fidelity (3 rows):** Input: rendered HTML. Expected: clean PNG capture via Playwright. Scoring: no rendering artifacts, correct pixel dimensions, all elements visible (fonts, Canvas, SVG rendered). |
| | | |
| | **Sprint 3: IterationAgent + Integration (Weeks 8-9)** | |
| 12 | Engineer: IterationAgent | Implement IterationAgent wrapping Stages 12-13. Input: user comment text + annotations + drawing data + edit changes (text/style modifications from frontend's 3 edit modes). Output: updated asset code. Stage 13 depends on Stage 1 (source context) + Stage 11 (current asset) — IterationAgent must access cross-agent state. |
| 13 | Engineer: Orchestrator integration | Wire all 4 agents under Orchestrator. Full flow: user request → Orchestrator → ContentAgent (parse → outline → flesh) → DesignAgent (design spec chain) → RenderAgent (layout → fit → PDF per section) → output. Iteration flow: user comment → Orchestrator → IterationAgent → RenderAgent → updated asset. **Preserve existing API contracts:** FastAPI endpoints (`/chatwithpdf/upload-source-documents`, `/chatwithpdf/stages`, `/chatwithpdf/stages-mix`), S3 bucket structure (`chats/{chat_id}/`), database schema (STAGES, REVISIONS, SECTIONS tables). Feature flag: `USE_AGENTIC_PIPELINE=True/False` to route between old Celery pipeline and new agentic pipeline. |
| 14 | SA: Convert iteration skills + KBs | Skills: `code-iteration-s1.md`, `code-iteration-s2.md` — from Claude-based prompts. KB: `kb/sca/common-failures.md` — compiled from production bug patterns (content overflow at page boundaries, citation index mismatches, Mermaid syntax breaking in specific diagram types, Adobe credential timeout patterns). |
| | | |
| | **Testing (Continuous Across All Sprints)** | |
| 15 | Tier 1: Automated checks (every commit) | Pre-commit hooks: Python syntax (Ruff), secrets detection, skill file schema validation (frontmatter must include: name, version, product_area, model, execution_mode), KB format validation (valid markdown with required sections). Custom checks: hallucinated drug name detection (only names from source PDFs allowed in output), XML schema validation (outline must be valid `<Asset>` structure with proper nesting). |
| 16 | Tier 2: LLM-as-Judge evals (every PR) | **Content eval (5-row quick):** Judge model: Claude Opus (never the same model that generated the output). Dimensions: data accuracy (PASS/FAIL), content completeness, source fidelity. Pass criteria: weighted >= 0.80, zero data accuracy FAILs. **Visual eval (5-row quick):** Judge: Gemini 2.5 Pro with image input (screenshot of rendered asset). Dimensions: layout quality, template compliance, visual readability. Note: visual eval requires multi-modal judge — screenshot is the input, not just code. |
| 17 | Tier 3: Human review (weekly) | QC reviews 10 assets per week: 3 slide decks, 3 infographics, 2 posters, 2 emailers. Review blind (without seeing LLM-Judge scores first). Compare agentic output vs. current pipeline output on same inputs. Track: where agentic is better, where it's worse, novel failure modes not caught by automated evals. New failure patterns → new eval rows. |
| 18 | A/B comparison | Run same 15-20 inputs through both current Celery pipeline and new agentic pipeline. Compare on all dimensions: quality scores, end-to-end latency, per-asset cost (broken down by agent), pipeline failure rate. **This is the key gate** — agentic system must be at parity or better on all dimensions before proceeding. |
| 19 | Auto-refinement | Run AI-assisted improvement on content skills (`outline-generation.md`, `section-fleshing.md`) using eval feedback. Guardrails: max 5 modifications per session, $50 cost cap, all changes human-reviewed before merge. Hold-out set (3 content rows + 2 visual rows) never exposed to auto-refinement — used only for final validation. |
| 20 | PR review and merge | **Sprint 1 PR:** ContentAgent + 4 skills + content eval dataset (15 rows). **Sprint 2 PR:** DesignAgent + RenderAgent + 8 skills + 8 tools + visual eval dataset (10 rows). **Sprint 3 PR:** IterationAgent + Orchestrator + 2 skills + KBs + A/B comparison results. Each PR includes before/after eval scores. Required reviewers: 1 peer SA (skill accuracy) + 1 engineer (code quality). |

**Gate 3 Outputs:**

- [x] All 15 skills converted, versioned, and passing eval
- [x] All 8 tools implemented and tested
- [x] Content eval: >= 85% weighted score, zero data accuracy FAILs
- [x] Visual eval: layout quality >= 4/5, zero overflow/truncation on standard templates
- [x] A/B comparison: agentic >= current pipeline on quality, latency, cost, and failure rate
- [x] Hold-out set passes (5 rows never seen during development/auto-refinement)
- [x] All code reviewed by engineering
- [x] Known limitations documented (e.g., Mermaid rendering edge cases, very large PDFs, custom asset types)

---

## STAGE 4: DEPLOY & VALIDATE

| # | Action Item | SCA/MedComm Implementation |
|---|-----------|---------------------------|
| 1 | Deploy to staging | Deploy agentic pipeline to staging alongside current Celery pipeline. Feature flag `USE_AGENTIC_PIPELINE` controls routing — both must be runnable simultaneously. Staging uses separate API keys from production (Gemini, Bedrock, Adobe). |
| 2 | Run full eval in staging | Execute complete eval suite (25-30 rows) in staging container. Verify scores match local dev within 0.05 tolerance. **Check specifically:** Playwright screenshot rendering works in staging (headless Chromium dependencies installed), S3 paths resolve correctly (`chats/{chat_id}/` structure), Adobe PDF credentials rotate properly (APIKeyManager with multiple client_id/secret pairs), LLM rate limits don't cause cascading timeouts (4 RPS, 15 concurrent, 300s queue wait), fallback chain fires correctly (Gemini 3 Pro → 2.5 Pro with 30s/60s delays). |
| 3 | Compare staging vs. local | If eval scores differ by > 0.05 on weighted average → investigate environment parity before proceeding. Common causes: different Playwright/Chromium version in container, model access differences (rate limits, quotas), S3 latency in staging VPC. |
| 4 | Pin model versions | Lock in `config/models.yaml`: `gemini-3-pro-preview` (PDF extraction, section layout for standard templates), `gemini-2.5-pro` (outline, content fleshing, section fit), `claude-sonnet-3.7` via Bedrock (design specs, code iteration). Template overrides: az-infographic/slide-deck use `gemini-3-pro` for all Stage 10 sub-stages. Document fallback chain. Never use "latest" — always exact version strings. |
| 5 | Set up monitoring | Structured logging for every agent and tool call: `{agent: "ContentAgent", skill: "pdf-extraction", skill_version: "1.0.0", model: "gemini-3-pro", latency_ms: 45000, tokens_in: 12000, tokens_out: 3000, cost_usd: 0.45, status: "completed", run_id: "...", chat_id: "..."}`. Leverage existing MONITOR_LLM_CALLS table (already stores full request/response, large payloads in S3 at `llm-payloads/`). **Alerts:** Pipeline failure rate > 10%, single asset cost > $10, end-to-end latency p95 > 15 min, agent stall (no progress for 5 min). |
| 6 | Test rollback | Verify feature flag can instantly route all traffic back to current Celery pipeline. Execute rollback drill: flip flag → run 3 test assets through old pipeline → confirm outputs correct and DB state consistent. Document: rollback takes < 2 minutes (flag flip + cache clear), no data migration needed (both systems share same PostgreSQL schema and S3 structure). |
| 7 | Cost validation | Run 20 identical assets through both pipelines. Compare total LLM API cost per asset broken down by agent/stage. Validate within $5/asset ceiling. Calculate model tiering savings: Gemini 2.5 for text tasks vs Gemini 3 for visual tasks vs Claude for reasoning. Track infrastructure costs: Playwright container compute, S3 storage, Adobe API calls. |
| 8 | Incident response runbook | **SEV-1:** Asset generates hallucinated clinical data → immediate rollback to Celery pipeline + investigate skill + add regression test row. **SEV-2:** Layout consistently overflows for a template type → disable that template, fix section-fit skill, add visual eval row. **SEV-3:** Cost spike (Orchestrator spawning unnecessary agent calls or retry loops) → check agent delegation logic, verify rate limiter, add cost guardrail per asset. **SEV-4:** Minor visual inconsistency (font rendering, spacing) → update `design-principles` KB, add to corrections KB. |
| 9 | Security check | Verify: no API keys in skill files or KB files. S3 presigned URLs still use 15-min expiry. LLM request/response payloads stored in S3 (not logged to console or stdout). Adobe credential rotation still works through APIKeyManager. JWT auth flow unchanged. `.env` files gitignored. Secrets scanning active in CI (detect-secrets). Separate API keys for staging vs production. |
| 10 | Production deployment plan | **Canary rollout via feature flag:** Week 1: 10% of new projects routed to agentic pipeline. Monitor quality, latency, cost, failure rate daily. Week 2: If all metrics within targets → ramp to 50%. Week 3: If stable → 100%. Engineer + Leadership approval required at each ramp step. Old Celery pipeline kept available for 4 weeks post-100% as safety net. |

**Gate 4 Outputs:**

- [x] Full eval passes in staging (within 0.05 of local scores)
- [x] Monitoring live with per-agent metrics, cost dashboard, failure alerts
- [x] Rollback tested and documented (feature flag switch < 2 min)
- [x] Cost per asset validated within $5 ceiling with breakdown
- [x] Incident response runbook with SCA-specific scenarios
- [x] Model versions pinned in config
- [x] Security verified (no secrets in code, separate keys, scanning active)
- [x] Engineering + Leadership sign-off on canary deployment plan

---

## STAGE 5: OPERATE & EVOLVE

| # | Action Item | SCA/MedComm Implementation |
|---|-----------|---------------------------|
| 1 | Assemble handoff package | **Architecture doc:** Multi-agent topology diagram (Orchestrator → ContentAgent → DesignAgent → RenderAgent → IterationAgent), data flow (S3 → agents → tools → PDF), tool dependency map (which tools each agent uses). **Skill files:** All 15 skills in `/skills/sca/`, each versioned with model and prompt metadata. **KBs:** 6 knowledge bases covering asset types, templates, XML schema, writing conventions, design principles, common failures. **Eval suite:** 25-30 rows (content + visual) + hold-out set + LLM-as-Judge prompts + automated checks. **Known limitations:** Mermaid rendering edge cases, very large PDFs (100+ pages), custom asset type handling, Adobe credential timeout under high concurrency. **Decision log:** Why multi-agent over single-agent, why specific model assignments per skill, framework decision rationale. |
| 2 | Train delivery team | **Session 1 — System overview:** How the 4 agents work, what each skill does, how tools interact, where data flows through S3/PostgreSQL. Walk through a complete asset generation trace. **Session 2 — Daily operations:** How to monitor agent performance via structured logs, read the cost dashboard, interpret eval scores. How to add a new template (update `kb/sca/template-catalog.md` + add template override if needed). How to adjust a skill (edit `.md` file, run eval, submit PR). **Session 3 — Troubleshooting:** Layout overflow → check `section-fit.md` skill + asset dimensions in `template-resolver`. Content hallucination → check `section-fleshing.md` + source extraction quality from Stage 1. Agent timeout → check LLM queue rate limits and fallback chain. Cost spike → check Orchestrator delegation logic. All sessions recorded. |
| 3 | Validate independence | Delivery team runs `python run_eval.py --mode full` independently. They can interpret the output: which skills are underperforming, which dimensions need attention. They can make a skill edit, run quick eval, and submit a PR without builder involvement. If they can't → training is incomplete. |
| 4 | Define escalation tiers | **L1 (Delivery handles):** Known issues with documented fixes — pipeline stall (restart per runbook), template rendering glitch (known Playwright workaround), Adobe credential timeout (trigger rotation). **L2 (Delivery + SA consult):** Known issue type but novel specifics — new document format causing PDF extraction failures, unfamiliar asset type edge case. **L3 (Build team):** Requires skill/KB/code change — systematic quality regression on a dimension, new tool needed, framework limitation discovered. **L4 (Leadership):** Architectural decision — e.g., Strands framework fundamentally doesn't scale, need to re-evaluate approach. |
| 5 | Activate feedback loop | QC classifies every piece of feedback on MedComm assets: **(A) Factual error** (wrong data, hallucinated claim) → add regression test row with data_accuracy = FAIL → route to build team for skill fix. **(B) Missing content** (section incomplete, citations missing) → add eval row with completeness < 1.0 → SA reviews skill. **(C) Style mismatch** (client wants different tone, layout preference) → update `design-principles` or `medical-writing-conventions` KB → add client-specific corrections. **(D) New capability request** (new asset type, new edit mode) → not added to eval dataset, goes through Stage 0 intake as separate engagement. Track rework rate — target < 20%. |
| 6 | Transfer monitoring ownership | **Daily:** Automated quality spot checks + cost dashboard review (delivery team). **Weekly:** QC human review of 10 assets (blind scoring). **Bi-weekly:** Full eval suite re-run (automated). **Monthly:** Quality trend report to stakeholders — average scores, failure patterns, cost trends, recommendations. |
| 7 | Support warranty | Builders remain available for L3 escalations for 4 weeks post-handoff. During this period, track: how many L3 escalations per week? Are they trending to zero? If not, revisit training materials or identify systemic issues. |
| 8 | Scale to new asset types | Once pilot succeeds, test scalability: add a new asset type (e.g., microsite) following **Type B process** (Stages 0 → 2 → 3 → 4 → 5, skip Stage 1 since requirements framework exists). Should require: new skill variants (`microsite-layout.md`), template addition to catalog KB, 10-row eval dataset for new type. **If this takes hours not days, the architecture is working.** |
| 9 | WoW process retrospective | After pilot completes, run a dedicated retro on the WoW process itself: What stages added real value? What felt like overhead? Where did we skip steps and regret it? Where did the process save us from a mistake? Which gate caught a real issue? Feed learnings back into the process map for the next team that uses it. **This retro is the real deliverable of the pilot** — not just the agentic platform, but validated ways of working. |

**Gate 5 Outputs:**

- [x] Handoff package complete (architecture, 15 skills, 6 KBs, eval suite, runbook, decision log)
- [x] Delivery team trained (3 sessions recorded)
- [x] Delivery team can run eval suite and interpret results independently
- [x] Escalation tiers defined and agreed (L1-L4)
- [x] Feedback loop active with QC classification
- [x] Monitoring ownership transferred
- [x] Support warranty: 4 weeks, tracking L3 escalation trend
- [x] Scalability tested: new asset type added via Type B process
- [x] WoW process retro completed with documented learnings

---

## CROSS-CUTTING: APPLIES THROUGHOUT THIS PILOT

### Scope Boundaries

Explicitly **out of scope** for this pilot — any request touching these goes through Stage 0 as a separate engagement:

| Out of Scope | Reason |
|-------------|--------|
| Frontend redesign | React app stays as-is; agentic changes are backend-only |
| Authentication changes | JWT + SSO flow unchanged |
| New asset types | Microsites, etc. deferred to post-pilot scalability test |
| Database schema changes | Agentic system uses same PostgreSQL tables (STAGES, REVISIONS, SECTIONS) |
| Client-facing deployment | Internal pilot first; client rollout is a separate decision |

### Cost Governance

| Phase | Expected Daily Spend | Governance |
|-------|---------------------|-----------|
| Development (Sprints 1-3) | $10-30/day (eval runs + dev testing) | SA reviews weekly |
| Staging validation | $20-50/day (full eval suite + A/B comparison) | Leadership notified |
| Production canary (10%) | $5-15/day | Auto-approved |
| Production full (100%) | $30-80/day | Monthly cost report to leadership |
| Any single asset > $10 | — | Engineer reviews after the fact |

### Timeline

| Week | Milestone | Gate |
|------|-----------|------|
| Week 1 | Stage 0 complete — classified, STO assigned, prioritized | Gate 0 |
| Week 2-3 | Stage 1 complete — pipeline documented, eval plan, scalability params, requirements | Gate 1 |
| Week 3 | Stage 2 complete — architecture decided, skills + tools mapped, framework chosen | Gate 2 |
| Week 4-5 | Sprint 1 — ContentAgent + 4 skills + content eval passing | — |
| Week 6-7 | Sprint 2 — DesignAgent + RenderAgent + 8 skills + 8 tools + visual eval passing | — |
| Week 8-9 | Sprint 3 — IterationAgent + Orchestrator + A/B comparison passing | Gate 3 |
| Week 10 | Stage 4 — Staging deployment + full eval + rollback test + monitoring | Gate 4 |
| Week 11-12 | Stage 4-5 — Production canary → ramp → handoff + retro | Gate 5 |

### Success Criteria Summary

| Dimension | Target | How Measured |
|-----------|--------|-------------|
| Content quality | >= 85% weighted eval score | LLM-as-Judge + Tier 3 human review |
| Data accuracy | Zero FAILs | Automated + LLM-as-Judge (binary) |
| Visual quality | >= 4/5 average | Multi-modal LLM-as-Judge + human review |
| Pipeline failure rate | < 5% | Production monitoring |
| End-to-end latency | < 8 min per asset | Structured logging p50/p95 |
| Cost per asset | < $5 | Per-agent cost tracking |
| Rework rate | < 20% | QC feedback classification |
| Time to add new asset type | Hours, not days | Post-pilot scalability test |
| Process followed | All gates passed | Gate checklists completed |
