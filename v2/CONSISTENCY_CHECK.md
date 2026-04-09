# WoW v2 Suite -- Cross-Document Consistency Check

*Generated 8 April 2026. Covers all 8 documents in `/home/tanmay/Ways of Working/v2/`.*

---

## Issue 1: All cross-references in WoW_Proposed_Approach.md point to `../v1/` instead of same-directory v2 files

**Documents affected:** WoW_Proposed_Approach.md (64 occurrences)

**What is wrong:** Every internal link in the master framework document uses the path `../v1/Granular_*.md`. Since these documents live in `/v2/`, the links resolve to the older v1 copies, not the current v2 versions.

Example (line 17):
> `[Granular: Solutioning & Requirements](../v1/Granular_Solutioning_Requirements.md)`

**Correction:** Change all 64 `../v1/` path prefixes to `./` (same-directory relative links). For example:
`[Granular: Solutioning & Requirements](./Granular_Solutioning_Requirements.md)`

The same applies to the two supporting-doc links on lines 27-28 (`../v1/WoW_Comprehensive_Analysis.md` and `../v1/WoW_Gap_Analysis.md`).

**File to change:** WoW_Proposed_Approach.md

---

## Issue 2: Tech Talk cadence mismatch -- Proposed Approach says "Bi-weekly", Cross-Cutting Operations says "Monthly"

**Documents affected:** WoW_Proposed_Approach.md, Granular_Cross_Cutting_Operations.md

**Conflicting text:**

WoW_Proposed_Approach.md (line 504):
> `| Tech talk | Bi-weekly (alternates with sprint review) | Deep-dive by one team member |`

Granular_Cross_Cutting_Operations.md (line 14):
> `| **Tech Talk** | Monthly, last Friday | 45 min | Full team | Knowledge sharing | ...`

Cross-Cutting Ops (line 23) explicitly explains the downgrade:
> "Tech talks are monthly, not bi-weekly. Bi-weekly was aspirational but unsustainable alongside delivery."

**Correction:** The Cross-Cutting Operations document has the considered, final decision. Change line 504 of WoW_Proposed_Approach.md from "Bi-weekly (alternates with sprint review)" to "Monthly, last Friday" and update the description to "45-min deep-dive by one team member."

**File to change:** WoW_Proposed_Approach.md

---

## Issue 3: Cross-Cutting Operations section numbers off by one in Proposed Approach cross-references

**Documents affected:** WoW_Proposed_Approach.md, Granular_Cross_Cutting_Operations.md

**What happened:** Cross-Cutting Ops v2 added Section 1.2 (Remote/Hybrid Participation Protocol), shifting all subsequent section numbers up by one. The Proposed Approach cross-references still use the old numbering.

| Proposed Approach reference | Label in link text | Actual section in Cross-Cutting Ops |
|---|---|---|
| Line 134 | `Cross-Cutting Operations: 1.5` (Decision Documentation) | **1.6** Decision Documentation |
| Line 144 | `Cross-Cutting Operations: 1.4` (Client communication rules) | **1.5** Client Communication Rules |
| Line 431 | `Cross-Cutting: 1.3` (Escalation paths) | **1.4** Escalation Paths |
| Line 508 | `client communication rules` (anchor `#14-client-communication-rules`) | Anchor should be `#15-client-communication-rules` |

The anchor slugs in the URLs (e.g., `#15-decision-documentation`) also need to match the actual heading numbers (e.g., `#16-decision-documentation`).

**Correction:** Update all four references and their anchors to match the actual v2 section numbers.

**File to change:** WoW_Proposed_Approach.md

---

## Issue 4: Cost Management section number mismatch -- Proposed Approach says "Section 5", Build doc has it as Section 6

**Documents affected:** WoW_Proposed_Approach.md, Granular_Build_Test_Deploy.md, Granular_Eval_Dataset_Lifecycle.md

**What happened:** Build_Test_Deploy v2 added Section 5 (Security) before Cost Management, pushing Cost Management to Section 6. Cross-references still say Section 5.

Affected references in WoW_Proposed_Approach.md:
- Line 138: `Build, Test & Deploy: 5.1` -- should be **6.1** (Tracking Granularity)
- Line 376: `BTD: 5.1` -- should be **6.1**
- Line 481: `BTD: 5.2` -- should be **6.2** (Budget Thresholds and Approvals)
- Line 522: `Build, Test & Deploy: 5.1-5.5` -- should be **6.1-6.5**
- Line 625: `BTD: 5.5` -- should be **6.5** (Reporting to Stakeholders)

Affected reference in Granular_Eval_Dataset_Lifecycle.md:
- Line 646: `Granular_Build_Test_Deploy.md Section 5` -- should be **Section 6**

**Correction:** Update all six references from Section 5.x to Section 6.x and fix the corresponding anchor slugs.

**File to change:** WoW_Proposed_Approach.md (5 references), Granular_Eval_Dataset_Lifecycle.md (1 reference)

---

## Issue 5: Engagement types A-D in Proposed Approach vs. A-F in Solutioning doc

**Documents affected:** WoW_Proposed_Approach.md, Granular_Solutioning_Requirements.md

**Conflicting text:**

WoW_Proposed_Approach.md (lines 168-172) defines only 4 types: A, B, C, D.
Lines 189, 195, 581, 695 all reference "A/B/C/D" as the complete set.

Granular_Solutioning_Requirements.md (lines 164-180) defines 6 types: A, B, C, D, **E (Internal Tooling/Productivity)**, and **F (Demo/Competitive Benchmark)**. The doc explicitly explains why E and F matter: "Without explicit typing, these either get treated like production work (too much process, too slow) or get no process at all."

**Correction:** Add Type E and Type F to the engagement typing table in WoW_Proposed_Approach.md (Part 4, lines 168-177), and update references on lines 189, 195, 581, and 695 from "A/B/C/D" to "A/B/C/D/E/F".

**File to change:** WoW_Proposed_Approach.md

---

## Issue 6: Retention period inconsistency -- 5 years vs. 7 years vs. 15+ years

**Documents affected:** Granular_Eval_Dataset_Lifecycle.md, Granular_Cross_Cutting_Operations.md, Granular_Solutioning_Requirements.md

**Conflicting text:**

Granular_Eval_Dataset_Lifecycle.md (line 612):
> "Minimum 5-year retention per pharma norms"

Granular_Cross_Cutting_Operations.md (lines 541, 574):
> "All audit trail data is retained for a minimum of 7 years (standard pharma document retention)."
> "Retention policy is enforced (7-year minimum)"

Granular_Solutioning_Requirements.md (line 222):
> "Pharma companies typically retain regulatory submission data for 15+ years."

These are three different numbers for what is essentially the same regulatory concern. The Solutioning doc accurately describes client reality (15+ years for regulatory submissions). The Cross-Cutting Ops doc states 7 years as the team's internal standard. The Eval doc states 5 years.

**Correction:** Align Eval Dataset Lifecycle to the same 7-year minimum stated in Cross-Cutting Operations. Change line 612 from "5-year" to "7-year." The 15+ year figure in the Solutioning doc is correct as stated (it describes client requirements to ask about, not the team's own retention policy).

**File to change:** Granular_Eval_Dataset_Lifecycle.md

---

## Issue 7: Eval Dataset cross-reference to client status template uses wrong section number

**Documents affected:** Granular_Eval_Dataset_Lifecycle.md, Granular_Cross_Cutting_Operations.md

**What is wrong:** Eval Dataset Lifecycle line 642 says:
> "How eval results are reported to stakeholders | Granular_Cross_Cutting_Operations.md | Section 1.4 (Client status template)"

The actual section is **1.5** Client Communication Rules (which contains the client status template).

**Correction:** Change "Section 1.4" to "Section 1.5" on line 642.

**File to change:** Granular_Eval_Dataset_Lifecycle.md

---

## Issue 8: Proposed Approach Build Gate references "1.7" for CODEOWNERS but actual section is 1.8

**Documents affected:** WoW_Proposed_Approach.md, Granular_Build_Test_Deploy.md

**What is wrong:** WoW_Proposed_Approach.md line 334:
> `All code reviewed and approved by engineering (per [CODEOWNERS](../v1/Granular_Build_Test_Deploy.md#17-preventing-non-engineers-from-breaking-things))`

The linked section title "Preventing Non-Engineers from Breaking Things" is actually Section **1.8** in the Build doc (line 158), not 1.7. Section 1.7 is "Conflict Resolution." The anchor slug `#17-preventing-non-engineers-from-breaking-things` also does not match the actual heading number.

**Correction:** Change the reference from `#17-preventing-non-engineers-from-breaking-things` to `#18-preventing-non-engineers-from-breaking-things`.

**File to change:** WoW_Proposed_Approach.md

---

## Issue 9: Build doc rollback section referenced as "3.3" in Proposed Approach but actual section is 3.5

**Documents affected:** WoW_Proposed_Approach.md, Granular_Build_Test_Deploy.md

**What is wrong:** WoW_Proposed_Approach.md lines 140 and 373 reference:
> `Build, Test & Deploy: 3.3` and `BTD: 3.3 rollback procedure`

with anchor `#33-step-by-step-rollback-procedure`. The actual rollback section in the Build doc is **3.5** Step-by-Step Rollback Procedure (line 429). Section 3.3 is "Skill/KB Version Management Across Environments."

**Correction:** Change "3.3" to "3.5" in both references and update the anchor slugs accordingly.

**File to change:** WoW_Proposed_Approach.md

---

## Issue 10: Build doc model version pinning referenced as "3.4" but actual section is 3.6

**Documents affected:** WoW_Proposed_Approach.md, Granular_Build_Test_Deploy.md

**What is wrong:** WoW_Proposed_Approach.md line 366:
> `Model version management: [Build, Test & Deploy: 3.4](../v1/Granular_Build_Test_Deploy.md#34-model-version-pinning)`

The actual section is **3.6** Model Version Pinning (line 465 in the Build doc). Section 3.4 is "Deployment to Client Environments."

**Correction:** Change "3.4" to "3.6" and update the anchor slug.

**File to change:** WoW_Proposed_Approach.md

---

## Summary

10 issues found. Most are cross-reference errors in WoW_Proposed_Approach.md caused by sections being renumbered or added in the granular v2 documents without updating the master framework's links. The two substantive inconsistencies are:

1. **Tech talk cadence** (Issue 2): bi-weekly vs. monthly -- a real process contradiction.
2. **Engagement types** (Issue 5): A-D vs. A-F -- the master framework is missing two types defined in the granular doc.
3. **Retention period** (Issue 6): 5 vs. 7 years -- a compliance-relevant numeric mismatch.

All remaining issues are stale cross-reference numbers. The role assignments, threshold numbers (0.80/0.85/0.70), auto-refinement guardrails ($50 cap, 5 modifications per session), cost governance tiers, and process sequences are consistent across all documents.
