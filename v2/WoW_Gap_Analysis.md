# Ways of Working: Exhaustive Gap Analysis


## How to Read This Document

This analysis compares what the current proposed WoW approach (3 layers, 5 stages) covers against everything a comprehensive WoW for this team actually needs. Each gap is tagged with:

- **Severity**: CRITICAL (will cause failure if missing), HIGH (will cause repeated pain), MEDIUM (will cause inefficiency), LOW (nice-to-have)
- **Type**: MISSING (not addressed at all), SHALLOW (mentioned but lacks operational depth), IMPLICIT (assumed but never spelled out)
- **Layer**: Where it belongs in the 3-layer structure (L1 = Lifecycle Process, L2 = Technical Playbook, L3 = Templates/Artifacts)
- **Stage**: Which of the 5 stages it maps to, or CROSS-CUTTING if it spans all stages

---

## PART 1: COVERAGE MAP -- What the Current Approach Gets Right

Before listing gaps, acknowledge what the proposed approach already handles well:

| Area | Coverage Quality | Notes |
|------|-----------------|-------|
| 5-stage lifecycle flow | Strong | Requirement > Solutioning > Build/Test > Deploy > Operate. Logical and complete at the stage level. |
| Gate definitions | Strong | Each gate has concrete checklist items. |
| RACI framework | Strong | Functional roles, not names. Covers 10 activity types. |
| Flexibility mechanisms | Strong | Swappable playbooks, quarterly review, fallback paths. |
| Design principles | Strong | Framework-agnostic, MedCom-first, layered not monolithic. |
| Parked questions | Good | Honest about what the WoW cannot decide. |
| Golden dataset concept | Good at concept level | But shallow on operationalization (see gaps below). |

---

## PART 2: CRITICAL GAPS

### GAP-01: No Day-1 Onboarding Playbook
**Type:** MISSING | **Severity:** CRITICAL | **Layer:** L2 + L3 | **Stage:** CROSS-CUTTING

**What's missing:** There is no section on how a new team member gets productive. The WoW assumes the reader already knows the team's context, tools, codebases, clients, platforms, and tribal knowledge. Given that the Director and a team member joined only 6 months ago and still appear to be ramping, this is a live problem.

**Why it matters:** the Senior Manager himself said "If someone asks a question, it will either have to come to me or to the Director. There is no one else that can answer that question." Knowledge silos are the #1 scalability bottleneck for a 10-person team that explicitly decided "we will not be bringing in more people." If someone leaves or a new person joins, there is no documented way to transfer context.

**What it needs to cover (at minimum):**
- Team structure, reporting lines, who owns what product area
- Access provisioning checklist (GitHub, AWS, Cursor, prompt management platform, Jira, client environments, Langfuse/Braintrust, S3 log buckets)
- Map of all active engagements with current status, client contact, and internal owner
- Glossary of Indegene-specific terminology (MLR, MWA, MedCom, CTO office structure, who is the VP/Senior Leadership/the MWA track lead/the CTO in the org)
- Architecture overview of each existing platform (even if just a 1-page diagram per platform)
- "Where to find things" guide: code repos, prompt libraries, eval datasets, SOPs, knowledge bases, S3 log locations
- First-week schedule: who to shadow, what to read, what to try hands-on
- Common failure modes and how to debug them

**Granularity needed:** L3 template (onboarding checklist) + L2 playbook (onboarding guide with links to all resources).

---

### GAP-02: No Incident Response / "2 AM Break" Protocol
**Type:** MISSING | **Severity:** CRITICAL | **Layer:** L1 + L3 | **Stage:** Stage 5 (Operate & Evolve)

**What's missing:** The proposed approach mentions "L1/L2 issues handled by delivery team using runbook" and "L3 escalations loop back to builders." But there is zero specification of:
- What constitutes L1 vs. L2 vs. L3
- Who is on call and when
- Response time SLAs per severity level
- Escalation path with names/roles and contact methods
- What to do when the person who knows the answer is unavailable
- How to communicate to the client during an incident
- Post-incident review process (blameless retro)
- How incidents feed back into the system (correction knowledge bases, eval dataset additions)

**Why it matters:** The transcripts describe a team that is already drowning in delivery support. a Solution Architect identified deployment time as his main challenge on MedCom. The team acknowledged POCs go straight to production without proper operational readiness. When something breaks in production, the current answer is "call the Senior Manager or the Director" -- which is exactly the bottleneck the WoW is supposed to eliminate.

**Real scenario:** An LLM provider has an outage, or a model version gets deprecated, or a client SOP change breaks the prompt chain at 2 AM before a client deadline. Who does what? Today the answer is chaos. The WoW must define the answer.

**Granularity needed:** L1 process (severity classification + escalation ladder), L3 template (incident response runbook template, post-incident review template).

---

### GAP-03: No Financial Tracking / Cost Governance Model
**Type:** MISSING | **Severity:** CRITICAL | **Layer:** L1 + L3 | **Stage:** CROSS-CUTTING (touches all stages)

**What's missing:** The proposed approach mentions "cost estimate within acceptable range" at the Solution Gate and "cost per run" tracking during Build & Test. But there is no actual cost governance framework:
- Who approves API spend? What are the thresholds?
- How is cost tracked per engagement, per client, per sprint?
- What happens when auto-refinement runs burn $100+ in a session (as The Director's demo did)?
- How is cost allocated between R&D/experimentation and billable client work?
- What is the cost ceiling per agent execution in production?
- Who monitors cumulative cost and raises flags?
- How is cost-per-output tracked as a quality metric alongside accuracy?
- Budget for experimentation (Opus usage was flagged as a dependency)

**Why it matters:** the VP's expected metric is "revenue per employee / average revenue per resource." The Director's demo cost ~$42 per CSR run (unoptimized). The team explicitly decided not to add headcount. If API costs balloon without governance, the revenue-per-resource math gets worse, not better. The transcripts also flag that budget for API costs (Opus usage) is a critical dependency that the Director owns but has no framework around.

**Granularity needed:** L1 process (cost governance policy with approval thresholds), L3 templates (cost tracking spreadsheet per engagement, monthly cost review template).

---

### GAP-04: No Client Interaction Model
**Type:** MISSING | **Severity:** CRITICAL | **Layer:** L1 + L2 | **Stage:** Stages 1, 4, 5

**What's missing:** The WoW describes internal processes but barely mentions how the team interacts with clients. The only client touchpoint is "Client/stakeholder signs off on evaluation rubric" in Stage 1. But:
- How are client expectations set at engagement kickoff?
- What does the client see during Build & Test? How often? In what format?
- How are scope changes managed when clients add requirements mid-build?
- How does the team handle the "this doesn't feel right" subjective feedback loop?
- What is the communication cadence (weekly status? demo sessions?)?
- Who is the single point of contact for the client?
- How are client-side SME requirements extracted when "the majority of the people don't want to know how the solution works"?
- What happens when the client's own teams are at loggerheads (Vertex scenario: tech leadership vs. SME head)?
- How is IP protected when deploying in client environments?

**Why it matters:** The team is losing clients (Vertex, AZ). The transcripts describe a pattern where clients complain about "long processing times and time taken for refinement before we reach a certain level of quality." The Vertex case study shows client-side politics directly impacting the team's work. Without a defined client interaction model, the same patterns will repeat.

**Granularity needed:** L1 process (client engagement lifecycle within each stage), L2 playbook (client communication templates, scope change management), L3 templates (kickoff deck template, weekly status template, scope change request form).

---

### GAP-05: No Stakeholder Engagement Map Beyond RACI
**Type:** SHALLOW | **Severity:** CRITICAL | **Layer:** L1 | **Stage:** CROSS-CUTTING

**What's missing:** The RACI covers functional roles for 10 activities. But the team interacts with at least 7 distinct stakeholder groups, each requiring a different engagement model:

1. **CTO Office / Engineering** (Satyak, the CTO Rao, Sreekanth teams) -- The RACI mentions "Engineering (CTO)" but does not define how to actually work with them day-to-day. How do you request engineering support? What is the handoff format? How do you resolve the "you can't write code / you don't understand GenAI" standoff?
2. **DevOps / AWS team** -- Currently requests go through email with unpredictable turnaround. The WoW says "assume DevOps exists" but provides no fallback workflow for the current reality.
3. **SMEs** (a QC team member, a QC team member, or external) -- The WoW makes them Responsible for golden datasets but does not address that "the majority of the people don't want to do all of this."
4. **the VP / VP layer** -- How does the team report progress? What format? What metrics does the VP care about?
5. **Senior Leadership / EVP layer** -- When and how does escalation to this level happen?
6. **the MWA track lead's parallel MWA track** -- How does the team coordinate or avoid collision?
7. **QA teams** -- Mentioned in RACI but no engagement protocol.

**Why it matters:** the Director explicitly said "The accountability everything will be on us." But accountability without defined engagement protocols means the team takes blame for dependencies it cannot control. The CTO office relationship is described as adversarial. The WoW must define how to operate within that reality.

**Granularity needed:** L1 section (stakeholder engagement map: who, what, how, frequency, escalation path for each group), L3 template (stakeholder register per engagement).

---

## PART 3: HIGH-SEVERITY GAPS

### GAP-06: Golden Dataset Operationalization is Surface-Level
**Type:** SHALLOW | **Severity:** HIGH | **Layer:** L2 + L3 | **Stage:** Stage 1

**What's covered (surface level):** "Build golden dataset (input-output pairs scored on 3-5 dimensions)" and "min 20 rows or plan + timeline to create it."

**What's missing at operational depth:**
- **Who physically creates the golden dataset?** The RACI says QA/Testing is Responsible and SME/Domain is Responsible. But the transcripts say "I would not recommend involving SMEs in anything apart from what they already do" (the Senior Manager) and "the majority of the people don't want to know how the solution works." So who actually does it?
- **Where does the source data come from?** Client-provided examples? Historical outputs? Production logs? Manual work products? Each source has different availability and quality.
- **What format?** The bootcamp says "Google Sheets or Excel." Is that the production standard? What columns are mandatory? What metadata is needed (difficulty level, edge case flag, therapeutic area, document type)?
- **How do you score dimensions?** What does a "pass" on "accuracy" mean for MLR vs. MedCom vs. MWA? Who calibrates inter-rater reliability?
- **Minimum viable size per use case type?** 20 rows is mentioned, but for a complex CSR with 15 sections, 20 rows may be 20 documents or 20 sections. The unit is undefined.
- **How is the golden dataset maintained?** When client SOPs change, who updates it? How often? What triggers a refresh?
- **Version control for golden datasets?** The WoW says "version everything" but does not specify how datasets are versioned alongside prompts/skills.
- **Confidentiality handling?** Golden datasets contain client data. How is access controlled? Can they be shared across engagements?
- **Edge case collection process?** How do production failures get systematically added to the golden dataset?

**Why it matters:** The entire eval-driven development approach hinges on golden datasets existing and being good. If the process for creating them is vague, teams will either skip it ("we'll add evals later") or create low-quality datasets that give false confidence. The chicken-and-egg problem raised in Day 2 -- "the thoughts will come up once they see the output" -- remains unresolved.

**Granularity needed:** L2 playbook (step-by-step golden dataset creation guide per use case type), L3 templates (golden dataset template with mandatory columns, scoring rubric template with calibration guide).

---

### GAP-07: No Knowledge Management System Design
**Type:** SHALLOW | **Severity:** HIGH | **Layer:** L1 + L2 | **Stage:** Stage 5 (but feeds all stages)

**What's covered:** The analysis mentions "three levels of knowledge bases" (platform-wide conventions, client-specific brand guidelines/SOPs, user-specific preferences/corrections) and "knowledge should be in structured formats (JSON preferred)."

**What's missing:**
- **Where do knowledge bases live?** File system? Database? Versioned alongside code? The demo used a file/folder-based approach, but the Director himself asked about scaling that.
- **Who curates and maintains each knowledge base?** Knowledge bases that are nobody's job to maintain become stale within weeks.
- **How does institutional knowledge get captured?** The transcripts are full of hard-won lessons (PR should not have gone agentic, folder-based architecture scaling concerns, specific client quirks). Where do these go?
- **How are manual edits converted into correction knowledge bases?** This was mentioned in the demo but has no process defined.
- **What is the "what we tried and what we learned" living document?** The analysis mentions this as a recommendation but the proposed approach does not include it.
- **How does the team avoid repeating mistakes?** There is no retrospective or lessons-learned process defined anywhere in the 5 stages.
- **Cross-engagement knowledge reuse:** When a Solution Architect solves a problem on MedCom, how does a Solution Architect learn about it for his work?

**Why it matters:** "If someone asks a question, it will either have to come to me or to the Director." Knowledge silos were called the bottleneck of scalability. The WoW proposes fixing this but does not define the mechanism.

**Granularity needed:** L1 process (knowledge management lifecycle: capture, store, curate, share, retire), L2 playbook (how to maintain each knowledge base type), L3 templates (decision log template, lessons-learned template, knowledge base contribution form).

---

### GAP-08: No Branch Strategy / Code Contribution Workflow
**Type:** MISSING | **Severity:** HIGH | **Layer:** L2 | **Stage:** Stage 3 (Build & Test)

**What's missing:** The WoW says "Non-engineers contribute skills and prompt logic; engineers review and approve." The Director's call confirmed: "how will we ensure that we are not overwriting each other's code? What is the best practice if everybody is coding?" But the WoW does not answer this question. Specifically:
- What is the branch strategy? (feature branches? trunk-based? GitFlow?)
- What is the PR process? (who reviews, how many approvals needed, what checks must pass?)
- What can non-engineers change without review? (skill files only? prompt configs? any Python code?)
- What requires engineer review? (infrastructure code? pipeline configs? anything touching deployment?)
- How are merge conflicts resolved when 8 people are contributing to the same repo?
- What CI/CD checks run on every PR? (linting? eval suite? cost estimation?)
- How are environment branches managed? (dev/staging/prod promotion flow)

**Why it matters:** This was the single biggest debate of Day 2. The Engineer's core objection was accountability: "If they're not the core contributors, then why access?" The WoW must operationalize the compromise (everyone contributes, engineers review) with enough specificity that the Engineer can enforce quality and non-engineers can contribute without fear of breaking things.

**Granularity needed:** L2 playbook (branch strategy, PR workflow, review checklist, merge policy), L3 template (PR template with mandatory sections).

---

### GAP-09: No Definition of "Quality" and How It Is Measured Over Time
**Type:** SHALLOW | **Severity:** HIGH | **Layer:** L1 | **Stage:** CROSS-CUTTING

**What's covered:** The proposed approach mentions specific metrics in passing: "eval suite passes at 85%+ on golden dataset," "success rate, hallucination rate, latency, cost, domain-specific metrics."

**What's missing:**
- **What are the standard quality dimensions for each product type?** MLR accuracy is different from MedCom visual quality is different from MWA section completeness. These are not one-size-fits-all.
- **Who defines "good enough" and how?** The WoW says "agree on good enough quality thresholds before starting work" but does not define the negotiation process or fallback when stakeholders disagree.
- **How is quality measured in production over time?** Dashboard design, alert thresholds, review cadence, who looks at the numbers weekly?
- **Quality drift detection:** How do you know when a production system's quality is degrading? Model behavior changes, data distribution shifts, SOP changes. What is the monitoring approach?
- **Client satisfaction tracking:** CSATs were mentioned in the original problem statement but do not appear anywhere in the proposed WoW.
- **Quality benchmarking against competitors:** the Director wants to benchmark against Claude Cowork. This is not operationalized.

**Why it matters:** "Clients often complain about long processing times and time taken for refinement before we reach a certain level of quality." The fundamental client problem is quality perception. The WoW must make quality measurable, trackable, and improvable -- not just at gates, but continuously.

**Granularity needed:** L1 process (quality management framework with dimensions per product type, measurement cadence, escalation thresholds), L2 playbook (how to set up quality monitoring per deployment type), L3 templates (quality dashboard specification, quality review meeting agenda).

---

### GAP-10: No Capacity Planning / Work Allocation Model
**Type:** MISSING | **Severity:** HIGH | **Layer:** L1 | **Stage:** CROSS-CUTTING

**What's missing:** The WoW says nothing about how work gets assigned, how capacity is managed, or how the team decides what to work on when everything is urgent. Consider:
- With 10 people across 4 capability pillars (content authoring, content generation, MLR review, visual/MedCom), who works on what?
- How is the 60/30/10 split (delivery/building/experimentation) actually enforced? Who tracks it?
- When a new engagement comes in, how is it staffed? What if everyone is already at capacity?
- What is the prioritization framework when delivery demands conflict with building demands?
- How does the team manage the explicit Catch-22: "they can't build because they're delivering, and they can't stop delivering because there's no one else"?
- What does the Single-Threaded Owner model look like in practice when one person owns a product area but gets pulled into delivery for another area?

**Why it matters:** "It always feels like we are always doing catch up... we rush things." The team explicitly decided not to grow headcount. Without capacity planning, the 60/30/10 aspiration will never happen. The team will default to 100% delivery.

**Granularity needed:** L1 process (capacity planning model, work intake process, prioritization framework), L3 templates (capacity tracker, work intake form, prioritization matrix).

---

### GAP-11: No Retrospective / Continuous Improvement Process
**Type:** MISSING | **Severity:** HIGH | **Layer:** L1 | **Stage:** Stage 5 + CROSS-CUTTING

**What's missing:** The proposed approach has a "Quarterly WoW Review" for the process itself, but no sprint-level or engagement-level retrospective. There is no mechanism for:
- What went wrong on this engagement and why?
- What took longer than expected and what should we estimate differently next time?
- What failure patterns are we seeing repeatedly across engagements?
- What did we learn about a specific technology/approach/client that others should know?
- How do we track whether our process improvements are actually working?

**Why it matters:** "We created a POC on our customer and it straight away went to production." The team has a pattern of repeating the same mistakes. The same Vertex story plays out on AZ. The same blame game happens with engineering. Without structured retrospectives, the WoW itself cannot improve.

**Granularity needed:** L1 process (retrospective cadence: per-sprint, per-engagement, per-quarter), L3 templates (retrospective template with prompts, action item tracker).

---

### GAP-12: No Scope Change / Requirements Evolution Process
**Type:** MISSING | **Severity:** HIGH | **Layer:** L1 | **Stage:** Stages 1-3

**What's missing:** The Requirement Gate assumes requirements are defined once and signed off. But the transcripts explicitly identified the chicken-and-egg problem: "the thoughts will come up once they see the output." The WoW does not address:
- How are scope changes formally requested and evaluated?
- What is the impact assessment process (cost, timeline, quality implications)?
- Who approves scope changes? At what threshold does it require re-running the Solution Gate?
- How do you prevent the "endless iteration" trap where the client keeps adding requirements because they never formally agreed on scope?
- How do client SOP changes (Vertex scenario) trigger formal scope reassessment vs. being absorbed silently?

**Why it matters:** The original problem statement says "clients often complain about long processing times and time taken for refinement." Much of this refinement is actually scope creep disguised as quality issues. Without formal change management, the team cannot distinguish between "the system doesn't work" and "the requirements changed."

**Granularity needed:** L1 process (change request workflow with impact assessment), L3 templates (change request form, impact assessment template).

---

### GAP-13: No Risk Management Framework
**Type:** MISSING | **Severity:** HIGH | **Layer:** L1 + L3 | **Stage:** Stages 1-2

**What's missing:** The analysis document lists 8 critical dependencies and 26 open questions. The proposed approach acknowledges risks but does not define how risks are:
- Identified at engagement kickoff
- Assessed for probability and impact
- Mitigated or accepted with documented rationale
- Monitored throughout the engagement
- Escalated when they materialize

Specific risk categories the WoW should address:
- **Technical risk:** LLM provider outage, model deprecation, framework abandonment (Autogen's 3 pivots in one year)
- **Client risk:** SOP changes, political dynamics, deployment environment constraints
- **Organizational risk:** the VP not approving time allocation, CTO office non-cooperation, the MWA track lead's parallel track
- **Data risk:** Golden dataset quality, client data confidentiality, training data contamination
- **Vendor risk:** Model lock-in (Claude-only vs. model-agnostic), framework lock-in
- **People risk:** Knowledge silos, key person dependency on the Senior Manager/the Director

**Why it matters:** The team has been blindsided repeatedly -- by Vertex pushback, by AZ issues, by framework changes, by leadership changes. A lightweight risk register at engagement kickoff would surface these early.

**Granularity needed:** L1 process (risk identification at Stage 1, risk review at each gate), L3 templates (risk register template, risk assessment matrix).

---

## PART 4: MEDIUM-SEVERITY GAPS

### GAP-14: No Communication Cadence / Reporting Structure
**Type:** MISSING | **Severity:** MEDIUM | **Layer:** L1 | **Stage:** CROSS-CUTTING

**What's missing:**
- What meetings does the team hold? Daily standup? Weekly sync? Sprint review?
- What is reported to the VP and at what cadence?
- What is the format for sprint reviews? (The analysis recommends showing actual LLM outputs including failures, but this is not in the proposed approach.)
- How does the team communicate internally? (Slack channels? Email? Jira? All three?)
- What information must be documented vs. what can be verbal?
- How are decisions communicated to people who were not in the room?

**Why it matters:** "All-hands meetings should include technical deep-dives, not just status updates" was a recommendation from the analysis that did not make it into the proposed approach. The team's communication patterns directly affect whether the WoW gets followed or becomes shelf-ware.

**Granularity needed:** L1 section (communication charter: meeting cadence, reporting format, communication channels by topic type).

---

### GAP-15: No Engagement Typing / Intake Classification
**Type:** MISSING | **Severity:** MEDIUM | **Layer:** L1 | **Stage:** Stage 1

**What's missing:** The Engineering Lead's preparation distinguished between "New Product Engagement" (kickoff checklist), "Ongoing Product" (monthly evaluation), and "Service Engagements" (continue as-is). The proposed WoW treats all engagements identically through 5 stages. But:
- A new greenfield build (MedCom agent from scratch) is fundamentally different from a prompt improvement request on an existing platform (MLR accuracy tuning)
- A client-deployed engagement is different from an internally-deployed one
- A POC/demo is different from a production deployment
- Bug fixes and maintenance don't need to go through a Solutioning Workshop

**What's needed:** An engagement classification matrix at intake that determines which stages and gates are mandatory vs. optional. Example:
- Type A (New Product): All 5 stages mandatory
- Type B (Major Enhancement): Stages 2-5, with streamlined Stage 1
- Type C (Prompt/Skill Improvement): Stages 3-4 only, with regression gate
- Type D (Bug Fix / Maintenance): Fast-track with engineer review only

**Why it matters:** If the WoW mandates the full 5-stage process for a minor prompt tweak, the team will bypass it entirely. The process must scale down for small changes without losing its rigor for large ones.

**Granularity needed:** L1 process (engagement classification criteria, stage applicability matrix), L3 template (intake form with classification logic).

---

### GAP-16: No Solutioning Workshop Protocol
**Type:** SHALLOW | **Severity:** MEDIUM | **Layer:** L2 + L3 | **Stage:** Stage 2

**What's covered:** "Cross-functional workshop (GenAI team + engineering rep minimum)" with an activity list.

**What's missing:**
- How long should the workshop be? (1 hour? Half day? Depends on complexity?)
- Who facilitates? (the Senior Manager? the Director? Rotating?)
- What preparation must attendees do before the workshop?
- What is the agenda structure?
- How are decisions documented during the workshop?
- What happens when the team disagrees? (The experimentation-first vs. architecture-first split is still unresolved.)
- How is the complexity ladder evaluation actually conducted? (Just discussion? Hands-on prototyping? Both?)
- What artifacts come out of the workshop? (The gate checklist says "architecture documented" but not the format or depth.)

**Why it matters:** Both the Director and the Senior Manager committed to stopping ad-hoc solutioning on calls. But without a defined workshop protocol, they will either fall back into old habits or hold workshops that are disorganized and inconclusive. The philosophical split between the Engineer (architecture-first) and the Director (experimentation-first) needs a structured resolution process, not just goodwill.

**Granularity needed:** L2 playbook (workshop facilitation guide with agenda template), L3 templates (workshop preparation checklist, decision record template, architecture diagram template).

---

### GAP-17: No Handoff Package Specification
**Type:** SHALLOW | **Severity:** MEDIUM | **Layer:** L3 | **Stage:** Stage 5

**What's covered:** "Handoff package delivered (architecture docs, skill files with rationale, eval suite, known limitations, runbook, training)."

**What's missing at specification level:**
- What does "architecture docs" mean concretely? System diagram? Data flow? Sequence diagrams? All of the above?
- What level of detail in the runbook? (The difference between "restart the service" and "SSH into X, check Y log, if Z error then run A command" is the difference between a usable and unusable runbook.)
- What format for "known limitations"? (Prose? Structured table with severity/workaround/expected-fix-date?)
- What does training consist of? (Slide deck? Hands-on session? Shadow period? Recorded sessions for future reference?)
- Who signs off that the handoff is complete? (The delivery team receiving it? The builder team releasing it? Both?)
- What is the support warranty period after handoff? (How long does the builder remain available for questions?)
- How is the eval suite transferred? (Does the delivery team know how to run it? Who maintains it post-handoff?)

**Why it matters:** "Solutions that can't be handed off should be flagged as a product design failure." But if the handoff package standard is vague, teams will produce minimal documentation and declare the handoff complete. The current pattern where "delivering needs GenAI expertise which no one else wants to take up" will persist.

**Granularity needed:** L3 templates (handoff package checklist with acceptance criteria per artifact, runbook template with required sections, training session plan template).

---

### GAP-18: No Prompt/Skill Versioning Standard
**Type:** SHALLOW | **Severity:** MEDIUM | **Layer:** L2 | **Stage:** Stage 3

**What's covered:** "Prompt versioning (semantic versions with environment labels)" and "prompts decoupled from code."

**What's missing:**
- Which platform? (Langfuse, Braintrust, AWS-native, custom? Decision is deferred but the WoW should define requirements.)
- What is the naming convention for skills? (skill-mlr-claims-extraction-v2.1? Or free-form?)
- How are skills organized? (By product? By client? By capability?)
- What metadata must be attached to each skill version? (Author, date, eval score, linked golden dataset version, change description)
- What is the promotion workflow? (dev > staging > prod? Who promotes? What checks?)
- How are rollbacks executed? (Revert to previous version? How quickly?)
- How are skill dependencies managed? (If skill A calls skill B, and skill B gets updated, how is regression detected?)

**Why it matters:** The entire build strategy depends on skills being the atomic unit of work. If skills are not properly versioned, named, and organized, the component library vision (40%+ assembly from existing components) will fail. The team will rebuild rather than reuse because they cannot find or trust existing skills.

**Granularity needed:** L2 playbook (skill versioning standard, naming conventions, metadata requirements, promotion workflow).

---

### GAP-19: No IP Protection and Data Security Protocol
**Type:** MISSING | **Severity:** MEDIUM | **Layer:** L1 | **Stage:** Stages 1, 4, 5

**What's missing:** The analysis raises IP protection as a live issue (Vertex deployment made the platform "their product"). But the proposed WoW says nothing about:
- What IP does the team own vs. what becomes client property?
- How are skills, knowledge bases, and eval datasets classified (reusable IP vs. client-specific)?
- What data can be used across engagements and what cannot?
- How is client data handled in development/testing? (Can client documents be used in golden datasets shared with other team members?)
- What are the guardrails for LLM API calls? (Is client data sent to third-party APIs? What are the data residency requirements?)
- How are client environment deployments handled to preserve IP?

**Why it matters:** The Senior Manager's preparation positions golden datasets as "our most valuable IP per client." But without data security and IP classification, this IP is at risk of being lost (deployed into client environments with no retention), contaminated (client data mixed across engagements), or exposed (sensitive data in eval datasets accessible to the full team).

**Granularity needed:** L1 process (IP classification policy, data handling rules per engagement type), L2 playbook (secure development practices for LLM systems), L3 templates (IP classification checklist per engagement).

---

### GAP-20: No Defined Experimentation / Innovation Process
**Type:** MISSING | **Severity:** MEDIUM | **Layer:** L1 | **Stage:** CROSS-CUTTING

**What's missing:** The 60/30/10 allocation (delivery/building/experimentation) is proposed but the 10% experimentation has no structure:
- What qualifies as experimentation vs. building vs. delivery?
- How does someone propose an experiment? (Just start doing it? Write a brief? Get approval?)
- What is the time-box for an experiment?
- How are experiment results shared with the team?
- What happens when an experiment succeeds? (Who decides to productionize it? Through which gate?)
- How does this relate to The Engineer's "monthly innovation sprint" proposal?
- How does the framework evaluation (Strands vs. Claude Agent SDK vs. LangGraph) fit into this?

**Why it matters:** "Every 6 months something new comes up" -- the team needs a structured way to evaluate new approaches without the pattern of adopting something and abandoning it. The Director's 2-week Claude Agent SDK prototype was essentially an unstructured experiment. The WoW should make such experiments repeatable and their results comparable.

**Granularity needed:** L1 process (experiment proposal workflow, time-boxing rules, result-sharing format), L3 template (experiment brief template with hypothesis/method/result structure).

---

### GAP-21: No Upskilling Integration Into the Lifecycle
**Type:** IMPLICIT | **Severity:** MEDIUM | **Layer:** L1 | **Stage:** CROSS-CUTTING

**What's covered:** The Senior Manager's preparation includes a detailed 6-week bootcamp. The Engineer proposed bi-weekly tech talks and monthly innovation sprints. The proposed approach does not mention either.

**What's missing:**
- When does the bootcamp happen relative to the MedCom pilot? (Before? During? In parallel?)
- How does ongoing learning (tech talks, innovation sprints) get protected from delivery pressure?
- What skills are mandatory for which roles? (Must all Solution Architects be able to run evals? Must engineers understand pharma domain?)
- How is skill development tracked and assessed?
- What happens when someone fails to develop a required skill?
- How does the team stay current with the agentic AI ecosystem (which they acknowledged being 6-7 months behind on)?

**Why it matters:** The WoW proposes significant capability expansion (non-engineers contributing code, everyone creating evals, agentic architecture literacy). Without operationalized upskilling, these remain aspirations. The team will default to existing competencies.

**Granularity needed:** L1 section (learning and development cadence embedded in the lifecycle), L3 template (individual development plan template, skill matrix).

---

### GAP-22: No Component Library / Reuse Governance
**Type:** SHALLOW | **Severity:** MEDIUM | **Layer:** L2 | **Stage:** Stage 3

**What's covered:** "40%+ of any new solution is assembled, not built" and "component library (prompt templates, eval frameworks, RAG pipeline patterns, guardrail configs)."

**What's missing:**
- Where does the library live? (Code repo? Shared drive? Dedicated platform?)
- How are components indexed and discoverable? (Tags? Categories? Search?)
- What is the quality bar for a component to be added to the library? (Must pass eval suite? Must have documentation? Must be used on at least 2 engagements?)
- Who maintains the library? (Everyone? A designated librarian? No one, and it rots?)
- How are components versioned? (Same as skill versioning or separate?)
- How does a new engagement know what components exist before starting from scratch?
- What is the licensing model for client-specific components? (Can a component built for Vertex be reused for AZ?)

**Why it matters:** "Every solution we build should leave behind components that make the next solution faster." This is the key productivity multiplier. But component libraries that are not actively curated become dumping grounds that nobody trusts or uses. The WoW must define the governance, not just the aspiration.

**Granularity needed:** L2 playbook (component contribution and consumption workflow, quality criteria), L3 template (component documentation template).

---

### GAP-23: No Auto-Refinement Process Standard
**Type:** SHALLOW | **Severity:** MEDIUM | **Layer:** L2 | **Stage:** Stage 3

**What's covered:** "Run auto-refinement cycles (AI runs tests, compares against golden outputs, modifies skills, re-tests)" and the Build Gate requires "minimum N cycles with documented improvement."

**What's missing:**
- What is "N"? Who decides the minimum number of cycles per engagement?
- What are the guardrails on auto-refinement? (Max cost per session? Max number of skill modifications? Human review after how many iterations?)
- How are auto-refinement sessions scheduled? (Ad-hoc or planned?)
- Who monitors the auto-refinement while it runs? (The demo had Cursor as a testing agent running autonomously.)
- What happens when auto-refinement plateaus? (Quality stops improving despite iterations.)
- How are auto-refinement outputs reviewed before being accepted? (Does every skill change from auto-refinement get human review?)
- How is the cost of auto-refinement justified per engagement?

**Why it matters:** The Director's demo showed quality improving from 4.1 to 9.0 over 17 runs at ~$100. But without process standards, auto-refinement could become an expensive black box. The cost and quality tradeoff must be explicit.

**Granularity needed:** L2 playbook (auto-refinement session planning, guardrails, review process, cost controls).

---

### GAP-24: No Cross-Engagement Consistency Standards
**Type:** MISSING | **Severity:** MEDIUM | **Layer:** L1 | **Stage:** CROSS-CUTTING

**What's missing:** With multiple people working on different engagements (a Solution Architect on MedCom, a Solution Architect on MLR, etc.), there is no defined standard for:
- Consistent naming conventions across engagements
- Consistent folder/project structure
- Consistent eval rubric format
- Consistent documentation depth
- Consistent quality thresholds (is 85% the standard or engagement-specific?)
- Consistent deployment configuration patterns
- Consistent client communication format

**Why it matters:** The team wants to build reusable components and assemble solutions from templates. This only works if outputs from different people and engagements are structurally consistent. Without standards, the "template-first delivery" vision fails because every engagement produces outputs in a different format.

**Granularity needed:** L2 playbook (project structure standard, naming conventions, documentation standards), L3 templates (project scaffolding/template).

---

### GAP-25: No Model Version Management Policy
**Type:** SHALLOW | **Severity:** MEDIUM | **Layer:** L2 | **Stage:** Stages 3, 4, 5

**What's covered:** "Pin model versions (never latest)" and "re-run full eval suite before any model upgrade."

**What's missing:**
- When does the team evaluate new model versions? (As they release? Quarterly? When performance issues arise?)
- Who decides to upgrade a model version in production?
- What is the testing protocol for model upgrades? (Run full eval suite on new version, compare with current, require X% parity?)
- How are model version upgrades coordinated across engagements? (If Claude releases a new Sonnet version, does every engagement upgrade simultaneously or independently?)
- What happens when a model version is deprecated by the provider?
- How is multi-model usage managed? (Tiered model strategy: Haiku for simple, Sonnet for medium, Opus for complex. Who decides which tier for which task? How is this documented?)
- What is the fallback when a model provider has an outage?

**Why it matters:** "What happens when a client wants a different model provider?" was an open question from Day 2. Model version management is not a one-time decision but an ongoing operational concern that affects cost, quality, and reliability.

**Granularity needed:** L2 playbook (model version management policy, upgrade testing protocol, multi-model selection criteria).

---

## PART 5: LOW-SEVERITY GAPS (But Important for Completeness)

### GAP-26: No Team Culture / Working Norms
**Type:** MISSING | **Severity:** LOW | **Layer:** L1 | **Stage:** CROSS-CUTTING

**What's missing:** The WoW is purely process-focused. It does not address:
- Core values or principles the team agrees to operate by
- Decision-making norms (consensus? Leader decides? Majority?)
- Disagreement resolution protocol (the Engineer vs. The Director experimentation debate is still "unresolved")
- Meeting norms (active participation expectations, time zone management if applicable)
- Feedback culture (how do team members give each other constructive feedback?)
- The team building / offsite the Engineer requested

These may feel soft, but for a 10-person team undergoing a major working model change, explicit norms reduce friction.

**Granularity needed:** L1 section (brief team charter with decision-making norms and conflict resolution protocol).

---

### GAP-27: No Documentation Standards
**Type:** MISSING | **Severity:** LOW | **Layer:** L2 | **Stage:** CROSS-CUTTING

**What's missing:** The WoW produces many artifacts (golden datasets, architecture docs, runbooks, eval suites, skill files). But there is no standard for:
- Where documentation lives (repo? Confluence? Notion? Google Drive?)
- What format (Markdown? Word? Google Docs?)
- What constitutes "documented" vs. "mentioned in passing"
- Documentation review process (peer review of docs, not just code?)
- How stale documentation is identified and updated

**Granularity needed:** L2 section (documentation standards and storage locations).

---

### GAP-28: No Success Metrics for the WoW Itself
**Type:** MISSING | **Severity:** LOW | **Layer:** L1 | **Stage:** CROSS-CUTTING

**What's missing:** The WoW proposes a quarterly review but does not define what "success" of the WoW looks like. Metrics might include:
- Reduction in prototype-to-production time (target: 30% in two quarters)
- Increase in eval coverage (% of engagements with golden datasets)
- Reduction in L3 escalations post-handoff
- Revenue per resource trend
- Gate compliance rate (% of engagements passing through all required gates)
- Client satisfaction scores
- Time from requirement to first eval-passing prototype
- Number of components reused vs. built from scratch

Without these, the quarterly review has no data to work with and becomes a subjective discussion.

**Granularity needed:** L1 section (WoW success metrics with baselines and targets).

---

### GAP-29: No Environment Management Standard
**Type:** MISSING | **Severity:** LOW | **Layer:** L2 | **Stage:** Stages 3, 4

**What's missing:**
- What environments does the team need? (local dev, shared dev, staging, production, client sandbox)
- How are environments provisioned? (Self-serve? DevOps request? CTO office ticket?)
- How is parity between environments ensured? (The transcript specifically flagged: "testing works on my things but fails in production")
- How is environment configuration managed? (Environment variables, secrets, API keys)
- What is the sandbox environment the Engineer proposed and how does it work?

**Granularity needed:** L2 playbook (environment matrix, provisioning workflow, configuration management).

---

### GAP-30: No External Vendor / Tool Management
**Type:** MISSING | **Severity:** LOW | **Layer:** L1 | **Stage:** CROSS-CUTTING

**What's missing:** The team uses or considers using many external tools: Claude API, Cursor, Langfuse, Braintrust, Promptfoo, GitHub, AWS, n8n, Streamlit. But:
- Who decides which tools are adopted?
- What is the evaluation process for new tools?
- Who manages licenses and access?
- What happens when a tool is deprecated or changes pricing?
- How is tool usage tracked and justified (especially paid tools)?

**Granularity needed:** L1 section (tool governance policy), L3 template (tool evaluation criteria checklist).

---

## PART 6: DEPTH GAPS -- Where the Approach Mentions Something but Lacks Operational Specificity

These are areas where the proposed approach says the right words but does not go deep enough to be actionable.

| # | Topic | What's Said | What's Missing (the Operational "How") |
|---|-------|-------------|---------------------------------------|
| D1 | Eval infrastructure | "Build evaluation suite" | Who builds it? With what tooling? How is it maintained? What is the eval suite format? How are evals run (CLI? CI/CD? Dashboard?) |
| D2 | Canary deployment | "Small traffic %" | What percentage? How long before full rollout? Who monitors? What metrics gate promotion? How is traffic split technically? |
| D3 | Auto-rollback | "If any metric drops below threshold, auto-rollback" | What thresholds specifically? Per-engagement or standard? Who configures the rollback? What is the notification process? |
| D4 | Monitoring dashboards | "Monitoring dashboards live" at Deploy Gate | What tool? What metrics displayed? Who builds the dashboard? Who reviews it and how often? |
| D5 | "Weeks to independence" metric | Tracked at Handoff Gate | How is it measured? (Calendar weeks from handoff to zero L3 escalations? Or something else?) What is the target? |
| D6 | Pivot gates | "Does this still make sense?" | Who decides? What triggers a pivot? What data informs the decision? What happens to work already done? |
| D7 | Fallback paths | "If we're on our own" at every gate | Only one example is given (Deploy Gate). What are the fallbacks for Requirement Gate (no SME cooperation), Solution Gate (no engineering input), Build Gate (no engineer for review)? |
| D8 | Skills inventory | "What existing skills apply?" at Stage 2 | Where is the skills catalog? How is it kept current? What metadata does it contain? |
| D9 | Cross-functional workshop | "GenAI team + engineering rep minimum" | How do you get the engineering rep to show up? What is the engagement protocol? What if they refuse? |
| D10 | Client sign-off on rubric | "Client signs off on the rubric, not the prompt" | How is this explained to clients who are used to signing off on outputs? What if the client insists on approving prompts? What format is the rubric sign-off in? |

---

## PART 7: SYNTHESIS -- Priority Order for Addressing Gaps

### Must be in Version 1 of the WoW (before MedCom pilot):
1. **GAP-04: Client Interaction Model** -- Cannot run a pilot without knowing how to interact with the client.
2. **GAP-08: Branch Strategy / Code Contribution Workflow** -- Cannot have everyone coding without this.
3. **GAP-15: Engagement Typing** -- The MedCom pilot needs to know which gates apply at what depth.
4. **GAP-06: Golden Dataset Operationalization** -- Stage 1 of MedCom cannot start without knowing how to actually create the dataset.
5. **GAP-02: Incident Response Protocol** -- Even a pilot will have production issues.
6. **GAP-16: Solutioning Workshop Protocol** -- Stage 2 of MedCom needs a facilitation guide.

### Must be in Version 2 (during or immediately after pilot):
7. **GAP-03: Financial Tracking** -- Pilot costs must be tracked to present to the VP.
8. **GAP-05: Stakeholder Engagement Map** -- Needed before scaling beyond MedCom.
9. **GAP-09: Quality Measurement Framework** -- Needed to prove the WoW works.
10. **GAP-10: Capacity Planning** -- Needed when second engagement starts in parallel.
11. **GAP-12: Scope Change Process** -- Will be needed as MedCom requirements evolve.
12. **GAP-07: Knowledge Management** -- Should start capturing from pilot Day 1.
13. **GAP-17: Handoff Package Specification** -- Needed before MedCom moves to Stage 5.

### Must be in Version 3 (before broader rollout):
14. **GAP-01: Onboarding Playbook** -- Critical when WoW goes beyond the core team.
15. **GAP-11: Retrospective Process** -- Needed to improve the WoW from pilot learnings.
16. **GAP-13: Risk Management** -- Needed for multi-engagement governance.
17. **GAP-18: Prompt/Skill Versioning Standard** -- Needed before the component library grows.
18. **GAP-19: IP Protection** -- Needed before deploying in client environments at scale.
19. **GAP-22: Component Library Governance** -- Needed to make reuse work.
20. **GAP-20: Experimentation Process** -- Needed to formalize the innovation sprint model.

### Can be added incrementally:
21-30. All remaining gaps (culture norms, documentation standards, WoW success metrics, environment management, vendor management, depth gaps D1-D10, model version management, auto-refinement standards, cross-engagement consistency, upskilling integration).

---

## PART 8: STRUCTURAL RECOMMENDATIONS

### Recommendation 1: Add a "Stage 0: Intake & Classification" Before Stage 1
The current Stage 1 (Requirement & Scoping) assumes you already know what type of engagement you are dealing with. Add a lightweight intake step that classifies the engagement type, determines which stages/gates apply, and assigns a Single-Threaded Owner.

### Recommendation 2: Add Cross-Cutting Sections to Layer 1
The current Layer 1 is linear (5 stages). Many gaps are cross-cutting: they apply to all stages, not any one stage. The Layer 1 document needs cross-cutting sections for:
- Communication cadence and reporting
- Financial governance
- Risk management
- Knowledge management
- Quality management
- Stakeholder engagement

### Recommendation 3: Layer 3 Needs a Template Index
The proposed approach lists templates implicitly (golden dataset template, solutioning workshop template, handoff package template). Create an explicit template index that maps every gate requirement to a specific template with a fill-in guide.

### Recommendation 4: Add a "Day-1 Survival Guide" as a Layer 2 Playbook
Separate from the onboarding checklist (L3), create a narrative playbook that answers: "I just joined this team. What do I need to know to be useful within a week?"

### Recommendation 5: Build the WoW as a Living Repository, Not a Document
Given the 3-layer design with swappable playbooks and versioned templates, the WoW should be a structured repository (e.g., a git repo or a well-organized folder system) rather than a single Markdown file or Word document. This makes modular updates possible without version control nightmares.

---

*Gap analysis generated 8 April 2026. Based on: 2 days of team discussion transcripts, The Senior Manager's 10-theme asset, The Engineer's engineering strategy, The Director's original brief, The Director's 8 April call, and the proposed 3-layer/5-stage approach.*

---

## PART 9: GAP CLOSURE TRACKER 

This section tracks which original gaps have been addressed by the v2 granular documents.

### CLOSED Gaps (Fully Addressed)

| Gap | Title | Addressed By | How |
|-----|-------|-------------|-----|
| GAP-01 | Onboarding Playbook | Cross-Cutting Ops v2, §3.3 | Full Week 1/2/Month 1 schedule, access provisioning checklist, buddy system, success criteria |
| GAP-02 | Incident Response Protocol | Build/Test/Deploy v2, §4.3 | SEV-1 through SEV-4 definitions, business-hours-first response model, full detection→triage→fix→postmortem flow |
| GAP-04 | Client Interaction Model | Solutioning v2, §1.1-1.2 + §5 | Step-by-step discovery, client communication rules, scope change process, expectation-setting scripts, weekly status template |
| GAP-06 | Golden Dataset Operationalization | Eval Dataset v2, §1.1-1.6 + §7 | Full creation process with CSR S11 worked example, JSON schema, time estimates, bootstrapping guide for first-ever dataset |
| GAP-08 | Branch Strategy / Code Contribution | Build/Test/Deploy v2, §1 | Trunk-based with feature branches, CODEOWNERS, PR template, git essentials for non-engineers, conflict resolution |
| GAP-09 | Quality Definition & Measurement | Eval Dataset v2 (scoring dimensions per product) + Cross-Cutting Ops v2, §7 (quality culture mechanisms) | Per-product scoring rubrics, production monitoring metrics, weekly quality reports, quality culture principles with enforcement |
| GAP-11 | Retrospective Process | Cross-Cutting Ops v2, §2.1 (sprint structure) | Sprint retro every 2 weeks, quarterly WoW retro, post-engagement retrospective format |
| GAP-13 | Risk Management Framework | Cross-Cutting Ops v2, §6 | Risk register template with 13 risks, escalation thresholds, pharma-specific risks (audit, data privacy), audit preparedness |
| GAP-14 | Communication Cadence | Cross-Cutting Ops v2, §1 | Full meeting cadence table, async vs sync framework, escalation paths L1-L5, decision documentation template |
| GAP-15 | Engagement Typing / Intake | Solutioning v2, §1.5 + the Proposed Approach (Stage 0) | 6 engagement types (A-F) with stage applicability matrix |
| GAP-16 | Solutioning Workshop Protocol | Solutioning v2, §2 | Pre-workshop prep, 3 agenda variants (3hr/1.5hr/1hr), complexity ladder with worked examples, output template |
| GAP-17 | Handoff Package Specification | the Proposed Approach + Build/Test/Deploy v2, §3.3 (rollback as part of handoff) | Artifact table with contents and acceptance criteria, runbook depth defined, training requirements |
| GAP-18 | Prompt/Skill Versioning Standard | Skills/KB v2, §1.5 + §6 | Semantic versioning, naming conventions, repository layout, promotion workflow, metadata requirements |
| GAP-20 | Experimentation / Innovation Process | Cross-Cutting Ops v2, §4 + Solutioning v2, §4 | POC process with time-box, success criteria, experiment brief template, preventing POC-to-production pattern |
| GAP-22 | Component Library Governance | Skills/KB v2, §4 | Catalog structure with auto-generated index, metadata per skill, quality bar for library inclusion, fork vs parameterize |
| GAP-23 | Auto-Refinement Process Standard | Skills/KB v2, §1.7 + Eval Dataset v2, §5.2 | Max sessions per sprint, cost caps, cooldown periods, governance table for disagreements, human review of all changes |
| GAP-26 | Team Culture / Working Norms | Cross-Cutting Ops v2, §7 + §1.2 | Quality culture principles, remote/hybrid protocol, disagreement resolution |
| GAP-27 | Documentation Standards | Skills/KB v2, §6 (naming conventions, repo layout) + Cross-Cutting Ops v2, §3.1 (where knowledge lives) | Repository structure, documentation locations table, format standards |

### PARTIALLY CLOSED Gaps (Addressed But With Remaining Items)

| Gap | Title | What's Addressed | What Remains |
|-----|-------|-----------------|-------------|
| GAP-03 | Financial Tracking / Cost Governance | Build/Test/Deploy v2, §5: per-project tracking, budget thresholds, optimization levers, reporting template | Missing: integration with Indegene's finance systems, billable vs non-billable allocation, formal budget approval workflow with the VP |
| GAP-05 | Stakeholder Engagement Map | Cross-Cutting Ops v2, §5: per-stakeholder engagement model, CTO office relationship protocol, the MWA track lead track coordination | Missing: formal MoU or SLA template with CTO office (requires the VP); engagement model for new stakeholder groups that emerge |
| GAP-07 | Knowledge Management System | Cross-Cutting Ops v2, §3: documentation locations, tech talks, cross-review, onboarding | Missing: tooling decision (Confluence vs Notion vs git-only); search/discovery mechanism for growing knowledge base; formal knowledge audit process |
| GAP-10 | Capacity Planning | Cross-Cutting Ops v2, §4: time allocation phased plan, protecting build time, handling unplanned work | Missing: formal capacity tracker tool; per-person allocation visibility; process for when team is at capacity and new work arrives |
| GAP-12 | Scope Change Process | Solutioning v2, §5.3 + §5.5: client scope change + internal scope change processes | Missing: quantified cost-of-change formula; escalation to the VP when scope change exceeds budget threshold |
| GAP-19 | IP Protection & Data Security | Eval Dataset v2, §8.2 (data privacy) + Build/Test/Deploy v2, §5 (security) + Cross-Cutting Ops v2, §6.4 (data privacy guardrails) | Missing: formal IP classification policy document; legal review of skill/KB ownership when built for specific clients; client contract template language |
| GAP-21 | Upskilling Integration | Cross-Cutting Ops v2, §3.4 (external learning) + Eval Dataset v2, §7 (bootstrapping) | Missing: formal skill matrix per role; individual development plans; formal bootcamp scheduling against delivery calendar |
| GAP-24 | Cross-Engagement Consistency | Skills/KB v2, §6 (naming conventions, repo layout) + the Proposed Approach (unified RACI) | Missing: style guide enforcement mechanism; automated consistency checks across engagements |
| GAP-25 | Model Version Management | Build/Test/Deploy v2, §3.4 (model pinning + upgrade process) | Missing: multi-model routing logic documentation; fallback model eval validation process |

### OPEN Gaps (Require External Decisions)

| Gap | Title | Why Still Open | What Would Close It |
|-----|-------|---------------|-------------------|
| GAP-28 | WoW Success Metrics | Partially addressed in the Proposed Approach (8 metrics added). But baselines don't exist yet — need MedCom pilot data | Run MedCom pilot through Stages 1-3, measure baseline, then set targets |
| GAP-29 | Environment Management Standard | Build/Test/Deploy v2 covers environment parity but actual provisioning depends on DevOps resource | DevOps resource decision from the VP; or self-serve AWS access for the team |
| GAP-30 | External Vendor/Tool Management | Not addressed — tool decisions (Langfuse vs Braintrust, GitHub tier, monitoring stack) are parked pending framework decision | Framework evaluation sprint completes; team standardizes on toolset |

### Structural Recommendations — Implementation Status

| Recommendation | Status | Where Implemented |
|---------------|--------|------------------|
| Add Stage 0: Intake & Classification | **DONE** | the Proposed Approach + Solutioning v2, §1.5 |
| Add cross-cutting sections to Layer 1 | **DONE** | Cross-Cutting Ops v2 (full document) |
| Create explicit template index | **DONE** | the Proposed Approach (template index table) |
| Day-1 Survival Guide | **DONE** | Cross-Cutting Ops v2, §3.3 (Onboarding Guide) |
| Build WoW as living repository | **DONE** | Skills/KB v2, §6 (repository layout) applies to skills; WoW docs themselves follow same structure |

---

## PART 10: NEW GAPS DISCOVERED IN v2 REVIEWS

### GAP-31: Pharma Regulatory Compliance Not Centralized
**Type:** IMPLICIT | **Severity:** HIGH | **Layer:** L1 | **Stage:** CROSS-CUTTING

Pharma compliance requirements (audit trails, GxP, 21 CFR Part 11, data privacy) are now addressed but spread across 3 documents: Eval Dataset v2 §8, Build/Test/Deploy v2 §5, Cross-Cutting Ops v2 §6.3-6.5. For an external auditor, there should be a single compliance section or at minimum a cross-reference map that says "here is everything related to regulatory compliance."

**Action:** Add a compliance cross-reference table to the Proposed Approach as a central index.

### GAP-32: MedCom Pilot Specifics Scattered
**Type:** SHALLOW | **Severity:** MEDIUM | **Layer:** L1 | **Stage:** CROSS-CUTTING

MedCom pilot-specific guidance is now in Solutioning v2 §1.6, Eval Dataset v2 §6, Skills/KB v2 §5.5. There is no single "MedCom Pilot Playbook" that a team member can read to understand the full pilot plan. This was by design (the WoW is product-agnostic) but creates a practical problem for the first implementation.

**Action:** Consider creating a lightweight MedCom Pilot Quick-Start guide that links to the relevant sections across all documents. Not a new WoW layer — just a navigation document.

### GAP-33: No Process for WoW Adoption Itself
**Type:** MISSING | **Severity:** MEDIUM | **Layer:** L1 | **Stage:** CROSS-CUTTING

The WoW describes how the team should work, but there is no process for how the team adopts the WoW. Specifically:
- How do you introduce 3,800+ lines of process to a 10-person team without overwhelming them?
- What is the minimum viable subset to start with?
- How do you handle the transition period where some work follows old patterns and some follows the WoW?
- Who enforces WoW compliance and how?

**Action:** Add a "WoW Adoption Guide" to the Proposed Approach — a phased rollout where the team adopts one layer at a time.

### GAP-34: No Guidance for When the WoW Doesn't Fit
**Type:** MISSING | **Severity:** LOW | **Layer:** L1 | **Stage:** CROSS-CUTTING

Every process has exceptions. The WoW does not address what happens when a specific engagement genuinely cannot follow the defined process (e.g., emergency client request with 48-hour deadline, leadership directive to skip gates, client refuses rubric sign-off).

**Action:** Add an "Exception Process" to the Proposed Approach — how to document and approve exceptions without undermining the entire process.

### GAP-35: Inter-Document Version Alignment
**Type:** IMPLICIT | **Severity:** LOW | **Layer:** Meta | **Stage:** N/A

With 8 documents that cross-reference each other, there is a risk of version drift — one document gets updated but its cross-references in other documents become stale. No mechanism exists to check cross-document consistency.

**Action:** Add a version alignment check to the quarterly WoW retrospective. Alternatively, maintain a master cross-reference index that is updated when any document changes.

---

*v2 gap analysis updated 8 April 2026. Reflects closure status based on: the Proposed Approach, Eval Dataset Lifecycle v2, Skills/KB Lifecycle v2, Build/Test/Deploy v2, Cross-Cutting Operations v2, and Solutioning/Requirements v2.*
