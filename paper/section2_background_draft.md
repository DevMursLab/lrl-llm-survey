# Section 2 - Background & Scope (Draft)

> Word target: ~1,200. All factual claims below were checked via web
> search on 2026-07-27 (see `[TODO: cite]` markers for the specific
> primary source each still needs). Speaker-count figures are drawn
> from multiple secondary aggregations of Ethnologue and the 2011
> Indian Census and vary by source/year — flagged explicitly rather
> than presented as single precise numbers, since reviewers penalize
> false precision more than an honest range.

---

## 2.1 What "Low-Resource" Means Here

"Low-resource" is a contested term with no single agreed definition
(a point this section states rather than glosses over). We adopt Joshi
et al.'s (2020) six-class taxonomy — "The State and Fate of Linguistic
Diversity and Inclusion in the NLP World" (ACL 2020) — which grades
languages 0-5 by the joint availability of unlabeled data (e.g.,
Wikipedia scale) and labeled/task-specific resources: Class 0 ("The
Left-Behinds") denotes languages with almost no digital resources at
all, through Class 5 ("The Winners") denoting languages such as
English with abundant labeled and unlabeled data and mature tooling.
[TODO: confirm exact class names/descriptions directly from the ACL
PDF before quoting them verbatim in the final manuscript — this draft
relies on secondary summaries, not a direct primary-source read.] This
review's inclusion criteria (§4) target languages in classes 0-3.

Two caveats about this choice, stated up front rather than left for a
reviewer to find. First, the Joshi classes were assigned in 2020 and
some languages have since gained resources the classification does not
reflect (e.g., Bangla has seen substantial resource growth via
AI4Bharat and CSEBUETNLP efforts since 2020) — we treat the 2020
classification as a historical baseline, not a current status claim,
and note where our own findings suggest a language's effective status
has shifted. Second, "low-resource" is a property of the
NLP-infrastructure ecosystem around a language, not of the language or
its speakers — a framing we return to in the positionality statement
(§14).

## 2.2 LLM-Era Multilingual NLP: What Changed

A brief technical grounding, kept intentionally short since this is not
this paper's contribution: general-purpose LLMs since approximately
2022-2023 are typically pretrained on a multilingual corpus mixture,
then adapted via instruction tuning and/or RLHF, and are queried
zero-shot or few-shot rather than fine-tuned per task. This differs
from the pre-LLM low-resource NLP paradigm — surveyed by Hedderich et
al. (2021) and Magueresse et al. (2020) — where the default was a
task-specific model trained or fine-tuned on whatever labeled data
existed for a given language. The practical consequence for this
review: many of the pre-LLM literature's central concerns (data
augmentation strategies, task-specific architecture choices) are less
load-bearing today, while concerns that were secondary or absent from
that literature — tokenizer design, evaluation-benchmark provenance,
in-context learning behavior across languages, and the inference-time
economics of serving a language — have become primary. Section 5's
taxonomy is built around this shift.

## 2.3 The South Asian Language Landscape Covered by This Review

This review covers Bangla/Bengali and eleven related South Asian
languages and varieties, selected for a mix of speaker scale,
typological diversity, and resource-tier diversity (Joshi classes 0-3):

| Language/variety | Approx. speakers | Family | Primary script | Joshi class (2020 baseline) |
|---|---|---|---|---|
| Bangla (Bengali) | ~228M native / ~265-274M total [TODO: cite specific Ethnologue edition] | Indo-Aryan | Bengali-Assamese | [TODO: confirm from primary source] |
| Assamese | ~15M native (+~8M L2) | Indo-Aryan | Bengali-Assamese (Asomiya variant) | [TODO] |
| Odia | ~34-35M | Indo-Aryan | Odia | [TODO] |
| Nepali | ~19M native (+~14M L2) | Indo-Aryan | Devanagari | [TODO] |
| Sinhala | ~18-20M | Indo-Aryan | Sinhala | [TODO] |
| Urdu | ~78M native (contested totals up to ~230M incl. L2) | Indo-Aryan | Perso-Arabic | [TODO] |
| Sindhi | ~35-37M | Indo-Aryan | Perso-Arabic (also Devanagari in India) | [TODO] |
| Maithili | ~13.6M (2011 Indian Census) | Indo-Aryan | Devanagari (historically Tirhuta) | [TODO] |
| Bhojpuri | ~50.6M (2011 Indian Census) | Indo-Aryan | Devanagari | [TODO] |
| Santali | ~7.6M total | Austroasiatic (Munda) | Ol Chiki (invented 1925 by Pandit Raghunath Murmu; also written in Bengali/Devanagari/Latin) | [TODO] |
| Manipuri (Meitei) | ~1.8-2M | Tibeto-Burman | Meitei Mayek (also historically Bengali script) | [TODO] |
| Sylheti | ~10-13M | Indo-Aryan (variety of Bangla, contested language-vs-dialect status) | Bengali script today; historically Sylheti Nagri | [TODO] |

**On Sylheti and script history specifically:** Sylheti historically
had its own script, Sylheti Nagri, dating to roughly the 14th century
and used mainly for religious "puthi" literature; it declined through
the 20th century and is now endangered/near-extinct in everyday use,
with Sylheti today written predominantly in Bengali script when
written at all [TODO: cite Banglapedia/Wikipedia: Sylheti Nagri
directly rather than this secondary summary]. This history matters for
L1 of our taxonomy (§5): a model asked to render Sylheti faithfully
faces a script question with no single settled answer, which no
current tokenizer or benchmark to our knowledge addresses.

**Typological range:** the set spans three language families
(Indo-Aryan, Tibeto-Burman via Manipuri, Austroasiatic via Santali),
scripts derived from three distinct traditions (Brahmic-family scripts
for most Indo-Aryan languages, Perso-Arabic for Urdu/Sindhi, and Ol
Chiki as a script invented independently of any existing writing
system for Santali), and a resource-tier range from actively-developed
(Bangla, with dedicated efforts like AI4Bharat and CSEBUETNLP) to
near-absent in mainstream NLP tooling (Santali, Manipuri, Sylheti as a
distinct variety).

## 2.4 Scope Boundaries (What This Review Does Not Cover)

Stated explicitly to pre-empt the "coverage incomplete" rejection mode
(§F2 of the blueprint): this review does not systematically cover (i)
South Asian languages outside the twelve above (e.g., Punjabi, Tamil,
Telugu, and other Dravidian languages are referenced only where they
appear in a benchmark shared with an included language, not
independently reviewed); (ii) speech-only processing without a textual
component (excluded per EC2, §4); or (iii) non-English-medium
publications (a declared limitation, §14). These boundaries follow
directly from the inclusion/exclusion criteria formalized in the
pre-registered protocol (`protocol/osf_preregistration_draft.md`).

---

## TODO before this draft is submission-ready

- [ ] Every `[TODO: confirm from primary source]` Joshi-class assignment must be filled from the actual ACL 2020 paper appendix, not left blank or guessed.
- [ ] Pick one Ethnologue edition (with access date) and use it consistently for every speaker-count figure in the table above — do not mix vintages across rows.
- [ ] Confirm the Ol Chiki / Pandit Raghunath Murmu / 1925 date and the Sylheti Nagri history directly against Banglapedia or an academic source, not this secondary summary.
- [ ] Cross-check "AI4Bharat and CSEBUETNLP" as the correct named efforts for Bangla resource growth since 2020 — cite their specific papers/resources, not just the org names.
- [ ] Re-read for banned words ("significantly", "dramatically", "clearly") — none currently present.
