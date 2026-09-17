# Framework Rendering Prompt Template

本模板用于已经完成内容提炼后的绘图。方括号是工作占位符，提交绘图前必须全部替换为本稿的具体内容。没有依据的模块直接删除，不用网络术语填空。

---

Create a compact, publication-oriented academic method framework figure for the method specified below. Use the attached reference image only as a visual style anchor. Reconstruct the scientific content entirely from the supplied method specification.

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

Use a white canvas and a compact horizontal composition. Organize the method into softly tinted functional groups, with thin dark dashed outer borders and bold serif stage titles placed just above the group borders. Arrange the main flow left to right and most internal pipelines top to bottom. Let the core mechanism receive more space when needed.

Use thin solid outlines and modest rounded corners for internal modules. Use nested grouping only where it reflects real structure. Preserve three levels of hierarchy: functional stages, operations, and compact local representations of data or mechanisms.

Use a restrained pastel palette: soft gray for inputs, pale peach for representation when applicable, light blue-gray for the core mechanism, and pale cream-yellow for outputs when applicable. Use consistent pale green, pale blue, peach, pink, or lavender accents for actual operation or feature categories. Maintain any manuscript-specific color semantics given above. Use dark, thin arrows and readable serif typography similar to the reference.

Integrate small meaningful pictograms or local schematics: the actual input entities, feature blocks, graph relations, token sequences, candidate trajectories, constrained geometry, belief representations, or output objects specified above. Do not insert irrelevant pictograms merely to decorate the figure.

Keep connectors short and clean, using explicit ports and mostly orthogonal routing. Place supported feedback or recurrent paths around the outside. Avoid crossings, and do not allow arrows to pass through text. Distinguish training-only edges from online data flow when the method actually contains both.

Keep labels concise and readable at the specified final column width. Align same-level modules and stage titles. Use a small legend only when needed. Keep the caption outside the figure image.

## Hard exclusions

Do not copy the reference method, caption, network modules, branch topology, or mathematical variables. Do not invent Transformer, GRU, MLP, Gaussian distributions, losses, residual links, layer counts, training updates, or control interfaces.

Do not turn the figure into a sparse row of generic boxes, a slide deck, a dashboard, a dark technology poster, or a glossy infographic. No large headline, heavy shadows, glow, decorative 3-D layers, long paragraphs inside boxes, or unsupported results.

Any illustrative local distribution or curve must be schematic, not presented as measured evidence. Do not invent physical experimental photographs.

Final canvas and label settings:
[Actual target aspect ratio, output dimensions where applicable, typography hierarchy, language, and any final-width constraints.]

Render the specified method, not a generic example of a plausible method.
