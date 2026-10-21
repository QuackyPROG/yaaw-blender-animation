---
name: blender-qa
description: Use for scene topology, action-curve, asset, timeline, render, licensing, sound sync and human visual quality checks.
---

# Blender production quality assurance

Machine gates: required files and license manifest, all scene collections, unique object IDs, 3D renderable geometry (not a picture pretending to be a modeled object), valid Action Slots/keyframes, correct cameras, safe projected text bounds, contiguous shot frames, source .blend reopen, full PNG count and encoded output metadata. Audit frames -2,-1,0,+1,+2 around transition boundaries.

Human gates: playback at normal speed with sound, silent motion review, final identity comparison, readable and intentional composition, convincing morphs, pleasant audio balance. Never convert HUMAN_REVIEW_REQUIRED into PASS on automated evidence alone.

Each result: {status: PASS|FAIL|BLOCKED|NOT_RUN|HUMAN_REVIEW_REQUIRED, evidence_paths, command, threshold, actual, notes}. If failing, fix and rerun the original threshold; don't lower it silently.
## Non-negotiable operation rules

- Use the approved project brief and declarative frame/event specification; never invent missing institutional facts, copy or licenses.
- Produce native Blender bpy objects and editable .blend scene data, not a browser animation mislabeled as Blender.
- Verify using actual tests, rendered frames, reproducible commands and output paths.
- Technical PASS is distinct from aesthetic or listening HUMAN_REVIEW_REQUIRED.
- If required assets or executable APIs are unavailable, report BLOCKED; never silently substitute.
