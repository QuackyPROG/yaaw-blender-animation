---
name: blender-motion
description: Use for procedural Blender 5.2 keyframes, easing, anticipation, squash/stretch, stagger, 3D rotation, camera rigs and Action Slot validation.
---

# Blender procedural animation

## Native implementation
Treat each motion as {object IDs, start/end inclusive frames, source/target world and projected coordinates, easing, velocity, anticipation, follow-through, hold}. Use bpy Object transforms, parent rigs, keyframe_insert, Action/Slot-aware F-curve edits, constraints and deterministic data. Detect 5.2 API variants from installed bpy; older direct-action F-curve recipes may not apply.

## Validation
Evaluate the actual depsgraph at specified frames. Sample screen-projected position, heading, apparent speed and bbox, especially frames around handoffs. No discontinuous teleporting between shots unless approved match-cut. Never use random unseeded motion, non-seek-safe frame-change handlers, or camera movement that hides readable typography. Save the Blender file and sample rendered frames; a unit test alone doesn't prove beautiful easing.
## Non-negotiable operation rules

- Use the approved project brief and declarative frame/event specification; never invent missing institutional facts, copy or licenses.
- Produce native Blender bpy objects and editable .blend scene data, not a browser animation mislabeled as Blender.
- Verify using actual tests, rendered frames, reproducible commands and output paths.
- Technical PASS is distinct from aesthetic or listening HUMAN_REVIEW_REQUIRED.
- If required assets or executable APIs are unavailable, report BLOCKED; never silently substitute.
