# Section 4 - Review Methodology (Draft)

> Word target: ~1,800. This section converts the OSF preregistration
> protocol (`protocol/osf_preregistration_draft.md`) into flowing
> manuscript prose. Every `[TODO]` here mirrors an unresolved item in
> that protocol — **do not fill these with invented numbers**; they
> can only be completed once the actual search, screening, and
> extraction have been run.

---

## 4.1 Protocol and Pre-Registration

This review follows the PRISMA 2020 statement (Page et al., 2021) for
reporting systematic reviews. The review protocol — research questions,
search strategy, inclusion/exclusion criteria, and the pre-specified
empirical audit design — was registered on the Open Science Framework
prior to database searching (DOI: [TODO: populate after OSF submission
— see `protocol/osf_preregistration_draft.md`]). Registering before
search execution, rather than after, is what allows this section to
state that no inclusion or exclusion decision was made with knowledge
of which studies it would include or exclude.

## 4.2 Research Questions

Three research questions guided the search and synthesis, stated here
exactly as pre-registered:

- **RQ1:** How has research on LLM-era NLP for South Asian low-resource
  languages evolved (2019-2026) in terms of task coverage, model
  families, adaptation methods, and evaluation practice?
- **RQ2:** Where in the LLM pipeline (script/encoding, data,
  tokenization, adaptation, evaluation, or deployment) do the largest
  unaddressed gaps concentrate, and how does this differ across
  language typology and resource tier?
- **RQ3:** What is the measurable magnitude of tokenization cost
  asymmetry, benchmark translation-provenance bias, and
  native-speaker-perceptible error patterns for Bangla and related
  languages under current LLMs, and do standard automatic metrics
  detect these errors?

RQ1 and RQ2 are addressed by the systematic review (§§6-12); RQ3 is
addressed by the three-study empirical audit (Studies A-C, integrated
into §8 and §10).

## 4.3 Information Sources

Six databases were searched: ACL Anthology, arXiv (cs.CL), OpenAlex,
Semantic Scholar, IEEE Xplore, and the ACM Digital Library, supplemented
by backward and forward snowballing via Semantic Scholar's citation
graph. [TODO: if institutional Scopus/Web of Science access was
unavailable at search time, state here: "Scopus and Web of Science were
queried via OpenAlex (v3 API) owing to institutional access
constraints; OpenAlex indexes over 250 million works and shows high
overlap with Scopus for NLP venues." Otherwise remove this sentence and
report direct Scopus/WoS search instead.] Grey literature — technical
reports accompanying widely used resources such as NLLB, Aya, and
IndicTrans2 — was included but flagged separately in extraction, with a
sensitivity analysis (§4.9) reporting whether excluding it changes the
synthesis.

## 4.4 Search Strategy

The search combined three concept blocks (low-resource-language terms
AND LLM/multilingual-model terms AND named South Asian
languages/regional terms), restricted to records dated 2019-01-01
through [TODO: search execution date], justified by the transformer-era
pretraining paradigm shift that followed BERT. The full search string,
adapted per database syntax, is reported in Table [TODO: table number]
and archived at `protocol/osf_preregistration_draft.md` §6. Only
English-language full text was searched — a decision declared as a
limitation (§14) rather than presented as unproblematic, since it
plausibly excludes relevant work published in Bangla-, Hindi-, or
Urdu-medium venues.

## 4.5 Eligibility Criteria

Inclusion required (IC1) at least one low-resource language in Joshi et
al.'s (2020) classes 0-3, (IC2) involvement of an LLM or large
pretrained multilingual model, (IC3) peer-reviewed publication or an
arXiv preprint with at least 10 citations, (IC4) English-language full
text, and (IC5) publication between 2019 and 2026. Exclusion removed
(EC1) high-resource-only studies, (EC2) speech-only work without a
textual component, (EC3) short-form publications under four pages,
(EC4) duplicate preprints where a published version existed, and (EC5)
non-NLP applications where language was incidental. The full criteria
table appears as Table [TODO] and is reproduced verbatim from the
pre-registered protocol without post-hoc modification.

## 4.6 Screening Process and Inter-Rater Reliability

Records retrieved across all sources were deduplicated by DOI and by
normalized title-year matching. Title-and-abstract screening against
the criteria above was conducted by the first author; at least 20% of
records were independently double-screened by a second reviewer
[TODO: name/role of co-screener] to compute inter-rater reliability.
Cohen's kappa on this dual-screened sample was κ = [TODO: value once
screening is complete] ([TODO: interpretation band — substantial
agreement is κ ≥ 0.75 per Landis & Koch, 1977]). Disagreements were
resolved by discussion, with unresolved cases referred to a third-party
arbitrator [TODO: name]. Full-text eligibility assessment then
re-applied the same criteria to the surviving records, with exclusion
reasons logged per criterion code to populate the PRISMA flow diagram
(Figure 2, [TODO: build once real counts exist — template and expected
structure are in `LRL-LLM-MASTER-PROTOTYPE.md` → C5]).

## 4.7 Data Extraction

A 22-field extraction form was applied to every included study,
covering bibliographic metadata, languages and scripts studied, Joshi
resource class, task type, the taxonomy layer (§5) each study maps to,
model family and size, adaptation method, data source and scale,
evaluation benchmark and its provenance code (native/human-translated/
machine-translated/synthetic — the same coding scheme used
independently in Study B, §10), metrics reported, human evaluation
presence, code/data release status, whether dialectal variation was
addressed, reported limitations, and a quality score (§4.8). The full
field-by-field codebook is maintained at
`protocol/extraction_form_codebook.md` [TODO: create alongside the
first extraction pass] and the completed sheet will be released at
`extraction/extraction_sheet.csv`.

## 4.8 Quality Appraisal

Because established appraisal instruments for clinical systematic
reviews (e.g., AMSTAR, CASP) do not transfer cleanly to NLP research
practice, we constructed a 10-point rubric specific to this literature:
reproducibility (code/data/seeds public, 0-2 points), baseline strength
(≥2 competitive baselines, 0-2), statistical rigor (multi-seed
reporting, confidence intervals, or significance testing, 0-2),
evaluation validity (use of native rather than machine-translated
benchmarks, 0-2), documented native-speaker involvement (0-1), and
honest declaration of limitations (0-1). Studies scoring ≥7 are
classified high quality, 4-6 moderate, and below 4 low; §4.9 reports
whether excluding low-quality studies changes the synthesis.

## 4.9 Pre-Specified Sensitivity Analyses

Two sensitivity analyses were specified before screening began, to
avoid the appearance of post-hoc rationalization of any surprising
result: (i) excluding grey literature and re-checking whether
taxonomy-layer coverage conclusions hold, and (ii) excluding
low-quality studies (score <4) and re-checking whether headline
findings — dialect coverage percentage, translated-benchmark
percentage — hold. Results are reported in §12 alongside the
unrestricted synthesis.

## 4.10 The Empirical Audit (Studies A-C)

Distinct from the literature synthesis above, three original empirical
studies were pre-specified in the same registered protocol to generate
reproducible evidence rather than rely solely on synthesized claims
from prior work:

- **Study A** measures tokenizer fertility and cost premium across
  multiple tokenizers and South Asian languages on a parallel corpus.
  A pilot using an ungated substitute corpus (Tatoeba, Bengali-English,
  n=2,499 sentence pairs) found a token premium ranging from 0.78x
  (Bengali-specific tokenizer) to 1.67x (a widely used commercial
  tokenizer) relative to English; the full 12-language design requires
  FLORES-200, which is access-gated on HuggingFace (see
  `audit/study_a_tokenizer_fertility/README.md` for exact pending steps).
- **Study B** catalogs the provenance (native-authored,
  human-translated, machine-translated, or mixed/inherited) of
  South-Asian-language NLP benchmarks. Twenty-six benchmarks were
  verified against primary sources (original papers, dataset cards,
  repositories); 69.2% were found not to be purely native-authored
  (`audit/study_b_benchmark_provenance/`).
- **Study C** applies a nine-code native-speaker error taxonomy
  (conjunct-consonant malformation, ZWJ/ZWNJ misuse, register collapse,
  honorific inconsistency, calque, lexical anglicization, numeral/date
  localization failure, cultural/factual error, and dialect flattening)
  to LLM-generated Bangla text, with agreement measured via Fleiss'
  kappa. A pilot taxonomy, annotation protocol, and 10 single-model
  sample outputs are released; the full ~200-sample, 4-model,
  3-annotator study remains to be run
  (`audit/study_c_error_taxonomy/README.md`).

All three studies' code, data, and — where applicable — annotation
guidelines are released in this paper's public repository, so that
every quantitative claim attributed to the audit can be independently
regenerated rather than taken on faith.

---

## TODO before this draft is submission-ready

- [ ] Populate the OSF DOI once registered.
- [ ] Fill every `[TODO]` above only with real values once search, screening, and extraction are actually complete — this section must not ship with invented kappa or record counts.
- [ ] Build the PRISMA flow diagram (Figure 2) using the official PRISMA 2020 template once real counts exist.
- [ ] Create `protocol/extraction_form_codebook.md` before or during the first extraction pass.
- [ ] Confirm final table/figure numbering once the full manuscript skeleton is assembled.
- [ ] Re-read for banned words ("significantly", "dramatically", "clearly") — none currently present.
