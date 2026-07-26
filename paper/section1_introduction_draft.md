# Section 1 - Introduction (Draft)

> Word target: ~1,200. This draft follows the 5-paragraph formula in
> `LRL-LLM-MASTER-PROTOTYPE.md` → B4. Bracketed `[TODO]` items require
> screening/extraction numbers that don't exist yet (PRISMA hasn't run).
> Everything else — the Study A/B pilot numbers — is real data already
> in this repository, not placeholder.

---

Large language models (LLMs) have transformed natural language
processing at a pace with few historical precedents, yet this
transformation has not reached most of the world's languages evenly.
Of the world's more than 7,000 languages, effective LLM support
concentrates on a few dozen; Bangla — among the sixth-to-seventh
most-spoken languages globally, with approximately 230-270 million
speakers depending on source and count method [TODO: cite one
Ethnologue edition] — remains persistently underrepresented in
benchmark suites, training-data allocation, and tokenizer design,
despite being spoken by more people than French, Italian, or Korean
combined. This paper asks a narrow but consequential
question: in the specific era of instruction-tuned, general-purpose
LLMs, exactly where and how much does this underrepresentation cost
Bangla and neighboring South Asian low-resource languages, and can that
cost be measured rather than asserted?

The pre-LLM literature on low-resource NLP (Magueresse et al., 2020;
Hedderich et al., 2021) framed the central problem as one of absence:
no model, no annotated data, no benchmark. That framing has not aged
well. Today, general-purpose LLMs "support" Bangla in the narrow sense
that they can process and generate Bangla text at all — the bottleneck
has moved downstream, into the pipeline stages that determine whether
that support is fair, faithful, and measurable. Our own pilot audit
illustrates the shift concretely: encoding a parallel English-Bangla
sentence set with the tokenizer behind a widely deployed commercial
LLM (GPT-4/o200k) costs Bangla speakers a 1.67x token premium over
English for saying the same thing, which under a fixed context window
translates into roughly 40% less usable context per query — an
asymmetry invisible to a monolingual English user and largely absent
from "the model works in Bangla" claims common in release
announcements. This is not a training-data problem in the traditional
sense; it is a tokenization-and-evaluation-pipeline problem that the
2020-2021 survey generation was not positioned to see, because it
predates the paradigm that created it.

Three specific gaps follow from this paradigm shift, none of which is
closed by the survey literature published since 2023. First, no
existing survey of South Asian LLM-era NLP is built on a registered,
dual-screened systematic review protocol with reported inter-rater
reliability — the two closest recent works, Gupta (2025) and Poria
& Huang (2025), rely respectively on unvalidated LLM-assisted
classification and narrative/curatorial synthesis, neither reporting
a pre-registered protocol or screening agreement statistic. Second, no
existing survey organizes the field around a pipeline-stage taxonomy
that separates script/encoding, data curation, tokenization,
adaptation, evaluation, and deployment as distinct loci of measurable
harm; general LLM-era multilingual surveys (Qin et al., 2024; Huang et
al., 2024) instead organize around methods at global scale, with South
Asian languages appearing as rows in aggregate tables rather than a
sustained unit of analysis. Third, and most consequentially, no
existing survey pairs its literature synthesis with original,
reproducible measurement. Our companion audit begins to close this:
alongside the tokenization premium above, a provenance catalog of 26
South-Asian-language NLP benchmarks finds that 69.2% are not purely
native-authored — they are human-translated, machine-translated, or
inherit provenance from an upstream translated benchmark — meaning a
majority of "Bangla" or "Urdu" evaluation scores reported in the
literature may partly reflect translation artifacts rather than native
language competence, a claim no prior survey in this space has
measured directly.

This paper makes four contributions. First, a systematic literature
review following the PRISMA 2020 protocol, pre-registered prior to
database searching, covering [N] records across six databases and
including [n] studies after dual screening (inter-rater κ = [x.xx]).
Second, an original six-layer LRL-LLM Lifecycle taxonomy — spanning
script and encoding substrate, data acquisition and curation,
tokenization and representation, adaptation and transfer, evaluation
and measurement, and deployment/equity/governance — that organizes the
included literature around pipeline-stage bottlenecks rather than a
flat topic list, with every included study mapped to one or more
layers. Third, a reproducible three-study empirical audit: tokenizer
fertility and cost-premium measurement across multiple tokenizers and
South Asian languages on a parallel corpus (Study A, pilot results
above), a provenance audit of South Asian NLP benchmarks (Study B, 26
benchmarks catalogued, 69.2% not purely native-authored), and a
native-speaker-annotated taxonomy of nine LLM output error types not
reliably captured by automatic metrics (Study C, pipeline and pilot
released). Fourth, a research agenda of nine concrete, falsifiable open
problems, each specifying a first step and a measurable success
criterion, rather than a general call for "more research." All
screening decisions, extraction data, audit code, and annotation
guidelines are released publicly to make every claim in this paper
independently checkable.

The remainder of this paper proceeds as follows. Section 2 establishes
background on LLM-era multilingual NLP, the contested definition of
"low-resource," and the South Asian language landscape this review
covers. Section 3 positions this work against existing surveys,
including the two closest 2025 contemporaries, via a structured
comparison table. Section 4 details the systematic review methodology.
Section 5 introduces the six-layer taxonomy. Sections 6-11 synthesize
the literature layer by layer, integrating the empirical audit results
where relevant. Section 12 reports bibliometric patterns across the
included corpus. Section 13 sets out the nine open problems. Section
14 discusses threats to validity, including a positionality statement
on the first author's native-speaker perspective. Section 15
concludes.

---

## TODO before this draft is submission-ready

- [ ] Replace `[N]`, `[n]`, `κ = [x.xx]` with real PRISMA screening numbers once search + dual screening is complete.
- [x] Verified via web search (2026-07-27): "270 million, 6th most spoken" was imprecise. Ethnologue-based sources give ~228M native / ~265-274M total speakers, ranking 6th-7th depending on edition/count method — text above already hedged accordingly. Remaining TODO: pick and cite one specific Ethnologue edition rather than the hedge, before final submission.
- [ ] Confirm Study A's 1.67x figure is still described as a **pilot** (Bengali-English via Tatoeba) here, not the full 12-language FLORES-200 result, until that expansion happens — see `audit/study_a_tokenizer_fertility/README.md`.
- [ ] Add citations for Qin et al. 2024, Huang et al. 2024, Gupta 2025, Poria & Huang 2025 (arXiv IDs are in `LRL-LLM-MASTER-PROTOTYPE.md` → B5) once the references.bib file exists.
- [ ] Re-read for the banned words: "significantly", "dramatically", "clearly" — none currently appear in this draft, keep it that way through revision.
