# GenLIP Academic Homepage Design

Date: 2026-05-01

## Context

This spec defines the academic project homepage for the paper **Let ViT Speak: Generative Language-Image Pre-training**. The source material is in `paper_version2.pdf` and `GenLIP_Tech/`.

The homepage is primarily a paper release page for researchers, with strong first-viewport access to the public release assets: paper, code, model, and demo. The page should make the work memorable through the phrase **Let ViT Speak**, while keeping the core technical positioning clear: **GenLIP is a generative pretraining framework for building scalable vision encoders in MLLMs**.

## Confirmed Direction

Use the **Vision Encoder Storyline**:

> Pretrain by speaking, deploy as a vision encoder.

The page should explain that GenLIP trains a ViT to predict language tokens from visual tokens, but the deployed artifact is a vision encoder for multimodal large language models. Captioning and patch readout examples are evidence probes of learned visual-language representations, not the main product claim.

## Goals

- Make the paper's core idea understandable within the first 5 seconds.
- Preserve the central theme that GenLIP is a **vision encoder** for MLLMs.
- Show evidence quickly: simplicity, data efficiency, Doc/OCR strength, scaling behavior.
- Provide launch-ready access to Paper, arXiv, Code, Model, and Demo.
- Convert dense paper figures and tables into a scan-friendly academic web page.
- Keep the visual style distinctive but credible for researchers.

## Non-Goals

- Do not make the page primarily a product landing page.
- Do not let the live demo dominate the research contribution.
- Do not paste every paper table in full density.
- Do not present GenLIP as a captioning model; generation is a pretraining signal and interpretability probe.
- Do not introduce unrelated template sections such as generic carousels, poster embeds, or unused video areas.

## Audience And Priority

Priority order:

1. Researchers and reviewers who need to understand method novelty, evidence, and baselines.
2. Engineers and open-source users looking for code, checkpoints, quick-start, and demo.
3. Broader launch traffic that should remember the **Let ViT Speak** concept.

## Visual System

Use a restrained **Token Lab** style:

- Main background: clean white and very light blue-gray surfaces.
- Visual-token accent: aqua/cyan, derived from the paper diagrams.
- Text-token accent: warm cream, derived from the paper diagrams.
- Structure lines: dark blue-green technical strokes.
- Typography: modern academic sans-serif, high readability, no decorative type.
- Cards: subtle borders and low-radius containers. Avoid nested cards and heavy drop shadows.
- Motifs: token blocks and pipeline arrows should serve information structure, not decoration.

Use higher contrast, darker panels only inside the demo or qualitative probe area if needed.

## Information Architecture

Recommended page order:

1. Hero
2. Evidence strip
3. Abstract and TL;DR
4. Method
5. Results
6. Qualitative probes and demo
7. Release hub
8. BibTeX and acknowledgements

## Hero

Use a **top / bottom** layout rather than a left / right split.

Top section:

- Centered paper identity.
- H1: **Let ViT Speak**
- Full name near the title: **GenLIP: Generative Language-Image Pre-training**
- Subtitle: **A minimalist generative pretraining framework for scalable vision encoders in multimodal large language models.**
- Authors and affiliations:
  - Yan Fang, Mengcheng Lan, Zilong Huang, Weixian Lei, Yunqing Zhao, Yujie Zhong, Yingchen Yu, Qi She, Yao Zhao, Yunchao Wei
  - Beijing Jiaotong University, ByteDance, Nanyang Technological University
- Equal contribution and corresponding author markers.
- Primary buttons: Paper, arXiv, Code, Model, Demo.

Bottom section:

- A full-width custom pipeline teaser, designed for the webpage rather than copied directly from the paper figure.
- It should show:
  - **Pretrain by speaking**: image tokens plus text tokens enter a single GenLIP Transformer and are trained with language modeling loss.
  - **Deploy as vision encoder**: tokenizer and LM head are discarded; visual embeddings flow through a projector into an MLLM.
- The endpoint of the figure must be MLLM vision encoding, not caption generation.

Evidence chips below or integrated into the wide teaser:

- Single Transformer
- No contrastive batches
- No extra text decoder
- 8B pretraining samples
- MLLM vision encoder

## Evidence Strip

Place a compact metric strip immediately after the hero or after the abstract intro. Use 3 to 4 metrics:

- **73.6 ALL AVG** under the GenLIP-g/16 + Qwen2.5-7B frozen visual representation setting.
- **+4.7 over SigLIP2-g/16** under the same Qwen2.5-7B frozen setting.
- **8B samples** compared with 40B-pair SigLIP2 baselines.
- **Doc/OCR strength** across ChartQA, OCRBench, DocVQA, TextVQA, InfoVQA, AI2D, and SEED-Bench-2-Plus.

Include concise setting labels so the metrics are not overgeneralized.

## Abstract And TL;DR

Use the paper abstract, lightly formatted for web reading. Directly below it, add three short cards:

- **Simplicity**: a single Transformer with standard LM objective.
- **Scalability**: scales with data and model size, with gated attention stabilizing training.
- **Performance**: strong MLLM results, especially on detail-sensitive Doc/OCR tasks.

## Method

Method should be understandable without reading the full paper.

Recommended structure:

- A short section title such as **Minimal Generative Pretraining for Vision Encoders**.
- Three method cards:
  - **Unified Transformer**: visual and text tokens are modeled together.
  - **Prefix-LM Objective**: visual prefix attends bidirectionally; text suffix attends causally; LM loss is applied to text tokens.
  - **Gated Attention**: alleviates attention sink and improves visual representation stability.
- A wide method figure derived from `GenLIP_Tech/figures/fig2-arch_2.png`, simplified for web reading.
- A deployment note: when used as a vision encoder, GenLIP discards tokenizer and LM head, extracts visual embeddings, and connects to an MLLM through a lightweight projector.

## Results

Results should be scan-first, detail-second.

Main result module:

- Compact grouped table comparing CLIP, AIMv2, OpenVision2, SigLIP2, and GenLIP.
- Columns grouped as Doc/OCR, General VQA, Caption, and ALL AVG.
- Prefer aggregated or selected columns over the full rotated-column paper table.
- Include a link to the full PDF table for complete numbers.

Result subsections:

- **Frozen visual representation**: primary benchmark story with Qwen2.5-1.5B and Qwen2.5-7B settings.
- **Standard LLaVA-NeXT evaluation**: secondary confirmation that the encoder remains strong in unfrozen settings.
- **Data scaling**: use `GenLIP_Tech/figures/data-scale.png`.
- **Native aspect-ratio adaptation**: use `GenLIP_Tech/figures/stage2-validation.png`.
- **Discriminative ability**: smaller supporting section for ImageNet-1K and ADE20K frozen feature evaluation.

The Doc/OCR advantage should be visually highlighted because it is the clearest practical strength of GenLIP as an MLLM vision encoder.

## Qualitative Probes

Use title: **What does "speak" reveal?**

Qualitative content:

- **Let ViT Speak caption examples** from `GenLIP_Tech/figures/caption-1-ver3.pdf` and OCR-heavy examples from `GenLIP_Tech/figures/caption-3items.pdf`.
- **Patch semantics readout** from `GenLIP_Tech/figures/patchsemantics-1-ver2.pdf`.

Positioning:

- Captioning shows that the pretrained ViT can generate grounded visual descriptions.
- Patch readout shows local visual embeddings align with language concepts.
- Both are probes of the learned representation, supporting the vision encoder story.

Avoid presenting these examples as the main benchmark or final product.

## Demo

Place demo after the qualitative probes.

Recommended copy:

> Explore the pretrained encoder's visual-language alignment through generation probes.

Demo should include:

- Link or embedded preview for the online demo.
- Fixed examples: natural image, document/OCR, chart or diagram, tiny text.
- A short note that generation is used here to inspect alignment; the deployed model is intended as an MLLM vision encoder.

## Release Hub

Release hub should be practical but compact.

Include:

- Model cards for GenLIP-L/16, GenLIP-So/16, and GenLIP-g/16.
- Fields for parameters, stage, recommended use, and checkpoint link.
- Quick links: GitHub, Hugging Face or model host, demo, paper, supplementary material if present.
- A short quick-start block or a link to full documentation.

If the project has multiple stage checkpoints, label them clearly as S1 and S2.

## Citation And Metadata

Include:

- BibTeX block with copy button.
- SEO and social preview metadata.
- Citation metadata for Google Scholar indexing.
- Acknowledgement:
  - Sponsored mainly by the National Natural Science Foundation of China (No. 92470203).
  - Work conducted during Yan Fang and Mengcheng Lan's internships at ByteDance.

The social preview image should use the hero title plus the wide train/deploy pipeline.

## Assets

Primary assets:

- `paper_version2.pdf`
- `GenLIP_Tech/figures/fig1-ver4-low_2.png`
- `GenLIP_Tech/figures/fig2-arch_2.png`
- `GenLIP_Tech/figures/data-scale.png`
- `GenLIP_Tech/figures/stage2-validation.png`
- `GenLIP_Tech/figures/attention-sink-ga-long.png`
- `GenLIP_Tech/figures/caption-1-ver3.pdf`
- `GenLIP_Tech/figures/caption-3items.pdf`
- `GenLIP_Tech/figures/patchsemantics-1-ver2.pdf`

PDF figures used on the webpage should be converted to web-friendly images during implementation.

## Responsive Behavior

- Desktop: centered hero identity followed by full-width pipeline teaser.
- Tablet: hero remains centered; pipeline reduces detail but keeps train/deploy labels visible.
- Mobile: pipeline stacks into three bands:
  1. Pretrain by speaking
  2. Single GenLIP Transformer
  3. Deploy as vision encoder
- Metric cards wrap to two columns on tablet and one column on narrow mobile.
- Large tables collapse into grouped cards or horizontally scrollable, labelled tables.

## Accessibility And UX

- Buttons must have clear labels and accessible names.
- Figures need alt text focused on the scientific meaning, not visual appearance only.
- Color should not be the only carrier of meaning for visual/text tokens.
- Text inside metric cards and buttons must not overflow on mobile.
- Page sections should be navigable through semantic headings.
- Avoid auto-playing video unless muted and nonessential.

## Implementation Notes

- Keep the existing static site approach unless a later implementation plan identifies a strong reason to change the stack.
- Replace remaining template marker content and remove unused generic sections.
- Use project-specific images and figures; do not keep sample carousel/video/poster content.
- Prefer custom HTML/CSS for the hero pipeline and web-native result summaries.
- Do not make broad refactors outside the homepage and its assets unless needed to remove template residue.

## Verification Criteria

Before final delivery, verify:

- The first viewport clearly states that GenLIP is for scalable MLLM vision encoders.
- The hero pipeline endpoint is MLLM vision encoding.
- Paper, arXiv, Code, Model, and Demo buttons are present.
- No sample template text remains.
- Figures render crisply on desktop and mobile.
- Result numbers match the paper source.
- Mobile layout has no overlapping text or clipped buttons.
- Browser screenshots confirm the page is visually coherent at desktop and mobile widths.
