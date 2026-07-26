# OSF Preregistration Draft

**Status:** draft — not yet submitted to OSF Registries. Fill in every
`[TODO]` field, then copy into the OSF Preregistration form at
https://osf.io/registries → New Registration → "OSF Preregistration"
template, and record the resulting DOI in this file and in the paper's
Methodology section.

> This document is the single most important gate before writing the
> manuscript body: registering it **before** database searching begins
> is what lets the paper say "the review protocol was pre-registered
> prior to screening" — the sentence that pre-empts the "post-hoc
> cherry-picking" rejection line.

---

## 1. Title

Low-Resource Language NLP in the Era of Large Language Models: A
Systematic Review and Empirical Audit of the Bangla and South Asian
Language Ecosystem

## 2. Authors

- [TODO: Full name], [TODO: Affiliation — Netrakona University]
- Md. Shovon (Supervisor), [TODO: Affiliation]

## 3. Research Questions

- **RQ1:** How has research on LLM-era NLP for South Asian low-resource
  languages evolved (2019–2026) in terms of task coverage, model
  families, adaptation methods, and evaluation practice?
- **RQ2:** Where in the LLM pipeline — script/encoding, data, tokenization,
  adaptation, evaluation, or deployment — do the largest unaddressed
  gaps concentrate, and how does this differ across language typology
  and resource tier?
- **RQ3:** What is the measurable magnitude of tokenization cost
  asymmetry, benchmark translation-provenance bias, and native-speaker-
  perceptible error patterns for Bangla and related languages under
  current LLMs, and do standard automatic metrics detect these errors?

## 4. Hypotheses / Expected Patterns (stated in advance, non-binding)

- H1: The share of studies addressing dialectal variation (Sylheti,
  Chittagonian, etc.) will be small relative to Standard Bangla-only work.
- H2: A majority of evaluation benchmarks used for these languages will
  be human- or machine-translated rather than natively authored.
- H3: Tokenizer fertility for Bangla and related Brahmic-script languages
  will exceed English by a factor >1, varying by tokenizer vocabulary design.
- H4: Automatic metrics (BLEU/chrF/COMET/LLM-as-judge) will show weak
  correlation with native-speaker-identified error counts in Bangla output.

These are stated to be falsifiable, not to be defended if disconfirmed —
any of H1–H4 turning out false is itself a reportable finding.

## 5. Databases to Search

1. ACL Anthology
2. arXiv (cs.CL)
3. OpenAlex (Scopus/WoS proxy — see justification below)
4. Semantic Scholar (also used for backward/forward snowballing)
5. IEEE Xplore
6. ACM Digital Library

**Justification for OpenAlex in place of Scopus/Web of Science:**
[TODO: confirm institutional access status] — if no institutional
Scopus/WoS access is available, the paper will state: "Scopus and Web
of Science were queried via OpenAlex (v3 API) owing to institutional
access constraints; OpenAlex indexes over 250 million works and shows
high overlap with Scopus for NLP venues."

## 6. Search String

```
(
  "low-resource language*" OR "low resource NLP" OR "under-resourced language*"
  OR "underrepresented language*" OR "long-tail language*" OR "endangered language*"
)
AND
(
  "large language model*" OR "LLM" OR "foundation model*"
  OR "multilingual model*" OR "instruction tun*" OR "in-context learning"
  OR "GPT" OR "LLaMA" OR "Gemma" OR "Mistral" OR "BLOOM" OR "mT5"
)
AND
(
  Bangla OR Bengali OR Assamese OR Sylheti OR Odia OR Oriya OR Nepali
  OR Maithili OR Bhojpuri OR Santali OR Bodo OR Manipuri OR Meitei
  OR Chakma OR Rohingya OR Urdu OR Sindhi OR Pashto OR Sinhala
  OR Dhivehi OR "South Asia*" OR Indic OR "Indo-Aryan"
)
```

- **Date range:** 2019-01-01 to [TODO: search execution date]. Rationale:
  transformer-era pretraining paradigm shift (post-BERT).
- **Publication language filter:** English full text required (declared
  as a limitation in Threats to Validity — see §8 of the paper).

## 7. Inclusion Criteria (IC)

| Code | Criterion |
|---|---|
| IC1 | At least one low-resource language (Joshi et al. 2020 class 0–3) with empirical or methodological contribution |
| IC2 | Involves an LLM or large pretrained multilingual model |
| IC3 | Peer-reviewed venue, or arXiv preprint with ≥10 citations |
| IC4 | Full text available in English |
| IC5 | Published 2019–2026 |

## 8. Exclusion Criteria (EC)

| Code | Criterion |
|---|---|
| EC1 | High-resource languages only (English/Chinese-only) |
| EC2 | Speech-only, no textual/linguistic component |
| EC3 | Abstract/poster/extended abstract (<4 pages) |
| EC4 | Duplicate of an already-included publication (keep the published version, drop preprint) |
| EC5 | Non-NLP application where language is incidental |

## 9. Screening Process

- Records deduplicated by DOI/title+year after export from all 6 databases plus snowballing.
- Title/abstract screening performed by [TODO: name] against IC/EC above.
- **≥20% of records** independently double-screened by a second
  reviewer ([TODO: co-screener name]).
- Disagreements resolved by discussion; unresolved cases go to
  third-party arbitration ([TODO: arbitrator name]).
- **Cohen's κ** will be computed and reported on the dual-screened
  sample; target ≥0.75 ("substantial agreement" per Landis & Koch 1977).
  If κ < 0.75, screening criteria will be clarified and a further
  sample re-screened before continuing — this will be reported
  transparently, not hidden.
- Full-text eligibility assessment applies IC/EC again to the surviving
  set; exclusion reasons recorded per EC code for the PRISMA flow diagram.

## 10. Data Extraction Fields (22 fields — see full codebook)

Paper ID/DOI, year, venue+type, author affiliation country, languages
studied, Joshi class per language, script(s), task(s), taxonomy layer
(L1–L6), model family, model size, adaptation method, data source,
dataset size, evaluation benchmark, benchmark origin (native/human-
translated/machine-translated/synthetic), metrics reported, human
evaluation (Y/N + count), code released (Y/N), data released (Y/N),
dialect addressed (Y/N), reported limitations (free text), quality
score (0–10, rubric below).

Full field-by-field codebook: `protocol/extraction_form_codebook.md`
[TODO: create alongside first extraction pass].

## 11. Quality Appraisal Rubric (custom 10-point — justified in-paper)

| Criterion | Points |
|---|---|
| Reproducibility: code + data + seeds public | 0–2 |
| Baselines: ≥2 competitive baselines compared | 0–2 |
| Statistical rigor: multi-seed, CI, or significance test | 0–2 |
| Evaluation validity: native (not machine-translated) benchmark | 0–2 |
| Native-speaker involvement documented | 0–1 |
| Limitations honestly declared | 0–1 |

Score ≥7 = high, 4–6 = moderate, <4 = low. A sensitivity analysis will
report whether excluding low-quality studies changes the synthesis
conclusions.

## 12. Empirical Audit Studies (pre-specified, not post-hoc)

- **Study A — Tokenizer fertility & cost audit:** ≥8 tokenizers ×
  12 South Asian languages (+English, Hindi as reference) on a
  perfectly parallel corpus (FLORES-200 devtest, pending gated-access
  resolution — see `audit/study_a_tokenizer_fertility/README.md` for
  interim pilot on Tatoeba Bengali-English data).
- **Study B — Benchmark provenance audit:** 25–30 multilingual
  benchmarks coded native/human-translated/machine-translated/synthetic.
- **Study C — Native-speaker error taxonomy:** ~200 LLM output samples
  across 4 LLMs × 5 tasks, annotated by 3 Bangla-speaking annotators
  against a 9-code error taxonomy (E1–E9), with Fleiss' κ reported and
  correlated against automatic metric scores.

## 13. Sensitivity Analyses (pre-specified)

- Exclude grey literature (technical reports, non-peer-reviewed
  preprints) and re-check whether taxonomy-layer coverage conclusions hold.
- Exclude low-quality studies (score <4) and re-check whether the
  headline findings (dialect coverage %, translated-benchmark %) hold.

## 14. Known Limitations Declared in Advance

- English-language-only search introduces language bias (declared,
  mitigated by a supplementary non-English-venue search pass).
- First author is a native Bangla speaker — positionality statement to
  be included in the manuscript (see `LRL-LLM-MASTER-PROTOTYPE.md` §A3).
- Fast-moving field: hard cutoff date declared; repository will be
  maintained as a "living review" on GitHub after publication.

## 15. Timeline (from registration)

- Search execution: within 2 weeks of OSF registration.
- Screening complete: within 7 weeks of registration.
- Full-text + extraction complete: within 12 weeks of registration.

## 16. Registration Metadata

- **OSF DOI:** [TODO — populate after submission to osf.io/registries]
- **Registration date:** [TODO]
- **Amendments:** any protocol deviation after registration will be
  logged here with a date and justification, not silently applied.

---

### Next steps to finalize

1. Fill every `[TODO]`.
2. Resolve FLORES-200 access (HuggingFace token + license acceptance)
   so Study A's design section above stops depending on a pilot substitute.
3. Copy this content into the OSF Preregistration web form at
   osf.io/registries and submit.
4. Paste the resulting DOI back into §16 and into the paper's
   Methodology section (`LRL-LLM-MASTER-PROTOTYPE.md` → C1).
