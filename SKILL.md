---
name: ppt-chart-design
description: >
  Design professional, logically-complete charts and infographics for PowerPoint
  in one of five named designer styles, and render them as high-fidelity images to
  drop into slides. Use this skill whenever the user is making a PPT/deck and needs
  to present data, asks for a chart/graph/infographic, says their charts "look
  unprofessional" or "don't look good", asks "how should I show this data", or
  uploads numbers that need visualizing for a presentation - even if they don't
  explicitly say the word "chart". Also use when the user asks to apply a specific
  visual style to a data graphic.
---

# PPT Chart Design

Helps non-designers turn data into professional, well-reasoned charts for PowerPoint.
The value is two systems: (1) a decision logic for **which chart** and **which style**,
and (2) a faithful **design system** distilled from five professional designers.

Output mode (fixed): **high-fidelity images**. Charts are rendered to PNG/SVG at high
DPI and inserted into the slide as pictures - pixel-faithful to the design, but not
editable as native PPT chart objects. Tell the user this trade-off if relevant.

## Workflow (follow in order)

1. **State the message first.** Write one sentence: what should the audience conclude?
   That sentence becomes the chart title. One chart = one point. If the user only gave
   raw data, infer the likely message and confirm briefly. If the message is a single
   number, attach a comparison (see principle 1 below) - a lone number is never enough.

2. **Pick the chart type.** Read `references/chart-selection.md`. It is a two-level
   decision: intent (comparison / trend / composition / KPI / table / deviation /
   flow / distribution / relationship / geo) -> then data shape (how many categories /
   series / time). Pick the leaf recommendation. Never choose by what looks familiar.

3. **Pick the style (auto-recommend).** Read `references/style-selection.md` and choose
   ONE of the five styles from the content type, audience, density, and tone. Only ask
   the user if it is genuinely ambiguous. State the chosen style in one line.

4. **Load that style's spec + tokens.** Read the matching `references/style-N-*.md` and
   pull its palette/fonts from `assets/design-tokens.json`. Do not mix styles within
   one chart.

5. **Render the chart as a high-fidelity image.** Use `scripts/render_chart.py`, which
   themes matplotlib from the tokens (palette, fonts, grid/spine rules). For styles that
   require illustration (2, 3, 4, 5) also generate the illustration (see below) and
   composite it. Output PNG (raster) or SVG.

6. **Assemble into PPTX.** Use `scripts/build_pptx.py` to place the rendered image on a
   16:9 slide (full-bleed or framed per style). Save to the outputs directory.

7. **Run the QC checklist** (bottom of this file) before presenting.

## Data-storytelling principles (apply on every chart)

Before rendering (step 5), apply the seven principles in
`references/data-storytelling-principles.md`. They govern *how the data is told* and
override nothing in the styles - they sit on top. In short:

1. Never show a single number alone - give it a comparison (history > benchmark > stated
   best guess), apples-to-apples (quarter vs quarter, not vs YTD).
2. One focus per chart - highlight one element; if multiple datasets, reveal in stages.
3. Use color for contrast and to encode meaning (older=light, recent=dark, current/own=
   brand color, forecast=lighter), drawing colors from the chosen style's tokens.
4. Keep formatting consistent across all charts in one request (same highlight, same sort).
5. For proposals / investment asks, offer a two-scenario comparison with an annotation
   label naming the lever - dramatize the cost of inaction.
6. Use the right chart type and don't manipulate it (pie only <=3 + one dominant; line
   axis from zero, label any zoom; waterfall to show how one number becomes another).
7. Add a status sticker when data is draft/early/placeholder: WIP / Discussion /
   Preliminary / Illustrative.

## The five styles (one-line identities)

Full specs in `references/`. Pick via `references/style-selection.md`.

1. **Airy Systematic** (`style-1`) - minimal, white space, mint-teal + coral, alpha
   overlays. For annual reports / policy: "professional and calm".
2. **Retro Editorial** (`style-2`) - high-contrast, grid rules, riso/flat illustration,
   one of 5 muted recipes. For "opinionated, eye-catching".
3. **Metaphor Object** (`style-3`) - cream background, a real object IS the chart,
   witty original title. For "viral / single punchy stat".
4. **Corporate Gradient** (`style-4`) - blue->purple gradient, flat, rounded, structure
   diagrams. The safe, neutral business default.
5. **Magazine Monochrome** (`style-5`) - one hue per page + tints, richest chart variety,
   isometric pictograms, magazine masthead. For "deep single-topic data page".

## Illustration handling (styles 2-5)

These styles need generated illustration. When the chosen style's token `illustration.mode`
is `"generate"`:

- Build a list of needed illustrations (e.g. 1 hero object + N spot icons).
- Generate each with the **image-generation tool**, using the style's
  `illustration.prompt_fragment` from the tokens so palette and look stay consistent.
- Generate a whole set with ONE fixed style fragment + ONE palette so the deck is
  coherent; then de-background and composite at the positions the style dictates.
- If no image-generation tool is available, fall back: icon library + isotype + large
  numbers + texture blocks (the layout still reads as the style).

## Copyright & safety guardrails (always)

We extract **design approach and style, never content**:

- Illustrations and metaphor objects must be **generic, non-branded**: no copyrighted
  characters, logos, or licensed IP; **no real identifiable people**.
- Witty/conceptual titles must be **original wordplay** - never reproduce song lyrics,
  film quotes, or other copyrighted lines.
- Do not reproduce a specific published infographic; rebuild palettes/layouts as
  original templates.

## QC checklist (before presenting)

- [ ] Title states a conclusion, not just a topic; one chart = one point.
- [ ] No lone number without a comparison (history / benchmark / labeled best guess), and
      comparisons are apples-to-apples (same time span).
- [ ] Exactly one focal element highlighted; multiple datasets revealed in stages.
- [ ] Color encodes meaning consistently (recency/ownership); same highlight + sort order
      reused across all charts in this request.
- [ ] Chart type matches the intent + data shape (per chart-selection).
- [ ] Exactly one style applied; palette/fonts pulled from tokens (not improvised).
- [ ] Bars sorted by value (not alphabetical) where ranking matters; bar axis from 0;
      no zoomed line axis without a clear label.
- [ ] Proposal/investment framing offers a two-scenario comparison with an annotation.
- [ ] Direct labels used where possible; legend only if necessary.
- [ ] No chartjunk: no stray gridlines/3D/shadow unless the style calls for it.
- [ ] Source/unit noted; numbers sensibly rounded.
- [ ] Draft/early/placeholder data carries a status sticker (WIP/Discussion/Preliminary/
      Illustrative).
- [ ] Any illustration is generic (no IP / no real people); title is original.
- [ ] Rendered at high DPI; placed cleanly on the slide; text legible at slide size.

## Files

- `references/chart-selection.md` - intent -> chart type (two-level table)
- `references/data-storytelling-principles.md` - the 7 principles applied on every chart
- `references/style-selection.md` - data/scenario -> one of 5 styles (auto-recommend)
- `references/style-1-airy-systematic.md` ... `style-5-magazine-monochrome.md`
- `assets/design-tokens.json` - all palettes/fonts/illustration modes (machine-readable)
- `scripts/render_chart.py` - theme matplotlib from tokens, render PNG/SVG
- `scripts/build_pptx.py` - place rendered image(s) into a PPTX slide
