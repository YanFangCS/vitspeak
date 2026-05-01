# GenLIP Homepage Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the generic academic template with a polished GenLIP project homepage that presents "pretrain by speaking, deploy as a vision encoder" as the central story.

**Architecture:** Keep the current static GitHub Pages structure. Build the homepage in `index.html`, project-specific styling in `static/css/index.css`, minimal progressive behavior in `static/js/index.js`, and generated/copy assets under `static/images/` and `static/pdfs/`.

**Tech Stack:** Static HTML, Bulma utility classes already vendored in `static/css/bulma.min.css`, local Font Awesome, custom CSS, small vanilla JavaScript, Ghostscript for PDF figure rasterization, optional local Python HTTP server for verification.

---

## File Structure

- Modify `index.html`: Replace template content with the GenLIP homepage sections, metadata, structured data, release links, and citation.
- Modify `static/css/index.css`: Replace template styling with the restrained Token Lab visual system, responsive layout rules, tables, hero pipeline, figures, release cards, and accessibility states.
- Modify `static/js/index.js`: Keep only scroll-to-top and BibTeX copy behavior; remove carousel/dropdown/video logic.
- Create `scripts/check-homepage.sh`: A deterministic smoke check for required assets, required copy, and removed template residue.
- Create `static/pdfs/paper.pdf`: Copy of `paper_version2.pdf` for the Paper button and citation metadata.
- Create `static/images/genlip-method-architecture.png`: Copy of `GenLIP_Tech/figures/fig2-arch_2.png`.
- Create `static/images/genlip-data-scale.png`: Copy of `GenLIP_Tech/figures/data-scale.png`.
- Create `static/images/genlip-stage2-validation.png`: Copy of `GenLIP_Tech/figures/stage2-validation.png`.
- Create `static/images/genlip-attention-sink.png`: Copy of `GenLIP_Tech/figures/attention-sink-ga-long.png`.
- Create `static/images/genlip-caption-examples.png`: Rasterized first page of `GenLIP_Tech/figures/caption-1-ver3.pdf`.
- Create `static/images/genlip-ocr-examples.png`: Rasterized first page of `GenLIP_Tech/figures/caption-3items.pdf`.
- Create `static/images/genlip-patch-semantics.png`: Rasterized first page of `GenLIP_Tech/figures/patchsemantics-1-ver2.pdf`.
- Create `static/images/social_preview.svg`: SVG social preview using the hero title and train/deploy pipeline motif.

Current release-link policy:

- Paper button: `static/pdfs/paper.pdf`
- arXiv button: `static/pdfs/paper.pdf` until an arXiv identifier is assigned
- Code button: `#release-code`
- Model button: `#release-models`
- Demo button: `#demo`

This keeps every primary button functional now and leaves a small, obvious edit surface when public external URLs are assigned.

---

### Task 1: Assets And Smoke Check

**Files:**
- Create: `scripts/check-homepage.sh`
- Create: `static/pdfs/paper.pdf`
- Create: `static/images/genlip-method-architecture.png`
- Create: `static/images/genlip-data-scale.png`
- Create: `static/images/genlip-stage2-validation.png`
- Create: `static/images/genlip-attention-sink.png`
- Create: `static/images/genlip-caption-examples.png`
- Create: `static/images/genlip-ocr-examples.png`
- Create: `static/images/genlip-patch-semantics.png`
- Create: `static/images/social_preview.svg`

- [ ] **Step 1: Create the smoke check script**

Create `scripts/check-homepage.sh`:

```bash
#!/usr/bin/env bash
set -euo pipefail

required_files=(
  "index.html"
  "static/css/index.css"
  "static/js/index.js"
  "static/pdfs/paper.pdf"
  "static/images/genlip-method-architecture.png"
  "static/images/genlip-data-scale.png"
  "static/images/genlip-stage2-validation.png"
  "static/images/genlip-attention-sink.png"
  "static/images/genlip-caption-examples.png"
  "static/images/genlip-ocr-examples.png"
  "static/images/genlip-patch-semantics.png"
  "static/images/social_preview.svg"
)

for file in "${required_files[@]}"; do
  if [[ ! -s "$file" ]]; then
    echo "Missing or empty required file: $file"
    exit 1
  fi
done

required_text=(
  "Let ViT Speak"
  "GenLIP: Generative Language-Image Pre-training"
  "vision encoders in multimodal large language models"
  "Pretrain by speaking"
  "Deploy as vision encoder"
  "No contrastive batches"
  "No extra text decoder"
  "73.6"
  "Doc/OCR"
  "What does &quot;speak&quot; reveal?"
  "GenLIP-L/16"
  "GenLIP-So/16"
  "GenLIP-g/16"
)

for text in "${required_text[@]}"; do
  if ! grep -Fq "$text" index.html; then
    echo "Missing required homepage text: $text"
    exit 1
  fi
done

banned_text=(
  "Lorem ipsum"
  "PAPER_TITLE"
  "YOUR_DOMAIN"
  "FIRST_AUTHOR_NAME"
  "Academic Project Page"
  "First image description"
  "Another Carousel"
  "Video Presentation"
  "Poster"
  "More Works"
  "JkaxUblCGz0"
)

for text in "${banned_text[@]}"; do
  if grep -Fq "$text" index.html; then
    echo "Found template residue in index.html: $text"
    exit 1
  fi
done

echo "Homepage smoke checks passed"
```

- [ ] **Step 2: Make the smoke check executable**

Run:

```bash
chmod +x scripts/check-homepage.sh
```

Expected: command exits with code 0 and prints nothing.

- [ ] **Step 3: Generate and copy image/PDF assets**

Run:

```bash
mkdir -p static/images static/pdfs scripts
cp paper_version2.pdf static/pdfs/paper.pdf
cp GenLIP_Tech/figures/fig2-arch_2.png static/images/genlip-method-architecture.png
cp GenLIP_Tech/figures/data-scale.png static/images/genlip-data-scale.png
cp GenLIP_Tech/figures/stage2-validation.png static/images/genlip-stage2-validation.png
cp GenLIP_Tech/figures/attention-sink-ga-long.png static/images/genlip-attention-sink.png
gs -dSAFER -dBATCH -dNOPAUSE -sDEVICE=pngalpha -r180 -dFirstPage=1 -dLastPage=1 -o static/images/genlip-caption-examples.png GenLIP_Tech/figures/caption-1-ver3.pdf
gs -dSAFER -dBATCH -dNOPAUSE -sDEVICE=pngalpha -r180 -dFirstPage=1 -dLastPage=1 -o static/images/genlip-ocr-examples.png GenLIP_Tech/figures/caption-3items.pdf
gs -dSAFER -dBATCH -dNOPAUSE -sDEVICE=pngalpha -r180 -dFirstPage=1 -dLastPage=1 -o static/images/genlip-patch-semantics.png GenLIP_Tech/figures/patchsemantics-1-ver2.pdf
```

Expected: Ghostscript prints `Processing pages 1 through 1.` for each PDF conversion and exits successfully.

- [ ] **Step 4: Create the SVG social preview**

Create `static/images/social_preview.svg`:

```svg
<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630" role="img" aria-labelledby="title desc">
  <title id="title">Let ViT Speak: GenLIP</title>
  <desc id="desc">Social preview for GenLIP, showing visual tokens and text tokens flowing into a vision encoder for MLLMs.</desc>
  <rect width="1200" height="630" fill="#f6fafb"/>
  <rect x="58" y="58" width="1084" height="514" rx="36" fill="#ffffff" stroke="#d7e5e8" stroke-width="3"/>
  <text x="600" y="150" text-anchor="middle" font-family="Inter, Arial, sans-serif" font-size="76" font-weight="800" fill="#071b22">Let ViT Speak</text>
  <text x="600" y="208" text-anchor="middle" font-family="Inter, Arial, sans-serif" font-size="32" font-weight="600" fill="#375867">Generative Language-Image Pre-training</text>
  <text x="600" y="258" text-anchor="middle" font-family="Inter, Arial, sans-serif" font-size="25" fill="#58707a">Pretrain by speaking. Deploy as a vision encoder for MLLMs.</text>
  <g transform="translate(214 330)">
    <rect x="0" y="0" width="62" height="62" rx="12" fill="#b9e3e5" stroke="#07303a" stroke-width="5"/>
    <rect x="78" y="0" width="62" height="62" rx="12" fill="#b9e3e5" stroke="#07303a" stroke-width="5"/>
    <rect x="156" y="0" width="62" height="62" rx="12" fill="#b9e3e5" stroke="#07303a" stroke-width="5"/>
    <text x="260" y="43" font-family="Inter, Arial, sans-serif" font-size="42" font-weight="800" fill="#07303a">+</text>
    <rect x="310" y="0" width="62" height="62" rx="12" fill="#f6eddb" stroke="#07303a" stroke-width="5"/>
    <rect x="388" y="0" width="62" height="62" rx="12" fill="#f6eddb" stroke="#07303a" stroke-width="5"/>
    <path d="M482 31 H572" stroke="#07303a" stroke-width="8" stroke-linecap="round"/>
    <path d="M572 31 l-22 -18 M572 31 l-22 18" stroke="#07303a" stroke-width="8" stroke-linecap="round"/>
    <rect x="604" y="-16" width="230" height="94" rx="22" fill="#eaf3f4" stroke="#07303a" stroke-width="5"/>
    <text x="719" y="40" text-anchor="middle" font-family="Inter, Arial, sans-serif" font-size="32" font-weight="800" fill="#071b22">GenLIP ViT</text>
  </g>
  <text x="600" y="506" text-anchor="middle" font-family="Inter, Arial, sans-serif" font-size="24" font-weight="700" fill="#375867">Single Transformer - No contrastive batches - No extra text decoder</text>
</svg>
```

- [ ] **Step 5: Run smoke check and confirm initial expected failure**

Run:

```bash
./scripts/check-homepage.sh
```

Expected: FAIL with `Missing required homepage text: Let ViT Speak` because `index.html` still contains the template.

- [ ] **Step 6: Commit assets and smoke test**

Run:

```bash
git add scripts/check-homepage.sh static/pdfs/paper.pdf static/images/genlip-method-architecture.png static/images/genlip-data-scale.png static/images/genlip-stage2-validation.png static/images/genlip-attention-sink.png static/images/genlip-caption-examples.png static/images/genlip-ocr-examples.png static/images/genlip-patch-semantics.png static/images/social_preview.svg
git commit -m "chore: add GenLIP homepage assets"
```

Expected: commit succeeds and includes only the listed files.

---

### Task 2: Minimal JavaScript Behavior

**Files:**
- Modify: `static/js/index.js`
- Test: `scripts/check-homepage.sh`

- [ ] **Step 1: Replace `static/js/index.js` with focused behavior**

Replace the whole file with:

```javascript
function copyBibTeX() {
  const bibtexElement = document.getElementById('bibtex-code');
  const button = document.querySelector('.copy-bibtex-btn');
  const label = button ? button.querySelector('.copy-text') : null;

  if (!bibtexElement || !button || !label) {
    return;
  }

  const text = bibtexElement.textContent;
  const markCopied = () => {
    button.classList.add('copied');
    label.textContent = 'Copied';
    window.setTimeout(() => {
      button.classList.remove('copied');
      label.textContent = 'Copy';
    }, 1800);
  };

  if (navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard.writeText(text).then(markCopied).catch(() => fallbackCopy(text, markCopied));
    return;
  }

  fallbackCopy(text, markCopied);
}

function fallbackCopy(text, onCopied) {
  const textArea = document.createElement('textarea');
  textArea.value = text;
  textArea.setAttribute('readonly', '');
  textArea.style.position = 'absolute';
  textArea.style.left = '-9999px';
  document.body.appendChild(textArea);
  textArea.select();
  document.execCommand('copy');
  document.body.removeChild(textArea);
  onCopied();
}

function scrollToTop() {
  window.scrollTo({
    top: 0,
    behavior: 'smooth'
  });
}

window.addEventListener('scroll', () => {
  const scrollButton = document.querySelector('.scroll-to-top');
  if (!scrollButton) {
    return;
  }
  scrollButton.classList.toggle('visible', window.scrollY > 360);
});
```

- [ ] **Step 2: Verify removed template-only JS hooks**

Run:

```bash
rg -n "toggleMoreWorks|bulmaCarousel|bulmaSlider|setupVideoCarouselAutoplay|HELP_IMPROVE_VIDEOJS" static/js/index.js
```

Expected: no matches and exit code 1.

- [ ] **Step 3: Commit focused JavaScript**

Run:

```bash
git add static/js/index.js
git commit -m "chore: simplify homepage scripts"
```

Expected: commit succeeds and includes only `static/js/index.js`.

---

### Task 3: Metadata, Hero, And Pipeline HTML

**Files:**
- Modify: `index.html`
- Test: `scripts/check-homepage.sh`

- [ ] **Step 1: Replace `index.html` head with GenLIP metadata**

Use this head structure at the top of `index.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="title" content="Let ViT Speak: Generative Language-Image Pre-training">
  <meta name="description" content="GenLIP is a minimalist generative pretraining framework that turns ViTs into scalable vision encoders for multimodal large language models.">
  <meta name="keywords" content="GenLIP, Vision Transformer, vision-language pretraining, multimodal large language models, vision encoder, OCR, document understanding">
  <meta name="author" content="Yan Fang, Mengcheng Lan, Zilong Huang, Weixian Lei, Yunqing Zhao, Yujie Zhong, Yingchen Yu, Qi She, Yao Zhao, Yunchao Wei">
  <meta name="robots" content="index, follow">
  <meta name="language" content="English">
  <meta property="og:type" content="article">
  <meta property="og:site_name" content="GenLIP Project Page">
  <meta property="og:title" content="Let ViT Speak: Generative Language-Image Pre-training">
  <meta property="og:description" content="Pretrain by speaking, deploy as a vision encoder for MLLMs.">
  <meta property="og:url" content="https://yanfangcs.github.io/vitspeak">
  <meta property="og:image" content="https://yanfangcs.github.io/vitspeak/static/images/social_preview.svg">
  <meta property="og:image:alt" content="GenLIP project preview with token pipeline">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Let ViT Speak: Generative Language-Image Pre-training">
  <meta name="twitter:description" content="A minimalist generative pretraining framework for scalable MLLM vision encoders.">
  <meta name="twitter:image" content="https://yanfangcs.github.io/vitspeak/static/images/social_preview.svg">
  <meta name="citation_title" content="Let ViT Speak: Generative Language-Image Pre-training">
  <meta name="citation_author" content="Fang, Yan">
  <meta name="citation_author" content="Lan, Mengcheng">
  <meta name="citation_author" content="Huang, Zilong">
  <meta name="citation_author" content="Lei, Weixian">
  <meta name="citation_author" content="Zhao, Yunqing">
  <meta name="citation_author" content="Zhong, Yujie">
  <meta name="citation_author" content="Yu, Yingchen">
  <meta name="citation_author" content="She, Qi">
  <meta name="citation_author" content="Zhao, Yao">
  <meta name="citation_author" content="Wei, Yunchao">
  <meta name="citation_publication_date" content="2026">
  <meta name="citation_pdf_url" content="https://yanfangcs.github.io/vitspeak/static/pdfs/paper.pdf">
  <meta name="theme-color" content="#0b3038">
  <title>Let ViT Speak: Generative Language-Image Pre-training</title>
  <link rel="icon" type="image/x-icon" href="static/images/favicon.ico">
  <link rel="stylesheet" href="static/css/bulma.min.css">
  <link rel="stylesheet" href="static/css/fontawesome.all.min.css">
  <link rel="stylesheet" href="static/css/index.css">
  <script defer src="static/js/fontawesome.all.min.js"></script>
  <script defer src="static/js/index.js"></script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "ScholarlyArticle",
    "headline": "Let ViT Speak: Generative Language-Image Pre-training",
    "description": "GenLIP is a minimalist generative pretraining framework for scalable MLLM vision encoders.",
    "datePublished": "2026-05-01",
    "url": "https://yanfangcs.github.io/vitspeak",
    "image": "https://yanfangcs.github.io/vitspeak/static/images/social_preview.svg",
    "isAccessibleForFree": true,
    "author": [
      {"@type": "Person", "name": "Yan Fang"},
      {"@type": "Person", "name": "Mengcheng Lan"},
      {"@type": "Person", "name": "Zilong Huang"},
      {"@type": "Person", "name": "Weixian Lei"},
      {"@type": "Person", "name": "Yunqing Zhao"},
      {"@type": "Person", "name": "Yujie Zhong"},
      {"@type": "Person", "name": "Yingchen Yu"},
      {"@type": "Person", "name": "Qi She"},
      {"@type": "Person", "name": "Yao Zhao"},
      {"@type": "Person", "name": "Yunchao Wei"}
    ],
    "about": [
      {"@type": "Thing", "name": "Vision-language pretraining"},
      {"@type": "Thing", "name": "Multimodal large language models"},
      {"@type": "Thing", "name": "Vision encoders"}
    ]
  }
  </script>
</head>
```

- [ ] **Step 2: Replace the opening body through hero pipeline**

Immediately after `</head>`, add:

```html
<body>
  <button class="scroll-to-top" onclick="scrollToTop()" title="Scroll to top" aria-label="Scroll to top">
    <i class="fas fa-chevron-up" aria-hidden="true"></i>
  </button>

  <main id="main-content">
    <section class="hero publication-hero" aria-labelledby="hero-title">
      <div class="hero-body">
        <div class="container">
          <div class="publication-kicker">GenLIP: Generative Language-Image Pre-training</div>
          <h1 class="title publication-title" id="hero-title">Let ViT Speak</h1>
          <p class="publication-subtitle">A minimalist generative pretraining framework for scalable vision encoders in multimodal large language models.</p>

          <div class="publication-authors" aria-label="Authors">
            <span class="author-block">Yan Fang<sup>*</sup></span>
            <span class="author-block">Mengcheng Lan<sup>*</sup></span>
            <span class="author-block">Zilong Huang<sup>&dagger;</sup></span>
            <span class="author-block">Weixian Lei</span>
            <span class="author-block">Yunqing Zhao</span>
            <span class="author-block">Yujie Zhong</span>
            <span class="author-block">Yingchen Yu</span>
            <span class="author-block">Qi She</span>
            <span class="author-block">Yao Zhao</span>
            <span class="author-block">Yunchao Wei<sup>&dagger;</sup></span>
          </div>

          <div class="publication-affiliations">
            <span>Beijing Jiaotong University</span>
            <span>ByteDance</span>
            <span>Nanyang Technological University</span>
          </div>
          <p class="publication-notes"><sup>*</sup>Equal contribution &nbsp; <sup>&dagger;</sup>Corresponding authors</p>

          <nav class="publication-links" aria-label="Project links">
            <a class="project-button" href="static/pdfs/paper.pdf" target="_blank" rel="noopener">
              <i class="fas fa-file-pdf" aria-hidden="true"></i><span>Paper</span>
            </a>
            <a class="project-button" href="static/pdfs/paper.pdf" target="_blank" rel="noopener">
              <i class="fas fa-book-open" aria-hidden="true"></i><span>arXiv</span>
            </a>
            <a class="project-button" href="#release-code">
              <i class="fab fa-github" aria-hidden="true"></i><span>Code</span>
            </a>
            <a class="project-button" href="#release-models">
              <i class="fas fa-cube" aria-hidden="true"></i><span>Model</span>
            </a>
            <a class="project-button" href="#demo">
              <i class="fas fa-play" aria-hidden="true"></i><span>Demo</span>
            </a>
          </nav>

          <div class="hero-pipeline" role="img" aria-label="GenLIP trains a single transformer with image and text tokens, then deploys visual embeddings as an MLLM vision encoder.">
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

          <div class="evidence-chips" aria-label="Key GenLIP facts">
            <span>Single Transformer</span>
            <span>No contrastive batches</span>
            <span>No extra text decoder</span>
            <span>8B pretraining samples</span>
            <span>MLLM vision encoder</span>
          </div>
        </div>
      </div>
    </section>
```

- [ ] **Step 3: Verify hero text is present**

Run:

```bash
rg -n "Let ViT Speak|Pretrain by speaking|Deploy as vision encoder|No contrastive batches" index.html
```

Expected: each phrase appears in `index.html`.

- [ ] **Step 4: Commit hero and metadata**

Run:

```bash
git add index.html
git commit -m "feat: add GenLIP hero narrative"
```

Expected: commit succeeds and includes `index.html`.

---

### Task 4: Abstract, Method, And Results HTML

**Files:**
- Modify: `index.html`
- Test: `scripts/check-homepage.sh`

- [ ] **Step 1: Add abstract and TL;DR sections after the hero**

After the closing `</section>` from Task 3, add:

```html
    <section class="section metrics-section" aria-labelledby="metrics-title">
      <div class="container">
        <h2 class="sr-only" id="metrics-title">Key results</h2>
        <div class="metric-grid">
          <article class="metric-card"><strong>73.6</strong><span>ALL AVG with GenLIP-g/16 and Qwen2.5-7B frozen visual representation</span></article>
          <article class="metric-card"><strong>+4.7</strong><span>ALL AVG over SigLIP2-g/16 in the same setting</span></article>
          <article class="metric-card"><strong>8B</strong><span>pretraining samples, compared with 40B-pair SigLIP2 baselines</span></article>
          <article class="metric-card"><strong>Doc/OCR</strong><span>largest gains on detail-sensitive document and text-centric benchmarks</span></article>
        </div>
      </div>
    </section>

    <section class="section paper-summary" aria-labelledby="abstract-title">
      <div class="container is-max-desktop">
        <h2 class="section-title" id="abstract-title">Abstract</h2>
        <div class="content lead-copy">
          <p>In this paper, we present <strong>Generative Language-Image Pre-training (GenLIP)</strong>, a simplified generative pretraining approach for Vision Transformers tailored to multimodal large language models. To better align ViTs with the autoregressive nature of LLMs, GenLIP trains a ViT to predict language tokens directly from visual tokens using a standard language modeling objective, without contrastive batch construction or an additional text decoder.</p>
          <p>GenLIP offers three key advantages: simplicity, scalability, and performance. With training totaling 8B samples on Recap-DataComp-1B, GenLIP matches or surpasses strong baselines such as SigLIP2. With continued pretraining on multi-resolution images at native aspect ratios, GenLIP further excels at detail-sensitive tasks such as OCR, chart understanding, and visual question answering.</p>
        </div>
        <div class="tldr-grid">
          <article><h3>Simplicity</h3><p>A single Transformer jointly models visual and linguistic tokens with one language modeling objective.</p></article>
          <article><h3>Scalability</h3><p>Performance improves with both data and model size, supported by gated attention for stable pretraining.</p></article>
          <article><h3>Performance</h3><p>GenLIP delivers strong MLLM vision encoder performance, especially on document and OCR-heavy tasks.</p></article>
        </div>
      </div>
    </section>
```

- [ ] **Step 2: Add method section after the abstract**

Append:

```html
    <section class="section method-section" aria-labelledby="method-title">
      <div class="container">
        <div class="section-heading">
          <p class="section-kicker">Method</p>
          <h2 class="section-title" id="method-title">Minimal Generative Pretraining For Vision Encoders</h2>
          <p>GenLIP uses language generation as the pretraining signal, then deploys the trained Transformer as a visual feature extractor for MLLMs.</p>
        </div>
        <div class="method-grid">
          <article class="method-card"><h3>Unified Transformer</h3><p>Image patches and text tokens are concatenated into one sequence and modeled by one Transformer.</p></article>
          <article class="method-card"><h3>Prefix-LM Objective</h3><p>Visual tokens attend bidirectionally, text tokens attend causally, and loss is applied only to text tokens.</p></article>
          <article class="method-card"><h3>Gated Attention</h3><p>A lightweight gate regulates attention outputs, reducing attention sink and stabilizing visual representation learning.</p></article>
        </div>
        <figure class="figure-panel">
          <img src="static/images/genlip-method-architecture.png" alt="GenLIP architecture with image-text sequence modeling, gated attention, and Prefix-LM attention.">
          <figcaption>Training uses the LM head for next-token prediction; deployment keeps the Transformer visual features and discards language-only modules.</figcaption>
        </figure>
      </div>
    </section>
```

- [ ] **Step 3: Add results section after method**

Append:

```html
    <section class="section results-section" aria-labelledby="results-title">
      <div class="container">
        <div class="section-heading">
          <p class="section-kicker">Results</p>
          <h2 class="section-title" id="results-title">Strong Vision Encoder Performance With Less Pretraining Data</h2>
          <p>GenLIP consistently improves frozen visual representation evaluation, with its clearest gains on Doc/OCR tasks.</p>
        </div>

        <div class="table-panel">
          <div class="table-header">
            <h3>Qwen2.5-7B Frozen Visual Representation</h3>
            <a href="static/pdfs/paper.pdf" target="_blank" rel="noopener">Full table in paper</a>
          </div>
          <div class="responsive-table">
            <table>
              <thead>
                <tr>
                  <th>Model</th>
                  <th>Arch</th>
                  <th>Data</th>
                  <th>Doc/OCR Avg</th>
                  <th>General VQA Highlights</th>
                  <th>Caption Highlights</th>
                  <th>ALL AVG</th>
                </tr>
              </thead>
              <tbody>
                <tr><td>OpenVision2</td><td>L/16</td><td>12.8B</td><td>49.5</td><td>VQAv2 60.0, MME-P 1325</td><td>TextCaps 133.8</td><td>64.9</td></tr>
                <tr><td>SigLIP</td><td>L/16</td><td>40.0B</td><td>52.0</td><td>ScienceQA 86.7</td><td>NoCaps 81.5, COCO 72.0</td><td>64.5</td></tr>
                <tr><td>SigLIP2</td><td>g/16</td><td>40.0B</td><td>53.2</td><td>ScienceQA 87.7, MME-P 1422</td><td>TextCaps 142.7</td><td>68.9</td></tr>
                <tr class="highlight-row"><td>GenLIP</td><td>g/16</td><td>8.0B</td><td>62.1</td><td>GQA 54.5, MME-P 1483</td><td>NoCaps 85.0, TextCaps 144.8</td><td>73.6</td></tr>
              </tbody>
            </table>
          </div>
        </div>

        <div class="result-figure-grid">
          <figure class="figure-panel">
            <img src="static/images/genlip-data-scale.png" alt="Data scaling curves for OCR, VQA, and Caption tasks from 1B to 8B pretraining samples.">
            <figcaption>Data scaling shows sustained gains, with gated attention improving stability across scales.</figcaption>
          </figure>
          <figure class="figure-panel">
            <img src="static/images/genlip-stage2-validation.png" alt="Stage 1 versus Stage 2 validation curves across evaluation resolutions.">
            <figcaption>Native-aspect adaptation improves OCR, VQA, and caption performance at higher evaluation resolutions.</figcaption>
          </figure>
        </div>
      </div>
    </section>
```

- [ ] **Step 4: Verify required content now exists**

Run:

```bash
rg -n "73.6|\\+4.7|Minimal Generative Pretraining|Qwen2.5-7B|static/images/genlip-data-scale.png" index.html
```

Expected: all patterns are found in `index.html`.

- [ ] **Step 5: Commit summary, method, and results HTML**

Run:

```bash
git add index.html
git commit -m "feat: add GenLIP summary method and results"
```

Expected: commit succeeds and includes `index.html`.

---

### Task 5: Qualitative Probes, Demo, Release, Footer

**Files:**
- Modify: `index.html`
- Test: `scripts/check-homepage.sh`

- [ ] **Step 1: Add qualitative probe and demo sections after results**

Append:

```html
    <section class="section probes-section" aria-labelledby="probes-title">
      <div class="container">
        <div class="section-heading">
          <p class="section-kicker">Representation Probes</p>
          <h2 class="section-title" id="probes-title">What does &quot;speak&quot; reveal?</h2>
          <p>Generation and patch readout are used here to inspect the learned visual-language representation, not to redefine GenLIP as a captioning model.</p>
        </div>
        <div class="probe-grid">
          <figure class="figure-panel">
            <img src="static/images/genlip-caption-examples.png" alt="GenLIP caption generation examples comparing model scales and pretraining stages.">
            <figcaption>Direct caption generation shows that the pretrained ViT can produce grounded descriptions from visual tokens.</figcaption>
          </figure>
          <figure class="figure-panel">
            <img src="static/images/genlip-patch-semantics.png" alt="Patch semantic readout showing local visual regions mapped to language tokens.">
            <figcaption>Patch semantics reveal local visual embeddings aligned with language concepts.</figcaption>
          </figure>
        </div>
        <figure class="figure-panel wide-figure">
          <img src="static/images/genlip-ocr-examples.png" alt="OCR-heavy GenLIP generation probes on receipt, geometry, and tiny text examples.">
          <figcaption>OCR-heavy probes explain the strong Doc/OCR benchmark behavior and expose remaining failure modes.</figcaption>
        </figure>
      </div>
    </section>

    <section class="section demo-section" id="demo" aria-labelledby="demo-title">
      <div class="container">
        <div class="demo-panel">
          <div>
            <p class="section-kicker">Demo</p>
            <h2 class="section-title" id="demo-title">Explore GenLIP Through Generation Probes</h2>
            <p>Explore the pretrained encoder's visual-language alignment through generation probes. The deployed model is intended as an MLLM vision encoder.</p>
          </div>
          <div class="demo-samples" aria-label="Demo sample categories">
            <span>Natural image</span>
            <span>Document/OCR</span>
            <span>Chart or diagram</span>
            <span>Tiny text</span>
          </div>
          <a class="project-button light-button" href="#release-code">Demo entry</a>
        </div>
      </div>
    </section>
```

- [ ] **Step 2: Add release hub and citation**

Append:

```html
    <section class="section release-section" id="release" aria-labelledby="release-title">
      <div class="container">
        <div class="section-heading">
          <p class="section-kicker">Release</p>
          <h2 class="section-title" id="release-title">Paper, Code, Models, And Citation</h2>
          <p>The first release path keeps all resources visible from the first viewport and collected here for repeated access.</p>
        </div>
        <div class="release-grid" id="release-models">
          <article class="release-card"><h3>GenLIP-L/16</h3><p>0.3B parameters - 24 layers - recommended for efficient evaluation.</p><a href="static/pdfs/paper.pdf">Model details</a></article>
          <article class="release-card"><h3>GenLIP-So/16</h3><p>0.4B parameters - 27 layers - balanced scale for MLLM experiments.</p><a href="static/pdfs/paper.pdf">Model details</a></article>
          <article class="release-card"><h3>GenLIP-g/16</h3><p>1.1B parameters - 40 layers - strongest benchmark and Doc/OCR performance.</p><a href="static/pdfs/paper.pdf">Model details</a></article>
        </div>
        <div class="quick-links">
          <a id="release-code" href="https://github.com/yanfangcs/vitspeak" target="_blank" rel="noopener">GitHub repository</a>
          <a href="static/pdfs/paper.pdf" target="_blank" rel="noopener">Paper PDF</a>
          <a href="#demo">Demo section</a>
          <a href="GenLIP_Tech/paper.pdf" target="_blank" rel="noopener">Technical source PDF</a>
        </div>
      </div>
    </section>

    <section class="section citation-section" id="citation" aria-labelledby="citation-title">
      <div class="container is-max-desktop">
        <div class="bibtex-header">
          <h2 class="section-title" id="citation-title">BibTeX</h2>
          <button class="copy-bibtex-btn" onclick="copyBibTeX()" title="Copy BibTeX to clipboard" type="button">
            <i class="fas fa-copy" aria-hidden="true"></i>
            <span class="copy-text">Copy</span>
          </button>
        </div>
        <pre id="bibtex-code"><code>@article{fang2026letvitspeak,
  title={Let ViT Speak: Generative Language-Image Pre-training},
  author={Fang, Yan and Lan, Mengcheng and Huang, Zilong and Lei, Weixian and Zhao, Yunqing and Zhong, Yujie and Yu, Yingchen and She, Qi and Zhao, Yao and Wei, Yunchao},
  year={2026},
  url={https://yanfangcs.github.io/vitspeak}
}</code></pre>
      </div>
    </section>
  </main>

  <footer class="footer">
    <div class="container is-max-desktop">
      <p>This work was mainly sponsored by the National Natural Science Foundation of China (No. 92470203). This work was conducted during Yan Fang and Mengcheng Lan's internships at ByteDance.</p>
      <p>Website template adapted from the Academic Project Page Template and Nerfies project page.</p>
    </div>
  </footer>
</body>
</html>
```

- [ ] **Step 3: Run smoke check and confirm CSS is now the remaining blocker**

Run:

```bash
./scripts/check-homepage.sh
```

Expected: PASS if all assets from Task 1 exist and the template content has been replaced. If it fails with banned template content, remove the reported content from `index.html`.

- [ ] **Step 4: Commit qualitative, release, and citation HTML**

Run:

```bash
git add index.html
git commit -m "feat: add GenLIP probes release and citation"
```

Expected: commit succeeds and includes `index.html`.

---

### Task 6: Token Lab CSS And Responsive Layout

**Files:**
- Modify: `static/css/index.css`
- Test: `scripts/check-homepage.sh`

- [ ] **Step 1: Replace `static/css/index.css` with the GenLIP visual system**

Replace the whole file with:

```css
:root {
  --ink: #071b22;
  --muted: #58707a;
  --line: #d7e5e8;
  --panel: #ffffff;
  --wash: #f6fafb;
  --wash-strong: #eef6f7;
  --visual-token: #b9e3e5;
  --text-token: #f6eddb;
  --accent: #0b3038;
  --accent-soft: #2c6a78;
  --good: #2f7d4a;
  --radius: 8px;
  --shadow: 0 12px 30px rgba(7, 27, 34, 0.08);
}

html {
  scroll-behavior: smooth;
}

body {
  margin: 0;
  font-family: Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  color: var(--ink);
  background: var(--panel);
  line-height: 1.6;
  font-size: 16px;
}

a {
  color: var(--accent-soft);
}

a:hover {
  color: var(--accent);
}

.container {
  max-width: 1160px;
}

.section {
  padding: 4rem 1.5rem;
}

.publication-hero {
  background:
    linear-gradient(180deg, #ffffff 0%, var(--wash) 100%);
  border-bottom: 1px solid var(--line);
}

.publication-hero .hero-body {
  padding: 4.8rem 1.5rem 3.5rem;
}

.publication-kicker,
.section-kicker {
  color: var(--accent-soft);
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  font-size: 0.78rem;
  margin-bottom: 0.75rem;
}

.publication-title {
  color: var(--ink);
  font-size: clamp(3.1rem, 7vw, 6.4rem);
  line-height: 0.94;
  font-weight: 850;
  letter-spacing: 0;
  margin: 0;
  text-align: center;
}

.publication-subtitle {
  max-width: 820px;
  margin: 1.25rem auto 1.8rem;
  color: var(--muted);
  font-size: clamp(1.1rem, 2vw, 1.45rem);
  text-align: center;
}

.publication-authors,
.publication-affiliations,
.publication-notes {
  text-align: center;
  color: var(--muted);
}

.author-block,
.publication-affiliations span {
  display: inline-block;
  margin: 0.12rem 0.38rem;
}

.publication-links,
.evidence-chips,
.quick-links,
.demo-samples {
  display: flex;
  flex-wrap: wrap;
  gap: 0.65rem;
  justify-content: center;
  align-items: center;
}

.project-button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.45rem;
  min-height: 42px;
  padding: 0.7rem 1rem;
  border-radius: var(--radius);
  background: var(--accent);
  color: #ffffff;
  font-weight: 800;
  border: 1px solid var(--accent);
  box-shadow: 0 8px 18px rgba(7, 27, 34, 0.16);
}

.project-button:hover {
  color: #ffffff;
  background: var(--accent-soft);
  border-color: var(--accent-soft);
}

.hero-pipeline {
  position: relative;
  display: grid;
  grid-template-columns: 1.15fr auto 0.85fr auto 1.25fr;
  gap: 1rem;
  align-items: center;
  margin: 2.8rem auto 1.1rem;
  padding: 3.2rem 1.5rem 1.5rem;
  max-width: 1120px;
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  box-shadow: var(--shadow);
}

.pipeline-label {
  position: absolute;
  top: 1rem;
  font-weight: 850;
  color: var(--accent);
}

.pipeline-label-left {
  left: 1.5rem;
}

.pipeline-label-right {
  right: 1.5rem;
}

.pipeline-stage {
  min-height: 130px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 0.65rem;
  padding: 1rem;
  border: 1px solid var(--line);
  border-radius: var(--radius);
  background: var(--wash);
  text-align: center;
}

.token-row {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 0.35rem;
}

.token {
  width: 32px;
  height: 38px;
  border: 3px solid var(--accent);
  border-radius: 8px;
  display: inline-block;
}

.visual-token {
  background: var(--visual-token);
}

.text-token {
  background: var(--text-token);
}

.token-plus,
.pipeline-arrow {
  color: var(--accent);
  font-size: 2rem;
  font-weight: 900;
}

.transformer-stage {
  background: var(--wash-strong);
}

.transformer-stage strong {
  font-size: 1.05rem;
}

.transformer-stage span,
.pipeline-stage p {
  color: var(--muted);
  font-size: 0.92rem;
  margin: 0;
}

.deploy-flow {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 0.5rem;
}

.deploy-flow span,
.evidence-chips span,
.demo-samples span {
  padding: 0.55rem 0.7rem;
  border: 1px solid var(--line);
  border-radius: var(--radius);
  background: #ffffff;
  color: var(--accent);
  font-weight: 800;
  font-size: 0.9rem;
}

.metrics-section {
  padding-top: 2.5rem;
  padding-bottom: 2.5rem;
  background: var(--panel);
}

.metric-grid,
.tldr-grid,
.method-grid,
.release-grid {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 1rem;
}

.metric-card,
.tldr-grid article,
.method-card,
.release-card,
.table-panel,
.figure-panel,
.demo-panel {
  border: 1px solid var(--line);
  border-radius: var(--radius);
  background: var(--panel);
  box-shadow: 0 6px 20px rgba(7, 27, 34, 0.06);
}

.metric-card {
  padding: 1.2rem;
  min-height: 130px;
}

.metric-card strong {
  display: block;
  color: var(--accent);
  font-size: 2rem;
  line-height: 1;
  margin-bottom: 0.65rem;
}

.metric-card span,
.lead-copy,
.section-heading p,
.figure-panel figcaption,
.release-card p,
.footer {
  color: var(--muted);
}

.paper-summary,
.results-section,
.demo-section {
  background: var(--wash);
}

.section-heading {
  max-width: 820px;
  margin: 0 auto 2rem;
  text-align: center;
}

.section-title {
  font-size: clamp(1.9rem, 4vw, 3rem);
  line-height: 1.08;
  font-weight: 850;
  letter-spacing: 0;
  margin: 0 0 1rem;
}

.lead-copy {
  font-size: 1.08rem;
}

.tldr-grid,
.method-grid {
  grid-template-columns: repeat(3, minmax(0, 1fr));
  margin-top: 2rem;
}

.tldr-grid article,
.method-card,
.release-card {
  padding: 1.2rem;
}

.tldr-grid h3,
.method-card h3,
.release-card h3,
.table-header h3 {
  margin: 0 0 0.6rem;
  font-size: 1.08rem;
  font-weight: 850;
}

.figure-panel {
  padding: 1rem;
  margin: 1.5rem 0 0;
}

.figure-panel img {
  display: block;
  width: 100%;
  height: auto;
  border-radius: var(--radius);
}

.figure-panel figcaption {
  margin-top: 0.85rem;
  font-size: 0.95rem;
}

.table-panel {
  padding: 1rem;
}

.table-header {
  display: flex;
  justify-content: space-between;
  gap: 1rem;
  align-items: center;
  margin-bottom: 0.8rem;
}

.responsive-table {
  overflow-x: auto;
}

table {
  width: 100%;
  border-collapse: collapse;
  min-width: 820px;
}

th,
td {
  padding: 0.85rem;
  border-bottom: 1px solid var(--line);
  text-align: left;
  vertical-align: top;
}

th {
  color: var(--accent);
  background: var(--wash);
  font-size: 0.86rem;
}

.highlight-row {
  background: #eef8f6;
  font-weight: 750;
}

.result-figure-grid,
.probe-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 1.2rem;
}

.wide-figure {
  max-width: 980px;
  margin-left: auto;
  margin-right: auto;
}

.demo-panel {
  display: grid;
  grid-template-columns: 1.3fr 1fr auto;
  align-items: center;
  gap: 1.25rem;
  padding: 1.4rem;
  background: #10252d;
  color: #ffffff;
}

.demo-panel .section-title,
.demo-panel .section-kicker,
.demo-panel p {
  color: #ffffff;
}

.light-button {
  background: #ffffff;
  color: var(--accent);
  border-color: #ffffff;
  box-shadow: none;
}

.light-button:hover {
  background: var(--visual-token);
  color: var(--accent);
}

.release-grid {
  grid-template-columns: repeat(3, minmax(0, 1fr));
}

.quick-links {
  margin-top: 1.25rem;
}

.quick-links a {
  border: 1px solid var(--line);
  border-radius: var(--radius);
  padding: 0.65rem 0.85rem;
  font-weight: 800;
  background: var(--panel);
}

pre {
  background: var(--wash) !important;
  border: 1px solid var(--line) !important;
  border-radius: var(--radius) !important;
  padding: 1.2rem !important;
  overflow-x: auto;
}

code {
  color: var(--ink) !important;
  background: transparent !important;
}

.bibtex-header {
  display: flex;
  justify-content: space-between;
  gap: 1rem;
  align-items: center;
}

.copy-bibtex-btn {
  border: 1px solid var(--accent);
  border-radius: var(--radius);
  background: var(--accent);
  color: #ffffff;
  font-weight: 800;
  padding: 0.65rem 0.9rem;
  cursor: pointer;
}

.copy-bibtex-btn.copied {
  background: var(--good);
  border-color: var(--good);
}

.footer {
  background: var(--wash);
  border-top: 1px solid var(--line);
  padding: 2rem 1.5rem;
}

.scroll-to-top {
  position: fixed;
  right: 1.25rem;
  bottom: 1.25rem;
  width: 44px;
  height: 44px;
  border-radius: 50%;
  border: 0;
  background: var(--accent);
  color: #ffffff;
  opacity: 0;
  visibility: hidden;
  z-index: 10;
  cursor: pointer;
}

.scroll-to-top.visible {
  opacity: 1;
  visibility: visible;
}

.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}

a:focus,
button:focus {
  outline: 3px solid var(--visual-token);
  outline-offset: 3px;
}

@media screen and (max-width: 900px) {
  .hero-pipeline {
    grid-template-columns: 1fr;
    padding-top: 4.5rem;
  }

  .pipeline-label {
    position: static;
    text-align: center;
  }

  .pipeline-label-left {
    order: -5;
  }

  .pipeline-label-right {
    order: -1;
  }

  .pipeline-arrow {
    transform: rotate(90deg);
    justify-self: center;
  }

  .metric-grid,
  .tldr-grid,
  .method-grid,
  .release-grid,
  .result-figure-grid,
  .probe-grid,
  .demo-panel {
    grid-template-columns: 1fr;
  }

  .metric-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}

@media screen and (max-width: 560px) {
  .section {
    padding: 3rem 1rem;
  }

  .publication-hero .hero-body {
    padding: 3.5rem 1rem 2.5rem;
  }

  .publication-title {
    font-size: 3rem;
  }

  .publication-links .project-button {
    width: 100%;
  }

  .metric-grid {
    grid-template-columns: 1fr;
  }

  .table-header,
  .bibtex-header {
    flex-direction: column;
    align-items: flex-start;
  }

  .deploy-flow {
    grid-template-columns: 1fr;
  }
}
```

- [ ] **Step 2: Run smoke check**

Run:

```bash
./scripts/check-homepage.sh
```

Expected: `Homepage smoke checks passed`.

- [ ] **Step 3: Commit CSS**

Run:

```bash
git add static/css/index.css scripts/check-homepage.sh
git commit -m "style: add GenLIP homepage visual system"
```

Expected: commit succeeds and includes `static/css/index.css`; `scripts/check-homepage.sh` is included only if it changed after Task 1.

---

### Task 7: Local Browser Verification And Final Cleanup

**Files:**
- Modify: `index.html` and `static/css/index.css` only for fixes revealed by verification
- Test: `scripts/check-homepage.sh`

- [ ] **Step 1: Start a local static server**

Run:

```bash
python3 -m http.server 8000
```

Expected: prints `Serving HTTP on :: port 8000` or `Serving HTTP on 0.0.0.0 port 8000`.

- [ ] **Step 2: Open the local page in the in-app browser**

Open:

```text
http://localhost:8000
```

Expected: page loads with the centered title, full-width train/deploy pipeline, metric strip, abstract, method, results, probes, demo, release hub, and BibTeX.

- [ ] **Step 3: Verify desktop visual requirements**

Check at a desktop viewport:

```text
The first viewport states "Let ViT Speak" and "vision encoders in multimodal large language models".
The wide hero pipeline ends at "MLLM".
The metric strip is visible without horizontal scrolling.
Figures render crisply and stay inside their containers.
The results table scrolls horizontally only inside its table wrapper.
No generic template sections are visible.
```

Expected: all statements are true.

- [ ] **Step 4: Verify mobile visual requirements**

Check at a narrow mobile viewport:

```text
Primary buttons wrap without clipped text.
The hero pipeline stacks vertically.
Metric cards are one column.
Large table remains contained in the horizontal table wrapper.
No text overlaps the next section.
```

Expected: all statements are true.

- [ ] **Step 5: Run the smoke check and template residue search**

Run:

```bash
./scripts/check-homepage.sh
rg -n "TO""DO|Lorem ipsum|PAPER_TITLE|YOUR_DOMAIN|Academic Project Page|Another Carousel|Video Presentation|Poster|More Works" index.html static/css/index.css static/js/index.js
```

Expected: smoke check passes; `rg` returns no matches and exit code 1.

- [ ] **Step 6: Check working tree scope**

Run:

```bash
git status --short
```

Expected: only homepage implementation files, generated assets, and planned script changes are modified or untracked. Existing untracked user materials such as `GenLIP_Tech/`, `paper_version2.pdf`, `.DS_Store`, and `.superpowers/` remain unstaged unless the user explicitly asks to track them.

- [ ] **Step 7: Commit verified homepage**

Run:

```bash
git add index.html static/css/index.css static/js/index.js static/pdfs/paper.pdf static/images/genlip-method-architecture.png static/images/genlip-data-scale.png static/images/genlip-stage2-validation.png static/images/genlip-attention-sink.png static/images/genlip-caption-examples.png static/images/genlip-ocr-examples.png static/images/genlip-patch-semantics.png static/images/social_preview.svg scripts/check-homepage.sh
git commit -m "feat: build GenLIP academic homepage"
```

Expected: commit succeeds and does not stage `GenLIP_Tech/`, `paper_version2.pdf`, `.DS_Store`, or `.superpowers/`.

---

## Self-Review

Spec coverage:

- Hero top/bottom structure: Task 3.
- Wide train/deploy pipeline with MLLM vision encoder endpoint: Task 3.
- Evidence strip with headline results: Task 4.
- Abstract and TL;DR cards: Task 4.
- Method cards and method figure: Task 4.
- Results table, scaling, and native-aspect curves: Task 4.
- Qualitative probes framed as representation evidence: Task 5.
- Demo section after probes: Task 5.
- Release hub with model cards and links: Task 5.
- BibTeX, metadata, and acknowledgement: Tasks 3 and 5.
- Static assets and PDF figure conversion: Task 1.
- Responsive and accessibility requirements: Tasks 6 and 7.
- Verification commands and visual checks: Tasks 1, 6, and 7.

Placeholder scan:

- The plan intentionally uses current functional links for missing public URLs: local paper PDF and in-page anchors. There are no unresolved marker strings in the implementation steps.

Type and naming consistency:

- CSS class names referenced in HTML are defined in Task 6.
- JavaScript functions referenced in HTML are defined in Task 2.
- Asset filenames used in HTML are created in Task 1.
