# Chart selection (two levels)

First match the **message to an intent**, then refine by **data shape**. Never pick a
chart by what looks familiar (this is why non-designers overuse pie and 3D).
Encoding accuracy (Cleveland-McGill): position > length > angle/area > color. So bars
beat pies for quantitative comparison.

## Level 1 - intent -> chart family

| Intent (what you're saying) | Default chart |
|---|---|
| Comparison / ranking ("who is more") | Bar (vertical) or horizontal bar, **sorted by value** |
| Trend over time | Line (1-2 series), area for cumulative magnitude |
| Composition (part-to-whole) | Stacked bar, 100% stacked, waterfall, treemap; pie only if <=3 parts and one dominates |
| KPI / single value | Big number + one line of context + sparkline; progress ring |
| Precise lookup / multi-attribute | Table (plain, heat, or with in-cell mini-charts) |
| Deviation (vs target/baseline, +/-) | Diverging bar, bullet chart |
| Flow / conversion | Funnel, sankey, alluvial, flow map |
| Distribution | Histogram, box plot |
| Relationship / correlation | Scatter, bubble (3rd var) |
| Geographic | Choropleth / region map |

## Level 2 - refine by data shape

- **Comparison**: <=7 categories -> column; many or long labels -> horizontal bar;
  multiple series -> grouped bar; too many series -> small multiples.
- **Trend**: 1-2 series -> line; many series -> small multiples; cumulative total -> area.
- **Composition**: single point in time -> stacked bar / pie(<=3); over time ->
  100% stacked; start-to-end add/subtract -> waterfall; hierarchy -> treemap.
- **KPI**: pair the big number with a tiny trend or a one-line "so what".
- **Table**: sort rows meaningfully; color cells by value (heat) if scanning matters.

## Coverage note

This 10-intent set covers ~85-90% of PPT needs. The often-missed-but-high-frequency
ones for business decks are **KPI big-number** and **table** - keep them first-class.
Concept/structure content (process, cycle, hierarchy, relationship) is not a data chart;
it pairs best with **Style 4 (corporate gradient)**.
