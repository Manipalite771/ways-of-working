# 9 April 2026 Workshop Transcript Analysis

> **Note:** Due to audio recording limitations (microphones were only on for a few participants), speaker attributions in the original transcript may be inaccurate. This analysis therefore omits person-specific attributions and uses role-based references throughout.

---

## OUTPUT 1: COMPLETE EXTRACTION OF KEY DETAILS

---

### TOPIC 1: TEAM CREDIBILITY AND ORGANIZATIONAL POSITIONING (Part 1, 0:00 - 2:33)

**What was discussed:**
The session opened with a frank assessment that the GenAI team has "lost credibility" within the organization. Three interlinked problems were identified:

1. **Trust deficit**: "I don't think right now anybody is willing to trust saying that you guys will build it out yourself." Nobody in the broader org believes the GenAI team can independently build and ship products.

2. **Role ambiguity**: There is ongoing confusion about roles and responsibilities across the organization -- "everybody is figuring out what the roles and responsibilities are going to be."

3. **Platform ownership conflicts**: Multiple people/teams are working on overlapping areas, making parallel work difficult:
   - **Medical Writing Platform (MWP)**: Another team member is working on it. Doing anything in parallel is "not great." This had been flagged previously, asking what the GenAI team's role would be.
   - **MLR**: Engineering is looking into it independently. "Even there, doing something is going to be a little hard."
   - **SAA**: This is the one area where "there's still a lot of appetite." SAA has "complete control" with the GenAI team "for now." It was proposed to use SAA as a pilot to demonstrate capability. However, senior leadership was exploring whether they could get "one or two good guys" from engineering to partner with.

**What was decided:**
- SAA should be taken as a pilot project to prove the team can deliver.
- The team needs to produce strong artifacts (agentic framework recommendation, scalability benchmarks, Ways of Working) to share with the broader org and regain credibility.
- "Whatever we align on is what we will build. There is no going back from it."

**What was left open:**
- Whether senior leadership will get engineering resources to partner with the GenAI team on SAA.
- The exact mechanism for reclaiming ownership or influence on MWP and MLR.

---

### TOPIC 2: STRATEGIC PRIORITIES AND IMMEDIATE NEXT STEPS (Part 1, 2:33 - 7:34)

**What was discussed:**
The key workstreams the team must address were laid out, acknowledging that the past few days had been disruptive (team members were occupied with MLR and interviews):

1. **Agentic Framework Selection**: Must decide which framework to standardize on. Needs "really strong points and proof points." "Whatever we align on is what we will build."

2. **Scalability**: Called "very important" and "core of the platform." It was noted that Vertex had asked whether users had been consulted on acceptable wait times -- they had not. "There has not been a single client that's been okay with anything more than 5 minutes." The team needs to "recalibrate how we think about it."

3. **Ways of Working**: Must set the process down formally.

4. **Competitive Differentiation / Quantitative Metrics**: A gap was identified -- "We say that our platform is good, but we don't have anything else to say other than the fact that yes, we have tested. Do we have quantitative metrics? No." Comparison data showing where the platform outperforms competitors is needed.

5. **Document Repository / Eval Datasets**: The document repository work is "going to be very important" for creating eval datasets and measurement parameters.

6. **Work-from-Home Policy Change**: WFH exceptions are being cut. The team currently operates mostly on WFH exceptions. Individual discussions will happen in one-on-ones.

**Concerns raised:**
- Team members have been stretched thin on MLR and interviews.
- No quantitative metrics exist to demonstrate platform superiority.
- No user research on acceptable wait times has been done.
- 5-minute threshold is a hard line -- no client has accepted more than 5 minutes.

---

### TOPIC 3: AGENTIC FRAMEWORK EVALUATION (Part 2, 0:00 - 36:42)

Three frameworks were evaluated by different team members.

#### 3A: Claude Agent SDK

**What was tested:** Built a content outline agent. Took approximately 30 minutes to build.

**Findings:**
- **Model lock-in**: Can only use Anthropic models natively. Could not select different models. "From a scalability perspective... if I want to use image generation, I wouldn't use anthropic models."
- **Time**: Content outline agent took 30 minutes to run (though it was noted this is likely implementation-dependent, not framework-inherent).
- **Built-in capabilities**: Tool calling is extensive and comes as part of the SDK. Automatic retries are built in at the API level. Can detect duplicate tool calls.
- **Sandbox**: Has a native sandbox environment where tool results can be filtered before sending back to the LLM. This is a significant advantage.
- **Error recovery**: Described as "clearly better" than Strands for real-time error recovery -- uninterrupted sessions, right tool calls, logged operations at runtime.
- **Auditability concern**: Auditing which approach the agent took and why is "very complex" in Claude Agent SDK because it uses a hooks approach.

**Concerns:**
- Anthropic recently announced restrictions on using Claude models in third-party platforms, including open-source ones.
- Not model-agnostic. This is a risk for enterprise use.
- Image generation quality from Anthropic is poor compared to Gemini.

#### 3B: Strands (AWS)

**What was tested:**
- An MLR/ISI pipeline was built using Strands.
- A full content authoring pipeline was built on Strands including: parsing agent, planning agent, authoring agent, QA agent, and export agent. Also connected to PostgreSQL and integrated MCP.

**Findings:**
- **Model agnostic**: Can connect via Bedrock or Foundry to use any model.
- **Tool creation**: Tools must be built manually. No native sandbox -- all tool output goes back to the LLM.
- **Agent-to-agent handoff**: Different from Claude's parent-child model. Has "swarm" and "graph" patterns.
- **AWS integration**: Observability, evaluation framework, auto-scaling all come from AWS infrastructure.
- **Skills**: Prompts-based, not .md skill files natively. But skills concept is supported via "agent skills plugin."
- **Cloud Code integration**: Claude Agent SDK can be wrapped as a custom tool inside Strands.
- **Scalability**: AWS backing means provisioned throughput, server control, ability to scale.
- **Production readiness concern**: "Not heard a single person use it except for Indegene." No community evidence. No YouTube content beyond AWS's own marketing.
- **Content authoring results**: ~60% matched current database structure. Used Opus 4.6. Connected to PostgreSQL. MCP integration worked. Full end-to-end authoring with QA report. Helion CSR generated in ~15 minutes including parsing.

#### 3C: LangGraph

**What was tested:** Ran the MedCom asset pipeline with orchestrator, QC quality check, and retry mechanism.

**Findings:**
- **Speed**: Generated one asset end-to-end in 18 minutes vs. 30 minutes on current platform (35-40% faster).
- **Retry mechanism**: LLM-driven. If tool fails 3 times, on 4th attempt creates new tool.
- **Model agnostic**: Can hook multiple models.
- **Manual orchestration**: Like Strands, retries must be manually defined.

#### 3D: Architectural Insight on Framework Layers

**Key point raised:** Claude Code should NOT be compared at the same level as Strands, LangGraph, CrewAI, or Google ADK. "Cloud code is a layer below than these." The comparison should be between orchestration frameworks, and Claude Code should be used as an agent within whichever orchestration framework is chosen.

- Recommended: debate should be between ADK, CrewAI, LangGraph, Strands.
- CrewAI vs Strands is the most relevant comparison.
- For MedCom specifically, Claude Code as an agent is strong due to runtime code modification capabilities.

**Concerns raised against Claude Agent SDK as orchestrator:**
1. More token-consuming
2. Advised to run only in sandboxed/contained environments
3. Less control: "We mention which tool NOT to use" vs Strands where "we say which tool to use"
4. Better enterprise control in Strands
5. In Claude Code, you rely too much on the framework

#### Framework Decision:

**Summary:** "We broadly feel Strands might be better suited for enterprise use. Claude has certain advantages, but it still might not work out."

**Decision:** PAUSE framework evaluation pending CTO office discussion. Reasoning:
- NWA (another product) is being built on Strands
- MLR side also using Strands
- Indegene is an "AWS shop" with possible financial incentives
- The team's evaluation was "super unstructured"
- "Let me have a discussion to figure out where the org is heading."

---

### TOPIC 4: SCALABILITY BENCHMARKING (Part 2, 49:14 - 1:13:41)

Comparative benchmarks of the Indegene platform vs. competitors (Cowork/CoPilot, OpenAI, Canva) were presented across multiple products.

#### MedCom / Slide Generation:
| Parameter | Competitors | Indegene |
|-----------|------------|----------|
| Time (20 slides) | 8-15 min | ~30 min |
| Slide quality (life sciences) | 80-85% (claimed) | Higher (team consensus) |
| Concurrent users | Unknown (enterprise) | 13 projects/9 users tested successfully |
| Max input | ~400 pages (estimated) | 1000-1500 pages; tested up to 70 source files |
| Cost per deck | Cowork: $0.50-$3; Canva: $0.05 | Comparable to Cowork |

#### Content Authoring (CSR):
- Time: 300-400 minutes for Indegene vs. lower for competitors
- Concurrent users is a major issue: as load increases, speed decreases
- 32 CSR runs were tested overnight on Dev -- completed within one hour

#### MLR:
- Time: 20-40 minutes with new pipeline vs. less than 10 minutes for competitors
- Asset recovery: Indegene can only do 4 concurrent checks for one user
- Competitors claim 15-20 minutes for all checks combined
- A competitor does all checks in 15-20 minutes

#### Cross-cutting Scalability Observations:

**Additional parameters identified as missing from the benchmarks:**
- Time to onboard a document / template / client
- Deployment time
- Error rate

**User behavior insights:**
- "There has not been a single client okay with anything more than 5 minutes."
- Users stay engaged if something is appearing on screen (partial results).
- Proposed: show partial results; let users start reviewing while pipeline completes.
- Proposed: color-coding confidence levels (green = don't review, yellow = review needed).
- A similar approach was used in patient narratives -- highlighted in yellow.

**Three scalability measurement dimensions:** Time, Rework, and Engagement.

**Prerequisites per platform:**
- MedCom: Without templates, nothing works (currently 1-2 days to create).
- MLR: Without bounding box visualization, review is unusable.

**Competitor access:** The commercial team was given access to competitor platforms to run comparative tests as of April 9.

---

### TOPIC 5: USER-CENTRIC DESIGN (Part 2, ~1:05 - 1:10)

- The team is "not helping users change their behavior."
- Users will resist AI replacing their work -- "They will try and look for issues only."
- Proposed "SME-facing agent" concept (ego massaging) -- agent validates user's expertise.
- Must find cooperative SMEs. Some will "guide you in the wrong way."
- **Requirements discussion is very important and has not been happening.**

---

### TOPIC 6: WAYS OF WORKING PORTAL WALKTHROUGH (Part 2, ~1:15:54 - 1:52)

#### Time Allocation (CRITICAL CHANGE):
- Current portal: 60-30-10 (Delivery-Building-Learning)
- **Decision: Reverse to approximately 20-60-10 or 20-70-10 (Delivery-Building-Learning).**
- "Delivery cannot be at 60% and we will not basically build a good product."
- Startup companies can move faster. "First person is going to get business basically."
- It was acknowledged that resource constraints have never been escalated to senior leadership. This now needs to change -- the team must start pushing back.

#### Product vs. Service Debate:
- A concern was raised: Features should come from Indegene's vision, not just client demands. Roadmap should not shift per client.
- Clarification: "We are only doing product. We are not doing the service thing." Service delivery is for service teams.
- But reality: team gets pulled into delivery.
- Sales halt is "on paper already being discussed."
- **Resolution:** "Client" includes internal SMEs. Validate with SMEs before building, not after.

#### Build, Test, Deploy Discussion:

**Git/PR Process:**
- Non-engineers should learn Git.
- Who-can-do-what matrix: Feature branch (all), modify skill files (all), infra configs (engineer only), approve PRs to main (engineer only).
- PR template: type of change, eval scores, comments, testing done, checklist.
- Never commit API keys. Never use `git push --force`.

**Sandbox Environment:**
- A sandbox for per-branch testing before Dev was requested.
- **Decision:** Create additional sandbox instance. Rationale: if two engineers work on features X and Y for the same product, they need to test independently before merging to Dev. Local testing doesn't catch front-end dependencies or infra behavior.

**CI/CD:**
- AWS CodeBuild may not support LLM-as-Judge.
- Alternatives: Jenkins, GitLab pipelines.
- MWP team already moved to GitLab.
- **Left open:** Need DevOps consultation.

**Testing 3 Tiers:**
- Tier 1: Automated code checks (syntax, secrets, schema validation).
- Tier 2: LLM-as-Judge (Sonnet/Haiku, 5-10 min limit, cost-effective).
- Tier 3: Human review (QC/SME team, periodic).

**Eval Datasets:**
- Rubric is the PRIMARY artifact to create first.
- Rubrics don't exist for many areas -- major gap.
- Manual scoring needed before calibrating LLM-as-Judge.
- Synthetic data: avoid for now; use real documents.
- Document repository must connect to SharePoint.
- Client-specific vs. universal datasets.

**Process Consolidation Request:**
- Convert WoW into a simple process chart / diagram.
- Ideally codify as an executable command/workflow.
- Concern that most team members won't review the portal in its current long-form format.

---

### TOPIC 7: KNOWLEDGE MANAGEMENT (Part 2, ~1:43-1:46)

- Knowledge management must be part of the WoW. The team is "running everywhere" because only a few people know what's happening behind the scenes.
- Stop "spoon-feeding" new joiners. Self-service model. Use Cursor to explore codebases, come back with questions.
- Generate flowcharts from codebases as standard practice.
- Not just engineering onboarding -- also for prompting/solution architect roles.
- Two dimensions: textual knowledge (Confluence/Wiki) and code knowledge (common code base as starting point).

---

### TOPIC 8: UPSKILLING AS PREREQUISITE (Part 2, ~1:52-1:53)

- "The first thing is the last tab -- upskilling. That is the truth."
- "There's a skills gap. I know that for a fact."
- Upskilling is the real first priority before any process can work.

---

### TOPIC 9: PROCESS RISKS AND AUTOMATION (Part 2, ~1:53-1:55)

- When strict processes meet urgent needs, what happens?
- Real example: an engineer mediating prompt uploads got frustrated and gave direct access. This broke process but sped up iteration.
- **Solution:** Automate more. "We are only using GenAI in our products, let's start using it in our ways of working also."

---

### TOPIC 10: TEAM MORALE AND CELEBRATIONS (Part 2, ~1:55-1:59)

- Team events/celebrations were raised as important for morale.
- Budget constraints: ~1,500 per person, distributed team makes in-person gatherings difficult.
- "I don't think we celebrate our wins. We should also celebrate failures."
- Will be raised in skip-level meeting with senior leadership.

---

### TOPIC 11: AGENT vs. NON-AGENT DECISION (Part 2, ~1:12-1:13)

- PR analysis was run agentic when simpler approach would have worked.
- Team should maintain a decision table: agent vs. not-agent, pros and cons.
- Consult it before every new build.
- Same applies to model selection -- which model to use depends on the use case.

---

## OUTPUT 2: ITEMS THAT IMPACT THE CURRENT WoW PORTAL

---

### CRITICAL IMPACTS

| # | Impact | Portal Document | What Needs to Change | Type |
|---|--------|----------------|---------------------|------|
| 1 | **Time Allocation Ratio** | Cross-Cutting Operations | Change from 60-30-10 to **20-60-10** (Delivery-Building-Learning) | Content change |
| 2 | **Agentic Framework Guidance** | Build/Test/Deploy + new Technical Playbook | Add framework evaluation section, layer distinction (orchestration vs agent), interim findings on Strands vs Claude vs LangGraph | New addition |
| 3 | **Scalability as Core Requirement** | Solutioning & Requirements; Master Framework | Add mandatory scalability parameters to requirements checklist; "5-minute rule"; three dimensions (Time, Rework, Engagement); define before solutioning | Content + structural change |
| 4 | **User-Centric Design Requirements** | Solutioning & Requirements | Add partial results display, confidence color-coding, SME behavioral considerations, "trailer approach", user interviews as requirement | New addition |

### IMPORTANT IMPACTS

| # | Impact | Portal Document | What Needs to Change | Type |
|---|--------|----------------|---------------------|------|
| 5 | **Sandbox Deployment Environment** | Build/Test/Deploy | Add sandbox/feature-testing environment for per-branch testing before Dev | Structural change |
| 6 | **CI/CD Pipeline -- DevOps Alignment** | Build/Test/Deploy | Acknowledge GitHub-to-GitLab migration possibility; AWS CodeBuild limitations for LLM-as-Judge; Jenkins/GitLab alternatives | Content change |
| 7 | **Agent vs Non-Agent Decision Framework** | Solutioning & Requirements or Skills/KB | Add decision table/checklist for when to use agentic vs simpler approach; include model selection guidance | New addition |
| 8 | **Competitive Benchmarking** | Eval Dataset Lifecycle; Cross-Cutting Operations | Add ongoing competitive benchmarking practice with quantitative metrics | New addition |
| 9 | **Rubric as Primary Artifact** | Eval Dataset Lifecycle | Elevate rubric creation to FIRST step; note rubrics missing for many areas; add LLM-as-Judge failure modes; avoid synthetic data | Content change |
| 10 | **Knowledge Management & Onboarding** | Cross-Cutting Operations or Upskilling | Add self-service model; Cursor-based exploration; flowchart generation; non-engineering onboarding | New addition |
| 11 | **Product vs Service Positioning** | Executive Summary or Master Framework | Add explicit statement: team builds PRODUCTS; service delivery is for service teams; roadmap stability | Content change |
| 12 | **Upskilling as Prerequisite** | Upskilling Plan | Position as gating requirement, not aspiration; acknowledge skills gap; add "using GenAI in WoW" as upskilling goal | Content change |

### NICE-TO-HAVE IMPACTS

| # | Impact | Portal Document | What Needs to Change | Type |
|---|--------|----------------|---------------------|------|
| 13 | **Process Consolidation Format** | Portal structure | Create single-page process chart or executable workflow; supplementary to existing portal | Structural change |
| 14 | **Celebration & Team Morale** | Cross-Cutting Operations | Make celebrations section actionable, not aspirational; add budget/distributed team considerations | Content change |
| 15 | **Skills File Portability** | Skills & KB Lifecycle | Emphasize .md files are fungible across frameworks as design principle | Content change |

---

## OUTPUT 3: NEXT STEPS AND ACTION ITEMS

---

### IMMEDIATE

| # | Action | Dependencies | Notes |
|---|--------|-------------|-------|
| 1 | **CTO Office Discussion on Framework Direction** | None | Blocks framework decision for entire team. "Let me have a discussion with the CTO office." |
| 2 | **Circulate Next Steps Document** | Workshop done | With assigned owners, within 1-2 days post-workshop. |

### HIGH PRIORITY

| # | Action | Dependencies | Notes |
|---|--------|-------------|-------|
| 3 | **Prepare Proper Agentic Framework Evaluation** | CTO discussion outcome (#1) | Only if CTO has NOT made directional call. Must be structured with evidence, not "a chat on a lunch table." |
| 4 | **Competitor Platform Testing** | Commercial team access active | Run same assets through competitor tools. In progress as of April 9. |
| 5 | **Share Strands CSR Output for Quality Review** | None | Helion CSR generated on Strands in ~15 min. Quality review needed. |
| 6 | **Complete Scalability Benchmarks** | Competitor data (#4) | Fill missing params, add Gamma, add prerequisites per platform, structure around Time/Rework/Engagement. |
| 7 | **Consolidate WoW into Implementable Process** | None | Process diagram, checklists, ideally executable workflow. |
| 8 | **Define Eval Datasets Per Product** | Pilot product choice | For each product: sample set, asset variety, scoring rubric, universal vs client-specific. |

### MEDIUM PRIORITY

| # | Action | Dependencies | Notes |
|---|--------|-------------|-------|
| 9 | **Document Repository Update & SharePoint Connection** | SharePoint access | Enable agent to pull relevant docs based on eval criteria. |
| 10 | **DevOps Consultation on CI/CD** | None | CodeBuild limitations, Jenkins/GitLab options, sandbox provisioning. |
| 11 | **Create Sandbox Deployment Environment** | DevOps consultation (#10) | Per-branch testing before Dev. |
| 12 | **Build Agent vs Non-Agent Decision Table** | None | Consult before every new build. |
| 13 | **Explore Template Creation Agent** | Framework decision | Currently 1-2 days to create MedCom template manually. |
| 14 | **Deeper Dive on Strands Content Authoring Implementation** | None | Technical walkthrough was cut short due to time. Good for team knowledge sharing. |
| 15 | **WFH Policy 1:1 Discussions** | None | WFH exceptions being reduced. |
| 16 | **SAA Pilot Planning** | CTO direction, framework decision | Develop plan including framework, scalability, requirements, eval datasets, timeline. |
| 17 | **Review WoW Portal Offline** | Portal link shared | Concern that most team members won't actually do this. |

### LOW PRIORITY

| # | Action | Dependencies | Notes |
|---|--------|-------------|-------|
| 18 | **Team Celebration Initiative** | Budget approval | Will be raised in skip-level meeting with senior leadership. |

### IMPLICIT ACTION ITEMS (Not explicitly assigned but clearly needed)

| # | Action | Notes |
|---|--------|-------|
| IA-1 | Investigate MCP suitability for long-running agent tasks | Flagged as open question during framework discussion |
| IA-2 | Research Strands production usage evidence | Currently zero evidence outside AWS marketing |
| IA-3 | Design partial-results UX pattern for long pipelines | Show results incrementally |
| IA-4 | Design confidence color-coding system for AI outputs | Green = verified, yellow = review |
| IA-5 | Conduct user interviews / find cooperative SMEs | For requirements validation |
| IA-6 | Establish quantitative metrics for platform quality | Currently no data backing "our platform is good" |
| IA-7 | Add Python syntax validation & secrets-checking libs to automated testing | Suggested during build/test discussion |
| IA-8 | Escalate resource constraints to senior leadership | Acknowledged as never done before, now recognized as necessary |
