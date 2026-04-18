dance: `src/config/generator.ts`
- regression tests: `src/hooks/__tests__/prompt-guidance-*.test.ts`

In this repository, `prompts/*.md` remain the canonical source files even when their installed runtime form is injected into TOML or other launcher-specific wrappers. Treat the XML-tagged prompt body itself as the canonical role surface.

This document is the contributor-oriented index for those surfaces.

## Exact-model mini adaptation seam

OMX also has a narrow **instruction-composition seam** for subagents/workers whose **final resolved model** is exactly `gpt-5.4-mini`.
That seam is part of prompt delivery, but it is intentionally narrower than the general GPT-5.4 behavioral contract described below.

Contributor rules for that seam: