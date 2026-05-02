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
