# ppt-chart-design

A Claude skill that helps non-designers turn data into professional, logically-complete
charts and infographics for presentation slides, rendered as **high-fidelity PNG images**
in one of five named designer styles.

The value is three systems: a **decision logic** (which chart, which style), a
**design system** distilled from professional reference work, and a `frontend-design`
inspired aesthetic layer that raises typography, color, composition, and visual-detail
standards for static infographic PNGs.

## What it does

1. Forces a one-sentence message (which becomes the chart title) - one chart, one point.
2. Picks the chart type from intent + data shape (`references/chart-selection.md`).
3. Auto-recommends one grouped basic/upgrade style from content/audience/density/tone
   (`references/style-selection.md`).
4. Applies seven data-storytelling principles on every chart
   (`references/data-storytelling-principles.md`).
5. Applies a `frontend-design` aesthetic pass so the image has a clear point-of-view and
   avoids generic dashboard/template looks.
6. Renders two high-fidelity PNG images themed from `assets/design-tokens.json`
   (`scripts/render_chart.py`): a complete annotated version and a clean version that
   removes only readable text/numbers while preserving all non-text visuals and
   data-bearing marks.

When this skill runs inside a larger PPT workflow, it inherits the deck/slide background
plan first. Style background colors are fallback defaults only.

Generation logic is split by option group:

- Basic options prioritize clarity: choose the chart/diagram structure first, then polish.
- Upgrade options require image generation first: turn the data theme and numeric
  relationship into a data-bearing illustration, then compose the final infographic around
  that illustration with exact labels and auxiliary data.

## Style options

| Group | # | Style | Use it for |
|---|---|-------|-----------|
| Basic | 1 | Airy Systematic | Annual reports / policy - clean, calm, professional |
| Basic | 2 | Corporate Gradient | Safe neutral business default; process/structure diagrams |
| Upgrade (requires image generation) | 3 | Retro Editorial | Opinionated, eye-catching, illustration-rich |
| Upgrade (requires image generation) | 4 | Metaphor Object | Viral / single punchy stat (an object becomes the chart) |
| Upgrade (requires image generation) | 5 | Magazine Monochrome | Deep single-topic data page, magazine authority |

Each style's palette was sampled pixel-by-pixel from reference works and stored in
`assets/design-tokens.json`. Upgrade options use generated illustrations. Corporate
Gradient can optionally use image generation for a custom gradient vector asset when the
user or data concept requires it.

## Structure

```
ppt-chart-design/
├── SKILL.md                  # workflow, decision logic, QC checklist
├── assets/design-tokens.json # palettes / fonts / illustration modes (machine-readable)
├── references/               # chart-selection, style-selection, 7 principles, 5 styles
└── scripts/                  # render_chart.py; build_pptx.py is legacy optional
```

## Requirements

```
pip install -r requirements.txt   # matplotlib, pillow, numpy; python-pptx only for legacy PPTX export
```

Optional fonts for full fidelity: Pretendard / Noto Sans CJK, Anton, Archivo Black,
Oswald, Poppins, Montserrat, Playfair Display, Inter. Without them, rendering falls back
to a default sans-serif.

## Quick start (scripts standalone)

```bash
python scripts/render_chart.py --style style_4_corporate_gradient --chart donut --out chart.png
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
