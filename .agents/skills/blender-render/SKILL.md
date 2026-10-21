---
name: blender-render
description: Use to render, resume, reopen, composite, encode and inspect native Blender animation image sequences and video outputs.
---

# Blender-native rendering

Probe exact blender executable/version and Eevee/Cycles engine enum. Render representative stills first, then short draft ranges. On low RAM hardware use conservative geometry/texture budgets, measure real memory and frame time, and optimize without deleting approved content.

Save a versioned .blend with relative assets. Test reopen using a new headless process, then render a checkpoint frame. Render a PNG/EXR image sequence to a dedicated output directory (not directly to MP4 as the only master); validate unique ordered filenames, dimensions, continuity and nonzero images. Resume missing frames only.

Encode using ffmpeg and mux licensed audio after image verification. Validate fps, count, stream codecs, audio/sample rate and duration with ffprobe. Report exact commands and measured results. Never mark a Blender build PASS without an actual render.
## Non-negotiable operation rules

- Use the approved project brief and declarative frame/event specification; never invent missing institutional facts, copy or licenses.
- Produce native Blender bpy objects and editable .blend scene data, not a browser animation mislabeled as Blender.
- Verify using actual tests, rendered frames, reproducible commands and output paths.
- Technical PASS is distinct from aesthetic or listening HUMAN_REVIEW_REQUIRED.
- If required assets or executable APIs are unavailable, report BLOCKED; never silently substitute.
