# ppt-chart-design

A Claude skill that helps non-designers turn data into professional, logically-complete
charts and infographics for PowerPoint, rendered as **high-fidelity images** in one of
five named designer styles.

The value is two systems: a **decision logic** (which chart, which style) plus a
**design system** distilled from professional reference work, encoded as machine-readable
design tokens.

## What it does

1. Forces a one-sentence message (which becomes the chart title) - one chart, one point.
2. Picks the chart type from intent + data shape (`references/chart-selection.md`).
3. Auto-recommends one of five styles from content/audience/density/tone
   (`references/style-selection.md`).
4. Applies seven data-storytelling principles on every chart
   (`references/data-storytelling-principles.md`).
5. Renders a high-fidelity image themed from `assets/design-tokens.json`
   (`scripts/render_chart.py`) and drops it into a slide (`scripts/build_pptx.py`).

## The five styles

| # | Style | Use it for |
|---|-------|-----------|
| 1 | Airy Systematic | Annual reports / policy - clean, calm, professional |
| 2 | Retro Editorial | Opinionated, eye-catching, illustration-rich |
| 3 | Metaphor Object | Viral / single punchy stat (an object becomes the chart) |
| 4 | Corporate Gradient | Safe neutral business default; process/structure diagrams |
| 5 | Magazine Monochrome | Deep single-topic data page, magazine authority |

Each style's palette was sampled pixel-by-pixel from reference works and stored in
`assets/design-tokens.json`. Styles 2-5 use generated illustrations.

## Structure

```
ppt-chart-design/
├── SKILL.md                  # workflow, decision logic, QC checklist
├── assets/design-tokens.json # palettes / fonts / illustration modes (machine-readable)
├── references/               # chart-selection, style-selection, 7 principles, 5 styles
└── scripts/                  # render_chart.py, build_pptx.py
```

## Requirements

```
pip install -r requirements.txt   # matplotlib, python-pptx, pillow, numpy
```

Optional fonts for full fidelity: Pretendard / Noto Sans CJK, Anton, Archivo Black,
Oswald, Poppins, Montserrat, Playfair Display, Inter. Without them, rendering falls back
to a default sans-serif.

## Quick start (scripts standalone)

```bash
python scripts/render_chart.py --style style_4_corporate_gradient --chart donut --out chart.png
python scripts/build_pptx.py --image chart.png --out deck.pptx --mode framed
```

## Using as a Claude skill

Install the packaged `.skill` file in a Claude product that supports skills, or point your
agent at this folder. The skill triggers when a user is making a deck and needs to present
data, asks for a chart/infographic, or says their charts "don't look good".

## Design ethics

This skill extracts **design approach and style, not content**. Generated illustrations
and metaphor objects must be generic and non-branded - no copyrighted characters or
logos, no real identifiable people - and conceptual titles must be original. See the
guardrails in `SKILL.md` and the per-style reference files.

## License

MIT - see [LICENSE](LICENSE). Replace `[Your Name]` in the license with your name.
