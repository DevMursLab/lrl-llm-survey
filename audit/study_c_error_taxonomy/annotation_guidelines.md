# Study C - Native-Speaker Error Taxonomy: Annotation Guidelines

## Purpose

Identify error types in LLM-generated Bangla text that native speakers
notice but automatic metrics (BLEU/chrF/COMET) and LLM-as-judge
approaches typically miss.

## Scope of this pilot (read before annotating)

This pilot uses outputs from **a single model (Claude, Sonnet 5)**
only. The paper's full design (blueprint §D3) calls for 4 LLMs (Claude,
Gemini, Llama-3, Qwen2) across ~200 samples. That requires API access
(Groq/Google AI Studio keys) that was not available when this pilot was
built. **Do not present single-model results as multi-model findings in
the manuscript** — report this explicitly as a pilot and extend to the
other three models before final submission (see `README.md` in this
directory for the exact steps).

## The 9 Error Codes

| Code | Error type | What to look for |
|---|---|---|
| E1 | Conjunct/যুক্তাক্ষর malformation | A conjunct consonant cluster (যুক্তাক্ষর) rendered broken, split with a stray hasanta, or visually malformed |
| E2 | ZWJ/ZWNJ misuse | Invisible zero-width joiner/non-joiner characters inserted where they change or corrupt rendering |
| E3 | Register collapse (সাধু↔চলিত) | Formal (সাধু) and colloquial (চলিত) verb/pronoun forms mixed within the same passage |
| E4 | Honorific inconsistency | আপনি/তুমি/তুই forms switching inconsistently when addressing the same referent |
| E5 | Calque / English syntax leak | Bangla sentence structure that is a literal English syntax transplant, sounding unnatural to a native ear |
| E6 | Lexical anglicization | An English loanword used where a common, natural Bangla word exists and would be expected |
| E7 | Numeral/date localization fail | Mixing Bangla (১২) and Arabic (12) numerals inconsistently, or Gregorian/Bengali calendar (বঙ্গাব্দ) confusion |
| E8 | Cultural/factual localization error | Wrong festival, wrong regional geography, or another culturally-specific factual error |
| E9 | Dialect flattening | When a dialect (e.g., Sylheti) was explicitly requested, the output silently reverts to Standard Bangla |

## Annotation Procedure

1. Read the full output once before marking anything.
2. For each output, mark **every instance** of each error code that
   applies (an output can have zero, one, or several codes; a code can
   apply more than once in the same output — count occurrences).
3. Do not penalize typos or awkward phrasing that isn't captured by
   E1–E9 — the taxonomy is intentionally specific; a residual "other"
   note field is provided for anything notable that doesn't fit.
4. Annotate independently — do not discuss with co-annotators until
   all annotators have finished their independent pass.
5. Record annotator metadata once (region, primary dialect exposure,
   education) in `annotator_demographics.csv` — this is required for
   the paper's bias-mitigation reporting (Threats to Validity, F1).

## Required Annotators

Minimum 3 Bangla-speaking annotators, ideally from different regions
(to avoid all three sharing one dialect background, which would bias
E9 detection). Fleiss' κ will be computed across all three on the full
sample; target ≥0.70 per the blueprint.

## Files in this Directory

- `annotation_guidelines.md` - this file
- `llm_outputs_pilot.csv` - the generated sample outputs to annotate (single-model pilot)
- `annotations_template.csv` - blank template each annotator copies and fills in
- `annotator_demographics_template.csv` - blank demographic form
- `compute_agreement.py` - Fleiss' kappa + metric-correlation script (run after annotation)
