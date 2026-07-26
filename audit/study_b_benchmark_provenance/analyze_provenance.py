"""
Study B - Benchmark Provenance Audit
Analyzes benchmark_catalog.csv and produces provenance distribution
statistics and a stacked-bar figure for the paper (Figure 7 / Section 10).

Run: python analyze_provenance.py
"""

import json
import pandas as pd
import matplotlib.pyplot as plt

CODE_LABELS = {
    "N": "Native-authored",
    "H": "Human-translated",
    "M": "Machine-translated",
    "Mixed": "Mixed / inherited",
}


def simplify_code(code: str) -> str:
    code = code.strip()
    if code.startswith("N") and "Mixed" not in code and "/" not in code:
        return "N"
    if code.startswith("H") and "Mixed" not in code and "/" not in code:
        return "H"
    if code.startswith("M") and "Mixed" not in code and "/" not in code and not code.startswith("Mixed"):
        return "M"
    return "Mixed"


def main():
    df = pd.read_csv("benchmark_catalog.csv")
    df["simple_code"] = df["provenance_code"].apply(simplify_code)

    counts = df["simple_code"].value_counts()
    pct = (counts / len(df) * 100).round(1)

    print(f"Total benchmarks catalogued: {len(df)}")
    print("\nProvenance distribution:")
    for code in ["N", "H", "M", "Mixed"]:
        c = counts.get(code, 0)
        p = pct.get(code, 0.0)
        print(f"  {CODE_LABELS[code]:20s} ({code}): {c:2d} benchmarks ({p}%)")

    non_native_pct = 100 - pct.get("N", 0.0)
    print(f"\nShare NOT purely native-authored (H + M + Mixed): {non_native_pct:.1f}%")

    low_conf = df[df["confidence"] == "low"]
    print(f"\nLow-confidence entries needing further verification: {len(low_conf)}")
    print(low_conf[["benchmark", "provenance_code"]].to_string(index=False))

    # Figure: stacked bar of provenance share
    fig, ax = plt.subplots(figsize=(7, 4))
    order = ["N", "H", "M", "Mixed"]
    values = [counts.get(c, 0) for c in order]
    colors = ["#1a9850", "#fee08b", "#d73027", "#999999"]
    ax.bar([CODE_LABELS[c] for c in order], values, color=colors)
    for i, v in enumerate(values):
        ax.text(i, v + 0.3, str(v), ha="center", fontweight="bold")
    ax.set_ylabel("Number of benchmarks")
    ax.set_title(
        f"Provenance of {len(df)} South-Asian-language NLP benchmarks\n"
        f"(N cataloged = {len(df)}; {non_native_pct:.0f}% not purely native-authored)",
        fontsize=11, fontweight="bold",
    )
    plt.tight_layout()
    plt.savefig("figure7_provenance.pdf", bbox_inches="tight", dpi=300)
    plt.savefig("figure7_provenance.png", bbox_inches="tight", dpi=300)
    print("\nSaved figure7_provenance.pdf / .png")

    summary = {
        "total_benchmarks": len(df),
        "counts": {CODE_LABELS[c]: int(counts.get(c, 0)) for c in order},
        "percentages": {CODE_LABELS[c]: float(pct.get(c, 0.0)) for c in order},
        "pct_not_native": round(non_native_pct, 1),
        "low_confidence_entries": low_conf["benchmark"].tolist(),
        "note": (
            "Catalog built from web-verified sources (arXiv/ACL Anthology/HF dataset "
            "cards/GitHub) as of 2026-07; entries marked confidence=low or medium need "
            "direct primary-source re-verification before final submission."
        ),
    }
    with open("study_b_summary.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
    print("Saved study_b_summary.json")


if __name__ == "__main__":
    main()
