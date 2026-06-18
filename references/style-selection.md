# Style selection (recommend + Chinese grouped confirmation)

Pick ONE recommended style from four signals. State the recommendation in one line with
the reason, then ask the user to choose a style by replying with **1、2、3、4或5**. The
confirmation prompt must be written in Chinese. Do not proceed to render until the user
confirms a style. If the user already explicitly named a style, grouped option, or
unambiguous internal style number in the request, treat that as confirmation and continue.
If the user replies with an outdated grouped label, ask them to choose from the current
continuous numbers `3`、`4`、`5`.

Mapping:

- 1 -> 基础选项 / internal Style 1 Airy Systematic
- 2 -> 基础选项 / internal Style 4 Corporate Gradient
- 3 -> 升级选项 / internal Style 2 Retro Editorial
- 4 -> 升级选项 / internal Style 3 Metaphor Object
- 5 -> 升级选项 / internal Style 5 Magazine Monochrome

Generation logic:

- 基础选项优先考虑清晰展示数据：先确定图表类型、信息层级、比例尺、排序、标签、
  单位、留白和对齐，再做风格化润色。
- 升级选项优先把数据转译为插画：确认风格后，先判断标题/信息中的主视觉主体与
  次要辅助元素，删除会让画面复杂或别扭的次要元素，再调用 image 生成符合数据主题
  和数值关系的数据插画，最后围绕插画进行构图，并添加精确数字、辅助图表、注释
  和来源。

Use this Chinese confirmation format:

> 我推荐 **[基础/升级]选项 N：[中文风格名]**，原因是：[简短原因]。
> 请回复数字选择生成风格：
>
> **基础选项**
> 1. 清透系统信息图（Airy Systematic）
> 2. 企业渐变模板信息图（Corporate Gradient）
>
> **升级选项（需调用生图大模型）**
> 3. 复古网格编辑信息图（Retro Editorial）
> 4. 隐喻物象编辑信息图（Metaphor Object）
> 5. 杂志专题单色信息图（Magazine Monochrome）
>
> 请回复：1、2、3、4或5。

## Signals

1. **Content type** - quantitative data chart vs concept/structure (process, cycle,
   hierarchy, relationship, timeline, map).
2. **Audience / context** - internal corporate vs editorial/publication vs social/viral.
3. **Density** - single punchy stat vs a data-rich multi-chart page.
4. **Tone** - neutral/professional vs opinionated/playful.

## Decision rules (first match wins)

1. Content is **concept/structure** (process, cycle, org, relationship, timeline, map),
   OR audience is generic corporate and the user wants something safe/fast
   -> **Style 4 Corporate Gradient**.
2. Audience is **annual report / policy / serious professional**, quantitative, wants a
   clean restrained look -> **Style 1 Airy Systematic**.
3. Goal is **social / viral**, a single punchy stat, and a real-world **metaphor object**
   fits the topic -> **Style 3 Metaphor Object**.
4. Tone is **opinionated / editorial**, wants to grab attention, illustration-rich,
   magazine attitude, moderate density -> **Style 2 Retro Editorial**.
5. It's a **deep single-topic page** packing several related charts + big numbers, with
   magazine authority -> **Style 5 Magazine Monochrome**.

## Quick map

| If the request feels like... | Style |
|---|---|
| "make my business slide look clean and on-brand" | 2 / Style 4 |
| "this is for the board / annual report" | 1 / Style 1 |
| "I want this to get shared / go viral" | 4 / Style 3 |
| "give it attitude, editorial, eye-catching" | 3 / Style 2 |
| "one page, lots of related data, magazine feel" | 5 / Style 5 |

## Tie-breakers

- Quantitative + neutral but unsure between Airy Systematic and Corporate Gradient:
  choose **2** if it's structure-ish or generic business; **1** if it's pure data for a
  serious/quiet audience.
- Playful + single stat between Retro Editorial and Metaphor Object: choose **4** if a
  clean object metaphor exists; **3** if it's multiple stats on one busy page.
