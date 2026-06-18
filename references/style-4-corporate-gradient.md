# Style 4 - Corporate Gradient (企业渐变模板信息图)

**Identity:** clean, neutral, reusable business infographic. Flat vector, rounded,
glossy, one blue->purple gradient on an inherited PPT background or white fallback. Best
for **concept/structure** content (process, cycle, hierarchy, relationship, timeline, map)
rather than precise data charts. The safe default.

**Palette (tokens: `style_4_corporate_gradient`):** signature linear gradient
**#00A0FA -> #5064FA -> #6E14AA** (~135deg) fills almost every shape. Fallback background
`#F8F8F8`.
Icons reversed white. Title `#333`/gradient blue, body muted `#8A8A8A`. **No second hue** -
levels come from gradient depth/lightness, which gives the unified corporate feel.
If a PPT workflow supplies a deck/slide background, inherit it and adjust shadows,
contrast, card fills, and text color so the gradient system sits natively on that slide.
Do not force a white dashboard block unless the PPT design system calls for white cards.

**Type:** Poppins / Montserrat (free). Two-tone title (one word black, one gradient blue).
Step numbers 01/02/03 in gradient bold.

**Layout:** rounded shapes + soft drop shadow + glossy gradient on every card/circle/arrow.
Many structure templates: cycle, infinity, pyramid, venn, hexagon chains, arrow flows, org
tree, timeline, puzzle, funnel, stairs, maps. Pair gradient icon-circle + title + caption.
Symmetric, balanced, medium whitespace.

**Focus:** gradient depth itself implies order/flow (light=start, deep=end); reversed icons
pop; large step numbers anchor.

**Illustration (optional image tool):** Style 4 is a **basic option**, so it should default
to code-rendered gradient templates: cards, circles, arrows, maps, icons, connectors, and
structured chart marks. Use image generation only when the user requests a custom vector
asset or the data concept genuinely needs a custom gradient object/icon that cannot be
handled by the template system. When used, the asset must be **flat vector in the same
gradient** (not photographic) - e.g. an object segmented by gradient to carry categories
or a small isometric scene attached to a process node. Do not hand-draw a crude substitute
while image generation is available for a required custom asset. If image generation is
needed but unavailable or repeatedly fails, pause and ask the user in Chinese whether to
retry image generation or approve a fallback. Guardrail: generic only.

## Execution rules from references

- Use Style 4 references for reusable business-template structure: rounded cards,
  connected nodes, gradient arrows, process steps, maps, cycles, and icon circles. Do not
  copy a reference layout or subject exactly.
- Style 4 is a basic option, so its generation logic is clarity-first. Start from the
  clearest corporate structure for the data: process, timeline, map, hierarchy, funnel,
  relationship diagram, or peer card grid. Use gradient polish to clarify order and
  grouping, not to make the slide more complex.
- If used inside a PPT workflow, inherit the PPT background first. Adapt card fills,
  gradients, shadows, and text contrast to that background; avoid dropping an unrelated
  white template slab onto a colored deck unless the deck system uses white cards.
- If generated vector scenes or segmented objects are used, they must share the same
  gradient/vector language as the chart components. Do not mix realistic/painterly assets
  with flat corporate gradient cards.
- Follow the global Data-Art Integration Rules from `SKILL.md`: vector scenes, icons, and
  segmented objects must be nested into the same process, map, hierarchy, card, or
  relationship structure as the data. Do not place a generic gradient illustration in a
  corner if it does not clarify a specific node, step, metric, or relationship.
- Before rendering, translate the source data into a corporate structure template:
  process chain, timeline, pyramid, map, cycle, hierarchy, funnel, relationship network,
  or peer card grid. Choose the template because it clarifies the data shape, not because
  it is visually convenient.
- Optional generated vector assets must be attached to nodes, steps, map regions,
  segments, or cards. If an asset only decorates the side of the slide, remove it or
  regenerate it as a node-level/segment-level visual that helps explain the data.
- When the content is quantitative, vector assets must be data-shaped, not only
  topic-shaped. Node size, segment thickness, stack height, fill level, route length,
  icon count, or gradient depth should reflect the value/order/share when those visual
  properties are part of the message. Exact labels remain code-rendered, but the template
  object should still intuitively express the same relationship.
- Generated scenes or objects, when used, must be inspected before compositing. Reject or
  regenerate any asset that contains fake text, pseudo-labels, random numbers, cropped
  key parts, mismatched perspective, or data-looking marks that do not match the source
  values.
- Every illustration must semantically match the data or concept it supports. If an
  available vector object/icon does not match the metric, process step, map region, or
  relationship, regenerate a better asset with image generation or omit it.
- Information hierarchy must control the structure template. Same-level steps, nodes,
  cards, map regions, or relationship blocks should use comparable size, icon treatment,
  gradient intensity, and caption hierarchy. Parent/summary nodes may be larger or more
  saturated; child/detail nodes should be smaller or nested. In non-grid diagrams such as
  cycles, funnels, maps, radial flows, and object scenes, allocate visual territory by
  hierarchy rather than by decorative balance alone.
- Text in rounded cards, nodes, circles, and badges must be optically centered with
  balanced padding. Step captions should be short and aligned to a consistent grid.
  Long Chinese labels should wrap within the card instead of touching the border.
- Follow the global frontend-design typography rules in `SKILL.md`: every card, node,
  step, KPI, and repeated data module needs a measured text-stack contract and a
  typographic alignment spine. Corporate polish depends on exact alignment: titles,
  values, units, captions, metadata, icons, and connector labels must sit on declared
  lanes rather than independently guessed coordinates.
- Summary cards, decomposition bars, formula strips, and bottom verification modules must
  follow the global composite-module subgrid rules from `SKILL.md`. Split the module into
  left explanation, center graphic, and right formula/total zones before rendering. Align
  all text and numbers to shared baselines, measure formula token widths, and keep clear
  gutters between text, bars, percentages, and totals. Do not assemble these elements
  with unrelated hard-coded coordinates.
- Connectors/arrows/leader lines must attach to the correct node, step, map region,
  segment, or data-bearing gradient block. Avoid lines pointing at shadows, gaps, or
  nearby decorative gradients. The opposite endpoint must attach to the corresponding
  label/text group or node label; loose connector strokes are failed annotations.
- Data encoding must stay exact after rendering. Gradient segment sizes, node counts,
  step order, map-region marks, icon counts, connectors, color intensity, and label values
  must be checked against the source numbers or structure. Gloss, shadow, and gradient
  polish must not change the implied value, order, share, or relationship.
- Corporate templates should reduce cognitive load, so each metric should appear once in
  the structure. A node/card/gradient segment may carry an exact label, but do not repeat
  the same values as a second mini chart, table, or formula row in the same slide area.
  Use supporting space for the implication, step caption, or relationship explanation.
- Output both PNGs: a complete annotated version and a clean version with the same
  inherited/fallback background, gradient structure, icons, connectors, arrows,
  data-bearing gradient blocks, template geometry, shadows, and non-text visual structure.
  The clean version removes only readable text and numbers; it must not neutralize,
  recolor, or replace gradient marks, icon shapes, connectors, or data-bearing geometry.

## User reference images

Use the local files in `../assets/style-4-corporate-gradient-references/` as style
direction for this style. They are references for structure/template language, not
templates to copy.

Available references:
- `preview-business-structure-templates.webp` - slide grid of process, hierarchy,
  arrows, puzzle, cycle, pyramid, and cloud/SEO-style business templates.
- `preview-timeline-line-templates.webp` - timelines, line steps, puzzle grids, and
  connected node templates.
- `preview-cycle-map-templates.webp` - radial cycles, target, stacked layers, trophy,
  maps, and regional statistic templates.
- `preview-piggy-bank-gradient-object.webp` - segmented gradient object that carries
  category labels inside the object.
- `preview-circle-puzzle-shapes.webp` - circular, puzzle, triangle, Venn, banner,
  number, diamond, and linked shape templates.

When applying these references, preserve Style 4 traits: inherited PPT background or clean
white fallback, blue to purple gradient as the main visual system, rounded
cards/circles/arrows, reversed white icons inside nodes, subtle shadows, balanced
symmetry, template-like clarity, and small caption blocks. Prefer this style for concept
structures, workflows, timelines, maps, relationship diagrams, and business process
slides. For precise analytical charts, use it only when the user explicitly wants a
corporate template look.
