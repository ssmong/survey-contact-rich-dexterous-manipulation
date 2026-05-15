# Systematic Survey Construction Prompt

> A reusable prompt template for building comprehensive, critically-reviewed academic surveys with Claude Code.
> Derived from a real survey construction process. Field-agnostic — works for any research domain.
> Hand this entire file to Claude Code along with your topic.

---

## How to Use

1. Copy this entire file into a Claude Code conversation (or reference it with `@Prompt_review.md`).
2. State your survey topic (e.g., "stochastic MPC for safe robotics", "diffusion models in drug discovery", "federated learning for medical imaging").
3. Claude will ask clarifying questions before starting, then proceed through the phases below.

---

## Phase 0: Scoping (ask the user)

Before any research begins, ask the user the following questions using the AskUserQuestion tool. Do NOT proceed until answers are collected.

### Q0. Permission Setup (do this FIRST, before asking questions)

Before asking ANY scoping questions, configure tool permissions so the survey workflow runs uninterrupted. Use the `update-config` skill to add these to the project `.claude/settings.json`:

```json
{
  "permissions": {
    "allow": [
      "WebFetch(domain:arxiv.org)",
      "WebFetch(domain:doi.org)",
      "WebFetch(domain:ieeexplore.ieee.org)",
      "WebFetch(domain:link.springer.com)",
      "WebFetch(domain:dl.acm.org)",
      "WebFetch(domain:openreview.net)",
      "WebFetch(domain:proceedings.mlr.press)",
      "WebFetch(domain:papers.nips.cc)",
      "WebFetch(domain:openaccess.thecvf.com)",
      "WebFetch(domain:sciencedirect.com)",
      "WebFetch(domain:linkinghub.elsevier.com)",
      "WebFetch(domain:github.com)",
      "WebFetch(domain:huggingface.co)",
      "WebFetch(domain:scholar.google.com)",
      "WebFetch(domain:semanticscholar.org)",
      "WebSearch",
      "Bash(curl *)"
    ]
  }
}
```

**Ask the user:** "Should I add these academic domain permissions to your project settings? This prevents permission popups during the survey. You can also add field-specific domains (e.g., `biorxiv.org` for biomedical, `ssrn.com` for economics)."

**Institutional access note:** WebFetch routes through Anthropic's servers, NOT your local network. If you have institutional access (e.g., university IP for paywalled IEEE/Springer papers), use `Bash(curl ...)` instead — curl runs locally and benefits from your institutional IP. The prompt will automatically fall back to curl for paywalled content when WebFetch returns 403/paywall.

### Q1. Topic & Scope
- What is the survey topic? (user already provided this)
- What are the 2-3 intersecting research threads the survey should map?
  - e.g., "stochastic optimization + MPC + safety constraints"
  - e.g., "protein structure prediction + generative models + experimental validation"
  - e.g., "multi-agent RL + communication + emergent behavior"
  - e.g., "neural radiance fields + dynamic scenes + real-time rendering"

### Q2. Time Window
- How far back should the survey go?
  - Options: Last 3 years / Last 5 years / Last 7 years / Custom range
  - Note: "foundational" papers outside the window can be included with justification

### Q3. Source Scope
- Which publication tiers to include?
  - Options:
    - Top-tier venues only (Q1 journals + A* conferences)
    - Top-tier + strong workshops/arXiv with high citations
    - Broad (Q1-Q2 journals + A/B conferences + notable arXiv)
  - Field-specific venue list will be established after initial search
  - **Excluded publishers (non-negotiable):**
    - **MDPI** (mdpi.com): Exclude all MDPI journals (Sensors, Energies, Electronics, Aerospace, Applied Sciences, etc.). Use `blocked_domains: ["mdpi.com"]` during searches. MDPI papers are not to be included in the survey.

### Q4. Gap Discovery Mode
- How should research gaps be identified?
  - **User-directed**: User specifies known gaps upfront; survey validates/refutes them
  - **Emergent**: Survey discovers gaps organically through capability mapping
  - **Hybrid**: User provides initial hypotheses; survey refines and discovers additional gaps

### Q5. Deliverable Structure
- What sections does the user want? Propose a default based on the topic, but let the user override. Typical structures:

**For methods-heavy topics** (e.g., stochastic MPC, Bayesian optimization, ADMM variants):
```
1. Problem Formulation Variants
2. Solution Methods (by algorithm family)
3. Theoretical Guarantees (convergence, safety, stability)
4. Applications & Benchmarks
5. Software / Implementations
6. Open Problems
```

**For systems-heavy topics** (e.g., surgical robotics, autonomous driving perception, warehouse automation):
```
1-N. Capability categories (by task type or method)
N+1. Foundation models / Large-scale approaches
N+2. Datasets & Benchmarks
N+3. Simulation Platforms
N+4. Hardware
N+5. Open Problems
```

**For intersection topics** (e.g., LLMs + chemistry, diffusion models + protein design, RL + compiler optimization):
```
1. Thread A survey
2. Thread B survey
3. Intersection A+B (the core contribution)
4. Datasets & Benchmarks
5. Open Problems
```

### Q6. Field-Specific Columns
- What metadata matters for this field? Propose defaults and let the user add/remove:
  - **Universal**: Paper, Group, Venue, Year, Code, Weights/Models
  - **Methods** (e.g., optimization, numerical methods): Theoretical guarantees?, Computational complexity, Scalability
  - **Systems** (e.g., robotics, autonomous vehicles): Hardware, Sim platform, Sim2Real, Real-world validated?
  - **ML/AI** (e.g., foundation models, generative AI): Model size, Training data, Inference speed, Open weights?
  - **Control** (e.g., MPC, adaptive control): Stability proof?, Real-time?, Constraint handling
  - **Biomedical** (e.g., drug discovery, medical imaging): Clinical validation?, Dataset size, Patient diversity, Regulatory status
  - **HCI/NLP** (e.g., dialogue systems, accessibility): User study?, Sample size, Languages tested, Ethical review

### Q7. Output Language
- What language should the final deliverables be written in?
  - Options: English / Korean / Chinese / Japanese / Other
  - Note: Paper titles and technical terms remain in English regardless of output language

### Table Formatting Rules (non-negotiable)

These rules apply to ALL tables in survey.md. Enforce strictly.

1. **Column order must be consistent** within each section. Once a table header is defined, every row follows the same column order. Do NOT reorder columns between rows.

2. **Venue column = venue name only.** Do NOT include the year in the Venue column (e.g., write `NeurIPS` not `NeurIPS 2025`). The year is already in the dedicated Year column.

3. **Paper column = hyperlinked title.** Use the paper's DOI or arXiv link as the hyperlink target:
   - Preferred: `[**Paper Name**](https://doi.org/10.xxxx/xxxxx)` (DOI is permanent)
   - Fallback: `[**Paper Name**](https://arxiv.org/abs/XXXX.XXXXX)` (if no DOI)
   - No link: `**Paper Name**` (if neither DOI nor arXiv exists)

4. **All hyperlinks must be verified.** After building each table, batch-verify all links with HTTP status checks. Re-verify after any edit pass.

5. **Year column = integer only.** Just the publication year (e.g., `2025`), not `2025a` or `2025 (preprint)`.

---

## Phase 1: Initial Survey Construction

### Step 1.1: Seed Paper Discovery
```
Search strategy (parallel agents):
1. Search "[topic] survey 202X" for existing surveys — extract their reference lists
2. Search "[topic] [key_method]" for each sub-area
3. Search top venues in the field for recent accepted papers
4. Search Google Scholar / Semantic Scholar for highly-cited papers in the time window
5. Check "Awesome-[topic]" GitHub lists if they exist
```

### Step 1.2: Build the Main Table
For each paper found:
- Fetch arXiv/DOI page
- Extract: title, authors, venue, year, and field-specific columns from Q6
- Verify code/data links are accessible (HTTP status check)
- Add to the survey.md main table

### Step 1.3: Create Detailed Entries
For each paper, create an individual .md file under `detailed_survey/sectionN/paper_name.md` containing:

```markdown
# Paper Name

**Full title:** ...
**Authors:** First Author et al. (Affiliation)
**Venue/Year:** ...
**arXiv/DOI:** ...

## Key Methodology
2-3 sentence summary of the core approach. State what is NEW vs prior work.

## [Field-Specific Sections]
(Adapted from Q6 — e.g., Theoretical Guarantees, Hardware, Architecture)

## Main Contributions
- Contribution 1 (state delta over prior work, not method description)
- Contribution 2
- Contribution 3

## Limitations / Gaps
- [Dimension 1 from the consistency checklist — see Phase 3]
- [Dimension 2]
- ...

## Results
| Task/Benchmark | Metric | Value | Context |
|----------------|--------|-------|---------|
| ... | ... | ... | (sim)/(real)/(theoretical) |

## Inference / Deployment (if applicable)
- Inference latency, hardware, real-time capability

## Dataset / Data (if applicable)
- Dataset used, collection method, scale, availability
```

### Step 1.4: Cross-Cutting Observations
For each section, create `_overview.md` with:
- Paper index table
- 5-10 cross-cutting observations identifying patterns, trends, and gaps
- Every observation must be verifiable against individual entries

---

## Phase 1.5: PDF Collection

### Step 1.5.1: Automated Download (`scripts/download_papers.py`)

PDFs are saved in the `docs/reference/` folder using the format `{Year}_{Journal}_{Title}.pdf`.

**Access method by publisher:**

| Publisher | Method | Tool |
|-----------|--------|------|
| **arXiv** | Direct download | `urllib` (`https://arxiv.org/pdf/{id}`) |
| **IEEE** (TAC, TRO, TAES, RA-L, etc.) | Playwright headless → DOI redirect → extract `xplGlobal.document.metadata.arnumber` → `stampPDF/getPDF.jsp` | `playwright` (channel=chrome, headless, User-Agent spoof) |
| **Springer** | Direct PDF URL with User-Agent header | `urllib` + `User-Agent: Mozilla/5.0...` |
| **Elsevier** (Automatica, Acta Astronautica, Aerospace Sci Tech, etc.) | **Manual download** (cannot bypass Cloudflare Turnstile bot detection) | Provide DOI/URL list to user → user downloads via browser |

**Elsevier manual download process:**
1. After running the script, print the Elsevier paper list (filename, DOI, URL) to the console
2. User opens each URL in Chrome and downloads the PDF
3. Rename files to the `{Year}_{Journal}_{Title}.pdf` format and save to `docs/reference/`
4. Claude reads the local PDFs using the Read tool and incorporates them into the survey

**IEEE access details:**
- `channel='chrome'` (uses system Chrome to evade bot detection)
- `--disable-blink-features=AutomationControlled` flag
- DOI → IEEE document page → extract arnumber from `window.xplGlobal.document.metadata` JSON
- Download PDF from `stampPDF/getPDF.jsp?tp=&arnumber={arnumber}&ref=`

**Note:** IEEE Xplore blocks direct HTML crawling by headless browsers (returns a 12KB JS shell), but metadata becomes accessible after DOI redirect followed by waiting for JS rendering (8 seconds). PDFs are downloaded as binary via the Playwright request API.

---

## Phase 2: Fact & Metadata Verification

> **Note:** Since PDFs have already been downloaded to `docs/reference/` in Phase 1.5, HTTP verification of arXiv/DOI links themselves is unnecessary. Phase 2 focuses on **the accuracy of survey descriptions relative to actual paper content**.

### Step 2.1: Venue Verification & File Renaming
Many papers downloaded from arXiv have actually been published at conferences or in journals. Cross-reference the PDF first page and Google Scholar to confirm the actual venue, then update the filename and survey.md table accordingly.

```
For each paper with "arXiv" in the filename:
1. Search the paper title on Google Scholar to confirm the actual publication venue
   - arXiv PDFs always display only arXiv, so checking the PDF first page alone is insufficient
   - WebSearch query: "{paper title}" site:scholar.google.com
   - Or CrossRef API: curl https://api.crossref.org/works?query.title={title}&rows=1
2. If published at a conference/journal:
   a. Rename file: "2024, arXiv, ..." → "2024, IEEE TCST, ..."
   b. Update the Venue column in the survey.md table
   c. Update Venue/Year in the corresponding detailed_survey/ file
   d. If the publication year differs from the arXiv submission year, update to the publication year
3. If still a preprint, keep as arXiv
```

**Filename format:** `{Year}, {Journal}, {Title}.pdf`
- IEEE journals: `IEEE TAC`, `IEEE TRO`, `IEEE TAES`, `IEEE RA-L`, `IEEE TCST`, etc.
- IEEE conferences: `CDC`, `ACC`, `ICRA`, etc.
- Other journals: journal name only without publisher (`Automatica`, `Acta Astronautica`, etc.)
- Unpublished preprints: `arXiv`

### Step 2.2: Metadata Verification (PDF cross-check)
Open the downloaded PDFs using the Read tool and cross-check against the survey.md table metadata:
- **Authors/Group**: Are the author list and affiliations accurate?
- **Constraint type**: Does the constraint type listed in the table match what the paper actually uses?
- **Stability/Real-time/Scalability**: Does the table match what the paper actually proves/demonstrates?

### Step 2.3: Code/Data Link Verification
```
Only for papers marked Code = "Yes" in survey.md:
1. If a GitHub/GitLab URL exists, use WebFetch to verify the repo exists and check its contents
2. If it does not exist, change Code to "No"
```

### Step 2.4: Results Verification
Cross-check the Results tables in individual paper .md files against the original PDFs:
- Are the specific numbers actually reported in the paper?
- Are the (sim)/(real)/(theoretical) labels accurate?
- Replace vague expressions like "improved" or "reduced" with specific numbers

---

## Phase 3: Objectivity & Consistency Review

This is the most critical phase. Run review agents in parallel, one per section group.

### 3.1: Consistency Checklist
Define a set of **limitation dimensions** that EVERY paper in the survey must address. These are field-specific. Examples:

**For robotics/manipulation:**
- Force/impedance awareness (yes/no)
- Dexterous hand support (yes/no/partial)
- Sim-to-real transfer (yes/no/not applicable)
- Real-world validation scope (# objects, # tasks, # trials)
- Code/weights availability

**For control theory (e.g., MPC, adaptive control, robust control):**
- Stability guarantee (yes/no, what type: Lyapunov, ISS, etc.)
- Computational complexity (real-time feasible?)
- Constraint satisfaction (hard/soft/probabilistic)
- Scalability (state/input dimensionality tested)
- Comparison with baselines (which, fair?)

**For ML/AI (e.g., foundation models, generative models, RL):**
- Training data requirements
- Generalization tested? (in-distribution / OOD / zero-shot)
- Computational cost (training + inference)
- Reproducibility (code, data, hyperparams released?)
- Comparison fairness (same data splits, same compute budget?)

**For biomedical/clinical (e.g., drug discovery, imaging, genomics):**
- Clinical validation stage (in silico / in vitro / in vivo / clinical trial)
- Dataset diversity (patient demographics, multi-site?)
- Comparison to clinical standard of care
- Regulatory pathway addressed?
- Ethical approval / IRB status

**For NLP/HCI (e.g., dialogue, translation, accessibility):**
- Languages / domains tested
- User study conducted? (sample size, statistical test)
- Bias/fairness evaluation
- Real-world deployment evidence
- Ethical considerations discussed?

**For physics/simulation (e.g., CFD, molecular dynamics, climate):**
- Physical fidelity (validated against experiment?)
- Computational scaling (strong/weak scaling)
- Resolution / accuracy tradeoff
- Open-source solver?
- Reproducibility (input files, parameters shared?)

Adapt these to your specific field. The key principle: define dimensions BEFORE reviewing, then apply uniformly.

Every paper file MUST address every dimension. If a dimension doesn't apply, explicitly state "Not applicable because [reason]."

### 3.2: Review Criteria (per paper)

**A. Contributions — are they honest deltas?**
- Does each contribution state what is NEW vs prior work?
- Remove: "first", "pioneering", "novel", "groundbreaking", "state-of-the-art" unless:
  - Backed by comparative data, AND
  - Scoped precisely (e.g., "among the first RL-based approaches to X with sim-to-real transfer")
- Replace unqualified "First X" with: "Proposes X" or "Among the first to demonstrate X"
- Contributions must NOT restate the abstract — they must state the delta

**B. Limitations — are real gaps captured?**
- Apply ALL dimensions from the consistency checklist
- Use standardized wording for recurring limitations:
  - `> **Limitation ([dimension]):** [Standard text]`
- Flag if a paper claims generality but tests narrowly
- Flag if a paper claims "real-world" but tests on <5 objects in controlled settings
- Flag computational requirements if unusually high

**C. Results — are numbers real?**
- Every result must be a specific number, not "improved performance" or "strong results"
- If numbers unavailable: "Quantitative results: specific values not reported in the paper"
- Label every result: (sim), (real), (theoretical)
- For comparative results: state the baseline, the metric, and the margin
- Flag success rates presented without: trial count, object count, or success criterion

**D. Paper narrative bias**
- Are contributions taken directly from the paper's abstract without critical evaluation?
- Are "First X" claims verified or at least attributed ("per the authors")?
- Are papers from prestigious labs treated more favorably than equivalent work from smaller groups?

### 3.3: Review Execution
```
Launch parallel review agents (one per 2-3 sections):
- Each reads ALL files in assigned sections
- Checks every criterion above
- Reports: file, section, problematic text, suggested fix, severity
- Severity levels: CRITICAL (factual error / misleading) / MEDIUM (inconsistency) / MINOR (style)
```

### 3.4: Fix Application
```
Launch fix agents to apply all reported issues:
- CRITICAL fixes: apply immediately
- MEDIUM fixes: apply in batch
- MINOR fixes: apply if time permits
```

### 3.5: Final Verification Pass
After fixes, run one more review pass to verify:
- All CRITICAL issues resolved
- No new issues introduced by fixes
- Cross-cutting observations still accurate after individual entry changes
- Counts and categorizations in overview files match individual entries

---

## Phase 4: Missing Paper Discovery

### Step 4.1: Reference-Based Discovery
```
Launch parallel agents (one per section group):
1. For each paper in the survey, search for papers it cites and papers that cite it
2. Check existing survey papers in the field for papers they cover but we don't
3. Search "[topic] [year]" for recent top-venue publications
4. For each candidate, check: Is it within scope? Within time window? Already included?
5. Report: title, authors, venue, year, arXiv, which section, importance (critical/important/nice-to-have)
```

### Step 4.2: Gap-Based Discovery
```
For each gap identified in Phase 3 cross-cutting observations:
1. Search whether any paper addresses this gap
2. If found: add to survey
3. If not found: confirm as genuine open problem
```

### Step 4.3: Integration
```
For each missing paper to add:
1. Add row to survey.md table
2. Create detailed file with all standard sections
3. Update section _overview.md counts and observations
4. Run objectivity review on new entries only
```

---

## Phase 5: Enrichment (field-dependent, ask user)

Some enrichment passes are field-specific. Ask the user which apply:

### 5.1: Inference / Deployment (for ML/robotics)
- Add `## Inference / Deployment` to each paper:
  - Inference latency (ms, Hz)
  - Deployment hardware (GPU model, edge device)
  - Real-time capability assessment
  - Training hardware is optional (note but don't emphasize)

### 5.2: Dataset / Data Collection (for data-driven methods)
- Add `## Dataset / Data Collection` to each paper:
  - Dataset name (custom vs established benchmark)
  - Collection method (teleop, simulation, human video, MoCap, procedural)
  - Scale (episodes, hours, trajectories)
  - Equipment used (if teleop: what device)
  - Format and public availability

### 5.3: Theoretical Analysis (for theory-heavy fields)
- Add `## Theoretical Guarantees` to each paper:
  - What is proven (convergence, stability, safety, optimality)
  - Under what assumptions
  - Tightness of bounds
  - Gap between theory and practice

### 5.4: Computational Complexity (for algorithms)
- Add `## Complexity` to each paper:
  - Time/space complexity
  - Scaling behavior with problem dimension
  - Practical runtime on benchmark problems

---

## Phase 6: Final Structure & Cleanup

### 6.1: File Organization
```
project_root/
  survey.md                    # Main tables + cross-cutting analysis
  detailed_survey/
    section1/
      _overview.md             # Section summary + observations
      paper_name.md            # One per paper
      ...
    section2/
      ...
    ...
  Prompt_review.md             # This file
```

### 6.2: Final Checks

**Content quality:**
- [ ] All papers have quantitative results (or explicit "not reported" flag)
- [ ] All papers address every consistency dimension
- [ ] No unqualified "First" / "state-of-the-art" / "groundbreaking" claims
- [ ] All (sim)/(real)/(theoretical) labels on results
- [ ] Cross-cutting observation counts match individual entries
- [ ] No hardware/platform contradictions within entries
- [ ] Missing paper search completed for all sections
- [ ] Overview files updated after all additions

**Table formatting:**
- [ ] Column order consistent within each section table
- [ ] Venue column contains venue name only (no year)
- [ ] Year column contains integer only
- [ ] Paper column uses DOI hyperlink (preferred) or arXiv link (fallback)

**Link integrity (re-verify after EVERY edit pass):**
- [ ] All DOI links resolve correctly (HTTP 200 or 302 redirect)
- [ ] All arXiv IDs resolve to the correct paper (not just HTTP 200 — verify title match)
- [ ] All GitHub/project page links accessible
- [ ] 0 broken links total

**Language:**
- [ ] Output language matches user preference from Q7
- [ ] Paper titles and technical terms remain in English regardless of output language

---

## Parallelism Strategy

The following operations are independent and should run in parallel:

**Within each phase:**
- Phase 1: One agent per section for paper discovery + detailed file creation
- Phase 2: Split link verification by type (GitHub / arXiv / other)
- Phase 3: One review agent per 2-3 sections
- Phase 4: One missing-paper agent per section group
- Phase 5: Split enrichment by type (inference vs dataset) AND by section

**Across phases:**
- Phases 1-2 must complete before Phase 3
- Phase 3 must complete before Phase 4 (gaps inform missing paper search)
- Phase 5 can run in parallel with Phase 4

**Agent sizing:**
- Keep each agent to ~20-40 papers max for quality
- Large sections (40+ papers) should be split across 2 agents
- Review agents should read ALL files in their scope (no skipping)

---

## Anti-Patterns to Avoid

1. **Don't accept paper claims at face value.** Every "First X" and "SOTA" claim must be verified or attributed.
2. **Don't let WebFetch failures become permanent placeholders.** If arXiv is blocked, retry. If still blocked, use training knowledge but flag as unverified.
3. **Don't apply limitations unevenly.** If Paper A is criticized for lacking sim2real, Paper B with the same limitation must also be criticized.
4. **Don't inflate contributions by restating the method.** Contributions = what is new. Method = how it works. These are different.
5. **Don't use vague results.** "Improved performance" is not a result. "15% higher success rate on 100 objects (sim)" is a result.
6. **Don't confuse uniqueness-within-the-survey with paper contribution.** "Only paper in this section that does X" is a survey observation, not a paper contribution.
7. **Don't propagate stale arXiv IDs.** Verify every arXiv ID resolves to the correct paper.
8. **Don't mix up hardware.** If the deployment section contradicts the header, resolve it from the source paper.
9. **Don't skip the final verification pass.** Fixes can introduce new inconsistencies.
10. **Don't treat all papers equally in depth.** Foundational papers deserve more context; incremental papers should be honestly positioned as incremental.
