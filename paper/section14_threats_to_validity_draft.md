# Section 14 - Threats to Validity (Draft)

> Word target: ~700. Follows the blueprint's explicit framing (§F1):
> a survey that claims "no bias" reads as naive to a Q1 reviewer:
> the credible move is naming each bias and stating a concrete
> mitigation, not denying bias exists. The positionality statement in
> 14.9 is adapted from the blueprint (§A3) with the placeholder name
> still to be filled in.

---

## 14.1 Publication Bias

Negative or null results are underrepresented in published NLP
literature relative to positive results, which risks making adaptation
and evaluation methods appear more uniformly effective than they are.
*Mitigation:* grey literature and arXiv preprints were included
alongside peer-reviewed venues (§4.3); the extraction form includes a
dedicated field for reported limitations and failures (§4.7, field 21),
extracted and synthesized separately rather than discarded.

## 14.2 Language Bias

Restricting the search to English-language full text (§4.4) plausibly
excludes relevant work published in Bangla-, Hindi-, or Urdu-medium
venues, which this review cannot claim to have found. *Mitigation:*
this restriction is declared here rather than left implicit; [TODO: a
supplementary targeted search of at least one non-English-medium venue
or conference, if time permits, with its findings reported separately
from the main synthesis rather than silently merged into it].

## 14.3 Database Bias

The heaviest-represented database in NLP-specific systematic reviews is
typically the ACL Anthology, which risks under-sampling adjacent
engineering or applied-computing venues. *Mitigation:* six databases
were searched, not one (§4.3), and [TODO: a per-database contribution
table will be reported once search is complete, showing how many
included studies came from each source] so this bias is measurable
rather than assumed away.

## 14.4 Geographic and Institutional Bias

Papers from well-resourced institutions and large industry labs are
cited and indexed at disproportionately high rates relative to work
from institutions in the languages' countries of origin, which can
distort a synthesis toward those institutions' framings of the
problem. *Mitigation:* author affiliation country is an extraction
field (§4.7, field 4); [TODO: report the share of included studies with
at least one author affiliated with a South Asian institution once
extraction is complete] — this is treated as a finding in its own
right, not only a bias to control for.

## 14.5 Selection Bias in Screening

Any human screening process is subject to the screener's own judgment
of borderline cases. *Mitigation:* the protocol was pre-registered
before screening began (§4.1), at least 20% of records were
independently dual-screened with Cohen's kappa reported (§4.6), and
disagreements were arbitrated by a third party rather than resolved
unilaterally.

## 14.6 Temporal Bias

The LLM field changes fast enough that a systematic review risks being
outdated before or shortly after publication. *Mitigation:* a hard
search cutoff date is declared (§4.4) rather than left ambiguous, and
this paper's repository is intended to be maintained as a living
resource on GitHub after publication, with updates version-tracked
rather than silently overwriting the reviewed record.

## 14.7 Author (Positionality) Bias

Addressed at length in §14.9 below, given its importance to this
paper's specific claims.

## 14.8 Confirmation Bias

Approaching this review already believing South Asian languages are
underserved by LLMs risks selectively noticing evidence that confirms
this and discounting evidence that does not. *Mitigation:* the research
questions (§4.2) are stated in neutral, measurable terms rather than as
a foregone conclusion, and the extraction form includes no field that
presumes a negative finding — a study reporting strong LLM performance
for a South Asian language is extracted with the same fields and the
same rigor as one reporting a gap.

## 14.9 Positionality Statement

The first author, [TODO: full name], is a native Bangla speaker based
in Bangladesh. This positionality directly informs the linguistic error
taxonomy in Study C (§10) and enables a kind of validation — native
judgment of register collapse, honorific inconsistency, and dialect
flattening — that a non-native researcher could not straightforwardly
perform. It also introduces a plausible advocacy bias toward
emphasizing Bangla-specific gaps over those of the other eleven
languages and varieties in this review's scope. Three concrete steps
mitigate this: (i) all screening decisions are pre-registered and
dual-coded rather than made unilaterally post hoc (§4.6); (ii) the
empirical audit spans eleven additional languages beyond Bangla, not
Bangla alone (§4.10); and (iii) all annotation data, screening
decisions, and extraction sheets are released publicly
(`README.md`, "Repository Map") for independent re-analysis by
researchers without this positionality.

## 14.10 Annotator Bias in Study C

If Study C's native-speaker annotators share a single regional or
dialect background, they may under-detect dialect-flattening errors
(E9) for varieties they are not personally exposed to, or apply
inconsistent judgment on register-collapse (E3) items where regional
norms differ. *Mitigation:* annotator recruitment targets speakers from
different regions (§`audit/study_c_error_taxonomy/README.md`),
demographic metadata (region, dialect exposure, education) is recorded
for every annotator (`annotator_demographics_template.csv`), and
inter-rater agreement (Fleiss' kappa) is reported per error code, not
only pooled, so that low agreement on a specific code is visible rather
than averaged away.

---

## TODO before this draft is submission-ready

- [ ] Fill in the first author's name in §14.9.
- [ ] Complete the per-database contribution table (§14.3) and South-Asian-institution authorship share (§14.4) once extraction is done.
- [ ] Decide whether the supplementary non-English-medium search (§14.2) is feasible given time constraints; if not run, say so explicitly rather than leaving the TODO unresolved in the submitted version.
- [ ] Re-read for banned words ("significantly", "dramatically", "clearly") — none currently present.
