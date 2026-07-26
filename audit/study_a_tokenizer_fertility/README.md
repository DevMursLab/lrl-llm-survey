# Study A - Tokenizer Fertility & Cost Asymmetry Audit

## Status: Pilot (Bengali-English only)

This directory currently contains a **single-language-pair pilot**, not
the full 12-language audit described in the paper blueprint.

### Why a pilot first

The originally planned corpus, FLORES-200 (and its `openlanguagedata/flores_plus`
mirror), is a **gated dataset on HuggingFace** and requires an
authenticated access token that was not available when this pilot was
run. To validate the measurement pipeline without blocking on that
access, this pilot uses `Helsinki-NLP/tatoeba_mt` (`ben-eng` config),
which is ungated and provides 2,499 parallel Bengali-English sentence
pairs.

### What this pilot does NOT yet cover

- Only Bengali vs. English - none of the other 11 target languages
  (Assamese, Odia, Nepali, Sinhala, Urdu, Sindhi, Maithili, Bhojpuri,
  Santali, Manipuri, Sylheti) are included, because Tatoeba does not
  have parallel data for most of them.
- Only 6 tokenizers (GPT-4/o200k, XLM-R, NLLB, BanglaBERT, MuRIL, mT5)
  rather than the full 9+ list (Llama-3, Gemma-2, Qwen2 require gated
  or auth-walled access on HuggingFace and were not run here).
- Cost-premium in USD is only computed for GPT-4/o200k, since that is
  the only tokenizer here with public per-token API pricing tracked.

### Files

- `run_fertility_pilot.py` - the pipeline (fertility, token premium,
  byte efficiency, context-window shrinkage).
- `results/study_a_pilot_results.csv` - raw per-tokenizer, per-language
  metrics.
- `results/study_a_pilot_summary.json` - aggregate Bengali summary.

### Pilot findings (n=2,499 parallel pairs)

| Tokenizer | Bengali fertility | Token premium vs. English | Context shrinkage |
|---|---|---|---|
| GPT-4/o200k | 2.08 | 1.67x | 40.0% |
| mT5 | 2.72 | 1.51x | 33.7% |
| XLM-R | 2.37 | 1.25x | 20.1% |
| NLLB | 2.17 | 1.16x | 13.6% |
| MuRIL | 1.92 | 1.05x | 4.8% |
| BanglaBERT | 1.78 | 0.78x | -27.6% (Bengali is *cheaper* than English) |

The BanglaBERT result is expected and worth keeping in the paper: a
tokenizer trained with a Bengali-specific vocabulary allocation removes
the premium entirely and inverts it, which is itself evidence for the
paper's argument that the premium is a vocabulary-allocation problem,
not an inherent property of the script.

### To complete the full study

1. Obtain a HuggingFace access token with read permission and request
   access to `facebook/flores` (or `openlanguagedata/flores_plus`).
2. Extend `TOKENIZERS` in the script with the gated model IDs (Llama-3,
   Gemma-2, Qwen2), which also require accepting their model licenses
   on HuggingFace.
3. Re-run across all 12 target languages using FLORES-200 devtest
   (1,012 perfectly parallel sentences per language) instead of Tatoeba.
4. Recompute cost premiums using current provider pricing at time of
   writing (verify before citing - pricing changes).
