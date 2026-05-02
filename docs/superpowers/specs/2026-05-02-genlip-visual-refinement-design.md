# GenLIP Homepage Visual Refinement Design

Date: 2026-05-02

## Context

This spec is a visual refinement addendum for the GenLIP academic homepage. The current homepage already reaches the right information architecture and technical story: **Pretrain by speaking, deploy as a vision encoder**. The next goal is to improve perceived polish, editorial quality, and narrative rhythm while preserving the central GenLIP positioning.

The visual reference is `https://beyond-llms.github.io/`. The approved direction is:

> **A + small C**: Editorial academic polish, with a limited figure-first narrative treatment for the strongest results and probes.

## Goals

- Raise the homepage's visual quality from a clear engineering-style project page to a polished academic release page.
- Borrow the reference site's editorial strengths: refined typography, generous vertical rhythm, understated section rules, and concise research takeaways.
- Keep GenLIP's core theme explicit: GenLIP is a scalable **vision encoder** for MLLMs, not a captioning product.
- Reduce the current repeated-card feeling by introducing more varied section rhythm.
- Make paper figures feel like evidence anchors rather than decorative supporting assets.

## Non-Goals

- Do not convert the page into a dark reference-site clone.
- Do not change the overall page order or remove required release links.
- Do not make generation probes dominate the product claim.
- Do not add heavy JavaScript, animations, external web fonts, or new runtime dependencies.
- Do not redesign the content into a marketing landing page.

## Visual Direction

Use a refined editorial-academic style layered on top of the existing Token Lab palette.

The page should feel calmer and more premium:

- More generous whitespace between major sections.
- Serif typography for the hero title and major section titles.
- Sans-serif typography for authors, buttons, tables, captions, and dense technical text.
- Thin editorial divider rules under major section titles.
- Fewer equally weighted card boxes.
- Subtle paper-like surfaces instead of a uniformly card-heavy dashboard feel.
- Research takeaways styled as understated callouts with a left rule.

The existing palette remains the base:

- Aqua/cyan for visual-token accents.
- Warm cream for text-token accents.
- Dark blue-green for technical strokes and primary controls.
- White and very light blue-gray for page surfaces.

## Hero Refinement

The hero should remain a top/bottom layout. The top section presents paper identity; the bottom section presents the train/deploy pipeline.

Changes:

- Change the H1 from a heavy sans-serif treatment to a refined serif display treatment.
- Keep the H1 literal: **Let ViT Speak**.
- Keep the subtitle focused on vision encoders for multimodal large language models.
- Keep author and affiliation text compact and readable; avoid making it visually compete with the H1.
- Keep primary buttons visible in the first viewport, but make them feel more editorial and less chunky.
- Use a light paper-like hero background with a very subtle cyan wash, not a full dark hero.

## Pipeline Refinement

The pipeline remains the central first-viewport technical motif.

Required meaning:

1. Visual and text tokens enter one GenLIP Transformer during pretraining.
2. The model is trained through language modeling.
3. At deployment, tokenizer and LM head are discarded.
4. The endpoint is **MLLM vision encoder**.

Visual changes:

- Reduce card heaviness inside the pipeline.
- Use one elegant wide frame instead of several equally dominant boxes.
- Keep the dark central Transformer block for contrast.
- Keep arrow flow legible on desktop and stacked mobile layouts.
- Add a short takeaway below the pipeline: GenLIP is released and evaluated as a vision encoder, not as a captioning product.

## Section Rhythm

Major sections should feel more like a paper essay:

- Section titles use serif typography.
- Section headings are centered for large narrative sections.
- A thin cyan-to-blue editorial rule sits below major titles.
- Paragraph sections use constrained measure and generous line-height.
- Repeated card grids should be reduced or softened when they make the page feel mechanically uniform.

The page order stays:

1. Hero
2. Evidence metrics
3. Abstract and TL;DR
4. Method
5. Results
6. Representation probes and demo
7. Release hub
8. BibTeX and acknowledgements

## Evidence Metrics

Keep the four existing metric points:

- 73.6 ALL AVG
- +4.7 over SigLIP2-g/16
- 8B samples
- Doc/OCR strength

Visual changes:

- Make the metric strip feel like a concise evidence band, not four unrelated cards.
- Preserve mobile readability by stacking metrics cleanly.
- Keep labels precise so values are not overgeneralized.

## Figure-First Treatment

Apply the "small C" treatment only to selected results/probe areas.

Use the pattern:

1. A major figure or table.
2. A concise research takeaway beside or below it.
3. A restrained left-rule callout, inspired by the reference site's suggestion blocks.

Apply this to:

- Data scaling figure.
- Stage/native-aspect adaptation figure.
- Qualitative probe figures where useful.

Do not apply this to every section; overuse would make the page busy.

## Results Refinement

The result table should stay, but the surrounding story should improve.

Changes:

- Keep the Qwen2.5-7B frozen representation table.
- Keep Doc/OCR advantage visually highlighted.
- Use figure-first modules after the table to make scaling and native-aspect evidence easier to scan.
- Add concise takeaways that connect figures back to vision encoder quality.
- Keep the full PDF table link.

## Qualitative Probes Refinement

The probes section should become more visually memorable while keeping the correct interpretation.

Required framing:

- Caption generation and OCR-heavy examples are probes of learned visual-language alignment.
- Patch readout shows local visual embeddings aligned with language concepts.
- These are not presented as the main product.

Visual changes:

- Give the section more white space before and after.
- Use larger figure presentation for the strongest probe image.
- Pair figures with short interpretability takeaways.

## Demo And Release Refinement

The demo section should remain honest and compact.

- Keep the copy clear that generation is used to inspect alignment.
- Keep the CTA as release-oriented unless a real demo URL is available.
- Release cards should become quieter and more editorial.
- Quick links should remain practical and visible.

## Mobile Requirements

Mobile must remain first-class:

- Buttons wrap without clipped text.
- The pipeline stacks in the correct order.
- Section titles do not overflow.
- Figures stay inside containers.
- Tables scroll only inside the table wrapper.
- BibTeX remains horizontally scrollable without page overflow.

## Accessibility Requirements

- Maintain meaningful image alt text.
- Preserve existing table semantics.
- Preserve visible focus states.
- Ensure hidden scroll-to-top button is not keyboard-focusable while hidden.
- Do not rely on color alone for key meaning.
- Keep sufficient contrast in dark pipeline and demo panels.

## Implementation Scope

Expected files:

- `index.html`: small structural additions for editorial takeaways and figure-first wrappers.
- `static/css/index.css`: main visual refinement work.
- `scripts/check-homepage.sh`: update only if new required text needs smoke coverage.

No new dependencies or external font requests should be added.

## Acceptance Criteria

- The first viewport feels more refined and academic while still immediately communicating **Let ViT Speak** and the vision encoder story.
- The pipeline endpoint remains MLLM vision encoding.
- Results/probes have clearer visual hierarchy and stronger figure-led storytelling.
- The page no longer feels like a sequence of similar cards.
- Smoke check passes.
- Template residue search remains clean.
- Browser review confirms no obvious overlap, clipped text, broken images, console errors, or missing local assets.
