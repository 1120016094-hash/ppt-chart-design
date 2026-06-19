# Style 3 - Metaphor Object (隐喻物象编辑信息图)

**Identity:** poster-like single graphic built on a clever visual metaphor. Don't put data
into a chart - find a real object that embodies the topic and **make the object the chart**.
For "viral / single punchy stat". Concept-driven.

**Core method (4 steps):**
1. Find a metaphor object whose physical property (length/segments/level/count/size)
   encodes the data (whale=catches, rocket exhaust=flights, tree slices=causes,
   book spines=religions, cargo containers=exports).
   Before choosing the object, decide the visual subject hierarchy: which noun is the
   primary subject and which nouns are context, route, location, cause, time, or supporting
   evidence. The metaphor object should usually be the primary subject. Secondary elements
   may appear as background, trail, shadow, small marker, annotation, or label anchor, but
   they should not mutate the primary object.
   If the theme has two or more categories, first find their shared parent object or
   process and make that the metaphor object. The object should represent the common
   ground, not one category plus decorations for the others. For example, categories such
   as marriage and divorce should be abstracted to one carrier such as relationship
   status, civil registration, paired documents, a bond/connection, or household-state
   transition; category values then alter the carrier through thickness, gap, stamp,
   layer, split, or position. Do not prompt for a collage of separate category symbols.
2. Give it an **original** pun/hook title (no copyrighted lyrics/quotes).
3. One core number, huge, leader-labeled.
4. Unify the set with a shell: inherited PPT background or cream fallback + red/indigo
   accents + a circular stamp badge.

**Palette (tokens: `style_3_metaphor_object`):** fallback bg `#EAEADE`; red `#C45446`
(dark #A8382A); indigo `#46467E` (dark #383870); text `#1A1A1A`. The **object keeps its
own natural colors**; red/indigo only on title, leader lines, badge, key numbers.
If an upstream PPT workflow provides a slide/deck background, inherit it and adapt text,
stamp, shadow, and object edge treatment for contrast. Do not force a cream rectangle
behind the object unless the deck design explicitly uses cream panels.
If the generated object asset already contains a cream/paper/texture field, treat that
field as the chart background and extend or crop it to the full canvas. Do not place it
as a smaller rectangle on top of a second fallback background unless that outer field
separates data or is required by the upstream PPT design system.

**Type:** expressive, matched to subject - serif (Playfair) for solemn, distressed/bold
(Anton) for edgy. Core number always huge bold. Captions in [brackets]. Keep editorial
typography loose and reference-like: titles may be large, but supporting copy must be
short, wrapped into readable lines, and separated from the title by clear vertical
spacing. Never run a long subtitle as one cramped line just because there is horizontal
room. For Chinese layouts, if the title is poster-scale, set the subtitle at a clearly
smaller size, usually no more than 40-45% of the title height, and keep the note/caption
another step smaller. Prefer two short subtitle lines over one dense line; use generous
leading and avoid compressing title, subtitle, and note into one tight block.

**Motifs:** circular postmark/stamp badge (curved text), simple edge-landing leader
lines, photo cut-out + collage with halftone, generous whitespace, single focal point.

**Annotation layout rules (strict):**
- Follow the global frontend-design typography rules in `SKILL.md`: define a measured
  text-stack contract and typographic alignment spine before rendering. Poster looseness
  does not permit arbitrary text placement; title, focal number, units, captions, badges,
  and external labels must use declared anchors, baselines, and gutters.
- Same-level external data labels must use one calm label rail or a clearly documented
  mapped rhythm. Year/name labels should share a baseline, value labels should share a
  second baseline, and connector starts should be derived from the measured label group.
  Do not stagger label y positions without a data or layout reason.
- Bordered KPI/text cards must center their internal text on the card's visual centerline
  unless the reference style explicitly uses a different alignment. Do not let text sit
  close to the left/top border; preserve generous padding and balanced vertical spacing.
  Treat the card text as a centered group: top and bottom whitespace should feel equal,
  and the largest number should sit optically in the middle of the card.
- Circular stamps/badges must keep all text comfortably inside the inner ring. Reduce
  type size before allowing text to crowd the ring; center all lines optically.
- Leader lines must terminate at the exact corresponding data-bearing color block,
  drawer, slice, layer, contour, or segment. For simple geometric marks they may land
  inside the mark; for generated object/animal/product illustrations they must land on
  the nearest semantically correct visible edge or just outside that edge, not in the
  subject center. Do not draw lines through bodies, faces, product surfaces, dense
  textures, or the main illustration mass. Target-side endpoint dots are normally
  disabled for object-as-chart illustrations because they damage the object; if a marker
  is needed, use a tiny external tick/dot in adjacent empty space, never a dot on the
  illustration body. Lines must not point to shadows, object frames, gaps, or nearby but
  unrelated colors. When the generated object has perspective, choose anchor points
  manually after inspecting the render.
- Leader lines must also attach to the corresponding external label group, not merely run
  across the page near it. For each line, define two anchors before drawing: one anchor
  inside/on the exact object segment and one anchor on the related title-number-note label
  group. If the object is scaled or cropped after anchor selection, recompute the segment
  anchor in final canvas coordinates. Lines that float near a segment, cross an unrelated
  segment, or stop short of the label group fail the style.
- External labels should sit outside the object and align in a calm column; lines may cross
  empty space but should not cross unrelated labels or obscure the hero object.

**Illustration (generate with image tool, this IS the chart):** generate the metaphor
object **already transformed by the data**: sliced, segmented, filled, stacked, stretched,
or otherwise altered so the color/shape/data encoding is physically integrated into the
object at generation time. Do not generate a clean object first and then paste flat chart
blocks on top; that creates a mismatched "real object + flat overlay" look. The generated
asset should contain the data-bearing object and its colored slices/fills as one coherent
illustration. The subject matter and material must also match: avoid mixing photoreal
objects with watercolor/flat data fills, avoid liquid/paint metaphors for finance unless
the data is literally about flow/liquidity, and prefer topic-native physical encodings
(e.g. vault compartments, ledgers, coin stacks, bond certificates, storage drawers for
financial data). Use one coherent rendering medium across object and data encoding. Use
code afterward only for precise Chinese text, exact numeric labels, small leader lines,
source notes, and PNG assembly. Fragment in tokens. Because the object is the chart,
call the image-generation tool for the data-integrated metaphor object whenever it is
available; do not hand-draw or programmatically fake the object in PIL/SVG/canvas. If
image generation is unavailable or repeatedly fails, pause and ask the user in Chinese
whether to retry image generation or approve a fallback. Only with approval may you use a
simplified icon/object treatment.
Before prompting, run the style-specific simplicity check: the object concept must be
summarizable as "one subject + one data behavior". Do not combine every title keyword
into the object's anatomy. Routes, roads, maps, locations, seasons, policy contexts, and
other secondary ideas may guide the object placement or labels, but should stay outside
the object's body unless they are naturally part of the object and essential to the data
encoding. If a route is secondary to an animal migration story, use a trail, soft ground
path, map cue, or leader annotation around the animal; do not turn the animal itself into
a road. If this rule makes the metaphor weak, switch to a flow/timeline structure or a
basic chart style instead of forcing the metaphor.
For multi-category data, the simplicity check must also pass the common-carrier test:
can the viewer read one shared object/process before noticing category differences? If
not, remove category-specific objects and encode the categories as states of the shared
carrier, or keep the illustration contextual and let code-rendered marks carry the exact
comparison.

**Guardrail (strict):** generic, non-branded, non-IP objects; no real people; original
wordplay only - extract the metaphor *approach*, not the content.

## Execution rules from references

- Use Style 3 references for object-as-chart mechanics, leader-label language, stamp/badge
  treatment, and sparse editorial poster rhythm. Do not borrow the reference subject,
  central creative idea, or exact composition.
- Before generating the object, write the object-mapping decision: source data shape,
  chosen physical property of the object, which value each segment/fill/layer/count
  represents, and which labels remain code-rendered. Reject metaphors whose physical
  property does not naturally match the data.
- Before generating a multi-category object, write the common-carrier decision: the
  categories, their shared parent idea, the one metaphor object/process chosen from that
  parent, and which category-specific symbols were intentionally omitted. Reject image
  prompts that try to include a separate object for every category.
- Before generating the object, also write the subject-hierarchy decision: primary object,
  secondary/context elements, omitted elements, and why the chosen metaphor remains
  simple. Reject prompts that treat multiple nouns as equal subjects to be fused.
- Before using object slices, fills, or color areas, prove that the values are either
  same-level peer quantities or additive parts of the same whole. If the source values are
  a sequence/event, cumulative total, derived increment, and contextual note, do not split
  the animal/object body into proportional color blocks. Use a route, parent-child
  relationship, milestone marker, focal total, or attached note structure instead.
- Style 3 is an upgrade option, so the data-integrated metaphor object is generated before
  final poster composition. First call image generation for the object already transformed
  by the data; then compose the title, exact labels, leader lines, badge, compact
  contextual notes, and source around that object. Do not design a conventional chart first
  and then look for an object to decorate it.
- The metaphor object must pass a dual-expression test: without reading the labels, the
  viewer should still sense the main comparison, ranking, composition, or change from the
  object's physical form. Labels and numbers make it exact; the object makes it intuitive.
  If the object only names the topic but does not embody the data relationship, choose a
  new object or a different style.
- If used inside a PPT workflow, inherit the PPT background first and adapt object shadow,
  edge treatment, text color, and badge contrast to that background.
- The generated object and its data encoding must be one coherent image/material system.
  Avoid real-object-plus-flat-overlay, mismatched materials, or topic-inappropriate
  metaphors.
- Code compositing may crop, scale, de-background, add leader lines, add exact labels, or
  apply very subtle global color correction. It must not recolor the generated object,
  clip flat fills into the object's silhouette, or paint new data-bearing sections onto
  the object after generation. A clipped post-hoc color field is still a flat overlay and
  should be rejected unless the user explicitly approves a fallback.
- Follow the global Data-Art Integration Rules from `SKILL.md`: the image is not an
  add-on. The metaphor object, its divisions, the title, leader labels, and exact values
  must be planned as one poster system before generation. If the object cannot carry or
  clarify the data, use a different style or keep the object contextual and move exact
  encoding to code-rendered marks.
- If the generated object cannot integrate the data cleanly, regenerate with a clearer
  object-mapping prompt or downgrade the object to a contextual illustration and use
  code-controlled marks for the exact data. Do not keep a visually attractive object that
  implies the wrong value, material, or topic.
- Generated object assets must be inspected before compositing. Reject or regenerate any
  object that contains fake text, pseudo-labels, random numbers, cropped key parts,
  mismatched materials, distorted data segments, or data-looking marks that do not match
  the source values.
- Information hierarchy must be visible through the whole poster. The metaphor object or
  object region that carries the primary statistic should own the dominant area/scale and
  strongest contrast. Secondary comparisons, leader labels, badges, and notes must be
  smaller and visually subordinate. If several object parts represent same-level metrics,
  their scale, material, label treatment, and visual weight must be comparable.
- Data encoding must stay exact after rendering. Object segment lengths, fill levels,
  slice sizes, stack counts, color blocks, leader-line anchors, and label values must be
  checked against the source numbers. If the generated object cannot carry exact numeric
  encoding reliably, treat the object as contextual and use code-rendered marks for exact
  data.
- Because the object is the chart, do not place a second conventional chart, full table,
  or duplicate ranking beside it to restate the same values. Exact labels, leader notes,
  badges, and one compact contextual comparison are acceptable when they attach to the
  object; a second full data system means the metaphor failed or should be simplified.
- Typography, badges, KPI cards, labels, and leader lines must follow the strict
  annotation layout rules above.
- Any supporting formula strip, decomposition bar, or KPI verification module must follow
  the composite-module subgrid rules in `SKILL.md`; keep object labels, formulas, and
  proportion marks separated by measured zones and clear gutters.
- Output both PNGs: a complete annotated version and a clean version with the same
  inherited/fallback background, data-integrated object, object proportions/colors,
  badge/stamp shapes, leader lines, dots, and non-text visual structure. The clean version
  removes only readable text and numbers; it must not replace the object with a neutral
  placeholder or remove/recolor data-bearing object parts.

## User reference images

Use the local files in `../assets/style-3-metaphor-object-references/` as style direction
for this style. They are references for the visual language and metaphor mechanics, not
templates to copy. Many references contain recognizable people, brands, characters, flags,
or political figures; do not reproduce those. Generate generic, non-branded replacements
that use the same *kind of mapping*. Reference images should explain **how** object and
data fuse into one visual, not **what** subject, metaphor, or composition to reuse. Always
invent a new metaphor object from the user's topic and data; never borrow the reference
image's main subject or creative idea.

Available references:
- `preview-segmented-beam-pop-culture.webp` - one long object segmented into colored
  percentage bands with hanging labels.
- `preview-sports-object-ranking.webp` - sports objects become ranking/comparison forms.
- `preview-rocket-exhaust-comparison.webp` - plume/exhaust shape becomes a comparison
  mountain/area chart.
- `preview-portrait-fragment-bars.webp` - face/portrait dissolves into data fragments
  with a benchmark bar.
- `preview-book-ufo-belief.webp` - book/object silhouette carries a conceptual comparison.
- `preview-cup-blood-bag-levels.webp` - liquid/container fill levels encode composition.
- `preview-orbit-radial-ranking.webp` - orbital rings and dots encode ranked duration.
- `preview-gun-bullet-bar-ranking.webp` - object extension becomes an extreme-value bar.
- `preview-nature-object-stacks.webp` - natural objects stacked/sized by contribution.
- `preview-book-spines-composition.webp` - object widths encode composition categories.
- `preview-cargo-ship-bars.webp` - cargo containers and shadows become country bars.
- `preview-building-window-composition.webp` - building/window lights encode part-to-whole.
- `preview-smiley-ufo-composition.webp` - icon/object plus beam segments encode survey
  composition.
- `preview-medal-ribbon-bars.webp` - ribbons/medals become stacked comparison bars.
- `preview-whale-segment-ranking.webp` - one object is sliced into ranked pieces.

When applying these references, first choose a metaphor object whose physical property
matches the data shape:
- **Length/segment** for ranking or part-to-whole.
- **Fill level** for composition or progress.
- **Stacked slices/layers** for contributors or causes.
- **Rings/orbits/rays** for radial ranking or distance/duration.
- **Object multiples** for category comparison.

Then generate the integrated object/scene with the image tool, including the visual data
encoding inside the object itself. Place only precision overlays afterward: leader lines,
brackets, exact labels, percentages, source, and small UI-like notes. Keep the page sparse,
editorial, and poster-like: inherited PPT background or warm cream fallback, one strong
title, one hero object, one focal number or comparison, restrained red/indigo accents, and
generous whitespace.

For outputs, produce both PNGs. The complete version includes title, labels, exact values,
leader lines, stamp/badge, and source. The clean version uses the same background and
object/composition style and removes only readable text and numbers from labels, badges,
KPI cards, and source notes. Keep the object, encoded proportions/colors, leader lines,
dots, badge shapes, and non-text structure exactly aligned with the complete version.
