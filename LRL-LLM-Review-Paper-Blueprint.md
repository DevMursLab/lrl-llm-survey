# Low-Resource Language NLP in the LLM Era — Q1 Review Paper Blueprint
### একটা complete, reviewer-proof prototype যেটা দেখে দেখে তুমি পেপার লিখতে পারবে

---

## ⚠️ PART 0 — আগে একটা সৎ কথা (venue reality check)

তোমার original plan-এ লেখা ছিল **ACM TALLIP**। সত্যি কথাটা বলি:

| Venue | Quartile (রিয়েলিটি) | Survey নেয়? | মন্তব্য |
|---|---|---|---|
| ACM TALLIP | **Q2** (Scopus, CS-Language) | হ্যাঁ | ভালো fit, কিন্তু Q1 না |
| LREC / COLING | Conference (Q না) | হ্যাঁ | Resource paper-এর জন্য ideal, কিন্তু journal metric নেই |
| **Artificial Intelligence Review** (Springer) | **Q1**, IF ~10+ | **শুধু survey/review-ই ছাপে** | ⭐ তোমার #1 target |
| **Information Processing & Management** (Elsevier) | **Q1**, IF ~7-8 | হ্যাঁ (systematic review নেয়) | ⭐ #2 target |
| **ACM Computing Surveys (CSUR)** | **Q1**, IF ~23 | শুধু survey | সবচেয়ে prestigious, কিন্তু acceptance ~15%, editor desk-reject অনেক |
| **Language Resources & Evaluation** (Springer) | Q1/Q2 borderline | হ্যাঁ | ভালো backup |
| Natural Language Engineering (CUP) | Q2 | হ্যাঁ | backup |
| IEEE Access | Q1 (Engineering-multidisciplinary) | হ্যাঁ | দ্রুত, কিন্তু survey-তে reviewer কড়া হয়েছে ইদানীং |

**Strategy:** Artificial Intelligence Review → (reject হলে) Information Processing & Management → (reject হলে) ACM TALLIP → LRE.

একই manuscript, শুধু format বদলাবে। তাই লেখাটা **journal-agnostic** ভাবে লিখবে (formatting শেষে)।

---

## 🔥 PART 1 — Novelty Positioning: কেন এই survey reject হবে না

### সমস্যা যেটা বেশিরভাগ student survey-কে মারে

Reviewer-এর #1 rejection line হয়: *"This paper summarizes existing work but offers no new insight beyond what is already available in [Hedderich et al. 2021] and [Joshi et al. 2020]."*

মানে — **শুধু পড়ে-লিখে-summarize করলে Q1-এ যাবে না।** ২০২৬ সালে Q1 survey-তে লাগে **survey + evidence**।

### তোমার Killer Move: "Survey + Reproducible Audit" hybrid

পেপারটা ৩টা জিনিস একসাথে করবে:

```
┌─────────────────────────────────────────────────────────┐
│  CONTRIBUTION 1: Systematic Review (PRISMA 2020)        │
│  → 250-350 papers, formal protocol, inter-rater kappa   │
├─────────────────────────────────────────────────────────┤
│  CONTRIBUTION 2: Original Taxonomy                      │
│  → 6-layer "LRL-LLM Lifecycle" framework                │
│  → প্রতিটা paper এই taxonomy-তে map করা                  │
├─────────────────────────────────────────────────────────┤
│  CONTRIBUTION 3: Empirical Companion Audit ⭐ (KILLER)   │
│  → নিজে measurement চালাবে: tokenizer fertility,        │
│    benchmark coverage, corpus quality — 12 ভাষায়        │
│  → এইটা কেউ fake করতে পারবে না, এইটাই তোমার moat        │
├─────────────────────────────────────────────────────────┤
│  CONTRIBUTION 4: Research Agenda + Open Problems        │
│  → 9টা concrete, falsifiable open problem               │
└─────────────────────────────────────────────────────────┘
```

**Contribution 3-ই তোমার আসল অস্ত্র।** কারণ:
- এটা GPU লাগে না (tokenizer counting CPU-তেই হয়) → তোমার resource constraint-এ fit করে
- এটা reproducible → reviewer verify করতে পারবে → trust বাড়ে
- এটা "novel empirical finding" দেয় → "no new insight" অভিযোগ মরে যায়
- এটা native-speaker knowledge লাগে (Bangla conjunct, Sylheti Nagri, dialect) → তোমার unfakeable edge

### তোমার Native-Speaker Edge কীভাবে *academically* cash করবে

শুধু "আমি native speaker" বললে reviewer পাত্তা দেবে না। যেভাবে দেবে:

1. **Linguistic error taxonomy** — LLM output-এ Bangla-specific error types তুমি label করবে (যুক্তাক্ষর ভাঙা, সাধু-চলিত mixing, ZWNJ misuse, honorific/আপনি-তুমি-তুই register collapse)। এটা non-native reviewer/গবেষক পারবেই না।
2. **Dialect–standard gap documentation** — Sylheti, Chittagonian, Rangpuri, Chakma-র জন্য কী resource আছে/নেই, তার first-hand catalog।
3. **Native-speaker validation panel** — ৩-৫ জন Bangla native speaker দিয়ে একটা ছোট annotation round (Cohen's kappa রিপোর্ট করবে)। এইটা methodology section-এ বিশাল weight যোগ করে।

---

## 📐 PART 2 — Title, Abstract, Keywords (ready-to-adapt)

### Title options (Q1-friendly)

**Option A (recommended):**
> *Low-Resource Language NLP in the Era of Large Language Models: A Systematic Review and Empirical Audit of the Bangla and South Asian Language Ecosystem*

**Option B (broader, CSUR-style):**
> *From Scarcity to Systematicity: A PRISMA-Guided Survey of Low-Resource Language Processing with Large Language Models*

**Option C (sharper, evidence-forward):**
> *Who Gets Left Behind? A Systematic Review and Measurement Study of Tokenization, Data, and Evaluation Gaps for South Asian Low-Resource Languages in LLMs*

> **টিপ:** Title-এ "Systematic Review" শব্দটা রাখো — editor immediately বোঝে এটা casual survey না।

### Abstract structure (250 words, structured)

```
[1-2 বাক্য: Context]      LLM-এর দ্রুত অগ্রগতি সত্ত্বেও, বিশ্বের বেশিরভাগ
                          ভাষা — যার মধ্যে ৩০ কোটি+ speaker-এর Bangla ও
                          সংশ্লিষ্ট South Asian ভাষা — systematically
                          underserved।

[1 বাক্য: Gap]            LLM-যুগে এই ভাষাগুলোর tokenization, data,
                          adaptation ও evaluation নিয়ে কোনো unified,
                          protocol-driven synthesis নেই।

[2 বাক্য: Method]         আমরা PRISMA 2020 অনুসরণ করে ৬টি database থেকে
                          [N] টি study screen করে [n] টি include করেছি
                          (κ = 0.xx)। পাশাপাশি [K] টি tokenizer × [M] টি
                          ভাষার উপর একটি reproducible empirical audit
                          চালিয়েছি।

[3-4 বাক্য: Findings]     আমরা একটি ৬-স্তরের LRL-LLM Lifecycle taxonomy
                          প্রস্তাব করছি। Audit-এ দেখা যায় Bangla-র
                          tokenizer fertility ইংরেজির তুলনায় X গুণ বেশি,
                          যা inference cost-এ সরাসরি Y% premium তৈরি করে।
                          [n]% study শুধু Standard Bangla নিয়ে কাজ করে;
                          dialect coverage <Z%। Evaluation-এর [w]%
                          translated benchmark ব্যবহার করে, যা
                          translationese artifact তৈরি করে।

[1-2 বাক্য: Implication]  আমরা ৯টি open problem ও একটি community
                          roadmap প্রস্তাব করছি। সব code, screening
                          decision ও extraction sheet public।
```

### Keywords (৬টা, indexing-optimized)
`low-resource languages` · `large language models` · `Bangla NLP` · `systematic literature review` · `tokenization fairness` · `multilingual evaluation`

---

## 🔬 PART 3 — PRISMA 2020 Protocol (এইটাই তোমার rejection-shield)

### 3.1 Protocol pre-registration (⭐ করতেই হবে)

লেখা শুরুর **আগে** protocol register করো:
- **OSF Registries** (osf.io/registries) — free, instant, DOI পাবে
- Paper-এ লিখবে: *"The review protocol was pre-registered on OSF (DOI: 10.17605/OSF.IO/XXXXX) prior to screening."*

এই এক লাইন reviewer-এর "post-hoc cherry-picking" অভিযোগ পুরো মেরে দেয়।

### 3.2 Databases (৬টা — কম হলে reviewer ধরবে)

| # | Database | কেন |
|---|---|---|
| 1 | ACL Anthology | NLP-র primary venue, অপরিহার্য |
| 2 | Scopus | broad indexing |
| 3 | Web of Science Core Collection | quality filter |
| 4 | IEEE Xplore | engineering-side |
| 5 | ACM Digital Library | CSUR/TALLIP-সহ |
| 6 | arXiv (cs.CL) | preprint — LLM field-এ না নিলে recency মিস |
| + | Semantic Scholar API | backward/forward snowballing-এর জন্য |

**Grey literature:** technical report (NLLB, Aya, IndicTrans2) অবশ্যই include করবে, কিন্তু আলাদা flag দিয়ে — এবং sensitivity analysis-এ দেখাবে grey lit বাদ দিলে conclusion বদলায় কি না।

### 3.3 Search String (ready to use — প্রতিটা DB-তে adapt করো)

```
(
  "low-resource language*" OR "low resource NLP" OR "under-resourced language*"
  OR "underrepresented language*" OR "long-tail language*"
)
AND
(
  "large language model*" OR "LLM" OR "foundation model*"
  OR "multilingual model*" OR "instruction tun*" OR "in-context learning"
)
AND
(
  Bangla OR Bengali OR Assamese OR Sylheti OR Odia OR Oriya OR Nepali
  OR Maithili OR Bhojpuri OR Santali OR Bodo OR Manipuri OR Meitei
  OR Chakma OR Rohingya OR Urdu OR Sindhi OR Pashto OR Sinhala
  OR Dhivehi OR "South Asia*" OR "Indic" OR "Indo-Aryan"
)
```

- **Date range:** 2019-01-01 → 2026-06-30 (BERT-পরবর্তী থেকে; justify করবে "transformer-era pretraining paradigm shift" দিয়ে)
- **Language of publication:** English (limitation হিসেবে declare করবে — নিচে bias section দেখো)

### 3.4 Inclusion / Exclusion Criteria (টেবিল আকারে paper-এ দেবে)

**Inclusion (IC):**
- IC1: অন্তত একটি low-resource ভাষা (Joshi et al. taxonomy class 0–3) নিয়ে empirical বা methodological contribution
- IC2: LLM বা large pretrained multilingual model জড়িত
- IC3: peer-reviewed venue বা ≥10 citation-সহ arXiv preprint
- IC4: full text ইংরেজিতে পাওয়া যায়
- IC5: 2019–2026 প্রকাশিত

**Exclusion (EC):**
- EC1: শুধু high-resource ভাষা (English/Chinese-only)
- EC2: speech-only, ভাষাগত text component ছাড়া
- EC3: abstract/poster/extended abstract (<4 pages)
- EC4: duplicate/preprint যার published version আছে (published-টা রাখবে)
- EC5: non-NLP application যেখানে ভাষা incidental

### 3.5 Screening Workflow

```
Identification  →  Records from 6 DBs        (n = 4,xxx)
                   Records from snowballing  (n = xxx)
                          ↓
                   Duplicates removed        (n = 1,xxx)
                          ↓
Screening       →  Title+abstract screened   (n = 3,xxx)
                   Excluded                  (n = 2,xxx)
                          ↓
Eligibility     →  Full-text assessed        (n = 5xx)
                   Excluded with reasons     (n = 2xx)
                     · EC1 না-related  (n=xx)
                     · EC3 too short   (n=xx)  ← reason-wise breakdown লাগবে
                          ↓
Included        →  Studies in synthesis      (n = 28x)
```

**Dual screening:** অন্তত ২০% record দুইজন (তুমি + Md. Shovon বা একজন peer) স্বাধীনভাবে screen করবে। **Cohen's κ রিপোর্ট করবে**। κ ≥ 0.75 হলে "substantial agreement" বলা যায়। Disagreement → third-party arbitration।

> ⚠️ κ ছাড়া systematic review পাঠালে Q1 reviewer প্রায় নিশ্চিত reject করবে। এটা skip করা যাবে না।

### 3.6 Data Extraction Form (spreadsheet columns)

প্রতিটা included paper-এর জন্য এই ২২টা field extract করবে:

| # | Field | Type |
|---|---|---|
| 1 | Paper ID / DOI | string |
| 2 | Year | int |
| 3 | Venue + type (conf/journal/preprint) | categorical |
| 4 | Author affiliation country | categorical |
| 5 | Languages studied | list |
| 6 | Joshi class of each language (0–5) | int |
| 7 | Script(s) | list |
| 8 | Task(s) (NER/MT/QA/summarization/…) | list |
| 9 | **Taxonomy layer** (L1–L6, নিচে দেখো) | categorical |
| 10 | Model family (encoder/decoder/enc-dec) | categorical |
| 11 | Model size | numeric |
| 12 | Adaptation method (CPT/SFT/LoRA/vocab-exp/ICL/none) | categorical |
| 13 | Data source (web-crawl/curated/synthetic/human) | categorical |
| 14 | Dataset size (tokens/sentences) | numeric |
| 15 | Evaluation benchmark used | list |
| 16 | Benchmark origin (native/translated/machine-translated) | categorical |
| 17 | Metric(s) reported | list |
| 18 | Human evaluation? (Y/N, #annotators) | bool+int |
| 19 | Code released? Data released? | bool ×2 |
| 20 | Dialect/variety addressed? | bool |
| 21 | Reported limitations | free text |
| 22 | Quality score (নিচের rubric) | 0–10 |

### 3.7 Quality Appraisal Rubric (custom, 10-point)

Standard medical tools (CASP/AMSTAR) NLP-তে fit করে না, তাই নিজে বানাবে এবং justify করবে:

| Criterion | Points |
|---|---|
| Reproducibility: code + data + seeds public | 0–2 |
| Baselines: ≥2 competitive baseline compared | 0–2 |
| Statistical rigor: multi-seed, CI বা significance test | 0–2 |
| Evaluation validity: native (not machine-translated) benchmark | 0–2 |
| Linguistic grounding: native speaker involvement documented | 0–1 |
| Limitations honestly declared | 0–1 |

Score ≥7 = high quality, 4–6 = moderate, <4 = low। Synthesis-এ quality-weighted করবে এবং low-quality বাদ দিয়ে sensitivity analysis দেখাবে।

---

## 🧬 PART 4 — তোমার Original Taxonomy (এইটাই paper-এর "Figure 1")

### The **LRL-LLM Lifecycle Taxonomy** — ৬টা layer

প্রতিটা included paper ঠিক একটা (বা একাধিক) layer-এ pin করবে। এই framework-টাই তোমার intellectual contribution।

```
╔══════════════════════════════════════════════════════════════╗
║  L1 · SCRIPT & ENCODING SUBSTRATE                            ║
║  Unicode normalization (NFC/NFD), যুক্তাক্ষর/conjunct handling,║
║  ZWJ/ZWNJ, Sylheti Nagri vs Bengali script, OCR quality,      ║
║  romanization (Banglish), script-mixing                       ║
╠══════════════════════════════════════════════════════════════╣
║  L2 · DATA ACQUISITION & CURATION                            ║
║  Web-crawl quality (mC4/OSCAR/CulturaX audit), noise rate,    ║
║  deduplication, synthetic data, community sourcing,           ║
║  data sovereignty, licensing                                  ║
╠══════════════════════════════════════════════════════════════╣
║  L3 · TOKENIZATION & REPRESENTATION                          ║
║  Fertility, token premium, vocabulary allocation, BPE vs      ║
║  Unigram vs byte-level, vocabulary expansion, embedding init  ║
╠══════════════════════════════════════════════════════════════╣
║  L4 · ADAPTATION & TRANSFER                                  ║
║  Continued pretraining, cross-lingual transfer, PEFT/LoRA,    ║
║  instruction tuning, multilingual RLHF/DPO, model merging,    ║
║  distillation                                                 ║
╠══════════════════════════════════════════════════════════════╣
║  L5 · EVALUATION & MEASUREMENT                               ║
║  Native vs translated benchmarks, translationese, data        ║
║  contamination, LLM-as-judge validity in LRL, human eval,     ║
║  metric transferability (BLEU/chrF/COMET in Bangla)           ║
╠══════════════════════════════════════════════════════════════╣
║  L6 · DEPLOYMENT, EQUITY & GOVERNANCE                        ║
║  Inference cost asymmetry, latency, safety/guardrail gaps,    ║
║  annotator labor ethics, dialect erasure, policy, community   ║
║  ownership                                                    ║
╚══════════════════════════════════════════════════════════════╝
```

**কেন এই taxonomy novel:** বিদ্যমান survey (Hedderich et al. 2021 ধরনের) শুধু *method*-ভিত্তিক (data augmentation / transfer learning / …)। তোমারটা **lifecycle/pipeline-ভিত্তিক**, যা LLM-যুগে বেশি প্রাসঙ্গিক কারণ bottleneck এখন method না — bottleneck হলো L1, L2, L3, L5। এই argument-টা explicitly Section 3-এ লিখবে।

### Cross-cutting dimensions (taxonomy-র দ্বিতীয় অক্ষ)

প্রতিটা layer-কে এই ৩টা lens দিয়ে দেখবে → 2D grid তৈরি হবে:
- **D1: Language typology** (Indo-Aryan vs Tibeto-Burman vs Austroasiatic)
- **D2: Resource tier** (Joshi class 0–1 vs 2–3)
- **D3: Modality of writing** (standardized script / non-standardized / romanized-only)

এই 6×3 grid-ই তোমার **Table 3** এবং heatmap **Figure 4** — কোন cell খালি, সেটাই তোমার "research gap" এর visual proof। ⭐ এই খালি ঘরগুলোই reviewer-কে convince করবে যে gap আসল।

---

## ⚙️ PART 5 — Empirical Companion Audit (তোমার KILLER contribution)

এইটা survey-কে Q1-এ তোলে। GPU লাগবে না। ৩টা study।

### Study A — Tokenizer Fertility & Cost Asymmetry Audit

**Research Question:** একই semantic content express করতে South Asian ভাষায় কত বেশি token লাগে, এবং সেটার আর্থিক/context-window খরচ কত?

**Design:**
- **Languages (12):** Bangla, Assamese, Odia, Nepali, Sinhala, Urdu, Sindhi, Maithili, Bhojpuri, Santali, Manipuri, Sylheti (+ English, Hindi as reference)
- **Parallel corpus:** FLORES-200 devtest (সব ভাষায় একই ১০১২টা বাক্য — perfectly parallel, এটাই key)
- **Tokenizers (≥8):** GPT-4/o200k, Llama-3, Gemma, Qwen, mT5, XLM-R, NLLB, IndicTrans2, MuRIL, BanglaBERT
- **Metrics:**
  - `Fertility = tokens / word`
  - `Token Premium = tokens_L / tokens_English` (একই meaning)
  - `Byte-efficiency = tokens / UTF-8 bytes`
  - `Vocabulary allocation = |{vocab entries containing script X}| / |V|`
  - `Context-window shrinkage = 1 − (1 / premium)` → "একই 8k context-এ Bangla user কত কম তথ্য দিতে পারে"
  - `Cost premium (USD)` → API pricing দিয়ে actual টাকার অঙ্ক

**কেন এইটা killer:** এটা একটা **নীতিগত (policy-relevant) সংখ্যা** দেয় — "একজন বাংলাভাষী ব্যবহারকারী একই কাজের জন্য X গুণ বেশি টাকা দেয়"। Reviewer এই ধরনের concrete equity finding-কে খুব value করে, আর এটা press/citation ও টানে।

**Compute:** পুরোটা CPU, ~30 মিনিট। কোনো training নেই।

### Study B — Benchmark Coverage & Provenance Audit

**RQ:** LRL evaluation আসলে কতটা "native"?

- ২৫-৩০টা multilingual benchmark (XNLI, XQuAD, TyDiQA, Belebele, FLORES, MMLU-translated, IndicGLUE, IndicXTREME, BLUB, MEGA/MEGAVERSE ইত্যাদি) catalog করবে
- প্রতিটার জন্য কোড করবে: **native-authored / human-translated / machine-translated / synthetic**
- Output: stacked bar chart → দেখাবে LRL evaluation-এর বিশাল অংশ translated, মানে **translationese artifact** দিয়ে দূষিত
- সাথে: প্রতিটা ভাষার জন্য task coverage matrix (কোন ভাষার কোন task-এ কোনো benchmark-ই নেই)

### Study C — Native-Speaker Error Taxonomy (তোমার unfakeable edge)

**RQ:** LLM-generated Bangla-তে ঠিক কী ধরনের ভুল হয়, যেটা automatic metric ধরতে পারে না?

- ৩-৪টা LLM থেকে ১৫০-২০০টা Bangla output নমুনা (৪-৫টা task: summarization, QA, formal letter, dialect rewrite)
- **৩ জন native annotator** (তুমি + ২ জন) — নিচের error taxonomy দিয়ে label করবে:

| Code | Error type | উদাহরণ |
|---|---|---|
| E1 | Conjunct/যুক্তাক্ষর malformation | "সংখ্যা" → "সংখ‍্যা" ভাঙা |
| E2 | ZWJ/ZWNJ misuse | invisible char pollution |
| E3 | Register collapse (সাধু↔চলিত) | এক অনুচ্ছেদে mixing |
| E4 | Honorific inconsistency | আপনি/তুমি/তুই switch |
| E5 | Calque / English syntax leak | "আমি একটি ভালো সময় ছিল" |
| E6 | Lexical anglicization | দরকার নেই এমন English loan |
| E7 | Numeral/date localization fail | ১২/12 mixing, বঙ্গাব্দ |
| E8 | Cultural/factual localization error | ভুল উৎসব, ভুল ভূগোল |
| E9 | Dialect flattening | Sylheti চাইলে Standard Bangla দেয় |

- **Cohen's/Fleiss' κ রিপোর্ট করবে** (target ≥0.70)
- তারপর দেখাবে: BLEU/chrF/COMET/LLM-as-judge এই error গুলোর সাথে **correlate করে না** → মানে বর্তমান metric গুলো Bangla-র জন্য invalid। এটা একটা শক্তিশালী, publishable finding।

> এই Study C-ই সেই জিনিস যেটা "অন্য কেউ fake করতে পারবে না" — তোমার original edge-এর academic রূপ।

---

## 📄 PART 6 — Section-by-Section Skeleton (word budget সহ)

মোট target: **14,000–18,000 words** (Q1 survey-র standard)। AI Review/CSUR এই দৈর্ঘ্য আশা করে।

| § | Section | Words | কী থাকবে |
|---|---|---|---|
| 1 | Introduction | 1,200 | Motivation → gap → RQ → contributions (bulleted) → roadmap |
| 2 | Background & Scope | 1,200 | LLM basics (সংক্ষিপ্ত), "low-resource" এর definition debate, Joshi taxonomy, South Asian language landscape + speaker numbers |
| 3 | Related Surveys & Delta | 900 | **Table 1: existing survey comparison** — কে কী cover করেছে, তুমি কী নতুন দিচ্ছ ⭐ |
| 4 | Review Methodology | 1,800 | PRISMA protocol পুরোটা, search string, IC/EC, κ, extraction form, quality rubric, PRISMA flow diagram |
| 5 | Taxonomy | 1,200 | 6-layer framework + 3 cross-cutting dimensions + Figure 1 |
| 6 | L1: Script & Encoding | 1,200 | + Table |
| 7 | L2: Data | 1,600 | corpus audit findings, quality issues |
| 8 | L3: Tokenization | 1,400 | ← **Study A results এখানে** |
| 9 | L4: Adaptation | 1,800 | সবচেয়ে বড় literature body |
| 10 | L5: Evaluation | 1,600 | ← **Study B + C results এখানে** |
| 11 | L6: Equity & Governance | 1,000 | cost asymmetry, labor, sovereignty, policy |
| 12 | Bibliometric Analysis | 800 | year trend, venue, geography, language coverage — Figure 5-7 |
| 13 | Discussion: 9 Open Problems | 1,500 | প্রতিটা: statement + why hard + concrete first step + success metric |
| 14 | Threats to Validity | 700 | নিচের bias section |
| 15 | Conclusion | 500 | কোনো নতুন claim না |
| — | Data Availability / Ethics / CRediT | 300 | |

### §1 Introduction — লেখার formula (৫ paragraph)

```
P1 (Hook + scale):  বিশ্বে ৭,০০০+ ভাষা; LLM কার্যকরভাবে ~২০টিতে কাজ করে।
                    Bangla — বিশ্বের ৬ষ্ঠ বৃহত্তম ভাষা, ২৭+ কোটি speaker —
                    তবুও LLM benchmark-এ প্রায় অনুপস্থিত। [সংখ্যা verify করবে]

P2 (Why now):       Pre-LLM যুগে সমস্যা ছিল "model নেই"। LLM যুগে model
                    আছে কিন্তু সমস্যা স্থানান্তরিত হয়েছে — এখন bottleneck
                    tokenization, data quality, evaluation validity।
                    বিদ্যমান survey এই paradigm shift ধরেনি।

P3 (The gap):       তিনটা নির্দিষ্ট gap: (i) কোনো PRISMA-driven synthesis নেই;
                    (ii) কোনো unified lifecycle taxonomy নেই; (iii) কোনো
                    reproducible measurement নেই, ফলে দাবিগুলো anecdotal।

P4 (Contributions): বুলেট আকারে ৪টা contribution + ৩টা RQ স্পষ্ট করে।

P5 (Roadmap):       Section-wise navigation।
```

### §3 — Table 1 হলো তোমার সবচেয়ে গুরুত্বপূর্ণ টেবিল

> ⚠️ **আপডেট (2026-07-27):** নিচের টেবিলে ২০২৪-২০২৬-এর real, verified competing survey যোগ করা হয়েছে (web search + arXiv abstract cross-check)। সবচেয়ে কাছের direct competitor: **Poria & Huang 2025 (arXiv:2509.11570, "Bhaasha, Bhāṣā, Zaban")** এবং **Gupta 2025 (arXiv:2501.00029, breadth-first South Asian catalog)** — Related Surveys section-এ এই দুইটার সাথে explicit paragraph-এ differentiate করতে হবে (PRISMA rigor + tokenization audit + native-speaker error taxonomy না থাকার point ধরে)। জমা দেওয়ার আগে প্রতিটা arXiv ID নিজে খুলে verify করো।

| Survey | Year | PRISMA? | LLM-era? | South Asia focus? | Tokenization? | Empirical audit? | #Papers |
|---|---|---|---|---|---|---|---|
| Hedderich et al. | 2021 | ✗ | ✗ | ✗ | ✗ | ✗ | ~100 |
| Magueresse et al. | 2020 | ✗ | ✗ | ✗ | ✗ | ✗ | — |
| Joshi et al. | 2020 | ✗ | ✗ | partial | ✗ | ✓ (bibliometric) | — |
| Qin et al. — *Multilingual LLM Survey* (arXiv:2404.04925, *Patterns* 2025) | 2024 | ✗ | ✓ | ✗ | ✗ | ✗ | — |
| Huang et al. — *Survey on LLMs with Multilingualism* (arXiv:2405.10936) | 2024 | ✗ | ✓ | ✗ | ✗ | ✗ | — |
| Tamang & Bora — *Evaluating Tokenizer Performance across Official Indian Languages* (arXiv:2411.12240) | 2024 | ✗ | ✓ | ✓ | ✓ (empirical, not survey) | ✓ tokenizer-only | — |
| Lupascu et al. — *Large Multimodal Models for LRLs* (arXiv:2502.05568) | 2025 | ✗ | ✓ | partial (Bengali only) | ✗ | ✗ | 117 |
| Gupta — *Breadth-First Catalog, South Asian Languages* (arXiv:2501.00029) | 2025 | ✗ (LLM-assisted classification) | ✓ | ✓ | ✗ | ✗ (unvalidated) | ~505 |
| McGiff & Nikolov — *Overcoming Data Scarcity in Generative LM for LRLs* (arXiv:2505.04531) | 2025 | ⚠️ unconfirmed — verify | ✓ | ✗ | ✗ | ✗ | 54 |
| Poria & Huang — *Bhaasha, Bhāṣā, Zaban* (arXiv:2509.11570) | 2025 | ✗ | ✓ | ✓ | ✗ | ✗ (resource list only) | — |
| Doğruöz et al. — *LLMs-as-Judge in Multilingual/LRL Settings* (arXiv:2607.02235) | 2026 | ✗ (systematic, not PRISMA-labeled) | ✓ | ✗ | ✗ | ✓ (judging-practice audit) | 650 screened |
| Kumar et al. — *BhashaSutra* (arXiv:2604.18423, ACL 2026) | 2026 | ✗ | partial | ✓ (22 languages) | ✗ | ✗ | 200+ datasets |
| **This work** | **2026** | **✓** | **✓** | **✓** | **✓** | **✓** | **~28x** |

শেষ সারিতে সব ✓ — এটাই editor-কে ১০ সেকেন্ডে convince করে। **এই টেবিল ছাড়া survey পাঠাবে না।** (পূর্ণাঙ্গ sync করা version: MASTER-PROTOTYPE.md → B5)

### §13 — 9 Open Problems (template)

প্রতিটা এই format-এ লিখবে (vague হলে reviewer বিরক্ত হয়):

```
OP-3: Dialect-Faithful Generation
├─ Problem statement: বর্তমান LLM "Sylheti-তে লেখো" নির্দেশে
│                     Standard Bangla-ই ফেরত দেয় (Study C-তে xx% ক্ষেত্রে)।
├─ Why it is hard:    Sylheti-র standardized orthography নেই; parallel
│                     data নেই; evaluation metric নেই।
├─ Concrete first step: ৫,০০০-বাক্যের Sylheti–Bangla parallel seed corpus
│                     community elicitation দিয়ে; dialect-ID classifier।
└─ Success metric:    Native-speaker dialect-authenticity score ≥4/5,
                      এবং dialect-ID classifier accuracy ≥0.85।
```

৯টা OP suggestion: (1) Script-faithful tokenization, (2) Corpus quality certification, (3) Dialect-faithful generation, (4) Native-authored benchmark at scale, (5) Metric validity for Indic scripts, (6) Contamination detection in LRL, (7) Equitable inference cost, (8) Safety alignment coverage gap, (9) Community data governance.

---

## 📊 PART 7 — Figures & Tables Spec (Q1-এ ভিজ্যুয়াল না থাকলে দুর্বল লাগে)

**Figures (৮টা):**
1. LRL-LLM Lifecycle Taxonomy (6-layer diagram) — ⭐ signature figure
2. PRISMA 2020 flow diagram (official template ব্যবহার করবে)
3. Publication timeline: papers/year, layer-wise stacked
4. Taxonomy × language-tier heatmap (gap visualization) ⭐
5. Tokenizer fertility bar chart, 12 ভাষা × 8 tokenizer (Study A)
6. Context-window shrinkage + cost premium plot (Study A)
7. Benchmark provenance stacked bar (Study B)
8. Error-type distribution + metric-correlation scatter (Study C)

**Tables (৯টা):**
1. Existing surveys comparison (Δ table) ⭐
2. Language profile: speakers, script, Joshi class, corpus size
3. Taxonomy definition + example papers per layer
4. Search strings per database
5. IC/EC criteria
6. Quality appraisal rubric + score distribution
7. Adaptation methods comparison (L4)
8. Benchmark catalog with provenance coding
9. Open problems summary

> **Design tip:** সব figure একই color palette-এ, vector (PDF/SVG), font ≥8pt, colorblind-safe (viridis/ColorBrewer)। Reviewer খারাপ figure দেখলেই বাকিটা সন্দেহ করে।

---

## 🛡️ PART 8 — Bias & Threats to Validity (তুমি চেয়েছ "no bias" — এইভাবে হবে)

গুরুত্বপূর্ণ কথা: **bias শূন্য করা অসম্ভব; Q1-এ যেটা লাগে তা হলো bias গুলো নাম ধরে ডাকা এবং mitigate করার প্রমাণ দেখানো।** যে survey বলে "no bias" সেটাই সন্দেহজনক লাগে।

| Bias | ঝুঁকি | Mitigation (paper-এ লিখবে) |
|---|---|---|
| **Publication bias** | Negative result ছাপা হয় না → method গুলো বেশি কার্যকর মনে হয় | arXiv/grey lit include; "reported failures" আলাদা করে extract; funnel-style discussion |
| **Language bias** | শুধু English-ভাষী paper | Limitation হিসেবে declare; Bangla/Hindi-ভাষী venue থেকে অন্তত একটা supplementary search চালিয়ে দেখাবে কী মিস হচ্ছে |
| **Database bias** | ACL Anthology-heavy | ৬টা DB + snowballing; DB-wise contribution table দেবে |
| **Geographic/institutional bias** | Big-lab paper বেশি cite হয় | Affiliation extract করবে (field #4) এবং Global South authorship share রিপোর্ট করবে — এটা নিজেই একটা finding |
| **Selection bias** | Screening-এ subjectivity | Pre-registered protocol + dual screening + κ + arbitration |
| **Temporal bias** | LLM field দ্রুত বদলায় | Hard cutoff declare; "living review" হিসেবে GitHub repo maintain করার প্রতিশ্রুতি |
| **Author bias (তোমার নিজের)** | তুমি Bangla-র পক্ষে advocate | ⚠️ **Positionality statement** লিখবে (নিচে দেখো) |
| **Confirmation bias** | "LRL underserved" ধরে নিয়ে শুরু | RQ-গুলো neutral ভাবে লেখো; counter-evidence-এর জন্য আলাদা extraction field রাখো |
| **Annotator bias (Study C)** | ৩ জনই একই অঞ্চলের | Annotator demographic (region, education, dialect) রিপোর্ট করবে; κ দেবে |

### Positionality Statement (এই এক অনুচ্ছেদ তোমার credibility বাড়াবে)

> *"The first author is a native Bangla speaker based in Bangladesh. This positionality informs the linguistic error taxonomy in Section 10 and enables validation that non-native researchers could not readily perform. It also introduces a potential advocacy bias toward emphasizing Bangla-specific gaps. To mitigate this, (i) all screening decisions were pre-registered and dual-coded, (ii) the empirical audit includes eleven additional languages beyond Bangla, and (iii) all annotation data and screening decisions are released publicly for independent re-analysis."*

Reviewer এই ধরনের সততা দেখলে বাকি পেপারকে বেশি বিশ্বাস করে। এটা দুর্বলতা না, শক্তি।

---

## 🚨 PART 9 — Reviewer Rejection Modes → Pre-emption Matrix

Q1-এ survey যে ৯ কারণে reject হয়, আর তুমি আগেই কীভাবে বন্ধ করবে:

| # | Reviewer যা বলবে | তোমার pre-emption |
|---|---|---|
| 1 | "No novel contribution beyond existing surveys" | §3 Δ-table + original taxonomy + ৩টা empirical study |
| 2 | "Ad-hoc paper selection, not systematic" | PRISMA + OSF pre-registration + κ + full flow diagram |
| 3 | "Just a list of papers, no synthesis" | প্রতিটা layer section শেষে **"Synthesis & Takeaways"** box — কী মীমাংসিত, কী বিতর্কিত, কী অজানা |
| 4 | "Coverage incomplete — missing [X]" | Snowballing + reference-check করবে top-20 venue-এর LRL paper; Related Surveys-এ scope boundary স্পষ্ট করবে |
| 5 | "Claims unsupported / anecdotal" | প্রতিটা claim হয় citation নয় নিজের audit data-তে anchored। কোনো unsupported adjective না ("dramatically", "vastly") |
| 6 | "Not reproducible" | GitHub repo: search logs, screening CSV, extraction sheet, audit code, seeds, Dockerfile |
| 7 | "Bangla-centric, over-generalized title" | Title/abstract-এ scope সৎভাবে বলা; audit-এ ১২ ভাষা |
| 8 | "Poor English / structure" | নিচের polish checklist |
| 9 | "Out of scope for this journal" | Cover letter-এ journal-এর ৩টা সাম্প্রতিক paper cite করে fit argue করবে |

### "Synthesis & Takeaways" box template (প্রতিটা layer section-এ)

```
┌─ Takeaways: L3 Tokenization ─────────────────────────────┐
│ ✔ Settled:    Indic scripts show 2–5× fertility vs        │
│               English across all major tokenizers.        │
│ ⚡ Contested:  Whether vocabulary expansion outperforms    │
│               byte-level modeling — evidence conflicts    │
│               ([A] vs [B]), likely due to differing       │
│               CPT budgets.                                │
│ ✗ Unknown:    No study measures fertility effects on      │
│               downstream reasoning under fixed context.   │
│               → Open Problem OP-1                         │
└───────────────────────────────────────────────────────────┘
```

এই box গুলোই "synthesis নেই" অভিযোগের সরাসরি জবাব। ৬টা layer-এ ৬টা box।

---

## 📦 PART 10 — Reproducibility Package (GitHub repo structure)

```
lrl-llm-systematic-review/
├── README.md                      # badges, DOI, how to reproduce
├── protocol/
│   ├── osf_preregistration.pdf
│   └── search_strings_per_database.md
├── screening/
│   ├── 01_raw_records.csv          # সব DB export, timestamp সহ
│   ├── 02_deduplicated.csv
│   ├── 03_title_abstract_decisions.csv   # দুই reviewer-এর কলাম + reason
│   ├── 04_fulltext_decisions.csv
│   ├── 05_included_studies.csv
│   └── kappa_computation.ipynb
├── extraction/
│   ├── extraction_sheet.csv        # ২২ field × n paper
│   └── quality_scores.csv
├── audit/
│   ├── study_a_tokenizer_fertility/
│   │   ├── run_fertility.py
│   │   ├── config.yaml
│   │   └── results/
│   ├── study_b_benchmark_provenance/
│   └── study_c_error_taxonomy/
│       ├── annotation_guidelines.md   # ⭐ এইটা আলাদাভাবে valuable
│       ├── annotations_anonymized.csv
│       └── agreement.ipynb
├── figures/                        # সব figure-এর generating script
├── environment.yml / Dockerfile
└── CITATION.cff
```

Paper-এ **Data Availability Statement**: *"All screening decisions, extraction data, annotation guidelines, and audit code are available at https://github.com/DevMursLab/... and archived at Zenodo (DOI: ...)."*

> Zenodo-তে archive করে DOI নিও — GitHub link পরে ভাঙলে reviewer/editor বিরক্ত হয়।

---

## 📚 PART 11 — Seed Bibliography (anchor papers, ~50)

> ⚠️ **অত্যন্ত জরুরি:** নিচের প্রতিটা reference তোমাকে **নিজে verify করতে হবে** (সঠিক author list, year, venue, DOI)। আমি স্মৃতি থেকে দিচ্ছি — কোনো detail ভুল থাকতে পারে। ভুল citation Q1-এ desk-reject হওয়ার দ্রুততম রাস্তা। Semantic Scholar / DBLP / ACL Anthology থেকে প্রতিটা মিলিয়ে নিও এবং BibTeX সরাসরি সেখান থেকে কপি করো।

**Foundational / positioning**
- Joshi et al. — *The State and Fate of Linguistic Diversity and Inclusion in the NLP World* (ACL 2020) ← language class 0–5 taxonomy
- Blasi et al. — *Systematic Inequalities in Language Technology Performance* (ACL 2022)
- Bender — *The #BenderRule / Linguistically Naive != Language Independent*
- Hedderich et al. — *A Survey on Recent Approaches for NLP in Low-Resource Scenarios* (NAACL 2021)
- Magueresse et al. — *Low-resource Languages: A Review of Past Work and Future Challenges* (2020)
- Ruder et al. — cross-lingual representation learning survey

**Data quality & corpora**
- Kreutzer et al. — *Quality at a Glance: An Audit of Web-Crawled Multilingual Datasets* (TACL 2022) ← L2-র মেরুদণ্ড
- CulturaX / OSCAR / mC4 / MADLAD-400 / ROOTS dataset papers
- AI4Bharat — IndicCorp / IndicCorpv2

**Tokenization**
- Petrov et al. — *Language Model Tokenizers Introduce Unfairness Between Languages* (NeurIPS 2023) ← Study A-র সরাসরি ভিত্তি
- Ahia et al. — *Do All Languages Cost the Same? Tokenization in the Era of Commercial LMs* (EMNLP 2023)
- Rust et al. — *How Good is Your Tokenizer?* (ACL 2021)
- ByT5 / CANINE (tokenizer-free)
- Vocabulary expansion / adaptation papers

**Multilingual models**
- mBERT (Devlin et al.), XLM-R (Conneau et al.), mT5 (Xue et al.), MuRIL (Khanuja et al.)
- BLOOM / BLOOMZ, Aya Model & Aya Dataset (Cohere for AI), Glot500, Bactrian-X
- NLLB Team — *No Language Left Behind* (2022/Nature 2024)

**Indic / Bangla specific**
- Bhattacharjee et al. — *BanglaBERT* (NAACL Findings 2022) + BLUB benchmark
- BanglaNLG / BanglaT5 (CSEBUETNLP)
- IndicNLPSuite, IndicGLUE, IndicXTREME, IndicBART, IndicTrans2, Naamapadam
- SentNoB, BanFakeNews, Bangla NER/POS datasets
- Assamese/Odia/Sylheti/Chakma resource papers (যেগুলো পাও — এখানে কম আছে, সেটাই তোমার gap-এর প্রমাণ)

**Evaluation**
- FLORES-200, Belebele, TyDiQA, XQuAD, XNLI, XCOPA
- MEGA / MEGAVERSE (multilingual LLM evaluation)
- Translationese & translated-benchmark artifact papers
- Data contamination detection papers
- LLM-as-judge validity papers (multilingual limitations)

**Adaptation**
- LoRA (Hu et al.), QLoRA, adapter/MAD-X (Pfeiffer et al.)
- Continued pretraining for LRL papers
- Cross-lingual instruction tuning / multilingual RLHF

**Ethics & governance**
- Data sovereignty / Indigenous data governance (CARE principles)
- Annotator labor / crowdwork ethics papers
- Masakhane / community-driven NLP papers (African NLP — তোমার Bangla community argument-এর জন্য perfect analogue)

**Methodology**
- Page et al. — *PRISMA 2020 Statement* (BMJ 2021) ← cite করতেই হবে
- Kitchenham & Charters — SLR guidelines in software engineering
- Cohen (1960) — kappa

**Target:** ২৫০–৩৫০। এর মধ্যে ~২৮০টা included studies + ~৪০টা methodological/contextual। AI Review-তে ২৫০+ reference স্বাভাবিক।

---

## ⏱️ PART 12 — Execution Timeline (রিয়েলিস্টিক, ছাত্র হিসেবে)

| সপ্তাহ | কাজ | Output |
|---|---|---|
| 1 | Scope lock, RQ finalize, ৫টা competing survey পড়ে Δ-table draft | Table 1 draft |
| 2 | Protocol লেখা + OSF pre-registration + search string pilot | OSF DOI ✓ |
| 3 | ৬টা DB search চালানো, export, dedup | raw + dedup CSV |
| 4–5 | Title/abstract screening (~3,000 record) + dual-screen 20% + κ | screening CSV, κ |
| 6–7 | Full-text screening (~500) + extraction শুরু | included list |
| 8–10 | Extraction পূর্ণ (২২ field × ~280 paper) + quality scoring | extraction sheet |
| 8–9 | **সমান্তরালে:** Study A কোড ও রান (CPU-only) | Figure 5, 6 |
| 10 | Study B benchmark catalog | Figure 7 |
| 11–12 | Study C annotation (৩ জন) + κ + metric correlation | Figure 8 |
| 13–15 | Section 6–11 লেখা (layer-wise, প্রতি সপ্তাহে ২টা layer) | body draft |
| 16 | Section 1–5 লেখা (intro/method সবশেষে লিখলে ভালো হয়) | full draft |
| 17 | Figures polish, tables finalize, reference verification (প্রতিটা!) | v1 |
| 18 | Md. Shovon + ২ জন external-এর internal review, revision | v2 |
| 19 | Language polish, checklist, cover letter, repo public + Zenodo DOI | submission-ready |
| 20 | Submit → AI Review | ✓ |

**~৫ মাস part-time।** এর চেয়ে কম সময়ে Q1-quality systematic review হয় না — যেটা ২ সপ্তাহে হয় সেটা reviewer ধরে ফেলে।

---

## ✅ PART 13 — Pre-Submission Checklist

**Methodological**
- [ ] OSF pre-registration DOI paper-এ উল্লেখ আছে
- [ ] PRISMA 2020 flow diagram official template-এ, সব সংখ্যা যোগ মেলে
- [ ] PRISMA 27-item checklist supplementary হিসেবে জমা
- [ ] Cohen's κ রিপোর্ট করা (≥0.75)
- [ ] Exclusion reason-wise breakdown আছে
- [ ] Sensitivity analysis (grey lit বাদ দিলে / low-quality বাদ দিলে)

**Contribution**
- [ ] Δ-table (Table 1) আছে, শেষ সারি "This work"
- [ ] Taxonomy figure পরিষ্কার, প্রতিটা layer-এর operational definition আছে
- [ ] ৩টা empirical study-র result body-তে integrated (appendix-এ ঠেলে দেওয়া নয়)
- [ ] প্রতিটা layer section-এ Synthesis box
- [ ] ৯টা open problem — প্রতিটায় first step + success metric

**Rigor**
- [ ] কোনো unsupported claim নেই (Ctrl+F: "significantly", "dramatically", "clearly" → প্রতিটার পাশে citation বা data)
- [ ] Positionality statement আছে
- [ ] Threats to validity section আছে
- [ ] প্রতিটা reference DOI-verified (fabricated citation = instant desk reject)

**Presentation**
- [ ] Abstract ≤250 words, structured
- [ ] সব figure vector, colorblind-safe, ≥8pt font
- [ ] সব table caption উপরে, figure caption নিচে (journal style মেনে)
- [ ] Acronym প্রথমবার expand করা
- [ ] Grammarly + একবার line-by-line manual pass
- [ ] Word count journal limit-এর মধ্যে

**Compliance**
- [ ] GitHub repo public + Zenodo DOI
- [ ] Data Availability Statement
- [ ] CRediT author contribution statement (তুমি + Md. Shovon)
- [ ] Conflict of interest declaration
- [ ] AI-use disclosure statement (⭐ ২০২৬-এ বেশিরভাগ Q1 journal বাধ্যতামূলক করেছে — লিখবে LLM কোথায় ব্যবহার করেছ, যেমন "language editing only"; লুকালে ধরা পড়লে retraction-level সমস্যা)
- [ ] Cover letter: journal-এর ৩টা recent paper cite করে fit argue করা
- [ ] Suggested reviewers: ৪-৫ জন (তোমার supervisor বা co-author নয়)

---

## 🎯 শেষ কথা — সবচেয়ে গুরুত্বপূর্ণ ৩টা সিদ্ধান্ত

1. **Study A (tokenizer audit) বাদ দিও না।** এটাই পার্থক্য গড়ে দেবে "ভালো student survey" আর "Q1 paper"-এর মধ্যে। খরচ: ~২ সপ্তাহ, CPU-only। ROI বিশাল।

2. **Pre-registration আজই করো** — লেখা শুরুর আগে। এটা ১ ঘণ্টার কাজ কিন্তু পুরো paper-এর credibility-র ভিত্তি।

3. **Reference একটাও অনুমান করে লিখো না।** আমি উপরে যে seed list দিয়েছি সেটাও verify করতে হবে। ২০২৬-এ editor রা automated citation-checker চালায়; একটা hallucinated reference ধরা পড়লে পুরো paper সন্দেহের মুখে পড়ে।

পরের ধাপে যা চাইলে দিতে পারি: (ক) Study A-র সম্পূর্ণ Python কোড, (খ) OSF pre-registration form-এর পূরণ-করা draft, (গ) Introduction section-এর full draft, (ঘ) Study C-র annotation guidelines নথি।
