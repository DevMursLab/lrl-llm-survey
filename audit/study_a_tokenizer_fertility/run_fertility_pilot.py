"""
Study A (PILOT) - Tokenizer Fertility & Cost Asymmetry Audit
Bengali-English only, using Helsinki-NLP/tatoeba_mt (ungated).

Scope note: this is a single-language pilot, not the full 12-language
FLORES-200 audit described in the paper blueprint. FLORES-200 and its
mirrors are gated on HuggingFace and require an authenticated token;
this pilot uses Tatoeba as an ungated substitute so the pipeline and
metrics can be validated before the full multilingual run.

Run: python run_fertility_pilot.py
"""

import json
import pandas as pd
import tiktoken
from transformers import AutoTokenizer
from datasets import load_dataset

TOKENIZERS = {
    "GPT-4/o200k": ("tiktoken", "o200k_base"),
    "XLM-R": ("hf", "xlm-roberta-base"),
    "NLLB": ("hf", "facebook/nllb-200-distilled-600M"),
    "BanglaBERT": ("hf", "csebuetnlp/banglabert"),
    "MuRIL": ("hf", "google/muril-base-cased"),
    "mT5": ("hf", "google/mt5-base"),
}

# USD per 1K input tokens (verify against current provider pricing before citing)
API_PRICING = {
    "GPT-4/o200k": 0.0025,
}


def load_tokenizer(kind, ident):
    if kind == "tiktoken":
        return tiktoken.get_encoding(ident)
    return AutoTokenizer.from_pretrained(ident, use_fast=True)


def encode_len(tok, kind, text):
    if kind == "tiktoken":
        return len(tok.encode(text))
    return len(tok.encode(text))


def count_words(text):
    return len(text.split())


def main():
    print("Loading Tatoeba ben-eng...")
    ds = load_dataset("Helsinki-NLP/tatoeba_mt", "ben-eng", trust_remote_code=True)
    split = ds["test"]

    ben_sentences = [r["sourceString"] for r in split if r["sourceLang"] == "ben"]
    eng_sentences = [r["targetString"] for r in split if r["sourceLang"] == "ben"]
    n = min(len(ben_sentences), len(eng_sentences))
    ben_sentences, eng_sentences = ben_sentences[:n], eng_sentences[:n]
    print(f"Parallel pairs available: {n}")

    rows = []
    for name, (kind, ident) in TOKENIZERS.items():
        print(f"Loading tokenizer: {name} ({ident})")
        try:
            tok = load_tokenizer(kind, ident)
        except Exception as e:
            print(f"  SKIP {name}: {e}")
            continue

        for lang, sentences in [("Bengali", ben_sentences), ("English", eng_sentences)]:
            total_tokens = 0
            total_words = 0
            total_bytes = 0
            for s in sentences:
                total_tokens += encode_len(tok, kind, s)
                total_words += count_words(s)
                total_bytes += len(s.encode("utf-8"))
            rows.append({
                "tokenizer": name,
                "language": lang,
                "n_sentences": len(sentences),
                "total_tokens": total_tokens,
                "total_words": total_words,
                "total_bytes": total_bytes,
                "fertility": total_tokens / total_words if total_words else None,
                "byte_efficiency": total_tokens / total_bytes if total_bytes else None,
            })

    df = pd.DataFrame(rows)

    eng_fert = df[df.language == "English"].set_index("tokenizer")["fertility"]
    df["token_premium"] = df.apply(
        lambda r: r["fertility"] / eng_fert.get(r["tokenizer"], float("nan"))
        if r["language"] == "Bengali" else 1.0,
        axis=1,
    )
    df["context_shrink_pct"] = df["token_premium"].apply(
        lambda p: (1 - 1 / p) * 100 if p and p > 0 else None
    )
    df["cost_premium_usd_per_1k"] = df.apply(
        lambda r: r["token_premium"] * API_PRICING.get(r["tokenizer"], float("nan"))
        if r["tokenizer"] in API_PRICING else None,
        axis=1,
    )

    out_csv = "results/study_a_pilot_results.csv"
    df.to_csv(out_csv, index=False)
    print(f"\nSaved: {out_csv}")

    print("\n=== BENGALI SUMMARY (pilot, Tatoeba, n={} pairs) ===".format(n))
    ben_rows = df[df.language == "Bengali"]
    print(ben_rows[["tokenizer", "fertility", "token_premium", "context_shrink_pct"]]
          .to_string(index=False))

    summary = {
        "corpus": "Helsinki-NLP/tatoeba_mt (ben-eng)",
        "n_parallel_pairs": n,
        "mean_token_premium": float(ben_rows["token_premium"].mean()),
        "mean_fertility_bengali": float(ben_rows["fertility"].mean()),
        "mean_context_shrink_pct": float(ben_rows["context_shrink_pct"].mean()),
        "note": "PILOT on single language pair (Bengali-English) via ungated Tatoeba corpus. "
                "Full study requires FLORES-200 (gated on HF) for 12-language parallel coverage.",
    }
    with open("results/study_a_pilot_summary.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
    print("\nSaved: results/study_a_pilot_summary.json")


if __name__ == "__main__":
    main()
