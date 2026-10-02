# Framework Rendering Prompt Template

本模板用于已经完成内容提炼后的绘图。方括号是工作占位符，提交绘图前必须全部替换为本稿的具体内容。没有依据的模块直接删除，不用网络术语填空。

---

Create an academic method framework figure that closely follows the attached ORIGINAL reference figure. Preserve its composition, proportions, hierarchy, pictogram grammar, typography, colors and connector treatment as specified below. Rebuild scientific content entirely from the supplied method specification. Do not redesign the style.

## Scientific content

Central purpose:
[One sentence grounded in the current paper or text.]

Main information flow:
[The actual sequence, including any genuine parallel branches.]

Stage layout:
[For every stage, specify its short title, contents, position, incoming objects, outgoing objects, and manuscript-specific pictograms. Do not force four stages.]

Internal operations:
[Concrete nodes and meaningful local representations.]

Exact connections:
[Source port -> destination port; signal; edge type. Include only supported dependencies.]

Core mechanism to make visually explicit:
[The actual changed operation or relationship, not a vague “proposed module” box.]

Exact labels and notation:
[The final short labels and exact mathematical symbols.]

## Required visual grammar

Original reference: [paper ID, figure, PDF page and attached actual crop; no sketch substitute].

Layout to retain: [actual aspect ratio, normalized zone bounds, ordering, rows/columns and whitespace copied from the selected source's visual arrangement].

Typography and shapes to retain: [observed font family/hierarchy, border treatment, corners, group nesting, label placement]. Do not impose serif fonts, dashed groups, three layers or a horizontal flow when the selected reference uses another arrangement.

Palette and line treatment: [specific source colors or honestly approximate colors, fills, outline widths, arrowheads and solid/dashed semantics]. Reassign color meanings to the new research explicitly.

Source-to-new-content mapping: [each major source visual zone/pictogram → actual new scientific object; list minimal topology changes with their scientific reasons]. Do not replace mechanism graphics with identical text boxes.

Source slots to omit or merge: [operations in the reference that have no counterpart in this method]. Retain the source's visual grammar while adjusting card counts and relative space to the actual computations. Never repeat a perception output to fill a slot, or present an intermediate output signal as an additional algorithm. Distinguish computation, data, constraints and output signals explicitly.

Integrate small meaningful pictograms or local schematics: the actual input entities, feature blocks, graph relations, token sequences, candidate trajectories, constrained geometry, belief representations, or output objects specified above. Do not insert irrelevant pictograms merely to decorate the figure.

Each miniature must explain its named scientific relationship; do not fill every module with the same red dot and curve. Devote appropriate space to the supported core mechanism. If its internals are unspecified, preserve a named black-box operation and accurate interfaces instead of inventing internals for visual density.

Keep connectors short and clean, using explicit ports and mostly orthogonal routing. Place supported feedback or recurrent paths around the outside. Avoid crossings, and do not allow arrows to pass through text. Distinguish training-only edges from online data flow when the method actually contains both.

Keep labels concise and readable at the specified final column width. Align same-level modules and stage titles. Use a small legend only when needed. Keep the caption outside the figure image.

## Hard exclusions

Do not transfer unsupported reference scientific content. Match visual placement and routing closely wherever the actual new mechanism allows; change dependencies when scientific correctness requires it. Do not invent Transformer, GRU, MLP, Gaussian distributions, losses, residual links, layer counts, training updates, or control interfaces.

Do not turn the figure into a sparse row of generic boxes, a slide deck, a dashboard, a dark technology poster, or a glossy infographic. No large headline, heavy shadows, glow, decorative 3-D layers, long paragraphs inside boxes, or unsupported results.

Any illustrative local distribution or curve must be schematic, not presented as measured evidence. Do not invent physical experimental photographs.

Final canvas and label settings:
[Actual target aspect ratio, output dimensions where applicable, typography hierarchy, language, and any final-width constraints.]

Render the specified method, not a generic example of a plausible method.
