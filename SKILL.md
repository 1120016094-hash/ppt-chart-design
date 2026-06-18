---
name: ppt-chart-design
description: >
  Design professional, logically-complete charts and infographics in grouped basic
  and upgrade designer styles, and render them as high-fidelity PNG images for use
  in presentation slides. Use this skill whenever the user is making a PPT/deck and
  needs to present data, asks for a chart/graph/infographic, says their charts
  "look unprofessional" or "don't look good", asks "how should I show this data",
  or uploads numbers that need visualizing for a presentation - even if they don't
  explicitly say the word "chart". Also use when the user asks to apply a specific
  visual style to a data graphic.
---

# PPT Chart Design

Helps non-designers turn data into professional, well-reasoned presentation charts.
The value is two systems: (1) a decision logic for **which chart** and **which style**,
and (2) a faithful **design system** distilled from five professional designers.

Output mode (fixed): **PNG images only**. Do not create or output PPTX files unless the
user explicitly asks for a PPTX in that same turn. Every completed chart request must
produce two PNGs:

1. `*_complete.png` - the full finished graphic with title, labels, numbers, leader
   lines, source notes, and any required annotations.
2. `*_clean.png` - the same finished image with only text and numbers removed. This
   version must preserve the image, layout, illustration, frames, colors, data marks,
   bar/area/segment proportions, object proportions, icon counts, swatches, leader lines,
   and all non-text visual elements exactly as in `*_complete.png`. Do not neutralize,
   recolor, simplify, replace, or convert data-bearing graphics into placeholders. Remove
   only readable text/numbers/axis tick text/label text/source text. If the user needs a
   neutral template with no data-bearing marks, output that as a separate optional
   `*_template.png`, not as `*_clean.png`.

## Background inheritance for PPT workflows

This skill may run as one component inside a larger PPT/presentation workflow. In that
case, chart backgrounds must follow the upstream deck background plan, not the style's
standalone default.

Priority order:

1. **Upstream PPT workflow background plan** - if the current task includes a deck theme,
   slide background color, brand palette, dark/light mode, page section color, or visual
   system from a presentation workflow, inherit it.
2. **User-provided background direction** - if the user names a background color/style for
   this chart, use that.
3. **Style fallback** - only when no upstream/user background is available, use the
   selected style's default background token/reference color.

When inheriting a PPT background, adapt the chart safely:

- Preserve the selected style's layout logic, typography hierarchy, annotation system, and
  palette relationships, but tune contrast, neutrals, shadows, borders, and generated image
  prompts to sit naturally on the inherited background.
- Do not create a large foreign-colored rectangle behind the chart unless that rectangle
  is explicitly part of the deck design system. The PNG should feel native to the slide.
- If the chart needs transparency for flexible placement, output an additional transparent
  PNG variant only when the user or PPT workflow asks for it. Otherwise keep the inherited
  background baked into both `*_complete.png` and `*_clean.png`.
- The `*_complete.png` and `*_clean.png` backgrounds must match each other exactly.

## Workflow (follow in order)

1. **State the message first.** Write one sentence: what should the audience conclude?
   That sentence becomes the chart title. One chart = one point. If the user only gave
   raw data, infer the likely message and confirm briefly. If the message is a single
   number, attach a comparison (see principle 1 below) - a lone number is never enough.

2. **Design the whole information architecture before drawing.** Decide the page's
   hierarchy as one coherent composition: primary message, secondary evidence, supporting
   context, and source/notes. Allocate visual weight to data first. Illustration is
   allowed only when it makes the data easier to understand, improves grouping, or becomes
   part of a data encoding. Do not add a large decorative image just because the style
   supports illustration. Before generating any illustration, plan the illustration system
   for the whole page: which modules get illustrations, what scale they use, where they
   sit, and how they relate to the data. Modules at the same hierarchy level must use a
   consistent illustration decision logic: use illustration only where it has a clear
   semantic role for the specific data. Do not force repeated illustrations merely for
   symmetry. If an illustration is not semantically matched to the data it represents,
   regenerate a better asset with the image tool or remove the illustration from that
   module.

   Before assigning layout sizes, classify every metric into information levels:
   - same-level peer metrics (same scope, same role in the argument, similar analytical
     weight);
   - parent/child or summary/detail metrics;
   - primary focus vs secondary evidence vs contextual notes.
   Also classify every metric's **numeric relationship type** before choosing visual
   encoding:
   - peer comparison: independent values with the same unit, same denominator/scope, and
     same analytical role;
   - additive part-to-whole: components that sum to a stated total under the same scope;
   - sequence/event: milestones, first arrivals, dates, process steps, before/after states;
   - cumulative total: a running or period total;
   - derived increment: a value calculated from related totals, such as new calves =
     return total minus migrating mothers;
   - contextual comparison: timing difference, benchmark, or note.
   A visual encoding is allowed only when it matches this relationship type. Do not use
   one object split into proportional color segments, one bar family, one pie/donut, or
   one same-level row set unless the values are peers or additive parts of the same whole.
   Sequence/event, cumulative total, derived increment, and contextual comparison values
   need different visual roles: event markers, flow stages, focal totals, small notes, or
   formula/annotation labels. This check must happen before prompting image generation.
   Before prompting any illustration, also run a **visual subject hierarchy audit**:
   identify the title/message subject, the primary visual subject, secondary/supporting
   subjects, environmental cues, and any subjects to omit. One image should have one
   primary subject. Secondary subjects may become background context, a small marker,
   a route/trail, an annotation cue, or be removed. Do not merge two strong nouns into
   one hybrid object unless the fusion is natural, instantly readable, visually pleasant,
   and necessary to express the data. If the data story is "antelope migration route",
   decide whether the antelope or the route is the main carrier; do not turn the animal
   into a road merely because both words appear in the title.
   If the topic contains two or more category nouns or conceptual categories, run a
   **common-subject abstraction audit** before choosing an illustration subject. Ask what
   single parent idea, shared object, shared place, shared process, or shared physical
   carrier contains all categories. Use that common point as the illustration theme
   whenever possible, then encode each category as a measured state, layer, mark, gap,
   branch, shadow, route, or annotation on that common carrier. Do not generate one visual
   metaphor per category and combine them into a busy hybrid. For example, "marriage" and
   "divorce" should first be abstracted to a common carrier such as relationship status,
   civil registration, household bond, paired documents, or a connection line; then the
   data changes alter that one carrier. If no simple common carrier exists, choose the
   dominant category as the illustration subject and make the others code-rendered
   annotations, or fall back to a clearer basic chart.
   Run a **simple-image feasibility test** for upgrade styles:
   - Can a viewer identify the main subject in about one second?
   - Does the image express the data relationship without needing an awkward hybrid?
   - Are there more than two metaphors competing for attention?
   - If there are multiple categories, does the image use one common carrier instead of
     separate metaphors for each category?
   - Would removing the secondary subject make the image clearer while preserving the
     data message?
   If the answer shows the image would be complex, uncanny, or visually uncomfortable,
   demote or remove the secondary subject before generation, or choose a clearer basic
   chart path.
   Same-level peer metrics must use the same visual hierarchy: comparable module size,
   internal grid, chart type/mark grammar, type scale, padding, and visual element count.
   Different-level metrics must be deliberately scaled by hierarchy: focal/parent metrics
   may get larger modules or richer encodings, while detail/context metrics should be
   smaller or nested. Do not mix different module structures merely because one block has
   more text; first decide whether the data are peers or different levels.
   Same-level peer containers must also use one measurable geometry system. For card
   strips, KPI strips, table rows, label-card rows, and peer modules, declare the peer
   group before rendering and verify equal width/height, shared top/bottom or left/right
   axis, no overlap, minimum gutter, and near-equal gaps. A highlighted peer card may
   change fill, stroke, shadow, or emphasis, but it must not quietly change size, baseline,
   padding model, or spacing unless the hierarchy change is intentional and visibly
   explained.
   Assign every label, formula, note, and annotation to a **semantic owner module** before
   positioning it. A text item that explains a parent/summary value must live in the
   parent/summary territory, not underneath one child component merely because there is
   empty space there. A text item that explains one component must stay inside or directly
   attached to that component's territory. For example, a formula explaining a return
   total's composition belongs to the return-total module or merge point, not under the
   "new calves" module.
   This applies globally, not only to grid layouts. If the chart is poster-like,
   object-as-chart, full-bleed illustrated, radial, freeform, or magazine-style without
   visible grid cells, allocate each information level's share of the whole image through
   visual weight: area, scale, position, contrast, whitespace, object size, annotation
   density, and color intensity. The viewer should understand the hierarchy at a glance:
   the main conclusion first, supporting evidence second, context and notes last.

   Run a **single-expression audit** before layout: each source metric should have one
   primary visual expression on the page. Build a short metric-expression map with these
   columns: source metric, chosen primary expression, exact label position, supporting
   context, and omitted duplicate forms. Labels may identify or verify the primary
   expression, and notes may explain context, but do not repeat the same values as a
   second full chart, table, formula strip, timeline, ranking list, or duplicate pictorial
   system. If a value already shapes an object, area, bar, line, plume, map, or pictogram
   field, the adjacent number is a label for that mark, not a separate chart. If a source
   table is useful for provenance or event notes, show only the non-duplicative context or
   selected key rows; do not reproduce the full data table beside a chart that already
   encodes the same data unless the user explicitly asks for a lookup table.
   Also audit exact numeric text duplication across the page. The same exact source value
   should not appear as both a title/headline number and a separate large KPI/focal-number
   module. Choose one primary home for the number:
   - If the title contains the exact value, do not repeat that value as an independent big
     number elsewhere; use the freed space for the visual mark, context, or explanation.
   - If a big number module is the primary expression, make the title a verbal conclusion
     without repeating the same digits.
   - A compact formula or annotation should avoid repeating the exact result when that
     result already appears in the title/headline. However, do not create a fake formula
     to avoid duplication. If the line uses arithmetic operators such as `+`, `-`, `×`,
     `÷`, or percentages, it must use the mathematically appropriate operator, usually
     `=`, and include a valid result. A relationship arrow such as `→` means process,
     flow, or sequence, not calculation. If repeating the result would be too redundant,
     remove the arithmetic operators and rewrite the line as a prose relationship note
     instead. A compact repeated result is allowed only when needed to make the arithmetic
     formula correct, and it must remain visually subordinate to the primary expression.

   Treat "one data point appears as a mark plus a number" as calibration, not duplication.
   Treat "the whole dataset appears once as a chart and again as a complete table/list" as
   duplication. When the page feels complex, remove the secondary expression first before
   shrinking typography or adding more panels. Use freed space for interpretation,
   hierarchy, annotations, source notes, or whitespace.

   If the content might benefit from an upgrade option, note a candidate **data-art
   integration concept** at this stage, but do not call image generation until the user
   confirms an upgrade style. This concept explains how image, chart, grid, and labels
   could work as one system. State:
   - the visual subject hierarchy: primary subject, secondary/supporting subjects, what is
     intentionally omitted, and why any subject fusion is natural or unnecessary;
   - what data structure the page should become (continuous illustrated timeline,
     object-as-chart, map, flow corridor, pictogram matrix, editorial table, annotated
     scene, lightly implied modular field, etc.);
   - the **data-to-image translation**: which numeric relationship becomes a physical
     visual form such as height, area, volume, plume, terrain, layers, slices, fill level,
     route length, object count, density, or flow thickness;
   - which information is encoded by code-rendered marks and which information is only
     supported by illustration;
   - where illustration physically lives in the data structure (forming one continuous
     scene/route/terrain/object, inside softly implied modules, behind a route, forming a
     segmented object, marking a key event, becoming isotype units, etc.);
   - why the numbers and the image express the same idea in two forms: one exact, one
     visual.
   If the answer is "it sits in a corner as a nice picture", the integration concept has
   failed. Re-plan the page or omit illustration.
   If the concept uses the same segmentation/fill/area treatment for values with
   different relationship types, it has also failed. Re-plan as a sequence, flow,
   parent-child object, or focal-stat poster before image generation.

3. **Pick the chart type.** Read `references/chart-selection.md`. It is a two-level
   decision: intent (comparison / trend / composition / KPI / table / deviation /
   flow / distribution / relationship / geo) -> then data shape (how many categories /
   series / time). Pick the leaf recommendation. Never choose by what looks familiar.

4. **Resolve background context.** Before style confirmation/rendering, check whether the
   request is part of a PPT workflow or includes upstream deck/background planning. If so,
   record the inherited background color/style and use it as the chart canvas. If no
   background context exists, continue with the style fallback background.

5. **Recommend a style, then get user confirmation.** Read
   `references/style-selection.md` and recommend ONE of the grouped styles from the content
   type, audience, density, and tone. Then pause and ask the user to choose a style by
   replying with **1、2、3、4或5**. This style-choice prompt must be
   written in Chinese, including the recommended grouped option, reason, and the two
   grouped sections below. The upgrade section must include the note **需调用生图大模型**.
   Do not render or assemble outputs until the user confirms a style. If the user already
   explicitly named a style, grouped option, or unambiguous internal style number in the
   request, treat that as confirmation and continue. If the user replies with an outdated
   grouped label, ask them to choose from the current continuous numbers `3`、`4`、`5`.

6. **Load that style's spec + tokens.** Read the matching `references/style-N-*.md` and
   pull its palette/fonts from `assets/design-tokens.json`. Do not mix styles within
   one chart. Treat background tokens as fallback defaults; override or adapt them when a
   PPT workflow background has been inherited.

7. **Set the aesthetic direction using the frontend-design layer.** Apply the relevant
   parts of the `frontend-design` skill as an aesthetic director pass for this static PNG
   infographic. This layer raises the visual standard through typography character,
   palette confidence, spatial composition, background atmosphere, texture/detail, and a
   memorable point-of-view. It must not change the data, selected style, chart intent,
   output mode, clean-PNG rule, or the basic/upgrade generation path.

   Define one short aesthetic direction before rendering, for example: restrained
   analytical editorial, refined corporate utility, bold retro newsprint, data-object
   poster, or dense magazine feature. Adapt that direction to the selected style rather
   than inventing a sixth style. Avoid generic AI aesthetics: timid evenly distributed
   colors, default-looking layouts, random purple gradients, stock dashboard cards, and
   decorative effects that do not match the data topic. For static PNGs, ignore
   frontend-only motion guidance; convert the idea of interaction polish into refined
   spacing, contrast, typographic hierarchy, and visual rhythm.

   Treat frontend-design typography as **measurable layout craft**, not only font taste.
   Before rendering, define a compact type system for this chart: display/title,
   body/explanation, utility labels, numbers, and source notes. For each role, specify
   font size, weight, line height, maximum line width, intended alignment, and spacing to
   the next element. Distinctive typography is allowed only after the text block is
   readable, unclipped, and comfortably spaced at slide-view size.
   Comfortable spacing must be checked from actual rendered text boxes, not guessed y
   coordinates. For title/header stacks, measure each line's final bounding box and
   enforce minimum gaps between title line, number phrase, subtitle, formula, and notes.
   A stack that passes overlap checks but leaves only a few pixels between roles is still
   a typography failure. In PIL/custom renderers, use `layout_guard.require_vertical_gap(...)`
   or an equivalent measured gap assertion.

   Convert the type system into a **text-stack contract** for every repeated data module.
   A text stack is the measured vertical/horizontal sequence of title/name, subtitle,
   value, unit, metadata, note, and source labels inside one module. It must declare:
   role order, font for each role, anchor, baseline or top coordinate, minimum gap to the
   next role, reserved width, and the stack's bounding box. The renderer must measure all
   text boxes after font rendering and verify that roles do not overlap or visually
   crowd. Do not place names, English captions, large numbers, units, and metadata by
   unrelated hard-coded y offsets. If the stack does not fit, reduce the role count,
   shrink the full stack consistently, increase row height, or move secondary metadata to
   another lane.

   Also define a **typographic alignment spine** before rendering. The page must have
   explicit x positions for the main text spine, rank/marker lane, value lane, unit lane,
   metadata lane, connector lane, and right visual mark lane. Header title, subtitle,
   row names, row captions, and row values should align to the same main text spine unless
   the style reference intentionally creates a different hierarchy. Units must align to a
   unit lane or measured value edge; metadata must align to a separate metadata lane with
   a clear gutter. Passing collision checks is not enough: if the text looks like several
   unrelated columns, or if the title starts on one x-axis while the data text starts on
   another without a deliberate reason, the typography fails the frontend-design pass.
   For header/summary modules, align the **text blocks as blocks** first: title stack,
   subtitle/body line, formula/context note, and source/utility text should share the
   module's main text spine unless the style reference deliberately breaks it. Do not
   over-align unrelated internal tokens across different text roles. A headline number
   should sit naturally with its prefix/label using measured inline spacing; a formula
   should follow formula typography with balanced operators and token gaps. Only create
   internal value/result lanes when the module is intentionally tabular, accounting-like,
   or comparison-column based. Use `layout_guard.require_x_alignment(...)` to verify
   block-level spines and true tabular lanes, not to force every repeated number into the
   same x coordinate.

   Treat frontend-design as a **design pass, not a validator only**. When typography is
   criticized as ugly, scattered, crowded, or not aligned, do not merely add more checks
   to the old coordinates and re-run the same render. First revise the type/layout plan:
   row heights, row rhythm, header height, text stack order, font scale, column widths,
   metadata placement, and image crop/scale. Then update the renderer to use the revised
   plan. A render can pass collision and x-axis checks while still failing design if its
   vertical rhythm is inherited blindly from a generated image, if rows have awkward
   gaps, if the title area feels disconnected from the row system, or if labels are
   technically aligned but visually unbalanced.

   Run a typography preflight for every paragraph-like text block:
   - measure the rendered text width against the allocated text zone;
   - wrap Chinese copy into deliberate lines instead of letting it run under neighboring
     modules or past the canvas crop;
   - if the text is explanatory rather than a label, prefer 2-3 short lines with generous
     line height over one long line in a narrow column;
   - if the text still does not fit, widen the text zone, reduce the copy, or move the
     module. Do not squeeze line height, crop the text, or let a mask hide the overflow.

8. **Choose the generation path from the confirmed option.**

   **Basic options (基础1 / 基础2) are clarity-first.** Start from the audience's fastest
   comprehension path: chart type, hierarchy, sorting, scale, direct labels, units,
   readable typography, and whitespace. Use code-rendered marks, structured shapes,
   overlays, gradients, icons, and template components to make the data clear. Basic
   outputs should feel polished and presentation-ready, but they should not sacrifice
   reading speed for illustration. For Style 4, use image generation only if the user
   explicitly requests a custom vector asset or the data concept truly needs one; otherwise
   keep the slide as a code-rendered corporate infographic.

   **Upgrade options (3 / 4 / 5) are data-illustration-first.** After loading the
   selected upgrade style, first call the image-generation tool to create a data-themed
   illustration that expresses the core data through physical visual form. The illustration
   is not decoration; it is the primary visual premise. Before composing the final chart,
   generate or obtain this data-bearing illustration, inspect it, reject/regenerate it if
   it is generic or inaccurate, and only then design the page around it. The final layout
   should place title, exact numbers, leader labels, small charts, source notes, and
   secondary data as auxiliary layers around the illustration, so the viewer first feels
   the data through the image and then reads the exact values from the overlays.

   Upgrade image generation must follow this order:
   - choose the data theme and visual metaphor from the source values;
   - decide the visual subject hierarchy: one primary subject, secondary subjects as
     context/markers/annotations, and any omitted subjects;
   - run the simple-image feasibility test; if the concept needs an awkward hybrid or
     competing metaphors, remove/demote secondary elements before prompting;
   - decide which numeric relationship becomes visible as height, area, count, density,
     thickness, segment, fill, route, stack, layer, plume, or object size;
   - call image generation for the integrated data illustration in the chosen upgrade
     style, with no fake text or random numbers;
   - inspect whether the generated image really expresses the data relationship and fits
     the theme;
   - then build the composition around the image with code-rendered exact text, numbers,
     leader lines, auxiliary marks, and source notes.

   For upgrade options, run `scripts/image_backend_preflight.py` before the first image
   call. This skill may use only the built-in `image` / `image_gen` capability for image
   generation. Do not call Dreamina, external image CLIs, or API wrappers as fallbacks.
   The preflight goal is to confirm whether built-in image output can be observed as a
   local bitmap file for compositing. Use a before/after snapshot of
   `$CODEX_HOME/generated_images` around the built-in image call. If the image call shows
   a preview but no new accessible local file appears, stop before rendering and ask the
   user to download/save the preview image manually and send the saved file path, or
   approve a clearly labeled non-image fallback. The user-facing prompt must include:
   1) click the download/save control on the image preview; 2) the downloaded file usually
   appears in `/Users/guaren/Downloads/`; 3) move or save it into
   `/Users/guaren/outputs/ppt-chart-design-assets/` with a descriptive filename such as
   `spaceflight-record-style3-asset.png`. Also include quick-open commands for both
   folders: `open /Users/guaren/Downloads/` and
   `open /Users/guaren/outputs/ppt-chart-design-assets/`, plus Finder `前往` ->
   `前往文件夹...` instructions. Do not retry blindly, do not imitate the preview with
   code, and do not switch to another generator.

9. **Create a layout grid, spacing plan, and art-direction sketch before rendering.**
   Before drawing any final marks, define the chart's construction system in writing or
   code variables. This construction grid is primarily for alignment and spacing; it
   should not automatically become visible page dividers:
   - canvas safe area;
   - title/subtitle/source zones;
   - panel rectangles;
   - module gutters;
   - internal padding for every panel, card, pill, badge, and chart plot area;
   - text block widths, line counts, line heights, and vertical rhythm for explanatory
     copy;
   - fixed lanes for category labels, value labels, axes, group tags, bars/segments,
     legends, and annotations;
   - subgrid columns for every composite summary module that combines explanatory text,
     data marks, formulas, totals, legends, or percentages;
   - minimum clear distance between adjacent panels and between any panel edge and text.
   Use this as a hard construction plan, not an afterthought. If a title, subtitle, card,
   pill, group tag, axis label, or chart module cannot fit inside its allocated zone with
   safe padding, resize/reflow the layout before rendering instead of squeezing text or
   letting modules collide.

   For basic styles, the sketch is a data-layout sketch: plot area, label lanes, hierarchy,
   panels, and supporting annotations first. For upgrade styles (Style 2, Style 3, Style
   5), the sketch starts from the already generated or planned data illustration: its
   crop, anchor, dominant shape, reserved blank zones, and surrounding auxiliary data
   modules. For Style 4 Corporate Gradient, add an art-direction sketch only when a
   generated vector asset is explicitly needed by the user or by the data concept. This
   can be a concise text sketch or coordinate plan, but it must answer:
   - how the selected style's reference language changes the chart form, not just colors;
   - how the data's values/comparisons become the image's shape, scale, volume, count,
     layers, path, or spatial relationship;
   - how the illustration becomes one continuous object/scene/flow or, when modules are
     necessary, how it is nested into softly implied modules without hard box separation;
   - which blank zones are reserved for exact code-rendered text and numbers;
   - which generated image assets are needed and the exact role of each asset;
   - what would make an asset fail (decorative only, wrong subject, fake text, cropped
     key parts, different medium, or not matching its data module).
   When the chart is the same data type as a style reference, prefer the reference's
   structural approach, but translate visible grids into lighter composition devices when
   they would make the page feel mechanical. For example, a policy/event timeline in
   Style 2 should first be considered as a continuous editorial timeline, route, strip, or
   softly implied sequence with illustration carrying the change, before defaulting to a
   generic line chart plus a separate illustration.
   Record a **reference-structure translation note** before rendering:
   - source data pattern (timeline, peer KPI set, composition, ranking, flow, map, etc.);
   - selected style-native structure from the reference language;
   - exact data marks that remain code-controlled;
   - image-generation assets, if any, and how they physically attach to the structure.
   If a conventional chart is still chosen, state why it reads the data more clearly than
   the style-native alternative. Otherwise, do not default to the conventional chart.
   If the user has provided style references or is explicitly judging beauty/artfulness,
   use or mentally apply `layout-design-check` before rendering as a preflight art-layout
   review. Its job here is grid, visual hierarchy, whitespace, reference-structure
   matching, and image/data integration. It must not change the selected style, data
   values, chart intent, or this skill's output rules.

   Before rendering any text or graphic, create a **collision-safe layout contract** in
   code. Use `scripts/layout_guard.py` or an equivalent in-script guard. The contract must
   list text zones, chart zones, decorative/ambient zones, panel/card/plot edges, and
   approved text backgrounds. If this contract cannot be expressed as registered
   rectangles or paths in the render script, the layout is not ready to render. Do not
   rely on screenshot inspection alone. A chart with unregistered readable text or
   unregistered collision-relevant graphics fails the skill.

10. **Render the chart as high-fidelity PNG images.** Use `scripts/render_chart.py`, which
   themes matplotlib from the tokens (palette, fonts, grid/spine rules). For upgrade
   styles whose spec or token says `illustration.mode` is `"generate"` (Style 2, Style 3,
   and Style 5), call the image-generation tool before final composition to create the
   data illustration justified by the information architecture. For Style 4, image
   generation is optional:
   use it only when a custom gradient vector object/icon is necessary for the data concept
   or the user requests it; otherwise build the corporate template with code-rendered
   gradient shapes, icons, connectors, and chart marks. The generated asset must be
   integrated with the data module
   it supports (pictogram counts, category icons, object-as-chart, or a small contextual
   motif). Do not force a decorative hero illustration or let illustration compete with
   the data. Code is for chart geometry, annotation, layout, and compositing; image
   generation is for integrated hero objects, scenes, icon sets, or pictographic visuals.
   Generated illustrations must be requested to fit the art-direction sketch, not as
   generic topic art. Prompts must name the asset's data role, its intended crop/position,
   the numeric relationship it must visually embody, and the style medium. For example:
   "three smoke plumes with different widths matching low / middle / high emissions
   stages" is better than "CO2 factory illustration"; "three terrain/exhaust masses whose
   relative volumes match crewed spaceflight counts" is better than "rocket illustration".
   Do not use a standalone spot illustration if the data structure calls for cell-level,
   object-level, or data-shaped integration.
   If a generated full-template contains fake placeholder text, dashed pseudo-labels,
   misaligned frames, cropped illustration, or decorative marks that conflict with the
   data system, discard that template and rebuild with a controlled layout/compositing
   pass. The final image must be designed as one complete composition: typography,
   illustration, chart grammar, spacing, and data hierarchy must be solved together rather
   than assembled as unrelated overlays.
   During rendering, reserve explicit geometry lanes for every chart component: category
   labels, value labels, axes, bars/segments, comparison marks, legends, group tags, and
   annotations. A plotted mark must never pass underneath or touch readable text unless
   that text is intentionally placed inside the mark and has passed the label-fit checks
   in step 11. For compact KPI strips and mini-bars, use fixed text columns and fixed mark
   columns; do not let bars grow into the number column.
   For every leader line, connector, bracket, or callout ray, create a **connector binding
   table** before drawing. Each connector row must include: source metric/category,
   target data mark id, target anchor point on the actual visible mark/color block,
   label/text id, label anchor point on the label group, line path type, and allowed
   clearance. Draw the line from anchor to anchor, not from hand-guessed coordinates. A
   connector is valid only when one end touches or intentionally enters the target
   data-bearing mark and the other end touches the label group's anchor edge/dot. Lines
   floating near a color block, ending on a shadow/gap/frame, or stopping before the
   corresponding text group are failed renders.
   For composite summary modules, render from a module-local subgrid. Do not place a
   description block, proportion bar, formula, legend, and percentage labels with
   unrelated absolute coordinates. Define each sub-zone first, then draw within it.
   Register every text item and collision-relevant graphic with the layout guard as it is
   drawn. The render script must call the guard's final assertion before accepting the
   PNG. A failed assertion means the script must reflow, resize the module, shorten/remove
   the competing decorative shape, or move labels into a reserved lane; never solve it by
   covering the collision with a lighter color or by hoping it is visually acceptable.
   Output a full annotated PNG and a clean no-text/no-number PNG whose non-text visuals
   match the full version.

11. **Run data-graphic consistency verification.** Before saving/presenting, build a
   small verification table for every displayed number and every data-encoding graphic.
   Each row must include: source value, displayed text, visual mark type, visual encoding
   rule, expected visual proportion/count/position/color, and actual rendered
   proportion/count/position/color. Verify that text numbers and graphics still represent
   the same values after image generation, compositing, resizing, cropping, or style
   polishing. If any generated illustration, object-as-chart, bar segment, area, icon
   count, axis, color block, leader line, or label has changed the value or suggests a
   different value, fix and re-render before output. Never accept a visually nicer chart
   that changes the data.

   Also run a label/geometry fit verification before accepting the render:
   - Treat layout QA as a deterministic pass, not a visual afterthought. During rendering,
     maintain a registry of bounding boxes for every readable text label and every
     non-text object that can collide with text: cards, panels, plot frames, arcs, gauges,
     connectors, dots, large decorative overlays, zero axes, bar tracks, bars, pills, and
     callout lines. After drawing or before saving, test intersections between text boxes
     and forbidden graphic boxes. If any forbidden overlap exists, reflow the layout,
     move the supporting graphic to a separate lane, shrink the decorative element, or
     remove the decorative element. Do not accept the image because it "looks close".
   - The registry must be operational code, not a written checklist only. Prefer
     `scripts/layout_guard.py` for PIL/canvas renders. For matplotlib renders, use the
     final renderer to obtain text extents and transform them into figure/canvas
     coordinates, then perform the same intersection checks. If the chart is rendered by a
     custom script, that script must either import the guard or implement the same
     `add_text_box -> add_graphic_box -> assert_clear` logic.
   - The render fails if any readable text or number has no registered bounding box. This
     prevents manual absolute-position text from bypassing collision QA.
   - Measure or estimate each readable label's bounding box after final font rendering.
   - If a value label is inside a bar/segment/object, the full bounding box must fit
     within that mark with enough padding on all sides. If it does not fit, move the
     value to a reserved external value column or outside callout. Never crop, truncate,
     hide, or let rounded ends/axis lines cover any digit or sign.
   - Check label-to-mark and label-to-label collisions. Text, numbers, group tags, and
     badges must not overlap plotted marks unless intentionally embedded with sufficient
     padding and contrast.
   - Check alignment pairs: a number and its bar/marker must share the intended baseline,
     centerline, or anchor. If a mark encodes the same metric as an adjacent number, they
     must read as one aligned unit, not as two unrelated layers.
   - Check connector binding. Every leader line, callout line, bracket, or dot-line must
     have a registered target mark and a registered label/text group. Verify the line's
     endpoints against those anchors after all image scaling/cropping/compositing. If
     either endpoint shifts away from the mark or label because the generated image was
     resized, the connector must be recomputed from the transformed anchors and
     re-rendered.
   - Check composite summary modules as a whole: explanatory text, chart marks,
     percentages, legends, formulas, and totals must use a shared baseline/subgrid and
     enough gutters. Formula tokens must be laid out by measured text widths, not by
     guessed fixed x positions.
   - For bars, columns, bullets, progress strips, and comparison bars, the endpoint shape
     must be visually integrated with the bar. Use one continuous rounded rectangle/path,
     or keep endpoint dots fully inside the bar silhouette. Do not add protruding dots,
     caps, or overlapping circles that create a spike/pointed tip unless the chart type
     explicitly uses arrows and the meaning is directional.
   - Decorative or ambient shapes behind text are allowed only when they are deliberately
     used as a background field with sufficient contrast and no hard edge crossing the
     text. If a translucent circle, gradient blob, arc, route, or overlay crosses behind
     small grey text, unit labels, source notes, or key numbers, move it away, lower its
     opacity until it is optically invisible under the text, or reserve a clean text lane.

12. **Run layout and aesthetic QA.** After rendering the complete PNG, inspect the final bitmap or a
    rendered preview at slide-view size. If the image contains any of these issues, revise
    and re-render before presenting:
    - title/subtitle/source text cropped by the canvas edge or hidden behind a panel;
    - adjacent panels/cards/plot areas closer than the planned gutter;
    - text touching or crowding a panel, card, pill, badge, or plot-area edge;
    - a badge/group tag placed so close to a category label that the two read as one
      broken label;
    - plot area starting before the label column has enough room for the longest label;
    - summary/decomposition modules where text, bars, percentages, formulas, and totals
      appear to float as unrelated layers or compete for the same horizontal space;
    - source/footnote lines visually colliding with bottom rules or canvas edge;
    - any visual boundary whose spacing is inconsistent with peer boundaries.
    When available and useful, run or mentally apply the `layout-design-check` skill after
    the first render as an external layout review. Use it for grid, hierarchy, whitespace,
    safe-area, and alignment criticism only; do not let it change the chart data, chart
    type, numbers, or the selected style. The chart must still pass this skill's own data
    and clean-PNG rules.

    Also run a `frontend-design` aesthetic review before accepting the PNG:
    - Does the image have a clear aesthetic point-of-view rather than a generic dashboard
      or AI-template feel?
    - Are typography, palette, spacing, background treatment, and visual details cohesive
      with the selected style and data topic?
    - Is there one memorable visual decision that supports the message without reducing
      readability?
    - Are texture, shadow, gradient, pattern, or decorative effects intentional and
      restrained enough for a presentation slide?
    If the design feels bland, default, overly template-like, or stylistically timid,
    revise the visual direction and re-render while preserving data accuracy and layout
    safety.

13. **Create the clean PNG by text removal only.** The clean image must be derived from the
   same layout and data-graphic rendering as the complete image. Do not redraw bars,
   charts, icon counts, object-as-chart shapes, swatches, or illustrations in neutral
   placeholder colors. If code renders the clean version separately, it must use the exact
   same visual parameters for every non-text layer and simply skip text/number drawing.

14. **Save PNG outputs only.** Save both PNG files to the outputs directory with clear
   names, e.g. `topic-styleN_complete.png` and `topic-styleN_clean.png`. Do not run
   `scripts/build_pptx.py` and do not output a PPTX unless the user explicitly asks.

15. **Run the QC checklist** (bottom of this file) before presenting.

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

## Style options (one-line identities)

Full specs in `references/`. Pick via `references/style-selection.md`.

**Basic options**

1. **Airy Systematic** (`style-1`) - minimal, white space, mint-teal + coral, alpha
   overlays. For annual reports / policy: "professional and calm".
2. **Corporate Gradient** (`style-4`) - inherited PPT background or light fallback;
   blue->purple gradient, flat, rounded, structure diagrams. The safe, neutral business
   default. Generated vector assets are optional, not mandatory.

**Upgrade options - require image generation**

3. **Retro Editorial** (`style-2`) - high-contrast, grid rules, riso/flat illustration,
   one of 5 muted recipes. For "opinionated, eye-catching".
4. **Metaphor Object** (`style-3`) - inherited PPT background or cream fallback; a real
   object IS the chart, witty original title. For "viral / single punchy stat".
5. **Magazine Monochrome** (`style-5`) - inherited PPT background plus one-hue system,
   rich chart variety, isometric pictograms, magazine masthead. For "deep single-topic
   data page".

## Frontend-Design Aesthetic Layer

Use the `frontend-design` skill as a portable aesthetic standard for static chart PNGs.
Do not import web-app behavior, motion, or UI controls; translate its principles into
infographic craft.

- Commit to a clear aesthetic point-of-view. Each chart should feel intentionally designed
  for its data topic and audience, not like a default chart template.
- Typography should have character while remaining legible at slide size. Use the chosen
  style's font tokens as the base, but tune weight, scale, line-height, contrast, and
  display/body pairing so the page has a designed hierarchy.
- Color should be confident and cohesive. Avoid timid evenly distributed palettes, random
  accents, generic purple-on-white gradients, or color effects that ignore the selected
  style. Dominant colors, neutrals, and accents must have roles.
- Spatial composition should have rhythm: generous negative space or controlled density,
  deliberate asymmetry when useful, clear focal areas, and no accidental card collage.
- Backgrounds and details should create context without stealing attention from data.
  Texture, grain, hatches, shadows, borders, overlays, and gradients are acceptable only
  when they match the style, topic, and information hierarchy.
- Memorability must serve comprehension. One strong visual decision is welcome; several
  unrelated decorative tricks are not. If a flourish makes comparison, reading order, or
  data accuracy weaker, remove it.

## Global Layout Rules

These rules apply to all five styles. Style references determine the visual language, but
these layout rules protect readability and structural quality.

- Establish a construction grid before rendering, but do not confuse construction with
  visible decoration. Use a 12-column grid, modular grid, or explicit coordinate system
  for alignment, spacing, and hierarchy. Every panel, chart area, title, group tag, and
  source note must attach to that system, but the final image should avoid obvious
  full-page grids, heavy box partitions, and hard mechanical dividers unless the user
  explicitly asks for a table-like technical sheet. Prefer implied grouping through
  whitespace, alignment, scale, color fields, texture shifts, continuous illustration,
  or shared baselines.
- Avoid hard separation as the default organizing method. Visible dividers, panel
  borders, and plot frames should be used only when they improve reading accuracy. When a
  continuous illustration, route, terrain, object, flow, or soft background field can
  group the data clearly, use that instead of boxed cells. If a visible rule is necessary,
  make it light, purposeful, and subordinate to the data, not the dominant visual system.
- Do not trace an already clear color-field boundary with an extra hard divider. If two
  background color blocks, texture zones, image crop regions, whitespace bands, or soft
  fields already separate sections, their contrast and spacing are the separator. Adding a
  dark rule, vertical bar, boxed edge, or outline directly on that boundary is redundant
  and usually makes the design feel stiff. Use a visible line only when it encodes a real
  semantic structure such as an axis, measurement reference, table rule, callout path, or
  reading-order guide that cannot be understood from color/space alone.
- Register soft grouping fields and divider lines as first-class layout objects. Any
  alternating row band, soft table stripe, colored section field, image crop boundary, or
  whitespace grouping field must be registered with
  `layout_guard.add_soft_grouping_field(...)`. Any visible horizontal/vertical rule,
  divider, row separator, panel separator, or plot frame stroke must be registered with
  `layout_guard.add_divider_line(...)` and given a semantic role. Decorative separators
  or row rules drawn over/along a registered soft grouping field fail the render. If the
  grouping is already clear from color fields, texture, or spacing, remove the line
  instead of lowering its opacity.
- Do not double-frame elements. If a chart mark, illustration fragment, pictogram, object,
  badge, or data shape already has its own outline/stroke, do not place a second outer
  rectangle or border around it merely to contain it. Use internal padding, shadow,
  background tone, clipping masks, or an unbordered label area instead. A second frame is
  allowed only when it has a different semantic role, such as a selected-state highlight
  or warning callout, and it must not look like an accidental duplicate border.
- Use a clear canvas safe area. As a default for 16:9 PNGs, keep all readable text at
  least 4% of canvas width away from the left/right edge and 4% of canvas height away
  from top/bottom edges, unless a style reference intentionally uses a full-bleed
  masthead. If text is larger than normal body text, increase safe area.
- Keep module gutters visible. Adjacent panels, cards, plot areas, and background blocks
  must have a gutter large enough to read as deliberate separation. As a default, the
  gutter should be at least the body-text line height or 2% of canvas width, whichever is
  larger. Panel edges must not visually kiss each other.
- Register same-level repeated containers as peer groups. Any horizontal or vertical set
  of cards, KPI tiles, label boxes, table cells, small multiples, row modules, or repeated
  visual containers that represents the same analytical level must be passed to
  `layout_guard.require_peer_rect_group(...)` or an equivalent assertion before output.
  This check must verify equal width/height, shared row or column baseline, no overlap,
  a declared minimum gutter, and near-equal spacing. Do not accept a row of peer cards
  because individual text fits; the group itself must read as one deliberate system.
- Do not hand-place peer card centers independently. Compute peer container positions
  from one grid formula: available span, item count, item width/height, and gutter. If the
  available span cannot fit the planned card width plus gutters, reduce the card width,
  reduce copy, split into two rows, or choose a different layout. Never solve the last
  item by nudging its center manually, because this creates the exact uneven/overlapping
  failure the peer-group check is meant to catch.
- Internal padding must scale with the container. Text inside cards, plot panels, boxed
  notes, badges, and pills needs balanced padding on every side. As a default, use at
  least 1.2x body-text line height for panel padding and at least 0.6x label line height
  for pills/badges. If the style is dense/editorial, density may increase, but text still
  cannot touch edges.
- Explanatory copy is a text block, not a label. Any instruction, reading guide,
  methodology note, or multi-clause sentence must be allocated a real paragraph zone with
  measured width and height. Do not place explanatory copy in a narrow side area and let
  it run horizontally until it is clipped. If the copy is longer than the zone, wrap it
  into deliberate lines, shorten the wording, or move the block to a wider zone.
- Visible copy must be source-locked before rendering. Build a short visible-copy
  manifest for title, subtitle, labels, formulas, notes, stamps, and source text, then
  render from that manifest instead of rewriting strings ad hoc in the drawing loop.
  Punctuation, arrows, separators, units, and spaces are part of the copy and must match
  the manifest. For Chinese presentation graphics, use typographic symbols such as `→`
  rather than ASCII placeholders such as `->`, unless the source data explicitly uses the
  ASCII form and the user wants it preserved.
- Chinese text wrapping must be designed before drawing. As defaults for 16:9 slide PNGs:
  keep explanatory/body copy between 9 and 18 Chinese characters per line when it is in a
  compact note, use line height of at least 1.25x font size, and leave at least 0.75x body
  line height between a paragraph and the next label/pill/module. Titles and short labels
  may be tighter, but they still need measured bounding boxes and safe padding.
- Do not crop text as a layout solution. If a text block's rendered bounding box extends
  beyond its allocated zone, panel, or canvas, the render fails. Reflow the block, shrink
  the whole typographic role consistently, or reserve more space. Never hide overflow with
  a mask, clipping rectangle, or image crop unless the text is intentionally decorative
  and not meant to be read.
- Label-to-pill spacing must show hierarchy. Section labels such as "right/left",
  "increase/decrease", or group headers need a distinct lane above or beside their
  related pill/bar/card. Keep at least 0.5x label line height between the label and the
  pill edge, and align the label to the pill's text or leading edge. A label should not
  visually stick to the pill it names.
- Reserve the longest-label column first. For horizontal bars, tables, slope charts,
  leader labels, and category lists, measure the longest category label and allocate a
  fixed label column before placing the plot area. Group tags/badges sit in their own
  lane or outside the label column; they must never compress, cover, or split category
  text.
- For row-based charts, bind the entire row across columns. Each data item must have a
  declared row id, row slot, and row centerline before rendering. The left text module,
  middle connector/callout module, and right visual mark/module for that item must all
  reference the same row id and align to the same centerline or declared baseline
  relationship. Do not position label text, connector lines, and bars/trails as three
  independent layers that merely look close. If the left text block is taller than the
  mark, its bounding-box center or named anchor must still align to the row centerline,
  with consistent offsets for name, subtitle, value, unit, and metadata across all rows.
- Row centerlines must be designed, not inherited blindly. If a generated image contains
  bars, trails, objects, or segments at uneven vertical positions, do not let those
  positions automatically dictate the typography. Build a row rhythm first from the
  readable text stack height, header clearance, and desired scan order; then crop/scale
  the image, move connectors, or regenerate the asset so the visual marks fit the row
  rhythm. If the image asset cannot support readable row rhythm, treat it as a failed
  layout input rather than forcing text into awkward gaps.
- Repeated rows need an explicit vertical rhythm check. Unless row spacing encodes a real
  data dimension or a clearly documented hierarchy, peer rows should use equal or near-
  equal centerline gaps. As a default, the largest peer-row center gap should not exceed
  the smallest by more than 15%. If a generated illustration creates larger uneven gaps,
  redesign the composition, crop/scale/reposition the image, or regenerate the asset.
  Do not accept the render simply because every label is attached to its corresponding
  mark.
- Row text modules need their own frontend-design text stack. Within each row, name/title,
  secondary label, focal value, unit, and metadata must be laid out from measured text
  boxes with declared gaps and shared baselines. The large value and unit must read as one
  numeric phrase; metadata must occupy a separate lane with a clear gutter. A row fails if
  any text role touches, overlaps, visually sits on top of another role, or steals the
  baseline of a larger role. Do not make row-level centerline alignment by compressing
  the text stack until the typography becomes chaotic.
- Row text modules must share the page's typographic alignment spine. In a ranking/list,
  every repeated row should use the same x positions for marker, name/caption, value,
  unit, and metadata lanes. Header and row text should share the main text spine unless
  there is a documented visual reason for an offset. Avoid ad-hoc optical placement such
  as a title aligned to the page margin while all data rows start after a rank marker; it
  makes the page feel unstructured even when individual text boxes do not collide.
- Reserve a value-label lane. If values are outside marks, use a fixed value column or
  direct-label lane. If values are inside marks, they must pass the label-fit check; if
  the mark is too short or too narrow, move the value outside instead of shrinking it
  below legible size.
- For diverging bars, reserve four lanes before drawing: category labels, negative value
  labels, the bar plot area with the zero axis, and positive value labels. Measure the
  longest category label and the widest negative value label first; add a visible gutter
  between them. Never let a negative value label sit immediately after or on top of a long
  category label, and never let either lane overlap the plot area's left edge.
- Composite summary modules need their own subgrid. Any module that combines a section
  title, explanatory copy, bar/segment/proportion mark, percentages, legend labels,
  formula, total, or note must be split into explicit zones before drawing. Typical zones
  are: left explanation column, center data-mark column, right formula/total column, plus
  optional legend/percentage row. Each zone needs fixed width, internal padding, and a
  gutter to neighboring zones. Do not let the data mark and formula compete for the same
  row unless the formula is intentionally the primary graphic.
- Header summary modules also need a local subgrid, even when they look text-only. The
  headline, conclusion phrase, subtitle, and formula/context note must share declared
  block spines and vertical rhythm. Their internal words, values, operators, and units
  should follow natural typographic grouping rather than being pulled into artificial
  columns. Align internal value/result lanes only when the design is explicitly a table,
  ledger, scorecard, or comparison grid.
- Composite formulas and relationship notes must be placed by semantic ownership, not by
  leftover whitespace. If a formula combines child metrics to explain a parent or outcome
  value, it belongs to the parent/outcome module, merge point, or summary strip. It must
  not be placed inside one child metric's local module because that visually attributes
  the parent relationship to the child. In custom renderers, declare semantic modules
  with `layout_guard.add_semantic_module(...)` and require formula/context items with
  `layout_guard.require_semantic_owner(...)` or an equivalent check before saving.
- KPI cards and headline-number modules need their own subgrid too. Large numbers,
  units, comparison dots, gauges, sparklines, arcs, notes, and callout lines must occupy
  separate measured lanes or be intentionally embedded with enough contrast and padding.
  Do not place a decorative gauge, arc, connector, or dot behind or through a large number
  unless the number's rendered bounding box has been measured and the overlap is designed
  for legibility. If the KPI number is the focal element, move the supporting graphic to a
  side/bottom lane rather than using it as a background shape under the digits.
- Avoid nested card backgrounds. If a module has a visible or semi-visible rounded
  rectangle, do not draw another same-shape rounded rectangle behind it in nearly the same
  position, opacity, and size. This creates a multi-border/double-card effect even without
  explicit outlines. Use one card surface plus separate soft ambient overlays that do not
  trace the same contour.
- Register and test element bounds. Any render script or manual composition must keep a
  simple list of occupied rectangles for text and collision-relevant graphics. Text boxes
  may overlap only approved text backgrounds, such as their own card surface or a
  deliberately placed label pill. They must not overlap chart marks, decorative arcs,
  connector dots, track outlines, zero axes, hard edges of ambient blobs, neighboring
  labels, or panel/card edges. When a collision is detected, change the layout system,
  not just the color.
- Register visible separators in the same guard pass. Soft grouping fields and divider
  lines must be declared before final `assert_clear()`. A row background/alternating band
  plus a row divider is allowed only when the divider has a necessary semantic function
  that color/spacing cannot provide; otherwise `layout_guard.add_divider_line(...)`
  should make the render fail and the script should remove the divider.
- Register container boundaries, not only data marks. Row backgrounds, alternating table
  bands, cards, pills, plot panels, summary strips, and soft color fields are still real
  layout containers even when they are pale or borderless. Any text visually placed
  inside one of these containers must have a measured text stack and must pass
  `layout_guard.require_inside(...)` against that container with explicit padding. Do not
  draw a rounded row band and then place value labels or notes by absolute coordinates
  without checking their union bbox against the band. If the text touches or crosses the
  rounded corner, row edge, panel boundary, or table boundary, the render fails even when
  the text does not overlap a chart mark.
- Soft grouping is not enough for text-bearing fields. If a row band, table header,
  badge, pill, label cell, value cell, or summary strip contains readable text, register
  it as a text container with `layout_guard.add_text_container(...)`, then bind the
  measured text bbox or text-stack union with
  `layout_guard.require_text_stack_inside_container(...)`. A field registered only with
  `add_soft_grouping_field(...)` is treated as a visual grouping field, not as proof that
  its text has safe padding. Table headers and pills must be checked cell by cell, not
  only against the full header band, because text can touch the bottom/side of one cell
  even when the whole band looks large enough.
  `layout_guard.assert_clear()` also auto-checks any registered text box that intersects
  a registered text container, so unbound text inside a text container still fails if it
  violates the declared padding. This automatic check is the backstop; explicit
  `require_text_stack_inside_container(...)` remains required for multi-line text stacks
  because it checks the group as one typographic block.
- Container checks must include neighboring containers and neighboring text stacks. It is
  not enough for a row band/card to contain its own text; that band/card must also stay
  out of the previous and next rows' readable text safe areas. For alternating table
  bands, row backgrounds, and grouped color fields, measure every row's text stack and
  every background band, then verify a minimum vertical/horizontal gap between each band
  and all non-owned text stacks. In custom renderers, use
  `layout_guard.require_rect_clearance(...)` for this check; it is stricter than a
  one-direction vertical-gap check because it catches edge-kissing, corner contact, and
  horizontal/vertical boundary contact. If a band's rounded corner, fill edge, or table
  boundary touches the previous row's note or the next row's value, shrink the band,
  increase row spacing, move the text stack, or remove the band. Do not accept a render
  because the band is pale or because the text remains technically readable.
- Value columns and note columns need declared cells. Outside value labels, right-side
  notes, remarks, units, and metadata must be placed inside a reserved value/note cell
  with measured left/right/top/bottom padding. The renderer must check the union bbox of
  the value phrase plus its note against that cell. If the longest note cannot fit with
  padding, widen the cell, wrap/shorten the note, reduce the whole note role, or move the
  note to a separate lane; do not let it run into a table/background boundary.
- Treat the "approved text background" exception as strictly scoped. A circle, bubble,
  badge, pill, label background, or colored dot may be allowed to sit behind the text it
  owns, but that does not make it invisible to the rest of the layout. It must still fit
  completely inside its declared cell/row/card/module with padding, and it must not cover
  table headers, row rules, neighboring rows, adjacent labels, other chart marks, or
  unrelated text. In custom renderers, after drawing an allowed text background, also
  call `layout_guard.require_inside(...)` against its owning cell/module and keep the
  owner relationship explicit. Do not register a data mark as `allowed_background` merely
  to silence a collision error.
- For matrix, table, and row-based charts, data dots/bubbles must be sized from the cell
  geometry before they are sized for style. The maximum marker diameter plus stroke and
  padding must be smaller than the row height and column width allocated to that cell. If
  a circle large enough to contain text would touch row separators, headers, or adjacent
  cells, remove the internal text and use an external legend/direct label instead of
  enlarging the circle. A text-inside-marker design is allowed only when both the marker
  and the text fit inside the cell's safe area.
- Register connector anchors, not just connector lines. Any leader line, callout line,
  bracket, arrow, or dot-line must bind to named objects in the render data: a mark
  anchor and a label anchor. Anchors should be computed from the actual drawn geometry
  after scale/crop transforms: segment centroid, edge midpoint, bar endpoint, dot center,
  object hotspot, label-group edge midpoint, or text-box centerline. Do not draw
  connectors from independent hard-coded x/y coordinates unless those coordinates are
  derived from registered anchors in the same coordinate system.
- A connector must point to **both** sides of the relationship: one end belongs to the
  data label/value group, and the other end belongs to the corresponding visual
  mark/graphic. The data-side endpoint must be anchored to the specific number, label
  group, formula token, or callout that states the value; the graphic-side endpoint must
  be anchored to the exact bar, segment, color field, route, object part, pictogram,
  generated-image detail, or visual mark that represents that same value. A line that
  only points at empty space near the label, only points at a decorative dot, or only
  points at a general topic illustration is not a valid connector.
- Connector endpoint boxes must come from real rendered objects. Do not define a tiny
  arbitrary anchor box in empty space and call it the data side or graphic side. The
  data-side keepout/anchor must be derived from the measured bounding box of the exact
  number, unit, formula token, or label group. The graphic-side keepout/anchor must be
  derived from the actual data-bearing mark: bar/segment bounds, color-field edge, route
  stroke corridor, object part, pictogram, orbit/ring, dot, or verified generated-image
  hotspot. In `layout_guard.py`, prefer `add_measured_connector_path(...)` for ordinary
  data-to-graphic leaders; it derives legal anchor zones from the measured label and mark
  boxes and checks both `min_endpoint_gap` and `max_endpoint_gap`. Use
  `add_bound_connector_path(...)` only for non-rectangular marks after you have computed
  real mark hotspots/edge corridors from the drawn geometry. A connector endpoint that is
  merely floating between two antlers, over blank background, or near a general scene
  detail fails even if it sits inside a manually declared zone.
- Register connector paths and no-cross zones before drawing. Any leader line, callout
  line, bracket, arrow, or dot-line is itself a collision-relevant object, not harmless
  decoration. In PIL/custom renderers, use `scripts/layout_guard.py` methods such as
  `add_connector_path(...)`, `add_measured_connector_path(...)`,
  `add_bound_connector_path(...)`, and
  `add_no_cross_zone(...)` or an equivalent implementation.
  Register every readable number, formula, unit, source note, and label group as text
  boxes; register subject-dense image regions such as animal bodies, faces, product
  heroes, important generated-object details, chart marks, and pictogram clusters as
  no-cross zones. A connector may touch only its declared label anchor and target mark
  anchor; its intermediate path must not cross text, digits, formulas, units, dense
  subject areas, faces/bodies, or key illustration details.
- Route connectors through the shortest available negative-space corridor between the
  data label and its corresponding graphic. The default connector is the shortest path
  that stays in empty background, whitespace, or a deliberately reserved annotation lane.
  **Prefer a single straight segment** between the nearest valid point on the data label
  and the nearest valid point on the corresponding graphic. Do not add a bend, dogleg,
  bracket shape, scenic route, or decorative endpoint dot when a short straight connector
  would work. Only use an elbow/bracket path when the straight segment would cross
  readable text, dense subject matter, or a forbidden graphic zone; the elbow must then be
  the shortest available detour through blank space. Long strokes that slice through the
  hero object, herd, portrait, product, data-shaped object, or picture detail fail even
  when their endpoints are correct. If the shortest direct corridor is blocked, first move
  the label closer to the target or choose a nearer edge anchor; then use the shortest
  elbow/bracket path that remains in blank space. If no clean corridor exists, use a
  nearby label, bracket, edge tick, or regenerate/re-crop the image with a clearer callout
  landing zone. Never solve this by drawing a line over the image with higher opacity.
- Connector route priority is orthogonal before diagonal. In this skill, "straight
  connector" means a single horizontal or vertical segment whenever the label and target
  can be aligned by choosing a nearer label edge, mark edge, or reserved connector lane.
  First try a single horizontal/vertical line. If that would cross text, digits, dense
  illustration, or the wrong data mark, use the shortest right-angle elbow through blank
  space. Use an oblique/diagonal line only as a last resort after both orthogonal options
  fail, and document the reason in the connector binding table. Do not accept a slanted
  line merely because it is mathematically shorter; slanted leaders often look arbitrary
  and should not be the default.
- Keep connector endpoints slightly detached from both ends. A leader line should
  visually connect the label and the target graphic, but its stroke should stop short of
  the readable digits/text and stop short of the data-bearing graphic/object edge by a
  small, consistent gap. As a default for 16:9 PNGs, leave about 8-16 px at each end
  after final scaling, or at least half the connector dot radius when endpoint dots are
  used. The line may terminate in a small dot placed in the blank gap beside the label or
  near the mark, but that dot must not cover a digit, unit, animal/body detail, or
  data-bearing color region. Endpoint dots are optional; omit them when they make the
  connector look like two floating markers instead of a simple relation. In custom
  renderers, pass label/target keepout rectangles and `min_endpoint_gap` to
  `add_bound_connector_path(...)` or implement the same check.
- Do not replace a required connector with a legend marker. A colored dot, swatch, tick,
  or underline beside the label is only valid when the data-bearing mark is immediately
  adjacent to that label and the two read as one local unit. If the corresponding mark is
  elsewhere in the image, the label still needs a visible connection through negative
  space: a short routed leader, bracket, haloed target dot, or edge-following path whose
  start and end are registered as semantic anchors. Removing the line because it crossed
  content is not a fix; first redesign the label position, reserve an annotation lane, or
  choose a nearer mark anchor so the connector can route cleanly.
- Plan connector corridors before final label placement. For every callout, reserve three
  things together: the label zone, the target anchor zone on the actual data mark, and a
  clear route between them. If the route would cross formulas, labels, animal/person
  bodies, product heroes, or dense illustration details, move the label to the same side
  as the target, attach it to a closer edge of the mark, or change from a long leader to a
  bracket/halo placed in nearby whitespace. Do not place all labels first and then try to
  draw whatever line fits afterward.
- For generated data illustrations, reserve callout landing zones in the image concept.
  If a generated color flow, object segment, route, plume, slice, or data-shaped mark will
  need external labels, the image prompt and crop plan must leave at least one visible
  clean edge or endpoint for each important mark where a connector can land without
  crossing the subject. Do not let every data-bearing region sit underneath animal
  bodies, faces, product silhouettes, or dense object details. If the accepted generated
  image hides all usable target anchors under the subject, either regenerate with clearer
  label corridors, move labels directly onto/next to the mark with adequate contrast, or
  redesign the annotation system. Do not force connectors into the dense subject area.
- Align connector systems before drawing them. When several peer rows or modules use
  leader lines, define a connector lane with shared start or end coordinates before
  rendering. At least one side of the connector set should align to a common vertical or
  horizontal guide unless the chart is intentionally radial/freeform. Horizontal row
  connectors should share the same label-side x coordinate or the same mark-side x
  coordinate; vertical callouts should share the same baseline or target rail. Avoid
  zigzagging, uneven connector starts, and arbitrary line lengths that make annotations
  look hand-placed rather than bound to the layout system.
- Connector endpoints must visibly meet their targets. A leader line may terminate at a
  dot placed on the mark, at the mark edge, or at a label anchor dot, but it cannot hover
  near the target. When a line points to a color block or generated-object segment, the
  dot must sit inside the data-bearing colored region, not on a nearby shadow, border,
  background, or unrelated texture. When the line points to text, it must meet the label
  group's edge or anchor dot with consistent padding.
- Connector endpoint markers must use one declared geometry. In a connector group, both
  endpoint dots and all peer connector dots must share the same radius, stroke, fill
  rule, and optical weight unless a deliberate hierarchy encoding is documented. Do not
  mix a small label-side dot with a larger mark-side dot by accident. If one endpoint
  needs a different marker, use a different semantic shape and explain why in the
  connector binding table.
- Row connectors must be bound to row modules, not only to marks. In horizontal
  row-based compositions, the connector y coordinate must equal the row centerline used
  by the corresponding left text module and right mark module, unless a documented label
  baseline anchor is intentionally used. The renderer should verify
  `text_row_anchor_y == connector_y == mark_anchor_y` within a small tolerance for every
  row. If an image asset's bar/trail centerline does not match the text row, move the
  text row, connector, or image crop together; do not leave one column drifting.
- The element-bound registry is mandatory implementation, not optional documentation.
  Use `scripts/layout_guard.py` or equivalent code in every custom PNG renderer. The
  renderer should raise an error before saving/presenting if text boxes collide with
  forbidden graphics, card/plot edges, rails, axes, or neighboring labels. Manual
  coordinate nudges are allowed only after the failing collision report identifies the
  exact zones to reflow.
- Protect focal numbers and unit/source labels with reserved clean lanes. Decorative arcs,
  translucent circles, route strokes, sparkline markers, and ambient fields may approach
  these lanes only after their hard edges and visible color transitions are registered as
  forbidden graphics. If a supporting shape is purely decorative and competes with a
  focal number, remove the shape rather than moving the number into a compromised area.
- Formulas and mixed numeric phrases must be measured, not guessed. Lay out tokens such
  as `4058`, `母羊`, `+`, `1132`, `=`, `5190`, and units by reading each rendered text
  bounding box and adding consistent gaps. Never hard-code every token's x coordinate by
  eye. If the measured formula does not fit, stack it vertically, reduce the whole
  formula group as one unit, move it to a separate row, or simplify the module.
- Formula operators must match the semantic relation. Use `=` for arithmetic equality,
  `+`/`-` for calculation components, and arrows only for sequence, movement,
  transformation, or flow. Do not mix a calculation expression on the left with a process
  arrow on the right merely to avoid repeating a result. If the formula would need the
  same result already shown in the title, either allow a compact subordinate `= result`
  for correctness or rewrite the whole line as non-formula prose.
- Inline formulas and mixed numeric phrases must align token bboxes to a shared visual
  centerline. Mixed fonts make numbers, Chinese words, and operators sit at different
  optical heights when they share only a raw y coordinate. Draw from measured token
  centers and verify with `layout_guard.require_inline_centerline(...)` or an equivalent
  check.
- When a formula, arithmetic explanation, or numeric phrase describes a value already
  encoded by a graphic, keep it as a compact label or verification note attached to that
  graphic. Do not let the formula become a second full expression of the same dataset. If
  the formula itself is the clearest primary expression, remove or greatly simplify the
  competing mark instead of giving both equal weight in the same tight lane.
- Avoid duplicate encodings inside one chart. A data point may have a visual mark plus a
  direct label, but the same full dataset should not appear as both a full chart and a
  full table, both a line and a complete bar series, both a pictogram field and a full
  duplicate ranking list, or both an object-as-chart and a separate conventional chart.
  Use the secondary space for interpretation, selected annotations, context, or sources.
- Treat rails, baselines, zero axes, plot frames, guide tracks, and pale background bars
  as part of the graphic framework. A value label is not "outside the mark" if it still
  sits on top of a rail/track or touches the zero-axis/frame. Outside labels must occupy
  a genuinely empty value lane beyond the rail/plot framework, or the rail must be
  shortened/segmented to leave a clean label gap.
- Do not draw empty bar tracks or outline rails by default. If the colored bar itself
  already communicates the value and the empty remainder has no analytical meaning
  (target, capacity, benchmark, maximum, forecast, or missing share), remove the empty
  track/outline. Empty rounded outlines often create useless borders and collide with
  value labels. Use only the data-bearing colored bar plus a clean baseline/zero axis or
  faint reference grid when needed.
- For labels placed inside bars or segments, reserve padding against the real visible
  shape, including rounded caps. The label's bounding box must stay clear of the rounded
  end, zero-axis, and any rail/frame by at least 0.5x label line height. Do not place
  in-bar labels near the terminal cap merely because the text technically fits.
- Titles and subtitles must not be trapped under panels. Header text should occupy its
  own vertical zone before panels begin. If a large title overlaps a panel or appears
  cropped by a panel edge, increase the header height, wrap the title/subtitle, or reduce
  panel height.
- Avoid edge-hugging badges. Pills, group labels, stamps, and callouts need space from
  nearby panel edges and neighboring labels. If a badge marks a group of rows, align it
  to the group's vertical center or start line in a separate margin lane.
- Stamps, seals, badges, and circular labels are real text containers, not decorative
  leftovers. Their internal text must use a measured text-stack contract just like a card
  or row module: line order, font sizes, line heights, gaps, center/alignment, and an
  inner safe area must be declared before drawing. Do not place three or more text lines
  inside a circle by hard-coded y offsets. If the text cannot fit with balanced padding,
  enlarge the stamp, reduce or split the copy, remove internal dividers, or move secondary
  details outside the stamp. Separator rules inside stamps must never cross, touch, or
  visually crowd readable text.
- Centered stamps, seals, badges, and circular labels must be centered by the final
  rendered text bounding box, not by guessed line-height math. First measure all internal
  text lines, union their bboxes, then align that union bbox to the circle/card center
  within a small tolerance. In custom renderers, use
  `layout_guard.require_centered_in(...)` or an equivalent assertion. A badge can pass
  inside/safe-area checks and still fail if its text block is optically above, below, or
  off-center within the container.
- At slide-view size, scan from top-left to bottom-right: no boundary should feel like it
  accidentally slices through text, no text should feel squeezed into a shape, and no two
  frames should be so close that their relationship is ambiguous.

## Data-Art Integration Rules

These rules apply globally whenever illustration, generated imagery, object-as-chart,
pictograms, or editorial art is used.

- Basic and upgrade options have different priorities. In basic options, the chart or
  diagram is the product and visual polish serves clarity. In upgrade options, the
  generated data-themed illustration is the first material artifact and the main visual
  premise; the final page is composed around that illustration with exact labels,
  auxiliary marks, source notes, and supporting data. Upgrade work should not start by
  finishing a conventional chart and later adding art.
- Design the chart as one image system first. The data structure and the illustration
  structure must be planned together before any image prompt is written. Do not begin with
  a conventional chart and then place a decorative illustration in leftover space.
- Every illustrated system needs one dominant visual subject. The title may contain
  several nouns, but the image prompt must choose which noun carries the message and which
  nouns are only context. Secondary elements should support the primary subject as
  background, shadow, trail, small marker, environment, or label anchor. Remove secondary
  elements when they make the visual harder to read, less beautiful, or emotionally odd.
- Multi-category topics need one shared visual carrier. When the data compares or relates
  two or more categories, first find their common parent subject instead of illustrating
  each category literally. The image should usually be built around one shared object,
  scene, process, or field that all categories belong to. Category differences may become
  states of that carrier (open/closed, whole/broken, thick/thin, filled/empty,
  connected/separated), attached marks, layers, gaps, shadows, or label anchors. Avoid
  prompts that stack several category symbols into one image, such as ring + broken
  heart + courthouse + ledger, because the result reads as a crowded collage rather than
  one data idea.
- Do not force keyword fusion. Combining two concepts into one body is allowed only when
  the fusion is natural to the object and immediately legible, such as a container with a
  fill level or a route drawn beside a migrating subject. It is not allowed when it creates
  an uncanny hybrid, such as an animal whose body becomes a road, a person-object chimera,
  or a topic object mutated by an unrelated contextual noun. When in doubt, keep the
  primary subject intact and express the secondary element outside it or omit it.
- Run a visual simplicity test before image generation. The illustration should be
  describable in one short phrase, with one main subject and one data behavior. If the
  prompt needs multiple metaphors, multiple hero objects, or a long explanation to make
  sense, simplify the data-art concept: keep the primary subject, keep the numeric
  relationship, and remove decorative/contextual nouns.
- For upgrade styles, first ask whether the entire dataset can become one continuous
  illustration system. Timelines should usually become a continuous route, plume,
  river/flow, layered terrain, procession, orbit, shelf, ledger, or evolving scene whose
  shape changes across the full canvas; rankings can become a continuous slope, stack,
  landscape, market shelf, or object family; compositions can become one segmented
  object/field. Use separate cells only when the data genuinely requires independent
  peer modules. A set of boxed mini-scenes is a fallback, not the default.
- When generating illustration for upgrade styles, prompt for the whole data relationship
  at once before requesting separate icons or spot assets. The image prompt must describe
  how all key values relate in one continuous visual idea, such as rising height with a
  temporary dip, diverging positive/negative flow, segment thickness by share, or density
  by magnitude. Do not generate isolated decorative assets first and then try to arrange
  them around a chart.
- Use a **data-to-image visual translation** before prompting. Ask: "If the numbers had a
  physical form, what would change?" Map values or relationships to visible properties:
  height, width, area, volume, count, density, length, fill level, route length, stack
  height, layer thickness, plume size, terrain mass, beam width, orbit radius, or flow
  thickness. The generated image should be shaped by that mapping, while exact labels and
  final numeric values remain code-controlled unless the generated object is explicitly
  verified as the data mark.
- Before choosing a physical form, run a relationship-to-encoding compatibility check.
  Segments/slices/fills mean additive parts or comparable peer quantities. Routes/flows
  mean sequence, movement, or conversion. Object count means countable units. A focal
  object plus small attached marker means summary plus context. Do not encode an event
  milestone, a cumulative period total, and a derived outcome as three same-status color
  areas on one body merely because all are numbers. If relationship types differ, the
  picture must show hierarchy and process, not pretend the values are a proportional
  composition.
- Require dual expression. For every important illustrated data point, the number and the
  picture must express the same claim. The number provides exact reading; the image gives
  intuitive reading. If the image only says "this topic is about factories / travel /
  finance / animals" but does not express the specific relationship, it is not integrated
  enough.
- Dual expression is not duplicate storytelling. The image or chart mark is the primary
  expression; the number is an exact label attached to that mark. Do not add a second
  complete chart/table/formula that restates the same values. If exact lookup is required,
  make it a deliberate appendix-like module, visually subordinate and requested by the
  user.
- One dataset should not run on parallel rails. For example, a CO2 timeline can be a
  data-shaped smoke/terrain sequence with year/value/event callouts, or it can be a line
  chart with selected event annotations. It should not also carry a complete right-side
  year-value table that repeats every point. A tourism transport composition can be an
  isotype/stacked composition with direct labels, not the same composition repeated as a
  second bar list. A metaphor object can carry segments with exact labels, not a duplicate
  conventional chart beside it.
- Illustration must have a data role. Valid roles include:
  - **cell content**: fills or partially fills timeline/grid/table cells that correspond
    to specific events or categories;
  - **data mark**: becomes a pictogram unit, icon count, segment, object slice, route,
    drawer, layer, or category marker;
  - **context anchor**: frames the exact chart module it explains, such as a factory
    behind an emissions timeline or a transport motif inside a transport composition;
  - **hierarchy cue**: visually distinguishes the focal/summary module from supporting
    modules without changing the data;
  - **background texture**: supports the selected style while staying clearly subordinate
    and never pretending to encode values.
  Invalid roles include: corner decoration, generic topic art, stock-like scene, repeated
  icons for symmetry, or an unrelated picture used to fill empty space.
- Treat **context anchor** as a weak role unless paired with data shape. A factory behind a
  CO2 trend, a train beside transport data, or a bank vault beside deposit data is only
  acceptable when it is also shaped, segmented, scaled, counted, or positioned according
  to the data relationship. Otherwise it is topic decoration and should be removed or
  redesigned.
- Match data form to style form. A timeline/event table should become a timeline grid,
  editorial strip, route, continuous terrain, flow, or annotated sequence when the
  selected style's references use those forms. A composition dataset should become stacked
  segments, object layers, isotype units, or a clear part-to-whole module. A single punchy
  metric may become an object-as-chart. Do not default to a line/bar chart if the style
  reference offers a clearer and more integrated structure for the same data type.
- Generated assets must be modular when the layout is modular. If the page is a grid,
  first test whether a continuous data illustration can pass through the modules and
  visually bind them together. If separate modules are still necessary, generate
  cell-level assets or a background system that aligns to the grid; do not generate one
  unrelated full illustration and paste it into a random cell. If the page is an
  object-as-chart, generate the object and its data-bearing divisions as one coherent
  object, not a clean object plus flat overlays.
- Prefer generated **data-shaped image systems** over generated decorative assets. For
  rankings, generate comparable objects/terrain/plumes/stacks with relative sizes. For
  timelines, prefer one continuous evolving strip/route/terrain/plume/scene whose visual
  density/height/volume changes across time; use evolving cells only when discrete
  episode comparison is clearer. For compositions, generate segmented objects or
  pictogram fields. For flows, generate routes, streams, beams, or corridors whose
  thickness/length follows the data. Code-rendered marks may refine or verify the same
  mapping, but should not look like a separate layer pasted on top of an unrelated
  picture.
- Art quality is part of chart quality. Check whether the illustration improves
  comprehension, adds visual rhythm, and matches the style references in density,
  material, palette, crop, perspective, and line/texture treatment. If the page becomes
  less readable or less coherent after adding illustration, revise the art direction or
  remove the illustration.
- Exact data remains code-controlled unless the generated image itself is explicitly the
  data mark and has been verified. For most generated scenes, all numbers, labels,
  proportions, axes, bars, lines, and segments should be rendered by code or structured
  chart logic on top of, beside, or within reserved blank zones.
- A generated illustration is a required source asset, not a loose reference. If image
  generation succeeds for an upgrade style, the final PNG must use the generated asset
  itself as the illustration layer, cropped/composited into the design. Do not recreate,
  trace, approximate, or "simulate" that illustration with PIL/SVG/canvas/code-drawn
  shapes. Code may add exact labels, leader lines, masks, crop frames, subtle overlays,
  and verified chart marks, but it must not replace the generated illustration's visual
  substance.
- For upgrade styles, code may not create data-bearing colored regions by clipping flat
  fills into a generated silhouette, recoloring object parts, or painting new segments on
  top of the generated asset. That is still a post-hoc overlay even if it is clipped to
  the object's shape. If the generated image lacks the required integrated data fields,
  regenerate the image, use the object as contextual only with separate code-controlled
  marks, or ask the user to approve a fallback.
- When a user supplies style reference images, extract the structural method in addition
  to the look: grid rhythm, illustration placement, data module hierarchy, crop behavior,
  image/data overlap, and label system. Do not copy the subject or composition, but do
  apply the same level of integration.

### Hard rejection patterns

Reject and re-plan before rendering if any of these patterns appear:

- A normal chart is finished first, then an illustration is added to unused space.
- The illustration could be removed without changing how the viewer reads the data.
- The same dataset is fully expressed twice, such as data-shaped art plus a full line
  chart, a chart plus a full source table, or a pictorial ranking plus a duplicate bar
  ranking, without a user-requested lookup purpose.
- The same exact source number appears as both a title/headline number and a separate
  large KPI/focal-number module. This is duplicate numeric emphasis, not calibration.
  Either remove the number from the title or remove the separate big-number module.
- The same exact source number appears in the title/headline and is repeated again in a
  formula, note, label, or annotation when the repeated instance is not strictly required
  for arithmetic/provenance verification. Prefer relationship wording that does not repeat
  the title number.
- A formula, relationship note, or explanatory annotation is visually placed in the wrong
  semantic module. Examples: a parent total's composition note appears under one child
  component; a benchmark explanation sits inside a category row it does not belong to; a
  process note is placed next to an unrelated event marker only because the space was
  empty.
- Visible text, punctuation, units, or formula operators are rewritten by the renderer
  instead of coming from the approved visible-copy manifest. This includes using ASCII
  fallbacks such as `->`, `|`, or `-` where the intended Chinese typography requires
  `→`, `｜`, `—`, or another source-approved symbol.
- A calculation phrase uses a process arrow instead of an equality operator, such as
  `4058 + 1132 → 回迁`, when the left side is arithmetic. This is a formula-grammar
  failure. Use `=` with a valid result, or rewrite as prose without arithmetic operators.
- Formula tokens are drawn on mismatched optical baselines/centerlines, making an
  operator such as `=`, `+`, or `→` float above or below adjacent numbers and words.
- The illustration depicts the topic but not the data relationship, e.g. a generic factory
  for emissions, a generic animal for wildlife counts, or a generic bank object for
  deposits.
- The image fuses a primary subject with a secondary/contextual element into an awkward
  hybrid when the secondary element could have been a small marker, background, route,
  trail, shadow, label anchor, or omitted entirely.
- The data mark and image use unrelated forms: a precise line/bar chart floats above or
  beside a picture that has no matching shape, scale, count, or segmentation.
- Mixed relationship values are forced into one proportional encoding. For example, a
  first-arrival event, a cumulative migration total, and a return outcome are colored as
  if they were peer parts of one animal, one bar, or one composition.
- Code has repainted, recolored, clipped flat fills, or drawn new data-bearing segments
  onto a generated object to make it appear data-integrated after the fact. Integrated
  object data fields must come from the generated asset itself unless the user explicitly
  approves a labeled fallback.
- A chart relies on obvious full-page grids, hard boxed cells, or heavy dividing lines as
  its main visual idea when the data could be read through a continuous illustration,
  implied alignment, whitespace, or softer grouping.
- A dark divider, vertical bar, outline, or rule is drawn exactly along the boundary
  between two already distinct color fields, texture fields, image crops, or whitespace
  zones without adding a specific semantic reading function.
- A timeline or multi-point dataset is split into many isolated mini-scenes before
  testing a continuous data illustration that expresses the whole change across the page.
- An outlined chart mark, illustrated object, pictogram, or data shape is placed inside an
  additional outer rectangle/border that repeats the same containment role and creates a
  double-frame effect.
- Peer data modules use different visual grammars only because one module has a picture.
- A generated asset is generic topic art instead of a data-specific cell, unit, object,
  context anchor, or hierarchy cue.
- A generated full-page template dictates fake frames, fake labels, or cropped art that
  the real data cannot fit.
- Image generation produced a usable illustration, but the final chart replaces it with a
  hand-coded or manually drawn imitation instead of compositing the generated asset.
- The selected style has a reference for the same data form, but the design ignores that
  structure without a clear readability reason.
- Exact numbers depend on unverified generated-image geometry when they could be handled
  by code-controlled marks.
- Leader lines, connector dots, brackets, or callout rays are drawn as decorative strokes
  instead of bound annotations: they do not touch the intended data-bearing mark, point to
  the wrong color block/object region, stop before the corresponding text group, or remain
  fixed after the image asset was resized/cropped.
- A connector points to only one side of the relationship. Examples: it starts from a dot
  that is not attached to the data label/value group; it ends in empty background rather
  than the corresponding data mark; it points to a general illustration instead of the
  exact bar/segment/color field/object part; or it visually suggests a relationship
  between the wrong number and the wrong graphic.
- A connector endpoint is validated only against an arbitrary hand-made zone rather than
  the measured text/value box or actual data-mark geometry. This includes endpoints that
  float in whitespace, sit between subject details such as antlers/limbs, or point near a
  scene element that is not the data-bearing mark.
- A connector uses a bend, dogleg, bracket shape, multi-segment route, or prominent
  floating endpoint dots when a single short straight segment between the data label and
  the corresponding graphic would be clear and unobstructed. This is over-routing; it
  makes the annotation look arbitrary instead of helpful.
- A connector uses an oblique/diagonal line while a vertical or horizontal connector, or
  a simple right-angle elbow, could connect the same label and mark through blank space.
  Diagonal leaders are last-resort routes, not the default for nearby labels and marks.
- A connector path crosses or covers readable text, digits, formulas, units, source
  notes, animal/person/product subjects, faces/bodies, key generated-object detail, or
  the main data-shaped illustration. Correct endpoints do not save a connector whose
  middle path damages readability or image comprehension.
- A required connector is removed and replaced by a local color dot, swatch, tick, or
  underline even though the corresponding data mark sits elsewhere in the image. This
  breaks the label-to-mark relationship; redesign the label placement or route the
  connector through reserved negative space instead.
- A group of peer leader lines has unaligned starts/ends, irregular endpoint dot sizes, or
  arbitrary diagonal/zigzag paths when a shared connector lane would make the annotation
  system clearer.
- A row-based chart places the left label/value block, middle connector, and right data
  mark on different vertical anchors for the same data item, so the row reads as three
  misregistered layers instead of one aligned item.
- A data label module has no measured text-stack contract, causing role collisions such
  as name over English caption, English caption over number, unit too close to digits, or
  metadata sitting on the same baseline without a gutter. This is a frontend-design
  failure even if the row centerline and connector anchors are technically aligned.
- Header text, row text, values, units, and metadata use unrelated x coordinates without
  a declared alignment spine, so the layout feels arbitrary rather than designed. This is
  a frontend-design failure even if all text boxes fit and no overlaps are detected.
- A render responds to typography feedback only by adding collision/alignment assertions
  while keeping the same old row positions, header positions, type scale, and image crop.
  This fails because validation has replaced redesign.
- Row text rhythm is driven by an image asset's existing mark positions rather than by a
  planned readable text system, producing awkward gaps, cramped header clearance, or
  uneven row spacing.
- Peer row centerline gaps vary noticeably without data meaning or hierarchy, especially
  when the largest gap is more than 15% larger than the smallest. This is a typography
  rhythm failure even if row labels, connectors, and marks are individually aligned.

## Illustration handling

Upgrade options need generated illustration. When the chosen option is 3 / 4 / 5
(internal Style 2 / Style 3 / Style 5) and its token `illustration.mode` is
`"generate"`, image generation is mandatory unless the user has explicitly approved a
fallback. Basic option 2 (internal Style 4 Corporate Gradient) may use generated vector
assets only when the user requests them or the data concept genuinely needs a custom
object/icon; otherwise keep it as a code-rendered corporate template.

- Before any upgrade-style image generation, run
  `scripts/image_backend_preflight.py` and read its JSON report. Treat this as a hard
  readiness check. This skill is image-only: use the built-in `image` / `image_gen`
  capability and do not call Dreamina, external image CLIs, or API wrappers. Take a
  before/after snapshot and try built-in `image_gen` at most once for the required asset.
  If no new file appears under `$CODEX_HOME/generated_images` after that call, do not ask
  for another blind retry and do not switch tools. Explain that the built-in image preview
  did not create an accessible local file, then ask the user to download/save the preview
  image and send the final saved file path, or approve a labeled non-image fallback.
  Include the full file handoff instructions in that prompt: click download/save on the
  preview; check `/Users/guaren/Downloads/` if the app downloads automatically; move or
  save the image into `/Users/guaren/outputs/ppt-chart-design-assets/`; then send the
  saved path. Include quick-open commands for both folders:
  `open /Users/guaren/Downloads/` and
  `open /Users/guaren/outputs/ppt-chart-design-assets/`. This prevents repeated stalls
  after visible previews.
- For upgrade options, call image generation before final layout/rendering. The first
  generated asset should be a data-bearing illustration based on the whole dataset's
  theme and numeric relationship, not a generic topical picture and not separate spot
  decorations. Prefer a continuous image system that shows the overall change or
  composition in one visual idea. After inspecting the image, compose the chart around it:
  exact numbers, callouts, small comparisons, legends, and source notes are supporting
  layers that clarify the illustration, not competing main charts.
- Before every upgrade-style image call, write a short prompt preflight with these fields:
  `primary visual subject`, `secondary/context subjects`, `omitted subjects`,
  `common carrier for multiple categories`, `data behavior`, `why the image stays
  simple`, and `why no awkward fusion is needed`. If the preflight cannot choose a single
  primary subject or shared carrier, simplify the concept before calling image generation.
  The prompt should not list every title keyword as equal objects to combine.
- Build a list of needed image assets (e.g. 1 continuous data illustration, 1 hero object,
  1 integrated scene, an isometric pictogram field, or a segmented metaphor object). Only
  request N separate spot icons after confirming that a continuous or unified system would
  make the data less clear.
- Before generating assets, write the page-level illustration plan. It must specify
  whether illustrations are module markers, pictorial data marks, object-as-chart forms,
  or background texture. For repeated peer modules, the plan must use a balanced decision
  logic, not forced repetition: each illustration must be justified by the module's data
  meaning, and peer modules may omit illustration when no useful semantic match exists.
  Avoid giving only one peer module an illustration while adjacent peer modules remain
  visually empty, unless the illustrated module is intentionally the focal hero and the
  hierarchy makes that clear.
- Before generating, choose an integration pattern from `Data-Art Integration Rules` and
  state it in the prompt plan. If no valid pattern fits the data, do not generate
  illustration for that chart; use stronger typography, color, and data marks instead.
- Check every proposed illustration against its data before compositing:
  - Does the subject directly match the metric or category being shown?
  - Does a visible property of the illustration map to the data relationship (height,
    width, area, volume, count, density, route length, layer thickness, fill, etc.)?
  - Would the viewer still sense the main comparison/trend/composition if the numbers
    were hidden?
  - Does it make the data easier to understand, group, compare, or remember?
  - Is it integrated into the data mark, label system, or module structure rather than
    floating as decoration?
  If the answer is no, do not reuse or force the asset. Call image generation again with a
  more precise data-specific prompt, or omit the illustration.
- Generate each asset with the **image-generation tool**, using the style's
  `illustration.prompt_fragment` from the tokens so palette and look stay consistent.
- Lock generated-asset provenance before compositing. Before each image-generation call,
  take a file snapshot of `$CODEX_HOME/generated_images` or the expected image output
  directory. After generation, identify only the files newly created by that specific
  call, inspect them, and copy the accepted file into the current output directory. Record
  an asset manifest with the accepted file path, prompt summary, dimensions, byte size,
  and SHA-256 hash. Use `scripts/image_asset_guard.py` or equivalent code for snapshot,
  diff, lock, and verify steps.
- The final render script must load the accepted generated asset from the manifest or
  output-directory copy. It must not hard-code a path under `$CODEX_HOME/generated_images`
  found by manual browsing or mtime sorting, because those directories contain older
  candidates from previous attempts. It must not choose "the latest accessible" image if
  that image is not the exact approved preview.
- Calling image generation is not enough. The final compositing/render script must
  explicitly load and place the approved generated asset file, or explicitly document why
  that asset was rejected and either regenerate it or ask the user to approve a fallback.
  Never call image generation and then silently replace the generated asset with a crude
  hand-drawn PIL/SVG/canvas icon.
- If the image tool returns a visible result but no accessible local file path, treat the
  asset as unavailable for compositing. Do not proceed by imitating it in code. Pause in
  Chinese and ask the user to download/save the visible preview, then move or save it
  into `/Users/guaren/outputs/ppt-chart-design-assets/` and send the saved file path, or
  explicitly approve a clearly labeled non-image fallback. Also explain that downloaded
  preview images usually appear first in `/Users/guaren/Downloads/`, and explain how to
  open both folders quickly: `open /Users/guaren/Downloads/` and
  `open /Users/guaren/outputs/ppt-chart-design-assets/`, or Finder `前往` ->
  `前往文件夹...` and paste either path. Until one of those happens, do not render the
  final upgrade PNG.
- If a visible generated preview and the local file candidates disagree, trust neither.
  Stop and ask for a usable file path or regenerate. The final PNG must never use a
  different generated image from the one the user can see and judge.
- Generate the whole set with ONE fixed style fragment + ONE palette so the deck is
  coherent; then de-background/crop as needed and composite at the positions the style
  dictates.
- Do not replace a required generated asset with a manually drawn PIL/SVG/canvas shape,
  generic chart block, or icon-only approximation while image generation is available.
- Generated full-page backgrounds/templates must reserve truly blank areas for later
  code-rendered text and data. They may include texture, illustration, soft fields, and a
  few purposeful structural rules, but must not include obvious box grids, heavy
  mechanical dividers, text-like dashes, fake labels, fake UI copy, data-looking numbers,
  random bullets, or orphan leader lines that will sit under the final annotations.
- When illustration is not the chart itself, keep it subordinate to the data: crop with
  full object visibility, align it to the same grid as the related data module, and use it
  as a category marker, pictorial scale cue, or contextual anchor. Never let a large
  unrelated scene determine the layout if it weakens comparison, alignment, or reading
  order.
- If no image-generation tool is available, or generation fails repeatedly, pause and tell
  the user in Chinese. Ask whether to retry with image generation or proceed with a
  clearly labeled fallback. Only after the user approves fallback may you use an icon
  library + isotype + large numbers + texture blocks.
- If the user provides reference images, copy them into the matching `assets/` reference
  folder when useful and use them as style direction only. Do not copy protected
  composition/content; extract the design approach, palette behavior, density, object
  treatment, and label system.

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
- [ ] The whole page reads as one coherent information design: visual hierarchy,
      grouping, chart types, annotation, and illustration all support the same message.
      Data remains primary; illustration does not dominate unless it is itself the chart.
- [ ] The selected path was followed. Basic options are clarity-first: chart type, scale,
      labels, sorting, hierarchy, units, and whitespace make the data immediately
      understandable before decorative polish. Upgrade options are data-illustration-first:
      image generation produced a data-themed illustration before final composition, and
      title/numbers/callouts/auxiliary marks were arranged around it.
- [ ] The frontend-design aesthetic layer was applied: the PNG has a clear visual point
      of view, confident typography/color/spatial rhythm, and topic-appropriate background
      details. It does not feel like a default dashboard, generic AI template, or random
      decoration pasted over data.
- [ ] A data-art integration concept was defined before image generation for upgrade
      styles. It states the data theme, visual metaphor, each illustration's data role,
      the reserved zones for exact numbers/text, and why the art helps the viewer
      understand the data.
- [ ] A visual subject hierarchy audit was completed before image generation. The prompt
      has one primary visual subject, clearly subordinate secondary/context elements, and
      an explicit list of omitted subjects. No title keywords were blindly fused into one
      object.
- [ ] The simple-image feasibility test passed: the main subject is identifiable at a
      glance, the data behavior is clear, and secondary elements were removed or demoted
      when they made the concept complex, awkward, or visually uncomfortable.
- [ ] A data-to-image visual translation was defined before prompting: the values or
      relationships map to visible properties such as height, area, volume, count,
      density, route length, layer thickness, fill level, plume size, terrain mass, or
      flow thickness.
- [ ] For upgrade styles, the first image concept considers the full dataset as one
      continuous illustration system before splitting into separate panels, cells, icons,
      or mini-scenes. If separate modules are used, the reason is clarity, not habit.
- [ ] The dual-expression test passed: for each major illustrated data point, the number
      and the image express the same claim. If numbers were hidden, the viewer would
      still sense the main comparison, ranking, composition, trend, or change from the
      image's physical form.
- [ ] Data form was translated into the selected style's structural language. Timelines,
      event tables, compositions, flows, and single-metric stories were considered as
      style-native grids, sequences, routes, object layers, pictograms, or object-as-chart
      forms before defaulting to generic charts with pasted illustrations.
- [ ] The reference-structure translation note was completed: source data pattern,
      selected style-native structure, code-controlled exact marks, and generated asset
      roles are all stated. If a conventional chart was chosen over a reference-like
      structure, the readability reason is explicit.
- [ ] A layout grid/coordinate plan was established before rendering: canvas safe area,
      header zone, panel rectangles, plot areas, label lanes, value lanes, gutters,
      internal padding, and source-note zone are explicit and consistent.
- [ ] The construction grid stayed mostly invisible unless visible rules are necessary
      for comprehension. The final chart does not rely on obvious grids, hard dividers,
      or boxed cells as decoration when softer grouping or continuous illustration would
      read better.
- [ ] No redundant separator line is drawn on top of an already clear color/texture/image
      boundary. Color fields, whitespace, and soft background zones are not re-outlined
      unless the added rule has a distinct semantic role such as an axis, table rule,
      measurement guide, or bound callout.
- [ ] No double-frame effect is present. An element with its own outline/stroke is not
      wrapped in another border with the same containment role; any outer frame has a
      distinct semantic purpose such as highlight, selection, or warning.
- [ ] All repeated data containers use one consistent geometry system: same frame style,
      baseline, padding logic, title/value/supporting-copy order, and chart grammar unless
      a deliberate hierarchy change is visible and justified.
- [ ] Repeated peer containers passed a coded peer-group geometry check. Card strips,
      KPI tiles, label-card rows, table cells, and row modules have equal width/height,
      a shared row or column axis, no overlap, a declared minimum gutter, and near-equal
      spacing. Any highlighted peer keeps the same geometry unless the hierarchy change
      is intentional and documented.
- [ ] Information hierarchy verified before layout: metrics at the same analytical level
      use the same module size, element set, chart grammar, type scale, and spacing.
      Metrics at different levels are intentionally scaled or nested according to their
      role, not accidentally mixed.
- [ ] Numeric relationship types were classified before visual encoding. Peer comparison,
      additive part-to-whole, sequence/event, cumulative total, derived increment, and
      contextual comparison values are not mixed into one proportional segmentation or one
      same-level chart grammar unless the relationship truly supports it.
- [ ] For non-grid or freeform compositions, information weight across the whole image
      still follows hierarchy: focal data owns the largest/strongest visual territory,
      secondary data has smaller/supporting territory, and context/notes remain visually
      subordinate.
- [ ] Panel/card/plot gutters are visibly intentional. Adjacent borders do not visually
      kiss, compete, or create accidental narrow slivers; readable text never sits on a
      panel edge or canvas edge.
- [ ] Longest labels were measured or estimated before chart placement. Horizontal chart
      label columns, group tags, badges, and plot starts have separate lanes, so group
      badges do not press into category labels and labels do not press into bars.
- [ ] Header and source zones are protected. Titles/subtitles are not cropped, hidden
      behind panels, or forced into a single crowded line; source notes do not collide
      with bottom rules or the canvas edge.
- [ ] Exactly one style applied; palette/fonts pulled from tokens (not improvised).
- [ ] Background follows the upstream PPT/deck background plan when available; style
      background tokens were used only as fallback. Complete and clean PNG backgrounds
      match exactly.
- [ ] Bars sorted by value (not alphabetical) where ranking matters; bar axis from 0;
      no zoomed line axis without a clear label.
- [ ] Data-graphic consistency verified: every displayed number matches its visual
      encoding. Bar lengths, segment widths, areas, pictogram/icon counts, object
      proportions, color blocks, axis ticks, labels, and leader lines all reflect the
      original source values and were not changed by image generation, compositing,
      resizing, cropping, or style polishing.
- [ ] Connector binding verified: every leader line, connector dot, bracket, arrow, and
      callout ray has a registered source metric/category, target data mark, target mark
      anchor, label/text group, and label anchor. Endpoints were recomputed after all
      image scaling/cropping; no connector floats near a color block or stops short of
      its corresponding text.
- [ ] Connector two-sided pointing verified: the data-side endpoint clearly points to the
      exact data label/value/formula token, and the graphic-side endpoint clearly points
      to the corresponding visual mark/graphic for that same metric. Neither end points
      only to decorative empty space, a generic topic illustration, or the wrong mark.
- [ ] Connector endpoint source verified: data-side endpoint zones were derived from
      measured text/value/formula bounding boxes, and graphic-side endpoint zones were
      derived from actual mark geometry or verified generated-image hotspots. Endpoint
      distances pass both minimum-gap and maximum-gap checks, so the line neither touches
      nor floats away from either side.
- [ ] Connector path clearance verified: every leader/callout/bracket path is registered
      as a connector path, and all subject-dense image regions are registered as no-cross
      zones. Connector paths do not cross readable numbers, formulas, units, label text,
      source notes, animal/person/product bodies, faces, key illustration details, or
      data-shaped object regions except at their declared target anchor.
- [ ] Connector semantic function verified: every external label that refers to a mark
      elsewhere has a visible route from label anchor to target anchor through negative
      space. A local color dot/swatch is accepted only when the label and target mark are
      immediately adjacent and read as one unit; otherwise the connector must be routed,
      the label must move closer, or the annotation must be redesigned.
- [ ] Connector route efficiency and endpoint spacing verified: every connector uses the
      shortest available blank-space route between the label and corresponding graphic,
      not a scenic long diagonal. Both ends stop short of readable text/digits and the
      target graphic/object with a small consistent gap; endpoint dots, if used, sit in
      the gap and do not cover the label or data-bearing mark.
- [ ] Connector orthogonal-priority verified: each leader first attempts a horizontal or
      vertical single segment, then a simple right-angle elbow if needed. Oblique/diagonal
      connectors appear only when orthogonal routes would collide or mislead, and that
      exception is documented in the connector binding table.
- [ ] Connector straight-line preference verified: if the nearest valid data-side point
      and nearest valid graphic-side point can be joined by one unobstructed short
      straight segment, that straight segment is used. Bends, doglegs, brackets, and
      prominent endpoint dots are used only when a straight connector would collide or
      misread.
- [ ] Connector alignment verified: peer leader lines use a shared connector lane, with
      at least one side aligned to a common guide unless the design is intentionally
      radial/freeform. Endpoint dots in the same connector group use identical radius,
      stroke, fill, and optical weight unless a documented hierarchy requires otherwise.
- [ ] Row-level alignment verified for row-based charts: every item has one row id and
      one row centerline/baseline contract. The left text/value module, connector module,
      and right visual mark/module share that contract; their registered anchors match
      within tolerance, and rows do not appear as independently placed columns.
- [ ] Relationship-to-encoding consistency verified: the graphic form tells the same
      analytical relationship as the data. Segments/fills/slices are used only for peer or
      additive relationships; process/event/cumulative/derived values use sequence,
      hierarchy, attached labels, or focal-summary structures instead.
- [ ] Semantic ownership verified: every label, formula, relationship note, and
      explanatory annotation has a declared owner module. Parent/summary explanations sit
      in the parent/summary territory or merge point; child/component notes stay attached
      to their own component. No text was placed in a child module merely because there
      was empty space.
- [ ] Single-expression audit passed: every source metric appears in the metric-expression
      map with exactly one primary visual expression. Numeric text is only a label,
      calibration, or context note attached to that expression; the same dataset is not
      repeated as a second full chart, table, formula strip, timeline, ranking list, or
      pictorial system.
- [ ] Exact-number duplication audit passed: no source value is shown as both a
      title/headline number and a separate large KPI/focal-number module. If a title
      contains the exact digits, formulas/notes avoid repeating that exact result unless
      the arithmetic/provenance check explicitly requires it; repeated results must be
      compact, subordinate, and justified in the metric-expression map.
- [ ] Any source table/list was reduced to non-duplicative context, selected event
      callouts, source notes, or an explicitly user-requested lookup appendix. A full
      data table is not placed beside a chart/image system that already encodes those
      values.
- [ ] Text/number geometry verified after final rendering: no plotted mark, color block,
      axis line, badge, group tag, or illustration overlaps, clips, hides, or visually
      cuts through any readable digit, sign, unit, category label, or annotation.
- [ ] Collision testing was performed with registered bounding boxes for text and
      collision-relevant graphics. Any overlap between readable text and chart marks,
      decorative arcs, connector dots, hard edges of ambient overlays, zero axes, tracks,
      neighboring labels, or card edges was treated as a failed render and fixed by
      reflowing/removing elements.
- [ ] The collision test was executed by code, not only by visual inspection. Every
      readable text item and every collision-relevant graphic item is registered; the
      renderer raises/fails before output if any required item is missing from the
      registry or if a forbidden intersection remains.
- [ ] Every numeric label has a safe placement. Labels inside bars/segments/objects fit
      completely inside the mark with balanced padding and contrast; labels that do not
      fit are moved to a reserved outside value column or callout, not squeezed into the
      mark.
- [ ] Empty bar tracks/outline rails were removed unless they encode a real target,
      capacity, benchmark, maximum, forecast, or missing share. Value labels do not touch
      or overlap empty rail outlines, zero-axis lines, or pale track borders.
- [ ] Compact KPI strips, bullet charts, and mini comparison bars use separate fixed
      lanes for row labels, numbers, data marks, and notes. Bars must not grow under or
      across adjacent numbers.
- [ ] Composite summary/decomposition modules use a module-local subgrid. Section title,
      explanation, bars/segments, percentages, legends, formulas, totals, and notes each
      occupy declared zones with fixed gutters and shared baselines; no element is placed
      by unrelated hard-coded coordinates.
- [ ] KPI/headline-number modules use a module-local subgrid. Large numbers, units,
      comparison dots, gauges, arcs, sparklines, notes, and callout lines do not share the
      same unmeasured space. No decorative or supporting graphic passes behind, through,
      or over a large number unless its text bounding box has been measured and the
      overlap is intentional and legible.
- [ ] Card surfaces are not nested accidentally. The render does not stack two nearly
      identical rounded rectangles/panels around the same module, which would create a
      double-card or multi-border effect.
- [ ] Formulas and mixed numeric phrases were laid out from measured text bounding boxes
      with consistent token gaps. If a formula did not fit its zone, it was stacked,
      resized as a group, moved to a separate row, or simplified before rendering.
- [ ] Formula grammar verified: arithmetic expressions use arithmetic operators and a
      valid result. Arrows are used only for process/flow/sequence, not to stand in for
      equality.
- [ ] Formula inline alignment verified: every number, unit, word, and operator token in
      a formula shares a measured visual centerline within tolerance; mixed fonts do not
      make operators float.
- [ ] When one value has both a visual mark and an exact number, they read as one unit:
      the number labels/calibrates the mark instead of forming a second independent
      graphic. If both cannot fit cleanly, simplify to the stronger single expression.
- [ ] Bar/column/progress endpoints are clean and integrated: rounded ends are made from
      one continuous shape, or endpoint dots are fully contained within the bar silhouette.
      No accidental protruding caps, spikes, or pointed tips are visible.
- [ ] A source-value-to-visual-mark check was performed for each encoded metric. If exact
      visual measurement is impractical for a generated object, the object is treated as
      decorative/contextual only and the exact data encoding is handled by code-rendered
      marks.
- [ ] Proposal/investment framing offers a two-scenario comparison with an annotation.
- [ ] Direct labels used where possible; legend only if necessary.
- [ ] No chartjunk: no stray gridlines/3D/shadow unless the style calls for it.
- [ ] Source/unit noted; numbers sensibly rounded.
- [ ] Draft/early/placeholder data carries a status sticker (WIP/Discussion/Preliminary/
      Illustrative).
- [ ] Any illustration is generic (no IP / no real people); title is original.
- [ ] Any illustration clarifies or encodes data and is integrated into the relevant data
      module; no decorative hero image was forced into the page at the expense of clarity.
- [ ] Illustration is not merely inserted. It functions as cell content, a data mark,
      context anchor, hierarchy cue, or subordinate texture inside the data structure.
      Corner decoration, generic topic art, stock-like scenes, and unrelated filler images
      were rejected.
- [ ] No awkward concept fusion remains. Secondary context such as routes, locations,
      causes, time cues, or environments supports the primary subject as context,
      annotation, or background; it does not mutate the main subject into an uncanny or
      hard-to-read hybrid.
- [ ] The illustration system is balanced across peer modules: comparable modules have
      a comparable illustration decision logic, not forced repeated icons; any intentional
      exception is clearly explained by hierarchy.
- [ ] Every illustration semantically matches the data it represents. If an existing asset
      does not match the metric/category, it was regenerated with image generation or
      removed.
- [ ] No illustration is cropped accidentally. If an object is intentionally cropped by a
      page edge or frame, the crop must look designed and must not remove the object's
      identifying or functional part.
- [ ] No generated template artifacts remain under final overlays: no fake text, random
      dashed label rows, orphan bullets, placeholder boxes, or unconnected guide lines.
- [ ] Typography is not crowded: long subtitles/supporting copy are wrapped into readable
      lines with clear spacing, following the chosen style's reference layout language.
- [ ] Frontend-design typography was translated into a measurable type system: title,
      explanatory copy, utility labels, numbers, and source notes each have defined size,
      weight, line height, max line width, and spacing. Paragraph-like Chinese text is
      wrapped intentionally and is not clipped by the canvas, panel, mask, or neighboring
      module.
- [ ] Every repeated data label module has a measured text-stack contract. Role order,
      font size, baseline/top coordinate, minimum gaps, value-unit grouping, metadata
      lane, and stack bounding box were checked after final font rendering. No name,
      English caption, value, unit, metadata, note, or source label overlaps or crowds
      another text role.
- [ ] A typographic alignment spine was defined and used: header, row names, captions,
      values, units, metadata, connector anchors, and visual marks use declared lanes.
      Any intentional offset is documented by hierarchy; otherwise title/body/data rows
      align to the same main text spine and values/units/metadata align consistently.
- [ ] Typography feedback triggered a real redesign pass, not only new assertions. Row
      rhythm, header clearance, type scale, text-stack order, column widths, metadata
      placement, and image crop/scale were reconsidered. The final layout is aesthetically
      improved at slide-view size, not merely collision-free.
- [ ] Row centerlines were designed from the text system and reading rhythm before being
      matched to generated image marks. If the image asset's existing mark positions
      created awkward typography, the asset was cropped, scaled, repositioned, or
      regenerated rather than forcing text into those positions.
- [ ] Peer row vertical rhythm was checked numerically. Unless spacing encodes hierarchy
      or data, peer row center gaps are equal or near-equal; as a default, max gap is no
      more than 15% larger than min gap.
- [ ] Instructional/explanatory blocks have enough paragraph territory. Reading guides,
      methodology notes, and multi-clause descriptions are not forced into one long
      truncated line; they are shortened, wrapped, or moved to a wider zone before output.
- [ ] Visible-copy fidelity verified: every title, subtitle, label, formula, note, stamp,
      source line, punctuation mark, arrow, separator, unit, and space comes from the
      visible-copy manifest or source-approved rewrite. No renderer-introduced ASCII
      placeholder such as `->` remains unless explicitly required by the source.
- [ ] Group labels and pills/bars have deliberate spacing and alignment. Labels such as
      "right/left" or "increase/decrease" do not visually stick to the pill/card/bar they
      name, and pill text remains optically centered with balanced side padding.
- [ ] Text inside bordered cards or badges has balanced padding and is centered when the
      card style calls for centered content; no text sits too close to the border.
- [ ] Centered badge/stamp text was centered by final rendered bboxes, not only by
      declared line heights. The text block's union bbox is aligned to the container
      center within tolerance.
- [ ] A final layout QA pass was performed at slide-view size. If `layout-design-check`
      is available and useful, its grid/hierarchy/spacing/safe-area review was applied
      without changing data, chart type, selected style, or clean-PNG rules.
- [ ] Header/meta text such as dates, units, and section labels is aligned to a clear
      baseline or centerline; right-side header text is optically right-aligned and not
      visually ragged.
- [ ] Leader lines/dots attach to the exact corresponding data-bearing mark, color block,
      segment, drawer, or layer - never to a shadow, frame, gap, or unrelated nearby area.
      The opposite endpoint also attaches to the corresponding text/number label group,
      so the line reads as one exact annotation from label to mark.
- [ ] Two PNGs were produced: a complete annotated version and a clean visual-base version.
      The clean version removes only readable text/numbers/source/label copy. All
      non-text visual elements match the complete version, including data-bearing bars,
      segment colors, areas, pictograms, object proportions, swatches, leader lines,
      illustrations, frames, and background.
- [ ] If the selected style requires generated illustration, image generation was called
      for the visual asset(s), or the user explicitly approved a fallback after being told
      image generation was unavailable/failed.
- [ ] Generated-image usage verified: every required generated asset is actually loaded
      or composited into the final PNG from a concrete file path. No generated asset was
      silently replaced by a hand-drawn PIL/SVG/canvas icon or generic placeholder.
- [ ] Generated-image provenance locked: for every approved generated asset, an output
      directory copy and manifest exist with source path, prompt summary, dimensions,
      byte size, and SHA-256 hash. The final render script loads that locked asset, not a
      manually selected old file or a best-guess latest file from `generated_images`.
- [ ] Preview-to-file agreement verified: the generated preview accepted by the user or
      agent visually matches the file used in composition. If the preview is visible but
      no matching local file is accessible, the workflow stopped instead of substituting
      another image.
- [ ] If image generation returned only a visible preview and no accessible file path, the
      workflow stopped and asked the user to download/save the preview first, check
      `/Users/guaren/Downloads/` if the app downloads automatically, move or save the
      image into `/Users/guaren/outputs/ppt-chart-design-assets/`, and send the final
      saved path, or approve a labeled fallback. The user was also told how to open both
      folders quickly with `open /Users/guaren/Downloads/` and
      `open /Users/guaren/outputs/ppt-chart-design-assets/` or Finder `前往` ->
      `前往文件夹...`. The final PNG was not rendered from a code-made imitation of that
      preview.
- [ ] Generated-image integration verified: every generated asset appears in the intended
      data module, grid cell, object segment, route, pictogram set, or context zone from
      the art-direction sketch. Assets pasted into leftover space without a data role
      were removed or regenerated.
- [ ] No post-hoc data recoloring of generated objects: upgrade-style data fields are
      either present in the approved generated asset itself, or the asset is treated as
      contextual only and exact data marks are code-controlled elsewhere. The renderer did
      not clip flat fills, repaint object regions, or draw fake integrated segments on top
      of a generated silhouette.
- [ ] Rendered at high DPI; complete-version text is legible at slide size.

## Files

- `references/chart-selection.md` - intent -> chart type (two-level table)
- `references/data-storytelling-principles.md` - the 7 principles applied on every chart
- `references/style-selection.md` - data/scenario -> one of 5 styles (auto-recommend)
- `references/style-1-airy-systematic.md` ... `style-5-magazine-monochrome.md`
- `assets/design-tokens.json` - all palettes/fonts/illustration modes (machine-readable)
- `assets/style-1-airy-systematic-references/` - user-provided references for Style 1
  Airy Systematic chart language.
- `assets/style-2-retro-editorial-references/` - user-provided references for Style 2
  Retro Editorial Illustrated chart language.
- `assets/style-3-metaphor-object-references/` - user-provided references for Style 3
  Metaphor-Object Editorial chart language.
- `assets/style-4-corporate-gradient-references/` - user-provided references for Style 4
  Corporate Gradient Template chart language.
- `assets/style-5-magazine-monochrome-references/` - user-provided references for Style 5
  Magazine Monochrome Editorial chart language.
- `scripts/render_chart.py` - theme matplotlib from tokens, render PNG outputs
- `scripts/layout_guard.py` - reusable bounding-box and collision guard for custom PNG
  renderers. Use it to register text, chart marks, decorative graphics, panel edges, and
  label-fit zones; failed intersections must trigger reflow before output.
- `scripts/image_asset_guard.py` - reusable provenance helper for generated image assets.
  Use it to snapshot generated-image directories, identify new files from a specific
  generation call, lock the accepted file into a manifest, and verify the manifest before
  final compositing.
- `scripts/build_pptx.py` - legacy helper; use only if the user explicitly asks for PPTX
