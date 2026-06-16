# Data-storytelling principles (ALWAYS apply)

These govern *how the data is told* - they sit above chart-type and style choice. Apply
them on every chart, then verify with the QC items in SKILL.md. The common mechanism:
make the chart fit how the brain reads, and actively manage the viewer's expectation of
how to read it and how much to trust it.

## 1. Never present a single number alone
A lone number has no context ("sold 10k units at $5,000 each" - good or bad? unknowable).
Always give it a comparison: prefer **historical** data (vs past quarters), else an
**industry benchmark**, else even a stated **best guess** - anything beats nothing.
Keep it apples-to-apples: quarter vs quarter, never quarter vs YTD (different time spans
make the comparison invalid). Comparison is what gives a number meaning.

## 2. One focus per chart
Every table/chart should have exactly one focal point. The brain spots the anomaly
instantly, so highlighting one thing aims attention precisely. Multiple datasets crammed
in cause seconds of confusion - if several are needed, **reveal in stages (1, 2, 3)**.
Exception: documents designed to be read standalone may be intentionally dense.

## 3. Use color for contrast, and to encode meaning
The brain reads color faster than shape, so deliberate color sharply raises clarity.
Advanced: encode meaning with shade - older data light grey, recent past dark grey,
current/own-brand data in the brand color, forecast in a lighter tone. The viewer then
*feels* relative importance and recency without reading.

## 4. Keep formatting consistent across the deck
Same style throughout: always highlight the max in the same color, always sort products
high-to-low, keep titles consistent. Switching highlight color, sort order, or title
between slides unsettles viewers (the brain hunts for pattern/consistency). Consistency
lets one mental model read every new chart, removing re-learning cost.

## 5. Use contrast/comparison charts for proposals & investment asks
Don't draw a single "growth if supported" line - show **two scenarios side by side**
("accelerated / after investment" vs "status quo"). When the base case holds, the
side-by-side makes "do nothing" look almost foolish and exposes the cost of inaction.
Always add an annotation label stating the specific lever (e.g. "+$100k on product
marketing") so both the gain and the loss are visible. Comparison dramatizes the stakes.

## 6. Use the right chart type - and don't manipulate it
Right chart = clear structure; wrong chart or tampering = confusion or deception.
- Pie: only when <=3 categories and one dominates.
- Line: good for change over time, but don't mislead via the axis - zooming a slice makes
  a tiny change look dramatic; the 12-month full view is the truth. Rule: start from zero;
  if you must zoom, clearly label where it's zoomed.
- Waterfall: best for "how one number becomes another" - it decomposes the causes of
  change (each product's increment, even negative drag from e.g. legal risk) in a way a
  plain before/after bar cannot.
(See also `chart-selection.md` for full intent->chart mapping.)

## 7. Use status "stickers" to protect yourself & set expectations
Add a status label to manage expectations and leave the presenter room:
- **WIP** - this presentation isn't finished.
- **Discussion** - very early draft, needs review/feedback on direction.
- **Preliminary** - the slide is done but the underlying data is still in progress
  (e.g. survey completes in 2 months; these are early results).
- **Illustrative** - placeholder/made-up numbers used to convey the point ("the chart
  isn't 100% accurate, but the message I'm conveying is real").

## How the skill applies these
- Single value requested -> attach a comparison (principle 1); if none exists, say so and
  offer a benchmark or label it Illustrative (7).
- Default to highlighting one element (2) and encoding recency/ownership by shade (3),
  drawing those colors from the chosen style's tokens.
- Reuse the same highlight color and sort order across charts in one request (4).
- Investment/proposal framing -> offer a two-scenario comparison with an annotation (5).
- Pick the chart type per `chart-selection.md`; keep bar axes from zero; never zoom a line
  axis without a label (6).
- If the user flags data as draft/early/fake or it clearly is, add the matching status
  sticker (7).
