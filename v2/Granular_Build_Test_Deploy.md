# Build, Test & Deploy Pipeline — Granular Process

## 1. Code Contribution Model

### 1.1 Branch Strategy

**Model: Trunk-based development with short-lived feature branches.** This works best for a mixed-skill team because it keeps branches small, reviewable, and merge-conflict-free.

```
main (protected — no direct pushes)
  |
  +-- feature/skill-csr-s11-conciseness-fix     (Solution Architect)
  +-- feature/eval-dataset-s11-add-edge-cases    (QC/Testing)
  +-- feature/pipeline-orchestrator-retry-logic  (Engineer)
  +-- fix/kb-vertex-exposure-metric              (Solution Architect)
  +-- refactor/source-extraction-performance     (Engineer)
```

**Naming convention:** `{type}/{area}-{short-description}`
- Types: `feature/`, `fix/`, `refactor/`, `eval/`, `skill/`, `kb/`
- Keep branch names under 50 characters

**Practical note for non-engineers:** If you forget the naming convention, any reasonable branch name is fine — an engineer will rename it during PR review if needed. The convention is a courtesy, not a gate. What matters is: one branch per change, and never commit directly to main.

### 1.2 Git Essentials for Non-Engineers

Most of this team is new to git. Before the workflow below is useful, everyone needs to be comfortable with a small set of commands. This is not a substitute for a proper onboarding session — it is a reference card.

**The five commands you need:**

| Command | What it does | When to use it |
|---------|-------------|----------------|
| `git pull origin main` | Gets the latest version of main | Always before starting new work |
| `git checkout -b skill/my-change` | Creates a new branch for your work | Once, when starting a change |
| `git add <file>` | Stages a file for commit | After editing a file |
| `git commit -m "short description"` | Saves a snapshot of your changes | After staging files |
| `git push origin skill/my-change` | Uploads your branch to GitHub | When ready for review |

**Common mistakes and fixes:**

| Mistake | Symptom | Fix |
|---------|---------|-----|
| Forgot to create a branch, edited on main | `git status` shows changes on main | Ask an engineer — they will move your changes to a branch. Do NOT try to fix this yourself. |
| Merge conflict | Git says "CONFLICT" when you pull | Do NOT attempt to resolve. Post in the team channel, an engineer will handle it. |
| Pushed to the wrong branch | PR looks wrong | Ask an engineer. Do NOT use `git push --force`. |
| Want to undo a change | File is messed up | `git checkout -- <file>` undoes uncommitted changes. If already committed, ask an engineer. |

**Onboarding requirement:** Before anyone contributes their first PR, they must complete a 30-minute guided walkthrough with an engineer. The walkthrough uses a sandbox repo, not the production repo. This is not optional.

### 1.3 Who Can Do What

| Action | Solution Architect | QC/Testing | Engineer |
|--------|-------------------|-----------|----------|
| Create feature branch | Yes | Yes | Yes |
| Modify skill files (.md) | Yes | Yes (minor fixes) | Yes |
| Modify KB files (.json) | Yes | Yes | Yes |
| Modify eval datasets | Yes | Yes | Yes (with SA review) |
| Modify pipeline code (.py) | Yes (with engineer review) | No | Yes |
| Modify infrastructure/deployment configs | No | No | Yes only |
| Approve PRs (skill/KB changes) | Yes (peer) | No | Yes (required) |
| Approve PRs (code changes) | No | No | Yes (required) |
| Merge to main | No | No | Engineer only |
| Deploy to staging | No | No | Engineer only |
| Deploy to production | No | No | Engineer + Leadership approval |

### 1.4 PR Process

**PR Template:**

```markdown
## What changed
[1-2 sentences: what was modified and why]

## Type of change
- [ ] Skill modification
- [ ] Knowledge base update
- [ ] Eval dataset change
- [ ] Pipeline/code change
- [ ] Infrastructure change

## Files changed
[List of files]

## Eval results
- Quick eval score (before): X.XX
- Quick eval score (after): X.XX
- Any regressions: Yes/No
- [Link to eval run output]

## Testing done
- [ ] Ran locally on 3+ test inputs
- [ ] Quick eval (5 rows) passes
- [ ] No regressions on previously-passing rows
- [ ] Reviewed by peer (for skill/KB changes)

## Checklist
- [ ] No client-specific data in universal files
- [ ] No hardcoded API keys or secrets
- [ ] Metadata/version updated in frontmatter
- [ ] Eval dataset updated if scoring criteria changed
```

**How the PR template works in practice:** When you create a Pull Request on GitHub, this template automatically appears as a pre-filled form. You fill in each section describing your change. The template lives in the repository at `.github/PULL_REQUEST_TEMPLATE.md` and is set up once by an engineer.

**Required reviewers:**
- Skill/KB changes: 1 peer SA + 1 engineer
- Code changes: 1 engineer (different from author)
- Infrastructure changes: Both engineers

**PR must pass before merge:** All Tier 1 checks + Tier 2 quick eval

### 1.5 How Non-Engineers Contribute Using Cursor/Claude Code

**Practical workflow:**

```
1. Pull latest main: git pull origin main
2. Create branch: git checkout -b skill/csr-s11-add-interpretation-rule
3. Open skill file in Cursor
4. Use Cursor's AI chat to discuss the change:
   "I want to add a rule that Section 11 should interpret exposure duration 
    relative to the planned treatment period. Help me write this rule."
5. Cursor suggests the rule text — review it for domain accuracy
6. Edit the skill file directly
7. Run local eval: python run_eval.py --dataset csr-section-11 --mode quick
8. If pass: commit and push
   git add skills/mwa/csr-s11-authoring.md
   git commit -m "skill: add exposure interpretation rule to S11"
   git push origin skill/csr-s11-add-interpretation-rule
9. Create PR using the template
10. Wait for engineer review + CI checks
```

**What non-engineers should NOT do in Cursor:**
- Don't modify Python files beyond simple variable changes
- Don't change import statements or dependencies
- Don't modify CI/CD configs, Dockerfiles, or infrastructure files
- Don't resolve merge conflicts on code files (ask an engineer)
- Don't use `git push --force` ever

*These are examples of high-risk areas, not an exhaustive list. When in doubt, ask an engineer before modifying unfamiliar file types.*

### 1.6 Engineer Review Checklist for AI-Generated Code

When reviewing code contributed by non-engineers (often generated via Cursor/Claude):

- [ ] **Does it do what the PR says it does?** Read the diff, not just the PR description
- [ ] **No unintended side effects?** Check if the change affects other files or flows
- [ ] **No hardcoded values?** API keys, file paths, model names should be config-driven
- [ ] **No security issues?** Client data not logged, no secrets in code
- [ ] **Eval results look real?** Check that eval was actually run (not just checkbox ticked)
- [ ] **Performance OK?** For code changes: no unnecessary API calls, no unbounded loops
- [ ] **Style consistent?** Follows existing patterns in the codebase
- [ ] **Commit history clean?** No "fix typo" x10 commits — squash if needed

### 1.7 Conflict Resolution

- **Same skill, different changes:** Second PR to merge must rebase on latest main, re-run evals, and verify the combined effect
- **Competing approaches to same problem:** Escalate to solutioning workshop — don't resolve in PR comments
- **Engineer + non-engineer disagree on implementation:** Engineer has final say on code; SA has final say on domain content

### 1.8 Preventing Non-Engineers from Breaking Things

**Guardrails built into the system:**

1. **Branch protection rules on GitHub:** `main` is protected — no direct pushes, require PR reviews, require status checks to pass before merge. This is the single most important guardrail and works on any GitHub plan (Free, Team, or Enterprise).

2. **CODEOWNERS file:** Maps directories to required reviewers. Note: CODEOWNERS enforcement (automatically requiring reviews from the listed owners) requires GitHub Team plan or higher. On GitHub Free, CODEOWNERS serves as documentation of who should review, but is not automatically enforced — engineers must manually check that the right people have approved.
   ```
   /infrastructure/    @engineer-team
   /deployment/        @engineer-team
   /pipeline/*.py      @engineer-team
   /skills/            @solution-architect @engineer-team    # Both SA and engineer
   /knowledge-bases/   @solution-architect                   # SA sufficient
   /eval-datasets/     @solution-architect @qc-team          # SA or QC sufficient
   ```

3. **Pre-commit hooks (local):** Installed via `pre-commit` framework on each developer's machine. Blocks commits that modify protected file types (`.py`, `.yml`, `Dockerfile`) unless the committer is an engineer. Limitation: these run locally and can be bypassed. They are a safety net, not a security boundary.

4. **CI checks on PR:** Any PR that touches `.py`, `.yml`, `Dockerfile`, or `requirements.txt` is flagged automatically in the CI output. Engineers must verify these before approving.

**What to set up first (priority order):**
1. Branch protection on `main` (day 1 — takes 5 minutes in GitHub settings)
2. PR template (day 1 — add `.github/PULL_REQUEST_TEMPLATE.md`)
3. Pre-commit hooks (week 1 — `pre-commit` framework with basic checks)
4. CODEOWNERS file (week 1 — immediate documentation value even without enforcement)
5. CI checks (see Section 2 — phased rollout)

---

## 2. Testing Strategy (3-Tier)

### Tier 1: Automated Code Checks (Every Commit)

**Runs on:** Every push to any branch. ~30 seconds. $0 cost.

| Check | Tool | Blocks Merge? |
|-------|------|--------------|
| Python syntax validation | `py_compile` / `ruff` | Yes |
| Skill file schema validation (frontmatter has required fields) | Custom script | Yes |
| KB file JSON schema validation | `jsonschema` | Yes |
| No secrets in code (.env, API keys, passwords) | `detect-secrets` / `gitleaks` | Yes |
| No client data in universal files | Custom grep for client identifiers | Yes |
| Markdown lint for skill files | `markdownlint` | Warning only |
| Import check (no unused imports, no missing deps) | `ruff` | Yes |
| Eval dataset schema validation | Custom script | Yes |

**Phased CI rollout — the team may not have GitHub Actions set up today.** Do not try to build the full pipeline on day 1. Instead:

| Phase | What | When | How |
|-------|------|------|-----|
| **Phase 0: Local only** | Pre-commit hooks run Tier 1 checks on each developer's machine. No CI server needed. | Week 1 | `pre-commit` framework. Engineer sets up once, everyone installs with `pre-commit install`. |
| **Phase 1: Basic CI** | GitHub Actions runs Tier 1 checks on every PR. Single workflow file, no secrets needed. | Week 2-3 | See workflow below. Requires GitHub Actions minutes (2,000 free/month on GitHub Free). |
| **Phase 2: Eval CI** | GitHub Actions runs Tier 2 LLM-as-Judge evals on PRs. Requires API key in GitHub Secrets. | Month 2 | See Tier 2 section. Requires storing the Anthropic API key as a GitHub Secret. |
| **Phase 3: Full pipeline** | Scheduled jobs, deployment triggers, cost monitoring in CI. | Month 3+ | Only after the team has stabilized on Phases 0-2. |

**Phase 1 GitHub Actions workflow (Tier 1 only — no secrets needed):**

```yaml
name: Tier 1 Checks
on:
  pull_request:
    branches: [main]

jobs:
  tier1-checks:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - name: Install check dependencies
        run: pip install ruff jsonschema detect-secrets
      - name: Run linting and schema checks
        run: python scripts/tier1_checks.py
```

**Note:** The `scripts/tier1_checks.py` script must be written by the engineering team. It should wrap the checks listed in the table above. Start simple — even just `ruff check .` and a JSON schema validation is valuable.

### Tier 2: LLM-as-Judge Evals (Every PR)

**Runs on:** Every PR to main. 5-10 minutes. $0.50-$2.00.

**Prerequisites:** This tier requires an API key stored in GitHub Secrets. Before enabling, an engineer must:
1. Create a service account API key (not a personal key) for CI use
2. Store it as `ANTHROPIC_API_KEY` in the repository's GitHub Secrets (Settings > Secrets and Variables > Actions)
3. Confirm the key has appropriate rate limits and spend caps

**GitHub Actions workflow (Phase 2):**

```yaml
name: PR Eval Check
on:
  pull_request:
    branches: [main]

jobs:
  tier1-checks:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run linting and schema checks
        run: python scripts/tier1_checks.py

  tier2-eval:
    needs: tier1-checks
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Identify changed skills/KBs
        id: changes
        run: python scripts/identify_eval_targets.py
        # Outputs which eval datasets need to run based on changed files
      
      - name: Run quick eval
        if: steps.changes.outputs.eval_needed == 'true'
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          python run_eval.py \
            --datasets ${{ steps.changes.outputs.datasets }} \
            --mode quick \
            --output results/eval_report.json
      
      - name: Check thresholds
        run: python scripts/check_thresholds.py results/eval_report.json
        # Fails if any score below threshold
      
      - name: Post results to PR
        uses: actions/github-script@v7
        with:
          script: |
            const report = require('./results/eval_report.json');
            // Format and post as PR comment
```

**Before Phase 2 is ready:** Run Tier 2 evals manually. The PR author runs `python run_eval.py --mode quick` locally and pastes the output into the PR description. The reviewing engineer verifies the results are plausible. This is imperfect but better than nothing, and it builds the habit before automation arrives.

**Handling flaky evals (LLM non-determinism):**
- Run each eval row 2x. If scores differ by >0.3, run a 3rd time and take median.
- If the same row is flaky across 3+ PRs, investigate: is the rubric ambiguous? Is the row poorly defined?
- Track flaky rows in a `flaky_evals.json` — these get flagged for human review rather than blocking merge.
- Temperature set to 0 for all eval judge calls (maximum determinism).

### Tier 3: Human Review (Weekly)

**Frequency:** Weekly, or per-sprint (whichever is shorter).

**Process:**
1. System generates 10 outputs from the latest production skill versions, using inputs sampled from:
   - 3 easy inputs
   - 4 medium inputs
   - 3 hard inputs
2. QC team reviews all 10 without seeing LLM-as-Judge scores
3. QC scores each output on all dimensions using the same rubric
4. Compare human scores vs. LLM-as-Judge scores from the same outputs
5. Document: agreement rate, systematic biases, new failure patterns
6. New failure patterns become new eval dataset rows

**Output:** Weekly quality report (1-page summary):
- Average quality score this week vs. last week
- Any new failure patterns identified
- LLM-Judge vs. Human agreement rate
- Recommendations: skill changes needed, KB updates, eval dataset additions

---

## 3. Deployment Pipeline

### 3.1 Environment Progression

```
Local Dev --> Shared Dev --> Staging --> Production
   |              |            |           |
   |              |            |           +-- Real client data, real traffic
   |              |            +-- Full eval suite, client-specific datasets
   |              +-- Integration testing, team visibility
   +-- Individual testing, quick iteration
```

| Environment | Who Has Access | Data | Eval Level | Deployment |
|-------------|---------------|------|-----------|-----------|
| Local Dev | Individual developer | Synthetic/sample data | Tier 1 + Tier 2 quick | Automatic (local run) |
| Shared Dev | Full GenAI team | Anonymized client data | Tier 2 full eval | Push to branch triggers |
| Staging | GenAI team + Engineering | Client data (restricted) | Full eval + hold-out | Manual trigger after Build Gate |
| Production | Monitored access only | Live client data | Continuous monitoring | Manual trigger after Deploy Gate |

### 3.2 Environment Parity — Closing the Local-vs-Production Gap

A common failure mode: the pipeline works locally but behaves differently in staging or production. This happens because environments silently differ in configuration, model access, data format, or dependencies.

**Known divergence points and mitigations:**

| Divergence | What goes wrong | Mitigation |
|-----------|----------------|-----------|
| **Python/dependency versions** | Code works on dev machine (Python 3.11) but fails in container (Python 3.10) | Pin Python version in a `.python-version` file. Use `pip freeze > requirements.txt` for exact dependency versions. All environments install from the same `requirements.txt`. |
| **Model access** | Dev uses personal API key with different rate limits or model access than production service account | Use environment variables for all API keys. Document which models each environment has access to. Local dev and CI use the same model version string from a shared config file (`config/models.yaml`). |
| **Data format** | Local tests use clean sample data; production receives messy client PDFs with OCR artifacts, broken tables, unexpected encodings | Eval datasets must include at least 2-3 rows with "messy" real-world inputs (redacted client data or synthetic equivalents). Do not only test on clean samples. |
| **File paths / OS differences** | Hardcoded paths, Windows vs. Linux path separators | Use `pathlib` for all file paths. Never hardcode absolute paths. CI runs on Linux (same as production). |
| **Environment variables** | Missing or differently-named env vars between environments | Maintain a `.env.example` file listing all required environment variables (without values). CI startup script validates all required vars are set before running. |
| **Secrets** | API keys passed differently (env var locally, Secrets Manager in production) | Use a single config loading pattern that checks (in order): env var, secrets manager, config file. Same code path in all environments. |

**Validation step before staging promotion:** Run the full eval suite inside the staging container (not just locally). If scores differ from local by more than 0.05 on weighted average, investigate before proceeding.

### 3.3 Skill/KB Version Management Across Environments

```
skills/mwa-csr-s11-authoring.md
  Metadata:
    version: 2.1.0
    environment_labels:
      dev: 2.2.0-beta    # Latest experimental version
      staging: 2.1.0      # Approved for staging testing
      production: 2.0.3   # Current production version
```

**Promotion flow:**
1. Developer merges skill v2.2.0-beta to main -- automatically tagged `dev`
2. Build Gate passed -- Solution Architect promotes to `staging`: `python promote.py --skill mwa-csr-s11 --to staging`
3. Deploy Gate passed -- Leadership approves promotion to `production`

### 3.4 Deployment to Client Environments

The GenAI team does not control deployment end-to-end. Production deployment currently goes through a separate AWS/DevOps team via email request with unpredictable turnaround. This is a structural constraint, not a process failure — but it must be managed explicitly.

**Current reality:**
- The GenAI team has no direct access to production infrastructure
- Deployments are requested via email or ticket to the DevOps team
- Turnaround is unpredictable (hours to days)
- The GenAI team cannot independently verify production state after deployment

**Process to manage this:**

1. **Standardized deployment request:** Use a template for every deployment request to reduce back-and-forth.
   ```
   Subject: Deployment Request — [Project] — [Environment]
   
   What: [Brief description of what is being deployed]
   Artifact: [Git tag or commit SHA, container image tag, or S3 path]
   Environment: [staging / production]
   Config changes: [Any env var changes, new secrets needed, infrastructure changes]
   Rollback plan: [How to revert — specific previous version/tag]
   Urgency: [Routine / Expedited (client-facing deadline) / Emergency (production down)]
   Requestor: [Name]
   Approver: [Leadership name for production deployments]
   
   Pre-deployment checklist:
   - [ ] Full eval suite passes at threshold
   - [ ] Rollback version identified and tested
   - [ ] No new infrastructure dependencies (or they are listed above)
   ```

2. **Turnaround expectations:** Agree with the DevOps team on SLAs:
   - Routine: 2 business days
   - Expedited: same business day
   - Emergency: 2 hours
   
   If these SLAs are not met, escalate per the escalation path in the Cross-Cutting Operations doc (L3 to Director, who escalates to leadership if DevOps is unresponsive for >2 days).

3. **Post-deployment verification:** After the DevOps team confirms deployment, an engineer must:
   - Run 3-5 smoke test requests against the deployed environment
   - Verify the deployed version matches the requested version (check a `/health` or `/version` endpoint)
   - Confirm monitoring is receiving data

4. **Client-cloud deployments:** Some clients require deployment into their own AWS accounts or VPCs. For these engagements:
   - Document the client's deployment process during Stage 1 (requirements gathering)
   - Identify who on the client side approves deployments
   - Build deployment artifacts (container images, config bundles) that are portable — not tied to Indegene's specific AWS account or VPC
   - Plan for longer deployment cycles (client IT review, security scanning, change management)
   - Include client deployment lead in the weekly engineering sync when deployments are active

### 3.5 Step-by-Step Rollback Procedure

```
1. DETECT: Monitoring alert fires (quality drop, error spike, latency increase)
   |
2. ASSESS (5 minutes max):
   - Is this affecting live client work? If yes -- proceed immediately
   - Is this a model issue or a skill/code issue?
   |
3. ROLLBACK (engineer executes):
   a. Identify last known-good version from deployment log
   b. Run: python rollback.py --skill mwa-csr-s11 --to-version 2.0.3
      - This updates the production label to the previous version
      - No code deployment needed if skills are dynamically loaded
   c. If pipeline code change caused the issue:
      git revert <commit-hash>
      # Fast-track PR: engineer self-approves in emergency, second engineer reviews within 4 hours
   d. Verify: run 3 production requests with rolled-back version, check quality
   |
4. COMMUNICATE:
   - Notify team in Slack/Teams channel within 15 minutes
   - If client-facing: notify client contact with ETA for resolution
   |
5. ROOT CAUSE (within 24 hours):
   - Why did the change pass all eval gates but fail in production?
   - Add the failure case to the eval dataset
   - Update the process if a gate was insufficient
   |
6. FIX FORWARD:
   - Fix the original change on a new branch
   - Must pass all gates INCLUDING the new eval row from step 5
   - Standard PR process (not fast-tracked)
```

**Rollback when deployment goes through DevOps team:** If the GenAI team cannot execute rollback independently (because they lack production access), the rollback request to DevOps uses the same deployment request template with urgency marked "Emergency." The rollback artifact (previous version tag) must always be pre-identified in the original deployment request. Do not wait for a production incident to figure out what the rollback target is.

### 3.6 Model Version Pinning

**Policy:**
- Every deployment config specifies exact model version: `claude-sonnet-4-5-20250929` — never `claude-sonnet-4-5-latest`
- Model version is stored in a central config file, not per-skill
- Model upgrade is treated as a deployment: full eval suite must pass on the new version before swapping

**Model upgrade process:**
1. New model version released by provider
2. Engineer updates model version in dev config only
3. Run full eval suite on all product areas against new model
4. Compare scores: new model vs. current production model
5. If parity or improvement on all dimensions -- promote to staging
6. 1-week soak in staging with monitoring
7. Leadership approves production promotion
8. Record: model version, eval comparison results, approval date

**Fallback on model outage:**
- Primary: Claude Sonnet 4.5
- Fallback: Claude Sonnet 4 (previous generation)
- Emergency: Gemini or GPT-4o (requires separate eval validation)
- Config supports model priority list; system auto-falls to next if primary returns errors

---

## 4. Production Monitoring

### 4.1 Metrics to Track

*These are suggested metrics to track. The specific metrics and thresholds should be refined based on actual production experience and team discussion.*

| Category | Metric | Target | Alert Threshold |
|----------|--------|--------|----------------|
| **Quality** | Eval pass rate (automated spot checks) | >85% | <80% for 2 consecutive checks |
| | Data accuracy (programmatic check on sample) | 100% | Any failure |
| | Hallucination rate (detected fabricated data) | <2% | >5% |
| **Performance** | Latency p50 | <5 min per section | p50 >8 min |
| | Latency p95 | <15 min per section | p95 >25 min |
| | Agent completion rate | >95% | <90% |
| **Cost** | Cost per section authored | <$5 | >$10 |
| | Daily API spend | <$50 | >$100 |
| **Reliability** | Error rate (pipeline failures) | <5% | >10% |
| | Agent stall rate (agents that hang) | <2% | >5% |

### 4.2 Monitoring Tooling — Phased Approach

The team currently has no observability tooling in place. Do not attempt to set up CloudWatch dashboards, Langfuse tracing, and PagerDuty alerting all at once. Phase it.

| Phase | What | Cost/Effort | When |
|-------|------|-------------|------|
| **Phase 0: Structured logging** | Every pipeline run logs to a structured JSON file (or CloudWatch Logs if available). Each log entry includes: run_id, skill_id, skill_version, model, latency, token_count, error (if any), cost estimate. | Free (just code). Engineer: 1-2 days. | Week 1 of production. |
| **Phase 1: Daily summary script** | A cron job (or scheduled GitHub Action) that reads logs from the past 24 hours and posts a summary to the team Slack/Teams channel: total runs, error rate, average latency, total cost. | Free. Engineer: 0.5 day. | Week 2. |
| **Phase 2: Alerts** | Threshold-based alerts. If error rate > 10% or cost > $100/day, post an alert to the team channel. Start with a simple Python script checking the structured logs, not a full alerting platform. | Free. Engineer: 0.5 day. | Week 3. |
| **Phase 3: Dashboard** | If the volume of production runs justifies it, set up a lightweight dashboard (Grafana on a free tier, or a shared spreadsheet auto-updated daily). Only do this if Phase 1 summaries are insufficient. | Grafana free tier or $0. Engineer: 1-2 days. | Month 2+. |
| **Phase 4: Tracing** | Langfuse or similar LLM observability platform for per-request tracing (see which agent called which model, what tokens were used, where latency was spent). Valuable but only necessary once the team is running >50 production requests/week. | Langfuse self-hosted (free) or cloud ($50-200/month). Engineer: 2-3 days. | Month 3+. |
| **Phase 5: Alerting platform** | PagerDuty or Opsgenie for on-call routing. Only necessary if the team reaches a point where production incidents require after-hours response. See Section 4.3 for why this is not needed today. | $20+/user/month. | When justified. |

**The key principle:** Start with structured logs and a daily summary. Everything else is optimization. If the team cannot answer "how many runs did we do yesterday, how many failed, and how much did it cost?" then that is the first problem to solve.

### 4.3 Monitoring Cadence

| Check | Frequency | Who Reviews | Tool |
|-------|-----------|------------|------|
| Daily summary (runs, errors, cost) | Daily (automated) | Engineering lead glances at it | Phase 1 script (see above) |
| Quality spot check (sample 5 recent outputs, run LLM judge) | Daily (automated when Tier 2 CI is in place) | Solution Architect reviews report | `run_eval.py` on production outputs |
| Cost dashboard review | Daily | Engineering lead | AWS Cost Explorer or structured logs |
| Weekly quality report (Tier 3 human review) | Weekly | Solution Architect + QC team | Manual + template |
| Full production eval (run complete eval suite on production system) | Bi-weekly | Full team reviews | CI/CD scheduled job (Phase 3+) |

### 4.4 Incident Response

**On-call reality check:** This is a 10-person team with 2 engineers. There is no dedicated on-call rotation, and there should not be one — it would burn out the engineers. Instead, the team uses a "business hours first responder" model.

**Who responds:**
- **Business hours (9 AM - 6 PM, Mon-Fri):** Whichever engineer is not in a meeting or deep-focus block picks up the alert. If both are unavailable, the Solution Architect triages and decides whether it can wait.
- **After hours:** Alerts accumulate. They are reviewed first thing the next business day. If the system is producing outputs overnight (batch processing), the batch is paused automatically on error and resumed after review.
- **Exception — SEV-1 during active client delivery:** If a client is actively waiting on output and the system is down, the engineer who is reachable responds. This should be rare (less than once a quarter). If it becomes frequent, escalate to leadership as a resourcing issue.

**Severity levels:**

| Severity | Definition | Response Time | Who |
|----------|-----------|--------------|-----|
| **SEV-1** | Client-facing system down; data accuracy failure in live output | Next business hour (or immediately if during active delivery) | Engineer + Solution Architect + Leadership notified |
| **SEV-2** | Quality degradation detected (eval scores dropping); system slow but functional | 4 business hours | Engineer + Solution Architect |
| **SEV-3** | Non-client-facing issue; performance degradation; cost spike | Next business day | Engineer |
| **SEV-4** | Minor issue; cosmetic; non-urgent improvement | Next sprint | Whoever owns the area |

**Process:**

```
Detection (automated alert or human report)
  |
Triage (5 min): Classify severity, assign owner
  |
Diagnose: Is this...
  +-- Model degradation? --> Check model version, run eval on current model, compare to baseline
  +-- Skill bug? --> Check recent skill changes, compare outputs before/after last deployment
  +-- Data issue? --> Check input data quality, source document parsing
  +-- Infrastructure issue? --> Check AWS health, API quotas, network
  +-- Unknown? --> Collect logs, traces, reproduce, escalate
  |
Fix: Apply fix or rollback (see 3.5)
  |
Verify: Confirm fix resolves the issue
  |
Communicate: Update stakeholders
  |
Postmortem (within 48 hours for SEV-1/2):
  - What happened?
  - Why did it get past our gates?
  - What eval row / monitoring check would have caught it?
  - Action items with owners and deadlines
```

---

## 5. Security

### 5.1 API Key and Secrets Management

The team handles API keys for LLM providers, client data, and deployment credentials. Mishandling any of these is a client trust and compliance risk.

**Rules:**

| Rule | Detail |
|------|--------|
| **No secrets in code, ever** | API keys, passwords, tokens must never appear in source code, config files committed to git, or PR descriptions. Use environment variables or a secrets manager. |
| **`.env` files are gitignored** | The `.gitignore` must include `.env`, `.env.*`, `*.pem`, `credentials.json`, and similar patterns. Verify this on day 1. |
| **Secrets scanning in CI** | Tier 1 checks include `detect-secrets` or `gitleaks` (see Section 2). This catches accidental commits before they reach main. |
| **Separate keys per environment** | Dev, staging, and production use different API keys. If a dev key is compromised, production is not affected. |
| **Service accounts for CI** | GitHub Actions uses a dedicated service account API key, not a personal key. This key has a spend cap matching the CI budget. |
| **No secrets in Slack/Teams** | Never paste an API key in a chat message. If someone needs a key, share it through the secrets manager or a short-lived secure link. |

**Secrets rotation schedule:**

| Secret | Rotation frequency | Who rotates | How |
|--------|-------------------|-------------|-----|
| LLM provider API keys (Anthropic, OpenAI, Google) | Every 90 days, or immediately if compromised | Engineer | Rotate in provider dashboard, update secrets manager, update CI secrets, verify all environments |
| AWS access keys (if used) | Every 90 days | Engineer | IAM console. Prefer IAM roles over access keys where possible. |
| GitHub personal access tokens | Every 90 days | Individual | GitHub Settings > Developer Settings. Use fine-grained tokens with minimum required permissions. |
| Client-specific credentials | Per client security policy | Engineer + client IT | Follow client's rotation procedure. Document in engagement runbook. |

**If a secret is accidentally committed:**
1. Rotate the secret immediately (generate a new key, revoke the old one)
2. Remove the secret from git history (engineer uses `git filter-branch` or BFG Repo Cleaner)
3. Notify leadership if the secret had access to client data or production systems
4. Add a post-mortem entry: why did the pre-commit hook not catch it?

### 5.2 Client Data in CI/CD and Development

Pharma client data is sensitive (patient-level clinical trial data, proprietary SOPs, unpublished study results). It must not leak through CI/CD pipelines, logs, or development environments.

**Rules:**

| Context | What is allowed | What is NOT allowed |
|---------|----------------|---------------------|
| **Eval datasets in git** | Synthetic data, anonymized data, publicly available clinical trial data | Real patient data, client-proprietary SOPs (reference them by ID, don't embed the content) |
| **CI/CD logs** | Eval scores, skill versions, error messages | Input document content, generated output text, client names in log messages |
| **Local development** | Anonymized or synthetic sample data | Real client documents on personal machines without client approval |
| **Shared dev environment** | Anonymized client data with access controls | Client data accessible to team members not on that engagement |

**For eval datasets that need real-world inputs:** Use redacted versions where patient identifiers, study drug names, and sponsor names are replaced with placeholders. The eval measures structural quality, not whether the system knows the real drug name.

### 5.3 Access Control

| Resource | Who has access | How access is granted |
|----------|---------------|----------------------|
| GitHub repository | Full GenAI team | GitHub org membership, managed by engineer |
| Production AWS environment | Engineers only (via DevOps team) | Deployment request process (see 3.4) |
| Staging environment | GenAI team + Engineering | AWS IAM roles, managed by DevOps |
| Client data (S3 buckets, shared drives) | Engagement team members only | Per-engagement access request, approved by engagement SPOC |
| LLM provider dashboards | Engineers + Leadership | Per-provider account management |
| Monitoring dashboards | Full GenAI team (read), Engineers (write) | Set up during Phase 2-3 of monitoring rollout |

**Offboarding:** When someone leaves the team, an engineer must within 24 hours: revoke GitHub access, rotate any shared secrets the person had access to, remove from engagement-specific data access. Maintain a checklist.

---

## 6. Cost Management

### 6.1 Tracking Granularity

Every LLM call is tagged with:
```json
{
  "project": "medcom-asset-generation",
  "client": "vertex",
  "skill_id": "medcom-visual-generation",
  "skill_version": "1.2.0",
  "stage": "production",  // or "eval", "auto-refinement", "development"
  "agent_id": "orchestrator-001",
  "run_id": "run-2026-05-01-001"
}
```

This allows cost slicing by: project, client, skill, stage, time period.

**Implementation note:** This tagging is aspirational if the team does not yet have observability tooling. At minimum, start with Phase 0 structured logging (see Section 4.2) that records the fields above. Cost tracking does not require a dashboard — a weekly script that parses the logs and outputs a summary is sufficient to start.

### 6.2 Budget Thresholds and Approvals

*Note: The thresholds below are provided as examples. Actual threshold values will be determined based on engagement-specific approvals and may change over time.*

| Spend Level | Approval Needed | Action |
|-------------|----------------|--------|
| <$10/day per project | None — within normal operations | Auto-approved |
| $10-50/day per project | Solution Architect reviews | Check if expected (e.g., bulk processing) or anomalous |
| $50-100/day per project | Leadership notified | Investigate root cause; likely auto-refinement or testing spike |
| >$100/day per project | Leadership approval to continue | Pause non-critical workloads; optimize before resuming |
| Any single run >$20 | Engineer reviews after the fact | Check for infinite loops, unnecessary agent spawning |

### 6.3 Cost Optimization Levers

| Lever | When to Use | Expected Savings |
|-------|------------|-----------------|
| **Model tiering** (Haiku for simple extraction, Sonnet for authoring, Opus for complex reasoning) | Always — default architecture | 40-60% vs. using Opus for everything |
| **Caching** (identical inputs return cached outputs) | For repeated evaluations, demo runs | 20-30% on eval runs |
| **Token reduction** (shorter prompts, structured outputs) | When cost per section exceeds target | 10-20% |
| **Batching** (process multiple sections in one context window) | For independent sections that can share context | 15-25% |
| **Early termination** (stop agent if quality sufficient before max iterations) | During auto-refinement | Varies — prevents runaway sessions |

### 6.4 Cost-Quality Tradeoff Decisions

**Who decides:** Solution Architect proposes, Leadership approves.

**Decision framework:**
- If cost reduction has <5% quality impact -- approve automatically
- If cost reduction has 5-10% quality impact -- discuss: is this threshold still acceptable for the client?
- If cost reduction has >10% quality impact -- reject unless client explicitly agrees to lower quality for lower price
- Document every cost-quality tradeoff decision in the engagement decision log

### 6.5 Reporting to Stakeholders

**Monthly cost report (to Leadership):**
- Total API spend by project
- Cost per output (e.g., cost per CSR section, cost per MedCom asset)
- Trend: is cost increasing or decreasing per output?
- Breakdown: production vs. eval vs. auto-refinement vs. development
- Comparison to manual cost (if available)
- Optimization actions taken and their impact

---

## 7. Federated Development, Central Governance

The leadership model is "federated development, central governance" — multiple people contribute, standards are enforced centrally. This document operationalizes that model. Here is how the pieces connect:

| Principle | How this document implements it |
|-----------|-------------------------------|
| **Anyone can contribute** | Section 1.3 (Who Can Do What) defines what each role can touch. Non-engineers modify skills, KBs, and eval datasets. Engineers modify code and infrastructure. |
| **Quality is centrally governed** | Section 2 (Testing Strategy) enforces 3-tier quality gates. No change reaches production without passing automated checks, LLM-as-Judge evals, and human review. |
| **Engineers are the gatekeepers, not the bottleneck** | Section 1.4 (PR Process) requires engineer approval on every merge, but engineers review — they do not do the work. Non-engineers do 80% of the skill/KB work. |
| **Standards are encoded, not oral** | CODEOWNERS (Section 1.8), PR templates (Section 1.4), eval thresholds (Eval doc Section 3.5), and CI checks (Section 2) encode the standards in tooling. A new team member cannot accidentally bypass them. |
| **Central visibility into all changes** | Every change goes through a PR. PRs include eval scores. The weekly quality report (Section 2, Tier 3) gives leadership a single view of quality across all product areas. |
| **Governance scales without adding people** | The CI pipeline (Section 2), structured logging (Section 4.2), and cost thresholds (Section 6.2) automate enforcement. As the team grows from 10 to 20, the same guardrails apply without doubling the number of reviewers. |

**What is NOT centrally governed (and should not be):**
- Which skill changes to make (decided by the Solution Architect owning the product area)
- How to interpret domain content (decided by the SA or SME, not the engineer)
- Client-specific conventions (decided per engagement, documented in client-specific KBs)

This is the balance: the **what** is federated (each person/engagement decides what to build), the **how** is governed (everyone follows the same PR process, eval gates, and deployment pipeline).
