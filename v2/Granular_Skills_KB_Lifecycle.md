# Skills & Knowledge Base Lifecycle — Granular Process

## 1. Skills Lifecycle

### 1.1 What IS a Skill File

A skill is a markdown file that instructs an agent on **how** to perform a specific task. It is the atomic unit of capability in the system. Skills are not code — they are structured natural language instructions that an LLM agent reads and follows.

**Structure:**

```markdown
---
skill_id: mwa-csr-s11-authoring
name: CSR Section 11 Authoring
version: 2.1.0
product_area: MWA
document_type: CSR
section: "11 - Usage Results"
author: [solution-architect-id]
created: 2026-04-15
last_modified: 2026-05-02
dependencies:
  - skill: mwa-source-extraction
    min_version: 1.0.0
  - kb: structural/csr-ich-e3
  - kb: conventions/writing-style-clinical
eval_dataset: csr-section-11/universal_v1.2
pass_threshold: 0.85
tags: [authoring, csr, usage-results, section-11]
status: production  # draft | testing | staging | production | deprecated
execution_mode: single-agent  # single-agent | multi-agent-step | orchestrator (see 1.11)
output_type: text  # text | structured-data | multi-modal | decision (see 1.12)
---

# CSR Section 11: Usage Results Authoring

## Objective
Author the Usage Results section of a Clinical Study Report following ICH E3 guidelines, using provided source TFLs and protocol.

## Input Requirements
You MUST have the following before starting:
- [ ] Table 14.1 or equivalent (Subject Disposition / Exposure Summary)
- [ ] Table 14.3 or equivalent (Dose Compliance / Dose Intensity)
- [ ] Protocol sections covering: dosing schedule, planned treatment duration, dose modification criteria
- [ ] SAP sections covering: exposure metric derivations

If any input is missing, STOP and report which input is missing. Do NOT fabricate data.

## Output Structure
Generate the following subsections in order:

### 11.1 Disposition of Subjects
- Summarize patient flow: enrolled -> randomized -> treated -> completed -> discontinued
- Include reasons for discontinuation with N and %
- Reference the disposition figure if available

### 11.2 Duration of Exposure
- Report median and range of exposure duration per treatment group
- Compare against planned treatment duration from protocol
- Flag if >20% of patients had exposure <80% of planned duration

### 11.3 Dose Intensity and Compliance
- Report mean relative dose intensity per treatment group
- Define compliance metric used (from SAP)
- Categorize: <80%, 80-120%, >120% of planned dose

### 11.4 Dose Modifications
- Report N and % of patients requiring dose reductions, interruptions, delays
- Summarize most common reasons for modification
- Reference dose modification criteria from protocol

### 11.5 Treatment Discontinuations
- Break down by reason: AE, lack of efficacy, withdrawal of consent, protocol deviation, other
- Report N and % per treatment group per reason

## Rules
1. NEVER invent or extrapolate numeric values. Every number must trace to a source TFL.
2. When interpreting data, always tie back to the protocol context (e.g., "consistent with the planned 24-week treatment duration").
3. Use past tense throughout.
4. Do NOT copy-paste table data verbatim. Summarize in narrative form.
5. Use cross-references ("as described in Section 10.1") rather than repeating information.
6. If a subsection has no relevant data (e.g., no dose modifications occurred), state this explicitly rather than omitting the subsection.
7. Keep each subsection to 150-300 words unless complexity demands more.
8. Apply conventions from KB: conventions/writing-style-clinical

## Anti-Patterns (What NOT to Do)
- "The data is shown in Table 14.1" without summarizing the data
- Listing every row of a table in paragraph form
- Using promotional language ("excellent compliance rates")
- Making causal claims ("dose reductions led to improved outcomes")
- Including content that belongs in Section 12 (efficacy) or Section 10 (study population)
```

### 1.2 Who Creates Skills

| Skill Type | Primary Creator | Reviewer | Approver |
|-----------|----------------|----------|----------|
| Domain/authoring skills (what to write, how to interpret) | Solution Architect | Peer Solution Architect + Engineer | GenAI Solution Approvers |
| Technical/pipeline skills (how to execute, parse, format) | Engineer | Peer Engineer + Solution Architect | GenAI Solution Approvers |
| Orchestration skills (how agents coordinate) | Engineer with SA input | Both peers | GenAI Solution Approvers |
| Evaluation/QC skills (how to judge quality) | Solution Architect + QC | Engineer | GenAI Solution Approvers |
| Classification/routing skills (MLR claims, content triage) | Solution Architect | Engineer + Domain SME | GenAI Solution Approvers |
| Multi-modal output skills (text + visuals, text + structured data) | Engineer + Solution Architect jointly | Both peers + domain SME | GenAI Solution Approvers |

### 1.3 Creation Process

```
1. TRIGGER: Requirement identified in Stage 1/2 that maps to a new capability
   |
2. CHECK CATALOG: Does a reusable skill already exist?
   |-- YES -> Fork and customize (see 1.10)
   +-- NO -> Continue to 3
   |
3. FIRST DRAFT (Solution Architect, 2-4 hours)
   - Write skill following the template structure above
   - Include: objective, inputs, output structure, rules, anti-patterns
   - Reference applicable KBs
   - Tag with metadata
   - Set execution_mode and output_type in frontmatter (see 1.11, 1.12)
   |
4. PEER REVIEW (1-2 hours)
   - Another SA reviews for domain accuracy
   - Engineer reviews for structural correctness and agent-compatibility
   - Feedback incorporated
   |
5. UNIT TESTING (2-4 hours)
   - Run skill in isolation on 3 test inputs
   - Manually verify outputs against expected results
   - Document: does the agent follow all rules? Any unexpected behavior?
   |
6. EVAL DATASET TESTING (1-2 hours)
   - Run against applicable eval dataset (if exists)
   - If no dataset exists, create minimum viable dataset first (see Eval doc)
   - Record scores
   |
7. PIPELINE TESTING (2-4 hours)
   - Integrate skill into the full pipeline
   - Run end-to-end on 2-3 complete documents
   - Check for interactions with other skills (conflicts, redundancy)
   |
8. APPROVAL
   - PR created with: skill file, test results, eval scores
   - Engineer approves code/structure
   - SA approves domain content
   - Merge to main
   |
9. DEPLOYMENT
   - Promote from testing -> staging -> production via environment labels
   - Production promotion requires passing full eval suite
```

**Total time for a new skill: 10-20 hours over 3-5 days** (varies by complexity)

### 1.4 Good Skill vs. Bad Skill

**Good skill patterns:**

| Pattern | Example |
|---------|---------|
| **Specific input requirements** | "You MUST have Table 14.1 or equivalent" -- not "use the relevant tables" |
| **Explicit stop conditions** | "If any input is missing, STOP and report" -- prevents hallucination |
| **Concrete anti-patterns** | Shows what bad output looks like, not just good |
| **Output structure with word count guidance** | "150-300 words per subsection" -- prevents bloat |
| **KB references for conventions** | "Apply conventions from KB: conventions/writing-style-clinical" -- separates style from substance |
| **Traceable to eval dataset** | Metadata links to the exact dataset and threshold |
| **Clear output_type declaration** | Frontmatter declares whether output is text, structured data, or multi-modal -- prevents downstream confusion |

**Bad skill anti-patterns:**

| Anti-Pattern | Problem | Fix |
|-------------|---------|-----|
| "Write a high-quality Section 11" | Too vague -- agent interprets "quality" differently each run | Define quality dimensions explicitly |
| Skill contains client-specific SOP details | Breaks when SOP changes; not reusable across clients | Move client-specific conventions to KB |
| Skill lists every possible edge case inline | Becomes a 5000-word document the agent struggles to follow | Use KB for edge case catalogs; skill references KB |
| No anti-patterns section | Agent doesn't know what to avoid | Always include 3-5 explicit "do NOT" rules |
| Hardcoded model instructions ("use Claude Sonnet") | Breaks if model changes | Model selection is a pipeline concern, not a skill concern |
| No version or metadata | Can't track which version produced which output | Always use frontmatter metadata |
| Mixing task instructions with orchestration logic | Skill tries to do both "how to write" and "how to coordinate agents" | Separate into a task skill and an orchestration skill |

### 1.5 Versioning Strategy

Skills follow **semantic versioning** in git:

- **MAJOR** (1.x -> 2.0): Output structure changed, rules fundamentally altered, new subsections added/removed. Breaking change -- all downstream dependencies must be tested.
- **MINOR** (1.0 -> 1.1): Rule refinements, additional anti-patterns, improved instructions. Non-breaking -- should improve quality without changing structure.
- **PATCH** (1.0.0 -> 1.0.1): Typo fixes, metadata updates, formatting. No behavioral impact.

Version is tracked in the frontmatter AND in git tags: `skill/mwa-csr-s11-authoring/v2.1.0`

### 1.6 Skill Dependencies and Composition

Skills can depend on other skills and KBs:

```
mwa-csr-full-authoring (orchestration skill)
  |-- mwa-source-extraction (extracts data from TFLs)
  |-- mwa-csr-s10-authoring (Section 10)
  |-- mwa-csr-s11-authoring (Section 11)  <- depends on mwa-source-extraction
  |-- mwa-csr-s12-authoring (Section 12)  <- depends on mwa-source-extraction
  |-- mwa-cross-reference-validator (checks cross-refs between sections)
  +-- mwa-formatting-finalizer (applies document template)
```

**Dependency rules:**
- A skill declares dependencies in its frontmatter with minimum version
- When a dependency is updated, all dependent skills must re-run their eval suites
- Circular dependencies are prohibited
- Maximum dependency depth: 3 levels

**Composition patterns (how skills combine):**

| Pattern | When to Use | Example |
|---------|------------|---------|
| **Sequential chain** | Output of skill A is input to skill B | Source extraction -> Section authoring -> Cross-reference validation |
| **Parallel fan-out** | Multiple independent skills run on the same input | CSR sections 10, 11, 12 authored in parallel from the same source TFLs |
| **Gather/merge** | Multiple skill outputs combined into one final output | Individual section outputs -> Formatting finalizer assembles full CSR |
| **Conditional branch** | Different skills invoked based on input characteristics | MLR router: promotional claim -> claims-checking skill; non-promotional -> standard review skill |
| **Iterative refinement** | Same skill re-invoked with its own output + feedback | Auto-refinement loop: generate -> judge -> modify skill -> regenerate |
| **Multi-modal assembly** | Text skill + data skill + visualization skill produce combined output | MedCom: narrative skill + data extraction skill + chart specification skill -> assembled asset |

### 1.7 Auto-Refinement: How AI Modifies Skills

The auto-refinement agent (running in Cursor or similar) can propose skill modifications based on eval failures.

**What the agent CAN do:**
- Add or refine rules based on observed failure patterns
- Add anti-patterns based on specific recurring errors
- Adjust word count guidance based on reference output analysis
- Add KB references when domain conventions are missing
- Restructure subsection instructions for clarity

**What the agent CANNOT do (guardrails):**
- Change the output structure (subsection order, required subsections)
- Remove existing rules (can only add or refine)
- Add client-specific content to a universal skill
- Modify the eval dataset or scoring thresholds
- Change skill dependencies
- Modify more than 20% of the skill's content in a single iteration
- Promote its own changes to staging or production (human-only action)
- Override a previous human-rejected change (if a human rejected a proposed change, the agent cannot re-propose the same change in the same session)

**Governance: Who Can Override Auto-Refinement Decisions**

| Scenario | Who Decides | Escalation |
|----------|------------|------------|
| Auto-refinement proposes a change, SA reviews and approves | SA (standard flow) | None |
| Auto-refinement proposes a change, SA rejects | SA documents rejection reason in the refinement log | None |
| SA and Engineer disagree on whether an auto-refinement change is valid | SA has domain authority; Engineer has structural authority. If the disagreement is about domain correctness, SA wins. If about agent behavior or technical risk, Engineer wins. | If unresolved: GenAI Solution Approvers break tie. |
| Auto-refinement produces a change that improves eval scores but violates a known domain convention | Reject the change. Add the convention to the skill or KB so the agent learns it. | SA reviews. |
| GenAI Solution Approvers want to override an SA rejection of auto-refinement | GenAI Solution Approvers must provide written rationale. SA documents disagreement in decision log. | Decision logged with both perspectives. |
| Multiple auto-refinement sessions produce conflicting recommendations | SA reviews all sessions, picks the best approach, documents why alternatives were rejected. | None unless SA needs input from peers. |

**Human review of auto-refinement changes:**
Every auto-refinement session produces a diff showing exactly what changed. A Solution Architect must review and approve all changes before they are merged. The review checks:
- Is the change grounded in actual failure evidence (not speculation)?
- Does the change apply universally (not just to one specific document)?
- Could this change cause regressions on currently-passing rows?

**Auto-refinement session limits (for a team new to this):**

| Guard | Value | Rationale |
|-------|-------|-----------|
| Max skill modifications per session | 5 | Prevents runaway changes; keeps diffs reviewable |
| Max cost per session | $50 | Prevents budget surprises |
| Max sessions per skill per sprint | 3 | Prevents over-tuning; forces human reflection between sessions |
| Cooldown between sessions on the same skill | 24 hours minimum | Ensures human review happens before the next session |
| Hold-out set shown to agent | Never | Prevents overfitting (see Eval doc, Section 2.5) |
| First 3 sessions on any new skill | Must be run with SA actively observing (not just reviewing after) | Builds intuition for what auto-refinement does before trusting it asynchronously |

### 1.8 When to Split vs. Keep Monolithic

**Split when:**
- The skill file exceeds 2000 words (agent attention degrades)
- Different subsections require fundamentally different expertise (e.g., statistical interpretation vs. narrative writing)
- Parts of the skill are reusable independently (source extraction is used by multiple section skills)

**Keep monolithic when:**
- All instructions are for one coherent task
- Splitting would require complex coordination between sub-skills
- The skill is under 1000 words

### 1.9 Retirement/Deprecation

```
1. Mark skill status as "deprecated" in frontmatter
2. Add deprecation notice with: reason, replacement skill (if any), date
3. Remove from active pipeline but keep in repository
4. After 3 months with no usage: archive (move to /archive/ folder)
5. Never delete -- historical reproducibility requires old versions to exist
```

### 1.10 Forking and Adapting Skills

(See also Section 4.2 for fork vs. parameterize decision.)

When forking a skill for a new use case:

```
1. Copy the source skill file
2. Assign a new skill_id (follow naming conventions in Section 6)
3. Update metadata: product_area, document_type, section, tags, dependencies
4. Modify rules and output structure for the new use case
5. Keep a "forked_from" field in frontmatter: forked_from: mwa-csr-s11-authoring/v2.1.0
6. Create or assign an eval dataset specific to the new use case
7. Run through the standard creation process (steps 4-9 in 1.3)
```

**Important:** Forked skills are independent after forking. Changes to the source do NOT automatically propagate. If a rule improvement in the source is universally applicable, it must be manually ported to forks (or extracted into a shared KB).

### 1.11 Execution Modes: Agentic vs. Non-Agentic Skills

Not every skill requires an agentic architecture. The `execution_mode` field in frontmatter communicates how the orchestrator should invoke the skill.

| Execution Mode | Description | When to Use | Example |
|---------------|-------------|-------------|---------|
| `single-agent` | Skill is given to one LLM call. Input in, output out. No iteration, no tool use. | Simple authoring tasks, formatting, data extraction from a known template | CSR section authoring with well-structured source TFLs |
| `multi-agent-step` | Skill is one step in a multi-agent pipeline. It receives input from a prior step and passes output to the next. It does NOT decide what to do next. | Sequential pipelines where each step is deterministic | Source extraction -> authoring -> cross-reference validation |
| `orchestrator` | Skill instructs an agent that can make decisions, invoke sub-skills, iterate, and use tools. The agent decides what to do at runtime. | Open-ended tasks: auto-refinement, complex document assembly with conditional sections, content requiring research | Auto-refinement agent, MedCom asset generation with variable layouts |

**Why this matters:**
- `single-agent` skills are cheaper, faster, and more predictable. Default to this.
- `orchestrator` skills are powerful but harder to evaluate, more expensive, and prone to unexpected behavior. Use only when justified by the Complexity Ladder analysis (see Solutioning doc, Section 2.4).
- The pipeline/framework decides HOW to execute; the skill declares WHAT it expects. A skill should never contain instructions like "spawn a sub-agent" -- that is orchestration logic, not task logic.

**Skill writing differences by execution mode:**

| Concern | single-agent | multi-agent-step | orchestrator |
|---------|-------------|-----------------|-------------|
| Input specification | Complete -- all inputs provided up front | Declares what it receives from the prior step | May specify initial inputs + discovery instructions |
| Output specification | Fully defined structure | Fully defined structure (must match next step's expected input) | Defines required output components; structure may vary |
| Rules | All rules inline or via KB reference | All rules inline or via KB reference + "hand-off" rules (what to pass downstream) | Rules + decision criteria for when to invoke sub-skills |
| Anti-patterns | Standard | Standard + "do not modify upstream output" | Standard + "do not loop indefinitely", "do not exceed N sub-skill invocations" |
| Eval approach | Straightforward input-output comparison | Test in isolation AND as part of the chain (see Build doc, cascade testing) | Evaluate final output quality + trace agent decisions (see Eval doc) |

### 1.12 Output Types: Beyond Plain Text

Skills produce different types of output. The `output_type` field declares what the skill generates, which affects downstream handling, eval approach, and composition.

| Output Type | Description | Eval Approach | Examples |
|------------|-------------|---------------|---------|
| `text` | Narrative prose -- the most common type | Text comparison, LLM-as-Judge on quality dimensions | CSR section authoring, MedCom narrative content |
| `structured-data` | JSON, tables, or other machine-parseable output | Schema validation + value accuracy checks | Source extraction (TFL data -> JSON), MLR claims list |
| `multi-modal` | Combined output: text + visual specifications, text + table + chart descriptions | Evaluate each component separately + overall coherence check | MedCom visual assets (text copy + layout specification + chart data) |
| `decision` | A judgment or classification, not content generation | Accuracy against known labels, precision/recall | MLR claims checking (compliant/non-compliant), content triage |

**Multi-modal skill composition pattern:**

For MedCom visual generation or similar multi-modal outputs, use a composition pattern rather than one monolithic skill:

**Example: MedCom Visual Orchestrator skill**

```
medcom-visual-asset-generation (orchestrator skill)
  |-- medcom-narrative-authoring (output_type: text)
  |     Writes the narrative content for the asset.
  |-- medcom-data-extraction (output_type: structured-data)
  |     Extracts data points from source documents for charts/tables.
  |-- medcom-chart-specification (output_type: structured-data)
  |     Given data, produces chart specs (type, axes, labels, data series).
  |-- medcom-layout-specification (output_type: structured-data)
  |     Given components, produces layout specification (grid positions, sizes, flow).
  +-- medcom-assembly-validator (output_type: decision)
        Validates that all components are coherent and consistent.
```

Each sub-skill is independently testable and reusable. The orchestrator skill handles how they combine. The rendering of charts from specifications is a code/pipeline concern, not a skill concern.

**Example: MLR Claims Review Orchestrator skill**

```
mlr-claims-review (orchestrator skill)
  |-- mlr-claim-extraction (output_type: structured-data)
  |     Extracts individual claims from promotional material.
  |-- mlr-claim-classification (output_type: decision)
  |     Classifies each claim: factual, comparative, efficacy, safety, off-label.
  |-- mlr-source-matching (output_type: structured-data)
  |     Matches each claim to supporting source references.
  |-- mlr-compliance-judgment (output_type: decision)
  |     For each claim: supported / unsupported / requires revision.
  +-- mlr-report-generation (output_type: text)
        Produces the MLR review report with claim-by-claim assessment.
```

---

## 2. Knowledge Base Lifecycle

### 2.1 Three Types of KBs

**Type 1: Structural KB** -- Document format and organization rules

```json
// KB: structural/csr-ich-e3.json
{
  "kb_id": "structural/csr-ich-e3",
  "type": "structural",
  "version": "1.0.0",
  "description": "ICH E3 CSR structure requirements",
  "content": {
    "sections": [
      {
        "number": "11",
        "title": "Usage Results",
        "required": true,
        "subsections": ["11.1 Disposition", "11.2 Duration of Exposure", "11.3 Dose Intensity", "11.4 Dose Modifications", "11.5 Discontinuations"],
        "typical_length_words": "1500-2500",
        "placement": "After Section 10 (Study Population), before Section 12 (Efficacy)"
      }
    ]
  }
}
```

**Type 2: Conventions KB** -- Writing style and domain preferences

```json
// KB: conventions/writing-style-clinical.json
{
  "kb_id": "conventions/writing-style-clinical",
  "type": "conventions",
  "version": "1.2.0",
  "content": {
    "voice": "past tense, third person, passive voice acceptable for methods",
    "numeric_reporting": "Report as 'N (%)' for categorical, 'mean (SD)' or 'median [range]' for continuous",
    "hedging_language": "Use 'appeared to', 'was associated with' -- never causal claims",
    "cross_referencing": "Use 'as described in Section X.Y' -- never repeat data across sections",
    "table_references": "Always cite table number: '(Table 14.1)' -- never refer to tables generically",
    "abbreviations": "Define on first use per section; use standard list from protocol",
    "therapeutic_area_specific": {
      "oncology": {"response_criteria": "RECIST v1.1 terminology", "dosing": "mg/m2 or mg/kg as per protocol"},
      "cardiovascular": {"endpoints": "MACE components spelled out on first use"}
    }
  }
}
```

**Type 3: Corrections KB** -- Learning from manual edits

```json
// KB: corrections/vertex-csr-learnings.json
{
  "kb_id": "corrections/vertex-csr-learnings",
  "type": "corrections",
  "version": "1.5.0",
  "client": "vertex",
  "content": {
    "corrections": [
      {
        "id": "C-001",
        "date": "2026-03-15",
        "section": "11",
        "original": "Median exposure was 24 weeks.",
        "corrected": "Median duration of exposure to study drug was 24.0 weeks (range: 2.1 to 52.3 weeks).",
        "rule_extracted": "Always include range with median exposure. Always specify 'study drug' not just 'exposure'. Use one decimal place for weeks.",
        "applied_to_skill": "mwa-csr-s11-authoring",
        "applied_in_version": "2.1.0"
      }
    ]
  }
}
```

### 2.2 KB vs. Skill: When Does Something Go Where

**Skill**: A structured set of natural language instructions that tells an agent HOW to perform a specific task.

**Knowledge Base (KB)**: A structured collection of reference data, conventions, or corrections that a skill draws upon to produce higher-quality outputs.

| Goes in SKILL | Goes in KB |
|---------------|-----------|
| How to perform the task (steps, structure, rules) | Reference data the task uses (conventions, formats, corrections) |
| Universal to all clients and all documents of this type | May be client-specific or document-type-specific |
| Changes when the approach changes | Changes when domain knowledge updates |
| "Author Section 11 with these subsections..." | "In oncology, report response per RECIST v1.1..." |
| Anti-patterns (what not to do) | Corrections (what to do instead, based on past feedback) |

**Rule of thumb:** If removing it would change WHAT the agent does, it's a skill. If removing it would change HOW WELL the agent does it, it's a KB.

### 2.3 SME Feedback -> KB Corrections

```
1. SME reviews generated output, provides comments
   |
2. QC team receives comments, classifies each:
   |-- a) Factual error -> Fix in source extraction skill + add eval row
   |-- b) Style/convention issue -> Add to Conventions KB
   |-- c) Client-specific preference -> Add to Corrections KB (client-specific)
   +-- d) Out-of-scope -> Log as feature request
   |
3. For (b) and (c): QC drafts KB entry
   |
4. Solution Architect reviews: Is this universal or client-specific?
   |-- Universal -> Add to conventions KB
   +-- Client-specific -> Add to client corrections KB
   |
5. KB version bumped (minor), skill re-tested against eval dataset
   |
6. If eval scores improve or stay same -> merge
   If eval scores drop -> investigate (the correction may conflict with another rule)
```

### 2.4 SME Feedback When SMEs Are Resistant

The process above assumes willing SME participation. In practice, SMEs are often overcommitted, skeptical of AI, or simply not allocated to this work. The following approaches are ordered from lowest to highest SME burden.

**Tier 1: Zero-meeting feedback (SME time: <15 minutes per cycle)**
- Send SME a generated output alongside the manually-authored reference for the same document.
- Ask ONE question: "What is wrong with the generated version?" via email/Teams. Accept bullet points, redlines, or voice notes.
- QC team translates the SME's raw feedback into structured KB entries. SME never sees the KB.

**Tier 2: Structured redline review (SME time: 30-60 minutes per cycle)**
- Send SME 2-3 generated outputs in a tracked-changes document.
- SME reviews using standard "track changes" in Word -- the tool they already use.
- QC team extracts corrections from the tracked changes. No new tool or process for the SME.

**Tier 3: Calibration session (SME time: 1 hour, one-time)**
- Only needed when building the initial eval dataset or when scoring disagreements exceed 15%.
- Frame as: "We need 1 hour of your time to calibrate our quality measurement. After this, we will not need regular meetings -- just periodic redline reviews."

**When SMEs refuse entirely:**
1. Document the refusal and who was asked (this is a risk register item).
2. Fall back to: Solution Architect acts as proxy SME using published guidelines (ICH E3, client SOPs, etc.).
3. Mark all KB entries derived without SME validation with `"sme_validated": false`.
4. Flag these entries for review when an SME eventually becomes available.
5. Set a lower confidence threshold on eval scores for sections without SME validation -- accept 0.80 instead of 0.85 and document the reason.

**Escalation path for persistent SME resistance:**
- SA raises in weekly sync with client project lead.
- If unresolved after 2 weeks: Director raises with client leadership.
- If still unresolved: proceed with proxy SME approach, but the risk is documented in the engagement risk register and communicated to the client in the weekly status.

### 2.5 KB Versioning

KBs version alongside skills in the same git repo:

```
/knowledge-bases/
  /structural/
    csr-ich-e3.json              # v1.0.0
  /conventions/
    writing-style-clinical.json  # v1.2.0
    formatting-tables.json       # v1.0.0
  /corrections/
    vertex-csr-learnings.json    # v1.5.0
    az-mlr-learnings.json        # v1.1.0
    universal-csr-learnings.json # v2.0.0
```

**Version bump triggers:** Same semantic versioning as skills. KB version change triggers re-evaluation of all skills that reference it.

### 2.6 Preventing KB Bloat

- **Quarterly review:** QC team reviews each KB. Entries not referenced by any active skill -> candidate for removal.
- **Deduplication:** If two corrections express the same rule differently, merge them.
- **Graduation:** When a correction has been consistently applied for 3+ months, consider promoting it to the conventions KB (it's no longer a correction -- it's an established convention).
- **Max entries per KB file:** 100. If a corrections KB exceeds 100 entries, split by subsection or topic.

---

## 3. Skills + KB Interaction with Pipeline

### 3.1 How the Orchestrator Discovers and Loads Skills

```
Orchestrator receives task (e.g., "Author CSR Section 11 for Study ABC")
  |
1. Reads orchestration skill (mwa-csr-full-authoring)
2. Orchestration skill lists sub-skills needed
3. For each sub-skill:
   a. Load skill file by skill_id
   b. Check version constraints (min_version from dependency declaration)
   c. Load all KBs declared in skill's dependencies
   d. Inject KB content into agent context alongside skill instructions
4. Spawn agent with: skill instructions + KB content + input documents
```

**Execution mode determines invocation pattern:**
- `single-agent`: One LLM call with skill + KBs + input. Collect output.
- `multi-agent-step`: Feed output of prior step as input. One LLM call per step.
- `orchestrator`: Agent has access to sub-skill catalog and decides which to invoke, in what order, and whether to iterate.

### 3.2 Cascade Testing After Changes

When a skill or KB is modified:

```
1. Identify all skills that depend on the changed artifact
2. Run eval suite for EACH dependent skill (not just the changed one)
3. If any dependent skill's score drops: flag as regression
4. Regression must be resolved before merge (fix dependent skill, or revert the change)
```

### 3.3 Avoiding Conflicts When Multiple People Edit Skills

- **One owner per skill:** Each skill has a designated owner (in metadata). Only the owner can approve changes.
- **Feature branches per skill:** Skill changes happen on branches named `skill/{skill-id}/{change-description}`
- **Lock mechanism:** If auto-refinement is running on a skill, other changes to that skill are blocked until the session completes
- **Merge order:** If two branches modify the same skill, the second to merge must re-run evals on the combined changes

---

## 4. Skills Catalog & Reuse

### 4.1 Catalog Structure

Maintain a `CATALOG.md` at the root of the skills repository:

# Skills Catalog

Last updated: 2026-05-01

## MWA (Medical Writing Automation)
| Skill ID | Name | Version | Status | Owner | Eval Coverage | Last Validated |
|----------|------|---------|--------|-------|--------------|----------------|
| mwa-source-extraction | Source Document Extraction | 1.2.0 | production | Engineer | 92% | 2026-04-28 |
| mwa-csr-s11-authoring | CSR Section 11 Authoring | 2.1.0 | production | Solution Architect | 88% | 2026-05-01 |
| mwa-csr-s12-authoring | CSR Section 12 Authoring | 1.0.0 | testing | Engineer | 75% | 2026-04-20 |

## MLR (Medical-Legal-Regulatory)
| Skill ID | Name | Version | Status | Owner | Eval Coverage | Last Validated |
|----------|------|---------|--------|-------|--------------|----------------|
| mlr-claim-extraction | Claim Extraction | 1.0.0 | testing | Engineer | 80% | 2026-05-03 |
| mlr-claim-classification | Claim Classification | 1.0.0 | draft | Engineer | -- | -- |

## MedCom (Medical Communications)
| Skill ID | Name | Version | Status | Owner | Eval Coverage | Last Validated |
|----------|------|---------|--------|-------|--------------|----------------|
| medcom-narrative-authoring | MedCom Narrative Content | 1.1.0 | production | Engineer | 85% | 2026-04-25 |
| medcom-chart-specification | Chart Specification | 0.9.0 | testing | Engineer | 70% | 2026-04-22 |

## Cross-Product
| Skill ID | Name | Version | Status | Owner | Eval Coverage | Last Validated |
|----------|------|---------|--------|-------|--------------|----------------|
| cross-formatting-finalizer | Document Formatting | 1.1.0 | production | Engineer | 95% | 2026-04-30 |
| cross-source-extraction | Generic Source Extraction | 2.0.0 | production | Engineer | 93% | 2026-05-01 |

Auto-generated from skill metadata on each merge to main.

### 4.2 Adapting a Skill for New Client/Document Type

**Fork (create a new skill)** when:
- The new use case needs a fundamentally different output structure
- More than 40% of the rules would change

**Parameterize (same skill, different KB)** when:
- The structure and rules are the same but conventions differ
- Client-specific formatting or terminology is the only difference

**Example:** CSR Section 11 skill is universal. Vertex wants exposure reported in person-years instead of weeks. Don't fork the skill -- add a Vertex corrections KB entry: `"exposure_metric": "person-years"` and add a rule in the skill: "Check corrections KB for client-specific exposure metric preference."

---

## 5. Converting Existing SOPs/Prompts to Skills

*Note: This conversion process is currently in exploration. The approach described below is the suggested methodology and may be refined as the team gains experience with the migration workflow.*

### 5.1 Step-by-Step Migration

```
1. INVENTORY: List all existing SOPs and prompt files across all platforms
   - Location: project folders, S3, Cursor workspaces, Slack messages (yes, some live there)
   - For each: document type, product area, last used date, current owner
   |
2. CLASSIFY each SOP/prompt:
   |-- a) Active and working -> Convert to skill
   |-- b) Active but poor quality -> Convert + improve as part of migration
   |-- c) Inactive / replaced -> Do not convert, archive
   +-- d) Partially relevant -> Extract reusable parts, discard rest
   |
3. For each item to convert:
   a. Read the existing SOP/prompt thoroughly
   b. Separate into: task instructions (-> skill), domain conventions (-> KB),
      client-specific rules (-> corrections KB)
   c. Rewrite in skill template format (frontmatter, objective, inputs,
      structure, rules, anti-patterns)
   d. Identify: what was implicit knowledge in the SOP author's head?
      Document it explicitly. (See 5.3 for a structured approach.)
   e. Set execution_mode and output_type based on the task characteristics
   f. Create minimum eval dataset (5 rows) from existing test cases
      or production outputs
   g. Test the new skill against the eval dataset
   h. Compare output quality: new skill vs. old SOP
   i. If quality matches or improves -> approve migration
   j. If quality drops -> identify what was lost in translation, fix the skill
   |
4. Mark old SOP as "migrated to skill:{skill-id}" -- do not delete
```

### 5.2 Common Migration Pitfalls

| Pitfall | Symptom | Fix |
|---------|---------|-----|
| Implicit knowledge lost | Skill produces technically correct but contextually wrong output | Interview the person who wrote the SOP; add their tacit knowledge as explicit rules (see 5.3) |
| Over-specification | Skill is 4000 words and agent gets confused | Split into orchestration skill + sub-skills |
| Under-specification | Skill says "write appropriately" -- agent interprets differently each time | Add concrete examples and anti-patterns |
| Mixed concerns | Skill contains both instructions AND client data | Separate into skill (instructions) + KB (data/conventions) |
| Wrong execution_mode | Skill written as single-agent but task actually requires iteration or tool use | Re-evaluate using the Complexity Ladder; restructure if needed |
| Prompt-specific tricks lost | Old prompt relied on model-specific behavior (e.g., "think step-by-step" hacks) | Identify the underlying need (e.g., the task requires intermediate reasoning) and express it as a structural rule, not a prompt trick |

### 5.3 Extracting Implicit Knowledge

The hardest part of SOP-to-skill migration is capturing knowledge that exists in the SOP author's head but is not written down. Use this structured interview approach:

**Interview template (30-45 minutes with the SOP author or regular user):**

1. "Walk me through how you use this SOP on a real document. What do you do that is NOT written in the SOP?"
2. "When a new person uses this SOP for the first time, what mistakes do they always make?"
3. "What judgment calls does this task require? Where do you think, 'It depends...'?"
4. "Show me an output you are proud of and one that needed significant rework. What made the difference?"
5. "Are there shortcuts or checks you do that are not in the SOP? Things you just 'know' to do?"
6. "If a client pushed back on an output from this SOP, what did they complain about?"

**What to do with the answers:**
- Answers to Q1, Q5: Add as explicit rules in the skill.
- Answers to Q2: Add as anti-patterns in the skill.
- Answers to Q3: Add as conditional rules or KB entries (with decision criteria).
- Answers to Q4: Use as eval dataset rows (the good output as reference, the bad one as a negative example).
- Answers to Q6: Add as corrections KB entries.

### 5.4 Migration Timeline

For a product area with 10-15 existing SOPs/prompts:
- Inventory and classification: 1 day
- Implicit knowledge interviews (3-4 key SOPs): 2 days
- Migration of 3-4 core skills (highest value): 1 week
- Eval dataset creation for migrated skills: 1 week (parallel)
- Testing and refinement: 1 week
- Remaining skills: 2-3 weeks
- **Total: 5-7 weeks for full migration of one product area**

Prioritize by: frequency of use x quality impact x reuse potential

### 5.5 MedCom Pilot Migration Checklist

*Note: This checklist is currently in exploration and is provided as a suggested starting point. It will be refined based on actual pilot experience.*

MedCom is the designated pilot track. This checklist is specific to the MedCom migration.

```
Week 1: Inventory and Planning
  [ ] List all MedCom SOPs, prompts, and templates currently in use
  [ ] Classify each (active/inactive, convert/archive)
  [ ] Conduct implicit knowledge interviews with 2 primary MedCom users
  [ ] Identify which MedCom tasks produce text-only vs. multi-modal outputs
  [ ] Draft skill map: which skills are needed, which can be reused from MWA

Week 2: Core Skill Migration
  [ ] Migrate the highest-value MedCom authoring SOP to skill format
  [ ] Create MedCom conventions KB (style, terminology, formatting preferences)
  [ ] Create minimum eval dataset (5 rows) for the migrated skill
  [ ] Run initial eval; record baseline score
  [ ] Identify if multi-modal composition is needed (see 1.12)

Week 3: Testing and Expansion
  [ ] Run 1-2 auto-refinement sessions on the pilot skill (with SA observing)
  [ ] Migrate 2-3 additional MedCom skills
  [ ] Expand eval dataset to 10-15 rows
  [ ] Test skills in pipeline integration

Week 4-5: Validation and Handoff
  [ ] Run full eval suite on all migrated skills
  [ ] Get SME/QC review on 5 generated outputs (Tier 3 review)
  [ ] Document lessons learned for the next product area migration
  [ ] Present results in sprint review
```

---

## 6. Naming Conventions and Repository Organization

### 6.1 Skill Naming Convention

```
{product-area}-{task-type}-{specifics}
```

| Component | Values | Examples |
|-----------|--------|---------|
| product-area | `mwa`, `mlr`, `medcom`, `cross` | `cross` for skills shared across products |
| task-type | `authoring`, `extraction`, `classification`, `validation`, `formatting`, `review`, `orchestration` | Verb-based, describes what the skill does |
| specifics | Free-form, hyphenated, descriptive | `csr-s11`, `claim-compliance`, `visual-layout` |

**Examples:**
- `mwa-authoring-csr-s11` -- MWA, authoring task, CSR Section 11
- `mlr-classification-claim-type` -- MLR, classification task, claim type
- `medcom-extraction-data-for-charts` -- MedCom, extraction task, chart data
- `cross-validation-cross-reference` -- Cross-product, validation, cross-references
- `mwa-orchestration-csr-full` -- MWA, orchestration, full CSR assembly

**Rules:**
- All lowercase, hyphen-separated.
- No abbreviations beyond the standard product area codes (mwa, mlr, medcom, cross).
- Maximum 50 characters for the skill_id.
- The `name` field in frontmatter is the human-readable version (can include spaces, capitalization).

### 6.2 KB Naming Convention

```
{type}/{scope}-{subject}.json
```

| Component | Values | Examples |
|-----------|--------|---------|
| type | `structural`, `conventions`, `corrections` | Directory-level organization |
| scope | `universal`, client name, or product area | `universal`, `vertex`, `az`, `mwa`, `mlr` |
| subject | Free-form, hyphenated | `csr-ich-e3`, `writing-style-clinical`, `mlr-learnings` |

**Examples:**
- `structural/universal-csr-ich-e3.json`
- `conventions/universal-writing-style-clinical.json`
- `corrections/vertex-csr-learnings.json`
- `conventions/mlr-promotional-language.json`

### 6.3 Repository Layout

```
/skills/
  /mwa/
    orchestration-csr-full.md
    authoring-csr-s10.md
    authoring-csr-s11.md
    authoring-csr-s12.md
    extraction-source-tfl.md
  /mlr/
    orchestration-claims-review.md
    extraction-claim.md
    classification-claim-type.md
    review-compliance.md
  /medcom/
    orchestration-visual-asset.md
    authoring-narrative.md
    extraction-data-for-charts.md
    specification-chart.md
  /cross/
    validation-cross-reference.md
    formatting-finalizer.md
    extraction-source-generic.md
/knowledge-bases/
  /structural/
  /conventions/
  /corrections/
/eval-datasets/
  /mwa/
  /mlr/
  /medcom/
/archive/
  /skills/
  /knowledge-bases/
CATALOG.md
```

**Organizational rules:**
- Skills are organized by product area first, then by function.
- Within a product area directory, skills are named without the product area prefix (to avoid redundancy with the directory).
- The CATALOG.md uses the full `skill_id` (with product area prefix) for unambiguous reference.
- Archived skills and KBs retain their original directory structure under `/archive/`.

---

## 7. Cross-Reference Index

This section maps where Skills/KB lifecycle concerns are addressed across the WoW document suite. Use this to find related processes without duplicating content.

| Topic | Primary Document | Related Sections |
|-------|-----------------|-----------------|
| How to create eval datasets for a new skill | [Eval Dataset Lifecycle, Section 1](./Granular_Eval_Dataset_Lifecycle.md#1-creation) | This doc: 1.3 step 6, 5.1 step 3e |
| How eval gates block deployment | [Build, Test & Deploy, Section 2](./Granular_Build_Test_Deploy.md#2-testing-strategy-3-tier) | This doc: 1.3 step 9 |
| How auto-refinement sessions are budgeted | [Build, Test & Deploy, Section 5](./Granular_Build_Test_Deploy.md#5-cost-management) | This doc: 1.7 session limits |
| How skills are versioned across environments | [Build, Test & Deploy, Section 3.2](./Granular_Build_Test_Deploy.md#32-version-management) | This doc: 1.5 |
| How solutioning decides skill architecture | [Solutioning & Requirements, Section 2](./Granular_Solutioning_Requirements.md#2-solutioning-workshop-process) | This doc: 1.11 (execution modes) |
| How the Complexity Ladder applies to skill design | [Solutioning & Requirements, Section 2.4](./Granular_Solutioning_Requirements.md#24-complexity-ladder) | This doc: 1.11 |
| How SME feedback flows into KBs | This doc: 2.3, 2.4 | [Eval Dataset Lifecycle, Section 5.1](./Granular_Eval_Dataset_Lifecycle.md#51-sme-feedback) |
| How cascade testing works after KB changes | This doc: 3.2 | [Build, Test & Deploy, Section 2](./Granular_Build_Test_Deploy.md#2-testing-strategy-3-tier) |
| How client-specific KBs are created during onboarding | [Solutioning & Requirements, Section 1.3](./Granular_Solutioning_Requirements.md#13-client-onboarding) | This doc: 2.1 (Type 3), 4.2 |
| How production monitoring detects skill quality drift | [Build, Test & Deploy, Section 4](./Granular_Build_Test_Deploy.md#4-production-monitoring) | This doc: 1.7 (triggers for auto-refinement) |
| How new team members learn about skills | [Cross-Cutting Operations, Section 3.3](./Granular_Cross_Cutting_Operations.md#33-onboarding-guide) | This doc: 4.1 (catalog as entry point) |
