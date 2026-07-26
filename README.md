<div align="center">

# 🌏 Low-Resource Language NLP in the LLM Era

### A Systematic Review and Empirical Audit of the Bangla and South Asian Language Ecosystem

<img src="https://img.shields.io/badge/status-in--progress-yellow?style=for-the-badge" alt="status"/>
<img src="https://img.shields.io/badge/protocol-PRISMA%202020-blueviolet?style=for-the-badge" alt="prisma"/>
<img src="https://img.shields.io/badge/languages%20audited-12-ff69b4?style=for-the-badge" alt="languages"/>
<img src="https://img.shields.io/badge/license-MIT-brightgreen?style=for-the-badge" alt="license"/>

<img src="https://img.shields.io/badge/🎯%20target-Artificial%20Intelligence%20Review%20(Q1)-orange?style=flat-square"/>
<img src="https://img.shields.io/badge/💰%20cost-%240-success?style=flat-square"/>
<img src="https://img.shields.io/badge/🔬%20studies-3%20empirical%20audits-red?style=flat-square"/>
<img src="https://img.shields.io/badge/📖%20reviewed%20papers-~280-informational?style=flat-square"/>

</div>

---

## 🔥 What this is

A **systematic review + reproducible empirical audit** of how Large
Language Models serve — and fail — Bangla and neighboring South Asian
low-resource languages. This is not just another literature survey:
every claim in the paper is backed either by a citation or by data we
generated and can regenerate ourselves.

> 🇧🇩 Bangla has **270+ million speakers** — the 6th most-spoken language
> on Earth — yet remains near-invisible in LLM benchmarks. This project
> measures exactly how, and by how much.

---

## 🧬 The Four Pillars

<table>
<tr>
<td width="25%" align="center">

### 📚 Systematic Review
PRISMA 2020 protocol · 6 databases · dual-screened · Cohen's κ reported

</td>
<td width="25%" align="center">

### 🗺️ Original Taxonomy
6-layer **LRL-LLM Lifecycle** framework, script → governance

</td>
<td width="25%" align="center">

### ⚙️ Empirical Audit
Tokenizer fertility · benchmark provenance · native-speaker error taxonomy

</td>
<td width="25%" align="center">

### 🚀 Research Agenda
9 falsifiable open problems, each with a first step + success metric

</td>
</tr>
</table>

---

## 📊 Live Finding: The Bangla Token Tax

Pilot run on 2,499 parallel Bengali–English sentence pairs
([Study A](audit/study_a_tokenizer_fertility/)):

| Tokenizer | Bengali fertility | Token premium vs. English | Context lost |
|:---|---:|---:|---:|
| 🔴 GPT-4 / o200k | 2.08 | **1.67×** | −40.0% |
| 🟠 mT5 | 2.72 | **1.51×** | −33.7% |
| 🟡 XLM-R | 2.37 | **1.25×** | −20.1% |
| 🟢 NLLB | 2.17 | **1.16×** | −13.6% |
| 🟢 MuRIL | 1.92 | **1.05×** | −4.8% |
| 🔵 BanglaBERT | 1.78 | **0.78×** | **+27.6%** (cheaper than English) |

**Translation:** on the most widely used commercial tokenizer, a Bangla
speaker pays ~1.67× the token cost and loses ~40% of usable context
window compared to an English speaker — for saying the *same thing*.
The BanglaBERT row proves this isn't inherent to the script: it's a
vocabulary-allocation choice. *(Full 12-language FLORES-200 audit
pending gated-dataset access — see the Study A README.)*

---

## 📁 Repository Map

```
lrl-llm-survey/
├── LRL-LLM-MASTER-PROTOTYPE.md          # full paper blueprint (single source of truth)
├── LRL-LLM-Review-Paper-Blueprint.md    # earlier planning draft
├── audit/
│   └── study_a_tokenizer_fertility/     # tokenizer fertility & cost-premium pipeline
├── protocol/                            # PRISMA pre-registration (coming)
├── screening/                           # PRISMA screening decisions (coming)
├── extraction/                          # 22-field data extraction sheet (coming)
└── paper/                               # manuscript source (coming)
```

---

## 🛡️ Why This Survey Won't Get Desk-Rejected

| Common rejection reason | How this project pre-empts it |
|:---|:---|
| "No novel contribution" | Original 6-layer taxonomy + 3 reproducible empirical studies |
| "Ad-hoc paper selection" | PRISMA 2020 + OSF pre-registration + Cohen's κ |
| "Just a list, no synthesis" | Settled / Contested / Unknown takeaway box per taxonomy layer |
| "Claims unsupported" | Every number traces to a citation or to code in this repo |
| "Not reproducible" | Screening CSVs, extraction sheets, and audit code all public here |

---

## 🌐 Target Venue

**Artificial Intelligence Review** (Springer, Q1) → *Information Processing & Management* (Elsevier, Q1) → *Language Resources & Evaluation* (Springer) → ACM TALLIP

---

<div align="center">

**Status:** 🚧 systematic review + empirical audit in active progress · Δ-table and Related Surveys section drafted · Study A pilot complete

</div>
