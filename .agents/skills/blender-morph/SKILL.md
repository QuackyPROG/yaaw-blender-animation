---
name: blender-morph
description: Use for Blender-native shape transformations: mesh shape keys, curve resampling, contour morphs, text to geometry, trace draw and volume/SDF experiments.
---

# Blender morph engineering

## Technique order
1. Deform one persistent shape/object when possible.
2. For planar closed curves, normalize winding, landmark correspondence and point sample count; interpolate curve control points with measured silhouette continuity.
3. For meshes, use shape keys ONLY if vertex counts, indices and topology correspond.
4. For continuous strips/traces use Geometry Nodes, Trim Curve/Resample Curve/Curve to Mesh.
5. Use matched silhouette handoff only after documented test and explicit approval.
6. Never label an opacity crossfade as a true morph.

## Acceptance
Record object IDs, contour registration method, frames, outline landmarks, projected centroid/area, topology proof and chosen fallback. Render at 0/25/50/75/100% and ±1 frame near the seam. Detect self-intersection, inverted normals, discontinuous inner holes, sudden scale jumps and geometric tearing. Report BLOCKED if unsuitable topology prevents correct morph.
## Non-negotiable operation rules

- Use the approved project brief and declarative frame/event specification; never invent missing institutional facts, copy or licenses.
- Produce native Blender bpy objects and editable .blend scene data, not a browser animation mislabeled as Blender.
- Verify using actual tests, rendered frames, reproducible commands and output paths.
- Technical PASS is distinct from aesthetic or listening HUMAN_REVIEW_REQUIRED.
- If required assets or executable APIs are unavailable, report BLOCKED; never silently substitute.
