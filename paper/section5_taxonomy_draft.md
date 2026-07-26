# Section 5 - The LRL-LLM Lifecycle Taxonomy (Draft)

> Word target: ~1,200. Pairs with `figures/figure1_taxonomy.{pdf,svg,png}`
> (Figure 1) and, later, the Section 5 gap heatmap (Figure 4, §B6 in the
> blueprint — not yet built). This section defines the taxonomy that
> every included study will be mapped to during extraction (field #9 in
> the 22-field codebook, `protocol/osf_preregistration_draft.md` §10).

---

## 5.1 Motivation for a Pipeline-Stage Taxonomy

Existing surveys of low-resource NLP typically organize their synthesis
around *methods*: data augmentation, transfer learning, few-shot
prompting, and so on (Magueresse et al., 2020; Hedderich et al., 2021).
This organization made sense when the central obstacle was the absence
of any usable model for a given language — the question was "which
method gets us from nothing to something." In the LLM era, a
general-purpose model that can process Bangla, Urdu, or Sinhala already
exists; the question this paper asks is not whether a method exists,
but *where in the pipeline that a language's treatment diverges from
equitable*, and by how much. A method-centric taxonomy cannot express
this, because the same method (e.g., continued pretraining) can be
applied well or poorly depending on decisions made upstream (tokenizer
vocabulary allocation) or downstream (whether the evaluation benchmark
used to validate it is itself native-authored). We therefore organize
this review around six pipeline stages, each a distinct and separately
measurable locus of potential harm.

## 5.2 The Six Layers

**L1 - Script & Encoding Substrate.** The lowest layer: how a language's
writing system is represented in Unicode and processed before any model
sees it. This includes Unicode normalization form (NFC vs. NFD)
consistency, correct handling of conjunct consonants in Brahmic
scripts, zero-width joiner/non-joiner (ZWJ/ZWNJ) behavior, script
variants (e.g., Sylheti Nagri as a historical script distinct from
Bengali script), OCR quality for digitized text, and romanized
informal writing ("Banglish"). Errors introduced here are invisible to
any downstream evaluation that does not specifically check for them,
which is why L1 is frequently absent from evaluation entirely.

**L2 - Data Acquisition & Curation.** How pretraining and fine-tuning
data for a language is sourced: web-crawl quality (mC4, OSCAR,
CulturaX and similar corpora, each with reported noise and
language-identification error rates), deduplication practice, use of
synthetic/LLM-generated data as a substitute for scarce natural text,
community-sourced data collection, and the licensing and data
sovereignty questions this raises for community-held linguistic
resources.

**L3 - Tokenization & Representation.** How text is segmented into the
units a model actually computes over: fertility (tokens per word),
token premium relative to a reference language, vocabulary allocation
across scripts, the choice of subword algorithm (BPE, Unigram,
byte-level), and vocabulary-expansion strategies for adapting an
existing tokenizer to a new script. This is the layer our Study A
pilot directly measures (§8): a 1.67x token premium for Bengali on a
widely used commercial tokenizer, varying from a 0.78x premium
(cheaper than English) on a Bengali-specific tokenizer to a 1.51x
premium on a general multilingual one — evidence that the premium is a
vocabulary-design choice, not an inherent property of the script.

**L4 - Adaptation & Transfer.** How a pretrained multilingual base
model is specialized toward a target language: continued pretraining,
cross-lingual transfer, parameter-efficient fine-tuning (LoRA and
variants), instruction tuning, multilingual RLHF/DPO alignment, model
merging, and distillation. This is typically the largest literature
body by volume (§9) because it is the layer most directly amenable to
incremental, publishable experimentation.

**L5 - Evaluation & Measurement.** How claims of model competence in a
language are validated: whether benchmarks are native-authored,
human-translated, machine-translated, or synthetic; translationese
artifacts introduced by the latter two; data contamination risk;
whether LLM-as-judge protocols validated on English transfer to
low-resource languages; and whether standard automatic metrics
(BLEU, chrF, COMET) correlate with native-speaker judgments at all.
This is the layer our Study B and Study C results populate (§10):
69.2% of the 26 benchmarks we catalogued are not purely
native-authored, and our Study C pilot begins testing whether
automatic metrics detect the specific error types native speakers do.

**L6 - Deployment, Equity & Governance.** The layer where the previous
five compound into real-world consequence: inference cost asymmetry
(a direct downstream effect of L3's token premium), latency, gaps in
safety/guardrail coverage for lower-resource languages, the labor
conditions of annotators who produce the data in L2 and L5, erasure of
dialectal variation in favor of a standardized register, and the
policy and community-ownership questions this raises.

## 5.3 Cross-Cutting Dimensions

Each layer is further read through three lenses that do not define new
categories but stratify the analysis within each layer:

- **D1 - Language typology:** Indo-Aryan (Bengali, Assamese, Nepali,
  Sindhi, Urdu, ...) vs. Tibeto-Burman (Manipuri/Meitei) vs.
  Austroasiatic (Santali) vs. Dravidian-adjacent comparators, since
  script and morphological structure interact differently with each
  layer (e.g., L1's conjunct-handling burden differs by script family).
- **D2 - Resource tier:** Joshi et al. (2020) class 0-1 (the most
  under-resourced) vs. class 2-3, since the same layer can be
  well-addressed at one tier and essentially unaddressed at another.
- **D3 - Writing-system modality:** standardized script (Bengali) vs.
  non-standardized/contested orthography (Sylheti, spoken primarily in
  Bengali script by convention but lacking a single standardized
  writing system) vs. romanized-only informal use.

Crossing six layers by three dimensions yields an 18-cell grid; cells
with zero or near-zero included studies are the review's most direct
visual evidence of an unaddressed gap (planned as Figure 4, a heatmap
over the full extraction dataset - not yet built, pending completion
of full-text extraction).

## 5.4 How This Taxonomy Is Used in Synthesis

Every study surviving full-text screening is mapped to one or more of
L1-L6 during extraction (field #9 of the 22-field codebook). Sections
6-11 synthesize the included literature layer by layer; each layer
section closes with a "Settled / Contested / Unknown" takeaway box
(template in the blueprint, §B7) that makes explicit what the included
literature has resolved, where it disagrees, and what remains
unmeasured — the last category feeding directly into the nine open
problems of Section 13.

---

## TODO before this draft is submission-ready

- [ ] Build Figure 4 (6x3 gap heatmap) once full-text extraction is complete — cannot be built on pilot data alone.
- [ ] Confirm the Joshi et al. (2020) class assignments cited in D2 against the original paper's appendix, not from memory.
- [ ] Cross-check the "Sylheti Nagri as a historical script" claim in L1 against a citable source before submission.
- [ ] Insert `\ref{fig:taxonomy}` pointing at `figures/figure1_taxonomy.pdf` once the LaTeX manuscript skeleton exists.
