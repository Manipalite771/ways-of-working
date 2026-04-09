# Evaluation Dataset Lifecycle — Granular Process

## 1. Creation

### 1.1 Who Does What

| Role | Responsibility |
|------|---------------|
| **Solution Architect** | Initiates dataset creation; defines scoring dimensions and rubric; selects source documents; sets pass/fail thresholds |
| **QC/Testing** | Collects input-output pairs from manual work; scores rows; flags edge cases; maintains dataset over time |
| **Engineer** | Builds tooling to run evals programmatically; integrates with CI/CD; creates LLM-as-Judge prompts |
| **SME/Domain** (external domain experts or internal QC team members) | Provides manually-authored reference outputs; validates scoring rubric; calibrates scores |
| **GenAI Solution Approvers** | Approves rubric and pass/fail thresholds; signs off on dataset adequacy before build starts |

### 1.2 Source Data — Where It Comes From

For each eval dataset, you need **input documents** (what the system receives) and **reference outputs** (what a correct result looks like).

| Source Type | Where to Get It | Quality | Availability |
|-------------|----------------|---------|-------------|
| Manually authored CSR sections from past engagements | Client deliverables archive, project folders | High — represents gold standard | Limited — need client permission to reuse |
| Client-provided sample documents | Engagement kickoff materials | Medium — may not cover all edge cases | Usually 3-5 samples at kickoff |
| Production outputs reviewed and corrected by SMEs | S3 log archives + SME correction notes | High — represents real-world corrections | Available for existing platforms |
| Synthetic examples generated and human-validated | Created by Solution Architect + QC team | Medium — may miss real-world quirks | Unlimited but time-intensive |
| Published regulatory documents / public clinical trials | ClinicalTrials.gov, FDA submissions, EMA public assessment reports | Medium — not client-specific but good for edge cases | Freely available |

### 1.3 Worked Example: CSR Section 11 (Usage Results)

**What is Section 11?** Usage Results in a CSR summarize how the investigational product was administered and consumed during the trial — dosing, duration of exposure, compliance, dose modifications, and treatment discontinuations.

**Step 1: Identify input sources needed**
- Statistical Analysis Tables (TFLs): specifically Table 14.1 (demographics/exposure), Table 14.3 (dosing/compliance)
- Protocol: dosing schedule, planned treatment duration, dose modification rules
- SAP: how exposure metrics were derived
- Previous CSR Section 11 (if amending): for comparison and consistency

**Step 2: Collect 3+ manually-authored Section 11 examples**

You need at minimum 3 completed Section 11s from different studies to establish patterns. Ideal: 5-7 covering different scenarios.

| Example | Study Type | Complexity | Why Included |
|---------|-----------|------------|-------------|
| Ex 1 | Phase III oncology, 2-arm | Medium | Standard dosing, clear exposure tables |
| Ex 2 | Phase II rare disease, 3-arm + placebo | High | Multiple dose levels, titration schedule, small N |
| Ex 3 | Phase III cardiovascular, long-duration | Medium | Extended exposure period, dose modifications common |
| Ex 4 | Phase I healthy volunteer | Low | Simple single-dose, short exposure |
| Ex 5 | Phase III pediatric | High | Weight-based dosing, age cohorts, formulation differences |

**Step 3: Create input-output pairs**

For each example, the input is the set of source documents. The output is the manually-authored Section 11 text.

**Step 4: Define scoring dimensions**

For CSR Section 11 specifically:

| Dimension | Weight | What It Measures | Scoring |
|-----------|--------|-----------------|---------|
| **Data Accuracy** | 30% | Every numeric value (N, %, mean, median, range) matches source TFLs exactly | Pass (100% match) / Fail (any mismatch) — binary, no partial credit |
| **Completeness** | 25% | All required subsections present: disposition, exposure duration, dose intensity, compliance, dose modifications, discontinuations | Checklist: score = (subsections present) / (subsections required) |
| **Clinical Interpretation** | 20% | Narrative explains what the numbers mean (e.g., "Median exposure was 24 weeks, indicating most patients completed the planned treatment duration") — not just restating numbers | 1-5 scale: 1=data dump, 3=basic context, 5=insightful interpretation linking to protocol/endpoints |
| **Regulatory Compliance** | 15% | Follows ICH E3 structure; uses required regulatory language; no promotional claims; appropriate hedging | Checklist of 8-10 regulatory requirements, score = (met) / (total) |
| **Conciseness & Style** | 10% | No redundancy across subsections; cross-references used appropriately; consistent tense/voice; appropriate length | 1-5 scale: 1=severely bloated/redundant, 3=acceptable, 5=tight and clear |

**Step 5: Score the reference outputs themselves**

Before using the dataset, score your own manually-authored reference outputs on all dimensions. This establishes the baseline. If a manual output scores 4.2/5.0 on average, that's your realistic ceiling — don't expect the system to score 5.0.

**Step 6: Build the dataset rows**

### 1.4 Dataset Schema

```json
{
  "dataset_metadata": {
    "name": "csr-section-11-usage-results",
    "version": "1.0.0",
    "created_by": "[solution-architect-id]",
    "created_date": "2026-04-15",
    "product_area": "MWA",
    "document_type": "CSR",
    "section": "11 - Usage Results",
    "description": "Golden dataset for evaluating CSR Section 11 authoring quality",
    "scoring_dimensions": ["data_accuracy", "completeness", "clinical_interpretation", "regulatory_compliance", "conciseness_style"],
    "pass_threshold": 0.85,
    "total_rows": 20,
    "edge_case_count": 5
  },
  "rows": [
    {
      "row_id": "S11-001",
      "input": {
        "source_documents": [
          {"type": "TFL", "file": "study_abc_table_14_1.pdf", "description": "Demographics and Exposure Summary"},
          {"type": "TFL", "file": "study_abc_table_14_3.pdf", "description": "Dose Compliance Summary"},
          {"type": "protocol", "file": "study_abc_protocol_v3.pdf", "pages": "45-52", "description": "Dosing schedule and modifications"},
          {"type": "SAP", "file": "study_abc_sap_v2.pdf", "pages": "12-15", "description": "Exposure derivation methods"}
        ],
        "instructions": "Author CSR Section 11 (Usage Results) following ICH E3 guidelines"
      },
      "expected_output": {
        "file": "study_abc_section_11_manual.md",
        "word_count": 1850,
        "subsections": ["11.1 Disposition", "11.2 Duration of Exposure", "11.3 Dose Intensity and Compliance", "11.4 Dose Modifications", "11.5 Treatment Discontinuations"]
      },
      "scores": {
        "data_accuracy": {"score": 1.0, "notes": "All 47 numeric values verified against TFLs"},
        "completeness": {"score": 1.0, "notes": "All 5 subsections present"},
        "clinical_interpretation": {"score": 4, "notes": "Good interpretation of exposure duration; could improve compliance discussion"},
        "regulatory_compliance": {"score": 0.9, "notes": "8/9 ICH E3 requirements met; missing cross-reference to Section 10"},
        "conciseness_style": {"score": 4, "notes": "Minimal redundancy; one paragraph could be tightened"}
      },
      "weighted_score": 0.91,
      "difficulty": "medium",
      "edge_case": false,
      "therapeutic_area": "oncology",
      "study_phase": "Phase III",
      "special_characteristics": ["2-arm", "fixed-dose"],
      "last_validated": "2026-04-15",
      "validated_by": "[qc-team-member-id]"
    }
  ]
}
```

### 1.5 How Many Rows

| Engagement Type | Minimum Rows | Recommended | Edge Cases (of total) |
|----------------|-------------|------------|----------------------|
| New product area (first time doing CSR Section 11) | 15 | 20-25 | 25-30% |
| New client on existing product (same section type, different client conventions) | 10 | 15 | 20% |
| Prompt/skill improvement (already have baseline) | 5 additional rows targeting failure patterns | 10 | 50% (focus on failures) |

**Edge case examples for Section 11:**
- Study with 5+ treatment arms (complex exposure tables)
- Study with weight-based pediatric dosing (non-standard dose metrics)
- Study where >30% discontinued (heavy dose modification narrative)
- Open-label extension study (cumulative exposure from parent study)
- Study with multiple formulations (tablet + IV)

### 1.6 Realistic Time Estimates

| Activity | Who | Time | Notes |
|----------|-----|------|-------|
| Identify and collect source documents for 5 studies | QC/Testing | 3-4 hours | Assumes documents already exist in project archive |
| Collect corresponding manually-authored Section 11s | QC/Testing | 1-2 hours | May need client permission |
| Define scoring dimensions and rubric | Solution Architect | 2-3 hours | First time per section type; reuse for subsequent |
| Score all 5 reference outputs on all dimensions | QC/Testing (2 people independently) | 4-5 hours total | Each scorer does all 5; then calibrate |
| Calibrate inter-rater scores | Solution Architect + QC team | 1 hour meeting | Resolve disagreements, finalize rubric wording |
| Expand to 15-20 rows (synthetic + additional real) | QC/Testing + Solution Architect | 6-8 hours | Synthetic rows need human validation |
| Format into JSON schema | Engineer or Solution Architect | 1-2 hours | Template exists after first dataset |
| Review and approve dataset | GenAI Solution Approvers | 1 hour | Review rubric, check coverage, approve thresholds |
| **Total for first dataset of a new section type** | | **~20-25 hours across 1-2 weeks** | Subsequent section types: ~15 hours (rubric patterns reusable) |

---

## 2. Maintenance & Versioning

### 2.1 Versioning Strategy

Eval datasets use **semantic versioning**: `MAJOR.MINOR.PATCH`

- **MAJOR** (1.0 → 2.0): Scoring dimensions changed, threshold changed, or >50% of rows replaced. Triggers full re-evaluation of all skill versions against new dataset.
- **MINOR** (1.0 → 1.1): New rows added, edge cases expanded, or existing row scores recalibrated. Triggers regression check.
- **PATCH** (1.0.0 → 1.0.1): Typo fix, metadata correction, no scoring impact. No re-evaluation needed.

Datasets are stored in the same git repository as skills, under `/eval-datasets/{product-area}/{section-type}/`.

> This versioning strategy is managed through GitHub version control.

### 2.2 When to Add New Rows

| Trigger | Action | Who |
|---------|--------|-----|
| Production failure not covered by existing dataset | Add row capturing the failure case as a new edge case | QC/Testing within 1 week of failure |
| New client onboarding | Add 2-3 rows with client-specific conventions (e.g., different table formatting, different therapeutic area) | Solution Architect during Stage 1 |
| Skill auto-refinement plateaus | Analyze which failure patterns are not in the dataset; add targeted rows | Solution Architect |
| Quarterly review identifies coverage gaps | Add rows to underrepresented categories (difficulty levels, therapeutic areas, study phases) | QC/Testing |

### 2.3 When to Remove or Retire Rows

- Row reflects an outdated client SOP → mark as `deprecated`, do not delete (keep for historical comparison)
- Row has been consistently easy-pass for 3+ skill versions → move to `archive` set (not run in standard suite, only in full regression)
- Row scoring was found to be miscalibrated → fix scoring if possible, retire if the source output itself was wrong

### 2.4 Client-Specific vs. Universal

```
/eval-datasets/
  /mwa/
    /csr-section-11/
      universal_v1.2.json        # Generic ICH E3 Section 11 eval
      vertex_specific_v1.0.json  # Vertex brand/SOP conventions overlaid
      az_specific_v1.0.json      # AZ-specific conventions
```

**Rule:** Universal dataset runs on every eval. Client-specific dataset runs only for that client's engagements. A skill must pass both.

### 2.5 Preventing Eval Dataset Overfitting

Overfitting means the skill is tuned to pass these specific test cases but fails on new real-world inputs.

**Safeguards:**
1. **Hold-out set**: Reserve 20% of rows as a hold-out that is never shown during auto-refinement. Only run against it during final validation.
2. **Diverse sourcing**: Rows must span at least 3 therapeutic areas, 2 study phases, and 3 complexity levels.
3. **Regular injection of unseen data**: Every quarter, add 3-5 new rows from recent real-world outputs (not yet used in any refinement).
4. **Cross-validation**: Run the same skill against a different section type's dataset (e.g., Section 11 skill against Section 12 data). The skill should fail gracefully (recognize it's the wrong section) — if it hallucinates a "good" Section 11 from Section 12 inputs, the guardrails are missing.

---

## 3. Scoring & Evaluation

### 3.1 Manual Human Scoring

**When:** During dataset creation, during Tier 3 weekly reviews, when calibrating LLM-as-Judge.

**Process:**
1. Two independent scorers (ideally one Solution Architect + one QC person) score the same outputs
2. Each scorer uses the rubric independently — no conferring during scoring
3. Scores are compared. If they differ by >1 point on any 1-5 dimension, or disagree on a binary dimension, schedule a 30-minute calibration meeting
4. In calibration: discuss the specific passage, agree on a score, and update the rubric if the wording was ambiguous
5. Record the final agreed score plus a note explaining the calibration decision

**Calibration frequency:** Every new dataset gets a calibration round on the first 5 rows. After that, calibrate whenever a new scorer joins or scoring disagreement rate exceeds 15%.

### 3.2 LLM-as-Judge Setup

**Purpose:** Automate scoring for Tier 2 (every PR) so humans only review a sample.

**Judge Prompt Template (for CSR Section 11):**

```
You are evaluating the quality of an AI-authored CSR Section 11 (Usage Results).

## Source Documents
{source_documents_content}

## Generated Output
{generated_section_11}

## Reference Output (Gold Standard)
{reference_section_11}

## Scoring Rubric

Score the generated output on each dimension:

### 1. Data Accuracy (binary: PASS or FAIL)
Compare every numeric value in the generated output against the source TFLs. 
If ANY numeric value is wrong, misattributed, or fabricated: FAIL.
List every numeric value checked and whether it matches.

### 2. Completeness (0.0 to 1.0)
Required subsections: {list_of_required_subsections}
Score = (subsections present and substantively addressed) / (total required)
A subsection that exists but is a single placeholder sentence counts as 0.5.

### 3. Clinical Interpretation (1-5)
1 = Pure data dump — numbers restated with no context
2 = Minimal interpretation — occasional "this means..." statements
3 = Adequate — most numbers contextualized with protocol/clinical relevance
4 = Good — clear clinical narrative connecting exposure to study objectives
5 = Excellent — insightful interpretation, appropriate comparisons, clear implications

### 4. Regulatory Compliance (0.0 to 1.0)
Check against these requirements: {ich_e3_checklist}
Score = (requirements met) / (total requirements)

### 5. Conciseness & Style (1-5)
1 = Severely bloated, major redundancy, inconsistent voice
2 = Noticeable redundancy or style issues
3 = Acceptable — some tightening possible but functional
4 = Clean — minimal redundancy, consistent style
5 = Publication-ready — tight, clear, professional

## Output Format
Return JSON:
{
  "data_accuracy": {"score": "PASS|FAIL", "values_checked": [...], "mismatches": [...]},
  "completeness": {"score": 0.0-1.0, "subsections_found": [...], "subsections_missing": [...]},
  "clinical_interpretation": {"score": 1-5, "justification": "..."},
  "regulatory_compliance": {"score": 0.0-1.0, "requirements_met": [...], "requirements_missed": [...]},
  "conciseness_style": {"score": 1-5, "justification": "..."},
  "weighted_total": 0.0-1.0,
  "summary": "One paragraph overall assessment"
}
```

**Validating the judge:** Before trusting LLM-as-Judge in CI/CD, run it on 10 rows that already have human scores. If LLM scores diverge from human scores by >0.5 on weighted total for more than 2 rows, revise the judge prompt. Target: >85% agreement between LLM and human scores.

**Which model for judging:** Use Opus or Sonnet for judging — never the same model tier that generated the output. If Sonnet generated the content, use Opus to judge (or vice versa).

### 3.2.1 LLM-as-Judge Known Failure Modes

| Failure Mode | Symptom | Mitigation |
|-------------|---------|-----------|
| **Leniency bias** | Judge consistently scores 0.5-1.0 higher than humans | Add "Be strict. When in doubt, score lower." to judge prompt. Calibrate on 10 rows before trusting. |
| **Positional bias** | Judge favors whichever output is presented first (generated vs. reference) | Randomize order in prompt. Run 2x with swapped positions for high-stakes evals. |
| **Length bias** | Judge scores longer outputs higher regardless of quality | Add "Length is NOT a quality indicator. A concise, accurate 500-word section can score higher than a verbose 2000-word one." |
| **Self-evaluation blind spot** | If the same model generated and judges, it may not catch its own systematic errors | Never use the same model tier for generation and judging. Cross-model validation. |
| **Numeric verification weakness** | LLMs are unreliable at verifying exact numeric values | NEVER rely solely on LLM judge for data accuracy. Always pair with programmatic numeric extraction check (Tier 1). |
| **Reference anchoring** | Judge over-relies on reference output structure rather than evaluating generated output independently | Include instruction: "The reference output is one acceptable version. The generated output may differ in structure while still being correct." |
| **Domain knowledge gap** | Judge may not know pharma-specific conventions (e.g., ICH E3 structure, RECIST criteria) | Include relevant domain context in the judge prompt. For regulatory compliance dimension, provide the specific checklist inline. |

### 3.3 Programmatic Checks (No LLM Needed)

These run on every commit — fast, cheap, deterministic:

| Check | What It Validates | Tool |
|-------|------------------|------|
| Numeric extraction match | Every number in output exists in source TFLs | Python script: extract all numbers from output, check against source number set |
| Subsection headers present | Required subsection headings exist in output | Regex pattern matching |
| Word count within range | Output is between min and max expected length | `len(output.split())` |
| No hallucinated drug names | Only drug names from the protocol appear in output | Dictionary check against protocol's compound list |
| Table formatting valid | Inline tables have correct column count and headers | Schema validation |
| Cross-reference validity | Any "see Section X" references point to real section numbers | Regex + document structure check |
| Encoding clean | No Unicode garbage, broken tags, or encoding artifacts | Character class validation |

### 3.4 Handling Disagreement Between Human and LLM Scores

| Scenario | Action |
|----------|--------|
| LLM says PASS, human says FAIL on data accuracy | **Always trust human for factual/numeric dimensions.** Update the judge prompt to catch what it missed. Add the case to a "judge calibration" test set. |
| LLM scores interpretation as 4, human scores as 2 | Investigate: if the human has domain expertise the LLM lacks, trust human. If the disagreement is subjective, average the scores and flag for calibration. |
| Consistent LLM bias (always scores higher than human) | Adjust the judge prompt to be stricter. Add "err on the side of caution" instructions. |

### 3.5 Pass/Fail Thresholds

| Level | Threshold | Where Used |
|-------|-----------|-----------|
| **PR gate (Tier 2)** | Weighted score >= 0.80 on all eval rows; zero FAIL on data accuracy | Blocks merge if not met |
| **Build Gate** | Weighted score >= 0.85 averaged across full dataset; zero FAIL on data accuracy; no single row below 0.70 | Blocks deployment to staging |
| **Production release** | Same as Build Gate + hold-out set also passes at 0.85 | Blocks production deployment |

**Who sets thresholds:** Solution Architect proposes based on baseline scores of manual outputs. GenAI Solution Approvers approve. Client is shown the rubric and thresholds for sign-off during Stage 1.

---

## 4. Integration with Build Pipeline

### 4.1 How Evals Gate PRs

```
Developer pushes branch → PR created
  → CI triggers:
    1. Programmatic checks (Tier 1) — 30 seconds, $0
       - If FAIL: PR blocked, developer fixes
    2. LLM-as-Judge eval on minimum viable dataset (Tier 2) — 5-10 min, $0.50-$2.00
       - Runs on "quick eval" subset: 5 rows (2 easy, 2 medium, 1 hard)
       - If any data accuracy FAIL: PR blocked
       - If weighted score < 0.80 on any row: PR blocked
       - Results posted as PR comment with per-dimension scores
    3. Engineer reviews code + eval results
       - If eval passes but engineer has concerns: request full eval run
    4. Merge approved
```

### 4.2 Full Eval Suite (Pre-Deployment)

Runs before staging deployment — not on every PR (too expensive).

```
Merge to main → Full eval triggered
  - All rows in universal dataset
  - All rows in client-specific dataset (if applicable)
  - Hold-out set (only at this stage)
  - ~20-30 minutes, $5-$15 depending on dataset size
  - Results stored in eval history with skill version tag
  - If threshold not met: deployment blocked, alert to Solution Architect
```

### 4.3 Running Evals Locally

Any team member can run evals locally before pushing:

```bash
# Run quick eval (5 rows, ~2 min)
python run_eval.py --dataset csr-section-11 --mode quick --skill-version local

# Run full eval (all rows, ~20 min)
python run_eval.py --dataset csr-section-11 --mode full --skill-version local

# Run single row (for debugging a specific failure)
python run_eval.py --dataset csr-section-11 --row S11-003 --skill-version local --verbose
```

### 4.4 When Evals Fail — Process

1. **Developer sees failure in PR comment** — reads per-dimension scores
2. **Identify root cause**: is it a skill issue, knowledge base issue, or pipeline issue?
   - Data accuracy FAIL → likely skill is misinterpreting source table → fix skill
   - Completeness drop → likely skill is skipping a subsection → check skill instructions
   - Interpretation drop → likely skill wording needs refinement → update conventions KB
3. **Fix and re-run**: push new commit, Tier 2 re-runs automatically
4. **If stuck after 2 attempts**: escalate to Solution Architect for solutioning
5. **If the eval itself seems wrong**: flag to QC/Testing for rubric review (the eval might be miscalibrated)

### 4.5 Regression Testing

Every skill change is tested against the **full eval history**:
- Current dataset (active rows)
- Archived "previously passing" rows (should still pass)
- Known-fixed failure cases (should still be fixed)

If a previously-passing row now fails, the change introduced a regression. The developer must either fix the regression or justify why it's acceptable (with Solution Architect approval).

### 4.6 Cost of Running Evals

| Eval Type | Rows | LLM Calls | Estimated Cost | Time |
|-----------|------|-----------|---------------|------|
| Tier 1 (programmatic) | All | 0 | $0 | 30 sec |
| Tier 2 (quick eval) | 5 | 5 judge calls | $0.50-$2.00 | 5-10 min |
| Full eval | 20 | 20 judge calls + 20 generation calls | $5-$15 | 20-30 min |
| Full regression | 30+ | 30+ judge + 30+ generation | $10-$25 | 30-45 min |

**Monthly budget estimate:** Assuming 3 PRs/week × quick eval + 1 full eval/week = ~$30-80/month per product area. This is negligible compared to the cost of shipping a bad skill to production.

---

## 5. Feedback Loop

### 5.1 Client/SME Feedback → Eval Dataset

```
Client/SME reviews output → provides comments/edits
  → QC/Testing classifies each comment:
    A) Factual error (wrong number, wrong drug name)
       → Add as regression test row with data_accuracy = FAIL
    B) Missing content (subsection incomplete)
       → Add as row with completeness < 1.0
    C) Style/interpretation preference (client wants different tone)
       → Add to client-specific conventions KB
       → Add as row in client-specific eval dataset
    D) Out-of-scope request (feature the system doesn't do)
       → Log as feature request, NOT added to eval dataset
```

### 5.2 Auto-Refinement Cycle

```
Session start:
  1. Agent runs system on all eval dataset rows
  2. Agent scores outputs using LLM-as-Judge
  3. Agent identifies rows that fail or score below threshold
  4. Agent analyzes failure patterns across 3+ failing rows
  5. Agent proposes skill modification (with rationale)
  6. Agent applies modification to skill file
  7. Agent re-runs ONLY the previously-failing rows
  8. Agent checks: did scores improve? Did any passing rows regress?
  9. If improvement + no regression → accept change, log it
  10. If regression → revert change, try different approach
  11. Repeat until threshold met or budget exhausted

Guardrails:
  - Max 5 skill modifications per session
  - Max $50 per auto-refinement session
  - Human reviews all accepted changes before merge
  - Hold-out set is NEVER shown to auto-refinement agent
```

### 5.3 When to Retire Eval Rows

| Signal | Action |
|--------|--------|
| Row has been easy-pass (score > 0.95) for 5+ consecutive skill versions | Move to archive set |
| Row's source document is no longer representative (old SOP version) | Mark deprecated, add replacement row |
| Row's scoring was found to be wrong after calibration | Fix or retire with documented reason |
| Row represents a scenario the system will never need to handle (e.g., we dropped pediatric support) | Retire with documented reason |

**Never delete rows entirely** — move to archive. You may need to verify a historical claim about quality.

---

## 6. MedCom Pilot: Eval Datasets for Visual/Multi-Modal Outputs

MedCom is the designated pilot track. Unlike MWA (text-only CSR sections), MedCom generates multi-modal outputs: PowerPoint slides, charts (Plotly/SVG), infographics, and formatted documents with embedded visuals. This requires a different eval approach.

### 6.1 Scoring Dimensions for MedCom Assets

| Dimension | Weight | What It Measures | Scoring |
|-----------|--------|-----------------|---------|
| **Content Accuracy** | 25% | Claims, data points, and messaging match approved source materials | Binary PASS/FAIL per claim; score = correct/total |
| **Brand Compliance** | 20% | Colors, fonts, logos, layout match brand guidelines | Checklist of 10-15 brand elements; score = (met)/(total) |
| **Visual Quality** | 20% | Charts are readable, properly labeled, axes correct, legends present, no truncation | 1-5 scale per visual element |
| **MLR Readiness** | 15% | All claims have source annotations, no unsupported promotional language, required disclosures present | Checklist; binary per requirement |
| **Layout & Composition** | 10% | Slide hierarchy logical, text/visual balance appropriate, no overflow or blank space | 1-5 scale |
| **Completeness** | 10% | All required slides/sections present per the asset brief | Checklist: score = (present)/(required) |

### 6.2 How to Evaluate Visual Outputs

Visual outputs cannot be evaluated with text-only LLM judges. Three approaches:

**Approach 1: Decompose into evaluable components**
- Extract text content from PPTX → evaluate text accuracy, claims, messaging with standard LLM judge
- Extract chart data (if programmatically generated) → validate against source data programmatically
- Extract layout metadata (slide count, element positions) → validate against template requirements

**Approach 2: Screenshot + multimodal judge**
- Render each slide to PNG
- Use a multimodal LLM (Claude with vision) to evaluate visual quality, brand compliance, layout
- Judge prompt includes reference screenshots of "good" examples

**Approach 3: Human review with structured rubric**
- For dimensions that are hard to automate (aesthetic quality, brand "feel"), use structured human review
- QC team scores using the same rubric as the LLM judge, tracked in the same dataset format

**Recommended for MedCom pilot:** Start with Approach 1 (decompose) for accuracy and completeness checks. Add Approach 2 (multimodal judge) for brand and visual quality once the basic pipeline works. Reserve Approach 3 for Tier 3 weekly reviews.

### 6.3 MedCom Eval Dataset Schema Extension

*Note: This schema extension is provided as an example. The actual eval dataset schema may vary depending on the specific framework and engagement requirements.*

```json
{
  "row_id": "MC-001",
  "input": {
    "source_documents": [
      {"type": "key_messages", "file": "product_x_key_messages.pdf"},
      {"type": "brand_guide", "file": "product_x_brand_guide.pdf"},
      {"type": "data_source", "file": "study_xyz_results.pdf"}
    ],
    "asset_brief": {
      "asset_type": "detail_aid",
      "slide_count": 6,
      "target_audience": "HCP",
      "required_claims": ["efficacy_primary", "safety_profile", "dosing"]
    }
  },
  "expected_output": {
    "file": "product_x_detail_aid_manual.pptx",
    "screenshots": ["slide_1.png", "slide_2.png", "slide_3.png", "slide_4.png", "slide_5.png", "slide_6.png"],
    "extracted_text": "product_x_detail_aid_text.json",
    "extracted_chart_data": "product_x_charts.json"
  },
  "scores": {
    "content_accuracy": {"score": 0.95, "claims_checked": 12, "claims_correct": 11},
    "brand_compliance": {"score": 0.85, "brand_elements_checked": 13, "elements_met": 11},
    "visual_quality": {"score": 4, "notes": "Charts clear; one legend truncated"},
    "mlr_readiness": {"score": 0.9, "requirements_met": 9, "requirements_total": 10},
    "layout_composition": {"score": 4, "notes": "Good balance; slide 4 slightly text-heavy"},
    "completeness": {"score": 1.0, "slides_present": 6, "slides_required": 6}
  }
}
```

### 6.4 MedCom Bootstrapping

Since MedCom is the first track to use this eval framework, the team has no existing eval datasets. See Section 1.8 below for the general bootstrapping process, applied specifically:

1. Collect 3-5 manually-created MedCom assets (detail aids, leave-behinds, or conference slides) from past engagements
2. Define scoring dimensions using the table in 6.1
3. Score the manual assets — this establishes the quality ceiling
4. Start with 10 rows (3 easy, 4 medium, 3 hard) — less than the 15-20 recommended for mature areas, because the team is learning the process
5. Run the first eval cycle manually (no CI/CD yet — per the phased CI rollout in the Build/Test/Deploy doc)
6. Iterate: refine rubric based on what's actually differentiating good from bad outputs

---

## 7. Bootstrapping: Creating Your First-Ever Eval Dataset

When the team has never done eval-driven development before (which is now), the process described in Section 1 can feel overwhelming. This section describes how to get from zero to a usable dataset with minimal friction.

### 7.1 The Minimal Viable Eval Dataset (MVED)

**Goal:** 5 rows, 3 scoring dimensions, completed in 1 day.

```
Step 1 (30 min): Pick ONE output type you produce most often 
  (e.g., MedCom detail aid, or CSR Section 11)

Step 2 (1 hour): Collect 5 existing outputs — ones the team considers "done" and "good enough."
  These ARE your reference outputs. Don't create new ones.

Step 3 (30 min): Pick 3 scoring dimensions (not 5, not 8 — just 3).
  Recommended starting three: Accuracy, Completeness, Overall Quality (1-5)

Step 4 (1 hour): Two people independently score all 5 outputs on the 3 dimensions.
  Use a spreadsheet. Don't overthink format.

Step 5 (30 min): Compare scores. Where you disagree, discuss for 5 minutes.
  If you can't agree, the rubric wording is ambiguous — fix it.

Step 6 (30 min): You now have a 5-row eval dataset. 
  Run the system on the same inputs. Score the outputs the same way.
  Compare: system output vs. reference output.
  You have your first eval baseline.
```

**Total time: ~4 hours for 2 people.** This is deliberately minimal. Expand to the full process (Section 1) once the team is comfortable with the workflow.

### 7.2 When to Graduate from MVED to Full Dataset

| Signal | Action |
|--------|--------|
| Team has run 3+ eval cycles and the process feels routine | Expand to 15-20 rows |
| Edge cases are causing production failures not caught by the 5 rows | Add edge case rows targeting those failures |
| Client sign-off is needed | Expand scoring dimensions to 5 and formalize the rubric for client review |
| CI/CD integration is ready | Formalize into JSON schema (Section 1.4) |

---

## 8. Pharma Regulatory Compliance for Eval Datasets

### 8.1 Audit Trail Requirements

In pharma, any system that generates content for regulatory submissions or medical communications must maintain audit trails. Eval datasets are part of the quality system and must be traceable.

| Requirement | How We Address It |
|-------------|------------------|
| **Change history** | Eval datasets are in git — every change is committed with author, timestamp, and rationale |
| **Who approved what** | PR approval records in GitHub serve as electronic signatures for dataset changes |
| **Why thresholds were set** | Decision log entry required when pass/fail thresholds are set or changed |
| **Traceability to outputs** | Each eval run is logged with: dataset version, skill version, model version, timestamp, results |
| **Retention** | Eval datasets are never deleted (archived, not removed). Minimum 7-year retention per pharma norms |

### 8.2 Data Privacy in Eval Datasets

| Rule | Detail |
|------|--------|
| **No patient-identifiable data** | Source documents used in eval datasets must be de-identified. If using real clinical trial data, ensure it comes from published/approved sources only. |
| **Client data segregation** | Client-specific eval datasets are stored in client-namespaced folders with access restricted to team members assigned to that engagement |
| **Cross-client reuse** | Universal eval datasets may use publicly available data (FDA submissions, published CSRs). Client-specific data NEVER crosses into universal datasets. |
| **Access control** | Eval datasets containing client data inherit the same access restrictions as the client's source documents. Use git repository permissions or folder-level access. |
| **API call data handling** | When running evals, generated outputs may contain client data sent through LLM APIs. Ensure the LLM provider's data handling terms permit this (e.g., Anthropic's data retention policy). |

### 8.3 GxP Considerations

For solutions that will be part of a GxP-regulated workflow (e.g., CSR authoring for regulatory submissions):

- Eval datasets serve as part of the **Operational Qualification (OQ)** — they demonstrate the system produces acceptable outputs under defined conditions
- The eval pass/fail threshold serves as the **acceptance criteria** — document why this threshold was chosen (link to manual output baseline scores)
- Eval results at each deployment serve as **release testing evidence** — archive the full results alongside the deployment record
- Changes to eval datasets or thresholds are **controlled changes** — require documented rationale and approval

---

## 9. Cross-References to Other WoW Documents

| Topic | Primary Document | Section |
|-------|-----------------|---------|
| How eval datasets are used in CI/CD | [Granular_Build_Test_Deploy.md](./Granular_Build_Test_Deploy.md) | Sections 2 (Testing), 3 (Deployment) |
| How skills reference eval datasets | [Granular_Skills_KB_Lifecycle.md](./Granular_Skills_KB_Lifecycle.md) | Section 1.1 (metadata: eval_dataset field) |
| How eval requirements are defined during solutioning | [Granular_Solutioning_Requirements.md](./Granular_Solutioning_Requirements.md) | Section 2.3 (Workshop agenda) |
| How eval results are reported to stakeholders | [Granular_Cross_Cutting_Operations.md](./Granular_Cross_Cutting_Operations.md) | Section 1.5 (Client communication rules) |
| How eval thresholds are agreed with clients | [Granular_Solutioning_Requirements.md](./Granular_Solutioning_Requirements.md) | Section 1.1 (Step 6: Client sign-off) |
| How auto-refinement uses eval datasets | [Granular_Skills_KB_Lifecycle.md](./Granular_Skills_KB_Lifecycle.md) | Section 1.7 (Auto-refinement) |
| Overall lifecycle stage where eval datasets are created | [WoW_Proposed_Approach.md](./WoW_Proposed_Approach.md) | Stage 1 (Requirement Gate) |
| Cost of running eval suites | This document, Section 4.6 + [Granular_Build_Test_Deploy.md](./Granular_Build_Test_Deploy.md) Section 6 |
