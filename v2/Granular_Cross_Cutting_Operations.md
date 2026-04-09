# Cross-Cutting Operations -- Granular Process

## 1. Communication Protocols

### 1.1 Meeting Cadence

*This cadence is suggested as a starting point. The specific schedule should be discussed and adapted by the team.*

| Meeting | Frequency | Duration | Attendees | Purpose | Agenda |
|---------|-----------|----------|-----------|---------|--------|
| **Daily Standup** | Daily, 9:30 AM | 15 min | Full team | Blockers and coordination | Each person: what I'll do today, blockers, need help from whom |
| **Sprint Review** | Bi-weekly, Thursday 2 PM (Week 2) | 1 hour | Full team + Leadership | Demo actual outputs, review eval scores | Show LLM outputs (including failures), eval score trends, decisions needed |
| **Solutioning Workshop** | As needed (per Stage 2) | 2-4 hours | SA + Engineers + relevant stakeholders | Design and decide on solution architecture | See Solutioning doc |
| **Weekly Sync with Engineering** | Weekly, Wednesday | 30 min | GenAI Solution Approvers + Engineering lead | Cross-team coordination | Deployment requests, blocking issues, upcoming needs |
| **Leadership Update** | Bi-weekly, aligned with sprint | 30 min | Director + VP | Status, decisions, escalations | Proof points, metrics, resource/budget asks |
| **Tech Talk** | Monthly, last Friday | 45 min | Full team | Knowledge sharing | One team member presents a deep-dive (new tool, technique, post-mortem learning) |
| **Quarterly WoW Retro** | Quarterly | 2 hours | Full team | Process improvement | What's working, what's friction, WoW updates needed |

**Meeting load reality check for a 10-person team:**

The above cadence totals roughly 3-4 hours/week per person (standup 1.25h + sprint review amortized 0.5h + tech talk amortized 0.4h + any workshops). This leaves 32+ hours of focused work per week. Anything above 5 hours/week of meetings is a red flag -- raise it in the quarterly retro.

**Rules to keep it sustainable:**
- **Cancel aggressively.** If standup has no blockers for 3 consecutive days, skip the next one and use async. Resume when a blocker surfaces.
- **Tech talks are monthly, not bi-weekly.** Bi-weekly was aspirational but unsustainable alongside delivery. One solid talk per month with proper preparation beats two rushed ones.
- **Sprint review is sacred.** This is where trust gets built with leadership. Never skip or compress it.
- **No ad-hoc meetings during focus blocks** (see 4.2). If it can wait 4 hours, it waits.

### 1.2 Remote/Hybrid Participation Protocol

Some team members dial in rather than attending in person. Without explicit norms, remote participants become passive observers.

| Norm | Detail |
|------|--------|
| **Active participation required** | Every team member must contribute during meetings — no passive listening mode. Speak during standup, provide input during workshops. If you have nothing to add, explicitly say so rather than remaining silent. |
| **Meeting notes posted within 1 hour** | Rotating note-taker posts to the team channel. Remote participants who missed context can read back. |
| **Screen-share default for demos** | Sprint reviews and tech talks must screen-share, not rely on a room projector that remote people cannot see. |
| **Explicit round-robin for key decisions** | Before closing a solutioning workshop or sprint planning, the facilitator calls on each remote participant by name, e.g., "Any concerns?" directed to each person individually. Silence is not consent -- it is often a bad connection. |
| **Async pre-reads for workshops** | Send the pre-workshop packet (see Solutioning doc) 2 days in advance. Remote attendees especially need this because they cannot lean over and ask a neighbor for context. |
| **Recording for high-stakes sessions** | Record solutioning workshops and sprint reviews (not standups). Post recording + summary. Anyone who could not attend can catch up. |

### 1.3 Async vs. Sync

| Use Async (Teams/Slack message) | Use Sync (Call/Meeting) |
|--------------------------------|------------------------|
| Status updates, FYI notifications | Solutioning decisions |
| Simple questions with factual answers | Disagreements or debates |
| Sharing eval results or PR links | Post-mortem reviews |
| Non-urgent requests (response within 4 hours) | Client escalations (SEV-1/2) |
| Documentation links and handoffs | Onboarding a new team member |

**Rule:** If an async thread exceeds 10 messages without resolution, schedule a 15-minute call.

**Async response SLAs:**
- Team channel messages: respond within 4 business hours
- Direct messages tagged urgent: respond within 1 hour
- PR review requests: first review comment within 1 business day
- If you will be unavailable for >4 hours during business hours, post in the team channel

### 1.4 Escalation Paths

L1 -- Self-Serve (individual)
  Can resolve with: runbook, FAQ, skill documentation, eval dashboard
  Examples: routine deployment, eval score interpretation, known-issue workaround
  |
L2 -- Team Lead (Solution Architect / Engineering Lead)
  Escalate when: L1 resources don't cover it; needs domain judgment; quality issue
  Examples: new failure pattern, client-specific convention question, framework issue
  Response: within 4 hours
  |
L3 -- Senior Manager
  Escalate when: cross-team coordination needed; engineering/DevOps dependency blocked;
    client communication judgment call; risk register item materializing
  Examples: engineering team not responding for >2 days, deployment blocked, SME refusing,
    cost-quality tradeoff decision
  Response: within 8 hours
  |
L4 -- Director
  Escalate when: org-level dependency; client relationship at risk; resource conflict;
    strategic direction change; budget approval
  Examples: client escalation to leadership, dedicated DevOps resource needed,
    priority changes from senior leadership, need to pause delivery for building
  Team members escalate to Senior Manager, not Director directly,
    unless Senior Manager is unavailable for >1 business day.
  Response: within 1 business day
  |
L5 -- VP
  Escalate when: org-level blocker; budget approval; strategic direction affecting
    other teams; client at risk of churning
  ONLY Director escalates to VP. No one else contacts VP directly about
    team operational issues.
  How: scheduled bi-weekly update is the default channel.
    For urgent items, Director requests a 15-minute ad-hoc slot via email
    with a 1-paragraph problem statement + ask.

**Why this chain matters:** The team is in a building phase organizationally. Bypassing the chain (e.g., an engineer emailing senior leadership about a DevOps blocker) undermines the Director's credibility. Every escalation must be framed as a data-backed ask, not a complaint. The Director controls that framing.

**When the chain breaks:** If the Senior Manager is unavailable for >1 business day, team members escalate directly to the Director. If the Director is unavailable for >2 business days, the Senior Manager escalates to the VP but only for items that are genuinely blocked.

### 1.5 Client Communication Rules

| Rule | Detail |
|------|--------|
| **Single point of contact** | Each engagement has one SPOC from GenAI team (usually the Solution Architect owning that track). All client communication goes through SPOC. |
| **No sharing raw LLM outputs** | Review every output before sharing with client. Run through eval first. If eval fails, do not share. |
| **LLM uncertainty language** | Never promise "this error will not happen again." Instead: "We've added this failure pattern to our test suite and the system now passes. We monitor for quality drift weekly." |
| **Scope change acknowledgment** | Any client request that changes requirements must be acknowledged as a scope change: "I understand you'd like X. Let me assess the impact on timeline and quality and get back to you." Do NOT agree on the call. |
| **Status cadence** | Weekly written status to client (template below). Monthly in-person or video review with output demo. |
| **No timeline promises without buffer** | Always use range estimates: "We expect this in 2-3 sprints." Never commit to a specific date on a call. If the client presses for a date, respond: "Let me check our sprint plan and get back to you by [tomorrow/EOD]." |

**Weekly Client Status Template:**

```
Subject: [Project Name] Weekly Status -- Week of [Date]

Quality: [Eval score trend -- improving / stable / needs attention]
Progress: [What was completed this week]
Next Steps: [What's planned for next week]
Blockers: [Anything needing client action]
Metrics: [Key numbers -- outputs processed, eval pass rate, latency]
```

### 1.6 Decision Documentation

Every significant decision (architecture, framework, scope, trade-off) is logged:

## Decision: [Title]
**Date:** YYYY-MM-DD
**Participants:** [Roles/Teams]
**Context:** [Why this decision was needed -- 2-3 sentences]
**Options Considered:**
1. [Option A] -- pros: ... / cons: ...
2. [Option B] -- pros: ... / cons: ...
**Decision:** [What was decided]
**Rationale:** [Why -- the key argument that tipped the scale]
**Consequences:** [What this means for the project going forward]
**Review Date:** [When to revisit if conditions change]

Stored in: `/decisions/YYYY-MM-DD-{short-title}.md` in the project repo. Linked from sprint review notes.

---

## 2. Project Management & Sprint Cadence

### 2.1 Sprint Structure

**Sprint length: 2 weeks.** Aligns with the team's need for enough time to run auto-refinement cycles while staying accountable.

```
Week 1:
  Mon: Sprint planning (1 hour) -- assign work, set targets
  Tue-Thu: Build and test
  Fri: Mid-sprint check (15 min standup extension) -- are we on track?

Week 2:
  Mon-Wed: Build, test, and prepare demo
  Thu: Sprint review (1 hour) -- demo, metrics, decisions
  Fri: Retro (30 min) + next sprint grooming (30 min)
```

### 2.2 Estimating LLM Work

**Do NOT use story points.** LLM work is inherently uncertain -- prompts may need 2 iterations or 20. Instead:

**Use range estimates tied to quality gates:**

| Confidence Level | Estimate Format | Example |
|-----------------|----------------|---------|
| "We've done this before" | 70% confident in X sprints | "CSR Section 11 skill: 70% confident in 1 sprint, 90% in 2" |
| "New territory, similar to past work" | 50% confident in X sprints | "MedCom visual pipeline: 50% confident in 2 sprints, 80% in 3" |
| "Genuinely novel" | "We'll know more after a 1-week spike" | "Agentic auto-refinement: spike first, then estimate" |

**What to estimate per task:**
1. Effort to create/modify skill(s)
2. Effort to create/expand eval dataset
3. Expected number of auto-refinement iterations
4. API cost estimate (based on similar past runs)
5. Dependencies (on other team members, engineering, DevOps)

### 2.3 Backlog Management

**Tool:** Whatever the team already uses (Jira, Linear, or even a shared spreadsheet). Don't introduce new tooling for this.

**Backlog columns:**
```
Inbox > Groomed > Sprint Backlog > In Progress > In Review > Done
```

**Grooming criteria (item is ready for sprint):**
- [ ] Clear definition of what "done" looks like (linked to a gate)
- [ ] Eval dataset exists or creation is the first subtask
- [ ] Dependencies identified and unblocked (or explicitly noted as blocked)
- [ ] Estimated in range format
- [ ] Assigned to a person

### 2.4 Definition of Done -- Per Stage

| Stage | Done When |
|-------|----------|
| Stage 1 (Requirement) | Golden dataset plan exists, success parameters quantified, stakeholders identified, requirement gate checklist complete |
| Stage 2 (Solutioning) | Architecture documented, complexity decision justified, skills list finalized, solution gate checklist complete |
| Stage 3 (Build & Test) | Eval suite passes at threshold, auto-refinement run, code reviewed, build gate checklist complete |
| Stage 4 (Deploy) | Eval passes in deployed environment, monitoring live, rollback tested, deploy gate checklist complete |
| Stage 5 (Operate) | Handoff package delivered, delivery team trained, escalation path defined, handoff gate checklist complete |

### 2.5 Prioritization Framework

When everything feels urgent, use this matrix:

| | High Impact on Client/Revenue | Low Impact on Client/Revenue |
|---|---|---|
| **Blocking other work** | **P0: Do Now** (drop everything) | **P1: Do This Sprint** |
| **Not blocking** | **P2: Schedule Next Sprint** | **P3: Backlog** |

**Tie-breaker:** If two items are same priority, the one with an existing eval dataset goes first (faster to validate).

---

## 3. Knowledge Management & Cross-Learning

### 3.1 Where Knowledge Lives

| Knowledge Type | Location | Format | Owner |
|---------------|----------|--------|-------|
| Skills and KBs | Git repo: `/skills/`, `/knowledge-bases/` | Markdown, JSON | Skill owner (per metadata) |
| Eval datasets | Git repo: `/eval-datasets/` | JSON | QC team |
| Architecture decisions | Git repo: `/decisions/` | Markdown | Decision participants |
| Meeting notes | Teams/Confluence | Free-form | Rotating note-taker |
| Post-mortems | Git repo: `/postmortems/` | Markdown template | Incident owner |
| Client engagement docs | Shared drive (restricted access) | Mixed | Engagement SPOC |
| "What we tried & learned" | Git repo: `/learnings/` | Markdown -- one file per learning | Anyone |
| Onboarding materials | Git repo: `/onboarding/` | Markdown + links | Senior Manager (owner), updated by anyone |
| Org context / glossary | Git repo: `/onboarding/org-context.md` | Markdown | Senior Manager |

### 3.2 Preventing Knowledge Silos

| Mechanism | How It Works | Frequency |
|-----------|-------------|-----------|
| **Buddy pairing** | Each engagement has a primary + buddy. Buddy attends key meetings, reviews PRs, can cover if primary is unavailable. | Continuous |
| **Tech talks** | Monthly 45-min presentation by one team member. Topics: deep-dive on a skill, post-mortem, new tool evaluation, competitor analysis. | Monthly |
| **Skill documentation** | Every skill file is self-documenting (objective, inputs, rules, anti-patterns). Anyone can read and understand. | Per skill change |
| **Decision log** | Every significant decision is written down with context and rationale. | Per decision |
| **Cross-review** | PRs are reviewed by someone NOT on the same track (MLR person reviews MedCom PR). Builds cross-domain knowledge. | Per PR |
| **Engagement map** | A single page listing all active engagements: client, status, SPOC, buddy, key risks. Updated at sprint planning. | Bi-weekly |

### 3.3 Onboarding Guide

#### Week 1: Orientation and Access

**Day 1: Administrative Setup and Team Context**

| Task | Detail | Who Helps |
|------|--------|-----------|
| Team introductions | 30-min group call or in-person. Each person explains their role and current focus. | Senior Manager facilitates |
| Read team charter | Located at `/onboarding/team-charter.md`. Covers team mission, org position, how we work. | Self |
| Read org context doc | Located at `/onboarding/org-context.md`. Covers: key stakeholders and their roles, what the CTO office is, what MWA/MLR/MedCom mean, the team's current org dynamics. | Self |
| Access provisioning | See checklist below | Buddy + Senior Manager |

**Day 1 Access Provisioning Checklist:**

| System | What to Request | Who Grants | Expected Turnaround |
|--------|----------------|-----------|-------------------|
| GitHub | Repo access to GenAI org repos | Engineer | Same day |
| AWS Console | Read access to S3 buckets (log archives, eval datasets), CloudWatch | DevOps ticket (Engineer submits) | 1-2 business days |
| Cursor | License + workspace setup | Senior Manager | Same day |
| Langfuse / observability tool | Account creation + project access | Engineer | Same day |
| Jira / project tracker | Add to GenAI board | Senior Manager | Same day |
| Teams/Slack channels | Add to: genai-team, genai-alerts, genai-client-[name] | Senior Manager | Same day |
| Anthropic API | API key for development (dev account, spend-capped) | Engineer | Same day |
| Client VPN/environment (if applicable) | Access to client-deployed systems | Senior Manager submits request to client | 3-5 business days |
| Shared Drive | Access to client engagement docs (restricted per client) | Senior Manager | Same day |
| Claude Code / Claude Pro | Account setup for daily use | Self-provisioned, team expense | Same day |

**If any access takes longer than expected, the buddy owns tracking it. The new hire should not be chasing access requests in their first week.**

**Day 1-2: Read the WoW**
- Read this document (Cross-Cutting Operations)
- Read the Lifecycle Process doc (Layer 1)
- Skim the Build/Test/Deploy doc and Eval Dataset Lifecycle doc (focus on the "how it works" sections, skip the template details)

**Day 2-3: Shadow assigned buddy**
- Attend their meetings (standup, any client calls, any workshops)
- Watch how they work: how they modify a skill file, how they run an eval, how they submit a PR
- Ask questions freely. The buddy's job this week includes answering them.

**Day 3-4: Hands-on with the system**
- Read 3 skill files and their corresponding eval datasets
- Run one eval locally: `python run_eval.py --dataset [assigned-dataset] --mode quick`
- Read the traces in Langfuse for that eval run

**Day 5: End-to-end pipeline run**
- Run the full pipeline once on a sample input
- Read the traces end-to-end
- Write down 3 things that confused you. Share with buddy.

#### Week 2: First Contribution

- Assigned a small task: add 3 rows to an existing eval dataset, or fix a typo/add a rule to a skill file. Go through full PR process (branch, commit, push, PR, review, merge).
- Attend a solutioning workshop as observer (if one is scheduled; otherwise, read the notes from the most recent one)
- Read 2 post-mortems from past incidents (located at `/postmortems/`)
- 1:1 with Senior Manager (30 min): questions, context on team history, what matters, how the org dynamics work
- 1:1 with Director (30 min): strategic context, what leadership expects, vision for the team

#### Month 1: Ownership

- Own a minor skill improvement end-to-end (identify issue from eval data, modify skill, test, PR, merge)
- Present at a tech talk (even a short one: "what I learned in my first month")
- Complete the eval dataset creation exercise from the bootcamp
- By end of month: can explain the pipeline for their assigned track to someone else
- Buddy pairing shifts: now paired as buddy on a second engagement (observer role)

#### Onboarding Success Criteria

By end of Week 2, the new hire should be able to:
- [ ] Run an eval locally and interpret the results
- [ ] Submit a PR that passes review on the first or second attempt
- [ ] Name all active engagements and who owns them
- [ ] Explain the escalation path

By end of Month 1:
- [ ] Own and ship a minor skill improvement independently
- [ ] Present at a tech talk
- [ ] Explain their assigned track's pipeline to someone unfamiliar with it

### 3.4 External Learning

- **Monthly landscape scan:** One person (rotating) spends 2 hours reviewing: Anthropic blog, OpenAI releases, LangChain changelog, HuggingFace trends, competitor product updates (Gamma, Kopli, Cowork). Share a 1-page summary with the team.
- **Conference/paper budget:** Each team member can expense 1 online course or conference per quarter (pre-approved by the Director).
- **Tool trials:** When a new tool is relevant, one person runs a 1-week time-boxed evaluation and reports back. Uses the experiment brief template.
- **Individual learning plans:** Each team member is encouraged to identify one skill or knowledge area they want to develop each quarter. Discuss with your manager during 1:1s and align with team needs where possible.

*These external learning activities are suggested practices. The specific cadence and format should be adapted based on team capacity and priorities.*

---

## 4. Time Allocation & Prioritization

### 4.1 The Split

**Target allocation (requires leadership approval):**
- **60% Delivery** -- current client engagements, support, client communication
- **30% Building** -- new skills, eval datasets, pipeline improvements, component library
- **10% Learning** -- tech talks, external learning, experimentation, bootcamp

**Realistic allocation until leadership approves:**
- **85% Delivery** -- current engagements
- **15% Building + Learning** -- squeezed into gaps, Friday afternoons, between delivery milestones

**Being honest about the 85/15 reality:**

The 60/30/10 split is the aspiration. It will not happen until the team demonstrates proof points on MedCom that justify the ask. Here is the plan to get from 85/15 to 60/30/10:

| Phase | Timeline | Split | What Unlocks the Next Phase |
|-------|----------|-------|-----------------------------|
| **Phase 0: Current state** | Now | 85/15 | Nothing yet -- survival mode |
| **Phase 1: Prove the WoW works** | Weeks 1-6 (MedCom pilot) | 80/20 | Squeeze build time from delivery efficiency gains (faster testing via evals, less manual review). The extra 5% comes from time saved, not time taken from delivery. |
| **Phase 2: Present to leadership** | After MedCom pilot | Ask for 75/25 | Show: eval scores, time savings, client satisfaction on MedCom. Ask leadership for protected build time on one more track. |
| **Phase 3: Steady state** | After second track proves out | 60/30/10 | Two proof points. Revenue-per-resource trend improving. Leadership approves formal allocation. |

**What this means practically:** Do not schedule 30% build time into sprints until Phase 2. Instead, build within delivery: create eval datasets for current engagements, convert existing SOPs to skills as part of delivery work, run auto-refinement as a delivery improvement activity. This way "building" and "delivery" are the same work until leadership gives the green light.

### 4.2 Protecting Build Time

- **No-meeting blocks:** Tuesday and Thursday afternoons (1-5 PM) are protected for focused work. No internal meetings scheduled during these blocks.
- **Sprint commitment:** At sprint planning, explicitly allocate items to "delivery" and "building" buckets. Both are tracked.
- **Visibility:** Leadership status report includes both delivery metrics AND build/WoW progress. If build progress is zero for 2 consecutive sprints, escalate to Leadership as a blocker.

### 4.3 Handling Unplanned Work

```
Unplanned request arrives (client escalation, leadership ask, production issue)
  |
1. Classify: Is this SEV-1/2? -> Drop everything, handle immediately
  |
2. If not urgent: Add to backlog with priority label
  |
3. If it displaces sprint work: Discuss with Solution Architect
   - What gets pushed? Document the trade-off explicitly.
   - Notify affected stakeholders.
  |
4. If it happens repeatedly (>2 unplanned items per sprint):
   Raise in retro. Either buffer more in sprint planning or escalate the root cause.
```

**Tracking unplanned work:** At each retro, count how many unplanned items entered the sprint. If >30% of sprint capacity went to unplanned work for 2 consecutive sprints, this is a systemic problem. Escalate to the Director with data: "We absorbed X unplanned items in the last 2 sprints, displacing Y planned work. Here is the impact on build progress."

---

## 5. Stakeholder Management

### 5.1 Engagement Model Per Stakeholder

| Stakeholder | What They Need From Us | What We Need From Them | How We Engage | Frequency | Owner | Realistic Constraint |
|------------|----------------------|----------------------|--------------|-----------|-------|---------------------|
| **CTO/Engineering** | Solution designs to implement; clear requirements; eval suites to validate | Code reviews; deployment support; infra provisioning; architecture feedback | Weekly sync + PR-based collaboration | Weekly + per PR | Senior Manager | Adversarial dynamic. See 5.2 below. |
| **DevOps/AWS team** | Deployment requests with specs | Environment provisioning; deployment execution; monitoring setup | Ticket/email with standard request form | Per deployment | Engineer | Slow turnaround (days, not hours). Plan deployments 1 week ahead. |
| **SMEs** (domain experts, external) | Clear instructions on what to review; minimal time commitment | Manual reference outputs; scoring calibration; feedback on generated outputs | Structured review sessions with prep materials sent in advance | Weekly during active build | Solution Architect | Resistant to involvement. See 5.3 below. |
| **VP** | Proof that WoW works; metrics on productivity; client satisfaction | Time allocation approval; budget; org structure support; air cover | Bi-weekly 30-min update with metrics deck | Bi-weekly | Director | Gatekeeper. Only engages with data, not theory. |
| **Clients** | Working product; clear communication; realistic timelines | Requirements; sample documents; feedback on outputs; SOP access | Weekly status + monthly demo | Weekly/Monthly | Engagement SPOC | Some clients losing confidence. See 5.4 below. |
| **The parallel MWA track** | Non-interference; shared learnings if applicable | Clarity on scope boundaries; heads-up on overlapping work | See 5.5 below | As needed + monthly check-in | Director | Parallel track with unclear boundaries. |
| **QA teams** | Test plans; eval suites; quality criteria | Testing support; compliance review | Per-engagement involvement from Stage 2 | Per engagement | Solution Architect | Under-resourced. Engagement must be structured and efficient. |

### 5.2 Managing the CTO Office Relationship

The relationship is adversarial. The engineering team views GenAI's work as "not scalable and not properly engineered." GenAI views engineering as slow, unresponsive, and unwilling to learn. The WoW does not fix this relationship. It defines how to operate within it.

**Engagement protocol:**
1. **Every request to Engineering goes through the weekly sync.** Do not send ad-hoc Slack messages asking for engineering help. Collect requests during the week, prioritize them, and present them in the Wednesday sync. This is professional and reduces friction.
2. **Requests are formatted as structured tickets, not conversations.** Use the request template:
   ```
   Request: [What you need -- 1 sentence]
   Context: [Why -- link to engagement/decision doc]
   Impact: [What happens if this is delayed -- be specific]
   Preferred timeline: [When you need it by]
   Dependencies: [What you've already done / what's blocking]
   ```
3. **Never escalate directly from L2 to the CTO office.** Go through the Senior Manager (L3) who involves the Director (L4) if needed. The Director is the one who manages the CTO relationship at the leadership level.
4. **Document everything.** When the CTO office agrees to something, send a follow-up email confirming: "Per our discussion, Engineering will [X] by [date]. Please let me know if I've captured this incorrectly." This creates a paper trail without being aggressive.
5. **Share wins, not just requests.** When a joint effort produces a good result (deployment goes smoothly, eval scores improve), share credit with the engineering team in the sprint review. Building goodwill is a long game.
6. **If Engineering blocks and is unresponsive for >1 week:** The Senior Manager raises in the next L4 with the Director. The Director decides whether to escalate to the VP or find a workaround. The team does not go around the Director.

### 5.3 Managing SME Engagement

SMEs do not want to be involved in technical work. The WoW respects this. SMEs are asked for exactly two things:

1. **Manually completed examples** (3-5 per engagement, collected during Stage 1). Frame it as: "We need to understand how you do this manually so we can automate it. Can you share 3 recent completed documents?"
2. **1-hour scoring calibration session** (once per engagement, during eval dataset creation). Frame it as: "We've created a quality rubric. We'd like your expert judgment on whether our scoring criteria match your professional standards."

**That's it.** Do not ask SMEs to:
- Attend technical meetings
- Understand the platform, pipeline, or agent architecture
- Write or review prompts
- Do ongoing weekly reviews (Tier 3 human review is done by the QC team, not external SMEs)

**If the SME refuses even these two asks:** Document it in the risk register. Proceed with Solution Architect's domain knowledge as the baseline. Note in the engagement decision log: "Quality baseline established without SME calibration -- this is a known risk. SA provided domain expertise as proxy. Recommend re-calibrating if SME becomes available."

### 5.4 Managing Client Confidence

The team has lost some client confidence. Rebuilding it requires consistent, metrics-backed communication.

**What to say to clients:**
- "Our system achieves [X]% accuracy on our test suite of [N] real-world examples. Here's how we measure it."
- "When we find a new error pattern, we add it to our automated test suite so the system is checked against it on every update."
- "LLM systems are probabilistic. We target [X]% quality and monitor weekly. We cannot guarantee 100%, but we can guarantee we detect and address quality drift."

**What NOT to say:**
- "This error will never happen again" (it might -- models are non-deterministic)
- "The system is 99% accurate" (unless you have eval data to prove it)
- "We'll fix this by [date]" (use range: "We expect to address this in 1-2 sprints")
- "This is easy" (pharma AI is never easy)

**When a client raises a quality concern:**
1. Acknowledge: "Thank you for flagging this. We take quality seriously."
2. Investigate: Run the specific failure through the eval suite. Is it a known pattern?
3. Respond within 48 hours with: what happened, why it was not caught, what we are doing to prevent it (specific eval dataset addition, not vague promises)
4. Follow up in the next weekly status: "The pattern you flagged is now covered by test case [ID]. Here is the eval result."

### 5.5 Coordinating with the MWA Track

*Note: This coordination protocol is for the current organizational setup. As tracks evolve and organizational boundaries shift, this section may be updated or removed from the WoW suite.*

The MWA track lead is running a parallel MWA track through the CTO office. The GenAI team's MWA work may overlap. The WoW treats this as a boundary management problem, not a turf war.

**Protocol:**
1. **Monthly boundary check (owned by the Director).** A 30-minute call or async exchange between the Director and the MWA track lead to compare: what each track is working on, any overlapping document types or clients, any shared dependencies (models, infrastructure, SMEs).
2. **Shared learnings, not shared code.** If the MWA track discovers something useful (e.g., a new eval approach, a client SOP insight), and they choose to share it, capture it in the `/learnings/` folder. Do not integrate their code or skills into our pipeline without a solutioning workshop.
3. **If a client asks about both tracks:** The SPOC redirects to the Director. The Director and the MWA track lead align on messaging before responding. The team does not freelance answers about the other track.
4. **If scope overlap becomes a conflict:** The Director escalates to the VP with a clear proposal: "Track A covers X, Track B covers Y. Here is why." The team provides data (eval scores, timeline, cost) to support the proposal but does not engage in the political negotiation directly.

### 5.6 Presenting to Leadership

**Format the VP expects (inferred from discussions):**
1. Revenue per resource trend (are we improving?)
2. Client status (any at risk? any wins?)
3. Platform quality metrics (eval scores, not subjective)
4. Proof points (demo something working -- not slides, actual outputs)
5. Asks (what do you need from me to continue?)

**One-page deck template:**
```
Slide 1: Dashboard
  - [Metric 1] Revenue per resource: $X -> $Y
  - [Metric 2] Eval pass rate across platforms: X%
  - [Metric 3] Prototype-to-production time: X weeks
  - [Status] Client health: Green / Amber / Red

Slide 2: Demo
  - Live demo or recorded output comparison (before/after)

Slide 3: Ask
  - What we need + expected impact
```

**Rules for the VP update:**
- Never present a problem without a proposed solution
- Always lead with a proof point (something that worked) before the ask
- Keep it to 3 slides. The VP will ask questions -- leave room for discussion.
- If the ask is for time allocation or budget, quantify the expected return: "If we get X hours/week protected for building, we project Y% improvement in Z metric within N sprints, based on the MedCom pilot data."

---

## 6. Risk Management

### 6.1 Risk Register Template

| ID | Risk | Category | Likelihood (1-5) | Impact (1-5) | Score | Owner | Mitigation | Status |
|----|------|----------|------------------|-------------|-------|-------|-----------|--------|
| R-001 | Model provider outage during client delivery | Technical | 2 | 5 | 10 | Engineer | Fallback model configured; outputs cached | Mitigated |
| R-002 | Key person (Senior Manager/Director) unavailable for >1 week | People | 3 | 4 | 12 | Leadership | Buddy system; documented skills/decisions | Partially mitigated |
| R-003 | Framework we chose gets abandoned | Technical | 2 | 4 | 8 | SA | Framework-agnostic WoW; skills portable across frameworks | Mitigated by design |
| R-004 | Client SOP change breaks production pipeline | Client | 4 | 3 | 12 | SA/QC | SOP version tracking; eval dataset includes SOP-dependent rows | Active monitoring |
| R-005 | API costs exceed budget during auto-refinement | Financial | 3 | 2 | 6 | Engineer | Cost caps per session; daily spend alerts | Mitigated |
| R-006 | Eval dataset doesn't catch a production quality issue | Quality | 3 | 4 | 12 | QC | Tier 3 human review weekly; production failure -> new eval row | Active monitoring |
| R-007 | Regulatory audit requires audit trail of AI-generated content | Compliance | 3 | 5 | 15 | SA + Engineer | See 6.3 below | Partially mitigated |
| R-008 | Patient data exposure through LLM API calls | Data Privacy | 2 | 5 | 10 | Engineer | See 6.4 below | Mitigated by design |
| R-009 | CTO office non-cooperation blocks deployment for >2 weeks | Organizational | 3 | 4 | 12 | Director | Fallback: self-serve deployment to team-managed environment | Active mitigation |
| R-010 | The parallel MWA track supersedes our MWA work, rendering it redundant | Strategic | 3 | 3 | 9 | Director | Monthly boundary check; focus team on MedCom (our clear lane) | Monitoring |
| R-011 | SME refuses to participate in eval dataset calibration | People | 4 | 3 | 12 | SA | SA provides domain proxy; documented as risk; re-calibrate when SME available | Active |
| R-012 | Leadership does not approve time allocation shift | Organizational | 3 | 4 | 12 | Director | Build within delivery (Phase 1 plan); present proof points before asking | Active |
| R-013 | Client environment deployment loses IP control | Legal/IP | 3 | 4 | 12 | Director + Legal | Skills/eval datasets remain in our repo; only deployment artifacts go to client | Partially mitigated |

### 6.2 When to Escalate a Risk

- **Score >= 15:** Escalate to the Director immediately. Must be in the next Leadership update to the VP. Mitigation plan required within 1 week.
- **Score >= 12:** Must be in Leadership update. Mitigation plan required within 1 sprint.
- **Score >= 8:** Track in sprint retro. Mitigation plan within 2 sprints.
- **Score < 8:** Monitor. Review quarterly.

### 6.3 Pharma Compliance: Audit Trails for AI-Generated Content

Pharma is a regulated industry. Regulatory bodies (FDA, EMA) may require audit trails showing how documents were produced. The team must maintain the following for every production output:

| Audit Trail Element | Where It Lives | How It Is Generated |
|-------------------|----------------|-------------------|
| **Input document manifest** | Logged per run in Langfuse/observability tool | Automatically logged at pipeline start: list of all source documents consumed, with versions/hashes |
| **Skill versions used** | Logged per run | Pipeline logs the skill_id + version for every skill invoked |
| **KB versions used** | Logged per run | Pipeline logs the kb_id + version for every KB referenced |
| **Model version** | Logged per run | Pipeline logs the exact model identifier (e.g., `claude-sonnet-4-5-20250929`) |
| **LLM call traces** | Langfuse or equivalent | Every LLM call: input tokens, output tokens, model, timestamp, cost |
| **Eval scores** | Stored in eval history (git repo) | Every production output is scored; scores stored with run_id linkage |
| **Human review records** | Stored in engagement docs | When a human reviews/edits AI output, the original AI output and the edited version are both retained |
| **Change history** | Git log | All skill/KB/eval changes are in version control with author, date, and rationale |

**Retention policy:** All audit trail data is retained for a minimum of 7 years (standard pharma document retention). Storage is in S3 with versioning enabled and deletion protection.

**If a client or regulator asks "How was this document produced?":** The team can reconstruct the full chain: source documents -> skills (version) -> KBs (version) -> model (version) -> LLM calls (traces) -> output -> eval score -> human review edits. This is not optional. It is a baseline requirement for pharma AI.

### 6.4 Data Privacy Guardrails

| Guardrail | Implementation | Verified By |
|-----------|---------------|-------------|
| **No patient-level data in prompts unless explicitly approved by client** | Pipeline strips patient identifiers before LLM calls. Source extraction skill includes de-identification step. | Engineer reviews at PR level; Tier 1 automated check scans for PII patterns |
| **API calls go through approved endpoints only** | Model API calls routed through company-approved proxy/VPC. No direct calls from developer laptops to public APIs with client data. | Infrastructure config reviewed by engineer |
| **Client data does not leave approved environments** | Dev/test uses anonymized or synthetic data. Real client data only in staging/production environments with access controls. | Environment config; access audit quarterly |
| **Eval datasets with real client data are access-restricted** | Client-specific eval datasets stored in restricted folders. Access granted per engagement, not team-wide. | CODEOWNERS file + access review at engagement close |
| **No client data in universal skills or KBs** | Tier 1 automated check: scan for client identifiers in universal files. | CI/CD pipeline check on every commit |

### 6.5 External Audit Preparedness

If a client's regulatory team or an external auditor requests a review of the AI-assisted document production process:

**Who handles it:** The Director is the point of contact. The Senior Manager prepares the materials. No other team member engages directly with auditors unless the Director explicitly delegates.

**What we provide:**
1. **Process documentation:** The WoW suite itself -- showing the lifecycle, gates, eval methodology
2. **Audit trail for specific documents:** Per 6.3 above -- full chain from source to output
3. **Quality evidence:** Eval scores, human review records, production monitoring data
4. **Change control evidence:** Git history showing all skill/KB changes with review and approval

**What we do NOT provide without legal review:**
- Raw LLM call logs (may contain proprietary prompt engineering)
- Skill files in full (may be considered IP)
- Eval datasets containing other clients' data

**Pre-audit checklist (run annually or when a new client engagement starts):**
- [ ] Audit trail logging is active and verified for all production pipelines
- [ ] Retention policy is enforced (7-year minimum)
- [ ] Access controls are current (no stale permissions)
- [ ] At least one full audit trail reconstruction has been tested end-to-end in the last quarter
- [ ] Data privacy guardrails are passing in CI/CD

---

## 7. Quality Culture

### 7.1 Principles

1. **Eval failures are data, not blame.** When an eval reveals a problem, the right response is "let's add this to the test suite and fix it" -- not "who broke it."

2. **Show the failures.** Sprint reviews include outputs that failed, not just successes. This keeps expectations realistic and builds trust with stakeholders. The team has committed to showing actual LLM outputs including failures.

3. **"Good enough" is defined before starting.** The quality threshold is agreed with the client during Stage 1 (rubric sign-off). If mid-engagement the client wants higher quality, that's a scope change -- not a quality failure.

4. **Quality is measured, not felt.** "It looks better" is not valid evidence. "Eval score improved from 0.78 to 0.87 on the golden dataset" is.

5. **Catch it early, fix it cheap.** A failure caught in Tier 1 (commit) costs $0. In Tier 2 (PR) costs $2. In production, it costs client trust. Invest in eval datasets.

### 7.2 Concrete Quality Mechanisms

Principles without mechanisms are posters on a wall. Here is how each principle is enforced:

| Principle | Mechanism | Who Enforces | What Happens If Violated |
|-----------|-----------|-------------|--------------------------|
| Eval failures are data, not blame | Post-mortems use "5 Whys" format focused on process, not people. Template in `/postmortems/` | Senior Manager facilitates post-mortems | If someone is blamed in a post-mortem, the Senior Manager intervenes and redirects to process |
| Show the failures | Sprint review agenda template requires a "Failures and Learnings" section. Facilitator ensures it is covered. | Sprint review facilitator (rotating) | If a sprint review has no failure discussion, the facilitator adds it. If the team has no failures to discuss, that itself is discussed (are we testing hard enough?) |
| "Good enough" defined before starting | Requirement Gate checklist includes "pass/fail threshold agreed and documented." Gate does not pass without it. | SA + Leadership at gate review | Gate blocks. No build starts without documented threshold. |
| Quality is measured, not felt | Every quality claim in a client status update must cite an eval score or metric. No subjective language in quality sections. | SPOC reviews status before sending | Senior Manager reviews client statuses weekly during first 2 months. After that, spot-checks monthly. |
| Catch it early | Tier 1 and Tier 2 checks are mandatory in CI/CD. Cannot be bypassed without engineer + SA approval (and the bypass is logged). | CI/CD pipeline | If checks are bypassed, the bypass appears in the weekly engineering review. Repeated bypasses trigger a process review. |

### 7.3 Celebrating Wins

- **Sprint review shout-outs:** Call out skill improvements, eval score jumps, clever solutions
- **"Component of the sprint":** Highlight one reusable component that was created or improved
- **Client positive feedback:** Share in team channel immediately -- the team needs to hear that their work lands
- **Post "we survived" retros:** When the team handles a tough incident well, acknowledge the response -- not just the failure

---

## 8. Cross-Document References

This document connects to the rest of the WoW suite as follows:

| Topic in This Document | Detailed Coverage In |
|----------------------|---------------------|
| Solutioning workshops (Section 1.1, 5.1) | [Granular_Solutioning_Requirements.md](Granular_Solutioning_Requirements.md) -- full workshop protocol, complexity ladder, pre-workshop packet |
| Sprint structure and Definition of Done (Section 2) | [Granular_Build_Test_Deploy.md](Granular_Build_Test_Deploy.md) -- PR process, testing tiers, deployment pipeline |
| Eval datasets and scoring (Section 3, 7.2) | [Granular_Eval_Dataset_Lifecycle.md](Granular_Eval_Dataset_Lifecycle.md) -- dataset creation, scoring rubrics, LLM-as-Judge setup |
| Skills and KB lifecycle (Section 3.1) | [Granular_Skills_KB_Lifecycle.md](Granular_Skills_KB_Lifecycle.md) -- skill creation, versioning, auto-refinement, KB types |
| Incident response severity levels (Section 1.4) | [Granular_Build_Test_Deploy.md](Granular_Build_Test_Deploy.md) Section 4.3 -- SEV-1 through SEV-4 definitions and response process |
| Cost management and API budgets (Section 6.1 R-005) | [Granular_Build_Test_Deploy.md](Granular_Build_Test_Deploy.md) Section 5 -- cost tracking, budget thresholds, optimization levers |
| Client engagement lifecycle (Section 1.5, 5.4) | [Granular_Solutioning_Requirements.md](Granular_Solutioning_Requirements.md) -- requirement gathering, client sign-off, scope change management |
| Risk register pharma risks (Section 6) | [Granular_Eval_Dataset_Lifecycle.md](Granular_Eval_Dataset_Lifecycle.md) -- data handling, confidentiality, dataset versioning |
