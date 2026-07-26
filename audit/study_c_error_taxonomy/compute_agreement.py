"""
Study C - Native-Speaker Error Taxonomy: Agreement & Correlation Analysis

Run AFTER at least 3 annotators have independently filled in copies of
annotations_template.csv (named annotations_r1.csv, annotations_r2.csv,
annotations_r3.csv in this directory).

Computes:
  1. Fleiss' kappa per error code (binary present/absent per annotator)
  2. Overall Fleiss' kappa across all codes pooled
  3. (Optional) Spearman correlation between automatic metric scores
     and per-output total error counts, if a metrics CSV is supplied.

Run: python compute_agreement.py
"""

import glob
import json
import numpy as np
import pandas as pd
import krippendorff

ERROR_CODES = ["E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8", "E9"]


def fleiss_kappa_binary(ratings: np.ndarray) -> float:
    """
    ratings: (n_items, n_raters) binary matrix (0/1) for ONE error code.
    Standard Fleiss' kappa for two categories (present/absent) with a
    fixed number of raters per item.
    """
    n_items, n_raters = ratings.shape
    n_present = ratings.sum(axis=1)
    n_absent = n_raters - n_present

    p_i = (n_present * (n_present - 1) + n_absent * (n_absent - 1)) / (n_raters * (n_raters - 1))
    P_bar = p_i.mean()

    p_present = n_present.sum() / (n_items * n_raters)
    p_absent = 1 - p_present
    P_e = p_present**2 + p_absent**2

    if P_e == 1:
        return 1.0
    return (P_bar - P_e) / (1 - P_e)


def load_annotator_files():
    files = sorted(glob.glob("annotations_r*.csv"))
    if len(files) < 2:
        raise FileNotFoundError(
            "Need at least 2 files named annotations_r1.csv, annotations_r2.csv, "
            "(annotations_r3.csv, ...) in this directory. Copy annotations_template.csv "
            "per annotator and fill in 0/1 for each error code before running this script."
        )
    return files


def main():
    files = load_annotator_files()
    print(f"Found {len(files)} annotator files: {files}")

    dfs = [pd.read_csv(f).sort_values("output_id").reset_index(drop=True) for f in files]
    n_items = len(dfs[0])
    for d in dfs:
        assert len(d) == n_items, "All annotator files must cover the same output_ids"

    print(f"\n{'Code':<6}{'Fleiss kappa':>15}{'Interpretation':>20}")
    kappas = {}
    for code in ERROR_CODES:
        mat = np.stack([d[code].fillna(0).astype(int).values for d in dfs], axis=1)
        k = fleiss_kappa_binary(mat)
        kappas[code] = k
        if k >= 0.80:
            interp = "almost perfect"
        elif k >= 0.60:
            interp = "substantial"
        elif k >= 0.40:
            interp = "moderate"
        elif k >= 0.20:
            interp = "fair"
        else:
            interp = "poor/slight"
        print(f"{code:<6}{k:>15.3f}{interp:>20}")

    # Pooled kappa across all codes (stack all code-columns as separate "items")
    all_mats = []
    for code in ERROR_CODES:
        mat = np.stack([d[code].fillna(0).astype(int).values for d in dfs], axis=1)
        all_mats.append(mat)
    pooled = np.concatenate(all_mats, axis=0)
    pooled_kappa = fleiss_kappa_binary(pooled)
    print(f"\nPooled Fleiss' kappa (all codes): {pooled_kappa:.3f}")
    print("Target for the paper: >= 0.70")

    # Total error count per output (averaged across annotators) for optional
    # correlation with automatic metrics, if a metrics file is supplied.
    total_errors = np.mean(
        [d[ERROR_CODES].fillna(0).astype(int).sum(axis=1).values for d in dfs], axis=0
    )
    out = pd.DataFrame({"output_id": dfs[0]["output_id"], "mean_total_errors": total_errors})
    out.to_csv("error_counts_per_output.csv", index=False)
    print("\nSaved error_counts_per_output.csv (for metric-correlation analysis)")

    summary = {
        "n_annotator_files": len(files),
        "n_items": int(n_items),
        "per_code_kappa": {k: round(v, 3) for k, v in kappas.items()},
        "pooled_kappa": round(pooled_kappa, 3),
    }
    with open("agreement_summary.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)
    print("Saved agreement_summary.json")


if __name__ == "__main__":
    main()
