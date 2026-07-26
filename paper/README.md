# Manuscript Sections - Status Index

This directory holds section-by-section drafts of the manuscript
described in `LRL-LLM-MASTER-PROTOTYPE.md`. Each file is self-contained
with its own word-count target and a `TODO before this draft is
submission-ready` list at the bottom - read that list before treating
any section as final.

Citations used across all drafted sections are consolidated in
[`references.bib`](references.bib) (29 entries, syntax-validated) -
treat it as a checklist to re-verify against primary sources, not a
final bibliography.

## Status at a glance

| § | Section | File | Status | Blocked on |
|---|---|---|---|---|
| 1 | Introduction | [section1_introduction_draft.md](section1_introduction_draft.md) | Draft complete | Real PRISMA screening numbers (`[N]`, `[n]`, κ) |
| 2 | Background & Scope | [section2_background_draft.md](section2_background_draft.md) | Draft complete | Primary-source verification of Joshi-class assignments and one consistent Ethnologue edition |
| 3 | Related Surveys & Δ-table | `LRL-LLM-MASTER-PROTOTYPE.md` → B5 / B5b | Draft complete | Nothing - ready to move into a section file when the manuscript is assembled |
| 4 | Review Methodology | [section4_methodology_draft.md](section4_methodology_draft.md) | Draft complete | OSF DOI, actual search/screening/extraction execution |
| 5 | LRL-LLM Lifecycle Taxonomy | [section5_taxonomy_draft.md](section5_taxonomy_draft.md) | Draft complete | Figure 4 (gap heatmap) needs full extraction data |
| 6-11 | Layer-by-layer synthesis (L1-L6) | *(not started)* | **Blocked** | Cannot be written without actual included studies from PRISMA screening - writing this now would mean fabricating findings |
| 12 | Bibliometric Analysis | *(not started)* | **Blocked** | Same as above - needs the extraction sheet |
| 13 | Discussion: 9 Open Problems | [section13_open_problems_draft.md](section13_open_problems_draft.md) | Draft complete | A few problem statements cite pilot-only numbers flagged `[TODO]` pending the full Study C run |
| 14 | Threats to Validity | [section14_threats_to_validity_draft.md](section14_threats_to_validity_draft.md) | Draft complete | Author name, per-database contribution table, South-Asian-authorship share |
| 15 | Conclusion | *(not started)* | **Blocked** | Must synthesize findings from §§6-12, which don't exist yet |

## Why sections 6-12 and 15 are intentionally not drafted yet

Sections 1, 2, 4, 5, 13, and 14 could be written now because they
depend on the *design* of the review (taxonomy, protocol, research
questions) or on this project's own completed pilot audits (Studies
A/B/C), not on the outcome of literature screening. Sections 6-12 and
15 report what the *included studies actually say* - writing them
before real screening and extraction exist would mean inventing
findings and attributing them to a literature base that hasn't been
reviewed. That is the single fastest way to get a systematic review
desk-rejected, and it will not be done here even as a placeholder.

## What has to happen before 6-12 and 15 can be written

1. Execute the search across all six databases (`protocol/osf_preregistration_draft.md` §5-6).
2. Screen title/abstract and full-text against IC/EC, with dual-screening and Cohen's kappa (§4.6).
3. Complete the 22-field extraction sheet for every included study (§4.7).
4. *Then* §§6-11 synthesize per taxonomy layer, §12 reports bibliometric patterns over the extraction sheet, and §15 concludes from all of the above.

## Reading order for a reviewer of this repository

If you want to sanity-check the paper's design before the literature
review is run, read in this order: `section1_introduction_draft.md` →
`section2_background_draft.md` → `LRL-LLM-MASTER-PROTOTYPE.md` (§B5/B5b
for related-work positioning) → `section4_methodology_draft.md` →
`section5_taxonomy_draft.md` → `section13_open_problems_draft.md` →
`section14_threats_to_validity_draft.md`.
