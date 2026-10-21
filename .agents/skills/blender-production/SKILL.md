---
name: blender-production
description: Use for end-to-end Blender motion graphics from creative brief through storyboard, proof, editable .blend, rendering, audio and QA.
---

# Blender production orchestrator

## Pipeline
1. Probe Blender executable/API, FFmpeg, assets, GPU/RAM/disk. Verify required versions rather than presuming.
2. Inventory supplied materials and write BRIEF.md. Don't re-ask decisions already provided.
3. Ask blender-storytelling for approved motifs, narrative beats, and projected handoff positions.
4. Ask blender-audio to verify a legally obtained soundtrack and publish measured beat/downbeat events.
5. Ask blender-motion + blender-morph to implement precise frame-specific movement.
6. Ask blender-lookdev to lock styleframes, typography, geometry, lighting, camera and colors.
7. Produce a low-resolution complete animatic and human review report.
8. Produce an independently rendered polished 90-frame proof before scaling up.
9. On proof approval, generate native .blend scenes and image sequences, mix and encode outputs.
10. Ask blender-qa to report machine checks and human visual/listening gates and package deliverables.

## Hierarchy
Original supplied assets > user-approved creative brief > timeline configuration > shot implementation > general presets. Do not change the brand to fit a default aesthetic. Stop full production at explicit human approval boundaries.
## Non-negotiable operation rules

- Use the approved project brief and declarative frame/event specification; never invent missing institutional facts, copy or licenses.
- Produce native Blender bpy objects and editable .blend scene data, not a browser animation mislabeled as Blender.
- Verify using actual tests, rendered frames, reproducible commands and output paths.
- Technical PASS is distinct from aesthetic or listening HUMAN_REVIEW_REQUIRED.
- If required assets or executable APIs are unavailable, report BLOCKED; never silently substitute.
