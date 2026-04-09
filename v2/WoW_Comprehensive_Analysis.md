# GenAI Team Ways of Working -- Comprehensive Analysis


## 1. Executive Summary

Across two days of in-person discussions (1-2 April 2026), the GenAI team at Indegene conducted an intensive strategy and ways-of-working exercise. The sessions were led by the Director with full participation from the team.

**Day 1** focused on context-setting and a demo. The Director laid out the current crisis: client pushback from Vertex and AZ, engineering team friction, the team being 6-7 months behind state-of-art in agentic AI, and a perception internally that the team can only build prototypes but cannot scale. He then demonstrated a Claude Agent SDK-based platform he had built as a proof of concept -- a skill-driven, single-platform system for medical writing automation with dynamic orchestration, auto-refinement, knowledge bases, and error recoverability. The team asked questions, surfaced concerns about scalability from local to production, and documented key themes for Day 2 research.

**Day 2** opened with the Director proposing a North Star: build a unified AI platform for life sciences -- analogous to Claude Cowork or OpenClaw -- that uses skills, tools, and evaluation datasets as the fundamental building blocks. The team debated vigorously on whether to build their own platform vs. build skills for existing platforms (Claude Cowork), on the timeline for enterprise adoption of such tools in pharma, and on what would truly differentiate the team. The discussions converged on: (1) skills, tools, and evals as the immediate focus; (2) a lightweight harness or Claude Cowork for testing/demo; (3) a 2-3 week proof-point timeline; (4) a unified process document to govern requirements, solutioning, build, test, and deployment.

Two prep documents were also contributed: The Senior Manager's preparation -- a detailed, structured 10-theme ways-of-working framework with a 6-week upskilling plan; and The Engineering Lead's preparation -- an engineering-focused strategy covering requirement checklists, deployment strategy, SDLC discipline, MCP/Skills for internal productivity, and a request for DevOps resources.

---

## 2. Theme-by-Theme Deep Analysis

### Theme 1: Better Requirement Gathering

**Key discussion points:**
- The Senior Manager: Emphasized that the team has always operated on-the-fly with requirements -- "Today we do it on the fly, all of that, correct." Requirements are written as Jira tickets after-the-fact rather than before building.
- The Senior Manager: Noted the absence of product managers for their platforms -- "none of us have a product manager."
- The Engineer: Stressed that requirement gathering AND requirement defining are both needed -- "gathering plus proper defining before we do our solutioning."
- The Engineer: Said engineering teams historically assume the system will do everything, leading to disappointment: "we assume that our system will do everything and in engineering that is never a thing."
- Day 2: The team discussed that SMEs will sometimes give detailed requirements (citing the claims document case for Vertex) but only when they have ownership. When the team has to extract requirements, they rarely get them early enough.
- Day 2: the Director proposed that evaluation datasets (golden datasets) serve as the primary mechanism for requirement definition -- define what "correct" looks like before building.

**The Senior Manager's preparation proposed:**
- Flip the process: SMEs collect real examples of manually done tasks before building starts.
- Create a "golden dataset" scored on 3-5 dimensions (accuracy, completeness, tone, regulatory compliance).
- Client signs off on the rubric, not the prompt -- eliminating "this doesn't feel right" feedback loops.
- The golden dataset becomes the most valuable IP per client.

**The Engineering Lead's preparation proposed:**
- A formal kickoff checklist for new product engagements before engineering starts.
- A monthly evaluation checklist for ongoing products.
- Service engagements continue as-is.
- "No engineering work starts without defined scope and sign-off."

**Points of alignment:**
- All sources agree the current ad-hoc approach is failing.
- Everyone agrees evaluation data / golden datasets are needed.
- Both prep assets advocate for formal process before coding starts.

**Points of contention:**
- The Senior Manager's preparation relies heavily on SME involvement for golden dataset creation. In the transcripts, the Senior Manager himself acknowledged that "the majority of the people don't want to do all of this. They don't want to know how the solution works."
- Practical challenge raised in Day 2: SMEs will not give all requirements early on -- "the thoughts will come up once they see the output." This creates a chicken-and-egg problem.
- The Engineer and the Director debated whether requirements should include acceptance criteria in a traditional engineering sense vs. the more fluid approach the Director favors.

**Open questions:**
- Who owns the golden dataset creation process? Can SMEs be forced to participate?
- For existing platforms (MLR, MWA, MedCom), do we need to redo requirement gathering or can existing SOPs suffice?
- How do we handle the inherent unpredictability of LLM outputs in requirements?

**Dependencies:**
- Requires SME cooperation (a QC team member, a QC team member, or external SMEs).
- Requires the VP's support to formalize the process across teams.

---

### Theme 2: Reducing Deployment Time / Build and Test Strategy

**Key discussion points:**
- A Solution Architect: Identified deployment time for any change as the main challenge he faces on MedCom.
- The Senior Manager: "Out of the time that we took only 20% is built, 80% is testing. People won't really understand why 80% is testing."
- Day 2: the Director proposed embedding evaluation sets into PR deployment pipelines -- "when you're pushing a particular deployment to the platform, gets checked. There's an output that runs, goes through this evaluation process, and only when it passes is when it gets deployed."
- Day 2: Referenced Stripe's model of pushing 100+ PRs daily with automated test repositories.
- Day 2: The auto-refinement demo from Day 1 was positioned as the mechanism to speed testing -- let AI run test suites, compare against golden outputs, and iterate automatically.

**The Senior Manager's preparation proposed:**
- A five-phase, two-week cycle: error analysis (days 1-2), eval definition (days 3-4), development (days 5-8), validation (days 9-10), deploy handoff (day 10).
- Three-tier testing: automated code checks on every commit, LLM-as-Judge evals on every PR, weekly SME reviews.
- Integration of Promptfoo into GitHub Actions.
- Prompts decoupled from code and stored in a versioning platform (Langfuse or Braintrust).
- Target: cut prototype-to-production time by 30% within two quarters.

**The Engineering Lead's preparation proposed:**
- Deployment architecture differences between internal and client environments documented at engagement start.
- DevOps involvement from initial scoping, not after development.
- Dedicated or shared DevOps resource with defined SLA (4 business hours for requests, 2 business days for provisioning).

**Points of alignment:**
- Universal agreement that manual testing is unsustainable and AI-led testing must replace it.
- All agree prompt versioning is an unsolved problem that must be addressed.
- Both prep assets and transcripts agree evaluation datasets should gate deployments.

**Points of contention:**
- The team has not yet solved prompt versioning -- should they use Langfuse, Braintrust, AWS, or build their own?
- The Engineer pushed back on Day 2 about non-engineers pushing code to production, even with review.

**Open questions:**
- Which prompt versioning platform to adopt?
- How to set up automated CI/CD for LLM-based systems specifically?
- Who builds the eval infrastructure -- the GenAI team's engineers or the CTO office?

**Dependencies:**
- DevOps access/resource (currently requests go through email to a separate AWS team with unpredictable turnaround).
- CTO office cooperation for deployment pipeline setup.

---

### Theme 3: Ongoing Deployment Without Breaking / Validation

**Key discussion points:**
- Day 2: the Director noted that prompt changes in production are currently "a leap of faith."
- Day 2: The team discussed that testing works on their local system but may not work once deployed -- "it has worked on my things" but fails in production.
- Day 2: Canary deployment was raised -- CTO office rolls out to small percentage first.

**The Senior Manager's preparation proposed:**
- Four safeguards: prompt versioning (semantic versions with environment labels), regression testing (full eval suite before staging), canary deployment (small traffic percentage first), production monitoring (success rate, hallucination rate, latency, cost, domain-specific metrics).
- Auto-rollback if any metric drops below threshold.
- Pin model versions (e.g., claude-sonnet-4-5-20250929, never "latest") and re-run full eval suite before model upgrades.

**The Engineering Lead's preparation proposed:**
- Formalized deployment approval process beyond architecture diagrams.
- Clear deployment plan covering how to deploy, validation steps post-deployment, and rollback procedures.

**Points of alignment:**
- All agree current deployment is fragile and needs safeguards.
- Rollback capability is universally desired.

**Open questions:**
- Who implements canary deployment -- GenAI team or CTO office?
- How to handle model version upgrades without breaking existing flows?
- How to monitor production quality metrics when the GenAI team doesn't always have production access?

---

### Theme 4: Decision Making on Solutioning

**Key discussion points:**
- The Senior Manager: Admitted to solutioning on calls -- "I am totally guilty of this. So I'm putting it out... I will stop doing that as well." He proposed formal solutioning workshops going forward.
- The Senior Manager: Raised the critical point that the team went agentic on PR and ISI when they should not have -- "PR is a basic major issue. It should not have gone agentic."
- The Senior Manager: "How do we keep evolving with tech? I think it's a strategy question."
- Day 2: The team discussed Anthropic's "complexity ladder" -- start with simplest architecture, escalate to agents only when needed.
- Day 2: the Director proposed: solutioning workshops where everybody sits in, argues it out, then decides. "Solutioning should be workshop driven... I will stop doing that on calls."
- The Engineer: Emphasized that every time the team picks a new approach (agents, frameworks), something else comes up 6 months later. He wanted stability.

**The Senior Manager's preparation proposed:**
- A formal decision framework: fixed predictable steps = deterministic workflow; different inputs need different handling = add routing; independent subtasks = parallelize; genuinely open-ended = use agent.
- Default to RAG for pharma work (constantly changing regulatory data), fine-tune only for consistent style/format at scale.
- Tiered models -- Haiku for simple extraction, Sonnet/Opus for complex reasoning.
- Every architectural decision justified by eval results.

**The Engineering Lead's preparation proposed:**
- Solution sign-off authority resting with Satish, Suvesh, or Anant before engineering begins.
- Peer-to-peer solution review among engineers.
- SDLC with proper solution diagrams (architecture diagrams, data flow, integration points, deployment topology).

**Points of contention:**
- The Engineer pushed back on the idea that code base access and experimentation-driven solutioning should replace paper-based architecture design. He argued: "Solutioning from an engineer is different than solutioning from your side" and "when we start coding, that means start delivering."
- The Director countered: "Architecture decisions, if they are based on experimentation, you would actually be making stronger architectural decisions rather than just designing it on paper."
- This is a fundamental philosophical split between traditional SDLC (the Engineer) and experimentation-first approach (the Director/the Senior Manager).

**Open questions:**
- Who has final sign-off authority on solution architecture?
- When the CTO office has already picked a framework (Strands), how much freedom does the GenAI team have?
- How to prevent the pattern of adopting something and then having to abandon it 6 months later?

---

### Theme 5: What Should Engineering Do on an Ongoing Basis

**Key discussion points:**
- The Senior Manager: "I want to question that boundary between engineering and solution. I want to see why an Engineer and the Engineer cannot do prompt skills. And I also question why can't you [solution team] do what they're doing."
- The Director: Proposed that the entire team should have code base access and contribute code, with the Engineer/an Engineer doing reviews.
- The Director: "If only two people are doing it versus... we don't have a choice. We can't otherwise ship at the pace that we want to ship."
- The Engineer: Proposed that engineers should review code produced by the non-engineering team, build sandbox environments, and maintain architecture diagrams.
- Day 2: the Director proposed engineers should write AI-powered code review skills so they can scale their review capability.

**The Senior Manager's preparation proposed:**
- Engineers build five platform components: prompt management system, eval infrastructure, agent orchestration layer, self-service testing interface (Streamlit), observability stack.
- North-star metric: "percentage of team actions that can happen without an engineer in the loop."
- Engineers stop being pulled into every prompt test and debugging session.

**The Engineering Lead's preparation proposed:**
- Build abstracted, reusable skill sets and catalogue them.
- Build MCPs for Cursor (internal productivity multiplier).
- Create Claude Skills for Claude Code encoding engineering standards.
- Publish MCPs and skills that serve both developer productivity AND application runtime.
- Continuous learning: bi-weekly tech talks, monthly "innovation sprint," quarterly skill assessment.
- Key ask: "Protected time for engineering excellence is not a distraction from delivery, it is an accelerant."

**Points of contention:**
- The biggest debate of Day 2 was on code base access. The Engineer argued code access should be limited to core contributors and that non-engineers writing production code creates accountability issues. The Director argued everyone needs access to experiment, solution, and ship faster.
- The Engineer: "If they're not the core contributors, then why access?" the Director: "We fundamentally change the ways of working... everybody will do prompts, everybody will do code."
- The Engineer eventually conceded but proposed a sandbox approach as compromise.

**Dependencies:**
- DevOps resource needed (dedicated or shared with SLA).
- GitHub access for the full team.
- CTO office buy-in for engineers embedded in the GenAI team.

---

### Theme 6: Project Management / Timelines

**Key discussion points:**
- The Senior Manager: "It always feels like we are always doing catch up... we rush things. Parkinson's Law will always be there."
- The Director (Day 1, In-person 3): Noted that the team has never successfully done the second part -- scalability after POC. "We created a POC on our customer and it straight away went" to production.
- Day 2: the Director set a 2-3 week proof-point timeline for skills + evals + auto-refinement.

**The Senior Manager's preparation proposed:**
- Milestones tied to quality gates instead of story points: prototype working end-to-end (week 2-3), eval baseline (week 3), failure categories addressed per sprint (weeks 4-8), comprehensive eval suite (week 9-10), CTO handoff (week 11-12).
- Range estimates: "70% confident in 4 sprints, 90% confident in 6."
- Show actual LLM outputs including failures in every sprint review.
- "Agree on 'good enough' quality thresholds BEFORE starting work, not after three months of iteration."

**Points of alignment:**
- Everyone agrees the current pattern of rushing from POC to production without validation is broken.
- All agree on the need for quality-gate-based milestones.

**Open questions:**
- How to protect build time when delivery takes precedence?
- What is the right cadence for sprint reviews given the experimental nature of LLM work?

---

### Theme 7: Delivery vs. Building -- Who and How

**Key discussion points:**
- The Senior Manager: "I want to ship off delivery separately. Do somebody else manage delivery." He acknowledged no other team can deliver GenAI engagements without the GenAI team intervening -- "I do not see that happening in the last next one year."
- The Senior Manager: Proposed carving out delivery leads from within the team (e.g., a Solution Architect for internal automation).
- Day 2: the Director formalized: builders hand off a formal package (architecture docs, prompt templates, eval suite, limitations, runbook, training sessions). Only L3 escalations loop back to builders.
- Day 2: "Solutions that can't be handed off should be flagged as a product design failure."

**The Senior Manager's preparation proposed:**
- Formal handoff package: architecture docs, prompt templates with rationale, eval suite with pass/fail criteria, known limitations, operational runbook, 2-3 training sessions.
- Self-service tooling as the key enabler (prompt management platforms, eval dashboards, decision-tree playbooks).
- Target metric: "weeks from handoff to AI team no longer needed."

**The Engineering Lead's preparation:**
- Did not address this theme directly but implicitly supported it through the focus on reusable components and self-sufficiency tooling.

**Points of contention:**
- The VP will likely say "your current delivery cannot suffer" -- building new things must be in addition to delivery, not instead of.
- Day 2: The team acknowledged this is a Catch-22: they can't build because they're delivering, and they can't stop delivering because there's no one else.

**Dependencies:**
- The VP must approve any reallocation of team time from delivery to building.
- A delivery-capable person or team must be identified.

---

### Theme 8: Team's Role in the Organization

**Key discussion points:**
- The Senior Manager: "What is the position or the role of this particular team in the larger organization?... We are the third person coming into this whole thing."
- The Senior Manager: "We are the underdogs... we got to be able to convince people that whatever we are doing is the right thing."
- The Senior Manager: Described the original premise: "solution architect similar to how people build buildings." But noted the team is "not even in the room" when things go to scale.
- Day 2: the Director proposed the team owns: solution architecture, prompt quality, and eval/validation. CTO office owns: production infrastructure and scaling.
- The Engineer: "If you own solution architecture completely, then success and failure both comes to your bucket."
- Day 2: the Director acknowledged that for the broader org role, they need the VP's support and an organizational change that the team alone cannot enact.

**The Senior Manager's preparation proposed:**
- AI Solution Architects (2-3 people), AI Quality Specialists (2-3 people), AI Engineers (2 people), Delivery Manager, Project Manager.
- RACI: GenAI team Accountable for solution design and output quality; CTO office Accountable for production infrastructure.
- Amazon's Single-Threaded Owner model: 2-3 people own a product area end-to-end.

**The Engineering Lead's preparation proposed:**
- Evolve from "delivery-focused execution function" to "strategic GenAI engineering function that creates reusable IP."
- "Recognition of the team's evolving role -- from delivery execution to strategic GenAI engineering."

**Points of contention:**
- The CTO office views the GenAI team's work as not scalable and not properly engineered.
- Engineering teams feel: "why should I listen to you? You can't write a line of code."
- The broader org has not formally defined where this team fits.

**Dependencies:**
- The VP must champion the formal org structure change.
- Buy-in from Satyak/Ashok's team and the CTO Rao's team.
- Senior Leadership's support at the top.

---

### Theme 9: Team Aspirations

**Key discussion points:**
- The Senior Manager: "I personally feel that somewhere I have a responsibility to make sure that all of your aspirations are connected to the way... I don't want it to be divergent."
- Day 2: the Director stated that aspirations will be handled through one-on-ones, not in the group session.
- The Engineer: Asked directly -- "Do you guys would appreciate taking a development responsibility?" -- signaling his interest in the team learning to code.

**The Senior Manager's preparation proposed:**
- The pharma-AI intersection is the team's moat -- "70% of pharma hiring managers cannot find candidates with both deep pharmaceutical knowledge and AI skills."
- Emerging roles: Clinical Trial AI Analyst, Regulatory AI Specialist, Pharmacovigilance AI Lead.
- 60/30/10 time allocation: 60% delivery, 30% building reusable components, 10% experimentation.
- Priority skills for non-technical members: eval design, context engineering, rapid prototyping with Cursor/Claude, basic Python scripting, AI product management.
- A 6-week bootcamp covering eval-driven thinking, tooling, agentic architecture concepts, and a simulated sprint.

**Open questions:**
- Will the organization support the 60/30/10 allocation?
- Person-specific aspirations not yet mapped.

---

### Theme 10: Increasing Productivity / Revenue per Resource

**Key discussion points:**
- The Senior Manager: "There are single entrepreneurs... 5-6 people generating 100 million dollars in ARR." He asked: "Is our revenue dependent on number of resources?"
- The Senior Manager: "the VP will basically say, what is your average revenue per employee?" -- and acknowledge it is already low.
- Day 2: the Director: "There are entire companies being built... 100 million in revenue. MLR, we are losing to Kopli... MedCom, just Gamma Presentee."
- Day 2: the Director proposed: "We as a team set goals... we will not be bringing in more people. We will figure out a way to manage it ourselves."

**The Senior Manager's preparation proposed:**
- Three mechanisms: (1) Component library (prompt templates, eval frameworks, RAG pipeline patterns, guardrail configs) so 40%+ of new solutions are assembled not built. (2) Template-first delivery -- every engagement starts from a template, customizes only 20% client-specific. (3) AI-augmented individual output -- Cursor, Claude, no-code workflow tools for every team member.
- "Every solution we build should leave behind components that make the next solution faster."

**Points of alignment:**
- Universal agreement that the team should not grow in headcount but increase output per person.
- Skills and component reuse is the primary mechanism.

---

## 3. Key Decisions Made

1. **Skills, Tools, and Evals as fundamental building blocks** -- The entire team converged on this as the immediate focus area, regardless of which platform or framework is chosen (Day 2).

2. **Single platform vision** -- Agreed in principle that one unified platform serving all life science value streams is the target, not separate products for MWA, MLR, MedCom, etc. (Day 2).

3. **2-3 week proof-point timeline** -- Each track (MLR, MWA, MedCom) must demonstrate skills + evals + auto-refinement results within 2-3 weeks (Day 2).

4. **Solutioning workshops replace on-call decisions** -- Both the Director and the Senior Manager committed to stopping ad-hoc solutioning on calls (Day 1 In-person 3, Day 2).

5. **No team headcount growth** -- Increase revenue per resource instead. "We will not be bringing in more people" (Day 2).

6. **SMEs will not be involved in technical work** -- the Senior Manager explicitly stated: "I would not recommend involving SMEs in anything apart from what they already do" (Day 1 In-person 3).

7. **Four capability pillars remain** -- Content authoring, content generation, review (MLR), and visual/MedCom. No pivot needed (Day 2).

8. **Strands must be evaluated** -- As it is an org-level call. But other frameworks (Claude Agent SDK, LangGraph, etc.) should also be evaluated against defined criteria (Day 2).

9. **Code base access for all team members** -- Despite The Engineer's pushback, the Director decided the entire team should have access with engineer review of contributions (Day 2).

10. **Process document to be created** -- the Senior Manager tasked with creating an end-to-end lifecycle process with checkpoints, gates, roles, and artifacts (Day 2).

---

## 4. Points of Contention

### 4.1 Code Base Access and Who Writes Code
- **the Director**: Everyone should have access, everyone should contribute code, engineers review.
- **the Engineer**: Code access should be limited to core contributors. Non-engineers writing production code creates accountability issues. Engineers need proper requirements/acceptance criteria before they code.
- **Resolution**: the Director overrode -- all will have access. The Engineer proposed sandbox as compromise.

### 4.2 Experimentation-First vs. Architecture-First Solutioning
- **the Director**: "Architecture decisions, if they are based on experimentation, you would actually be making stronger architectural decisions."
- **the Engineer**: "In engineering, solutioning comes before you write a piece of code... if that happens, we always break in terms of scalability."
- **Resolution**: Unresolved. The Director wants to try the experimentation approach; the Engineer committed to going along but stated he would remain against it.

### 4.3 Timeline for Agentic Shift / Claude Cowork Adoption
- **the Senior Manager**: "I also feel that the third block [Claude Cowork-like platform] is at least a year early... the ecosystem, clients, internal teams would not be ready for such a radical jump."
- **the Director**: "If you already start with something that is behind, then we will always be behind." He acknowledged pharma adoption is slow but argued they must build ahead of the curve.
- **Resolution**: Compromise -- build skills/tools/evals immediately (not controversial), test on Claude Cowork (lightweight), and defer the full platform decision.

### 4.4 LangGraph vs. Cloud Agent SDK vs. Other Frameworks
- **a Solution Architect**: Advocated for LangGraph -- model agnostic, production-tested, conditional routing.
- **the Director**: Against LangGraph -- workflow-driven (not truly dynamic), state-based communication between agents, "defeating the purpose of truly building a dynamic system."
- **the Engineer**: Wanted to understand how skills connect to MCPs and how the practical plumbing works.
- **Resolution**: Evaluate all frameworks against defined criteria (10 parameters identified). Strands mandatory to evaluate. Decision deferred pending hands-on testing.

### 4.5 Product vs. Service
- **the Engineer**: Asked repeatedly whether they are building a product or providing a service, because the strategy changes completely.
- **the Director**: "In my mind, doesn't matter. You build good products, both let them use it."
- **the Senior Manager**: Proposed internal adoption first -- "if our approach is that we want our internal folks to use this to deliver things quicker for the client, we would have a lot of control."
- **Resolution**: Build for both, but immediate focus is on making something that works. GTM is secondary to product quality.

---

## 5. Critical Dependencies

| Dependency | Owner | Impact |
|---|---|---|
| the VP's approval for time reallocation (delivery vs. building) | the Director to pitch | Blocks all new development work |
| DevOps resource with SLA | the VP / CTO office | Blocks deployment improvements, environment provisioning |
| GitHub / code base access for all team members | the Director / CTO office | Blocks collaborative development |
| CTO office buy-in for new architecture / framework | the VP, the MWA track lead | Blocks framework decision |
| SME cooperation for golden datasets | the Senior Manager, a QC team member | Blocks eval-driven development |
| Formal org structure change to define team role | the VP, Senior Leadership | Blocks long-term positioning |
| Budget for API costs (Opus usage) | the Director | Constrains experimentation |
| Architecture review from senior external person (AVP+) | the VP to arrange | Blocks scalability validation |

---

## 6. Org Politics and Dynamics

### 6.1 CTO Office Relationship
- The engineering team (CTO office, led by people like Sreekanth, Satyak, the CTO Rao) operates like "typical Indian IT" with Jira tickets, fixed requirements, and low accountability for understanding the GenAI pipeline.
- The Senior Manager: "Pick anybody from the engineering team. If they can explain the entire pipeline to me, I will sign my gratuity to you."
- The engineering team's view of GenAI: "You can't write a line of code. Why should I listen to you?"
- GenAI team's view of engineering: They don't understand GenAI, resist learning, use "no proper requirements" as a shield.
- The Director acknowledged: "I don't want to get in there at all" re: involving the CTO office leadership in the new approach. He preferred to build proof internally first.

### 6.2 the VP's Role
- The VP is the VP who controls resource allocation, budget, and org structure decisions.
- The Director: "I am not sure the VP is going to agree to this... I've had one or two conversations with the VP before."
- The team planned to present to the VP after Day 2 but acknowledged he would likely say "your current delivery cannot suffer."
- The VP's expected metric: revenue per employee / average revenue per resource.

### 6.3 Internal Perception
- Leadership feedback: "This team is good at building prototypes... not good at scale."
- The message is getting reinforced that the GenAI team cannot build scalable products.
- The Director: "Nobody else other than me is to blame for this."
- Lost confidence from leadership due to Vertex and AZ pushback.

### 6.4 Client Politics (Vertex Specific)
- The client's own teams are at loggerheads: tech leadership wants to cut SME headcount, while the SME head keeps expanding.
- The platform was deployed in the client's environment, effectively making it "their product" -- loss of IP control.
- Client-specific SOPs keep changing, breaking existing platform configurations.

### 6.5 the MWA track lead's Parallel Track
- the MWA track lead (likely CTO-side) is working on a separate version of MWA. The GenAI team should "assume that will be a separate track" running in parallel.
- This creates uncertainty about the future of the current MWA platform the team has built.

### 6.6 Knowledge Silos
- The Senior Manager: "If someone asks a question, it will either have to come to me or to the Director. There is no one else that can answer that question. That is the bottleneck of scalability."
- What is proprietary vs. what should be democratized is still a gap.

---

## 7. The Agentic Shift

### 7.1 The Demo (Day 1)
The Director demonstrated a platform built on the **Claude Agent SDK** over approximately two weeks:
- **Architecture**: Orchestrator agent reads skill files, spawns sub-agents dynamically, monitors their progress, handles error recovery.
- **Skills-driven**: Markdown files describing how to perform tasks. No hard-coded workflows.
- **Dynamic orchestration**: The system decides pipeline stages, agent count, chunking strategy, and execution waves at runtime.
- **Code-native**: Agents can write and execute code (Python scripts, bash commands, grep commands). Programmatic + LLM hybrid approach for source extraction.
- **Knowledge bases**: Three types -- structural (document format), conventions (writing style), corrections (learning from manual edits).
- **Auto-refinement**: Used Cursor as a "testing agent" that runs the platform repeatedly, compares against manual benchmarks, identifies gaps, modifies skills, and re-tests. Quality improved from 4.1 to 9.0 over 17 runs and 16 system versions.
- **Cost**: ~$42 per full CSR authoring run (not optimized). Auto-refinement: ~$100 over 2 days across multiple sessions.
- **Visual assets**: Generated programmatic charts (Plotly), SVG, and embedded them in PPTs/Word with brand guidelines.
- **Error recoverability**: Orchestrator monitors agents, respawns on failure, detects stalled agents.

### 7.2 Key Technical Points
- Everything is file/folder-based (no DB). The Director argued agents are "much better interacting with files through commands."
- Logging through hooks (non-blocking to the application).
- Context management: Orchestrator writes session state to files, can spawn new orchestrator to continue from checkpoint.
- Max 150 turns per agent to prevent infinite loops.
- Agent cap: 8 concurrent agents (configurable).

### 7.3 Framework Evaluation Criteria (10 Parameters, Day 2)
1. Code execution capability (code-native platform)
2. Truly dynamic orchestration (not workflow-defined)
3. Model agnostic
4. Production grade (concurrency, state management, memory)
5. Low-code / no-code setup complexity
6. Multi-agent orchestration
7. Tools/plugins/skills ecosystem
8. Error handling and recovery
9. Latency / streaming
10. Community stability, support, and commercial licensing

### 7.4 Framework Contenders
- **Claude Agent SDK**: The Director's choice. Code-native, dynamic. But Claude-model-locked.
- **Strands**: Mandated by org (the MWA track lead's call). AWS-native, serverless. Unknown code execution capability. Must evaluate.
- **LangGraph**: a Solution Architect's recommendation. Model agnostic, production-proven, large ecosystem. But workflow-driven (state-based), not truly dynamic.
- **Google ADK**: the Director tested it. "Google is worse" -- doesn't support dynamic orchestration.
- **Autogen**: Microsoft has done 3 pivots in one year. Stability concern.
- **OpenAI Agents**: Available but less discussed.

---

## 8. Product vs. Platform Strategy

### 8.1 Single Platform vs. Multiple Products
- **Current state**: Three separate products (MLR, MWA, MedCom) with separate pipelines, separate teams, no integration.
- **The Director's position**: Must move to single platform. "Why will people come buy 4 platforms from us, which are not integrated, each taking one hour, which Claude Cowork will do end-to-end in 5 minutes?"
- **Value chain collapse**: the Director argued boundaries between writing, review, content generation, and visuals will collapse. A single platform that does end-to-end is the future.
- **Example**: He demonstrated going from raw clinical trial data to CSR authoring directly, bypassing the traditional biostats-to-TFL-to-CSR chain.

### 8.2 Build Platform vs. Build Skills for Existing Platforms
- **Option A**: Build own platform (full control, IP ownership, but massive effort).
- **Option B**: Build skills/tools/evals that plug into Claude Cowork or similar (faster, lower risk, but platform dependency).
- **Option C**: Start with skills (Option B), test on Claude Cowork, identify gaps, then decide if own platform is needed.
- **Team converged on Option C** -- skills + evals + lightweight harness first. Platform decision deferred.

### 8.3 Product vs. Service Positioning
- Indegene's revenue is 95% resource-based (services).
- The team historically started with product mindset but pivoted to service mindset (building client-specific features).
- The Engineer: "Initially we started the product mindset and later we converted into a service mindset... that's where we lose the track."
- The Senior Manager proposed internal adoption first (AI-enabled services where internal SMEs use the platform), with external product play as secondary.

### 8.4 The Differentiation Question
- Pure tech: "We are already behind. I don't think we'll ever be ahead" -- the Senior Manager.
- Differentiators identified: (1) Life science domain knowledge encoded in skills, (2) Evaluation datasets that are pharma-grade, (3) Client-specific customization (SOPs, brand guidelines, therapeutic area knowledge), (4) Integration with pharma systems (Veeva, Argus, CTMS).
- The Senior Manager: "I have privately focused on us working on evals, because that's what we can do and we should do."

---

## 9. Timeline and Immediate Next Steps

### 9.1 Immediate (2-3 Weeks)
- Each track (MLR, MWA, MedCom) produces: skills, evaluation datasets, and auto-refinement proof points.
- Agentic framework evaluation: hands-on testing of Strands, Claude Agent SDK, and potentially LangGraph against the 10 criteria.
- Scalability framework: rubric with benchmarks per product, tested against Claude Cowork as competitor baseline.
- Process document: the Senior Manager to create end-to-end lifecycle with checkpoints, gates, roles.
- Skills education session for the team.
- Reading material shared by the Director.

### 9.2 Near-Term (1-3 Months)
- Framework decision finalized.
- First version of unified platform (or skill library) operational.
- Eval infrastructure deployed (prompt versioning, automated testing in CI/CD).
- Present proof points to the VP and leadership.
- Begin internal adoption with SME teams.

### 9.3 Medium-Term (3-6 Months)
- Full skills library across all four capability pillars.
- Production deployment with canary and monitoring.
- Formal handoff process operational -- builders separate from delivery.
- Upskilling program complete (6-week bootcamp from The Senior Manager's plan).

### 9.4 Long-Term (6-12+ Months)
- Unified platform for all life science value streams.
- AI employee capabilities for complex, multi-step goals.
- Organization-wide ways of working adopted.

---

## 10. Comprehensive List of Open Questions

1. Which agentic framework should we standardize on? (Strands vs. Claude Agent SDK vs. LangGraph vs. other)
2. Should we build our own platform or build skills for Claude Cowork / similar?
3. How do we convince the VP to allocate time away from delivery to building?
4. How do we define "scalability" -- concurrent users? document volume? processing time? all of the above?
5. Who is the architecture reviewer from outside the team (AVP+ level)?
6. How do we get dedicated DevOps support?
7. How do we handle the model lock-in risk if we go Claude-only?
8. What happens when a client wants a different model provider?
9. How do we convert existing SOPs and prompt libraries into skills?
10. What is the interaction model between our team and the MWA track lead's parallel MWA track?
11. How do we handle the folder-based architecture at scale (vs. DB)?
12. What is the cost model for agent-heavy systems in production?
13. How do we get SMEs to create golden datasets without them wanting to?
14. When do we get buy-in from CTO office teams (Satyak, the CTO Rao) and at what stage?
15. Do we actually need the CTO office? (the Engineer asked directly: "Do we actually need them?")
16. What is the formal org structure change needed and who champions it?
17. How do we handle IP protection when deploying in client environments?
18. How to prevent skills degradation over time?
19. What is the disaster recovery / fallback process?
20. How do we measure "revenue per resource" improvement concretely?
21. What does "done" look like for us -- prototype handoff or production-grade delivery?
22. How do we handle the 80% testing / 30% building ratio more efficiently?
23. Can we pin model versions in production without breaking existing flows?
24. What is our differentiation when Claude Cowork releases life sciences plugins?
25. How do we ensure cross-section consistency in agentic authoring at scale?
26. What is our position on video/audio capabilities -- deprioritize or invest?

---

## 11. Ideas and Proposals Catalog

| # | Idea / Proposal | Who | Source |
|---|---|---|---|
| 1 | Build unified life sciences platform analogous to Claude Cowork | the Director | Day 2 |
| 2 | Skills + Tools + Evals as fundamental building blocks | the Director, the Senior Manager | Day 2 |
| 3 | Auto-refinement: AI agents test, compare against manual, update skills | the Director | Day 1 demo |
| 4 | Golden datasets as primary requirement artifact | the Senior Manager | Prep asset |
| 5 | LLM-as-Judge evals on every PR | the Senior Manager | Prep asset |
| 6 | Prompt versioning platform (Langfuse/Braintrust) | the Senior Manager | Prep asset |
| 7 | Canary deployments for prompt changes | the Senior Manager | Prep asset |
| 8 | Pin model versions, never use "latest" | the Senior Manager | Prep asset |
| 9 | Evaluation data sets as a product / differentiator | the Senior Manager | Day 2 |
| 10 | Build MCPs for Cursor (internal productivity) | the Engineer | Prep asset |
| 11 | Claude Skills for Claude Code | the Engineer | Prep asset |
| 12 | Dedicated DevOps resource with 4-hour SLA | the Engineer | Prep asset |
| 13 | Solution sign-off authority before engineering starts | the Engineer | Prep asset |
| 14 | Peer-to-peer solution review among engineers | the Engineer | Prep asset |
| 15 | SDLC with proper solution diagrams | the Engineer | Prep asset |
| 16 | Single-Threaded Owner model (Amazon-style) | the Senior Manager | Prep asset |
| 17 | Engineer-written AI code review skills | the Director | Day 2 |
| 18 | Non-engineers contributing code with engineer review | the Director | Day 2 |
| 19 | Sandbox environments for safe experimentation | the Engineer | Day 2 |
| 20 | Engineer pair programming (the Engineer + an Engineer on same project) | the Engineer | Day 1 In-person 3 |
| 21 | Solutioning workshops (not on-call decisions) | the Director, the Senior Manager | Day 1-2 |
| 22 | Formal handoff package (docs, evals, runbook, training) | the Senior Manager | Prep asset |
| 23 | "Solutions that can't be handed off = product design failure" | the Senior Manager | Prep asset |
| 24 | Team offsite / team building budget | the Engineer | Day 1 In-person 3 |
| 25 | 6-week bootcamp for upskilling | the Senior Manager | Prep asset |
| 26 | 60/30/10 time allocation | the Senior Manager | Prep asset |
| 27 | Test on Claude Cowork first, then decide platform | the Senior Manager, team | Day 2 |
| 28 | Use Cloud Cowork as competitor benchmark for scalability targets | the Director | Day 2 |
| 29 | Dynamic UI generation as a skill | the Director | Day 2 |
| 30 | Knowledge base at user/team/org levels | the Director | Day 2 |
| 31 | Bi-weekly tech talks, monthly innovation sprint | the Engineer | Prep asset |
| 32 | Agentic vs. non-agentic decision framework | the Senior Manager | Prep asset |
| 33 | Tiered model usage (Haiku for simple, Opus for complex) | the Senior Manager | Prep asset |
| 34 | Internal education sessions before external dissemination | the Director | Day 2 |
| 35 | Component library (prompt templates, eval frameworks, RAG patterns) | the Senior Manager | Prep asset |
| 36 | Template-first delivery (start from template, customize 20%) | the Senior Manager | Prep asset |
| 37 | Hybrid approach: start small agents, evaluate, then expand | a Solution Architect | Day 2 |
| 38 | LangGraph + Temporal hybrid for durability | a Solution Architect | Day 2 |
| 39 | Plugins for pharma systems (Veeva, Argus, CTMS) | the Director | Day 2 |
| 40 | Implement proof first within team, then disseminate WoW to org | the Director | Day 2 |

---

## 12. Raw Insights for WoW Document Creation

### 12.1 Process Gates and Checkpoints
The WoW document should include the following sequential gates:
1. **Requirement Gate**: Problem statement defined, golden dataset created (or planned), evaluation rubric agreed, success parameters defined (accuracy, time, cost), scalability requirements documented.
2. **Solutioning Workshop Gate**: Workshop held with all stakeholders (solution architects + engineers). Agentic vs. non-agentic decision documented with justification. Architecture diagram created. Deployment architecture identified. Non-functional requirements defined.
3. **Prototype Gate**: Skills written and tested. Eval suite built and passing. Auto-refinement run at least once. Cost and latency benchmarks established.
4. **Deployment Gate**: Full eval suite passes in staging. Prompt versions locked and labeled. Rollback procedure documented. Engineering review of all code changes complete.
5. **Handoff Gate**: Architecture docs, prompt templates with rationale, eval suite, known limitations, operational runbook, and training sessions all delivered.

### 12.2 Role Definitions
- **Solution Architects** (the Senior Manager, a Solution Architect, a Solution Architect, the Director, a Solution Architect): Define problem statements, write skills, create eval rubrics, iterate on prompt quality, own domain accuracy.
- **AI Engineers** (the Engineer, an Engineer): Own infrastructure, deployment pipelines, code reviews, technical user stories, framework evaluation, automated testing infrastructure.
- **QC/Testing** (a QC team member, a QC team member, a team member): Build and maintain golden datasets, run eval comparisons, monitor production quality metrics.
- **Delivery** (a Solution Architect, a team member): Manage client engagements, use formal handoff packages, escalate only L3 issues to builders.
- **Leadership** (the Director, the Senior Manager): Strategy, the VP interface, cross-team collaboration, architecture oversight.

### 12.3 Build and Test Strategy
- 80% of testing should become automated (LLM-as-Judge + programmatic checks).
- Eval datasets should be version-controlled alongside prompts/skills.
- Every skill change triggers a regression run.
- Auto-refinement sessions should be scheduled (not ad-hoc) with defined session boundaries.
- Cost tracking per agent execution must be built in from the start.

### 12.4 Knowledge Management
- Knowledge bases should be maintained at three levels: platform-wide (conventions), client-specific (brand guidelines, SOPs), and user-specific (preferences, corrections).
- All knowledge should be in structured formats (JSON preferred for programmatic querying).
- Version knowledge bases alongside skills.
- Correction knowledge bases should be created from manual edits and fed back into the system.

### 12.5 Cross-Team Collaboration Model
- The CTO office should have a designated reviewer (AVP+ level) for architecture sign-off.
- At minimum, GenAI team needs: code base access, DevOps support, and deployment pipeline access.
- Solution workshops should include CTO-office engineers from Day 1 of new engagements.
- For client deployments, DevOps must be involved from kickoff, not post-development.

### 12.6 Communication and Reporting
- All-hands meetings should include technical deep-dives, not just status updates.
- Every sprint review should show actual LLM outputs (including failures) to keep expectations grounded.
- Stakeholders should see range estimates, not point estimates, for timelines.
- The team should maintain a living "what we tried and what we learned" document.

### 12.7 Time Allocation Principles
- Delivery cannot be disrupted (the VP will insist on this).
- Build time must be carved from optimization of existing delivery (faster testing, less manual work).
- 2-3 weeks for initial proof points is the agreed timeline.
- After proof points, negotiate formal time allocation with the VP.

### 12.8 Risk Mitigation
- Framework lock-in: Evaluate model-agnostic frameworks alongside Claude-specific ones.
- Skills degradation: Build evaluation datasets that run continuously to catch regressions.
- Knowledge silos: Document everything in skills files (not in people's heads).
- Client data security: Skills and knowledge bases must be deployable within client environments.
- Budget overruns: Set per-session and per-project cost caps for agent execution.

---

## 13. April 8 the Director Call — Post-Offsite Clarifications 

On April 8, the Senior Manager had a follow-up call with the Director to clarify key open questions before creating the WoW. This section captures the findings and their implications.

### 13.1 the VP Has Not Fully Approved

The Director does not yet have "complete approval to run." He needs to go back to the VP with deliverables (evaluation datasets, skills, proof points) before getting formal go-ahead. The team is in a precarious position: "The situation is pretty bad... we don't have enough backing."

**Implication for WoW:** The WoW must be designed to produce visible results within existing delivery bandwidth. It cannot assume protected build time until the VP approves.

### 13.2 MedCom Is the Only Open Lane

- MWA: the MWA track lead is already working on it. "Nishan took it with the MWA track lead."
- MLR: Engineering team is trying to build with Strands.
- MedCom: "That leaves us only MedCom... we might end up just doing MedCom as a pilot."

**Implication for WoW:** All worked examples and pilot planning should target MedCom. The WoW should be product-agnostic in design but MedCom-specific in first implementation.

### 13.3 Write for End-State, Not Transition

The Director: "Create it in a holistic manner. Assuming that the overall org will fall to like engineering." The WoW should describe the full target operating model with cross-functional stakeholders, even though those stakeholders aren't yet on board.

### 13.4 Accountability Is on the GenAI Team

"The accountability everything will be on us." But the Director also clarified responsibility must be distributed: "Some of it should come from us on what we will take, what will engineering take, what will QA take, what will SMEs take, what will DevOps take."

**Implication for WoW:** The RACI must show GenAI team as Accountable for solution quality overall, while distributing Responsibility to other functions.

### 13.5 Platform Decision Still Open

Both Claude Cowork and building their own platform remain options. The Director senses "most of our organizations will say that we will build only and not use Cowork environment." But for now: "keep both options open."

### 13.6 the VP's Operating Model: Federated Development, Central Governance

"Development is federated, and then there's a central governance to check all of that." The WoW must fit within this model, not fight it.

### 13.7 Non-Engineers Contribute Code, Engineers Review

Confirmed. "Final approval review will always come from engineering." The WoW must define the contribution-review-merge workflow in detail.

### 13.8 Flexibility Is Non-Negotiable

"Tomorrow, if the direction changes, the tech wind blows in a different way, we should be able to quickly adapt. Which is now what we are struggling with."

### 13.9 Engineering Leadership Change

The CTO is "trying to cleanup the team." "the VP somehow doesn't have the appetite to build a team." the Director will still take end ownership but must work with engineering. Decisions are happening at "Amit, the MWA track lead, Senior Leadership level."

### 13.10 the VP Created an Asset Using the Platform

"the VP created an asset on our platform. It actually came out." This deck contains insights on how leadership thinks about the team's work and what was discussed at the AGM. Important context for understanding leadership expectations.

---

## 14. Cross-Reference to WoW Documents 

This analysis informed the creation of the following WoW documents. This table maps analysis sections to the documents they fed into.

| Analysis Section | Fed Into | How |
|-----------------|----------|-----|
| Theme 1 (Requirement Gathering) | Granular_Solutioning_Requirements.md | Discovery session process, golden dataset planning, client sign-off |
| Theme 2 (Deployment Time / Build Strategy) | Granular_Build_Test_Deploy.md | 3-tier testing, CI/CD pipeline, phased rollout |
| Theme 3 (Ongoing Deployment / Validation) | Granular_Build_Test_Deploy.md | Canary deployment, rollback, monitoring |
| Theme 4 (Decision Making on Solutioning) | Granular_Solutioning_Requirements.md | Complexity ladder, solutioning workshops |
| Theme 5 (What Should Engineering Do) | Granular_Build_Test_Deploy.md + Granular_Skills_KB_Lifecycle.md | Code contribution model, skill creation, eval infrastructure |
| Theme 6 (Project Management) | Granular_Cross_Cutting_Operations.md | Sprint cadence, estimation, prioritization |
| Theme 7 (Delivery vs Building) | WoW_Proposed_Approach.md | Stage 5 (Operate & Evolve), handoff package |
| Theme 8 (Role in Organization) | WoW_Proposed_Approach.md | RACI framework, role definitions |
| Theme 9 (Aspirations) | Granular_Cross_Cutting_Operations.md | Knowledge management, upskilling, external learning |
| Theme 10 (Revenue per Resource) | Granular_Skills_KB_Lifecycle.md | Component library, reuse governance, SOP migration |
| Section 4 (Points of Contention) | Granular_Solutioning_Requirements.md | Disagreement handling in §3.2; internal scope change process in §5.5 |
| Section 6 (Org Politics) | Granular_Cross_Cutting_Operations.md | CTO office relationship protocol (§5.2), escalation paths (§1.3) |
| Section 7 (Agentic Shift) | Granular_Skills_KB_Lifecycle.md | Skill structure, auto-refinement, KB types |
| Section 13 (April 8 Call) | WoW_Proposed_Approach.md | Assumptions, parked questions, design principles |
