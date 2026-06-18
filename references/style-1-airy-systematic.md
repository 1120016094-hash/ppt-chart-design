# Style 1 - Airy Systematic (清透系统信息图)

**Identity:** editorial, airy, systematic. Heavy white space, soft alpha overlays,
rounded organic forms. For annual reports / policy / brand data stories that must look
"professional and calm".

**Palette (tokens: `style_1_airy_systematic`)**
- Main `#4DCABE`, Key `#087C95`, Accent `#FDB697` (the only warm accent).
- Categorical: 087C95 -> 4DCABE -> 46508A -> FDB697 -> B2DBDD.
- Sequential (one intent, depth = magnitude): 087C95 -> 4DCABE -> B2DBDD -> E0F1F1.
- Fallback background white `#FEFFFF` or faint `#E8EDFB`->white gradient. Text `#3A4A4F`,
  grid `#E0E3E8`, muted `#B1BAC4`.
- If this chart is part of a PPT workflow, inherit the deck/slide background plan first.
  On non-white backgrounds, preserve the airy systematic feel through transparent overlays,
  restrained grey/teal/coral contrast, and generous whitespace rather than forcing a white
  rectangle.

**Type:** Pretendard / Noto Sans (free). Title bold, **tracking -2px (tight)**, states a
conclusion. Top-left kicker in teal = chart type name; small grey unit/source beneath.

**Layout / subtraction:** no chart border, no gridlines (line charts may keep one faint
dashed reference), no 3D/shadow, no legend (direct-label instead). Tables: only thin
horizontal rules, header on pale lilac. Asymmetric (text block + figure), lots of air.

**Focus:** alpha overlays so overlaps deepen naturally (arcs, bubbles, radar);
directional elements use gradient fills; one coral note among the teals.

**Illustration:** none - uses overlays/gradients, not generated art.

## Execution rules from references

- Use Style 1 references for systematic spacing, translucent overlays, direct labels, and
  clean chart/table hierarchy only; do not copy a reference composition verbatim.
- Style 1 does not use generated illustration, but its abstract visual forms still need a
  data role. Bubbles, arcs, routes, translucent blocks, and flow shapes must encode,
  group, compare, or guide the reader through the data. Do not add decorative translucent
  shapes that could be removed without changing the data reading.
- Translucent overlays are not allowed to share unmeasured space with readable text. Large
  KPI numbers, units, source notes, category labels, value labels, and sparkline endpoint
  labels each need clean lanes. Arcs, bubbles, route strokes, ambient circles, and
  sparkline dots must be registered as collision-relevant graphics and kept out of those
  lanes unless the label is deliberately embedded with verified padding and contrast.
- If an airy overlay or arc conflicts with a focal number, remove or relocate the overlay
  rather than letting it cross behind the digits. Style 1's "transparent overlap" language
  applies to graphic-to-graphic relationships, not to graphic-over-text accidents.
- Style 1 is a basic option, so its generation logic is clarity-first. Choose the clearest
  chart/diagram structure, sorting, scale, label lanes, unit treatment, and whitespace
  before adding airy overlays or decorative rhythm. The page should feel designed, but the
  viewer must understand the data faster because of the design.
- When this style is used inside a PPT workflow, inherit the PPT background first. If the
  inherited background is not white, keep the airy feel with low-opacity panels/overlays
  and adjusted text contrast instead of placing a hard white page rectangle.
- Typography must stay quiet and spacious: title, subtitle, unit, and source each need a
  clear size step and breathing room. Long Chinese subtitles must wrap rather than run as
  dense single lines.
- Follow the global frontend-design typography rules in `SKILL.md`: every repeated data
  module needs a measured text-stack contract and the page needs a typographic alignment
  spine. In this airy style, the spine should feel calm and spacious: title, subtitles,
  direct labels, values, units, and sources align to declared lanes rather than drifting
  by optical guesswork.
- Information hierarchy must be expressed through the whole canvas, not only through
  chart choice. When the layout is airy/asymmetric rather than gridded, allocate visual
  territory by hierarchy: the main finding gets the clearest plotted area and strongest
  contrast, secondary evidence gets lighter/smaller overlays, and notes/context remain
  small and quiet. Same-level metrics should keep comparable scale, opacity, label weight,
  and spacing.
- When source data matches a reference-like structure, translate that structure before
  defaulting to a generic chart. For example, route/process data should use a clean
  process-route or flow-map treatment; overlapping relationships should use translucent
  overlays or chord-like logic; timeline data should use airy bubble/arc sequencing when
  that better clarifies the story.
- Direct labels and leader lines must attach to the exact plotted mark, arc, bubble, route,
  row, or overlay region they describe, and the opposite endpoint must attach to the
  corresponding label/text group. Labels and connectors must not float near unrelated
  geometry.
- Data encoding must stay exact after rendering. Line positions, bar lengths, bubble/arc
  sizes, table values, overlay areas, colors, and direct-label anchors must be checked
  against the source numbers. Airy spacing and translucency may clarify hierarchy, but
  must not change the implied value, ranking, share, or comparison.
- Keep the airy page simple by expressing each metric once. A bubble timeline should not
  repeat the same year/value series as a full side table; a translucent overlay diagram
  should not be duplicated by a separate complete bar chart. Use labels, selected notes,
  source lines, or a few event callouts for precision and context instead of restating the
  full dataset.
- If boxed notes/tables/KPI cells are used, text must sit on the optical centerline with
  balanced padding; avoid text hugging borders.
- If a summary strip combines explanation, proportion marks, percentages, formulas, or
  totals, follow the composite-module subgrid rules in `SKILL.md`; keep explanation,
  graphics, and numeric verification in declared zones with measured text spacing.
- Output both PNGs: the complete version with all labels/data, and a clean version with
  the same inherited/fallback background, plotted marks, overlays, direct-label leader
  lines, table rules, KPI/card frames, colors, and non-text visual structure. The clean
  version removes only readable text and numbers; it must not neutralize, recolor, resize,
  or replace data-bearing marks from the complete version.

## User reference images

Use the local files in `../assets/style-1-airy-systematic-references/` as style direction
for this style. They are references for the visual language, not templates to copy.

Available references:
- `preview-chart-table-line.webp` - chart/table/line examples.
- `preview-bubble-timeline.webp` - bubble timeline with translucent circles.
- `preview-arc-diagram.webp` - arc diagram with layered alpha strokes.
- `preview-flowmap-chord.webp` - flow map and chord diagram treatment.
- `preview-process-route-map.webp` - process and route map treatment.

When applying these references, preserve the Style 1 traits: white/near-white fallback
background or inherited PPT background, teal key labels, restrained grey body text,
clean sans type, generous whitespace,
transparent overlapping shapes, direct labels, minimal legends, and systematic diagram
logic. Do not add generated hero illustration for Style 1; it should stay diagrammatic.
