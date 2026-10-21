---
name: blender-lookdev
description: Use for design-system styleframes, readable rounded typography, stylized Blender 3D materials, camera-safe framing and lighting.
---

# Blender look development

Deliver opening, busy-middle, and final brand styleframes with source colors, approved typeface and license, lighting/material swatches, dominant geometry, background treatment and projected camera-safe bounds.

Use genuine Blender Text objects with font paths and evaluated glyph-bounding boxes; do not equate font.size with pixel cap height. Keep headline readability at 50% downsample. Use Principled BSDF socket names queried from installed bpy, bevel geometry, correct normals and a deliberately simple light rig. Prefer Eevee on constrained hardware, but verify render engine enum with bpy first.

3D camera orbits should clarify geometry, not obscure the copy. Avoid uncontrolled bloom, unnecessary chrome, random decorations and mismatched seal colors. Human approval is required for artistic quality.
## Non-negotiable operation rules

- Use the approved project brief and declarative frame/event specification; never invent missing institutional facts, copy or licenses.
- Produce native Blender bpy objects and editable .blend scene data, not a browser animation mislabeled as Blender.
- Verify using actual tests, rendered frames, reproducible commands and output paths.
- Technical PASS is distinct from aesthetic or listening HUMAN_REVIEW_REQUIRED.
- If required assets or executable APIs are unavailable, report BLOCKED; never silently substitute.
