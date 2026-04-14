# GenAI Ways of Working — Process Map

> **Purpose:** This is the operational playbook. Every stage tells you exactly what to do, what to produce, what must be true before you move on, and what to do when things go wrong. If you're new to the team, start here.

---

## HOW TO USE THIS DOCUMENT

```
1. A request comes in → Go to STAGE 0 (classify it)
2. Classification tells you which stages apply (see table below)
3. Work through each applicable stage sequentially
4. At each stage gate, run through the checklist — all items must pass
5. If stuck, check the "When Things Go Wrong" section for that stage
```

### Which Stages Apply?

| Engagement Type | What It Is | Stages | Example |
|----------------|-----------|--------|---------|
| **A** — New Product / Major Feature | Greenfield build or major new capability | 0 → 1 → 2 → 3 → 4 → 5 (all) | "Build MedCom asset generation pipeline" |
| **B** — Significant Enhancement | New section type, new doc format, major skill overhaul | 0 → 2 → 3 → 4 → 5 (skip Stage 1 if requirements clear) | "Add CSR Section 14 to MWA" |
| **C** — Skill/KB Improvement | Improve quality on existing capability | 0 → 3 → 4 | "Section 11 clinical interpretation score too low" |
| **D** — Bug Fix | System not behaving per skill instructions | Fix → Eval → Engineer Review → Deploy | "Section 11 printing table headers twice" |
| **E** — Internal Tooling | Tools for team workflow, not client-facing | 0 → 2 (light) → 3 | "Build MCP server for Cursor workflows" |
| **F** — Demo / Benchmark | BD-driven demo, competitive analysis | 0 → 2 (light) → time-boxed build | "Benchmark against Gamma on visual generation" |

### How to Classify (Decision Tree)

```
Is it a code/pipeline bug? ────────────────────────────── Yes → Type D
Does it only change existing skills/KBs? ─────────────── Yes → Type C
Is it for internal use, not client delivery? ──────────── Yes → Type E
Is it a one-off demo or competitive exercise? ─────────── Yes → Type F
Does it need a solutioning workshop? ──────────────────── Yes → Type A
Does it need new eval datasets? ───────────────────────── Yes → Type A or B
Everything else ───────────────────────────────────────── Type B
```

---

## STAGE 0: INTAKE & CLASSIFICATION

**Purpose:** Classify the work, assign an owner, decide which stages apply.
**Time:** 30 minutes.

### Step-by-Step

| Step | Action | Output |
|------|--------|--------|
| 1 | Receive request (client, internal, or production monitoring) | Request logged |
| 2 | Run classification decision tree above | Engagement type (A-F) |
| 3 | Assign a Single-Threaded Owner (STO) — one person accountable end-to-end | STO named |
| 4 | Determine which stages and gates apply (from table above) | Stage plan |
| 5 | Prioritize using P0-P3 matrix (see below) | Priority assigned |
| 6 | Enter into backlog | Backlog entry |

### Priority Matrix

| Priority | Definition | Response Time |
|----------|-----------|---------------|
| **P0** | Production down / critical client blocker | Same day |
| **P1** | Quality failure caught by client / blocking demo | Within 2 days |
| **P2** | Quality improvement / planned enhancement | Next sprint |
| **P3** | Nice-to-have / future consideration | Backlog |

### Gate 0 Checklist

- [ ] Engagement type classified (A/B/C/D/E/F)
- [ ] STO assigned
- [ ] Applicable stages identified
- [ ] Priority assigned (P0-P3)
- [ ] Entered into backlog

**If unclear on classification:** Default to one level higher (e.g., if unsure between B and C, classify as B). It's cheaper to skip a gate you didn't need than to skip one you did.

---

## STAGE 1: REQUIREMENT & SCOPING

**Purpose:** Define the problem, build the golden dataset plan, agree on how quality will be measured.
**Applies to:** Type A engagements. Type B only if requirements are NOT already clear.
**Time:** 2-3 days of effort spread over 1-2 weeks.

### Step-by-Step

#### Step 1: Intake Call (30 min)

| What | Detail |
|------|--------|
| **Attendees** | GenAI Solution Approver + BD/client lead |
| **Actions** | Understand problem at high level. Classify: which product area? Product or service engagement? Engagement type? |
| **Output** | 1-paragraph problem statement + engagement type confirmation |

#### Step 2: Discovery Session (1-2 hours)

| What | Detail |
|------|--------|
| **Attendees** | Solution Architect + SME/domain rep + client |
| **Collect** | (see checklist below) |
| **Output** | Discovery notes document |

**Discovery Checklist — collect ALL of these:**
- [ ] Current manual process end-to-end (walk through it)
- [ ] Input sources (documents, templates, guidelines)
- [ ] Output specifications (document type, format, sections, length)
- [ ] 3-5 examples of manually completed work (good examples)
- [ ] Examples of common errors or rejections (bad examples)
- [ ] Client SOPs and style guides
- [ ] Current processing time (how long does it take manually?)
- [ ] Acceptable processing time (what would they accept from AI?)
- [ ] Volume (documents per month/quarter)
- [ ] Deployment environment (client cloud, our cloud, hybrid)
- [ ] Regulatory and compliance requirements (see pharma checklist below)
- [ ] Concurrent user expectations
- [ ] Cost sensitivity

**If client is too busy for 2-hour discovery:**
- **Option A (Delegate):** Sponsor designates working-level person. Sponsor attends only intake (30 min) and sign-off (30 min).
- **Option B (Async):** Send structured questionnaire. 45-min call only for gaps.
- **Option C (Artifact-driven):** Collect 5 examples + SOPs + style guide. SA drafts requirements from artifacts, client corrects.

#### Step 3: Scalability Parameters Definition (1 hour)

> This step was added based on the 9 April discussion. Scalability must be defined BEFORE solutioning, not after.

Define and document these parameters for the specific engagement:

| Parameter | Question to Answer | Example |
|-----------|-------------------|---------|
| **Max processing time** | What is the acceptable end-to-end time? | "No client has accepted > 5 minutes" |
| **Concurrent users** | How many simultaneous runs must be supported? | 10 users, 13 projects |
| **Time to onboard a document** | How long to add a new source document type? | 2 hours |
| **Time to onboard a template** | How long to add a new output template? | Currently 1-2 days for MedCom |
| **Time to onboard a client** | How long from kickoff to first usable output? | 1-2 weeks |
| **Error rate tolerance** | What % of pipeline failures is acceptable? | < 5% |
| **Cost per output** | What is the acceptable cost ceiling? | $0.50-$3 per asset |
| **Rework rate** | What % of outputs need human correction? | < 20% |

#### Step 4: Golden Dataset Planning (2-4 hours)

| What | Detail |
|------|--------|
| **Attendees** | Solution Architect + QC |
| **Actions** | From manual examples: identify input-output pairs. Define 3-5 scoring dimensions. Draft evaluation rubric. Estimate rows needed. Identify gaps. |
| **Output** | Golden dataset plan |

**Scoring dimensions to define (pick 3-5 relevant to the document type):**

| Dimension | What It Measures | Scoring Type |
|-----------|-----------------|-------------|
| Data Accuracy | Every value matches source | Binary PASS/FAIL (zero tolerance) |
| Completeness | All required sections/elements present | Checklist: present/total |
| Clinical/Domain Interpretation | Narrative explains what numbers mean | 1-5 scale |
| Regulatory Compliance | Follows required structure and language | Checklist of requirements |
| Conciseness & Style | No redundancy, consistent voice, appropriate length | 1-5 scale |
| Brand Compliance (MedCom) | Colors, fonts, logos, layout per brand guide | Checklist of brand elements |
| Visual Quality (MedCom) | Charts readable, properly labeled, no truncation | 1-5 scale |

**How many rows:**

| Scenario | Minimum | Recommended |
|----------|---------|-------------|
| New product area (first time) | 15 rows | 20-25 rows (25-30% edge cases) |
| New client on existing product | 10 rows | 15 rows (20% edge cases) |
| Skill/KB improvement | 5 additional rows targeting failures | 10 rows (50% edge cases) |

#### Step 5: Requirements Document (3-4 hours to draft)

**Must include ALL of the following:**
- [ ] Problem statement
- [ ] In-scope / out-of-scope
- [ ] Success criteria (quantified — accuracy threshold, latency target, cost ceiling)
- [ ] Input specification
- [ ] Output specification
- [ ] Quality dimensions with thresholds
- [ ] Scalability parameters (from Step 3)
- [ ] Timeline constraints
- [ ] Deployment requirements
- [ ] Dependencies
- [ ] Regulatory/compliance requirements
- [ ] Competitive landscape context (what commodity tools can do, where we differentiate)
- [ ] User-centric design considerations (partial results display, confidence indicators, SME behavioral factors)

#### Step 6: Internal Review (1 hour)

| Reviewer | Validates |
|----------|----------|
| Engineer | Technically feasible? Infrastructure concerns? |
| Leadership | Capacity and strategy alignment? |

#### Step 7: Client Sign-Off (30 min call + async)

Walk through requirements and rubric. Frame it: "You're signing off on how we measure quality, not solution approach. If outputs score above [threshold], it's a success." Get explicit sign-off (email confirmation minimum).

### Gate 1 Checklist

- [ ] Golden dataset exists OR plan + timeline to create it
- [ ] Scoring dimensions defined with rubric (3-5 dimensions)
- [ ] Success parameters quantified and agreed (accuracy, latency, cost)
- [ ] Scalability parameters defined (time, users, error rate, cost)
- [ ] Deployment environment identified
- [ ] Stakeholders identified and engagement model defined
- [ ] Client sign-off on rubric obtained (email confirmation minimum)
- [ ] Risk register initialized
- [ ] Competitive landscape documented (what commodity tools do, where we differentiate)

### When Things Go Wrong

| Blocker | Resolution |
|---------|-----------|
| Client doesn't know what they want | Get 3 manual examples (non-negotiable). Build minimal dataset. Run system once, show output. Client reaction = requirement. |
| SME won't participate | Request only: 3 recent completed documents + 1-hour scoring calibration. If refused: escalate to client project lead. If still blocked: proceed on SA domain knowledge, document as risk. |
| Requirements keep changing | This is a scope change — see Scope Change Process below. |
| No SME cooperation at all | Requirements based on SA domain knowledge. Documented as risk. Escalated to client project lead. |

---

## STAGE 2: SOLUTIONING WORKSHOP

**Purpose:** Design the architecture, decide complexity level, identify skills and KBs needed.
**Applies to:** Type A (full workshop), Type B (compressed), Type E/F (lightweight).
**Time:** 3 hours (Type A), 1.5 hours (Type B), 1 hour (Type E/F).

### POC Before Workshop — Mandatory

**Before any solutioning workshop, a lightweight POC should have been completed.** This is not a production-ready prototype — it is a focused test to answer one or two key technical unknowns.

| POC Element | What It Should Cover |
|-------------|---------------------|
| **Scope** | The single riskiest assumption. E.g., "Can this model handle the extraction quality we need?" or "Can the framework support parallel tool calls?" |
| **Time** | 2-5 days maximum. If it takes longer, scope was too broad. |
| **Output** | Concrete results: eval scores on 5-10 test inputs, latency measurements, cost per run. Not just "it works." |
| **Who** | SA + Engineer pair. SME consulted if domain accuracy is the question. |
| **Shared before workshop** | POC results included in pre-workshop packet. Workshop attendees review before arriving. |

**Why:** Without POC results, workshops devolve into opinion debates. POC evidence forces decisions to be data-driven. The Complexity Ladder walk-through is meaningless without test results to cite.

### Pre-Workshop (1-2 days before)

**Facilitator sends pre-workshop packet containing:**
- [ ] Requirements summary (1-pager from Stage 1)
- [ ] Agentic requirement signals from discovery
- [ ] POC results — what was tested, what was the outcome, what questions remain
- [ ] 2-3 possible approaches with pros/cons/evidence (not just one recommendation)
- [ ] Existing reusable components from skills catalog
- [ ] Competitive context
- [ ] Constraints (timeline, budget, infra, people, regulatory)
- [ ] Questions to resolve
- [ ] SME availability — confirm which domain SMEs will attend or be on-call

### Workshop Agenda (Type A — 3 hours)

**Required attendees:** Facilitator (SA Lead), all contributing SAs, Engineering Lead, SME/domain expert (at minimum on-call, ideally present for architecture discussion).

| Time | What | Led By |
|------|------|--------|
| 0:00-0:15 | Context setting. Does everyone understand requirements? Summarize POC results. State decisions to be made. | Facilitator |
| 0:15-0:45 | **Complexity Ladder walk-through.** Can this be a simple chain? Need routing? Parallelization? Genuinely open-ended → agent? Each step must cite evidence from POC results. | All |
| 0:45-1:00 | **Discuss alternative approaches.** Walk through the 2-3 approaches from the pre-workshop packet. Each approach gets 5 min to present, then group discussion. SME validates domain feasibility. Do NOT converge on one approach until all have been heard. | All |
| 1:00-1:30 | **Architecture design.** Based on chosen approach: agent topology, skill map, data flow. Which skills exist? Which need creation? KB requirements. Estimate LLM calls and cost per run. Engineer validates feasibility. SME validates domain coverage. | All |
| 1:30-1:45 | BREAK | |
| 1:45-2:15 | **Non-functional requirements.** Latency budget, concurrency, cost ceiling, security, deployment, pharma-specific (audit trail, data classification, retention). | Engineer-led |
| 2:15-2:45 | **Decision & action items.** State decision with rationale. Assign skill owners. Timeline with milestones. | Facilitator |
| 2:45-3:00 | **Document.** Fill decision record. Capture architecture diagram. All action items with owners + deadlines. | Note-taker |

### The Complexity Ladder — Use This to Decide Architecture

**Default: use the LOWEST level that works. Every step up must be justified by evidence.**

| Level | When to Use | Example | Evidence Needed |
|-------|------------|---------|-----------------|
| **1. Simple Chain** | Steps known in advance. No decision-making. Same process every time. | Converting structured data table into formatted paragraph | Run 10 test cases. If >90% eval score, stop here. |
| **2. Router** | Different inputs need different handling, but each path is deterministic once classified. | CSR section authoring — different skills per section type | Test router on 20 inputs. If classification >95%, router sufficient. |
| **3. Parallel** | Independent subtasks can run simultaneously. Each subtask is individually deterministic. | Authoring multiple CSR sections at once | Compare parallel vs sequential. If 3x faster with no quality loss, use it. |
| **4. Agent** | Steps cannot be predicted. System makes judgment calls. Iteration required. | Auto-refinement — system doesn't know what to modify in advance | Would a person need to make these decisions? If yes + enough guardrails, agent warranted. |
| **5. Multi-Agent** | Single agent can't hold sufficient context. Specialized agents produce better outputs in their domain. | End-to-end document generation with orchestrator + specialized agents | Single-agent quality degrades or hits context limits. Specialized agents score >15% higher. |

**Anti-pattern:** Most tasks that "feel" like Level 4-5 are actually Level 2 (router) or Level 3 (parallel) in disguise. Challenge the assumption.

> **9 April addition — Agent vs. Non-Agent Decision Table:** Before choosing Level 4+, consult this. Maintain it as a living reference and check it before every new build. Same applies to model selection — which model to use depends on the task (e.g., Gemini for images, Claude for text/code).

### Workshop Output — Must Produce All of These

| Artifact | Contents |
|----------|---------|
| **Architecture Diagram** | Agent topology, skill map, data flow, integration points |
| **Complexity Decision** | Level chosen (chain/router/parallel/agent) + rationale with evidence |
| **Skills Map** | Each skill: exists / to-create / to-modify, with owner and effort estimate |
| **KB Requirements** | Each KB: type (structural/conventions/corrections), exists / to-create, data source |
| **Non-Functional Requirements** | Max latency, cost ceiling, concurrency, deployment env, security |
| **Eval Dataset Plan** | Universal rows, client-specific rows, edge cases |
| **Timeline** | Range estimate with milestones |
| **Risk Register** | Updated with technical and client risks |
| **Action Items** | Each with owner and deadline |

### Gate 2 Checklist

- [ ] Architecture documented (diagram + decision record) and peer-reviewed
- [ ] Complexity level justified with evidence (not architectural ambition)
- [ ] Agent vs non-agent decision explicitly documented with rationale
- [ ] Skills map finalized: existing (reuse), to-create, to-modify — with owners and effort
- [ ] KB requirements identified (structural, conventions, corrections)
- [ ] Engineering sign-off on feasibility (or documented note proceeding without it)
- [ ] Cost estimate within acceptable range
- [ ] Non-functional requirements defined (latency, concurrency, cost ceiling)
- [ ] Scalability approach defined (how will the system meet the parameters from Stage 1?)
- [ ] Risk register updated

### When Things Go Wrong

| Blocker | Resolution |
|---------|-----------|
| No engineer available for workshop | SAs conduct workshop internally. Share architecture with engineering async (2-day feedback window). If no response: proceed, document gap, flag as risk. |
| Team disagrees on approach | Type A: do 1-week experimentation spike, then architecture. Type B: architecture first. Type C: experimentation first. If still stuck: Facilitator states decision + rationale, dissenter's objection documented, decision stands unless new evidence emerges. |
| Leadership commits to something on a client call | 24-hour rule: no architectural commitment on client call. Always "let me assess and get back to you." If it happens anyway: honor to client, correct internally in retro. |
| POC pressure — leadership wants to ship POC to production | Make the gap visible. Every POC output includes "Production Readiness Assessment" table showing gaps. Offer Type F demo as alternative. Never say "we can't" — say "we can, and here is what it takes." |

### Preventing POC → Production Anti-Pattern

| Safeguard | How |
|-----------|-----|
| POC code lives on separate branch | Never merged to main without going through full Build Gate |
| POC eval datasets marked "POC quality" | Must be expanded to full dataset before build starts |
| POC is NOT client-deliverable | Internal validation only |
| "What's Missing for Production" section required | This becomes Stage 3 input |
| Formal approval to transition POC → Build | Leadership explicitly acknowledges remaining work |

---

## STAGE 3: BUILD & TEST

**Purpose:** Build skills, KBs, and eval infrastructure. Iterate until quality gates pass.
**Applies to:** All engagement types (varies in rigor).
**Time:** Varies by engagement type. Type A: 2-4 sprints. Type C: 1-2 days. Type D: same day.

### Code Contribution Model

**Branch strategy:** Trunk-based development with short-lived feature branches.
**Branch naming:** `{type}/{area}-{short-description}` (under 50 chars)
- Types: `feature/`, `fix/`, `refactor/`, `eval/`, `skill/`, `kb/`

**Git commands every team member must know:**

| Command | What It Does | When |
|---------|-------------|------|
| `git pull origin main` | Gets latest version | Always before starting new work |
| `git checkout -b skill/my-change` | Creates new branch | Once when starting change |
| `git add <file>` | Stages file for commit | After editing file |
| `git commit -m "short description"` | Saves snapshot | After staging |
| `git push origin skill/my-change` | Uploads branch | When ready for review |

#### Who Does What — Build Phase Permission Matrix

| Action | Solution Architect | QC/Testing | Engineer | SME |
|--------|-------------------|-----------|----------|-----|
| Create feature branch | Yes | Yes | Yes | No (works through SA) |
| Write/edit skill files (.md) | **Primary author** | Review + suggest | Review + approve | Validate domain accuracy |
| Write/edit knowledge bases | **Primary author** | Review | Approve | Validate domain accuracy |
| Create/edit eval dataset rows | Provide domain input | **Primary author** | Review | Score calibration |
| Score eval outputs (human review) | Calibrate with QC | **Primary scorer** | — | Gold-standard scoring |
| Edit pipeline code (.py) | No | No | **Primary author** | No |
| Edit infrastructure/deployment configs | No | No | **Primary author** | No |
| Build tools | No | No | **Primary author** | No |
| Build agent/orchestrator | No | No | **Primary author** | No |
| Run evals on own PR | Yes (required) | Yes (required) | Yes (required) | — |
| Approve PRs (skill/KB changes) | Yes (peer review) | No | Yes (required) | Optional |
| Approve PRs (code changes) | No | No | Yes (required, different from author) | No |
| Merge to main | No | No | Yes | No |
| Deploy to production | No | No | Yes + Leadership approval | No |

**Key principle:** SAs own domain content (skills, KBs). QC owns quality measurement (eval datasets, scoring). Engineers own code (tools, agent, infra). SMEs validate domain accuracy when consulted. Everyone runs evals on their own work before submitting PRs.

**Common Git Mistakes and Fixes:**

| Mistake | Symptom | Fix |
|---------|---------|-----|
| Forgot to create branch, edited on main | `git status` shows changes on main | Ask engineer to move changes to branch; do NOT try fixing yourself |
| Merge conflict | Git says "CONFLICT" when pulling | Do NOT attempt to resolve; post in team channel; engineer will handle |
| Pushed to wrong branch | PR looks wrong | Ask engineer; do NOT use `git push --force` |
| Want to undo change | File is messed up | `git checkout -- <file>` undoes uncommitted changes; if already committed, ask engineer |

**Onboarding requirement:** 30-minute guided walkthrough with an engineer on sandbox repo BEFORE first PR contribution — MANDATORY.

**Things you must NEVER do:**
- Commit API keys or secrets
- Use `git push --force` (bypasses review)
- Edit directly on `main` branch
- Attempt to resolve merge conflicts yourself if you're not an engineer — post in team channel

### How Non-Engineers Contribute Using Cursor/Claude Code

This is the primary workflow for Solution Architects and QC team to make skill/KB changes:

```
1. Pull latest main: git pull origin main
2. Create branch: git checkout -b skill/csr-s11-add-interpretation-rule
3. Open skill file in Cursor
4. Use Cursor's AI chat to discuss the change:
   "I want to add a rule that Section 11 should interpret exposure duration
    relative to the planned treatment period. Help me write this rule."
5. Cursor suggests rule text — review for domain accuracy
6. Edit the skill file directly
7. Run local eval: python run_eval.py --dataset csr-section-11 --mode quick
8. If pass: commit and push
   git add skills/mwa/csr-s11-authoring.md
   git commit -m "skill: add exposure interpretation rule to S11"
   git push origin skill/csr-s11-add-interpretation-rule
9. Create PR using the template below
10. Wait for engineer review + CI checks
```

**What Non-Engineers Should NOT Do in Cursor:**
- Don't modify Python files beyond simple variable changes
- Don't change import statements or dependencies
- Don't modify CI/CD configs, Dockerfiles, or infrastructure files
- Don't resolve merge conflicts on code files
- Don't use `git push --force` ever

### Conflict Resolution — How to Handle Overlapping Work

#### Preventing Conflicts Before They Happen

| Mechanism | How It Works | When to Set Up |
|-----------|-------------|----------------|
| **Task ownership visibility** | Before starting work, post in team channel: "I'm working on `skills/sca/section-layout.md` on branch `skill/layout-improve`". Others see this and coordinate. | Day 1 |
| **CODEOWNERS file** | Defines who must review each directory. If two people need to modify the same area, CODEOWNERS ensures at least one reviewer sees both changes. | Week 1 |
| **Small, focused branches** | Each branch changes 1-3 files for one purpose. The smaller the change, the less likely it conflicts. Target: branches live < 2 days before PR. | Always |
| **Pull before push** | Always `git pull origin main` before starting AND before pushing. Catches divergence early. | Always |

#### When Two People Deliberately Work on the Same Files

This happens — e.g., two SAs both need to update the same skill file for different improvements.

| Step | Action |
|------|--------|
| 1 | **Communicate first.** Agree who goes first. Person A's PR merges first, Person B rebases after. |
| 2 | **Person A** creates branch, makes changes, runs eval, submits PR. |
| 3 | **Person A's PR merges** (after review + eval pass). |
| 4 | **Person B** rebases their branch on latest main: `git pull origin main && git rebase main` |
| 5 | If rebase has conflicts → **see conflict resolution below**. |
| 6 | **Person B** re-runs eval (critical — the combined effect of both changes must pass). |
| 7 | **Person B** submits PR. Reviewer checks: does the combined result still meet quality gates? |

**If this coordination overhead is too high:** Have both people work on the same branch together (pair/mob style). One branch, one PR, shared ownership.

#### Resolving Merge Conflicts

| Who | What They Do |
|-----|-------------|
| **Non-engineers (SAs, QC)** | **Do NOT attempt to resolve merge conflicts yourself.** Post in the team channel: "I have a conflict on `skill/my-branch`." An engineer will resolve it. This is a hard rule — resolving conflicts incorrectly can lose work. |
| **Engineers** | Resolve conflicts on code files. For skill/KB conflicts (`.md` files), consult the relevant SA to decide which version of the content is correct. Use `git mergetool` or manual resolution. |
| **Using AI for conflict resolution** | AI tools (Cursor, Claude Code) can help engineers understand conflicts in code files — show both versions, explain what changed. However, **AI should never auto-resolve and commit without human review.** For skill files, the SA must verify the domain content is correct after resolution. |

#### Conflict Resolution by Scenario

| Scenario | Resolution |
|----------|-----------|
| Same skill, different changes | Second PR to merge must rebase on latest main, re-run evals, verify combined effect |
| Same code file, different changes | Engineer resolves conflict. Both original authors verify their intent is preserved. Re-run all tests. |
| Competing approaches to same problem | Escalate to solutioning workshop — don't resolve in PR comments |
| Engineer + non-engineer disagree on implementation | Engineer has final say on code; SA has final say on domain content |
| Two PRs both touch eval datasets | Merge sequentially. Second PR must verify no duplicate or conflicting rows. |

### Guardrails to Prevent Non-Engineers from Breaking Things

Implement in this order:

| Priority | What | When | Detail |
|----------|------|------|--------|
| **Day 1** | Branch protection on `main` | Immediately | No direct pushes, require PR reviews, require status checks. 5 minutes in GitHub settings. |
| **Day 1** | PR template | Immediately | Add `.github/PULL_REQUEST_TEMPLATE.md` |
| **Week 1** | Pre-commit hooks | First week | Blocks commits that modify `.py`, `.yml`, `Dockerfile` unless committer is engineer. Safety net, not security boundary. |
| **Week 1** | CODEOWNERS file | First week | Documents who must review which directories |
| **Week 2+** | CI checks on PR | Ongoing | Any PR touching `.py`, `.yml`, `Dockerfile`, `requirements.txt` flagged automatically |

**CODEOWNERS example:**
```
/infrastructure/    @engineer-team
/deployment/        @engineer-team
/pipeline/*.py      @engineer-team
/skills/            @solution-architect @engineer-team
/knowledge-bases/   @solution-architect
/eval-datasets/     @solution-architect @qc-team
```

> Note: CODEOWNERS enforcement (auto-required reviews) requires GitHub Team plan or higher. On GitHub Free, it serves as documentation; engineers must manually verify.

### Eval Proof Before Pushing — Non-Negotiable

**No PR may be submitted without eval results.** This is the single most important quality gate in the build phase.

**Before pushing your branch, you must:**

| Step | What | Command | Who |
|------|------|---------|-----|
| 1 | Run quick eval locally | `python run_eval.py --dataset {relevant-dataset} --mode quick` | PR author |
| 2 | Verify zero data accuracy FAILs | Check eval output — any FAIL on data accuracy is a blocker | PR author |
| 3 | Verify weighted score >= 0.80 | Check eval output — below threshold means the change regresses quality | PR author |
| 4 | Check for regressions | Compare scores on previously-passing rows — no row should drop more than 0.1 | PR author |
| 5 | Paste eval output into PR description | Copy-paste the full eval output, not just "it passed" | PR author |
| 6 | Reviewer verifies eval is real | Read the pasted output. Are the numbers plausible? Does the dataset match the change? | Reviewer |

**What counts as eval proof:**
- The actual eval runner output showing per-row scores and per-dimension breakdown
- NOT a checkbox saying "I ran evals"
- NOT a screenshot (too easy to fake)
- If eval runner is not yet available (early sprints): manual test results on 3+ inputs with specific observations

**If you skip eval:**
- Reviewer must reject the PR. No exceptions.
- If it's merged without eval and causes a regression: post-mortem + add the missing eval as a new row.

### PR Template — Every PR Must Include This

```
## What changed
[1-3 sentences: what you modified and why]

## Type of change
- [ ] Skill modification
- [ ] Knowledge base update
- [ ] Eval dataset change
- [ ] Pipeline/code change
- [ ] Configuration change

## Files changed
[List the specific files]

## Eval results
- Before: [weighted score on quick eval]
- After: [weighted score on quick eval]
- Data accuracy: [PASS/FAIL]
- Rows tested: [N]

## Testing done
- [ ] Ran locally on 3+ test cases
- [ ] Ran quick eval (5 rows)
- [ ] Checked for regressions on previously-passing rows
- [ ] No API keys or secrets in committed files

## Checklist
- [ ] Branch is up to date with main
- [ ] Changes limited to files I should be editing (see permission matrix)
- [ ] PR description explains WHY, not just WHAT
```

**Required Reviewers:**

| Change Type | Required Reviewers |
|-------------|-------------------|
| Skill/KB changes | 1 peer SA + 1 engineer |
| Code changes | 1 engineer (different from author) |
| Infrastructure changes | Both engineers |

**PR must pass before merge:** All Tier 1 checks + Tier 2 quick eval.

### Engineer Review Checklist for AI-Generated Code

When reviewing a PR (especially changes from Cursor/Claude Code):

- [ ] **Does it do what the PR says?** Read the diff, not just the PR description
- [ ] **No unintended side effects?** Check if change affects other files or flows
- [ ] **No hardcoded values?** API keys, file paths, model names should be config-driven
- [ ] **No security issues?** Client data not logged; no secrets in code
- [ ] **Eval results look real?** Check that eval was actually run (not just checkbox ticked)
- [ ] **Performance OK?** For code changes: no unnecessary API calls, no unbounded loops
- [ ] **Style consistent?** Follows existing patterns in codebase
- [ ] **Commit history clean?** No "fix typo" x10 commits — squash if needed

### 3-Tier Testing — How It Works

#### Tier 1: Automated Code Checks (Every Commit)

Runs automatically. Takes 30 seconds. Costs $0.

| Check | What It Validates |
|-------|------------------|
| Python syntax (Ruff/flake8) | No syntax errors |
| Secrets detection (detect-secrets / trufflehog) | No API keys, passwords, tokens |
| Skill file schema | Frontmatter has required fields (name, version, product_area, section, execution_mode) |
| KB file format | JSON/YAML is valid, required fields present |
| Eval dataset schema | JSON is valid, all rows have required fields, scores in valid ranges |
| Output schema validation | If output has expected structure (e.g., citations), validate schema |
| Import check | No missing Python imports |
| No hallucinated drug names | Only drug names from protocol appear in output |
| Cross-reference validity | Any "see Section X" references point to real section numbers |

**If Tier 1 fails:** PR is blocked. Fix the issue and push again.

**Phased CI Rollout (don't try to do everything at once):**

| Phase | What | When | Detail |
|-------|------|------|--------|
| **Phase 0** | Local pre-commit hooks only | Week 1 | `pre-commit` framework. Engineer sets up once, everyone installs with `pre-commit install`. |
| **Phase 1** | GitHub Actions runs Tier 1 on every PR | Week 2-3 | Single workflow file, no secrets needed. Uses GitHub Actions free 2,000 min/month. |
| **Phase 2** | GitHub Actions runs Tier 2 LLM-as-Judge on PRs | Month 2 | Requires storing API key as GitHub Secret. |
| **Phase 3** | Scheduled jobs, deployment triggers, cost monitoring | Month 3+ | Only after team is stable on Phases 0-2. |

**Before Phase 2 is ready:** Run Tier 2 evals manually. PR author runs `python run_eval.py --mode quick` locally and pastes output into PR description. Reviewing engineer verifies results are plausible.

#### Tier 2: LLM-as-Judge Evals (Every PR)

Runs on PR creation. Takes 5-10 minutes. Costs $0.50-$2.00.

| Step | Detail |
|------|--------|
| Dataset | "Quick eval" subset: 5 rows (2 easy, 2 medium, 1 hard) |
| Judge model | Opus or Sonnet — NEVER the same model that generated the output |
| Time limit | 5-10 min total. If longer, something is wrong. |
| Pass criteria | Weighted score >= 0.80 on all rows. Zero FAIL on data accuracy. |
| Output | Scores posted as PR comment with per-dimension breakdown |

**If Tier 2 fails:**
1. Read per-dimension scores — identify which dimension failed
2. Data accuracy FAIL → skill is misinterpreting source → fix skill
3. Completeness drop → skill skipping a subsection → check skill instructions
4. Interpretation drop → skill wording needs refinement → update conventions KB
5. Push fix, Tier 2 re-runs automatically
6. If stuck after 2 attempts → escalate to Solution Architect

**Handling Flaky Evals (LLM Non-Determinism):**
- Run each eval row 2x. If scores differ by > 0.3, run 3rd time and take median.
- If same row is flaky across 3+ PRs: rubric is ambiguous or row is poorly defined — fix it.
- Track flaky rows in `flaky_evals.json` — flagged for human review rather than blocking merge.
- Set temperature to 0 for all eval judge calls (maximum determinism).

#### Tier 3: Human Review (Weekly)

QC/SME team reviews 10 outputs. Takes 2-3 hours. Validates that automated evals are actually catching real issues.

**Process:**
1. System generates 10 outputs from latest production skill versions, using inputs sampled from: 3 easy, 4 medium, 3 hard
2. QC team reviews all 10 WITHOUT seeing LLM-as-Judge scores first
3. QC scores each output on all dimensions using same rubric
4. Compare human scores vs. LLM-as-Judge scores from same outputs
5. Document: agreement rate, systematic biases, new failure patterns
6. New failure patterns become new eval dataset rows

**Weekly Quality Report Output (1-page summary):**
- Average quality score this week vs. last week
- Any new failure patterns identified
- LLM-Judge vs. Human agreement rate
- Recommendations: skill changes needed, KB updates, eval dataset additions

### Auto-Refinement Guardrails

When using AI to improve skills automatically:

| Guardrail | Limit |
|-----------|-------|
| Max skill modifications per session | 5 |
| Max cost per session | $50 |
| Human review | ALL changes reviewed before merge |
| Hold-out set | NEVER shown to auto-refinement agent — only used for final validation |
| Regression check | Every accepted change re-tested against previously-passing rows |

### Gate 3 Checklist

- [ ] Eval suite passes at agreed threshold (default: 85%+ weighted score)
- [ ] Zero FAIL on data accuracy dimension (binary, no tolerance)
- [ ] No single eval row below 0.70 weighted score
- [ ] Hold-out set passes (rows never seen during auto-refinement)
- [ ] Auto-refinement has run with documented improvement trajectory
- [ ] Cost per output within target
- [ ] Latency within target
- [ ] All code reviewed and approved by engineer (per CODEOWNERS)
- [ ] Known limitations documented
- [ ] Regression suite exists for ongoing monitoring

### When Things Go Wrong

| Blocker | Resolution |
|---------|-----------|
| No engineer available for code review | SA self-reviews skill/KB changes (not code changes). Code changes wait for engineer — this is a hard requirement. If > 3 days: escalate to leadership. |
| Auto-refinement plateaus (quality stops improving) | Revisit architecture from Stage 2. Problem may need a different complexity level. |
| Eval dataset seems wrong (system passes but output looks bad) | Flag to QC for rubric review. Eval may be miscalibrated. |
| Cost per run exceeds target | Check: are we using right model for task? Can chain work instead of agent? Can we reduce token count? |

---

## STAGE 4: DEPLOY & VALIDATE

**Purpose:** Move from dev to production with safeguards.
**Applies to:** Type A, B, C engagements (D is fast-tracked).
**Time:** 1-3 days.

### Environment Progression

```
Local Dev → Sandbox (per-branch) → Shared Dev → Staging → Production
   |              |                      |            |           |
   |              |                      |            |           +-- Real client data, real traffic
   |              |                      |            +-- Full eval suite, client-specific datasets
   |              |                      +-- Integration testing, team visibility
   |              +-- Individual feature testing before merge
   +-- Individual testing, quick iteration
```

| Environment | Who Has Access | Data | Eval Level | Deployment |
|-------------|---------------|------|-----------|-----------|
| Local Dev | Individual developer | Synthetic/sample data | Tier 1 + Tier 2 quick | Automatic (local run) |
| Sandbox | Individual developer | Synthetic/sample data | Tier 2 quick | Per-branch deploy |
| Shared Dev | Full GenAI team | Anonymized client data | Tier 2 full eval | Push to branch triggers |
| Staging | GenAI team + Engineering | Client data (restricted) | Full eval + hold-out | Manual trigger after Build Gate |
| Production | Monitored access only | Live client data | Continuous monitoring | Manual trigger after Deploy Gate |

> **9 April addition — Sandbox environment:** Engineers can deploy individual feature branches to sandbox for testing before merging to Dev. This prevents features from colliding during testing.

### Environment Parity — Closing the Local-vs-Production Gap

If eval passes locally but fails in staging/production, one of these is the cause:

| Divergence | What Goes Wrong | Mitigation |
|-----------|----------------|-----------|
| **Python/dependency versions** | Code works on dev (3.11) but fails in container (3.10) | Pin Python version in `.python-version`. Use `pip freeze > requirements.txt`. All envs install from same file. |
| **Model access** | Dev uses personal API key with different rate limits | Use environment variables for all API keys. Local and CI use same model version from shared config (`config/models.yaml`). |
| **Data format** | Local tests use clean samples; production gets messy PDFs with OCR artifacts | Eval datasets must include 2-3 rows with "messy" real-world inputs. Do not only test on clean samples. |
| **File paths / OS differences** | Hardcoded paths, Windows vs. Linux separators | Use `pathlib` for all file paths. Never hardcode absolute paths. CI runs on Linux (same as production). |
| **Environment variables** | Missing or differently-named env vars | Maintain `.env.example` listing all required vars (without values). CI startup validates all required vars are set. |
| **Secrets** | API keys passed differently (env var locally, Secrets Manager in production) | Single config loading pattern that checks: env var → secrets manager → config file. Same code path everywhere. |

**Validation step before staging promotion:** Run full eval suite inside staging container (not just locally). If scores differ by > 0.05 on weighted average, investigate before proceeding.

### Skill/KB Version Management Across Environments

```
skills/mwa-csr-s11-authoring.md
  Metadata:
    version: 2.1.0
    environment_labels:
      dev: 2.2.0-beta      # Latest experimental version
      staging: 2.1.0        # Approved for staging testing
      production: 2.0.3     # Current production version
```

**Promotion flow:**
1. Developer merges skill v2.2.0-beta to main → automatically tagged `dev`
2. Build Gate passed → SA promotes to `staging`: `python promote.py --skill mwa-csr-s11 --to staging`
3. Deploy Gate passed → Leadership approves promotion to `production`

### Step-by-Step Deployment

| Step | Action | Detail |
|------|--------|--------|
| 1 | Deploy to staging | Using deployment pipeline |
| 2 | Run full eval suite IN STAGING | Not just local — must run in deployed environment |
| 3 | Compare staging scores to local scores | If they differ by > 0.05 on weighted average, investigate before proceeding |
| 4 | Set up production monitoring | Quality spot checks, cost dashboard, error/stall alerts |
| 5 | Pin model version | Exact version, never "latest" |
| 6 | Document and test rollback procedure | Must be tested, not just documented |
| 7 | Create incident response runbook | Severity classification, escalation paths, rollback steps |
| 8 | Canary deployment (if applicable) | Small traffic percentage first |
| 9 | Deploy to production | Engineer + Leadership approval |

### Deployment to Client Environments

Some clients require deployment into their own AWS accounts or VPCs.

**Deployment Request Template (for DevOps-managed environments):**

```
Subject: Deployment Request — [Project] — [Environment]

What: [Brief description of what is being deployed]
Artifact: [Git tag or commit SHA, container image tag, or S3 path]
Environment: [staging / production]
Config changes: [Any env var changes, new secrets needed, infrastructure changes]
Rollback plan: [How to revert — specific previous version/tag]
Urgency: [Routine / Expedited / Emergency]
Requestor: [Name]
Approver: [Leadership for production deployments]

Pre-deployment checklist:
- [ ] Full eval suite passes at threshold
- [ ] Rollback version identified and tested
- [ ] No new infrastructure dependencies (or they are listed above)
```

**Turnaround SLAs (agree with DevOps team):**
- Routine: 2 business days
- Expedited (client-facing deadline): same business day
- Emergency (production down): 2 hours

**Post-Deployment Verification (engineer must do):**
- Run 3-5 smoke test requests against deployed environment
- Verify deployed version matches requested version (check `/health` or `/version` endpoint)
- Confirm monitoring is receiving data

### Model Version Pinning

**Policy:** Every deployment config specifies exact model version — `claude-sonnet-4-5-20250929`, never `claude-sonnet-4-5-latest`.

**Model Upgrade Process:**
1. New model version released by provider
2. Engineer updates model version in dev config only
3. Run full eval suite on all product areas against new model
4. Compare scores: new vs. current production model
5. If parity or improvement on all dimensions → promote to staging
6. 1-week soak in staging with monitoring
7. Leadership approves production promotion
8. Record: model version, eval comparison results, approval date

**Fallback on Model Outage:**
- Primary: Claude Sonnet 4.5
- Fallback: Claude Sonnet 4 (previous generation)
- Emergency: Gemini or GPT-4o (requires separate eval validation)
- Config supports model priority list; system auto-falls to next if primary returns errors

### Rollback Procedure (Must Be Pre-Tested)

```
1. DETECT: Monitoring alert fires (quality drop, error spike, latency increase)
   |
2. ASSESS (5 minutes max):
   - Is this affecting live client work? If yes — proceed immediately
   - Is this a model issue or a skill/code issue?
   |
3. ROLLBACK (engineer executes):
   a. Identify last known-good version from deployment log
   b. Run: python rollback.py --skill mwa-csr-s11 --to-version 2.0.3
   c. If pipeline code caused issue: git revert <commit-hash>
      (engineer self-approves in emergency, second engineer reviews within 4 hours)
   d. Verify: run 3 production requests with rolled-back version, check quality
   |
4. COMMUNICATE:
   - Notify team in channel within 15 minutes
   - If client-facing: notify client contact with ETA for resolution
   |
5. ROOT CAUSE (within 24 hours):
   - Why did change pass all eval gates but fail in production?
   - Add failure case to eval dataset
   - Update process if gate was insufficient
   |
6. FIX FORWARD:
   - Fix on new branch. Must pass ALL gates INCLUDING new eval row from step 5.
   - Standard PR process (not fast-tracked).
```

**Rollback when DevOps controls production:** Use same deployment request template with urgency marked "Emergency." Rollback artifact (previous version tag) must ALWAYS be pre-identified in original deployment request. Do NOT wait for production incident to figure out rollback target.

### Production Monitoring

#### Metrics to Track

| Category | Metric | Target | Alert Threshold |
|----------|--------|--------|----------------|
| **Quality** | Eval pass rate (automated spot checks) | > 85% | < 80% for 2 consecutive checks |
| | Data accuracy (programmatic check on sample) | 100% | Any failure |
| | Hallucination rate (detected fabricated data) | < 2% | > 5% |
| **Performance** | Latency p50 | < 5 min per section | p50 > 8 min |
| | Latency p95 | < 15 min per section | p95 > 25 min |
| | Agent completion rate | > 95% | < 90% |
| **Cost** | Cost per section authored | < $5 | > $10 |
| | Daily API spend | < $50 | > $100 |
| **Reliability** | Error rate (pipeline failures) | < 5% | > 10% |
| | Agent stall rate (agents that hang) | < 2% | > 5% |

#### Monitoring Tooling — Phased Approach

Don't try to set up everything at once. Start simple:

| Phase | What | Cost/Effort | When |
|-------|------|-------------|------|
| **Phase 0** | Structured logging — every run logs JSON: run_id, skill_id, version, model, latency, tokens, error, cost | Free. Engineer: 1-2 days. | Week 1 of production |
| **Phase 1** | Daily summary script — cron job posts to team channel: total runs, error rate, avg latency, cost | Free. Engineer: 0.5 day. | Week 2 |
| **Phase 2** | Threshold-based alerts — if error rate > 10% or cost > $100/day, alert team channel | Free. Engineer: 0.5 day. | Week 3 |
| **Phase 3** | Dashboard — Grafana free tier or auto-updated spreadsheet. Only if Phase 1 summaries insufficient. | Free. Engineer: 1-2 days. | Month 2+ |
| **Phase 4** | LLM tracing — Langfuse or similar for per-request traces. Only if > 50 production requests/week. | Self-hosted free or $50-200/mo. | Month 3+ |

**Key principle:** If you can't answer "how many runs did we do yesterday, how many failed, and how much did it cost?" — that is the first problem to solve.

### Incident Response

**On-call model (realistic for ~10-person team with 2 engineers):**
- **Business hours (9 AM - 6 PM, Mon-Fri):** Whichever engineer not in meeting picks up alert. If both unavailable, SA triages and decides if it can wait.
- **After hours:** Alerts accumulate. Reviewed first thing next business day.
- **Exception — SEV-1 during active client delivery:** Engineer who is reachable responds. Should be rare (< once/quarter). If frequent, escalate as resourcing issue.

**Severity Levels:**

| Severity | Definition | Response Time | Who |
|----------|-----------|--------------|-----|
| **SEV-1** | Client-facing system down; data accuracy failure in live output | Next business hour (or immediately if during active delivery) | Engineer + SA + Leadership notified |
| **SEV-2** | Quality degradation detected; system slow but functional | 4 business hours | Engineer + SA |
| **SEV-3** | Non-client-facing issue; performance degradation; cost spike | Next business day | Engineer |
| **SEV-4** | Minor issue; cosmetic; non-urgent | Next sprint | Area owner |

**Incident Process:**

```
Detection (automated alert or human report)
  |
Triage (5 min): Classify severity, assign owner
  |
Diagnose: Is this...
  +-- Model degradation? → Check model version, run eval, compare to baseline
  +-- Skill bug? → Check recent skill changes, compare outputs before/after last deploy
  +-- Data issue? → Check input data quality, source document parsing
  +-- Infrastructure issue? → Check AWS health, API quotas, network
  +-- Unknown? → Collect logs, reproduce, escalate
  |
Fix: Apply fix or rollback (see rollback procedure above)
  |
Verify: Confirm fix resolves the issue
  |
Communicate: Update stakeholders
  |
Postmortem (within 48 hours for SEV-1/2):
  - What happened?
  - Why did it get past our gates?
  - What eval row / monitoring check would have caught it?
  - Action items with owners and deadlines
```

### Security

#### API Key and Secrets Management

| Rule | Detail |
|------|--------|
| **No secrets in code, ever** | API keys, passwords, tokens must NEVER appear in source code, config files committed to git, or PR descriptions. Use environment variables or secrets manager. |
| **`.env` files are gitignored** | `.gitignore` must include `.env`, `.env.*`, `*.pem`, `credentials.json`. Verify on day 1. |
| **Secrets scanning in CI** | Tier 1 checks include `detect-secrets` or `gitleaks`. Catches accidental commits before they reach main. |
| **Separate keys per environment** | Dev, staging, production use different API keys. If dev key compromised, production not affected. |
| **Service accounts for CI** | GitHub Actions uses dedicated service account API key, not personal key. Key has spend cap matching CI budget. |
| **No secrets in Slack/Teams** | Never paste API key in chat. Share through secrets manager or short-lived secure link. |

**Secrets Rotation Schedule:**

| Secret | Rotation | Who | How |
|--------|----------|-----|-----|
| LLM provider API keys (Anthropic, OpenAI, Google) | Every 90 days or immediately if compromised | Engineer | Rotate in provider dashboard, update secrets manager, update CI secrets, verify all environments |
| AWS access keys | Every 90 days | Engineer | IAM console. Prefer IAM roles over access keys. |
| GitHub personal access tokens | Every 90 days | Individual | GitHub Settings > Developer Settings. Use fine-grained tokens with minimum required permissions. |
| Client-specific credentials | Per client security policy | Engineer + client IT | Follow client's rotation procedure. Document in engagement runbook. |

**If a secret is accidentally committed:**
1. Rotate secret immediately (generate new key, revoke old one)
2. Remove from git history (engineer uses `git filter-branch` or BFG Repo Cleaner)
3. Notify leadership if secret had access to client data or production systems
4. Add post-mortem entry: why did pre-commit hook not catch it?

#### Client Data in CI/CD and Development

| Context | Allowed | NOT Allowed |
|---------|---------|-------------|
| Eval datasets in git | Synthetic data, anonymized data, publicly available data | Real patient data, client-proprietary SOPs |
| CI/CD logs | Eval scores, skill versions, error messages | Input document content, generated output text, client names |
| Local development | Anonymized or synthetic sample data | Real client documents on personal machines without client approval |
| Shared dev environment | Anonymized client data with access controls | Client data accessible to team members not on that engagement |

#### Access Control

| Resource | Who Has Access | How Granted |
|----------|---------------|-------------|
| GitHub repository | Full GenAI team | GitHub org membership, managed by engineer |
| Production AWS environment | Engineers only (via DevOps) | Deployment request process |
| Staging environment | GenAI team + Engineering | AWS IAM roles |
| Client data (S3, shared drives) | Engagement team members only | Per-engagement access request, approved by SPOC |
| LLM provider dashboards | Engineers + Leadership | Per-provider account management |
| Monitoring dashboards | Full team (read), Engineers (write) | Set up during monitoring rollout |

**Offboarding (within 24 hours when someone leaves):** Revoke GitHub access → rotate any shared secrets they had access to → remove from engagement-specific data access. Maintain a checklist.

### Cost Tracking and Optimization

#### Tracking Granularity

Every LLM call is tagged with:
```json
{
  "project": "medcom-asset-generation",
  "client": "vertex",
  "skill_id": "medcom-visual-generation",
  "skill_version": "1.2.0",
  "stage": "production",
  "run_id": "run-2026-05-01-001"
}
```
This allows cost slicing by: project, client, skill, stage, time period.

> Start with structured logging (Phase 0 monitoring). A weekly script parsing logs and outputting summary is sufficient to start.

#### Cost Optimization Levers

| Lever | When to Use | Expected Savings |
|-------|------------|-----------------|
| **Model tiering** (Haiku for extraction, Sonnet for authoring, Opus for complex reasoning) | Always — default architecture | 40-60% vs. Opus for everything |
| **Caching** (identical inputs return cached outputs) | For repeated evals, demo runs | 20-30% on eval runs |
| **Token reduction** (shorter prompts, structured outputs) | When cost per section exceeds target | 10-20% |
| **Batching** (process multiple sections in one context window) | For independent sections sharing context | 15-25% |
| **Early termination** (stop agent if quality sufficient before max iterations) | During auto-refinement | Prevents runaway sessions |

#### Cost-Quality Tradeoff Decisions

- If cost reduction has < 5% quality impact → approve automatically
- If cost reduction has 5-10% quality impact → discuss: is threshold still acceptable?
- If cost reduction has > 10% quality impact → reject unless client explicitly agrees
- Document every cost-quality tradeoff in engagement decision log

#### Monthly Cost Report (to Leadership)

Must include: total API spend by project, cost per output, trend (increasing/decreasing), breakdown (production vs. eval vs. auto-refinement vs. development), comparison to manual cost (if available), optimization actions and their impact.

### Gate 4 Checklist

- [ ] Full eval suite passes in deployed environment (not just local)
- [ ] Monitoring dashboards live (quality, cost, performance, reliability)
- [ ] Rollback tested (procedure documented AND executed at least once)
- [ ] Incident response runbook exists with severity classification
- [ ] Model version pinned and documented
- [ ] Cost tracking tags configured per engagement
- [ ] Security: no secrets in code, separate keys per environment, `.env` gitignored
- [ ] Engineering/DevOps sign-off on deployment

### When Things Go Wrong

| Blocker | Resolution |
|---------|-----------|
| Eval scores drop significantly in staging vs local | Investigate environment parity (see table above). Do NOT push to production with unexplained score differences. |
| No DevOps support for deployment | Self-serve deployment to team-managed environment. Monitor via custom dashboards. Document as risk for scale. |
| Rollback needed but team can't access production | Use deployment request template with urgency "Emergency." Rollback artifact must always be pre-identified BEFORE original deployment. |
| Cost spike in production | Check for infinite loops, unnecessary agent spawning, auto-refinement running unmonitored. Pause non-critical workloads. |
| Secret accidentally committed | Rotate immediately, remove from git history, notify leadership if it had production/client access. |

---

## STAGE 5: OPERATE & EVOLVE

**Purpose:** Hand off to operations, maintain quality, continuously improve.
**Applies to:** Type A, B engagements. Optional for C.
**Time:** 1-2 weeks for handoff. Ongoing for operations.

### Handoff Package — Must Deliver ALL of These

| Artifact | Contents | Acceptance Criterion |
|----------|---------|---------------------|
| **Architecture docs** | System diagram, data flow, skill dependency graph, integration points | Someone NOT on the build team can explain the system from these docs |
| **Skill files with rationale** | All production skills, versioned, with metadata and linked eval datasets | Self-documenting per skill template |
| **Knowledge bases** | All structural, conventions, and corrections KBs, versioned | Linked from skills, no orphaned KBs |
| **Eval suite** | Full dataset + hold-out set + LLM-as-Judge prompts + programmatic checks | Delivery team can run: `python run_eval.py --mode full` |
| **Known limitations** | Structured table: limitation, severity, workaround, expected fix timeline | No surprises in production |
| **Operational runbook** | Step-by-step for common operations, troubleshooting tree, severity classification | Delivery team can handle L1/L2 without builder involvement |
| **Incident response plan** | Severity definitions, escalation paths, rollback steps, communication templates | Tested during Stage 4 |
| **Training sessions** | 2-3 sessions recorded: system overview, daily operations, troubleshooting | Delivery team operates independently after training |
| **Decision log** | All significant decisions with context and rationale | New team members understand WHY things are the way they are |

### Escalation Tiers Post-Handoff

| Tier | Handled By | Type of Issue | Example |
|------|-----------|--------------|---------|
| **L1** | Delivery team | Known issue with documented fix | "Pipeline stalled — restart per runbook" |
| **L2** | Delivery team + SA consult | Known issue type but novel specifics | "New document format causing parsing error" |
| **L3** | Build team | Requires skill/KB/code change | "Section 11 consistently misinterpreting dose modifications" |
| **L4** | Leadership | Requires architectural or strategic decision | "Entire approach needs rethinking for this client" |

### Production Feedback Loop

```
Client/SME reviews output → provides comments/edits
  → QC classifies each comment:

    A) Factual error (wrong number, wrong drug name)
       → Add as regression test row with data_accuracy = FAIL
       → Route to build team for skill fix

    B) Missing content (subsection incomplete)
       → Add as row with completeness < 1.0
       → Route to SA for skill review

    C) Style/convention preference (client wants different tone)
       → Add to client-specific corrections KB
       → Add as row in client-specific eval dataset

    D) Out-of-scope request (feature system doesn't do)
       → Log as feature request, NOT added to eval dataset
       → Goes through Intake (Stage 0) for classification
```

### Monitoring Cadence (Post-Deploy)

| What | Frequency | Who |
|------|-----------|-----|
| Automated quality spot checks | Daily | Automated |
| Cost dashboard review | Daily | Engineer |
| Error rate monitoring | Real-time alerts | Automated → Engineer |
| Tier 3 human review | Weekly | QC team |
| Full eval suite re-run | Bi-weekly | Automated |
| Quality trend report to stakeholders | Monthly | SA |

### Gate 5 Checklist

- [ ] Handoff package complete (all artifacts above) and reviewed by delivery team
- [ ] Delivery team trained (2-3 sessions minimum, recorded)
- [ ] Delivery team can run eval suite independently
- [ ] Escalation path defined and agreed (L1/L2/L3/L4)
- [ ] Eval monitoring ownership transferred
- [ ] Support warranty period defined (how long builders remain available)
- [ ] "Weeks to independence" tracking started (target: zero L3 escalations within N weeks)

---

## CROSS-CUTTING: APPLIES TO ALL STAGES

### Scope Change Process

```
Request for change arrives (client or internal)
  │
  ├─ Step 1: ACKNOWLEDGE. "Let me assess the impact."
  │          Do NOT agree or commit on the call.
  │
  ├─ Step 2: IMPACT ASSESSMENT (2-4 hours)
  │          - Does this change the eval rubric?
  │          - Does this need new skills or KB entries?
  │          - Effort estimate?
  │          - Timeline impact?
  │          - Cost impact?
  │
  ├─ Step 3: PRESENT OPTIONS
  │          (a) Add to scope with adjusted timeline
  │          (b) Replace another item
  │          (c) Defer to Phase 2
  │
  ├─ Step 4: GET EXPLICIT AGREEMENT. Document the decision.
  │
  └─ Step 5: UPDATE requirements, eval dataset, sprint backlog, stakeholder comms
```

**Key principle:** Scope changes are not failures. But every change has a cost. The cost must be made visible. Stop absorbing changes silently.

### Cost Governance

| Spend Level | Action Required |
|-------------|----------------|
| < $10/day per project | Normal operations, auto-approved |
| $10-50/day | SA reviews |
| $50-100/day | Leadership notified |
| > $100/day | Leadership approval to continue |
| Any single run > $20 | Engineer reviews after the fact |

### Communication Cadence

| Meeting | Frequency | Duration | Purpose |
|---------|-----------|----------|---------|
| Daily standup | Daily | 15 min | Blockers and coordination |
| Sprint review | Bi-weekly | 1 hour | Demo actual outputs (including failures), eval score trends |
| Tech talk | Bi-weekly (alternates with sprint review) | 1 hour | Deep-dive by one team member |
| Leadership update | Bi-weekly | 30 min | Metrics deck + demo + ask |
| Engineering sync | Weekly | 30 min | Cross-team coordination |
| WoW retro | Quarterly | 2 hours | Process improvement |
| Client status | Weekly (written) + Monthly (demo) | — | Per engagement |

### Time Allocation Target

| Category | Target | Note |
|----------|--------|------|
| **Building** (product development) | **60-70%** | This is the core. Startup competitors operate at 100%. |
| **Delivery** (client support, BAU) | **20-30%** | Must push back when this creeps up. |
| **Learning** (upskilling, research) | **10%** | Protected time. Not optional. |

> Changed from 60-30-10 (Delivery-Building-Learning) to 20-60-10 based on 9 April decision. Building must dominate to compete with product-focused companies.

**Protected time:** Designate specific afternoon blocks as no-meeting time for focused build work. Track build progress in sprint alongside delivery. If build progress is zero for 2 consecutive sprints, escalate.

### Escalation Path

| Level | When | Who Decides |
|-------|------|-------------|
| L1 | Day-to-day issues, scope within team | STO / SA |
| L2 | Cross-team dependency, resource conflict | Senior Manager |
| L3 | Strategic direction, budget approval, org-level | Director |
| L4 (max) | Existential / fundamental direction | VP / CTO |

### Knowledge Management

| Knowledge Type | Location | Owner |
|---------------|----------|-------|
| Skills and KBs | Git repo: `/skills/`, `/knowledge-bases/` | Skill owner |
| Eval datasets | Git repo: `/eval-datasets/` | QC team |
| Architecture decisions | Git repo: `/decisions/` | Decision participants |
| Post-mortems | Git repo: `/postmortems/` | Incident owner |
| "What we tried & learned" | Git repo: `/learnings/` | Anyone |
| Client engagement docs | Shared drive (restricted) | Engagement SPOC |

**Onboarding new team members:**
1. Give them access to this process map and the code repo
2. They use Cursor/Claude Code to explore the codebase — come back with questions
3. Generate flowcharts from codebases using AI tools as standard practice
4. Buddy pairing for first 2 sprints
5. No spoon-feeding — self-service first, ask questions second

---

## QUICK REFERENCE: THE ENTIRE PROCESS IN ONE VIEW

```
REQUEST IN
    │
    ▼
┌─────────────────────────────────────┐
│  STAGE 0: INTAKE & CLASSIFICATION   │  30 min
│  Classify (A-F) → Assign STO        │
│  → Determine applicable stages      │
│                                     │
│  GATE: Type assigned? STO assigned? │
│         In backlog?                  │
└───────────────┬─────────────────────┘
                │
    ┌───────────┼──────────────────────┐
    │           │                      │
    ▼           ▼                      ▼
  Type A      Type B               Type C/D
    │         (skip to              (skip to
    ▼          Stage 2)              Stage 3)
┌─────────────────────────────────────┐
│  STAGE 1: REQUIREMENT & SCOPING     │  2-3 days
│  Discovery → Scalability params     │
│  → Golden dataset plan → Rubric     │
│  → Client sign-off                  │
│                                     │
│  GATE: Rubric signed off?           │
│         Dataset plan exists?         │
│         Scalability defined?         │
└───────────────┬─────────────────────┘
                │
                ▼
┌─────────────────────────────────────┐
│  STAGE 2: SOLUTIONING WORKSHOP      │  1-3 hours
│  Complexity ladder → Architecture   │
│  → Skills map → KB requirements     │
│  → Non-functional requirements      │
│                                     │
│  GATE: Architecture documented?     │
│         Complexity justified?        │
│         Skills assigned?             │
└───────────────┬─────────────────────┘
                │
                ▼
┌─────────────────────────────────────┐
│  STAGE 3: BUILD & TEST              │  Days-Weeks
│  Write skills/KBs → Build eval      │
│  → 3-Tier testing → Auto-refine     │
│  → PR review → Iterate              │
│                                     │
│  GATE: Eval >= 85%? Data accuracy   │
│         PASS? Hold-out passes?       │
│         Code reviewed?               │
└───────────────┬─────────────────────┘
                │
                ▼
┌─────────────────────────────────────┐
│  STAGE 4: DEPLOY & VALIDATE         │  1-3 days
│  Staging deploy → Eval in staging   │
│  → Monitoring setup → Rollback test │
│  → Pin model version → Production   │
│                                     │
│  GATE: Eval passes in staging?      │
│         Monitoring live?             │
│         Rollback tested?             │
└───────────────┬─────────────────────┘
                │
                ▼
┌─────────────────────────────────────┐
│  STAGE 5: OPERATE & EVOLVE          │  1-2 weeks + ongoing
│  Handoff package → Train delivery   │
│  → Transfer monitoring → Warranty   │
│  → Feedback loop → Continuous       │
│    improvement                      │
│                                     │
│  GATE: Handoff complete? Team       │
│         trained? Can run evals       │
│         independently?               │
└─────────────────────────────────────┘
```

---

## TYPE D (BUG FIX) FAST-TRACK

Bug fixes skip the full process. Here is the exact sequence:

```
1. Identify the bug (what is the system doing wrong vs. skill instructions?)
2. Create branch: fix/{area}-{short-description}
3. Fix the skill, KB, or code
4. Run quick eval (5 rows) — must pass, zero regressions
5. Add a new eval row that specifically catches this bug (regression test)
6. Submit PR with eval results
7. Engineer reviews and approves
8. Deploy
```

**Time:** Same day for simple fixes. 1-2 days if eval dataset needs new rows.

---

## PHARMA REGULATORY CHECKLIST

Ask these during Stage 1 discovery. If client answers "yes" to GxP or 21 CFR Part 11, escalate to Leadership immediately — these fundamentally change cost, timeline, and architecture.

| Requirement | Question | Implication |
|-------------|----------|------------|
| **Audit trail** | Need to trace every output back to source data? | Log model version, skill version, KB version per output |
| **GxP validation** | Is this a GxP system (IQ/OQ/PQ required)? | Drastically changes deployment and testing |
| **21 CFR Part 11** | Need electronic signatures, tamper-proof audit logs? | Specific technical controls required |
| **Data classification** | What sensitivity level? (public / confidential / restricted / patient-level) | Determines if data can go to third-party LLM APIs |
| **Model explainability** | Need to explain how AI reached output? | May need confidence scores, uncertainty indicators |
| **Change control** | Require formal change control for skill updates? | PR becomes formal change request with impact assessment |
| **Retention** | How long must outputs be retained? | Pharma typically 15+ years |

**Default position for most current engagements:** System produces drafts that humans review. It's a "productivity tool," not a "validated system." Frame to clients: "Your team's review is the validation step. Our eval framework ensures draft quality is consistently high enough for efficient review."
