# Next Steps - What Only You Can Do From Here

Everything that could be built without real-world action (design,
protocol, pilot code, drafts) is done and pushed to
[github.com/DevMursLab/lrl-llm-survey](https://github.com/DevMursLab/lrl-llm-survey).
What remains requires accounts, human judgment, or people other than
an AI assistant. This file orders them by dependency so you know what
to do first.

## 1. Register the OSF protocol (do this first - ~1 hour)

The draft is ready at `protocol/osf_preregistration_draft.md`. To finish:

1. Fill in the `[TODO]` fields (your name, affiliation, co-screener name, arbitrator name).
2. Go to https://osf.io/registries -> New Registration -> "OSF Preregistration" template.
3. Copy the filled content in.
4. Submit and record the resulting DOI back into that file and into `paper/section4_methodology_draft.md`.

Nothing else should start before this, because the whole point of
pre-registration is that it happens *before* database searching.

## 2. Get a HuggingFace token (do this in parallel - ~5 minutes)

FLORES-200 (needed for Study A's real 12-language audit) is gated.

1. Go to https://huggingface.co/settings/tokens -> create a Read-access token.
2. Request access to `facebook/flores` (usually auto-approved or same-day).
3. Come back and I can immediately extend `audit/study_a_tokenizer_fertility/run_fertility_pilot.py`
   to the full 12-language design once you paste the token or confirm access.

## 3. Run the actual PRISMA search (after step 1)

Following `protocol/osf_preregistration_draft.md` §5-6:
1. Search all six databases (ACL Anthology, arXiv, OpenAlex, Semantic Scholar, IEEE Xplore, ACM DL) with the registered search string.
2. Export results, deduplicate.
3. Bring the raw record counts back here - I can help build the screening spreadsheet and PRISMA flow diagram numbers once you have them.

## 4. Recruit 2-3 Bangla-speaking annotators (can happen anytime)

For Study C (`audit/study_c_error_taxonomy/`):
- Ideally from different regions/dialect backgrounds (to avoid biasing dialect-flattening detection).
- Send them `annotation_guidelines.md` + `annotations_template.csv`.
- Once you have 2+ filled-in `annotations_r*.csv` files, `compute_agreement.py` will give you real Fleiss' kappa immediately.

## 5. Get free LLM API keys for Study C's remaining 3 models (optional, in parallel)

- Groq (groq.com) - free tier, fast, has Llama-3 and Qwen2.5.
- Google AI Studio (aistudio.google.com) - free tier, has Gemini Flash.
- Bring me the keys or the generated outputs, and I'll extend `llm_outputs_pilot.csv` to the full 4-model design.

## What happens after any of these land

Come back and tell me which step you completed - I'll immediately:
- Extend Study A to 12 languages (after step 2)
- Build the screening spreadsheet + PRISMA flow diagram (after step 3 gives real numbers)
- Compute real Fleiss' kappa and update Section 13/14's `[TODO]` numbers (after step 4)
- Extend Study C to 4 models (after step 5)
- Write Sections 6-12 and 15 (only possible after step 3's screening + extraction is substantially complete - this is the biggest remaining piece of work, ~120 hours per the blueprint's time budget)

## Everything that's already done (for reference)

See [`paper/README.md`](paper/README.md) for full section-by-section
status, and the main [`README.md`](README.md) for the project overview
and live findings so far (1.67x Bengali token premium, 69.2%
non-native benchmark provenance).
