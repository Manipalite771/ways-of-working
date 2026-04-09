# Solutioning & Requirements -- Granular Process

## 1. Requirement Gathering Process

### 1.1 New Engagements: Step-by-Step

```
TRIGGER: Client has a problem or business development identifies an opportunity
  |
STEP 1: Intake Call (GenAI Solution Approvers + BD/client lead, 30 min)
  - Understand the problem at a high level
  - Classify: Is this MWA, MLR, MedCom, or something new?
  - Classify: Product engagement or service engagement? (see 1.3)
  - Classify: Engagement type A/B/C/D (see 1.5)
  - Output: 1-paragraph problem statement + engagement type
  |
STEP 2: Discovery Session (Solution Architect + SME/domain rep + client, 1-2 hours)
  - Walk through the client's current manual process end-to-end
  - Collect: What are the inputs? (source documents, templates, guidelines)
  - Collect: What are the outputs? (document type, format, sections, length)
  - Collect: What does "good" look like? Ask for 3-5 examples of manually completed work
  - Collect: What does "bad" look like? Ask for examples of common errors or rejections
  - Collect: What are the client's SOPs and style guides?
  - Ask: What is the current processing time manually?
  - Ask: What processing time would be acceptable from the platform?
  - Ask: What volume are we talking about? (documents per month/quarter)
  - Ask: What is the deployment environment? (our cloud, client cloud, hybrid)
  - Collect: Regulatory and compliance requirements (see 1.7 for pharma-specific checklist)
  - Collect: Agentic requirement signals (see 1.8)
  - Output: Discovery notes document
  |
STEP 3: Golden Dataset Planning (Solution Architect + QC, 2-4 hours)
  - From the manually completed examples: identify input-output pairs
  - Define scoring dimensions based on the specific document type
  - Draft the evaluation rubric
  - Estimate: how many rows are needed for minimum viable eval dataset?
  - Identify gaps: do we have enough examples? Do we need more from the client?
  - Output: Golden dataset plan (see Eval doc for details)
  |
STEP 4: Requirements Document Draft (Solution Architect, 3-4 hours)
  - Compile discovery findings into a structured requirements document
  - Include: problem statement, in-scope/out-of-scope, success criteria (quantified),
    input specification, output specification, quality dimensions with thresholds,
    timeline constraints, deployment requirements, dependencies
  - Include: regulatory/compliance requirements from Section 1.7
  - Include: agentic vs. non-agentic signals from Section 1.8
  - Include: competitive landscape context from Section 1.9
  - Output: Requirements document (using template)
  |
STEP 5: Requirements Review (Solution Architect + Engineer + Leadership, 1 hour)
  - Internal review before sharing with client
  - Engineer validates: is this technically feasible? Any infrastructure concerns?
  - Leadership validates: does this align with our capacity and strategy?
  - Output: Revised requirements document
  |
STEP 6: Client Sign-Off (Solution Architect + client, 30 min call + async)
  - Walk client through the requirements document and rubric
  - Explain: "You are signing off on how we will measure quality, not on the solution approach.
    If our system produces outputs that score above [threshold] on this rubric, we consider it a success."
  - Get explicit sign-off (email confirmation minimum)
  - Output: Signed-off requirements + rubric
  |
REQUIREMENT GATE -- proceed to Stage 2
```

**Total time: 2-3 days of effort spread over 1-2 weeks** (depends on client responsiveness)

### 1.2 Handling Common Blockers

**"The client doesn't know what they want"**
- Don't wait for perfect requirements. Instead:
  1. Get 3 manually completed examples (this is non-negotiable)
  2. Build a minimal golden dataset from those examples
  3. Run the system once and show the output
  4. NOW the client can react: "Yes, but we want more detail in Section X" or "This is wrong because..."
  5. Their reaction becomes the requirement. Update the rubric and dataset.

**"The SME won't participate"**
- SMEs are asked for exactly two things: (1) manually completed examples and (2) 1-hour scoring calibration session. That's it. They are NOT asked to understand the platform, write prompts, or attend technical meetings.
- Frame it as: "We need to understand how you do this manually so we can automate it. Can you share 3 recent completed documents and spend 1 hour showing us how you evaluate quality?"
- If the SME still refuses: escalate to client project lead. If still blocked: document that requirements are based on Solution Architect's domain knowledge (not client-validated) -- this is a risk that goes in the risk register.

**"The client sponsor is too senior/busy for a 2-hour discovery session"**
- Pharma clients, especially VP-level sponsors, will not sit through a 2-hour discovery. Adapt the discovery format:
  1. **Option A -- Delegate model:** Ask the sponsor to designate a working-level person (associate director, senior manager, or lead SME) for the detailed discovery. The sponsor attends only the 30-min intake call and 30-min sign-off.
  2. **Option B -- Async-first model:** Send a structured discovery questionnaire (see template in Section 1.2.1) that the client fills out on their own time. Follow up with a focused 45-min call only for gaps and ambiguities.
  3. **Option C -- Artifact-driven model:** Skip the discovery conversation. Instead, collect 5 completed examples, their SOPs, and their style guide. The Solution Architect drafts the requirements document from the artifacts alone, then shares with the client for correction. This works best when the domain (e.g., CSR authoring) is well-understood by the team.
- **Fallback:** If the client provides nothing -- no examples, no SOPs, no discovery time -- document this as a risk and proceed with the Solution Architect's domain knowledge. Set expectations explicitly: "We are building against our understanding of standard [X] practices. Client-specific conventions will need to be captured once you review early outputs."

**1.2.1 Async Discovery Questionnaire Template**

```
Subject: Discovery Questionnaire -- [Project Name]

We need the following to define the project scope. Please answer what you can
and leave blanks for items you'd prefer to discuss on a call.

1. CURRENT PROCESS
   - Who does this work today? (role, not name)
   - How long does it take per [document/asset]?
   - What tools/systems are used?

2. INPUTS
   - What source documents does the person start with? (attach 1-2 examples if possible)
   - Are there templates, SOPs, or style guides that govern the output? (attach if yes)

3. OUTPUTS
   - What does the final deliverable look like? (attach 3-5 completed examples)
   - What sections/components does it contain?
   - What format? (Word, PPT, PDF, other)

4. QUALITY
   - What are the most common errors or rejections?
   - What does a "perfect" output look like vs. "acceptable"?
   - Are there specific regulatory or compliance standards it must meet?

5. SCALE AND TIMELINE
   - How many of these do you produce per month/quarter?
   - What is the desired turnaround time?
   - Is there a specific deadline or milestone driving this?

6. ENVIRONMENT
   - Where should this run? (your cloud, our cloud, hybrid)
   - Any data residency or security requirements?
   - Any system integrations needed? (Veeva, CTMS, SharePoint, etc.)
```

**"Requirements keep changing mid-build"**
- This is a scope change. See Section 5 below.

### 1.3 Existing Products: New Client Onboarding

When a new client comes onto an existing platform (e.g., new pharma company on MWA):

```
1. Standard discovery session (same as above, but can use Option B or C for busy clients) -- 1-2 hours
2. Client-specific KB creation:
   - Extract client SOPs, style guides, brand guidelines
   - Create client-specific corrections KB
   - Create client-specific eval dataset rows (5-10 rows on top of universal)
3. Run existing skills against client's sample documents
4. Score outputs against client-specific rubric
5. If score >= threshold: ready for pilot
6. If score < threshold: identify gaps, modify skills or KBs, re-test
```

**Timeline: 1-2 weeks** (much faster than new product because skills already exist)

### 1.4 Feature/Change Requests on Existing Products

```
1. Request received (client, internal, or from production monitoring)
2. Classify:
   a) Bug fix (system not doing what skill says) -> Fast-track: fix + regression test + deploy
   b) Skill improvement (system doing what skill says but quality insufficient) -> Standard: update skill + eval + PR
   c) New capability (system needs to do something it doesn't today) -> Full: may need new skill, new eval dataset, solutioning workshop
3. For (c): goes through engagement typing (see below)
```

### 1.5 Engagement Typing

Not every request needs the full 5-stage process.

| Type | Description | Stages Required | Examples |
|------|------------|----------------|---------|
| **A -- New Product/Major Feature** | Greenfield build or major new capability | All 5 stages, full gates | "Build a new MedCom asset generation pipeline" |
| **B -- Significant Enhancement** | New section type, new document format, major skill overhaul | Stages 2-5 (skip requirement gathering if requirements clear) | "Add CSR Section 14 support to MWA" |
| **C -- Skill/KB Improvement** | Improve quality on existing capability | Stages 3-4 only (build-test-deploy) | "Section 11 clinical interpretation score is too low" |
| **D -- Bug Fix** | System not behaving per skill instructions | Fast-track: fix -> eval -> engineer review -> deploy | "Section 11 is printing table headers twice" |
| **E -- Internal Tooling / Productivity** | Tools for the team's own workflow, not client-facing | Stages 2-3 only, no client gates, engineer approval sufficient | "Build MCP server for internal Cursor workflows", "Streamlit eval dashboard" |
| **F -- Demo / Competitive Benchmark** | BD-driven demo, competitive analysis, or proof-of-feasibility | Stage 2 (lightweight) + time-boxed build, no production gates | "Show MedCom capability to prospective client", "Benchmark against Gamma on visual generation" |

**Classification criteria:**
- Does it need new eval datasets? -> Type A or B
- Does it need a solutioning workshop? -> Type A
- Does it only change existing skills/KBs? -> Type C
- Is it a code/pipeline fix only? -> Type D
- Is it for internal use, not client delivery? -> Type E
- Is it a one-off demo or competitive exercise? -> Type F

**Why Type E and F matter:** The team regularly builds internal productivity tools (MCPs, eval dashboards, Cursor skills) and one-off demos for BD. Without explicit typing, these either get treated like production work (too much process, too slow) or get no process at all (straight to production, no review). Type E and F give them a lightweight but defined path.

### 1.6 Handling the MedCom Pilot Specifically

MedCom is the first engagement running through this WoW. The following requirements are specific to MedCom and serve as a worked example for future Type A engagements.

**MedCom context:**
- MedCom = Medical Communications: generation of visual assets (slides, infographics, key messages) from clinical/scientific data
- The assigned solution architect owns this track; deployment time is the identified main challenge
- Visual generation introduces requirements not present in text-based MWA/MLR work

**MedCom-specific requirement considerations:**
1. **Input types differ from MWA:** Inputs include clinical data, brand guidelines, visual templates (PPT masters, style guides with color palettes, font specs), and narrative briefs -- not TFLs and protocols.
2. **Output is visual, not textual:** Eval dimensions must include visual quality (layout, brand compliance, readability) alongside content accuracy. The eval rubric needs visual scoring dimensions that standard CSR rubrics don't cover.
3. **Competitor baseline:** Gamma/Presentee can generate presentations from prompts. The requirements document must include a competitive benchmark section: what can commodity tools already do? What is the delta the team must deliver above that? (See Section 1.9.)
4. **Asset types vary widely:** A "MedCom asset" could be a conference poster, a slide deck, a leave-behind, an email, or an infographic. Requirements must enumerate which asset types are in scope for the pilot vs. deferred.
5. **Brand compliance is non-negotiable:** Pharma clients have rigid brand guidelines. The requirements must capture these as hard constraints (color codes, font families, logo placement rules, legal disclaimers).
6. **Regulatory review of promotional materials:** Unlike CSR authoring (which is internal), MedCom assets often go through MLR (Medical-Legal-Regulatory) review before use. The requirements should capture whether the system needs to produce MLR-ready annotations or references.

**MedCom pilot Stage 1 checklist (on top of standard):**
- [ ] Visual template inventory collected from client (PPT masters, brand guides)
- [ ] Asset types in scope for pilot enumerated (e.g., slide deck only, not poster)
- [ ] Competitive benchmark established (what Gamma/Presentee can do on the same input)
- [ ] Visual quality scoring dimensions defined in eval rubric
- [ ] Brand compliance checklist extracted from client brand guide
- [ ] MLR annotation requirements clarified (in scope or out)

### 1.7 Pharma-Specific Requirements Checklist

Every pharma engagement has regulatory and compliance dimensions that general software requirements miss. Capture these during discovery.

**Regulatory and compliance requirements:**

| Requirement Area | Questions to Ask | Why It Matters |
|-----------------|-----------------|----------------|
| **Audit trail** | Does the client need to trace every output back to its source data? Do they need a log of which model version, skill version, and KB version produced each output? | Pharma companies submitting documents to regulators (FDA, EMA) may need to demonstrate the provenance of AI-generated content. Even if not required today, clients will ask for this as regulatory scrutiny of AI in pharma increases. |
| **Validation requirements** | Does the client consider this a GxP system? Do they require IQ/OQ/PQ (installation/operational/performance qualification)? | If the system is used in a regulated workflow (e.g., generating content that goes into a regulatory submission), the client may need formal validation documentation. This drastically changes the deployment and testing requirements. |
| **21 CFR Part 11 / Annex 11** | Does the output need electronic signatures? Do they need user authentication, access controls, and tamper-proof audit logs? | US FDA (21 CFR Part 11) and EU (Annex 11) regulate electronic records in pharma. If outputs are considered electronic records, the system must meet specific technical controls. |
| **Data classification** | What sensitivity level is the input data? (public, confidential, restricted, patient-level) | Determines whether data can be sent to third-party LLM APIs, what encryption is needed, and whether data residency constraints apply. Patient-level data almost certainly cannot be sent to Claude/GPT APIs without a BAA or on-premise deployment. |
| **Model explainability** | Does the client need to explain to regulators how the AI reached its output? Do they need confidence scores or uncertainty indicators? | Regulatory agencies increasingly ask about AI/ML transparency. If the client is submitting AI-assisted content, they may need documentation of the model's decision-making process. |
| **Change control** | Does the client require formal change control for any modification to the system (skill updates, KB changes, model upgrades)? | Validated systems in pharma require change control procedures. A skill update that would normally be a PR might need a formal change request, impact assessment, and re-validation. |
| **Retention requirements** | How long must outputs and their associated metadata be retained? | Pharma companies typically retain regulatory submission data for 15+ years. The system's output storage and archival strategy must accommodate this. |

**When to escalate:** If the client answers "yes" to GxP, 21 CFR Part 11, or formal validation requirements, escalate to Leadership immediately. These requirements fundamentally change the cost, timeline, and architecture. They cannot be added mid-build.

**Default position for non-validated use cases:** Most current engagements (CSR authoring, MedCom) produce draft outputs that undergo human review before use. In this case, the system is a "productivity tool" not a "validated system." Frame it this way to clients: "Our system produces drafts that your team reviews. The human review is the validation step. Our eval framework ensures draft quality is consistently high enough that review is efficient."

### 1.8 Agentic vs. Non-Agentic Requirement Signals

During discovery, capture signals that will inform the solutioning workshop's complexity decision. Don't decide architecture during requirements -- but do collect the data the solutioning workshop needs.

**Signals to capture during discovery:**

| Signal | What to Ask/Observe | Implication for Solutioning |
|--------|--------------------|-----------------------------|
| **Fixed vs. variable workflow** | "Is the process the same every time, or does it change based on the input?" | Fixed = likely chain/router. Variable = possibly agentic. |
| **Decision points** | "Where does the person doing this manually have to make a judgment call?" | Many judgment calls = higher complexity. But judgment calls with clear rules = router, not agent. |
| **Iteration/self-correction** | "Does the person review their own output and revise? How many times?" | If the manual process involves self-review loops, the automated process may need them too -- but first try a single-pass chain and see if quality is sufficient. |
| **Cross-document reasoning** | "Does this task require pulling information from multiple documents and synthesizing?" | Multi-source synthesis is common in pharma. It doesn't automatically require agents -- RAG with good chunking often suffices. |
| **Error recovery** | "What happens when something goes wrong in the manual process? How is it caught and fixed?" | If the manual process has built-in error recovery (e.g., QC reviewer catches mistakes), the automated process needs comparable guardrails. |
| **Output variability** | "Could two equally skilled people produce significantly different outputs for the same input?" | High variability = the task has subjective elements. This affects eval design (wider acceptable score ranges) more than architecture choice. |
| **Tool use** | "Does the person use other tools during this task? (calculators, databases, reference systems)" | If the manual process involves tool use, the automated process may need tool-calling capability -- which is an agentic feature. |
| **Parallelizable subtasks** | "Can parts of this task be done simultaneously by different people?" | Yes = consider parallel execution architecture, which doesn't require agents but does require orchestration. |

**Record these signals in the requirements document.** The solutioning workshop uses them as input. See Section 2.4 (Complexity Ladder) for how signals map to architecture decisions.

### 1.9 Competitive Landscape Context in Requirements

The team is not building in a vacuum. Competitors (Kopli for MLR, Gamma/Presentee for MedCom, Claude Cowork for general productivity) set the floor for what clients expect. Requirements should capture competitive context.

**Competitive context section in requirements document:**

## Competitive Landscape Context

### What commodity tools can do today
- [Tool 1]: [What it does on this task, e.g., "Gamma can generate a slide deck from a text prompt in 30 seconds"]
- [Tool 2]: [What it does, e.g., "Kopli claims 90% accuracy on MLR review with 2-hour turnaround"]

### Where commodity tools fall short (our differentiation opportunity)
- [Gap 1]: [e.g., "Gamma cannot enforce client-specific brand guidelines beyond basic templates"]
- [Gap 2]: [e.g., "Kopli does not handle client-specific claims libraries or SOPs"]

### Client-aware differentiation
- [What the client specifically needs that commodity tools cannot provide]
- [Why Indegene's domain knowledge, client-specific KBs, or pharma-grade evals matter here]

### Competitive benchmark target
- Minimum: Parity with [tool] on [dimension] (e.g., "at least as fast as Gamma on basic slide generation")
- Differentiation: Exceed on [dimension] (e.g., "brand compliance that Gamma cannot do")

**Who provides this:** Solution Architect, informed by the monthly landscape scan (see Cross-Cutting Operations doc, Section 3.4). If the SA doesn't know the competitive landscape for this task, flag it -- someone on the team should research it before solutioning.

**Why this matters for requirements:** If the team doesn't know what competitors can do, they risk building something that a free tool already handles -- or setting quality targets that are below what the market already offers.

---

## 2. Solutioning Workshop Process

### 2.1 When to Hold a Workshop

- **Always** for Type A engagements
- **Usually** for Type B if the enhancement is architecturally significant
- **Never** for Type C or D -- these go straight to build
- **Lightweight version (1 hour)** for Type E (internal tooling) -- scope and approach only, no formal output doc
- **Lightweight version (1 hour)** for Type F (demo/benchmark) -- scope, timeline, and what "good enough for demo" means

### 2.2 Pre-Workshop Preparation (1-2 days before)

| Attendee | Preparation |
|----------|------------|
| **Facilitator** (GenAI Solution Approver -- typically the Director or Senior Manager) | Prepare requirements summary (1-pager). Frame the key decisions to be made. Identify 2-3 possible approaches. |
| **Solution Architect(s)** | Review requirements. Read similar past skills/architectures. Draft initial thoughts on approach. Bring domain context. |
| **Engineer(s)** | Review requirements. Assess technical feasibility of approaches. Identify infrastructure constraints. Check what existing components are reusable. |
| **QC/Testing rep** (if available) | Review eval dataset plan. Identify what test cases are hardest. Bring past failure patterns. |

**Pre-workshop packet (sent 2 days before):**
## Solutioning Workshop: [Project Name]
**Date:** [Date] | **Duration:** [2-4 hours]
**Decision to make:** [1-sentence framing]

### Requirements Summary
[1-page summary from Stage 1]

### Agentic Requirement Signals (from discovery)
[Summary of signals captured in Section 1.8 -- fixed vs. variable workflow,
decision points, tool use, etc.]

### Possible Approaches
1. [Approach A -- brief description]
2. [Approach B -- brief description]
3. [Approach C -- brief description]

### Existing Components That May Be Reusable
[List from skills catalog]

### Competitive Context
[What commodity tools can do on this task -- from Section 1.9]

### Constraints
- Timeline: [X weeks]
- Budget: [$X for API costs]
- Infrastructure: [what's available]
- People: [who's available, how much time]
- Regulatory: [any pharma-specific constraints from Section 1.7]

### Questions to Resolve
1. [Question 1]
2. [Question 2]

### 2.3 Workshop Agenda

The agenda adapts to complexity. Not every workshop needs 3 hours.

**Suggested standard agenda (3-hour workshop) -- for Type A engagements:**

```
0:00-0:15  Context setting (Facilitator)
           - Read the room: does everyone understand the requirements?
           - State the decisions to be made today
           - State the agentic signals from discovery

0:15-0:45  Complexity Ladder walk-through (All)
           - Can this be a simple prompt chain?
           - Does it need routing?
           - Can subtasks be parallelized?
           - Is it genuinely open-ended -> agent needed?
           - Each step: cite evidence from eval data or similar past experience

0:45-1:30  Architecture design (All)
           - Whiteboard or draw.io: agent topology, skill map, data flow
           - Identify: which skills exist, which need creation
           - Identify: KB requirements
           - Estimate: how many LLM calls, approximate cost per run
           - Engineer validates: can we deploy this? Any infra blockers?

1:30-1:45  BREAK

1:45-2:15  Non-functional requirements (Engineer-led)
           - Latency budget (max end-to-end time)
           - Concurrency needs (how many simultaneous runs)
           - Cost ceiling per output
           - Security / data handling requirements
           - Deployment environment constraints
           - Pharma-specific: audit trail, data classification, retention (from 1.7)

2:15-2:45  Decision & action items (Facilitator)
           - State the decision: approach X because [rationale]
           - If disagreement: see 3.2 below
           - Assign: who builds which skill, who creates eval dataset, who handles infrastructure
           - Timeline: range estimate with milestones

2:45-3:00  Document (Note-taker)
           - Fill in the decision record template
           - Fill in the architecture diagram
           - Capture all action items with owners and deadlines
```

**Suggested compressed agenda (1.5-hour workshop) -- for Type B engagements or lower-complexity Type A:**

```
0:00-0:10  Context setting (Facilitator)
           - State the problem and constraints
           - Show which existing skills/components apply

0:10-0:30  Complexity Ladder (abbreviated)
           - Focus on: does this change the existing architecture or extend it?
           - If extending: which complexity level does the extension sit at?

0:30-1:00  Architecture delta (All)
           - What changes from the current architecture?
           - New skills, modified skills, new KBs
           - Impact on existing eval datasets

1:00-1:15  Decision & action items (Facilitator)
           - State the decision, assign work, set timeline

1:15-1:30  Document (Note-taker)
```

**Suggested lightweight agenda (1-hour workshop) -- for Type E/F:**

```
0:00-0:10  What are we building and why?
0:10-0:30  Scope: what's in, what's out, what does "done" look like?
0:30-0:45  Approach: quick consensus on architecture (no formal complexity ladder)
0:45-1:00  Who does what, by when? Hard deadline for time-box.
```

### 2.4 The Complexity Ladder -- Worked Examples

**Level 1: Simple Prompt Chain (deterministic, fixed steps)**

Example: Converting a structured data table into a formatted paragraph.
- Input: Table 14.1 (demographics)
- Process: Extract values -> format into narrative template -> validate against source
- Why not agentic: Steps are known in advance. No decision-making needed. Same process every time.
- Evidence to justify: Run 10 test cases. If simple chain achieves >90% eval score, don't escalate.
- **Agentic requirement signals that point here:** Fixed workflow, no decision points, no tool use, no iteration needed.

**Level 2: Router (different inputs need different handling)**

Example: CSR section authoring where different section types need different skills.
- Input: "Author Section 11" or "Author Section 12" (different requirements per section)
- Process: Classify input -> route to appropriate skill -> execute -> validate
- Why not agentic: Once classified, each path is deterministic. The routing logic is fixed.
- Evidence: Test the router on 20 inputs across 4 section types. If classification accuracy >95%, router is sufficient.
- **Agentic requirement signals that point here:** Fixed workflow per path, but multiple distinct paths based on input type.

**Level 3: Parallel Execution (independent subtasks)**

Example: Authoring multiple CSR sections simultaneously.
- Input: Full set of source documents
- Process: Parse sources -> spawn parallel workers for Section 10, 11, 12, etc. -> validate each -> assemble
- Why not agentic: Each section is authored by a known skill. The parallelism is planned, not decided at runtime.
- Evidence: Compare parallel vs. sequential execution. If parallel is 3x faster with no quality loss, use it.
- **Agentic requirement signals that point here:** Parallelizable subtasks identified during discovery, but each subtask is individually deterministic.

**Level 4: Agent (genuinely open-ended)**

Example: Auto-refinement -- the system doesn't know in advance what skills to modify or how.
- Input: Eval failures and source documents
- Process: Analyze failures -> hypothesize root cause -> modify skill or KB -> test -> iterate
- Why agentic: The steps cannot be predicted. The system makes judgment calls at each step.
- Evidence: Would require a person to make these decisions? If yes, and there's enough guardrails to make it safe, an agent is warranted.
- **Agentic requirement signals that point here:** Variable workflow, many decision points, iteration/self-correction required, tool use needed.

**Level 5: Multi-Agent Orchestration (multiple agents coordinating)**

Example: End-to-end document generation where an orchestrator delegates to specialized agents that may need to communicate results to each other.
- Input: Complex multi-part request requiring different expertise
- Process: Orchestrator decomposes task -> assigns to specialized agents -> agents may pass intermediate results -> orchestrator assembles and validates
- Why multi-agent: Single agent cannot hold sufficient context for the full task; specialized agents produce better outputs within their domain.
- Evidence: Single-agent approach hits context window limits or quality degrades significantly when all instructions are in one prompt. Specialized agents score >15% higher on their respective domains.
- **Agentic requirement signals that point here:** Cross-document reasoning across many sources, tool use, decision points at multiple levels, output variability. But be disciplined -- most tasks that feel like they need multi-agent are actually Level 2 (router) or Level 3 (parallel) in disguise.

**The default presumption is the lowest level that works.** Every step up the ladder must be justified by eval evidence or past experience, not by architectural ambition. The team's historical anti-pattern (identified in earlier sessions) is over-engineering with agents when a simpler approach would suffice.

### 2.5 Workshop Output Template

## Solutioning Workshop Output: [Project Name]

### Decision
Approach: [Chosen approach]
Rationale: [Why -- link to eval evidence or past experience]
Complexity level: [Chain / Router / Parallel / Agent / Multi-Agent / Hybrid]

### Architecture
[Diagram: ASCII art, draw.io link, or Mermaid diagram]

### Skill Map
| Skill | Status | Owner | Est. Effort |
|-------|--------|-------|------------|
| [skill-name] | Exists / To Create / To Modify | [Name] | [Range] |

### KB Requirements
| KB | Type | Status | Source |
|----|------|--------|--------|
| [kb-name] | structural/conventions/corrections | Exists / To Create | [Where data comes from] |

### Non-Functional Requirements
- Max latency: [X minutes]
- Cost ceiling: [$X per output]
- Concurrency: [X simultaneous runs]
- Deployment: [Internal / Client cloud]

### Pharma-Specific Requirements
- Audit trail: [Required / Not required / TBD]
- Data classification: [Public / Confidential / Restricted]
- Validation status: [GxP / Non-GxP]
- Retention: [X years]

### Eval Dataset
- Universal dataset: [Exists / To Create -- N rows]
- Client-specific: [To Create -- N rows]
- Edge cases: [N rows targeting specific risks]

### Timeline
- [Range estimate with milestones]

### Risks
| Risk | Mitigation |
|------|-----------|
| [Risk 1] | [Mitigation] |

### Action Items
| Action | Owner | Due |
|--------|-------|-----|
| [Action 1] | [Name] | [Date] |

---

## 3. Solution Review & Approval

### 3.1 Review Process

After the solutioning workshop, the output document goes through:

```
1. Peer SA review (async, 1 day)
   - Does the architecture make sense from a domain perspective?
   - Are the skills well-scoped?
   - Are there edge cases the workshop missed?

2. Engineer review (async, 1 day)
   - Is this technically implementable?
   - Infrastructure concerns?
   - Estimated deployment complexity?

3. If CTO office involved:
   - Share architecture diagram
   - Get acknowledgment (not blocking approval -- just awareness)
   - Document their feedback even if we proceed without their sign-off

4. GenAI Solution Approver review (30 min)
   - Aligns with strategy?
   - Resource allocation feasible?
   - Client expectations realistic?
```

### 3.2 Handling Disagreement

The team has a documented philosophical split: architecture-first vs. experimentation-first. The WoW resolves this with a **structured approach:**

1. **For Type A (new product):** Start with a 1-week experimentation spike (experimentation-first) to validate the basic approach. THEN document the architecture (architecture-first) before full build.

2. **For Type B (enhancement):** Architecture-first -- the system already exists, so changes should be designed before implemented.

3. **For Type C (improvement):** Experimentation-first -- try the skill change, run evals, iterate.

**If the team still disagrees after the workshop:**
- Facilitator states the decision and rationale
- Dissenter's objection is documented in the decision record
- Decision stands unless new evidence emerges
- Revisit at mid-sprint check if the chosen approach isn't working

### 3.3 Preventing Leadership Override of Process

A known risk: the team acknowledged the tendency toward ad-hoc solutioning on calls. Safeguards to prevent anyone -- including leadership -- from bypassing the process they committed to:

1. **The "24-hour rule":** No architectural commitment is made on a client call. If a client asks "can you do X?" the answer is always "let me assess and get back to you within 24 hours." This gives time for a proper evaluation, even if informal.
2. **Post-call debrief:** If a client call surfaces a potential new capability or approach, the person on the call writes a 3-sentence summary in the team channel within 1 hour: what was discussed, what was tentatively suggested, and what needs proper evaluation.
3. **No-blame retrospective trigger:** If someone (including leadership) makes an on-call commitment, the team treats it as a learning moment in the next retro, not a blame event. The commitment is honored to the client, but the internal process is corrected.
4. **Workshop-or-escalate:** For any Type A or B engagement, either a workshop happens or the decision to skip it is explicitly documented with rationale and risk acceptance by the person skipping it.

---

## 4. POC / Experimentation Process

### 4.1 When Is a POC Needed?

| Scenario | POC Needed? |
|----------|-------------|
| We've never done this document type before | Yes |
| We're trying a new framework or architecture pattern | Yes |
| Client wants to see feasibility before committing | Yes |
| We're improving quality on an existing skill | No -- just run evals |
| We're adding a section type to an existing pipeline | Depends on complexity -- if >50% new skills, yes |
| Leadership wants a demo for BD/sales | Type F engagement -- time-boxed build, not a POC |
| We need to benchmark against a competitor | Type F engagement -- time-boxed build, not a POC |

### 4.2 POC Structure

```
POC Brief (Solution Architect, 1 hour to write):
  - Hypothesis: "We believe [approach X] can achieve [target quality] on [document type]"
  - Scope: Exactly which sections/features are IN the POC and which are OUT
  - Success criteria: Specific eval scores on specific dataset rows
  - Time-box: Maximum [1-2 weeks] -- hard stop regardless of state
  - Budget: Maximum [$X] in API costs
  - Output: Working prototype + eval results + go/no-go recommendation

POC Execution (1-2 weeks):
  Day 1-2: Create minimum viable skills (2-3 core skills)
  Day 2-3: Create minimum eval dataset (5-10 rows)
  Day 3-7: Build, test, iterate. Run auto-refinement if applicable.
  Day 7-8: Run final eval. Document results.
  Day 8-10: Present to team. Go/no-go decision.

Go/No-Go Criteria:
  GO: Eval scores >= 70% of target threshold + clear path to improvement
  CONDITIONAL GO: Eval scores 50-70% of target + identified specific fixable gaps
  NO-GO: Eval scores < 50% of target OR fundamental approach doesn't work
```

### 4.3 Preventing "POC Goes Straight to Production"

This was the #1 anti-pattern identified in the discussions. Safeguards:

1. **POC code lives on a separate branch** -- never merged to main without going through full Build Gate
2. **POC eval datasets are marked as "POC quality"** -- must be expanded to full dataset before build starts
3. **POC is explicitly NOT client-deliverable** -- it's internal validation only
4. **POC output document includes a "What's Missing for Production" section** -- this becomes the Stage 2 input
5. **Leadership must formally approve transition from POC to Build** -- with explicit acknowledgment of remaining work

### 4.4 Handling Leadership Pressure to Ship POC

A known risk: POCs going straight to production without proper productionization. This happens because:
- Leadership wants to show results to senior stakeholders/clients quickly
- The POC "works on my machine" and looks good in a demo
- The gap between POC and production is invisible to non-engineers

**How the process handles this without becoming a bottleneck:**

1. **Make the gap visible.** Every POC output includes a "Production Readiness Assessment" table:

## Production Readiness Assessment

| Dimension | POC Status | Production Requirement | Gap |
|-----------|-----------|----------------------|-----|
| Eval coverage | 5 rows, 2 edge cases | 20+ rows, 5+ edge cases | 15+ rows needed |
| Error handling | Happy path only | Graceful failure on bad input | Not built |
| Concurrency | Single user | 5+ simultaneous | Not tested |
| Cost per run | $X (unoptimized) | <$Y target | Need optimization |
| Monitoring | None | Full observability | Not built |
| Security | Dev credentials | Production secrets management | Not configured |
| Rollback | None | One-command rollback | Not built |
| Client-specific KB | Generic | Client SOPs integrated | Not started |

2. **Offer a "fast path" that is not a shortcut.** If leadership needs to show something to a client, offer a structured demo (Type F engagement) using the POC -- clearly framed as a demo, not a deployment. The demo buys time for proper productionization.

3. **Estimate the production gap explicitly.** "The POC took 1 week. Production readiness will take 3-4 additional weeks. Here is why, broken down by task." This prevents the perception that POC = 90% done.

4. **Never say "we can't."** Say "we can, and here is what it takes." Leadership is more receptive to a plan with a timeline than to a refusal.

---

## 5. Client Expectation Setting

### 5.1 The Quality Conversation (During Stage 1)

**Script for explaining LLM quality to pharma clients:**

> "Our platform uses AI to author documents based on your source data. We measure quality using an evaluation framework we'll define together -- it measures [accuracy, completeness, interpretation, compliance, and style].
>
> We typically target [85%+] quality on this rubric, which means outputs are comparable to manual authoring. However, LLM-based systems are inherently probabilistic -- the same input may produce slightly different outputs each run.
>
> What we guarantee: (1) Every output is tested against our evaluation suite before delivery. (2) When we discover a quality gap, it's added to our test suite so it's caught automatically going forward. (3) We monitor quality weekly and share metrics with you.
>
> What we cannot guarantee: 100% perfection on every output. Manual review of AI outputs remains essential, just as it is with human-authored documents."

### 5.2 Pharma-Specific Expectation Setting

Beyond general LLM uncertainty, pharma clients have domain-specific concerns. Address these proactively -- do not wait for the client to raise them.

**Audit trail and traceability:**
> "Every output our system produces is traceable. We log which model version, skill version, and knowledge base version generated each output, along with the input documents used. If you need to demonstrate provenance for a regulatory submission or audit, we can provide this metadata."

**Regulatory submission readiness:**
> "Our system produces draft content. It is not a validated system in the GxP sense -- it is a productivity tool that accelerates your team's work. Your team's review and approval of the output is the validation step. If your regulatory affairs team needs formal validation documentation, we can discuss what that would require as a separate workstream."

**Data handling:**
> "We process your documents using [specific model provider, e.g., Anthropic Claude]. Data is transmitted via encrypted API calls and is not used for model training. [If applicable: We can deploy within your cloud environment for additional data control.] We can provide our data processing agreement for your information security team's review."

**Hallucination and accuracy:**
> "Our evaluation framework specifically tests for data accuracy -- every numeric value in the output is checked against source documents. Our target is zero tolerance for fabricated data. When we say '85% quality,' that does not mean 15% of numbers are wrong -- it means non-accuracy dimensions like style and interpretation have room for improvement. Factual accuracy is binary: pass or fail."

### 5.3 Timeline Communication

**Always give range estimates:**
- "We expect to have a working prototype in 2-3 weeks."
- "From prototype to client-ready quality, typically 3-5 sprints, depending on the complexity of your SOPs."
- "We'll share progress at each sprint review so you can see actual outputs and decide if we're on track."

**Never say:**
- "It will be done by [specific date]" (unless you have high confidence AND buffer)
- "This is easy" (pharma AI is never easy)
- "The system will handle all cases" (scope the specific document types explicitly)

### 5.4 Scope Change Management

```
Client requests something new or different mid-build
  |
1. Acknowledge: "I understand you'd like [X]. Let me assess the impact."
   Do NOT agree or commit on the call.
  |
2. Impact Assessment (Solution Architect, 2-4 hours):
   - Does this change the eval rubric?
   - Does this need new skills or KB entries?
   - What's the effort estimate?
   - Does this push the timeline?
   - Does this change the cost?
  |
3. Scope Change Document:
   - What was originally in scope
   - What the client is requesting
   - Impact: timeline (+X weeks), cost (+$X), quality risk
   - Options: (a) Add to scope with adjusted timeline, (b) Replace another item, (c) Defer to Phase 2
  |
4. Client Discussion:
   - Present options. Get explicit agreement.
   - Document the decision.
  |
5. Update:
   - Requirements document
   - Eval dataset (if rubric changed)
   - Sprint backlog
   - Stakeholder communication
```

**Key principle:** Scope changes are not quality failures. The system isn't broken because the client changed their mind. But the team must stop absorbing changes silently -- every change has a cost, and the cost must be made visible.

### 5.5 Scope Change Management When the Change Comes From Inside

The external scope change process above works for client requests. But scope changes often originate internally:
- A team member sees a new capability on a call and suggests adding it
- A team member discovers a better approach mid-build and wants to pivot
- Senior leadership asks for a demo that requires reprioritizing

**Internal scope change process:**

```
Internal request for change arrives
  |
1. Is this a direction change (affects architecture/approach) or a scope addition (more features)?
  |
  Direction change:
    - Requires workshop or mini-workshop to evaluate
    - Cannot be decided in standup or Slack
    - Existing work in progress: continue or pause? Decision must be explicit.
  |
  Scope addition:
    - Classify as Type A-F (see 1.5)
    - Goes through the same impact assessment as a client scope change
    - Displaces something else or gets scheduled for next sprint
  |
2. Document the change in the sprint backlog with:
   - Who requested it and why
   - What it displaces (if anything)
   - Impact on current commitments
  |
3. If it displaces client-committed work:
   - GenAI Solution Approvers must approve the priority swap
   - Client must be informed of the adjusted timeline
```

**Why this matters:** The team's biggest risk to process discipline is internal, not external. The client scope change process is easy to follow because it involves an external party. The internal change process requires the team to hold itself accountable -- especially when the change comes from leadership.

---

## 6. Cross-References to Other WoW Documents

| Topic | Document | Section |
|-------|----------|---------|
| Golden dataset creation process (detailed) | [Eval Dataset Lifecycle](Granular_Eval_Dataset_Lifecycle.md) | Section 1 |
| Eval scoring rubric design | [Eval Dataset Lifecycle](Granular_Eval_Dataset_Lifecycle.md) | Section 3 |
| Skill file structure and creation | [Skills & KB Lifecycle](Granular_Skills_KB_Lifecycle.md) | Section 1 |
| Knowledge base types and management | [Skills & KB Lifecycle](Granular_Skills_KB_Lifecycle.md) | Section 2 |
| Branch strategy and PR process | [Build, Test & Deploy](Granular_Build_Test_Deploy.md) | Section 1 |
| Testing tiers (Tier 1/2/3) | [Build, Test & Deploy](Granular_Build_Test_Deploy.md) | Section 2 |
| Deployment pipeline | [Build, Test & Deploy](Granular_Build_Test_Deploy.md) | Section 3 |
| Production monitoring | [Build, Test & Deploy](Granular_Build_Test_Deploy.md) | Section 4 |
| Cost management | [Build, Test & Deploy](Granular_Build_Test_Deploy.md) | Section 5 |
| Communication protocols | [Cross-Cutting Operations](Granular_Cross_Cutting_Operations.md) | Section 1 |
| Sprint cadence and estimation | [Cross-Cutting Operations](Granular_Cross_Cutting_Operations.md) | Section 2 |
| Stakeholder management | [Cross-Cutting Operations](Granular_Cross_Cutting_Operations.md) | Section 5 |
| Risk management | [Cross-Cutting Operations](Granular_Cross_Cutting_Operations.md) | Section 6 |
