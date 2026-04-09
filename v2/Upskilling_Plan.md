# Upskilling Plan

This document outlines what every team member needs to learn for the Ways of Working to function. The plan is organized by role because different roles have different gaps. Everyone should complete the "All Team Members" section first.

---

## 1. All Team Members

These are foundational topics that everyone on the team must be comfortable with, regardless of role.

### 1.1 The WoW Process Itself

| Topic | What to Learn | How to Learn | Time |
|-------|--------------|-------------|------|
| 6-stage lifecycle | What happens at each stage, what the gates require, what evidence is produced | Read the Master Framework document in this portal | 1 hour |
| Engagement typing | How to classify work as Type A through F, and which stages apply to each | Read Solutioning & Requirements, Section 1.5 | 30 min |
| RACI framework | Which role is Responsible, Accountable, Consulted, or Informed for each activity | Read Master Framework, Part 5 | 30 min |
| Quality culture | "Eval failures are data, not blame." How the team treats quality, shows failures, and defines "good enough" before starting | Read Cross-Cutting Operations, Section 7 | 20 min |

### 1.2 GenAI and Agentic Concepts

| Topic | What to Learn | Why It Matters | Resources |
|-------|--------------|---------------|-----------|
| What an LLM is and is not | Probabilistic generation, hallucination risk, non-determinism, context windows, token costs | Every team member explains AI to clients and makes quality judgments about AI outputs | Anthropic documentation, internal tech talks |
| Skills and Knowledge Bases | What a skill file is, what a KB is, how they relate, the three KB types (structural, conventions, corrections) | Skills and KBs are the core IP the team builds. Everyone reads, writes, or reviews them. | Read Skills & KB Lifecycle, Sections 1.1 and 2.1-2.2 |
| The Complexity Ladder | Simple chain → Router → Parallel → Agent → Multi-agent. When each is appropriate and the default presumption (simplest level that works) | Prevents over-engineering. Everyone participates in solutioning workshops where this is the primary decision framework. | Read Solutioning & Requirements, Section 2.4 |
| Evaluation-driven development | Golden datasets, scoring dimensions, LLM-as-Judge, the 3-tier testing strategy | Quality is measured, not felt. Everyone must understand how quality is defined and tracked. | Read Evaluation Datasets, Sections 1-3 |
| Auto-refinement | How AI modifies skills based on eval failures, the guardrails (5 modifications, $50 cap, human review) | This is a key productivity lever. Solution Architects run it, Engineers build the tooling, QC reviews the results. | Read Skills & KB Lifecycle, Section 1.7 |
| Cost awareness | Model tiering (Haiku/Sonnet/Opus), cost per call, why not everything should use Opus, cost tracking basics | Every team member's work has API cost implications. A skill that triggers 10 Opus calls when 2 Sonnet calls would suffice costs 10x more. | Read Build, Test & Deploy, Section 6 |

### 1.3 Pharma Domain Basics

| Topic | What to Learn | Who Needs It Most |
|-------|--------------|------------------|
| ICH E3 guideline structure | What a CSR is, what sections it contains, what each section covers | Everyone working on MWA |
| MLR review process | What Medical-Legal-Regulatory review is, why promotional materials need source annotations | Everyone working on MLR or MedCom |
| GxP, 21 CFR Part 11, Annex 11 | What regulated systems mean in pharma, validation requirements, audit trail obligations | Solution Architects and Engineers |
| Data classification and patient privacy | Why patient-level data cannot be sent to third-party APIs, de-identification requirements | Everyone handling client data |

---

## 2. Non-Engineers: Solution Architects and QC/Testing

This is the largest upskilling area. The WoW assumes non-engineers contribute skill files, KB entries, and eval datasets through a Git-based workflow. Most team members are new to this toolchain.

### 2.1 Git Fundamentals

**Why this matters:** Every skill, KB, and eval dataset lives in a Git repository. Every change goes through a branch → commit → push → PR → review → merge workflow. Without Git fluency, non-engineers cannot contribute independently.

| Topic | What to Learn | Practice Exercise |
|-------|--------------|------------------|
| What Git is | Version control concepts: repository, commit, branch, merge. Why we use it (history, collaboration, rollback). | Watch a 20-min Git intro video, then explain the concepts back to a partner |
| The 5 essential commands | `git pull`, `git checkout -b`, `git add`, `git commit`, `git push` — what each does and when to use it | Complete the guided walkthrough in the sandbox repo (mandatory before first PR) |
| Branch naming | `feature/`, `fix/`, `skill/`, `kb/`, `eval/` prefixes. One branch per change. Never commit to main directly. | Create 3 branches with correct naming in the sandbox |
| Commit messages | Short, descriptive messages: "skill: add exposure interpretation rule to S11" not "update file" | Write 5 commit messages for hypothetical changes and get engineer feedback |
| What NOT to do | Never `git push --force`. Never resolve merge conflicts on code files yourself. Never edit on `main`. If confused, ask an engineer. | Read the "Common mistakes and fixes" table in Build, Test & Deploy, Section 1.2 |

**Learning format:** 30-minute guided walkthrough with an engineer using a sandbox repository. This is mandatory before contributing the first PR.

### 2.2 GitHub and Pull Requests

| Topic | What to Learn | Practice Exercise |
|-------|--------------|------------------|
| What a PR is | A request to merge your changes into the main codebase. It shows what changed, why, and includes eval results. | Open a practice PR in the sandbox repo |
| The PR template | How to fill in: what changed, type of change, eval results, testing done, checklist items | Fill in the template for a hypothetical skill change |
| Code review basics | How to read review comments, respond to feedback, push follow-up commits. Reviews are collaborative, not adversarial. | Review a sample PR and leave 2 comments |
| CODEOWNERS | Who must approve which types of changes. Skill changes need SA + Engineer. Code changes need Engineer only. | Read the CODEOWNERS file and identify who reviews your files |
| PR status checks | What "checks passing" and "checks failing" mean. Tier 1 (automated) and Tier 2 (eval) checks run automatically. | Submit a PR with a deliberate error and observe the check failure |

### 2.3 Running Evals Locally

| Topic | What to Learn | Practice Exercise |
|-------|--------------|------------------|
| Command line basics | Opening a terminal, navigating directories (`cd`, `ls`), running Python scripts | Navigate to the project directory and list files |
| Running quick eval | `python run_eval.py --dataset [name] --mode quick` — what the output means, how to read per-dimension scores | Run a quick eval on an existing dataset and interpret the results |
| Running single-row eval | `python run_eval.py --dataset [name] --row [id] --verbose` — for debugging a specific failure | Debug a failing row: read the verbose output, identify which dimension failed and why |
| Interpreting eval results | What each score means, what "PASS/FAIL" on data accuracy means, when a score is concerning vs. acceptable | Score 3 sample outputs manually, then compare to LLM-as-Judge scores |

### 2.4 Cursor / Claude Code for Skill Editing

| Topic | What to Learn | Practice Exercise |
|-------|--------------|------------------|
| Opening and editing files | Open a skill file in Cursor, navigate to the rules section, make an edit | Edit a skill file to add one new rule |
| Using AI assistance | Ask Cursor's AI chat to help draft a rule, review the suggestion for domain accuracy, then accept or modify | Draft a new anti-pattern entry using Cursor's AI, validate it yourself |
| The end-to-end workflow | Pull latest → create branch → edit skill → run local eval → commit → push → create PR | Complete one full cycle on a sandbox skill file |
| What not to do | Don't modify `.py` files, import statements, CI configs, or Dockerfiles. Don't resolve merge conflicts on code. | Read the "What non-engineers should NOT do" list in Build, Test & Deploy, Section 1.5 |

### 2.5 Markdown and JSON Basics

| Topic | What to Learn | Why |
|-------|--------------|-----|
| Markdown syntax | Headings (`##`), bold (`**`), lists (`-`), code blocks, tables | Skill files are written in Markdown |
| Skill file frontmatter | The YAML metadata block at the top of every skill: `skill_id`, `version`, `dependencies`, `eval_dataset`, `status` | Every skill change requires updating the frontmatter |
| JSON structure | Objects `{}`, arrays `[]`, key-value pairs, proper quoting. How to validate JSON. | KB files and eval datasets are JSON |
| Common JSON errors | Missing commas, trailing commas, unmatched brackets, wrong quotes | Tier 1 checks will catch these, but fixing them yourself is faster |

### 2.6 CI/CD Concepts

Non-engineers don't need to build CI/CD pipelines, but they need to understand what happens after they push code.

| Concept | What to Know |
|---------|-------------|
| Continuous Integration | When you push to a branch, automated checks run on your changes. If they fail, the PR is blocked. |
| Tier 1 checks | Syntax validation, schema checks, secrets detection. Run in ~30 seconds, cost $0. If these fail, you have a formatting or structural error. |
| Tier 2 checks | LLM-as-Judge runs the eval on 5 rows. Takes 5-10 minutes, costs ~$2. If these fail, your skill change may have degraded quality. |
| What "checks passing" means | A green checkmark on your PR means automated tests passed. A red X means something failed — read the details to understand what. |
| What to do when checks fail | For Tier 1: fix the formatting/schema issue. For Tier 2: check if the eval failure is from your change or pre-existing. If stuck, ask an engineer. |

---

## 3. Engineers

Engineers are already comfortable with Git, CI/CD, and code. Their upskilling focuses on the GenAI-specific aspects of the WoW.

### 3.1 Skill File Ecosystem

| Topic | What to Learn | Practice Exercise |
|-------|--------------|------------------|
| Skill file anatomy | Frontmatter metadata, objective, input requirements, output structure, rules, anti-patterns. What makes a good skill vs. a bad skill. | Read 5 production skill files. Identify which patterns from the "Good vs. Bad" table each follows or violates. |
| Skill dependencies and composition | Sequential chains, parallel fan-out, gather/merge, conditional branch, iterative refinement. When to split vs. keep monolithic. | Map the dependency tree for one product area's skills |
| Execution modes | `single-agent`, `multi-agent-step`, `orchestrator` — when each applies and how the pipeline invokes each differently | Categorize 10 existing skills by execution mode |
| KB types and interaction | How skills reference KBs, how structural/conventions/corrections KBs serve different purposes, cascade testing after KB changes | Create a test corrections KB entry and observe how it affects skill output |

### 3.2 Eval Infrastructure

| Topic | What to Learn | Practice Exercise |
|-------|--------------|------------------|
| Eval dataset schema | The JSON structure, scoring dimensions, row metadata, hold-out sets | Create a 5-row eval dataset for a new skill |
| LLM-as-Judge setup | Writing judge prompts, calibrating against human scores, handling non-determinism (temperature 0, multiple runs) | Write a judge prompt for a new scoring dimension, calibrate on 10 rows |
| CI/CD integration | Setting up GitHub Actions for Tier 1 and Tier 2 checks, storing API keys in GitHub Secrets, posting results to PRs | Implement the Phase 1 CI workflow (Tier 1 checks) |
| Cost tracking | Tagging LLM calls with project/client/skill metadata, building the daily summary script, threshold-based alerting | Build a structured logging wrapper for API calls |

### 3.3 Pharma-Specific Engineering

| Topic | What to Learn | Why |
|-------|--------------|-----|
| Audit trail requirements | What must be logged per production run (input manifest, skill versions, KB versions, model version, traces) | Pharma clients may need to demonstrate provenance of AI-generated content to regulators |
| Data handling | De-identification requirements, client data segregation, what can and cannot be sent to LLM APIs | Mishandling client data is a compliance and trust risk |
| Model version pinning | Why "latest" is never acceptable, how to manage model upgrades as deployments, fallback model configuration | Model changes can silently degrade quality in a regulated domain |
| Retention policies | 7-year minimum retention for pharma data, S3 versioning, deletion protection | Data deletion in pharma is a compliance violation |

### 3.4 Supporting Non-Engineers

| Topic | What to Learn |
|-------|-------------|
| Running the sandbox walkthrough | How to guide a non-engineer through their first Git workflow in the sandbox repo |
| Reviewing skill/KB PRs | How to review domain content changes (not just code quality) — check eval results, not just syntax |
| Handling the common mistakes | How to rescue someone who committed to main, resolve their merge conflicts, move changes to the right branch |
| Building self-service tooling | What tools would reduce engineer-in-the-loop time: Streamlit eval dashboards, PR template automation, local eval runners |

---

## 4. QC/Testing Team

The QC team's role is central to the WoW — they own eval datasets, scoring calibration, and weekly human review.

### 4.1 Eval Dataset Mastery

| Topic | What to Learn | Practice Exercise |
|-------|--------------|------------------|
| Dataset creation end-to-end | Source identification, input-output pair creation, scoring dimension definition, calibration | Create a 5-row Minimum Viable Eval Dataset following the bootstrapping guide |
| Scoring calibration | Independent scoring, inter-rater reliability, calibration meetings, rubric refinement when wording is ambiguous | Score 5 outputs independently, compare with another scorer, calibrate disagreements |
| Edge case identification | What makes a good edge case, coverage analysis (therapeutic areas, complexity levels, study phases), gap identification | Review an existing dataset and propose 3 new edge case rows |
| Dataset maintenance | When to add rows (production failure, new client, refinement plateau), when to retire rows, versioning (major/minor/patch) | Process a mock client feedback item into a new eval dataset row |

### 4.2 Tier 3 Human Review

| Topic | What to Learn | Practice Exercise |
|-------|--------------|------------------|
| The weekly review process | Sampling 10 outputs (3 easy, 4 medium, 3 hard), blind scoring (without seeing LLM scores), comparison with LLM-as-Judge | Run one complete Tier 3 review cycle |
| Failure pattern identification | Classifying new failure patterns, writing them up for the weekly quality report, converting them into new eval rows | Identify 3 failure patterns from a set of 10 outputs and draft eval rows |
| LLM-Judge calibration | Comparing human vs. LLM scores, identifying systematic biases (leniency, positional, length), recommending judge prompt adjustments | Analyze score divergence across 20 outputs and report findings |

### 4.3 Client Feedback Processing

| Topic | What to Learn | Practice Exercise |
|-------|--------------|------------------|
| Feedback classification | Factual error → eval row, missing content → eval row, style preference → corrections KB, out-of-scope → feature request | Classify 10 sample client comments into the 4 categories |
| KB entry writing | How to write a corrections KB entry: original text, corrected text, extracted rule, linked skill | Write 3 corrections KB entries from redline feedback |
| SME interaction | Tier 1 (zero-meeting feedback), Tier 2 (structured redline), Tier 3 (calibration session) — adapting to SME availability | Role-play the "ask for 3 examples + 1-hour calibration" conversation |

### 4.4 Git for QC

Same as Section 2.1-2.2 above. QC team members need the same Git and GitHub fundamentals as Solution Architects.

---

## 5. Upskilling Delivery Plan

### 5.1 Suggested Schedule

| Week | Focus | Who | Format |
|------|-------|-----|--------|
| **Week 1** | WoW process overview (all team). Git sandbox walkthrough (non-engineers, mandatory). | All | 1-hour group session + 30-min per-person sandbox walkthrough with engineer |
| **Week 2** | Skill files and KB deep-dive. Eval dataset creation exercise. | All | Tech talk (45 min) + hands-on exercise (2 hours) |
| **Week 3** | End-to-end PR workflow practice. Cursor/Claude Code for skill editing. | Non-engineers | Paired session with engineer (1 hour per person) |
| **Week 3** | Eval infrastructure setup. CI/CD pipeline for Tier 1 checks. | Engineers | Engineering sprint work |
| **Week 4** | Eval dataset creation (first real dataset from MedCom pilot). Scoring calibration exercise. | QC + Solution Architects | Workshop (3 hours) |
| **Week 5** | First auto-refinement session (SA observes, engineer runs tooling). | Solution Architects + Engineers | Live session (2 hours) |
| **Week 6** | First Tier 3 human review cycle. First complete PR from a non-engineer through the full process. | QC team + all non-engineers | Structured review (2 hours) + async PR cycle |

### 5.2 Proficiency Milestones

**By end of Week 2, every team member should be able to:**
- [ ] Explain the 6-stage lifecycle and engagement typing
- [ ] Describe what a skill file and KB are, and how they differ
- [ ] Explain the 3-tier testing strategy

**By end of Week 4, non-engineers should be able to:**
- [ ] Create a branch, make a change, commit, push, and open a PR
- [ ] Run a quick eval locally and interpret the results
- [ ] Edit a skill file in Cursor and update the frontmatter

**By end of Week 4, engineers should be able to:**
- [ ] Read and understand a skill file well enough to review it
- [ ] Set up and run the eval pipeline locally
- [ ] Implement Tier 1 CI checks in GitHub Actions

**By end of Week 6, QC team should be able to:**
- [ ] Create a 5-row Minimum Viable Eval Dataset independently
- [ ] Run a Tier 3 human review cycle end-to-end
- [ ] Classify client feedback and route it correctly (eval row, KB entry, or feature request)

### 5.3 Ongoing Learning

| Activity | Frequency | Who |
|----------|-----------|-----|
| Monthly tech talk | Monthly | Rotating presenter from the team |
| Monthly landscape scan | Monthly | Rotating — 2 hours reviewing industry updates, 1-page summary to team |
| Individual learning plan | Quarterly | Each person identifies one area to develop, discussed with manager |
| External course / conference | Quarterly (1 per person per quarter) | Pre-approved by the Director |
| Tool trial | As needed (time-boxed to 1 week) | One person evaluates, reports back to team |

---

## 6. Learning Resources

### Git and GitHub

| Resource | Format | For Whom |
|----------|--------|----------|
| GitHub's "Git Handbook" | Web guide | Non-engineers — start here |
| "Oh Shit, Git" (ohshitgit.com) | Quick reference | Everyone — for when things go wrong |
| Internal sandbox repo walkthrough | Live session with engineer | Non-engineers — mandatory |
| Build, Test & Deploy doc, Sections 1.1-1.5 | This portal | Everyone — the team's specific Git workflow |

### Evaluation and Quality

| Resource | Format | For Whom |
|----------|--------|----------|
| Evaluation Datasets doc in this portal | This portal | Everyone — especially Sections 1 (creation) and 3 (scoring) |
| Anthropic's guide to evals | Web guide | Engineers and Solution Architects |
| Internal eval dataset creation exercise | Hands-on workshop | QC team and Solution Architects |

### Agentic AI and Prompt Engineering

| Resource | Format | For Whom |
|----------|--------|----------|
| Anthropic's prompt engineering guide | Web guide | Everyone |
| Claude Agent SDK documentation | Technical docs | Engineers |
| Solutioning doc, Section 2.4 (Complexity Ladder) | This portal | Everyone — especially Solution Architects |
| Skills & KB Lifecycle doc, Section 1 | This portal | Everyone who writes or reviews skills |

### Pharma Domain

| Resource | Format | For Whom |
|----------|--------|----------|
| ICH E3 guideline (condensed version) | PDF | Everyone on MWA |
| Internal onboarding org-context doc | Git repo (`/onboarding/org-context.md`) | New team members |
| Pharma-specific requirements checklist | This portal (Solutioning doc, Section 1.7) | Solution Architects |
