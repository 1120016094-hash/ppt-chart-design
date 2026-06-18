# Style 2 - Retro Editorial (复古网格编辑信息图)

**Identity:** magazine/annual-report spread. High contrast, full, with an editorial
structure that is usually implied by alignment, scale, type, texture, and a few purposeful
rules rather than obvious full-page boxes. Opposite of Style 1 (this one is additive,
packed, bold). For "opinionated, eye-catching".

**Palette = a formula, not one fixed set** (tokens: `style_2_retro_editorial.recipes`).
Always: 1 muted retro background + black + 1-2 saturated accents + texture fills. Pick ONE
recipe per chart. If this chart is part of a PPT workflow, the upstream deck/slide
background overrides the recipe background; adapt black rules, accent contrast, texture
fills, and generated illustration prompt to that inherited background instead of placing a
foreign recipe-colored page block.
- A sage: bg #E1EEDD, orange #CC8448, green #488460, cream #F6F7E8, black #1A1A1A
- B powder/coral: bg #C8E1E5, teal #18909C, coral #E44848, pink #F3C9C3
- C green grid: greens #54A860/#516A52, light #B8D5B7, near-black #272927
- D black/yellow: bg #F3F4E4, yellow #F0CC30, black #111
- E mono: bg #F9F8F4, black, white, hatch #CACACA/#6F6E6E
Secondary/"remainder" data uses **texture fill (hatch/halftone)**, not a light tint.

**Type:** Anton / Archivo Black (free). **Mixed-weight title** (one word thin, one bold).
Huge numbers + progress bars. Labels = black rounded-rect pills.

**Layout:** Use an editorial construction grid, but avoid making hard rectangular cells
the main visual idea. Prefer continuous strips, routes, data-shaped illustrations, soft
fields, shared baselines, and selective 1-2px black rules. Those rules are for emphasis,
baselines, axes, table-like measurement, or bound callouts; do not place a dark rule
directly on a clear background/image/color-field boundary just to restate the separation.
Leader lines + dots attach to exact marks. Isotype pictograms may be used for proportion
when they integrate with the composition.

**Illustration (generate with image tool):** Start with 1 continuous data illustration
whenever the dataset has a trend, ranking, composition, or flow that can be expressed as
one evolving visual system. Only then add supporting spot icons or isotype units if they
clarify a secondary module. Use ONE fixed fragment for the whole set: *flat 2-tone
bold-outline editorial vector, palette = recipe colors, riso/screen-print, no text, no
gradient*. First decide the full information architecture; then choose whether
illustration is needed. In this style, illustration should usually become a data-shaped
strip, route, object, field, or pictorial unit that helps the viewer read the values. Do
not force a decorative scene if it fragments the page or competes with the numbers. When
illustration is used, call the image-generation tool; do not hand-draw or
programmatically fake these illustrations in PIL/SVG/canvas while image generation is
available. If image generation is unavailable or repeatedly fails, pause and ask the user
in Chinese whether to retry image generation or approve a fallback. Only with approval may
you use icon library + isotype. Guardrail: generic objects only, no IP / no real people.

## Execution rules from references

- Use Style 2 references for editorial structure, screen-print illustration language,
  selective rule lines, pill labels, hatches, and dense-but-organized rhythm. Do not
  borrow the reference subject, main visual idea, or exact composition. Do not imitate
  obvious box grids when a softer continuous composition would be more beautiful and
  readable.
- Selective black rules must be purposeful editorial devices, not automatic separators.
  If two areas are already divided by color fields, texture, crop, or whitespace, do not
  draw another hard divider along that boundary. Let the field transition do the grouping
  unless the line carries axis, table, callout, or measurement meaning.
- If used inside a PPT workflow, inherit the PPT background first; choose/adapt the retro
  recipe so rule lines, black text, pills, hatches, and generated illustrations remain
  readable on that background.
- Generated hero scenes and icons must feel integrated with the chart system: color,
  texture, and data marks should share the same riso/vector material language. Avoid
  mixing a painterly/photographic object with flat chart overlays.
- Style 2 is an upgrade option, so image generation comes before final composition. First
  generate a data-themed editorial illustration that expresses the full source
  relationship through size, count, density, sequence, segmentation, texture, plume,
  terrain, route, flow, or pictorial units. Prefer a single continuous data illustration
  over separate illustrated cells. Then build exact labels, small charts, captions, and
  source notes around that generated data illustration.
- The generated illustration must be used as the actual illustration asset in the final
  PNG. Do not treat it as a visual reference and redraw a simplified PIL/SVG/canvas
  imitation. If the image tool produces a preview but no accessible local file, stop and
  ask the user to retry generation, provide/save the generated image, or explicitly
  approve a labeled fallback.
- The page must be designed as one coherent editorial chart, not a collection of cramped
  tiles plus a decorative picture. Establish a clear focal chart or KPI first, then let
  smaller modules support it. Illustration may sit inside a module, label a category, or
  become an isotype/data unit; it should not occupy a large unrelated region.
- Before choosing any generated illustration, translate the data into an editorial visual
  form. Ranking can become differently sized terrain/exhaust/plume masses; trend can
  become a sequence of growing cells, smoke volumes, stacked strata, or a route whose
  height follows the values; composition can become segmented objects, isotype fields, or
  textured blocks. The image and the number must tell the same story. A generic factory,
  vehicle, crowd, animal, or policy icon is not enough unless its size, count, density,
  segmentation, or position expresses the data relationship.
- For data types that match the references, borrow the structural method before choosing
  a conventional chart, but translate hard boxes into lighter editorial grouping when
  possible. Event/policy/year data should be considered as a continuous editorial
  timeline, route, strip, terrain, smoke/plume path, or softly implied sequence, not as a
  generic line chart plus a picture. Category/composition data should be considered as
  segmented fields, isotype rows, pictorial units, or textured blocks. The result should
  feel like the data and illustration were planned as one spread.
- For timeline or event-sequence data, the default first sketch is a continuous
  editorial timeline: a shared path/strip/terrain/plume/scene carries the change, with
  year/event labels and code-rendered dots/labels attached to it. Use boxed cells only
  when discrete episode comparison is clearer than a continuous reading. Use a line chart
  only when precise continuous trend reading is the main message, and state that reason
  before rendering.
- For quantitative timelines, first consider a data-shaped timeline image: the whole
  visual strip should grow, shrink, thicken, darken, stack, or change density according to
  the values. If a precise line is needed, it should trace or verify the same visual
  shape, not float above an unrelated illustration.
- Do not let the editorial structure make the same data talk twice. If a sequence, ranking, or
  composition is already encoded by data-shaped cells, bars, isotypes, plumes, blocks, or
  a line, do not add a complete table/list of the same values in another cell. Use those
  cells for selected event notes, interpretive captions, source context, or whitespace
  unless the user explicitly requested a lookup table.
- Before image generation, make a whole-spread thumbnail plan: focal area, any peer
  modules, continuous illustrated path/object/field, exact chart marks, label lanes, and
  empty zones for Chinese text. Generate the continuous data illustration first whenever
  the data can support it; generate separate cells or units only when they serve clarity.
- Before generating illustrations, define a page-level illustration map. In a row of peer
  editorial modules, use the same illustration decision logic for each module, but do not
  force repeated spot illustrations for symmetry. Each illustration must correspond to the
  data it supports: a tourism illustration for tourism traffic/activities, transport
  modes for transport composition, policy/subsidy or consumer-flow visuals for support and
  spending. If the available asset does not match the metric, regenerate a better asset
  with image generation or omit the illustration from that module. Avoid one peer module
  carrying a visible illustration while adjacent peer modules are visually empty unless it
  is intentionally the focal module.
- Repeated statistic modules must share one visible grammar: aligned frames, identical
  internal padding, consistent title/value/caption order, and the same comparison/proportion
  bar treatment. Do not mix unrelated bar styles, isolated KPI pills, free-floating badges,
  and decorative chart fragments in the same spread unless the difference is part of a
  clear hierarchy.
- In row-based editorial rankings or strips, each row must be one registered unit across
  the whole spread. The left label/value block, connector lane, and right illustrated
  bar/trail/object must share the same row centerline or declared baseline system. Do not
  let the label stack sit high, the connector sit in the middle, and the illustration sit
  elsewhere; if the text block is tall, align its measured center or named value anchor
  consistently across all rows.
- Row rhythm must be editorially designed, not inherited from the generated illustration.
  If a generated trail/strip/object has uneven vertical spacing, do not force the left
  text stack into those gaps. Establish the left text rhythm first from the title height,
  row height, text-stack order, and scan path; then crop, scale, mask, or regenerate the
  illustration so the visual strips meet that rhythm. Retro density should feel composed,
  not like labels were attached after the image was finished.
- In the editorial structure, judge whether neighboring modules are peers before designing
  them. Peer modules in one row should use the same cell size logic, stat-card count,
  chart mark language, caption placement, and illustration/data treatment. If one module
  needs a larger card, a richer chart, or extra explanatory block, it must be because that
  module is a higher-level focal/summary block, not because the layout filled space
  opportunistically.
- If the retro editorial page uses a looser poster/newsprint composition instead of
  strict cells, the same hierarchy rule still applies across the whole image. Focal data
  should own the largest visual territory and strongest contrast; same-level supporting
  metrics should use comparable scale and mark grammar; notes and context should stay
  visually subordinate.
- Retro editorial marks may look hand-printed, textured, or screen-printed, but the data
  encoding must stay exact. Proportion bars, stacked segments, dot/isotype counts, color
  swatches, arrows, callout lines, and any illustration/data hybrid must be checked against
  the source numbers after rendering. Texture, hatch, rough edges, or generated illustration
  may add character, but must not change the implied value, ranking, share, or comparison.
- Prefer a controlled continuous editorial composition with generated data illustration
  composited into the chart system over a generated full-page template when the full
  template would leave fake text, dashed placeholders, cropped objects, obvious box grids,
  or misaligned empty frames. Full-page generation is acceptable only when it gives clean
  blank zones and coherent structure.
- Typography may be bold and packed, but not cramped. Keep headlines, subheads, numbers,
  captions, and footnotes in separate zones with clear grid alignment. Long Chinese
  subtitles should wrap within a module rather than collide with neighboring cells.
- Treat dense editorial typography as a designed stack, not a pile of labels. For each
  repeated row/stat block, define a measured order such as Chinese name -> English caption
  -> large value + unit -> metadata, with fixed gaps, a shared number baseline, and a
  separate metadata lane. Bold newsprint character is welcome, but no role may overlap or
  crowd another role; if a row cannot hold all text cleanly, shorten the secondary text or
  move metadata to a quieter lane before rendering.
- Use one editorial text spine for the spread. Kicker/title/subtitle and repeated row
  text should either align to the same main text x-axis or use a documented hierarchy
  offset. Rank circles live in a marker lane; they do not define the main text spine.
  Values, units, and metadata must sit on consistent lanes across all rows. A retro
  editorial layout may feel energetic, but its type should still look intentionally
  gridded rather than loosely scattered.
- Bordered modules/pills must keep balanced internal padding. Text inside rounded pills or
  boxed stat cards should be optically centered unless the reference pattern clearly uses
  another alignment. Do not place an outlined data mark or illustrated object inside a
  second outer border unless that outer border has a distinct semantic role such as a
  highlighted event.
- Editorial summary strips that combine copy, proportion bars, percentages, formulas, or
  totals must follow the composite-module subgrid rules in `SKILL.md`; do not let dense
  newsprint styling become unrelated hard-coded layers.
- Leader lines, dots, isotype counts, and hatches must connect to or occupy the exact data
  module they describe. No line should point to a decorative icon, shadow, grid gap, or
  unrelated nearby block. When a leader line is used, its other endpoint must attach to
  the corresponding label/text group, not stop nearby as a loose decorative rule. In a
  repeated row set, all leader lines must share a connector lane on at least one side and
  all endpoint dots must use the same declared radius and stroke/fill treatment unless a
  specific hierarchy calls for a different marker.
- Output both PNGs: a complete annotated version and a clean version with the same
  inherited/fallback background, structural fields, illustrations, chart marks, colored bars,
  hatches, swatches, leader lines, and non-text visual structure. The clean version removes
  only readable text and numbers; it must not neutralize or replace the colored
  data-bearing marks from the complete version.

## User reference images

Use the local files in `../assets/style-2-retro-editorial-references/` as style direction
for this style. They are references for visual language, not templates to copy.

Available references:
- `preview-green-policy-timeline.webp` - tiled policy timeline with green grid cells and
  integrated editorial smoke/factory illustration.
- `preview-yellow-ai-retail-grid.webp` - cream newspaper grid, yellow highlight bars,
  black icons/isotypes, and dense multi-panel layout.
- `preview-black-white-returns.webp` - stark black-and-white editorial spread with
  hatched fills, pie charts, boxed panels, and large object illustration.
- `preview-blue-packaging-dashboard.webp` - muted blue dashboard with icon column,
  chart panels, pies, bars, and red/teal/black accent system.
- `preview-au250-marketplace.webp` - pale green market report with map, flow strips,
  pictorial retail icon, thick dividers, and pill labels.

When applying these references, preserve Style 2 traits: editorial/newsprint density,
large mixed-weight headlines, selective black rules, black labels or pill captions,
hatch/halftone fills for secondary areas, bold percentages, isotype rows, and flat
generated illustrations that look screen-printed or editorial. Avoid turning the page
into a visibly gridded worksheet unless the data is genuinely a lookup table. Use image
generation first for the continuous data illustration or integrated pictorial system,
then composite charts/text around it. Treat reference backgrounds and token recipe
backgrounds as fallback moods, not mandatory page colors when an upstream PPT background
has been supplied.
