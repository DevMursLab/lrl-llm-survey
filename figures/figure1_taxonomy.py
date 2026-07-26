"""
Figure 1 - The LRL-LLM Lifecycle Taxonomy (6-layer signature figure)

Generates a vector (PDF/SVG) diagram of the six-layer taxonomy for
Section 5 of the manuscript. Colorblind-safe palette (ColorBrewer
sequential blues), >=8pt font, captions handled separately in LaTeX.

Run: python figure1_taxonomy.py
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch

LAYERS = [
    ("L1", "Script & Encoding Substrate",
     "Unicode normalization (NFC/NFD) - conjunct-consonant handling -\nZWJ/ZWNJ - script variants - OCR quality - romanization"),
    ("L2", "Data Acquisition & Curation",
     "Web-crawl quality (mC4/OSCAR/CulturaX) - noise & dedup -\nsynthetic data - community sourcing - data sovereignty"),
    ("L3", "Tokenization & Representation",
     "Fertility - token premium - vocabulary allocation -\nBPE vs. Unigram vs. byte-level - vocabulary expansion"),
    ("L4", "Adaptation & Transfer",
     "Continued pretraining - cross-lingual transfer - PEFT/LoRA -\ninstruction tuning - multilingual RLHF/DPO - distillation"),
    ("L5", "Evaluation & Measurement",
     "Native vs. translated benchmarks - translationese -\ncontamination - LLM-as-judge validity - metric transferability"),
    ("L6", "Deployment, Equity & Governance",
     "Inference cost asymmetry - latency - safety gaps -\nannotator labor ethics - dialect erasure - policy"),
]

# ColorBrewer sequential blues (colorblind-safe), one shade per layer
COLORS = ["#eff3ff", "#c6dbef", "#9ecae1", "#6baed6", "#3182bd", "#08519c"]
TEXT_COLORS = ["#08306b"] * 3 + ["#ffffff"] * 3

def main():
    fig, ax = plt.subplots(figsize=(9, 12.5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, len(LAYERS) * 2 + 2.8)
    ax.axis("off")

    box_h = 1.7
    gap = 0.3
    title_space = 1.8
    y = len(LAYERS) * (box_h + gap) + title_space

    for i, (code, title, detail) in enumerate(LAYERS):
        y -= (box_h + gap)
        box = FancyBboxPatch(
            (0.3, y), 9.4, box_h,
            boxstyle="round,pad=0.02,rounding_size=0.08",
            linewidth=1.2, edgecolor="#08306b",
            facecolor=COLORS[i], zorder=2,
        )
        ax.add_patch(box)

        ax.text(0.7, y + box_h - 0.35, code, fontsize=15, fontweight="bold",
                 color=TEXT_COLORS[i], va="top", ha="left", zorder=3)
        ax.text(1.7, y + box_h - 0.35, title, fontsize=12.5, fontweight="bold",
                 color=TEXT_COLORS[i], va="top", ha="left", zorder=3)
        ax.text(1.7, y + box_h - 0.75, detail, fontsize=8.7,
                 color=TEXT_COLORS[i], va="top", ha="left", zorder=3,
                 linespacing=1.4)

        # Downward arrow between layers (pipeline flow)
        if i < len(LAYERS) - 1:
            ax.annotate(
                "", xy=(5, y - gap * 0.15), xytext=(5, y),
                arrowprops=dict(arrowstyle="-|>", color="#4a4a4a", lw=1.4),
                zorder=1,
            )

    top = len(LAYERS) * (box_h + gap) + title_space
    ax.text(5, top + 0.9,
             "The LRL-LLM Lifecycle Taxonomy",
             fontsize=15, fontweight="bold", ha="center", color="#08306b")
    ax.text(5, top + 0.4,
             "Six pipeline-stage layers, each a distinct locus of measurable harm for low-resource languages",
             fontsize=9.5, ha="center", style="italic", color="#333333")

    plt.tight_layout()
    plt.savefig("figure1_taxonomy.pdf", bbox_inches="tight", dpi=300)
    plt.savefig("figure1_taxonomy.svg", bbox_inches="tight")
    plt.savefig("figure1_taxonomy.png", bbox_inches="tight", dpi=300)
    print("Saved figure1_taxonomy.pdf / .svg / .png")


if __name__ == "__main__":
    main()
