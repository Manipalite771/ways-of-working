# GenAI Ways of Working — Process Map (Level 1)

> **What this is:** A scannable quick-reference for every stage. Each step is one line — enough to know what to do. If you need the full detail behind any line, go to the Process Map (Level 2) in the portal.

---

## ENGAGEMENT TYPE ROUTING

| Type | What | Stages |
|------|------|--------|
| **A** — New Product / Major Feature | Greenfield build or major new capability | 0 → 1 → 2 → 3 → 4 → 5 (all) |
| **B** — Significant Enhancement | New section type, new doc format, skill overhaul | 0 → 2 → 3 → 4 → 5 |
| **C** — Skill/KB Improvement | Quality improvement on existing capability | 0 → 3 → 4 |
| **D** — Bug Fix | System not behaving per skill instructions | Fix → Eval → Review → Deploy |
| **E** — Internal Tooling | Tools for team workflow, not client-facing | 0 → 2 (light) → 3 |
| **F** — Demo / Benchmark | BD demo, competitive analysis | 0 → 2 (light) → time-boxed build |

**Quick classifier:** Bug? → D. Only skills/KBs change? → C. Internal use? → E. One-off demo? → F. Needs solutioning workshop? → A. Needs new eval data? → A or B. Everything else → B.

---

## STAGE 0: INTAKE & CLASSIFICATION

**Time:** 30 minutes

| # | What to do | Detail |
|---|-----------|--------|
| 1 | Log the request | Capture source — client, internal, or production monitoring alert |
| 2 | Classify engagement type (A–F) | Use decision tree above; if unclear, default one level higher |
| 3 | Assign Single-Threaded Owner (STO) | One person accountable for this work end-to-end |
| 4 | Identify applicable stages | Based on engagement type — see routing table |
| 5 | Assign priority (P0–P3) | P0 = production down (same day), P1 = client-caught (2 days), P2 = planned (next sprint), P3 = backlog |
| 6 | Enter into backlog | With type, STO, stages, and priority all documented |

**Gate 0 Checklist:**
- [ ] Engagement type classified (A/B/C/D/E/F)
- [ ] STO assigned
- [ ] Applicable stages identified
- [ ] Priority assigned (P0–P3)
- [ ] Entered into backlog

---

## STAGE 1: REQUIREMENT & SCOPING

**Time:** 2–3 days of effort over 1–2 weeks
**Applies to:** Type A. Type B only if requirements are not already clear.

| # | What to do | Detail |
|---|-----------|--------|
| 1 | Intake call (30 min) | Understand problem at high level with BD/client lead; confirm engagement type |
| 2 | Discovery session (1–2 hrs) | Collect with SME/domain expert present: manual process walkthrough, input sources, output specs, 3–5 good examples, bad examples, SOPs, style guides |
| 3 | Define scalability parameters | Max processing time, concurrent users, onboarding time (doc/template/client), error rate tolerance, cost per output, rework rate |
| 4 | Plan golden dataset (2–4 hrs) | Identify input-output pairs from examples; define 3–5 scoring dimensions (accuracy, completeness, interpretation, compliance, style); draft rubric; estimate row count |
| 5 | Draft requirements document | Problem statement, in-scope/out-of-scope, success criteria (quantified), input/output spec, quality thresholds, scalability params, deployment needs, regulatory requirements |
| 6 | Internal review (1 hr) | Engineer validates technical feasibility; leadership confirms capacity and strategy alignment |
| 7 | Client sign-off (30 min + async) | Walk through rubric — "you're signing off on how we measure quality." Get explicit written agreement (email minimum) |

**Gate 1 Checklist:**
- [ ] Golden dataset exists OR plan + timeline to create it
- [ ] Scoring dimensions defined with rubric (3–5 dimensions)
- [ ] Success parameters quantified and agreed (accuracy, latency, cost)
- [ ] Scalability parameters defined (time, users, error rate, cost)
- [ ] Deployment environment identified
- [ ] Stakeholders identified and engagement model defined
- [ ] Client sign-off on rubric obtained (email confirmation minimum)
- [ ] Risk register initialized
- [ ] Competitive landscape documented (what commodity tools do, where we differentiate)

---

## STAGE 2: SOLUTIONING WORKSHOP

**Time:** 3 hrs (Type A), 1.5 hrs (Type B), 1 hr (Type E/F)
**Applies to:** Type A (full), Type B (compressed), Type E/F (lightweight).

| # | What to do | Detail |
|---|-----------|--------|
| 1 | <a href="javascript:void(0)" onclick="goDetail('poc-before-workshop-mandatory')">POC completed before workshop</a> | A lightweight POC (2–5 days) must be done before the workshop. Tests the riskiest assumption. Concrete results (eval scores, latency, cost) shared in pre-workshop packet. Without POC data, workshops are opinion debates. |
| 2 | Send pre-workshop packet (1–2 days before) | Requirements summary, POC results, <a href="javascript:void(0)" onclick="goDetail('pre-workshop-1-2-days-before')">2–3 possible approaches with pros/cons</a> (not just one recommendation), reusable components, constraints, SME availability confirmed |
| 3 | Context setting (15 min) | Confirm everyone understands requirements; summarize POC results; state decisions to be made. **SMEs must attend or be on-call** for domain feasibility validation. |
| 4 | <a href="javascript:void(0)" onclick="goDetail('the-complexity-ladder-use-this-to-decide-architecture')">Walk the Complexity Ladder</a> | Decide architecture level: L1 Simple Chain → L2 Router → L3 Parallel → L4 Agent → L5 Multi-Agent. Default to lowest that works. Every step up must cite evidence from POC. |
| 5 | Discuss alternative approaches | Walk through 2–3 approaches from pre-workshop packet. Each gets 5 min to present, then group discussion. <a href="javascript:void(0)" onclick="goDetail('workshop-agenda-type-a-3-hours')">Do NOT converge on one approach until all have been heard.</a> SME validates domain feasibility for each. |
| 6 | Design architecture | Agent topology, skill map, data flow. Which skills exist vs. need creation. KB requirements. Estimate LLM calls and cost per run. Engineer validates feasibility. SME validates domain coverage. |
| 7 | Define non-functional requirements | Latency budget, concurrency, cost ceiling, security, deployment environment, pharma-specific (audit trail, data classification, retention) |
| 8 | Decide and assign (30 min) | State decision with rationale. Assign skill owners. Set timeline with milestones. Capture all action items with owners + deadlines. |
| 9 | Document workshop outputs | Architecture diagram, complexity decision record, skills map with owners + effort, KB requirements, eval dataset plan, risk register update |

**Gate 2 Checklist:**
- [ ] Architecture documented (diagram + decision record) and peer-reviewed
- [ ] Complexity level justified with evidence (not architectural ambition)
- [ ] Agent vs. non-agent decision explicitly documented with rationale
- [ ] Skills map finalized: existing (reuse), to-create, to-modify — with owners and effort
- [ ] KB requirements identified (structural, conventions, corrections)
- [ ] Engineering sign-off on feasibility (or documented note proceeding without it)
- [ ] Cost estimate within acceptable range
- [ ] Non-functional requirements defined (latency, concurrency, cost ceiling)
- [ ] Scalability approach defined (how will system meet Stage 1 parameters?)
- [ ] Risk register updated

---

## STAGE 3: BUILD & TEST

**Time:** Type A: 2–4 sprints. Type C: 1–2 days. Type D: same day.
**Applies to:** All engagement types (rigor varies).

| # | What to do | Detail |
|---|-----------|--------|
| 1 | Codebase access provided to all | Repo access granted; branch protection enabled on `main` (no direct pushes, require PR reviews) |
| 2 | Branch + contribution model decided | Trunk-based dev with short-lived branches; naming: `{type}/{area}-{description}` (e.g., `skill/csr-s11-add-rule`) |
| 3 | <a href="javascript:void(0)" onclick="goDetail('who-does-what-build-phase-permission-matrix')">Role-based permissions set</a> | SAs own skills + KBs (primary author). QC owns eval datasets + scoring. Engineers own code + tools + infra. SMEs validate domain accuracy. Everyone runs evals on own work. Engineers approve + merge all PRs. |
| 4 | CODEOWNERS + PR template configured | CODEOWNERS defines review ownership per directory; <a href="javascript:void(0)" onclick="goDetail('pr-template-every-pr-must-include-this')">PR template</a> requires: what changed, eval before/after, testing checklist |
| 5 | Non-engineers onboarded on Git | 30-min guided walkthrough on sandbox repo — mandatory before first PR contribution. <a href="javascript:void(0)" onclick="goDetail('how-non-engineers-contribute-using-cursorclaude-code')">See: How non-engineers contribute using Cursor/Claude Code</a> |
| 6 | Skills and KBs developed | SAs use Cursor/Claude Code for skill/KB edits; engineers handle pipeline code. All changes on feature branches. SMEs consulted for domain validation on content skills. |
| 7 | Eval datasets built | Golden dataset rows with input-output pairs, 3–5 scoring dimensions, edge cases included (25–30% of rows). SMEs provide gold-standard scoring for calibration. |
| 8 | Tier 1: Automated code checks (every commit) | Syntax, secrets scan, skill/KB schema validation, hallucination detection, cross-reference checks. Costs $0. Blocks PR if fail. |
| 9 | <a href="javascript:void(0)" onclick="goDetail('eval-proof-before-pushing-non-negotiable')">Eval proof before pushing (non-negotiable)</a> | Run quick eval locally before submitting PR. Paste full eval output into PR description — not just a checkbox. Zero data accuracy FAILs. Reviewer must verify eval is real. |
| 10 | Tier 2: LLM-as-Judge evals (every PR) | 5-row quick eval against golden dataset. Pass: weighted score >= 0.80, zero data accuracy FAILs. Judge model different from generation model. ~$1 per run. |
| 11 | Tier 3: Human review (weekly) | QC reviews 10 outputs blind (without seeing LLM scores first), compares to LLM-Judge, identifies new failure patterns → new eval rows. SMEs provide gold-standard scoring for calibration. |
| 12 | Auto-refinement run (if applicable) | AI-assisted skill improvement. Guardrails: max 5 modifications/session, $50 cap, all changes human-reviewed, hold-out set never exposed. |
| 13 | <a href="javascript:void(0)" onclick="goDetail('conflict-resolution-how-to-handle-overlapping-work')">Handle conflicts + PR review</a> | Communicate ownership before starting. Small focused branches (< 2 days). If two people need same file → coordinate who merges first, second rebases + re-runs eval. Non-engineers never resolve merge conflicts — post in channel. <a href="javascript:void(0)" onclick="goDetail('pr-template-every-pr-must-include-this')">PR review:</a> Skill/KB = 1 peer SA + 1 engineer. Code = 1 different engineer. All Tier 1 + Tier 2 must pass. |

**Gate 3 Checklist:**
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

---

## STAGE 4: DEPLOY & VALIDATE

**Time:** 1–3 days
**Applies to:** Type A, B, C engagements (Type D is fast-tracked).

| # | What to do | Detail |
|---|-----------|--------|
| 1 | Deploy to staging | Using deployment pipeline. Environment progression: Local → Sandbox → Shared Dev → Staging → Production. Never skip. |
| 2 | Run full eval suite in staging | Must pass in deployed environment — not just local. Validates environment parity (deps, model access, data format). |
| 3 | Compare staging vs. local scores | If scores differ by > 0.05 on weighted average → investigate before proceeding. Do NOT push to production with unexplained differences. |
| 4 | Pin model version | Exact version in config (e.g., `claude-sonnet-4-5-20250929`), never "latest." Document model upgrade and fallback process. |
| 5 | Set up production monitoring | Structured logging (run_id, skill, model, latency, tokens, cost). Quality spot checks, cost dashboard, error/stall alerts. |
| 6 | Document and test rollback procedure | Identify rollback target version. Actually execute rollback once to verify it works — not just on paper. |
| 7 | Create incident response runbook | Severity levels (SEV-1 to SEV-4), escalation paths, communication templates, diagnosis decision tree. |
| 8 | Security verified | No secrets in code. Separate API keys per environment. `.env` gitignored. Secrets scanning active in CI. |
| 9 | Cost tracking configured | Every LLM call tagged: project, client, skill_id, skill_version, stage, run_id. Enables cost slicing. |
| 10 | Deploy to production | Engineer executes + leadership approves. Canary deploy (small traffic %) if applicable. Post-deploy: 3–5 smoke test requests + verify monitoring receives data. |

**Gate 4 Checklist:**
- [ ] Full eval suite passes in deployed environment (not just local)
- [ ] Monitoring dashboards live (quality, cost, performance, reliability)
- [ ] Rollback tested (procedure documented AND executed at least once)
- [ ] Incident response runbook exists with severity classification
- [ ] Model version pinned and documented
- [ ] Cost tracking tags configured per engagement
- [ ] Security: no secrets in code, separate keys per environment, `.env` gitignored
- [ ] Engineering/DevOps sign-off on deployment

---

## STAGE 5: OPERATE & EVOLVE

**Time:** 1–2 weeks for handoff. Ongoing for operations.
**Applies to:** Type A, B engagements. Optional for C.

| # | What to do | Detail |
|---|-----------|--------|
| 1 | Assemble handoff package | Architecture docs, all production skill files (versioned), KBs, full eval suite + hold-out set, known limitations, operational runbook, incident response plan, decision log |
| 2 | Train delivery team (2–3 sessions, recorded) | Session 1: system overview. Session 2: daily operations. Session 3: troubleshooting. Acceptance: team can explain system without builder help. |
| 3 | Validate delivery team independence | Delivery team runs `python run_eval.py --mode full` on their own. If they can't, training is incomplete. |
| 4 | Define escalation tiers | L1: delivery handles (known fix in runbook). L2: delivery + SA consult. L3: build team (needs skill/KB/code change). L4: leadership (architectural decision). |
| 5 | Activate production feedback loop | Client comments classified by QC: factual error → regression test row. Missing content → eval row. Style preference → corrections KB. Out-of-scope → back to Stage 0. |
| 6 | Transfer monitoring ownership | Daily: automated quality checks + cost dashboard review. Weekly: QC human review. Bi-weekly: full eval re-run. Monthly: quality trend report to stakeholders. |
| 7 | Define support warranty period | How long builders remain available for L3 escalations post-handoff |
| 8 | Start "weeks to independence" tracking | Target: zero L3 escalations within N weeks. If not trending toward zero, revisit training or runbook quality. |

**Gate 5 Checklist:**
- [ ] Handoff package complete (all artifacts) and reviewed by delivery team
- [ ] Delivery team trained (2–3 sessions minimum, recorded)
- [ ] Delivery team can run eval suite independently
- [ ] Escalation path defined and agreed (L1/L2/L3/L4)
- [ ] Eval monitoring ownership transferred
- [ ] Support warranty period defined (how long builders remain available)
- [ ] "Weeks to independence" tracking started (target: zero L3 escalations within N weeks)

---

## CROSS-CUTTING: APPLIES TO ALL STAGES

### Scope Change Process

| # | What to do | Detail |
|---|-----------|--------|
| 1 | Acknowledge | "Let me assess the impact." Never agree or commit on the call. |
| 2 | Impact assessment (2–4 hrs) | Does this change the eval rubric? Need new skills/KBs? Effort estimate? Timeline impact? Cost impact? |
| 3 | Present options | (a) Add to scope with adjusted timeline. (b) Replace another item. (c) Defer to Phase 2. |
| 4 | Get explicit agreement | Document the decision in writing. |
| 5 | Update everything | Requirements, eval dataset, sprint backlog, stakeholder comms. |

### Cost Governance

| Daily Spend | Action |
|-------------|--------|
| < $10/day per project | Auto-approved |
| $10–50/day | SA reviews |
| $50–100/day | Leadership notified |
| > $100/day | Leadership approval to continue |
| Any single run > $20 | Engineer reviews after the fact |

### Time Allocation

| Category | Target |
|----------|--------|
| **Building** (product development) | **60–70%** |
| **Delivery** (client support, BAU) | **20–30%** |
| **Learning** (upskilling, research) | **10%** (protected, not optional) |

### Communication Cadence

| Meeting | Frequency | Duration |
|---------|-----------|----------|
| Daily standup | Daily | 15 min |
| Sprint review | Bi-weekly | 1 hr |
| Tech talk | Bi-weekly (alternates with sprint review) | 1 hr |
| Leadership update | Bi-weekly | 30 min |
| Engineering sync | Weekly | 30 min |
| WoW retro | Quarterly | 2 hrs |
| Client status | Weekly (written) + Monthly (demo) | — |

---

## TYPE D (BUG FIX) FAST-TRACK

| # | What to do | Detail |
|---|-----------|--------|
| 1 | Identify the bug | What is system doing wrong vs. what skill instructions say? |
| 2 | Create branch | `fix/{area}-{short-description}` |
| 3 | Fix the skill, KB, or code | Targeted change only |
| 4 | Run quick eval (5 rows) | Must pass, zero regressions on previously-passing rows |
| 5 | Add regression test row | New eval row that specifically catches this bug |
| 6 | Submit PR with eval results | Include before/after scores |
| 7 | Engineer reviews and approves | — |
| 8 | Deploy | Same day for simple fixes, 1–2 days if eval dataset needs new rows |
