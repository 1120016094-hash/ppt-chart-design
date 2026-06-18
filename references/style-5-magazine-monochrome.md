# Style 5 - Magazine Monochrome (杂志专题单色信息图)

**Identity:** full-page magazine feature infographic. **One hue per page**, highest chart
variety, mature/authoritative. Best for a deep single-topic page (several related charts +
big numbers + captions). The most capable but heaviest style.

**Palette = pick one monochrome recipe** (tokens: `style_5_magazine_monochrome.recipes`).
Formula: 1 dominant hue fills the page -> levels from its tints/shades -> + 1 cream/neutral
-> reserve 1 contrast for title + key numbers. Recipes:
- cobalt #006CC0 + contrast #FC3C30 (title white)
- coral #F07860 (deep #3A2A4A, title white)
- sage #789C84 + cream #FCE4C0 + contrast #F06C54
- aubergine #604884 + magenta #E43078 + yellow title #F0CC30
- taupe #6C6054 + orange #E4843C
- pale-blue #006CA8 + yellow #F0CC60 (light bg)
- night #242424 + pink #D890A8 (rainbow allowed for category legend)
- teal #306060 + cream #F0F0D8

If this chart is part of a PPT workflow, treat the upstream deck/slide background as the
page base. Pick or adapt the monochrome recipe so it harmonizes with that background
rather than replacing it. The "one hue per page" rule still applies to chart marks,
type accents, pictograms, and section fills, but the base background must follow the
presentation's background plan unless the PPT workflow explicitly gives this chart a
special feature-page color.

**Type:** compressed bold grotesque title (Oswald/Anton/Archivo Narrow, free), serif deck,
small-caps underlined subheads, big contrast numbers.

**Layout (magazine skeleton):** black "信息图/INFOGRAPHIC" label top-left; thick+thin double
rule under masthead; page split into sections, each a subhead + sub-chart; high density but
clearly zoned; leader lines + dots; big numbers anchor.

**Charts (richest set):** donut, radial stacked bar, radar, isometric pictogram (count =
quantity), isometric cube towers (height = value), circular radial array, bar.

**Illustration (generate with image tool):** isometric/pictographic and **tinted to the
page's single hue** (barrels stacked = output, cube towers = market cap, cooling tower =
share). Fragment in tokens. When pictograms, isometric objects, or visual count units are
needed, call the image-generation tool; do not hand-draw or programmatically fake them in
PIL/SVG/canvas while image generation is available. If image generation is unavailable or
repeatedly fails, pause and ask the user in Chinese whether to retry image generation or
approve a fallback. Guardrail: generic pictograms only, no brand logos / IP / real people.

## Execution rules from references

- Use Style 5 references for magazine skeletons, mastheads, double rules, dense zoned
  sections, giant facts, isometric pictograms, radial arrays, and coordinated multi-chart
  systems. Do not copy the reference subject, page composition, or specific data story.
- If used inside a PPT workflow, inherit the PPT background first. Adapt the single-hue
  recipe so it feels like part of the deck; only use a special full-page feature color
  when the PPT workflow has assigned one.
- Generated pictograms, cubes, barrels, towers, or objects must use the same monochrome
  material and hue system as the charts. Avoid mixing realistic objects, watercolor fills,
  or unrelated color accents with the magazine recipe.
- Style 5 is an upgrade option, so image generation comes before final magazine layout.
  First generate the data-bearing pictogram/tower/barrel/object field that embodies the
  main quantity, ranking, composition, or trend. Then build the masthead, section grid,
  exact labels, auxiliary charts, captions, and source notes around that image system.
- Follow the global Data-Art Integration Rules from `SKILL.md`: pictograms, cubes,
  barrels, towers, or silhouettes must participate in the magazine data system as count
  units, ranking towers, segment carriers, focal object charts, or section anchors. Do not
  use isometric art as a decorative sticker separated from the data modules.
- Before rendering, write the magazine spread plan: lead fact, secondary sections,
  repeated section grammar, pictogram/object roles, exact chart marks, masthead/rule
  system, and label lanes. Dense pages must still read as one feature article, not as a
  collage of unrelated chart fragments.
- If a reference shows the same data form, translate its structural method first:
  pictogram counts for quantities, towers for ranked magnitudes, radial arrays for status
  or cyclic comparisons, and object silhouettes for focal single-topic modules. Use a
  standard bar/table only when it is clearer for exact comparison, and keep it inside the
  same magazine skeleton.
- Generated pictograms, cubes, barrels, towers, silhouettes, or object fields must pass
  the dual-expression test: the object system should visually express the same
  quantity/ranking/composition/trend as the numbers. A tower's height, cube count,
  barrel stack, silhouette fill, radial density, or pictogram count should carry meaning,
  not merely decorate the section.
- Generated pictograms, cubes, barrels, towers, or objects must be inspected before
  compositing. Reject or regenerate any asset that contains fake text, pseudo-labels,
  random numbers, cropped key parts, mismatched materials, or data-looking marks that do
  not match the source values.
- Every pictogram or illustration must semantically match the data it supports. If an
  existing object does not match the metric/category, regenerate a better asset with
  image generation or omit the illustration.
- High density is allowed, but every section needs clear zoning. Titles, subheads,
  captions, footnotes, and big numbers must sit on consistent columns/rules with enough
  line height. Long Chinese subtitles should wrap into editorial lines rather than
  crowding the masthead.
- Follow the global frontend-design typography rules in `SKILL.md`: every repeated
  section, row, KPI, and caption group needs a measured text-stack contract, and the page
  needs a typographic alignment spine. Magazine density should come from intentional
  columns, baselines, masthead rules, and section lanes, not from loosely stacked labels.
- Information hierarchy must be legible across the whole magazine page, even when the
  page is not a strict grid. The lead fact or primary chart should own the largest/most
  contrasted territory. Same-level supporting charts should share comparable size,
  pictogram scale, chart richness, and caption weight. Background context, footnotes, and
  secondary lists should occupy smaller, quieter zones so readers can scan the page in the
  intended order.
- Boxed guide panels, side callouts, and table cells must keep balanced padding. Text must
  not sit too close to rules or borders.
- Magazine guide boxes, decomposition strips, formula rows, and summary panels must
  follow the composite-module subgrid rules in `SKILL.md`; density is acceptable only
  when explanation, graphics, percentages, formulas, and totals have declared zones,
  measured text spacing, and shared baselines.
- Leader lines/dots and pictogram counts must attach to the exact region, tower, object,
  radial segment, bar, or table row they describe. No label should point to a decorative
  shadow, empty gutter, or unrelated chart module. Connector lines must also attach to the
  corresponding label/text group, not merely pass near it.
- Data encoding must stay exact after rendering. Donut/radial segments, bars, pictogram
  counts, cube/tower heights, table values, color swatches, leader-line anchors, and
  label values must be checked against the source numbers. Magazine density and
  monochrome styling must not change the implied value, ranking, share, or comparison.
- Magazine density is not permission to duplicate data. A section may combine a mark with
  direct labels, but the same full series/composition/ranking should not reappear as both
  pictograms and a full bar list, both radial chart and full table, or both tower heights
  and a duplicate ranking panel. Use extra sections for secondary questions, selected
  annotations, methodology, or source notes rather than repeating the same dataset.
- Output both PNGs: a complete annotated version and a clean version with the same
  inherited/fallback background, magazine grid, rules, section shells, pictograms,
  chart marks, bars, radial segments, towers, leader lines/dots, swatches, and non-text
  visual structure. The clean version removes only readable text and numbers; it must not
  neutralize, recolor, resize, or replace pictograms or data-bearing chart marks from the
  complete version.

## User reference images

Use the local files in `../assets/style-5-magazine-monochrome-references/` as style
direction for this style. They are references for full-page magazine editorial systems,
not templates to copy.

Available references:
- `preview-taupe-inflation-radar.webp` - taupe full-page economics feature with radar,
  big numbers, side callouts, and dense footnotes.
- `preview-oil-barrel-isometric.webp` - isometric barrel pictograms, regional blocks,
  guide box, and table/bar section.
- `preview-night-cbdc-radial-map.webp` - dark radial country status map with many labels
  and color-coded status legend.
- `preview-teal-stock-cube-towers.webp` - teal market-cap cube towers plus donut summary.
- `preview-cobalt-chips-dashboard.webp` - cobalt semiconductor dashboard with donut,
  semicircle bars, ranking list, and big-number callout.
- `preview-coral-nuclear-tower.webp` - coral topic page with large tower silhouette,
  leader lines, bottom ranking strip, and giant facts.
- `preview-sage-confidence-radial.webp` - sage radial trust chart plus right-side dot
  ranking and stacked historical bars.
- `preview-aubergine-games-dashboard.webp` - aubergine games page with growth bars,
  acquisition table, and pictorial big-number section.

When applying these references, preserve Style 5 traits: one dominant page color, a black
`INFOGRAPHIC` masthead label, thick and thin editorial rules, compressed bold title,
high-density but zoned sections, multiple coordinated chart types on one page, giant
contrast numbers, small source/footnote text, and one cream/neutral plus one contrast
accent. Pick a recipe that fits the topic and any inherited PPT background, then keep the
entire page inside that adapted recipe. Use generated isometric/pictographic assets when
the page needs barrels, towers, cubes, objects, or visual count units; code should assemble
the magazine layout and labels.
