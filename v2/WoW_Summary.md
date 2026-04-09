# Ways of Working — Executive Summary

## What This Is

This portal contains the complete operational framework for the GenAI team. It defines how the team takes a problem from requirements through solutioning, build, test, deployment, and ongoing operations — with quality gates at every stage.

The framework was developed collaboratively by the full team and is designed to be the single source of truth for how we work.

## Why We Built This

The team needed to move from reactive, ad-hoc delivery to a structured, repeatable process that produces measurable quality outcomes. Specifically:

- **Quality was subjective.** Outputs were reviewed by eyeballing on Slack, with no systematic evaluation. We now define quality upfront using golden datasets and score every output against agreed rubrics.
- **Testing consumed most of the time.** An estimated 80% of effort went to manual testing. We now use a 3-tier automated testing strategy (programmatic checks, LLM-as-Judge, human review) to catch issues early and cheaply.
- **POCs went straight to production.** Proof-of-concepts were shipped to clients without proper productionization. We now have explicit gates and a "Production Readiness Assessment" that makes the gap visible.
- **No reuse across engagements.** Every engagement started from scratch. We now build reusable skills, knowledge bases, and eval datasets that make each subsequent engagement faster.
- **Process varied by person.** How work got done depended on who was doing it. We now have a documented, role-based process that works regardless of who fills the role.

## How It Is Structured

The framework has **3 layers**:

| Layer | What It Defines | Changes When |
|-------|----------------|-------------|
| **Lifecycle Process** | The stages, gates, roles, and decisions — the "what and when" | Rarely — this is the stable spine |
| **Technical Playbooks** | Framework-specific guidance (Claude Agent SDK, Strands, etc.) — the "how" | When the team adopts a new framework |
| **Templates & Artifacts** | Eval rubrics, skill files, handoff packages — the "evidence" | Every engagement, continuously improving |

## The 6-Stage Lifecycle

Every piece of work flows through some or all of these stages:

| Stage | Purpose | Key Output |
|-------|---------|-----------|
| **0. Intake & Classification** | Classify the work and determine which stages apply | Engagement type (A through F) and owner assigned |
| **1. Requirement & Scoping** | Define the problem, build the golden dataset plan, agree on quality measurement | Signed-off evaluation rubric |
| **2. Solutioning Workshop** | Design the architecture, decide complexity level, identify skills needed | Architecture decision record |
| **3. Build & Test** | Build skills and KBs, run eval suites, iterate until quality gates pass | Passing eval scores at agreed threshold |
| **4. Deploy & Validate** | Move to production with safeguards, monitoring, and rollback capability | Live system with monitoring |
| **5. Operate & Evolve** | Hand off to operations, maintain quality, feed learnings back into the system | Complete handoff package |

**Not every request needs all 6 stages.** Engagement typing at intake scales the process: a new product goes through everything; a bug fix is fast-tracked through fix → eval → deploy.

## Core Concepts

| Concept | What It Means |
|---------|--------------|
| **Golden Dataset** | A curated set of input-output pairs scored on defined quality dimensions. This is how we define and measure "good." The client signs off on the rubric, not the solution. |
| **Skill** | A markdown file that instructs an AI agent on how to perform a specific task. Skills are the atomic unit of capability — reusable across engagements. |
| **Knowledge Base (KB)** | Reference data that a skill draws upon: document structure rules (structural), writing conventions (conventions), or learnings from past corrections (corrections). |
| **3-Tier Testing** | Every change goes through: (1) automated code checks at $0, (2) LLM-as-Judge eval on 5 rows at ~$2, (3) weekly human review by the QC team. |
| **Auto-Refinement** | An AI agent that identifies eval failures, proposes skill modifications, tests them, and iterates — with guardrails (max 5 changes, $50 cap, human review required). |
| **Engagement Typing** | Classification (A through F) that determines how much process a request needs. Prevents over-engineering small changes while maintaining rigor for large ones. |

## Key Roles

| Role | Primary Responsibility |
|------|----------------------|
| **Solution Architect** | Owns engagement quality end-to-end: requirements, solutioning, skill writing, client communication |
| **Engineer** | Owns infrastructure, code review, deployment pipeline, eval tooling, merge authority |
| **QC/Testing** | Owns eval dataset creation, scoring calibration, Tier 3 human review, data quality |
| **GenAI Solution Approvers** | Senior review authority for solution design, architecture decisions, and quality thresholds |

## Time Allocation

| State | Delivery | Building | Learning |
|-------|----------|----------|----------|
| **Current reality** (until leadership approves) | 85% | 15% | — |
| **Target** | 60% | 30% | 10% |

The path from 85/15 to 60/30/10 runs through proving the WoW works on the MedCom pilot, then presenting proof points to leadership.

## How to Navigate This Portal

| If You Want To... | Start With |
|-------------------|-----------|
| Understand the full lifecycle and architecture | Master Framework |
| Gather requirements or run a solutioning workshop | Solutioning & Requirements |
| Create or maintain evaluation datasets | Evaluation Datasets |
| Write, version, or improve skills and KBs | Skills & Knowledge Bases |
| Understand the build/test/deploy pipeline | Build, Test & Deploy |
| Learn about team communication, sprints, and stakeholder management | Cross-Cutting Operations |
| Understand what the team needs to learn | Upskilling Plan |
