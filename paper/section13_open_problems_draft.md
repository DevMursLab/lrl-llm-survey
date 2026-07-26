# Section 13 - Discussion: Nine Open Problems (Draft)

> Word target: ~1,500. Each problem follows a fixed template
> (statement / why it is hard / concrete first step / success metric)
> so that none reads as a vague call for "more research." Problems are
> tagged with the taxonomy layer(s) they belong to (§5). Several are
> grounded in this paper's own audit findings rather than only in prior
> literature — those are marked ⭐. `[TODO]` marks anything that needs
> a number from the completed systematic review before this section is
> submission-ready.

---

**OP-1: Script-Faithful Tokenization** *(L1, L3)*

- *Problem:* Subword tokenizers designed for high-resource Latin-script
  languages are typically extended to Brahmic and Perso-Arabic scripts
  by adding script-specific vocabulary post hoc, rather than by
  co-designing the tokenizer with the target script's structure
  (conjunct consonants, vowel diacritics, joiners). ⭐ Our Study A
  pilot shows this matters concretely: a Bengali-specific tokenizer
  (BanglaBERT) achieves a 0.78x token premium relative to English
  (Bengali is *cheaper* to tokenize), while general multilingual
  tokenizers range from 1.05x to 1.67x on the same text — the
  difference is a vocabulary-design choice, not an inherent property
  of the script.
- *Why it is hard:* Retraining a tokenizer for a widely deployed
  commercial LLM requires retraining or substantially fine-tuning the
  model itself, an enormous cost that vendors are not incentivized to
  bear for languages outside their primary markets.
- *Concrete first step:* A published, reproducible benchmark
  (extending Study A to the full 12-language, ≥8-tokenizer design)
  that ties fertility directly to a per-provider USD cost premium,
  making the cost of the status quo legible to decision-makers who do
  not read tokenization papers.
- *Success metric:* At least one commercial or open tokenizer release
  citing a South-Asian-language fertility benchmark (such as the one
  this paper releases) as part of its vocabulary-design justification.

**OP-2: Corpus Quality Certification Pipeline** *(L2)*

- *Problem:* Web-crawled multilingual corpora (mC4, OSCAR, CulturaX)
  are known to contain substantial language-identification noise for
  lower-resource languages (Kreutzer et al., 2022), but no standard,
  adopted certification process exists for South Asian language
  subsets specifically.
- *Why it is hard:* Manual audit does not scale to corpus sizes in the
  billions of tokens, and automated language-ID tools are themselves
  less reliable for the languages most in need of auditing.
- *Concrete first step:* A stratified-sample human audit protocol
  (audit N sentences per 1M-token shard, report noise rate with
  confidence interval) applied to at least one major crawl corpus for
  each of this review's twelve languages/varieties.
- *Success metric:* A published noise-rate estimate with reported
  confidence interval for each of the twelve languages, comparable
  across corpora.

**OP-3: Dialect-Faithful Generation** *(L4, L5)*

- *Problem:* Current LLMs, when instructed to generate in a named
  dialect (e.g., "write in Sylheti"), frequently revert to Standard
  Bangla. [TODO: replace with the exact percentage once Study C's full
  200-sample run is complete; our 10-sample pilot is too small to
  report a reliable rate here.]
- *Why it is hard:* Sylheti lacks a single standardized orthography in
  contemporary use (§2.3), there is no substantial parallel
  Sylheti-Standard Bangla training corpus, and no dialect-identification
  classifier exists to even measure the failure rate at scale.
- *Concrete first step:* A community-elicited parallel seed corpus
  (target: 5,000 sentence pairs) paired with a dialect-ID classifier
  trained to detect Standard-Bangla fallback.
- *Success metric:* Native-speaker-rated dialect authenticity ≥4/5 on
  a 5-point scale, and dialect-ID classifier accuracy ≥0.85.

**OP-4: Native-Authored Benchmarks at Scale** *(L5)*

- *Problem:* ⭐ Our Study B catalog finds 69.2% of 26 verified
  South-Asian-language NLP benchmarks are not purely native-authored —
  they are human-translated, machine-translated, or inherit provenance
  from an upstream translated benchmark — meaning a majority of
  reported "Bangla" or "Urdu" evaluation scores in the literature may
  partly measure translation artifacts rather than native language
  competence.
- *Why it is hard:* Native benchmark construction requires
  domain-expert item writers per language, is far more expensive than
  machine-translating an existing English benchmark, and produces
  benchmarks that are not directly score-comparable across languages
  (a feature some evaluation designs treat as a bug).
- *Concrete first step:* Extend Study B from a provenance catalog into
  a funding/effort case: quantify the per-item cost difference between
  native construction and machine-translation-based construction for
  one benchmark family, to make the tradeoff legible to funders.
- *Success metric:* At least one new, fully native-authored benchmark
  released for a language currently covered only by translated
  resources in our Study B catalog (e.g., a language marked
  machine-translated-only).

**OP-5: Metric Validity for Indic Scripts** *(L5)*

- *Problem:* ⭐ Automatic metrics (BLEU, chrF, COMET) and LLM-as-judge
  protocols are validated primarily on high-resource languages; whether
  they detect the specific error types native Bangla speakers notice
  (conjunct malformation, register collapse, honorific inconsistency,
  dialect flattening — our Study C taxonomy) is untested at scale.
  [TODO: report the actual Spearman correlation between metric scores
  and native-annotated error counts once Study C's full run and
  parallel automatic-metric scoring are complete; do not state a
  correlation value from the 10-sample pilot.]
- *Why it is hard:* Establishing metric validity requires exactly the
  kind of native-speaker-annotated ground truth that is expensive to
  produce and that this literature has historically lacked — the same
  scarcity that makes the problem worth stating.
- *Concrete first step:* Complete Study C's full design (200 samples,
  4 models, 3 annotators) and correlate per-output error counts against
  BLEU/chrF/COMET/LLM-judge scores for the same outputs.
- *Success metric:* A published correlation coefficient (with
  confidence interval) between each metric and native-annotated error
  count, for at least one South Asian language.

**OP-6: Contamination Detection in Low-Resource Settings** *(L5)*

- *Problem:* Data contamination detection methods (membership
  inference, n-gram overlap checks) are developed and validated
  primarily on English benchmarks; whether they function reliably for
  South Asian language benchmarks, which are smaller and more likely to
  circulate informally before formal publication, is largely
  unexamined in the literature we screen for this review. [TODO:
  report actual finding once full-text screening/extraction is done —
  this may turn out to be a genuinely empty cell in the taxonomy grid.]
- *Why it is hard:* Contamination detection requires access to training
  data manifests that most commercial model providers do not disclose,
  compounding an already-hard problem with an opacity problem specific
  to lower-resource languages.
- *Concrete first step:* Apply an existing contamination-detection
  method (e.g., n-gram overlap against a known pretraining corpus
  sample) to at least one South Asian language benchmark and report
  whether it flags plausible contamination.
- *Success metric:* A published contamination-risk estimate for at
  least one benchmark per language family in this review's scope.

**OP-7: Equitable Inference-Cost Framework** *(L6)*

- *Problem:* ⭐ Token premium (Study A) compounds directly into
  inference-time cost: on the tokenizer behind a widely used commercial
  LLM, our pilot finds Bengali speakers pay a 1.67x token-cost premium
  and lose approximately 40% of usable context window relative to
  English speakers for equivalent content — a cost structure invisible
  in per-request pricing that is uniform in currency but not in
  linguistic value delivered.
- *Why it is hard:* Correcting this requires either tokenizer redesign
  (OP-1, a model-level change) or a pricing policy change (a business
  decision), neither of which is within a researcher's direct control.
- *Concrete first step:* Publish the full 12-language cost-premium
  table (once FLORES-200 access is obtained, extending the current
  pilot) in a form directly usable by policy advocates and procurement
  decision-makers, not only by NLP researchers.
- *Success metric:* Citation of a token-premium-by-language table (this
  paper's or a successor's) in a non-academic policy, procurement, or
  journalistic context.

**OP-8: Safety Alignment Coverage Gap** *(L6)*

- *Problem:* Safety and guardrail behavior (refusal calibration, harmful
  content detection) in commercial LLMs is typically evaluated and
  tuned primarily in English; whether the same guardrails hold, over-
  trigger, or under-trigger for South Asian languages is addressed in
  only a small fraction of the literature we expect to find in this
  review. [TODO: report the actual fraction/count once extraction is
  complete.]
- *Why it is hard:* Safety evaluation requires adversarial test sets in
  each target language, which are expensive and sensitive to construct,
  and vendors have limited incentive to publish gaps in their own
  safety coverage.
- *Concrete first step:* A small-scale red-teaming pilot applying an
  existing English safety-evaluation prompt set, translated by native
  speakers (not machine-translated, to avoid the translationese problem
  this paper documents elsewhere), to at least one South Asian
  language.
- *Success metric:* A published refusal-rate or harmful-completion-rate
  comparison between English and at least one South Asian language on
  a matched prompt set.

**OP-9: Community Data Governance Model** *(L2, L6)*

- *Problem:* Data used to train and evaluate models for South Asian
  languages is frequently collected from community sources (social
  media, forums, crowdsourcing) without a clear governance framework
  analogous to the CARE Principles for Indigenous data governance,
  raising unresolved questions about consent, benefit-sharing, and
  control for the communities whose language data is used.
- *Why it is hard:* Existing NLP data-collection norms were developed
  primarily around high-resource languages where this tension is less
  visible; adapting a governance framework requires engagement outside
  standard NLP research practice (with community organizations, not
  only with data).
- *Concrete first step:* A case study applying the CARE Principles
  framework to one existing South Asian language corpus (e.g., an
  IndicCorp or similar community-sourced resource), documenting where
  its current practice does and does not meet CARE's criteria.
- *Success metric:* At least one South Asian language corpus release
  that explicitly documents its governance practice against a named
  framework (CARE or an adapted equivalent), rather than leaving data
  provenance and consent unaddressed.

---

## TODO before this draft is submission-ready

- [ ] Fill every bracketed `[TODO]` with a real number/finding once the systematic review and full Study C run are complete — do not estimate or invent these values.
- [ ] Verify the Masakhane/CARE Principles references cited implicitly in OP-9 against their actual publications before final citation.
- [ ] Confirm OP numbering/order matches the layer-synthesis sections (§6-11) once those are drafted, so open problems are introduced in a order consistent with where they were first raised.
- [ ] Re-read for banned words ("significantly", "dramatically", "clearly") — none currently present.
