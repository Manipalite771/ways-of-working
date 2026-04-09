# Ways of Working: Master Framework

*April 2026*

---

## How to Use This Document

This is the **master document** of the Ways of Working (WoW) system. Read this first. It provides the architecture, principles, and navigation for the entire WoW suite. Five granular documents flesh out specific areas in operational detail.

**Document Map:**

| Document | What It Covers | When to Read |
|----------|---------------|-------------|
| **This document** | Structure, stages, gates, RACI, principles, execution plan | First -- always |
| [Granular: Solutioning & Requirements](./Granular_Solutioning_Requirements.md) | Intake classification, requirement gathering, solutioning workshops, POC process, scope change management | When entering Stage 0/1/2 of any engagement |
| [Granular: Eval Dataset Lifecycle](./Granular_Eval_Dataset_Lifecycle.md) | Dataset creation, scoring, versioning, LLM-as-Judge setup, CI/CD integration | When creating or maintaining eval datasets (Stage 1 and 3) |
| [Granular: Skills & KB Lifecycle](./Granular_Skills_KB_Lifecycle.md) | Skill structure, creation, versioning, KB types, auto-refinement guardrails, catalog | When creating or modifying skills/KBs (Stage 2 and 3) |
| [Granular: Build, Test & Deploy](./Granular_Build_Test_Deploy.md) | Branch strategy, PR process, 3-tier testing, deployment pipeline, monitoring, cost management, incident response | When building, testing, or deploying (Stage 3 and 4) |
| [Granular: Cross-Cutting Operations](./Granular_Cross_Cutting_Operations.md) | Communication protocols, sprint cadence, stakeholder management, risk register, knowledge management, time allocation, quality culture | Ongoing -- applies to all stages |

---

## Part 1: Context and Constraints

### What We Know

**1. Scope: Write for end-state, not just transition**
The WoW describes how the team *should* work at steady state, with cross-functional stakeholders (engineering, DevOps, QA, SMEs) included -- even if those stakeholders are not yet on board. We write the target operating model.

**2. Accountability sits with us -- but must be distributed**
The GenAI team owns overall solution quality and outcome. The WoW defines a clear RACI across all stakeholders, explicitly carving out what other functions own.

**3. MedCom is the likely pilot**
MWA has an existing owner. MLR has engineering already moving with Strands. MedCom is the open lane. The WoW will be validated against MedCom first.

**4. Non-engineers contribute code, engineers review**
Final approval and merge authority rests with engineering. The WoW includes the contribution-review-merge workflow and safeguards. See [Build, Test & Deploy: Code Contribution Model](./Granular_Build_Test_Deploy.md#1-code-contribution-model) for the full branch strategy, CODEOWNERS setup, and PR process.

**5. Federated development, central governance**
Teams develop independently; a central layer checks and governs. The WoW fits within this model.

**6. Flexibility is non-negotiable**
Skills, evals, and knowledge bases are the constants. Everything else (framework, platform, deployment target) is a variable that can swap out. See [Flexibility Mechanisms](#flexibility-mechanisms) below.

**7. Proof points first -- no leverage without results**
The WoW must produce a visible result within weeks on MedCom to earn credibility for broader adoption. It cannot be aspirational shelf-ware.

---

### Parked Questions

These are decisions the WoW cannot make. They are owned by leadership or depend on external factors. The WoW is designed to work regardless of how they resolve.

| # | Question | Why Parked | Resolution Trigger | Status |
|---|----------|-----------|-------------------|--------|
| 1 | **Which agentic framework?** (Strands vs Claude Agent SDK vs LangGraph) | Framework evaluation is a parallel workstream. WoW is framework-agnostic. | After hands-on evaluation in 2-3 week sprint | Open |
| 2 | **Build own platform or use Cowork?** | Both options open. Decision pending leadership. | After MedCom pilot results + leadership presentation | Open |
| 3 | **Exact time allocation split** | Leadership has not approved yet. | After deliverables presentation to leadership | Open -- WoW assumes 85/15 until approved, targets 60/30/10 |
| 4 | **CTO office integration model** | Org-level decisions outside our control. | Depends on engineering leadership cleanup | Open |
| 5 | **Dedicated DevOps resource** | WoW assumes DevOps exists in the process. Actual resourcing is a leadership decision. | Tied to leadership approval and budget | Open -- fallback paths defined at every gate |
| 6 | **Formal org structure / team positioning** | Needs senior leadership to champion. | After WoW is proven on MedCom | Open |
| 7 | **What happens to existing MWA/MLR tracks?** | MWA has an existing owner, engineering is on MLR with Strands. | As those tracks stabilize | Open |
| 8 | **Product vs service positioning** | Not a blocking decision. Build good product, let both options play. | Emerges from what works in market | Parked by design |
| 9 | **Prompt versioning platform** (Langfuse vs Braintrust vs AWS-native) | Tool evaluation underway. WoW defines requirements, not the tool. | During MedCom pilot based on hands-on experience | New |
| 10 | **SME cooperation model** | SME participation is expected to be limited. Minimal-ask approach defined but not yet tested. | Validated during MedCom Stage 1 | New |

---

## Part 2: Design Principles

**1. Layer it, don't monolith it.**
The WoW is a system of documents, not one document. Three layers (lifecycle, playbooks, templates) can be adopted incrementally and updated independently.

**2. Framework-agnostic, outcome-anchored.**
Every process step is defined by what outcome it produces and what gate it must pass -- not by which tool or framework executes it. "Eval suite passes at 85%+ on golden dataset" works regardless of framework.

**3. Write for MedCom, generalize later.**
The first version of every artifact is built for MedCom. After the pilot, generalize where patterns hold and fork where they don't.

**4. Assume cross-functional, operate solo-ready.**
Every gate defines a primary path (cross-functional) and a fallback path (GenAI team only). The WoW works whether we get the support or not.

**5. Built-in pivot gates.**
Every stage ends with a review point where the team explicitly asks: "Does this still make sense? Do we need to change direction?" This prevents committing to an approach that no longer fits.

**6. Process scales to the work.**
Not every request needs the full 5-stage treatment. Engagement typing at intake determines which stages and gates apply. A bug fix does not go through a solutioning workshop. See [Engagement Typing](#engagement-typing-which-stages-apply).

---

## Part 3: WoW Architecture

### Three Layers

```
LAYER 1: Lifecycle Process (the "what and when")
  The end-to-end journey from problem to production.
  Framework-agnostic, role-based, gate-driven.
  --> Defined in THIS document + the 5 granular documents.

LAYER 2: Technical Playbooks (the "how")
  Framework-specific, tool-specific guidance. Swappable.
  Today: Claude Agent SDK. Tomorrow: Strands. The lifecycle doesn't change.
  --> To be created per framework decision.
  --> Playbook slots: Claude Agent SDK | Strands | LangGraph | Non-agentic (prompt chain)

LAYER 3: Templates and Artifacts (the "evidence")
  Checklists, eval rubrics, handoff packages, decision records.
  Living templates that improve with each engagement.
  --> Defined in granular documents; indexed in the Template Index below.
```

### Template Index

Every gate requires evidence. This index maps gate requirements to specific templates defined in the granular documents.

| Gate | Required Artifact | Template Location |
|------|------------------|-------------------|
| Intake Gate | Engagement classification + STO assignment | [Solutioning & Requirements: 1.5](./Granular_Solutioning_Requirements.md#15-engagement-typing) |
| Requirement Gate | Requirements document | [Solutioning & Requirements: 1.1 Step 4](./Granular_Solutioning_Requirements.md#11-new-engagements-step-by-step) |
| Requirement Gate | Golden dataset plan | [Eval Dataset Lifecycle: 1.3-1.6](./Granular_Eval_Dataset_Lifecycle.md#13-worked-example-csr-section-11-usage-results) |
| Requirement Gate | Evaluation rubric (client sign-off) | [Eval Dataset Lifecycle: 1.4](./Granular_Eval_Dataset_Lifecycle.md#14-dataset-schema) |
| Requirement Gate | Risk register (initial) | [Cross-Cutting Operations: 6.1](./Granular_Cross_Cutting_Operations.md#61-risk-register-template) |
| Solution Gate | Solutioning workshop output | [Solutioning & Requirements: 2.5](./Granular_Solutioning_Requirements.md#25-workshop-output-template) |
| Solution Gate | Architecture decision record | [Cross-Cutting Operations: 1.5](./Granular_Cross_Cutting_Operations.md#15-decision-documentation) |
| Solution Gate | Skills map | [Skills & KB Lifecycle: 4.1](./Granular_Skills_KB_Lifecycle.md#41-catalog-structure) |
| Build Gate | PR with eval results | [Build, Test & Deploy: 1.3](./Granular_Build_Test_Deploy.md#13-pr-process) |
| Build Gate | Eval suite passing at threshold | [Eval Dataset Lifecycle: 3.5](./Granular_Eval_Dataset_Lifecycle.md#35-passfail-thresholds) |
| Build Gate | Cost tracking per run | [Build, Test & Deploy: 5.1](./Granular_Build_Test_Deploy.md#51-tracking-granularity) |
| Deploy Gate | Monitoring dashboard specification | [Build, Test & Deploy: 4.1-4.2](./Granular_Build_Test_Deploy.md#41-metrics-to-track) |
| Deploy Gate | Rollback procedure | [Build, Test & Deploy: 3.3](./Granular_Build_Test_Deploy.md#33-step-by-step-rollback-procedure) |
| Handoff Gate | Handoff package | [Cross-Cutting Operations: 3.3](./Granular_Cross_Cutting_Operations.md#33-onboarding-guide) (for team); Stage 5 spec below |
| Handoff Gate | Incident response runbook | [Build, Test & Deploy: 4.3](./Granular_Build_Test_Deploy.md#43-incident-response) |
| All gates | Scope change impact assessment (if applicable) | [Solutioning & Requirements: 5.3](./Granular_Solutioning_Requirements.md#53-scope-change-management) |
| Weekly | Client status update | [Cross-Cutting Operations: 1.4](./Granular_Cross_Cutting_Operations.md#14-client-communication-rules) |
| Sprint | Sprint review with eval scores | [Cross-Cutting Operations: 2.1](./Granular_Cross_Cutting_Operations.md#21-sprint-structure) |

---

## Part 4: The Lifecycle -- 6 Stages

The lifecycle has 6 stages. **Stage 0: Intake & Classification** precedes the five core stages to ensure the right process is applied to the right type of work.

```
STAGE 0          STAGE 1          STAGE 2            STAGE 3          STAGE 4           STAGE 5
Intake &     --> Requirement  --> Solutioning    --> Build &      --> Deploy &       --> Operate &
Classification   & Scoping       Workshop            Test            Validate          Evolve
    |                |                |                 |                |                |
    v                v                v                 v                v                v
[INTAKE GATE]   [REQ GATE]     [SOLUTION GATE]   [BUILD GATE]    [DEPLOY GATE]   [HANDOFF GATE]
```

### Engagement Typing: Which Stages Apply

Not all work requires all stages. Classification at intake determines the path.

| Type | Description | Stages Required | Gate Rigor | Examples |
|------|------------|----------------|-----------|---------|
| **A -- New Product / Major Feature** | Greenfield build or major new capability | All 6 stages, full gates | Full | "Build a new MedCom asset generation pipeline" |
| **B -- Significant Enhancement** | New section type, new document format, major skill overhaul | Stages 0, 2-5 (streamlined Stage 1 if requirements already clear) | Full for Stages 2-5 | "Add CSR Section 14 support to MWA" |
| **C -- Skill/KB Improvement** | Improve quality on existing capability | Stages 0, 3-4 only (build-test-deploy) | Standard | "Section 11 clinical interpretation score is too low" |
| **D -- Bug Fix** | System not behaving per skill instructions | Fast-track: fix, eval, engineer review, deploy | Lightweight | "Section 11 is printing table headers twice" |

**Classification criteria (decide at intake):**
- Does it need new eval datasets? --> Type A or B
- Does it need a solutioning workshop? --> Type A
- Does it only change existing skills/KBs? --> Type C
- Is it a code/pipeline fix only? --> Type D

Full details: [Solutioning & Requirements: 1.5 Engagement Typing](./Granular_Solutioning_Requirements.md#15-engagement-typing)

---

### Stage 0: Intake & Classification

**Purpose:** Classify the work, assign an owner, and determine which stages apply.

**Activities:**
- Receive request (client, internal, production monitoring)
- Classify engagement type (A/B/C/D) using criteria above
- Assign Single-Threaded Owner (STO) -- one person accountable end-to-end
- For Type A: schedule discovery session
- For Type D: fast-track directly to fix-eval-review-deploy

**Gate: Intake Gate**
- [ ] Engagement type classified (A/B/C/D)
- [ ] STO assigned
- [ ] Applicable stages and gates identified
- [ ] Entered into backlog with priority (using [P0-P3 matrix](./Granular_Cross_Cutting_Operations.md#25-prioritization-framework))

**Fallback (no engineering support):** STO self-classifies and proceeds. Classification is reviewed at next standup.

Full process for new engagements vs. existing products vs. change requests: [Solutioning & Requirements: 1.1-1.4](./Granular_Solutioning_Requirements.md#11-new-engagements-step-by-step)

---

### Stage 1: Requirement & Scoping

**Purpose:** Define the problem, build the golden dataset plan, agree on how quality will be measured.

**Activities:**
- Discovery session with client/stakeholders (walk the manual process end-to-end)
- Collect manually-done examples from SMEs (minimum 3; target 5-7)
- Define scoring dimensions (3-5 per document type) and evaluation rubric
- Build golden dataset plan: source data, target row count, edge cases, timeline
- Define success parameters: accuracy target, time target, cost ceiling
- Document deployment environment and scalability requirements
- Create initial risk register
- Client signs off on the evaluation rubric (not the solution)

**Handling the "client doesn't know what they want" problem:**
1. Get 3 manually completed examples (non-negotiable minimum)
2. Build minimal golden dataset from those examples
3. Run the system once and show the output
4. Client reacts -- their reaction becomes the requirement
5. Update rubric and dataset accordingly

Full requirement gathering process: [Solutioning & Requirements: 1.1](./Granular_Solutioning_Requirements.md#11-new-engagements-step-by-step)
Golden dataset creation: [Eval Dataset Lifecycle: 1.1-1.6](./Granular_Eval_Dataset_Lifecycle.md#11-who-does-what)

**Gate: Requirement Gate**
- [ ] Golden dataset exists (minimum rows per [Eval Dataset: 1.5](./Granular_Eval_Dataset_Lifecycle.md#15-how-many-rows)) or plan + timeline to create it
- [ ] Scoring dimensions defined with rubric
- [ ] Success parameters quantified and agreed (accuracy threshold, latency target, cost ceiling)
- [ ] Deployment environment identified (internal / client / both)
- [ ] Stakeholders identified and engagement model defined (per [Cross-Cutting: 5.1](./Granular_Cross_Cutting_Operations.md#51-engagement-model-per-stakeholder))
- [ ] Client sign-off on rubric obtained (email confirmation minimum)
- [ ] Risk register initialized (per [Cross-Cutting: 6.1](./Granular_Cross_Cutting_Operations.md#61-risk-register-template))

**Fallback (no SME cooperation):**
- Requirements based on Solution Architect's domain knowledge (not client-validated)
- Documented as a risk in the risk register
- Escalated to client project lead

**Pivot check:** Does the problem still warrant the classified engagement type? If requirements reveal less complexity than expected, downgrade (e.g., Type A to Type B).

---

### Stage 2: Solutioning Workshop

**Purpose:** Design the solution architecture, decide complexity level, identify skills and KBs needed.

**Activities:**
- Cross-functional workshop (GenAI team + engineering rep minimum; 2-4 hours)
- Walk the complexity ladder: simple chain --> routing --> parallelism --> agent (only if genuinely open-ended)
- Architecture diagram (data flow, agent topology, integration points)
- Agentic vs. non-agentic decision documented with justification and eval evidence
- Skills inventory: what existing skills apply? What needs creation?
- KB requirements: which structural, conventions, and corrections KBs are needed?
- Non-functional requirements: latency budget, concurrency, cost ceiling, security
- Cost estimation (model calls, token usage, infrastructure)

**Workshop protocol:**
- Facilitator sends pre-workshop packet 2 days before
- Structured 3-hour agenda with complexity ladder, architecture design, NFRs, and decision
- Disagreements resolved via structured approach: Type A = experimentation spike then architecture; Type B = architecture first; Type C = experimentation first
- All decisions documented in decision record format

Full workshop process: [Solutioning & Requirements: 2.1-2.5](./Granular_Solutioning_Requirements.md#21-when-to-hold-a-workshop)
Complexity ladder with worked examples: [Solutioning & Requirements: 2.4](./Granular_Solutioning_Requirements.md#24-the-complexity-ladder--worked-examples)
Skills catalog for reuse check: [Skills & KB Lifecycle: 4.1](./Granular_Skills_KB_Lifecycle.md#41-catalog-structure)

**Gate: Solution Gate**
- [ ] Architecture documented (diagram + decision record) and peer-reviewed
- [ ] Complexity level justified (chain/router/parallel/agent) with evidence
- [ ] Agentic/non-agentic decision justified by eval results or past experience
- [ ] Skills map finalized: existing (reuse), to-create, to-modify -- with owners and effort estimates
- [ ] KB requirements identified (structural, conventions, corrections)
- [ ] Engineering sign-off on feasibility (or documented note that we proceed without it)
- [ ] Cost estimate within acceptable range
- [ ] Non-functional requirements defined (latency, concurrency, cost ceiling)
- [ ] Risk register updated with technical and client risks

**Fallback (no engineering rep available):**
- Solution Architects conduct the workshop internally
- Architecture shared with engineering async for feedback (2-day window)
- If no response: proceed, document the gap, flag as risk

**Pivot check:** For Type A, a 1-week POC/spike may precede the full workshop. If the spike reveals the problem is simpler than anticipated, adjust scope. See [Solutioning & Requirements: 4.1-4.3](./Granular_Solutioning_Requirements.md#41-when-is-a-poc-needed) for POC process and the safeguards against "POC goes straight to production."

---

### Stage 3: Build & Test

**Purpose:** Build the skills, KBs, and eval infrastructure. Iterate until quality gates pass.

**Activities:**
- Write/refine skill files following the skill template and quality patterns
- Build knowledge bases (structural, conventions, corrections)
- Build evaluation suite: programmatic checks + LLM-as-Judge + golden dataset comparison
- Run auto-refinement cycles with defined guardrails (max 5 skill modifications per session, max $50 per session, human review of all changes)
- Non-engineers contribute skills and prompt logic via Cursor/Claude Code; engineers review and approve
- Track: quality score, cost per run, latency, pass rate on eval suite
- Version everything: skills, knowledge bases, eval datasets, pipeline config

**Code contribution model:**
- Trunk-based development with short-lived feature branches
- Branch naming: `{type}/{area}-{short-description}` (feature/, fix/, skill/, kb/, eval/)
- Engineers merge to main; engineers + leadership approve production deployments
- CODEOWNERS enforces review requirements per directory
- PR template requires eval results before and after the change

Full branch strategy and PR process: [Build, Test & Deploy: 1.1-1.7](./Granular_Build_Test_Deploy.md#11-branch-strategy)
Skill creation process: [Skills & KB Lifecycle: 1.2-1.3](./Granular_Skills_KB_Lifecycle.md#12-who-creates-skills)
Auto-refinement guardrails: [Skills & KB Lifecycle: 1.7](./Granular_Skills_KB_Lifecycle.md#17-auto-refinement-how-ai-modifies-skills)
3-tier testing strategy: [Build, Test & Deploy: 2](./Granular_Build_Test_Deploy.md#2-testing-strategy-3-tier)

**Testing tiers:**

| Tier | What | When | Cost | Time |
|------|------|------|------|------|
| Tier 1: Programmatic checks | Syntax, schema, secrets, formatting | Every commit | $0 | 30 sec |
| Tier 2: LLM-as-Judge | Quick eval on 5 rows | Every PR | $0.50-$2 | 5-10 min |
| Tier 3: Human review | 10 outputs scored by QC team | Weekly | Human time | 2-3 hours |
| Full eval suite | All rows + hold-out set | Pre-deployment | $5-$15 | 20-30 min |

**Gate: Build Gate**
- [ ] Eval suite passes at agreed threshold (default: 85%+ weighted score on golden dataset)
- [ ] Zero FAIL on data accuracy dimension (binary, no tolerance)
- [ ] No single eval row below 0.70 weighted score
- [ ] Hold-out set passes (rows never seen during auto-refinement)
- [ ] Auto-refinement has run with documented improvement trajectory
- [ ] Cost per output within target
- [ ] Latency within target
- [ ] All code reviewed and approved by engineering (per [CODEOWNERS](./Granular_Build_Test_Deploy.md#17-preventing-non-engineers-from-breaking-things))
- [ ] Known limitations documented
- [ ] Regression suite exists for ongoing monitoring

**Fallback (no engineer for review):**
- SA self-reviews skill/KB changes (not code changes)
- Code changes wait for engineer review (this is a hard requirement, not waivable)
- If engineer unavailable for >3 days: escalate to leadership

**Pivot check:** If auto-refinement plateaus (quality stops improving despite iterations), revisit the architecture decision from Stage 2. The problem may need a different complexity level.

---

### Stage 4: Deploy & Validate

**Purpose:** Move from staging to production with safeguards. Validate in the deployed environment.

**Activities:**
- Deploy to staging environment
- Run full eval suite in deployed environment (not just local)
- Canary deployment if applicable (small traffic percentage first)
- Production monitoring setup: quality spot checks, cost dashboard, error/stall alerts
- Model version pinned (exact version, never "latest")
- Rollback procedure documented and tested
- Incident response runbook created

**Environment progression:**
```
Local Dev --> Shared Dev --> Staging --> Production
```

Full deployment pipeline: [Build, Test & Deploy: 3.1-3.4](./Granular_Build_Test_Deploy.md#31-environment-progression)
Model version management: [Build, Test & Deploy: 3.4](./Granular_Build_Test_Deploy.md#34-model-version-pinning)
Monitoring metrics and cadence: [Build, Test & Deploy: 4.1-4.2](./Granular_Build_Test_Deploy.md#41-metrics-to-track)
Incident response with severity levels: [Build, Test & Deploy: 4.3](./Granular_Build_Test_Deploy.md#43-incident-response)

**Gate: Deploy Gate**
- [ ] Full eval suite passes in deployed environment (not just local)
- [ ] Monitoring dashboards live (quality, cost, performance, reliability metrics per [BTD: 4.1](./Granular_Build_Test_Deploy.md#41-metrics-to-track))
- [ ] Rollback tested (per [BTD: 3.3 rollback procedure](./Granular_Build_Test_Deploy.md#33-step-by-step-rollback-procedure))
- [ ] Incident response runbook exists with severity classification (SEV-1 through SEV-4)
- [ ] Model version pinned and documented
- [ ] Cost tracking tags configured per [BTD: 5.1](./Granular_Build_Test_Deploy.md#51-tracking-granularity)
- [ ] DevOps sign-off (or self-serve deployment documented with fallback)

**Fallback (no DevOps support):**
- Self-serve deployment to team-managed environment
- Monitoring via Langfuse/custom dashboards
- Document the self-serve setup as a risk for scale

**Pivot check:** If eval scores drop significantly in the deployed environment vs. local, investigate environment parity before proceeding. Do not push to production with unexplained score differences.

---

### Stage 5: Operate & Evolve

**Purpose:** Hand off to operations, maintain quality, continuously improve.

**Activities:**
- Deliver handoff package (specification below)
- Delivery team (or ops team) takes over day-to-day operations
- L1/L2 issues handled by delivery team using runbook
- L3 escalations loop back to builders
- Periodic eval re-runs to catch quality drift (daily automated spot checks, bi-weekly full suite)
- Client/SME feedback classified and routed: factual errors --> eval rows, style preferences --> corrections KB, scope changes --> formal change process
- Scheduled skill refresh cycles

**Handoff package specification:**

| Artifact | Contents | Acceptance Criterion |
|----------|---------|---------------------|
| Architecture documentation | System diagram, data flow, skill dependency graph, integration points | Someone not on the build team can explain the system from these docs |
| Skill files with rationale | All production skills, versioned, with metadata and linked eval datasets | Self-documenting per [Skills & KB: 1.1 template](./Granular_Skills_KB_Lifecycle.md#11-what-is-a-skill-file) |
| Knowledge bases | All structural, conventions, and corrections KBs, versioned | Linked from skills, no orphaned KBs |
| Eval suite | Full dataset + hold-out set + LLM-as-Judge prompts + programmatic checks | Can be run by delivery team: `python run_eval.py --mode full` |
| Known limitations | Structured table: limitation, severity, workaround, expected fix timeline | No surprises in production |
| Operational runbook | Step-by-step for common operations, troubleshooting tree, severity classification | Delivery team can handle L1/L2 without builder involvement |
| Incident response plan | Severity definitions, escalation paths, rollback steps, communication templates | Tested during Stage 4 |
| Training sessions | 2-3 sessions recorded: system overview, daily operations, troubleshooting | Delivery team can operate independently after training |
| Decision log | All significant decisions with context and rationale | New team members understand why things are the way they are |

**Feedback loop -- from production back into the system:**
```
Client/SME reviews output --> provides comments/edits
  --> QC classifies each comment:
    A) Factual error --> add regression test row to eval dataset
    B) Missing content --> add row with completeness < 1.0
    C) Style/convention preference --> add to corrections KB
    D) Out-of-scope request --> log as feature request, not eval row
```

Full feedback process: [Eval Dataset Lifecycle: 5.1-5.3](./Granular_Eval_Dataset_Lifecycle.md#51-clientsme-feedback--eval-dataset)

**Gate: Handoff Gate**
- [ ] Handoff package complete (all artifacts above) and reviewed by delivery team
- [ ] Delivery team trained (2-3 sessions minimum, recorded)
- [ ] Delivery team can run eval suite independently
- [ ] Escalation path defined and agreed (L1/L2/L3/L4 per [Cross-Cutting: 1.3](./Granular_Cross_Cutting_Operations.md#13-escalation-paths))
- [ ] Eval monitoring ownership transferred (who reviews weekly quality reports)
- [ ] Support warranty period defined (how long builders remain available for questions)
- [ ] "Weeks to independence" tracking started (target: zero L3 escalations within N weeks)

**Fallback (no delivery team to hand off to):**
- Builder continues to operate but with reduced sprint allocation to the engagement
- Operational tasks tracked separately from build tasks in sprint planning
- Escalate to leadership: this engagement needs a delivery owner

**Pivot check:** If L3 escalations remain high after the warranty period, the handoff package is insufficient. Revisit the runbook and training before accepting the handoff as complete.

---

## Part 5: RACI Framework

**RACI** (Responsible, Accountable, Consulted, Informed)

This RACI uses functional roles (not names) so it survives team changes. It reflects the detailed role definitions in the granular documents.

**Current team mapping (for reference, not part of the RACI itself -- this list is not exhaustive and may include members from MedCom and CTO office tracks):**
- Solution Architects: Adithya, Tanmay, Yash, Karan, Ashutosh, Chakshu, and other solution architects as assigned
- Engineers: Current engineers plus additional engineering resources from MedCom and CTO office tracks as applicable
- QC/Testing: Current QC analysts and testers, expandable as engagement volume grows
- Delivery: Delivery leads assigned per engagement
- GenAI Solution Approvers: Director, Senior Manager (GenAI Solution Approvers)

### Stage-Level RACI

| Activity | GenAI Solution Architect | GenAI Engineer | QC/Testing | SME/Domain | Engineering (CTO) | DevOps | Delivery | Leadership |
|----------|------------------------|---------------|-----------|-----------|-------------------|--------|---------|-----------|
| **Stage 0: Intake & Classification** | R/A | C | - | - | - | - | C | A (for Type A) |
| **Stage 1: Discovery session** | R | C | C | R | - | - | - | C |
| **Stage 1: Golden dataset creation** | A | C | R | R | - | - | - | Approves thresholds |
| **Stage 1: Eval rubric definition** | R/A | C | R | C | - | - | - | Approves |
| **Stage 1: Requirements document** | R/A | R (feasibility) | - | C | - | - | - | Reviews |
| **Stage 1: Client sign-off** | R | - | - | C | - | - | - | A |
| **Stage 2: Workshop facilitation** | R | R | C | C | C | - | - | A |
| **Stage 2: Architecture design** | R/A | R | - | C | C | C | - | Reviews |
| **Stage 2: Complexity ladder decision** | R | R | - | - | C | - | - | A |
| **Stage 3: Skill writing** | R | R | - | C | - | - | - | Reviews |
| **Stage 3: KB creation/maintenance** | R | C | R | C | - | - | - | - |
| **Stage 3: Eval infrastructure** | C | R/A | R | - | C | C | - | - |
| **Stage 3: Auto-refinement** | R (runs) | R (tooling) | C | - | - | - | - | Reviews changes |
| **Stage 3: Code review & merge** | C | A | - | - | R | - | - | - |
| **Stage 4: Deployment pipeline** | C | R | - | - | R | A | - | Approves prod |
| **Stage 4: Production monitoring setup** | C | R | R | - | R | A | C | - |
| **Stage 4: Incident response** | R (domain) | R (technical) | R (quality) | - | C | C | C | Notified (SEV-1/2) |
| **Stage 5: Handoff package creation** | R/A | R | R | - | C | - | R | Reviews |
| **Stage 5: Delivery team training** | R | R | C | - | - | - | A | - |
| **Stage 5: Ongoing quality monitoring** | C | C | R | - | - | - | A | Reviews monthly |
| **Cross-cutting: Client communication** | R (SPOC) | C | C | C | - | - | C | A |
| **Cross-cutting: Cost governance** | R (engagement) | R (tracking) | - | - | - | - | - | A (approvals per [BTD: 5.2](./Granular_Build_Test_Deploy.md#52-budget-thresholds-and-approvals)) |
| **Cross-cutting: Risk management** | R (identification) | R (technical) | R (quality) | - | - | - | - | A (review) |
| **Cross-cutting: Scope change mgmt** | R (impact assessment) | C | - | - | - | - | C | A (approval) |
| **Cross-cutting: Knowledge capture** | R | R | R | - | - | - | R | - |

*R = Responsible (does the work), A = Accountable (owns the outcome), C = Consulted (provides input)*

Full stakeholder engagement model (who, what, how, frequency): [Cross-Cutting Operations: 5.1](./Granular_Cross_Cutting_Operations.md#51-engagement-model-per-stakeholder)

---

## Part 6: Cross-Cutting Processes

These apply across all stages and are not tied to any single gate. They are defined in detail in the granular documents and summarized here for navigation.

### Communication & Reporting

| What | Cadence | Details |
|------|---------|---------|
| Daily standup | Daily, 15 min | Blockers and coordination |
| Sprint review | Bi-weekly | Demo actual outputs (including failures), eval score trends |
| Tech talk | Bi-weekly (alternates with sprint review) | Deep-dive by one team member |
| Leadership update | Bi-weekly | Metrics deck + demo + ask |
| Weekly engineering sync | Weekly | Cross-team coordination |
| Quarterly WoW retro | Quarterly | Process improvement |
| Client status | Weekly written + monthly demo | Per [client communication rules](./Granular_Cross_Cutting_Operations.md#14-client-communication-rules) |

Full communication protocols: [Cross-Cutting Operations: 1.1-1.5](./Granular_Cross_Cutting_Operations.md#11-meeting-cadence)

### Cost Governance

| Spend Level | Action |
|-------------|--------|
| <$10/day per project | Normal operations, auto-approved |
| $10-50/day | SA reviews |
| $50-100/day | Leadership notified |
| >$100/day | Leadership approval to continue |
| Any single run >$20 | Engineer reviews after the fact |

Full cost management framework: [Build, Test & Deploy: 5.1-5.5](./Granular_Build_Test_Deploy.md#51-tracking-granularity)

### Risk Management

Risk register maintained per engagement. Risks scored on likelihood x impact (1-5 each). Score >=12 = leadership update required. Score >=8 = track in retro.

Full risk framework with template: [Cross-Cutting Operations: 6.1-6.2](./Granular_Cross_Cutting_Operations.md#61-risk-register-template)

### Knowledge Management

| Knowledge Type | Location | Owner |
|---------------|----------|-------|
| Skills and KBs | Git repo: `/skills/`, `/knowledge-bases/` | Skill owner |
| Eval datasets | Git repo: `/eval-datasets/` | QC team |
| Architecture decisions | Git repo: `/decisions/` | Decision participants |
| Post-mortems | Git repo: `/postmortems/` | Incident owner |
| "What we tried & learned" | Git repo: `/learnings/` | Anyone |
| Client engagement docs | Shared drive (restricted) | Engagement SPOC |

Knowledge silo prevention: buddy pairing, cross-review on PRs, tech talks, self-documenting skills.

Full knowledge management: [Cross-Cutting Operations: 3.1-3.4](./Granular_Cross_Cutting_Operations.md#31-where-knowledge-lives)

### Time Allocation

**Until leadership approves:** 85% delivery / 15% building + learning.
**Target:** 60% delivery / 30% building / 10% learning.

Protected time: Tuesday and Thursday afternoons (1-5 PM) are no-meeting blocks for focused work. Build progress tracked in sprint alongside delivery. If build progress is zero for 2 consecutive sprints, escalate.

Full time allocation and prioritization: [Cross-Cutting Operations: 4.1-4.3](./Granular_Cross_Cutting_Operations.md#41-the-split)

### Scope Change Management

Any client request that changes requirements mid-build triggers:
1. Acknowledge (do NOT agree on the call)
2. Impact assessment (timeline, cost, quality implications)
3. Present options to client (add to scope with adjusted timeline, replace another item, defer to Phase 2)
4. Document the decision
5. Update requirements, eval dataset, and sprint backlog

Full scope change process: [Solutioning & Requirements: 5.3](./Granular_Solutioning_Requirements.md#53-scope-change-management)

---

## Part 7: Flexibility Mechanisms

### 1. Swappable Technical Playbooks

The lifecycle stages and gates do not change. The *how* changes. Each Technical Playbook is a separate Layer 2 document:
- Playbook: Claude Agent SDK
- Playbook: Strands
- Playbook: LangGraph
- Playbook: Non-agentic (prompt chain)

When the framework decision is made (or changes), the playbook swaps. Process, gates, and artifacts remain the same. Skills are framework-agnostic by design (they are natural language instructions, not code).

### 2. Engagement Typing Scales the Process

The engagement typing system (A/B/C/D) means the WoW scales down for small changes without losing rigor for large ones. A bug fix does not go through a solutioning workshop. A new product goes through every stage and gate.

### 3. Quarterly WoW Retrospective

Every quarter, the team holds a retrospective specifically on the WoW:
- What gates are adding value vs. creating friction?
- What artifacts are being produced vs. being skipped?
- Has the tech landscape shifted enough to warrant a playbook swap?
- Review WoW success metrics (see below).
- Update the WoW. It is a living system, not a decree.

### 4. "If we're on our own" Fallback at Every Gate

Each gate has a primary path (cross-functional, as designed) and a fallback path (GenAI team only). These are documented inline with each gate above. Summary:

| Gate | Primary Path | Fallback (Solo) |
|------|-------------|-----------------|
| Intake | STO classified with leadership input | STO self-classifies, reviewed at standup |
| Requirement | Discovery with client + SME + engineering feasibility check | SA uses domain knowledge; gap documented as risk |
| Solution | Cross-functional workshop with engineering rep | Internal workshop; architecture shared async for feedback |
| Build | Engineer reviews all PRs; QC runs Tier 3 weekly | SA self-reviews skills/KBs; code changes wait for engineer (hard requirement) |
| Deploy | DevOps deploys; monitoring on shared infra | Self-serve to team-managed environment; monitoring via Langfuse/custom |
| Handoff | Delivery team takes over with training | Builder continues ops with reduced sprint allocation; escalate for delivery owner |

### 5. MedCom-First, Generalize Later

First version of every artifact is built for MedCom. After the pilot, review:
- What generalizes across MLR/MWA/MedCom?
- What needs to be forked per product area?
- Update templates accordingly.

---

## Part 8: Measuring WoW Success

The quarterly WoW retrospective needs data, not just opinions. These metrics track whether the WoW is working.

| Metric | Baseline (current) | Target (2 quarters) | How Measured |
|--------|-------------------|--------------------|--------------| 
| Prototype-to-production time | Unmeasured (estimated 3+ months) | 30% reduction | Calendar days from Build Gate to Deploy Gate |
| Eval coverage | ~0% of engagements have golden datasets | 100% of active engagements | Count of engagements with eval dataset vs. total |
| Gate compliance | 0% (gates do not exist yet) | >80% of engagements pass through all applicable gates | Gate checklist completion rate |
| L3 escalations post-handoff | Unmeasured (frequent) | 50% reduction per quarter | Count of L3 escalations per engagement per month |
| Component reuse rate | ~0% (no catalog) | 40%+ of skills in new engagements are reused or forked | Skills catalog: reused vs. net-new per engagement |
| Cost per output | Unmeasured | Tracked, trending down | [BTD: 5.5 monthly cost report](./Granular_Build_Test_Deploy.md#55-reporting-to-stakeholders) |
| Revenue per resource trend | Known to leadership | Improving quarter-over-quarter | Leadership metric |
| Time from requirement to first eval-passing prototype | Unmeasured | Tracked, trending down | Calendar days from Requirement Gate to first Build Gate pass |

---

## Part 9: Execution Plan

### Phase 1: Foundation (Weeks 1-2)

**Week 1:**
- [ ] Discuss with the larger team for alignment. Use this document as the basis for group discussion.
- [ ] Run MedCom through Stage 0 (Intake) and Stage 1 (Requirement & Scoping)
- [ ] Begin MedCom golden dataset creation with QC team (target: 10 rows minimum viable)
- [ ] Identify existing artifacts that can be repurposed (SOPs, eval data, skill files from demo)
- [ ] Set up git repository structure: `/skills/`, `/knowledge-bases/`, `/eval-datasets/`, `/decisions/`, `/postmortems/`, `/learnings/`

**Week 2:**
- [ ] Complete MedCom golden dataset to minimum viable size (15 rows)
- [ ] Run MedCom through Stage 2 (Solutioning Workshop) -- first test of the workshop protocol
- [ ] Create first skill files from existing SOPs/prompts (per [Skills & KB: 5.1 migration process](./Granular_Skills_KB_Lifecycle.md#51-step-by-step-migration))
- [ ] Set up Tier 1 automated checks (schema validation, secrets detection)
- [ ] First sprint planning using WoW sprint structure

### Phase 2: Pilot (Weeks 3-4)

**Week 3:**
- [ ] MedCom enters Stage 3 (Build & Test)
- [ ] First auto-refinement session with defined guardrails
- [ ] Set up Tier 2 LLM-as-Judge eval in CI/CD pipeline
- [ ] First WoW retrospective (mini): what is working, what is friction, what to adjust
- [ ] Begin tracking WoW success metrics (baselines)

**Week 4:**
- [ ] MedCom Build Gate review
- [ ] If passing: deploy to staging (Stage 4)
- [ ] First Tier 3 human review session with QC team
- [ ] Cost tracking operational per engagement
- [ ] Present MedCom progress to leadership with eval metrics (not just demos)

### Phase 3: Validation (Weeks 5-8)

- [ ] MedCom through Stage 4 (Deploy & Validate) with monitoring
- [ ] Begin MedCom Stage 5 preparations (handoff package, runbook)
- [ ] Apply WoW to a second engagement (Type B or C) to test generalizability
- [ ] Expand component catalog from MedCom learnings
- [ ] Monthly cost report to leadership
- [ ] If leadership approves time allocation: shift from 85/15 toward 60/30/10
- [ ] If leadership does not approve: continue within delivery bandwidth, refine WoW based on available running room

### Phase 4: Scale (Weeks 9+)

- [ ] MedCom handoff (Stage 5)
- [ ] Generalize templates from MedCom for cross-product use
- [ ] Onboard second product area to the WoW
- [ ] Full quarterly WoW retrospective with success metric data
- [ ] Present pilot results + WoW to leadership as proof point for broader adoption

**Contingency:** If at any point the MedCom pilot stalls (blocked by dependencies, resource constraints, or scope changes), the WoW still generates value through: eval dataset creation for existing engagements, skill migration from existing SOPs, and process discipline (gate checklists) applied to ongoing work. The WoW does not require a greenfield pilot to be useful.

---

## Part 10: What This Approach Deliberately Does NOT Do

1. **Does not pick a framework.** That is a parallel workstream. The WoW works regardless.
2. **Does not assume resources we don't have.** Every gate has a fallback path.
3. **Does not require leadership approval to start.** We can begin drafting and testing on MedCom within existing bandwidth. Approval unlocks scale, not the starting gun.
4. **Does not over-specify roles by name.** Uses functional roles so it survives team changes.
5. **Does not try to fix the CTO office relationship.** The WoW defines what we need from them; getting it is a separate effort.
6. **Does not create a monolith.** Three layers, independently updatable. Kill a playbook, the process survives. Change a template, the playbook survives.
7. **Does not mandate the full process for small changes.** Engagement typing (A/B/C/D) scales the process to the work.
8. **Does not ignore cost.** Cost governance is embedded at every stage, not treated as an afterthought.
9. **Does not assume clients will cooperate perfectly.** The "client doesn't know what they want" and "SME won't participate" scenarios have defined handling paths.
10. **Does not treat the WoW as finished.** Quarterly retrospectives with success metrics ensure it evolves.

---

*This document is the master index and architecture of the WoW system. The five granular documents contain the operational detail. Start here, then drill into the specific granular document for the stage you are working in.*
