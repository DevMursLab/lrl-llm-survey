# Study B - Benchmark Provenance Audit

## What this measures

For each of 26 real, verifiable multilingual/Indic NLP benchmarks that
include at least one South Asian low-resource language, we coded the
provenance of that language's test data:

- **N** - Native-authored (written directly by/for speakers, no translation step)
- **H** - Human-translated (professionally translated from another source language)
- **M** - Machine-translated
- **Mixed** - either a genuine mix of the above within one benchmark, or
  provenance inherited from a source dataset (e.g., MEGA reusing XNLI)

## Method

Each entry in `benchmark_catalog.csv` was verified against its original
paper (arXiv/ACL Anthology), GitHub repository, or HuggingFace dataset
card - not assumed from the benchmark's name or reputation. Every row
carries a `source` and a `confidence` column (`high`/`medium`/`low`);
low-confidence rows are entries where the exact South Asian language
list or provenance method could not be fully confirmed from public
documentation and need a direct primary-source check before final
citation in the manuscript.

## Key finding

```
Total benchmarks catalogued:      26
Native-authored (N):               8  (30.8%)
Human-translated (H):              8  (30.8%)
Machine-translated (M):            2  ( 7.7%)
Mixed / inherited:                 8  (30.8%)

Share NOT purely native-authored:  69.2%
```

**69.2% of the South-Asian-language evaluation resources we catalogued
are not purely native-authored** - they are translated (human or
machine) from another language, or inherit provenance from an upstream
translated benchmark. This is the empirical basis for the paper's
claim that a large share of LLM evaluation on these languages is
measuring translation-artifact behavior ("translationese"), not native
language competence.

Two caveats to state honestly in the manuscript:

1. This is a **catalog of 26 benchmarks that could be verified in this
   pass**, not an exhaustive census of every South-Asian-language
   benchmark in existence. The paper should describe the sampling
   method (systematic-review benchmark list + targeted search) rather
   than imply completeness.
2. Three entries (`IndicXParaphrase`, `DialectBench`, `INCLUDE`) are
   flagged `confidence=low` because their exact South Asian language
   coverage or translation method could not be confirmed from public
   documentation in this pass - re-verify these against the primary
   paper/appendix before citing specific numbers from them.

## Files

- `benchmark_catalog.csv` - the 26-benchmark catalog with provenance
  codes, justification, source, and confidence rating.
- `analyze_provenance.py` - computes the distribution above and
  generates the stacked-bar figure.
- `figure7_provenance.pdf` / `.png` - Figure 7 for the manuscript (§10).
- `study_b_summary.json` - machine-readable summary of the findings.

## Known gaps for the full study

- Task-coverage matrix (which language x which task has zero
  benchmarks at all) is not yet built - this is the second half of
  Study B described in the blueprint and should be added as a
  follow-up table.
- Sylheti, Chakma, Santali, and Manipuri/Meitei have only narrow,
  task-specific resources (not full benchmark suites comparable to the
  rest of this catalog) - this scarcity is itself a finding worth
  stating explicitly rather than omitting these languages silently.
