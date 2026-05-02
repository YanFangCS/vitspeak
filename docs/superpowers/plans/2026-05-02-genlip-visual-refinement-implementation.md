# GenLIP Visual Refinement Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Refine the GenLIP academic homepage into the approved "A + small C" editorial-academic design while preserving the central "GenLIP as MLLM vision encoder" story.

**Architecture:** Keep the static single-page homepage and existing asset structure. Add small semantic HTML hooks for pipeline takeaways and figure-first research stories, then layer the visual refinement through CSS without new runtime dependencies, external fonts, or page-order changes.

**Tech Stack:** Static HTML, CSS, existing Bulma/Font Awesome assets, existing local images/PDFs, Bash smoke checks, in-app browser QA.

---

## Repository Guardrails

- Worktree: `/Users/yanfang/workspace/vitspeak/.worktrees/genlip-homepage`
- Branch: `codex/genlip-homepage`
- Preserve the current user-authored author superscript edits in `index.html`. Do not rewrite the author block except if a task explicitly requires a surrounding structural edit.
- Do not stage or commit `GenLIP_Tech/`, `paper_version2.pdf`, or `.superpowers/`.
- Do not add external font requests, animation libraries, JavaScript frameworks, or new package dependencies.
- Keep the homepage order: hero, metrics, abstract, method, results, probes, demo, release, citation.
- Use `apply_patch` for manual edits.

## Files And Responsibilities

- `index.html`: Semantic content, hero pipeline copy, figure-first wrappers, concise research takeaways, release/demo/citation markup.
- `static/css/index.css`: Visual system, editorial typography, spacing, pipeline styling, evidence band, figure-first story modules, responsive behavior.
- `scripts/check-homepage.sh`: Smoke assertions for required homepage assets and key claims. Update only for new required text introduced by this refinement.

## Preflight

- [ ] **Step 1: Confirm worktree state**

Run:

```bash
git status --short --branch
```

Expected:

```text
## codex/genlip-homepage
 M index.html
?? GenLIP_Tech/
?? paper_version2.pdf
```

If additional tracked files are dirty, inspect them before editing. Preserve user changes unless the controller explicitly asks to replace them.

- [ ] **Step 2: Confirm the approved spec exists**

Run:

```bash
test -s docs/superpowers/specs/2026-05-02-genlip-visual-refinement-design.md && echo "visual spec present"
```

Expected:

```text
visual spec present
```

- [ ] **Step 3: Inspect the existing author hunk**

Run:

```bash
git diff -- index.html | sed -n '1,120p'
```

Expected: if the author hunk appears, it contains superscript affiliation markers such as `Yan Fang<sup>1,2,*</sup>`. Keep those lines as the current page state.

---

### Task 1: Add Editorial Story Hooks In HTML

**Files:**
- Modify: `/Users/yanfang/workspace/vitspeak/.worktrees/genlip-homepage/index.html`

Purpose: Add small semantic hooks needed by the approved editorial treatment. The content must continue to say that GenLIP is trained generatively but released/evaluated as a vision encoder.

- [ ] **Step 1: Add the pipeline takeaway below the existing pipeline**

In `index.html`, insert this block immediately after the closing `</div>` for `.hero-pipeline` and before `.evidence-chips`:

```html
          <p class="pipeline-takeaway">Released as an MLLM vision encoder: the language head teaches visual alignment during pretraining, then gets discarded at deployment.</p>
```

The surrounding section should become:

```html
          <div class="hero-pipeline" aria-labelledby="pipeline-title">
            <div class="pipeline-label pipeline-label-left">Pretrain by speaking</div>
            <div class="pipeline-label pipeline-label-right">Deploy as vision encoder</div>
            <div class="pipeline-stage token-stage">
              <div class="token-row" aria-hidden="true">
                <span class="token visual-token"></span>
                <span class="token visual-token"></span>
                <span class="token visual-token"></span>
                <span class="token-plus">+</span>
                <span class="token text-token"></span>
                <span class="token text-token"></span>
              </div>
              <p>Image patches and text tokens share one sequence.</p>
            </div>
            <div class="pipeline-arrow" aria-hidden="true">&rarr;</div>
            <div class="pipeline-stage transformer-stage">
              <strong>Single GenLIP Transformer</strong>
              <span>Prefix-LM objective - MRoPE - gated attention</span>
            </div>
            <div class="pipeline-arrow" aria-hidden="true">&rarr;</div>
            <div class="pipeline-stage deploy-stage">
              <div class="deploy-flow">
                <span>Visual embeddings</span>
                <span>Projector</span>
                <span>MLLM</span>
              </div>
              <p>Tokenizer and LM head are discarded at deployment.</p>
            </div>
          </div>

          <p class="pipeline-takeaway">Released as an MLLM vision encoder: the language head teaches visual alignment during pretraining, then gets discarded at deployment.</p>
```

- [ ] **Step 2: Replace result figure grid with figure-first story modules**

Replace the existing `<div class="result-figure-grid">...</div>` block with:

```html
        <div class="figure-story-grid">
          <article class="figure-story">
            <figure class="figure-panel story-figure">
              <img src="static/images/genlip-data-scale.png" alt="Data scaling curves for OCR, VQA, and Caption tasks from 1B to 8B pretraining samples.">
              <figcaption>Data scaling shows sustained gains, with gated attention improving stability across scales.</figcaption>
            </figure>
            <div class="research-takeaway">
              <p><strong>Scaling signal.</strong> As pretraining grows from 1B to 8B samples, GenLIP keeps improving OCR, VQA, and caption probes, supporting the vision encoder scaling story rather than a one-off benchmark gain.</p>
            </div>
          </article>
          <article class="figure-story reverse-story">
            <figure class="figure-panel story-figure">
              <img src="static/images/genlip-stage2-validation.png" alt="Stage 1 versus Stage 2 validation curves across evaluation resolutions.">
              <figcaption>Native-aspect adaptation improves OCR, VQA, and caption performance at higher evaluation resolutions.</figcaption>
            </figure>
            <div class="research-takeaway">
              <p><strong>Resolution signal.</strong> Continued pretraining with native aspect ratios strengthens detail-sensitive recognition, which is where an MLLM vision encoder most needs reliable spatial evidence.</p>
            </div>
          </article>
        </div>
```

- [ ] **Step 3: Replace probe figure grid with interpretability story modules**

Replace the existing `<div class="probe-grid">...</div>` block with:

```html
        <div class="figure-story-grid probe-story-grid">
          <article class="figure-story">
            <figure class="figure-panel story-figure">
              <img src="static/images/genlip-caption-examples.png" alt="GenLIP caption generation examples comparing model scales and pretraining stages.">
              <figcaption>Direct caption generation shows that the pretrained ViT can produce grounded descriptions from visual tokens.</figcaption>
            </figure>
            <div class="research-takeaway">
              <p><strong>Generation probe.</strong> Captioning is used here as an inspection tool for visual-language alignment, while deployment still uses GenLIP as the MLLM vision encoder.</p>
            </div>
          </article>
          <article class="figure-story reverse-story">
            <figure class="figure-panel story-figure">
              <img src="static/images/genlip-patch-semantics.png" alt="Patch semantic readout showing local visual regions mapped to language tokens.">
              <figcaption>Patch semantics reveal local visual embeddings aligned with language concepts.</figcaption>
            </figure>
            <div class="research-takeaway">
              <p><strong>Patch semantics.</strong> Local readouts make the learned representation more legible by showing which visual regions align with recognizable language concepts.</p>
            </div>
          </article>
        </div>
```

- [ ] **Step 4: Add a takeaway beside the OCR probe wide figure**

Replace the current standalone OCR `<figure class="figure-panel wide-figure">...</figure>` with:

```html
        <article class="figure-story wide-story">
          <figure class="figure-panel wide-figure story-figure">
            <img src="static/images/genlip-ocr-examples.png" alt="OCR-heavy GenLIP generation probes on receipt, geometry, and tiny text examples.">
            <figcaption>OCR-heavy probes explain the strong Doc/OCR benchmark behavior and expose remaining failure modes.</figcaption>
          </figure>
          <div class="research-takeaway">
            <p><strong>Doc/OCR behavior.</strong> The qualitative probes connect the benchmark gains to visible text-centric evidence, while keeping failure modes inspectable instead of hiding them behind aggregate scores.</p>
          </div>
        </article>
```

- [ ] **Step 5: Verify new HTML hooks exist**

Run:

```bash
rg -n "pipeline-takeaway|figure-story|research-takeaway|Scaling signal|Resolution signal|Generation probe|Patch semantics|Doc/OCR behavior" index.html
```

Expected: matches for all eight patterns.

- [ ] **Step 6: Run HTML smoke and whitespace checks**

Run:

```bash
./scripts/check-homepage.sh
git diff --check -- index.html
```

Expected:

```text
Homepage smoke checks passed
```

`git diff --check` exits with code 0 and prints no whitespace errors.

- [ ] **Step 7: Commit HTML story hooks**

Run:

```bash
git add index.html
git commit -m "feat: add GenLIP editorial story hooks"
```

Expected: commit succeeds. Do not add `GenLIP_Tech/`, `paper_version2.pdf`, or `.superpowers/`.

---

### Task 2: Refine Editorial Typography, Hero, And Section Rhythm

**Files:**
- Modify: `/Users/yanfang/workspace/vitspeak/.worktrees/genlip-homepage/static/css/index.css`

Purpose: Shift the page from an engineering-card look to a polished academic paper page: serif display typography, wider rhythm, restrained dividers, and calmer surfaces.

- [ ] **Step 1: Extend design variables**

Replace the current `:root` block with:

```css
:root {
  --page: #ffffff;
  --paper: #fbfaf7;
  --paper-soft: #f5f9fb;
  --panel: #ffffff;
  --panel-tint: #f8fbfc;
  --ink: #0b2328;
  --ink-soft: #39575f;
  --muted: #6d838a;
  --line: #d9e6e9;
  --line-strong: #7ba2a9;
  --rule-blue: #4b82e6;
  --stroke: #123d46;
  --visual: #58d7dc;
  --visual-dark: #16aab3;
  --text-token: #fff0cf;
  --text-token-dark: #c69131;
  --chip: #e9f8f8;
  --focus: #008f99;
  --shadow: 0 12px 28px rgb(18 61 70 / 0.08);
  --shadow-soft: 0 6px 18px rgb(18 61 70 / 0.055);
  --radius: 8px;
  --radius-sm: 6px;
  --max-width: 1120px;
  --display-serif: Georgia, "Times New Roman", serif;
  --body-sans: Inter, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
}
```

- [ ] **Step 2: Point base typography at variables**

Replace the `font-family` declarations in `body` and the form-control group with:

```css
body {
  margin: 0;
  color: var(--ink);
  background: var(--page);
  font-family: var(--body-sans);
  font-size: 16px;
  line-height: 1.65;
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

body,
button,
input,
select,
textarea {
  font-family: var(--body-sans);
}
```

- [ ] **Step 3: Increase editorial section rhythm**

Replace `.section` with:

```css
.section {
  padding: 5.6rem 1.5rem;
}
```

- [ ] **Step 4: Refine the hero surface and display title**

Replace `.publication-hero`, `.publication-hero .hero-body`, `.publication-kicker`, `.publication-title`, `.publication-subtitle`, `.publication-authors`, and `.publication-links` with:

```css
.publication-hero {
  color: var(--ink);
  background:
    linear-gradient(180deg, rgb(246 253 253 / 0.84) 0%, var(--paper) 48%, #ffffff 100%);
  border-bottom: 1px solid var(--line);
}

.publication-hero .hero-body {
  padding: 6.25rem 1.5rem 3.8rem;
}

.publication-hero .container {
  text-align: center;
}

.publication-kicker {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 1.95rem;
  margin-bottom: 1.25rem;
  padding: 0.28rem 0.7rem;
  color: var(--stroke);
  background: rgb(255 255 255 / 0.62);
  border: 1px solid rgb(22 170 179 / 0.26);
  border-radius: var(--radius-sm);
  font-size: 0.78rem;
  font-weight: 800;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.publication-title {
  max-width: 900px;
  margin: 0 auto !important;
  color: var(--ink) !important;
  font-family: var(--display-serif);
  font-size: clamp(3.6rem, 8.5vw, 7.1rem);
  font-weight: 400;
  line-height: 0.96;
  letter-spacing: 0;
}

.publication-subtitle {
  max-width: 760px;
  margin: 1.35rem auto 0;
  color: var(--ink-soft);
  font-size: 1.22rem;
  line-height: 1.6;
}

.publication-authors {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 0.26rem 0.7rem;
  max-width: 930px;
  margin: 1.65rem auto 0;
  color: var(--ink);
  font-size: 0.98rem;
  font-weight: 650;
}

.publication-links {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 0.62rem;
  margin: 1.8rem auto 0;
}
```

- [ ] **Step 5: Make buttons slimmer and more editorial**

Replace `.project-button, .light-button, .copy-bibtex-btn`, `.project-button`, and `.project-button:hover` with:

```css
.project-button,
.light-button,
.copy-bibtex-btn {
  min-height: 2.55rem;
  border-radius: var(--radius-sm);
  font-weight: 800;
  transition:
    background-color 160ms ease,
    border-color 160ms ease,
    color 160ms ease,
    transform 160ms ease,
    box-shadow 160ms ease;
}

.project-button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.48rem;
  padding: 0.6rem 0.92rem;
  color: #ffffff;
  background: var(--stroke);
  border: 1px solid var(--stroke);
  box-shadow: 0 5px 14px rgb(18 61 70 / 0.12);
  text-decoration: none;
}

.project-button:hover {
  color: #ffffff;
  background: #0a2f37;
  border-color: #0a2f37;
  transform: translateY(-1px);
}
```

- [ ] **Step 6: Add serif section titles and editorial divider rules**

Replace `.section-heading`, `.section-heading p`, `.section-kicker`, and `.section-title` with:

```css
.section-heading {
  position: relative;
  max-width: 820px;
  margin: 0 auto 2.45rem;
  padding-bottom: 1.1rem;
  text-align: center;
}

.section-heading::after {
  position: absolute;
  bottom: 0;
  left: 50%;
  width: min(220px, 42vw);
  height: 1px;
  background: linear-gradient(90deg, transparent, var(--visual-dark), var(--rule-blue), transparent);
  content: "";
  transform: translateX(-50%);
}

.section-heading p {
  color: var(--ink-soft);
}

.section-kicker {
  margin: 0 0 0.55rem;
  color: var(--visual-dark) !important;
  font-size: 0.78rem;
  font-weight: 850;
  letter-spacing: 0.09em;
  text-transform: uppercase;
}

.section-title {
  margin: 0;
  color: var(--ink);
  font-family: var(--display-serif);
  font-size: clamp(2rem, 4vw, 3rem);
  font-weight: 400;
  line-height: 1.08;
  letter-spacing: 0;
}
```

- [ ] **Step 7: Soften repeated content cards**

Replace the grouped card rule and the card headings with:

```css
.metric-card,
.method-card,
.tldr-grid article,
.release-card {
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  box-shadow: none;
}

.tldr-grid h3,
.method-card h3,
.release-card h3 {
  margin: 0 0 0.55rem;
  color: var(--stroke);
  font-size: 1.02rem;
  font-weight: 850;
}
```

- [ ] **Step 8: Verify typography and rhythm hooks**

Run:

```bash
rg -n "display-serif|body-sans|section-heading::after|rule-blue|font-family: var\\(--display-serif\\)" static/css/index.css
```

Expected: matches for the variables, divider pseudo-element, and serif title usage.

- [ ] **Step 9: Run checks**

Run:

```bash
./scripts/check-homepage.sh
git diff --check -- static/css/index.css
```

Expected:

```text
Homepage smoke checks passed
```

`git diff --check` exits with code 0 and prints no whitespace errors.

- [ ] **Step 10: Commit editorial visual system**

Run:

```bash
git add static/css/index.css
git commit -m "style: refine GenLIP editorial visual system"
```

Expected: commit succeeds.

---

### Task 3: Polish Pipeline And Evidence Band

**Files:**
- Modify: `/Users/yanfang/workspace/vitspeak/.worktrees/genlip-homepage/static/css/index.css`

Purpose: Keep the pipeline as the first-viewport technical anchor, but make it read as one elegant wide diagram. Convert metrics into a concise evidence band rather than four equal card boxes.

- [ ] **Step 1: Replace the pipeline frame and stage styles**

Replace `.hero-pipeline`, `.pipeline-label`, `.pipeline-stage`, `.pipeline-stage p`, `.pipeline-arrow`, `.transformer-stage`, `.transformer-stage strong`, and `.transformer-stage span` with:

```css
.hero-pipeline {
  position: relative;
  display: grid;
  grid-template-columns: minmax(0, 1fr) auto minmax(220px, 0.9fr) auto minmax(0, 1fr);
  align-items: stretch;
  gap: 0.85rem;
  width: 100%;
  margin: 3.2rem auto 0;
  padding: 3.45rem 1.05rem 1.1rem;
  background: rgb(255 255 255 / 0.78);
  border: 1px solid rgb(18 61 70 / 0.18);
  border-radius: var(--radius);
  box-shadow: 0 18px 45px rgb(18 61 70 / 0.09);
}

.pipeline-label {
  position: absolute;
  top: 1rem;
  color: var(--stroke);
  font-size: 0.72rem;
  font-weight: 850;
  letter-spacing: 0.1em;
  text-transform: uppercase;
}

.pipeline-stage {
  display: flex;
  min-height: 148px;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 0.75rem;
  padding: 1.15rem;
  color: var(--ink);
  background: rgb(255 255 255 / 0.7);
  border: 1px solid rgb(18 61 70 / 0.13);
  border-radius: var(--radius-sm);
}

.pipeline-stage p {
  max-width: 260px;
  margin: 0;
  color: var(--ink-soft);
  font-size: 0.92rem;
  line-height: 1.45;
}

.pipeline-arrow {
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--stroke);
  font-size: 1.75rem;
  font-weight: 800;
}

.transformer-stage {
  background: #102f37;
  border-color: #102f37;
  color: #ffffff;
  box-shadow: inset 0 0 0 1px rgb(255 255 255 / 0.08);
}

.transformer-stage strong {
  color: #ffffff;
  font-size: 1.05rem;
  font-weight: 850;
}

.transformer-stage span {
  color: #c5e5e8;
  font-size: 0.92rem;
  line-height: 1.45;
}
```

- [ ] **Step 2: Add styling for the pipeline takeaway**

Insert this block after `.hero-pipeline` or after `.deploy-flow span`:

```css
.pipeline-takeaway {
  max-width: 780px;
  margin: 1rem auto 0;
  color: var(--ink-soft);
  font-size: 0.98rem;
  line-height: 1.55;
}

.pipeline-takeaway::before {
  display: inline-block;
  width: 2.4rem;
  height: 1px;
  margin-right: 0.65rem;
  background: var(--visual-dark);
  vertical-align: middle;
  content: "";
}
```

- [ ] **Step 3: Replace metrics section and metric cards with evidence band styling**

Replace `.metrics-section`, `.metric-grid`, `.metric-card`, `.metric-card strong`, and `.metric-card span` with:

```css
.metrics-section {
  padding-top: 2.25rem;
  padding-bottom: 3.2rem;
  background: var(--page);
}

.metric-grid {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 0;
  overflow: hidden;
  background: var(--paper);
  border-top: 1px solid var(--line);
  border-bottom: 1px solid var(--line);
}

.metric-card {
  padding: 1.35rem 1.25rem;
  background: transparent;
  border: 0;
  border-right: 1px solid var(--line);
  border-radius: 0;
  box-shadow: none;
}

.metric-card:last-child {
  border-right: 0;
}

.metric-card strong {
  display: block;
  color: var(--stroke);
  font-family: var(--display-serif);
  font-size: 2.35rem;
  font-weight: 400;
  line-height: 1;
}

.metric-card span {
  display: block;
  margin-top: 0.65rem;
  color: var(--ink-soft);
  font-size: 0.92rem;
  line-height: 1.45;
}
```

- [ ] **Step 4: Update responsive pipeline and metrics rules**

In the `@media (max-width: 900px)` block, replace the `.metric-grid, ...` selector list with:

```css
  .metric-grid,
  .tldr-grid,
  .method-grid,
  .release-grid,
  .figure-story-grid,
  .probe-story-grid {
    grid-template-columns: 1fr;
  }
```

Still inside `@media (max-width: 900px)`, add:

```css
  .metric-card {
    border-right: 0;
    border-bottom: 1px solid var(--line);
  }

  .metric-card:last-child {
    border-bottom: 0;
  }
```

In the `@media (max-width: 560px)` block, keep `.metric-grid { grid-template-columns: 1fr; }` and add:

```css
  .pipeline-takeaway {
    text-align: left;
  }

  .pipeline-takeaway::before {
    display: none;
  }
```

- [ ] **Step 5: Verify pipeline and metrics selectors**

Run:

```bash
rg -n "pipeline-takeaway|box-shadow: 0 18px 45px|metric-grid|metric-card:last-child|font-family: var\\(--display-serif\\)" static/css/index.css
```

Expected: matches for the pipeline takeaway, wide-frame shadow, evidence band rules, and serif metric values.

- [ ] **Step 6: Run checks**

Run:

```bash
./scripts/check-homepage.sh
git diff --check -- static/css/index.css
```

Expected:

```text
Homepage smoke checks passed
```

- [ ] **Step 7: Commit pipeline and evidence band**

Run:

```bash
git add static/css/index.css
git commit -m "style: polish GenLIP pipeline evidence band"
```

Expected: commit succeeds.

---

### Task 4: Style Figure-First Stories And Quieter Release Areas

**Files:**
- Modify: `/Users/yanfang/workspace/vitspeak/.worktrees/genlip-homepage/static/css/index.css`

Purpose: Apply the "small C" figure-first treatment only where it improves the research narrative: results and representation probes. Keep release/demo practical and quieter.

- [ ] **Step 1: Replace figure panel base styling**

Replace `.figure-panel, .table-panel, .demo-panel`, `.figure-panel`, `.figure-panel img`, and `.figure-panel figcaption` with:

```css
.figure-panel,
.table-panel,
.demo-panel {
  overflow: hidden;
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  box-shadow: var(--shadow-soft);
}

.figure-panel {
  margin: 2rem 0 0;
}

.figure-panel img {
  width: 100%;
  background: var(--panel-tint);
}

.figure-panel figcaption {
  margin: 0;
  padding: 0.85rem 1rem 1rem;
  color: var(--muted);
  border-top: 1px solid var(--line);
  font-size: 0.9rem;
  line-height: 1.45;
}
```

This keeps existing figure behavior stable before adding story modules.

- [ ] **Step 2: Replace old figure grids with story-grid selectors**

Replace the `.result-figure-grid, .probe-grid` block with:

```css
.figure-story-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 1.25rem;
  margin-top: 2rem;
}

.probe-story-grid {
  margin-top: 0;
}

.figure-story {
  display: grid;
  grid-template-rows: auto 1fr;
  gap: 1rem;
  min-width: 0;
}

.figure-story .figure-panel {
  margin: 0;
}

.story-figure {
  align-self: start;
}

.research-takeaway {
  padding: 0.25rem 0 0.25rem 1rem;
  border-left: 2px solid var(--visual-dark);
}

.research-takeaway p {
  margin: 0;
  color: var(--ink-soft);
  font-size: 0.98rem;
  line-height: 1.65;
}

.research-takeaway strong {
  color: var(--stroke);
  font-weight: 850;
}

.wide-story {
  max-width: 960px;
  margin: 2rem auto 0;
}
```

- [ ] **Step 3: Refine the wide figure behavior**

Replace `.wide-figure` with:

```css
.wide-figure {
  max-width: 960px;
  margin-right: auto;
  margin-left: auto;
}
```

- [ ] **Step 4: Make table/result surfaces feel more editorial**

Replace `.table-panel`, `.table-header`, `.table-header h3`, `thead th`, `.highlight-row th, .highlight-row td`, and `.highlight-row th:first-child` with:

```css
.table-panel {
  margin-top: 2rem;
  box-shadow: 0 10px 26px rgb(18 61 70 / 0.055);
}

.table-header {
  padding: 1rem 1.1rem;
  background: var(--paper);
  border-bottom: 1px solid var(--line);
}

.table-header h3 {
  margin: 0;
  color: var(--stroke);
  font-size: 1rem;
  font-weight: 850;
}

thead th {
  color: var(--stroke);
  background: #eef8f8;
  font-size: 0.78rem;
  font-weight: 850;
  letter-spacing: 0.04em;
  text-transform: uppercase;
}

.highlight-row th,
.highlight-row td {
  background: #fff8e8;
}

.highlight-row th:first-child {
  box-shadow: inset 4px 0 0 var(--text-token-dark);
}
```

- [ ] **Step 5: Quiet release cards and quick links**

Replace `.release-section`, `.release-card a`, `.quick-links`, `.quick-links a`, and `.quick-links a:hover` with:

```css
.release-section {
  background: var(--page);
}

.release-card {
  box-shadow: none;
}

.release-card a {
  display: inline-flex;
  margin-top: 0.85rem;
  font-weight: 850;
}

.quick-links {
  display: flex;
  flex-wrap: wrap;
  gap: 0.65rem;
  margin-top: 1rem;
}

.quick-links a {
  text-decoration: none;
}

.quick-links a:hover {
  color: #ffffff;
  background: var(--stroke);
  border-color: var(--stroke);
}
```

- [ ] **Step 6: Update mobile section-heading behavior**

In `@media (max-width: 560px)`, replace:

```css
  .section-heading {
    text-align: left;
  }
```

with:

```css
  .section-heading {
    text-align: left;
  }

  .section-heading::after {
    left: 0;
    width: 8rem;
    transform: none;
  }
```

- [ ] **Step 7: Verify story selectors**

Run:

```bash
rg -n "figure-story-grid|probe-story-grid|research-takeaway|wide-story|section-heading::after" static/css/index.css
```

Expected: matches for all selectors.

- [ ] **Step 8: Run checks**

Run:

```bash
./scripts/check-homepage.sh
git diff --check -- static/css/index.css
```

Expected:

```text
Homepage smoke checks passed
```

- [ ] **Step 9: Commit figure-first refinement**

Run:

```bash
git add static/css/index.css
git commit -m "style: add GenLIP figure-first story treatment"
```

Expected: commit succeeds.

---

### Task 5: Update Smoke Coverage For New Required Claims

**Files:**
- Modify: `/Users/yanfang/workspace/vitspeak/.worktrees/genlip-homepage/scripts/check-homepage.sh`

Purpose: Ensure the key design/story additions are covered by automated smoke checks.

- [ ] **Step 1: Add required text assertions**

In `scripts/check-homepage.sh`, update `required_text` to include the new claims. The array should contain at least these entries:

```bash
required_text=(
  "Let ViT Speak"
  "GenLIP: Generative Language-Image Pre-training"
  "vision encoders in multimodal large language models"
  "Pretrain by speaking"
  "Deploy as vision encoder"
  "Released as an MLLM vision encoder"
  "No contrastive batches"
  "No extra text decoder"
  "73.6"
  "Doc/OCR"
  "Scaling signal"
  "Resolution signal"
  "Generation probe"
  "Patch semantics"
  "What does &quot;speak&quot; reveal?"
  "GenLIP-L/16"
  "GenLIP-So/16"
  "GenLIP-g/16"
)
```

- [ ] **Step 2: Run smoke check**

Run:

```bash
./scripts/check-homepage.sh
```

Expected:

```text
Homepage smoke checks passed
```

- [ ] **Step 3: Run script whitespace check**

Run:

```bash
git diff --check -- scripts/check-homepage.sh
```

Expected: exit code 0 and no output.

- [ ] **Step 4: Commit smoke update**

Run:

```bash
git add scripts/check-homepage.sh
git commit -m "test: cover GenLIP visual refinement claims"
```

Expected: commit succeeds.

---

### Task 6: Browser QA And Final Polish

**Files:**
- Modify if needed: `/Users/yanfang/workspace/vitspeak/.worktrees/genlip-homepage/index.html`
- Modify if needed: `/Users/yanfang/workspace/vitspeak/.worktrees/genlip-homepage/static/css/index.css`
- Modify if needed: `/Users/yanfang/workspace/vitspeak/.worktrees/genlip-homepage/scripts/check-homepage.sh`

Purpose: Verify the design in-browser at desktop and mobile widths, then make only targeted polish fixes.

- [ ] **Step 1: Start a local server from the worktree**

Run:

```bash
python3 -m http.server 8000
```

Expected: server prints a message like:

```text
Serving HTTP on :: port 8000
```

If port 8000 is already in use, run:

```bash
python3 -m http.server 8001
```

Expected:

```text
Serving HTTP on :: port 8001
```

Keep this process running during browser QA.

- [ ] **Step 2: Open the page in the in-app browser**

Use the Browser Use plugin to navigate to:

```text
http://localhost:8000/
```

If Task 6 Step 1 used port 8001, navigate to:

```text
http://localhost:8001/
```

Expected: the GenLIP homepage loads with no missing local assets.

- [ ] **Step 3: Desktop visual QA checklist**

At a desktop viewport, verify:

```text
1. First viewport shows the refined serif "Let ViT Speak" title, compact authors, visible buttons, and the full train/deploy pipeline.
2. Pipeline endpoint still reads as MLLM vision encoder, and the pipeline takeaway is visible below the diagram.
3. The page is not a dark clone of the reference site; it remains light and paper-like.
4. The four metrics read as one concise evidence band, not four unrelated heavy cards.
5. Results figure stories show a figure plus left-rule takeaway without overlap.
6. Probe figure stories keep generation framed as an interpretability probe, not the product claim.
7. Release links remain practical and visible.
8. No obvious clipped text, image distortion, broken icon, or horizontal page overflow.
```

- [ ] **Step 4: Mobile visual QA checklist**

Use a narrow mobile viewport and verify:

```text
1. Hero title wraps cleanly and does not collide with subtitle/authors/buttons.
2. Buttons wrap without clipped labels.
3. Pipeline stacks in order: Pretrain label, token stage, arrow, Transformer, arrow, Deploy label, deploy stage.
4. Pipeline takeaway is readable and does not create layout overflow.
5. Metrics stack with clean dividers.
6. Table scrolls inside the table wrapper only.
7. Figure stories stack as single-column modules.
8. BibTeX remains horizontally scrollable without page overflow.
```

- [ ] **Step 5: Inspect server output for missing assets**

Check the terminal running the server.

Expected: no `404` lines for:

```text
static/css/index.css
static/js/index.js
static/pdfs/paper.pdf
static/images/genlip-method-architecture.png
static/images/genlip-data-scale.png
static/images/genlip-stage2-validation.png
static/images/genlip-caption-examples.png
static/images/genlip-ocr-examples.png
static/images/genlip-patch-semantics.png
static/webfonts/fa-solid-900.woff2
static/webfonts/fa-brands-400.woff2
```

- [ ] **Step 6: Run final automated checks**

Run:

```bash
./scripts/check-homepage.sh
git diff --check -- index.html static/css/index.css scripts/check-homepage.sh
rg -n "Lorem ipsum|PAPER_TITLE|YOUR_DOMAIN|FIRST_AUTHOR_NAME|Academic Project Page|Another Carousel|Video Presentation|Poster|More Works|JkaxUblCGz0" index.html
```

Expected:

```text
Homepage smoke checks passed
```

`git diff --check` exits with code 0. The `rg` command exits with code 1 because no residue matches are found.

- [ ] **Step 7: Make targeted QA fixes only if needed**

If browser QA finds clipping or overlap, edit only the selector responsible for the defect. Use these allowed fixes:

For a too-large mobile title, adjust only this rule:

```css
  .publication-title {
    font-size: clamp(2.45rem, 13vw, 3.8rem);
  }
```

For cramped mobile story modules, add this inside `@media (max-width: 560px)`:

```css
  .figure-story-grid {
    gap: 1.4rem;
  }

  .research-takeaway {
    padding-left: 0.85rem;
  }
```

For an overflowing pipeline stage, add this inside `@media (max-width: 560px)`:

```css
  .pipeline-stage {
    padding: 1rem 0.85rem;
  }
```

For a clipped release/demo button, keep the existing full-width mobile button rule and add:

```css
  .project-button {
    white-space: normal;
  }
```

- [ ] **Step 8: Re-run checks after any QA fix**

Run:

```bash
./scripts/check-homepage.sh
git diff --check -- index.html static/css/index.css scripts/check-homepage.sh
```

Expected:

```text
Homepage smoke checks passed
```

- [ ] **Step 9: Commit QA fixes if any files changed**

If Task 6 required code changes, run:

```bash
git add index.html static/css/index.css scripts/check-homepage.sh
git commit -m "fix: polish GenLIP visual refinement QA"
```

Expected: commit succeeds.

If Task 6 required no code changes, do not create an empty commit.

- [ ] **Step 10: Final status check**

Run:

```bash
git status --short --branch
```

Expected: only intentionally untracked source inputs remain:

```text
## codex/genlip-homepage
?? GenLIP_Tech/
?? paper_version2.pdf
```

If `.superpowers/` appears, do not stage it.

## Final Acceptance Checklist

- [ ] First viewport is refined, academic, and still centered on "Let ViT Speak".
- [ ] The pipeline still communicates visual/text tokens -> single GenLIP Transformer -> MLLM vision encoder.
- [ ] The new pipeline takeaway explicitly says GenLIP is released as an MLLM vision encoder.
- [ ] Metrics read as a single evidence band.
- [ ] Results and probes use figure-first story modules with restrained left-rule takeaways.
- [ ] Generation probes are framed as interpretability evidence, not the released product.
- [ ] No new dependencies or external font requests were added.
- [ ] `./scripts/check-homepage.sh` passes.
- [ ] Browser QA shows no clipped text, overlap, missing assets, or page-level horizontal overflow.
