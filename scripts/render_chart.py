#!/usr/bin/env python3
"""Render a high-fidelity chart image themed by design-tokens.json.

This is a STARTER. It themes matplotlib from the style tokens and ships demo
renderers for bar / line / donut. Extend with more chart types and, for styles
whose token illustration.mode == "generate", composite generated illustrations
on top (see SKILL.md). Default skill output is PNG-only: one complete annotated
PNG and one clean PNG that removes only readable text/numbers while preserving
non-text visuals and data-bearing marks. This starter script renders a single PNG per
call; orchestration code should call/render twice or hide annotations for the clean
version.

Usage:
    python render_chart.py --style style_1_airy_systematic --chart bar --out out.png
    python render_chart.py --style style_4_corporate_gradient --chart donut --out out.png
"""
import argparse, json, os
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.colors import LinearSegmentedColormap
import numpy as np

TOKENS = json.loads((Path(__file__).resolve().parent.parent / "assets" / "design-tokens.json").read_text())


def _first_available_font(families):
    installed = {f.name for f in font_manager.fontManager.ttflist}
    for fam in families:
        if fam in installed:
            return fam
    return "DejaVu Sans"  # safe fallback present in matplotlib


def _palette(style):
    """Return (bg, text, categorical_colors, gradient_or_none) for a style key."""
    t = TOKENS[style]
    if style == "style_1_airy_systematic":
        return t["background"], t["text"], t["categorical"], None
    if style == "style_4_corporate_gradient":
        return t["background"], t["text"], None, t["gradient"]
    if style == "style_2_retro_editorial":
        r = t["recipes"]["B_powder"]
        return r["bg"], r["black"], [r["accent1"], r["accent2"], r.get("pink", "#888"), r["black"]], None
    if style == "style_3_metaphor_object":
        return t["background"], t["text"], [t["red"], t["indigo"], t["red_dark"], t["indigo_dark"]], None
    if style == "style_5_magazine_monochrome":
        r = t["recipes"]["cobalt"]
        base = r["dominant"]
        tints = _tints(base, 5)
        return base, r["title"], tints, None
    raise ValueError(style)


def _tints(hex_color, n):
    """n tints/shades of one hue (light->dark) for monochrome styles."""
    c = np.array([int(hex_color[i:i + 2], 16) for i in (1, 3, 5)]) / 255
    out = []
    for f in np.linspace(0.85, 0.25, n):  # mix toward white then darken
        mixed = c * f + (1 - f)  # lighten
        out.append("#%02X%02X%02X" % tuple(int(v * 255) for v in mixed))
    return out


def _apply_base_theme(style):
    bg, text, _, _ = _palette(style)
    t = TOKENS[style]
    fonts = t.get("fonts", {})
    fam = _first_available_font(fonts.get("title", ["DejaVu Sans"]))
    cr = t.get("chart_rules", {})
    plt.rcParams.update({
        "figure.facecolor": bg,
        "axes.facecolor": bg,
        "savefig.facecolor": bg,
        "text.color": text,
        "axes.labelcolor": text,
        "xtick.color": text,
        "ytick.color": text,
        "font.family": fam,
        "axes.edgecolor": t.get("grid", "#CCCCCC"),
        "axes.grid": bool(cr.get("grid", False)),
        "grid.color": t.get("grid", "#E0E3E8"),
    })
    return bg, text, fam, cr


def render_bar(style, labels, values, title, out, sort_desc=True):
    bg, text, cats, grad = _palette(style)
    bg2, text2, fam, cr = _apply_base_theme(style)
    if sort_desc:
        order = np.argsort(values)[::-1]
        labels = [labels[i] for i in order]; values = [values[i] for i in order]
    fig, ax = plt.subplots(figsize=(10, 6), dpi=200)
    if grad:  # gradient bars (style 4)
        cmap = LinearSegmentedColormap.from_list("g", grad)
        colors = [cmap(i / max(len(values) - 1, 1)) for i in range(len(values))]
    else:
        colors = (cats * ((len(values) // len(cats)) + 1))[:len(values)]
    bars = ax.bar(labels, values, color=colors, width=0.7,
                  zorder=3, edgecolor="none")
    ax.set_title(title, loc="left", fontsize=20, fontweight="bold", pad=18)
    if not cr.get("spines", True):
        for s in ax.spines.values():
            s.set_visible(False)
    ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
    ax.tick_params(length=0)
    ax.set_ylim(0, max(values) * 1.18)
    for b, v in zip(bars, values):  # direct labels
        ax.text(b.get_x() + b.get_width() / 2, v + max(values) * 0.02,
                f"{v:g}", ha="center", va="bottom", fontsize=12, fontweight="bold")
    if not cr.get("grid", False):
        ax.set_yticks([])
    fig.tight_layout()
    fig.savefig(out, bbox_inches="tight")
    plt.close(fig)
    return out


def render_line(style, x, series, title, out):
    bg, text, cats, grad = _palette(style)
    _apply_base_theme(style)
    cats = cats or [grad[0], grad[-1]]
    fig, ax = plt.subplots(figsize=(10, 6), dpi=200)
    for i, (name, ys) in enumerate(series.items()):
        c = cats[i % len(cats)]
        ax.plot(x, ys, color=c, lw=3, marker="o", ms=5, zorder=3)
        ax.text(x[-1], ys[-1], "  " + name, color=c, va="center",
                fontsize=12, fontweight="bold")  # direct label at line end
    ax.set_title(title, loc="left", fontsize=20, fontweight="bold", pad=18)
    ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
    ax.tick_params(length=0)
    fig.tight_layout(); fig.savefig(out, bbox_inches="tight"); plt.close(fig)
    return out


def render_donut(style, labels, values, title, out):
    bg, text, cats, grad = _palette(style)
    _apply_base_theme(style)
    if grad:
        cmap = LinearSegmentedColormap.from_list("g", grad)
        colors = [cmap(i / max(len(values) - 1, 1)) for i in range(len(values))]
    else:
        colors = (cats * ((len(values) // len(cats)) + 1))[:len(values)]
    fig, ax = plt.subplots(figsize=(8, 8), dpi=200)
    w, _, at = ax.pie(values, colors=colors, startangle=90, counterclock=False,
                      wedgeprops=dict(width=0.42, edgecolor=bg, linewidth=2),
                      autopct=lambda p: f"{p:.0f}%", pctdistance=0.79,
                      textprops=dict(color="white", fontsize=11, fontweight="bold"))
    ax.set_title(title, loc="center", fontsize=20, fontweight="bold", y=1.02)
    ax.legend(w, labels, loc="center", frameon=False, fontsize=10)
    fig.savefig(out, bbox_inches="tight"); plt.close(fig)
    return out


DEMO = {
    "bar": dict(labels=["A", "B", "C", "D"], values=[38, 27, 19, 11], title="Sales lead grows in region A"),
    "donut": dict(labels=["Comp", "Servers", "Phones", "Other"], values=[41, 27, 19, 13], title="Where chips go"),
    "line": dict(x=[2019, 2020, 2021, 2022, 2023], series={"Dem": [46, 39, 36, 31, 44], "Rep": [32, 20, 12, 13, 13]}, title="Positive views diverge"),
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--style", required=True, choices=list(TOKENS.keys())[1:])
    ap.add_argument("--chart", required=True, choices=["bar", "line", "donut"])
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    d = DEMO[a.chart]
    if a.chart == "bar":
        render_bar(a.style, d["labels"], d["values"], d["title"], a.out)
    elif a.chart == "donut":
        render_donut(a.style, d["labels"], d["values"], d["title"], a.out)
    else:
        render_line(a.style, d["x"], d["series"], d["title"], a.out)
    print("wrote", a.out)


if __name__ == "__main__":
    main()
