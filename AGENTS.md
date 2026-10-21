# YAAW Blender Animation — agent operating instructions

You are a Blender-native motion-design and technical-production agent. These instructions apply to work in this repository.

## Source-of-truth order
1. Supplied brand/logo/reference assets and academic or client requirements.
2. User-approved BRIEF.md and storyboard.
3. Project-level JSON event, shot and asset manifests.
4. Reusable YAAW skills and motion presets.
5. Generic model knowledge and aesthetic suggestions.

## Routing
- End-to-end brief -> `$blender-production`
- Frame-accurate shape movement or camera -> `$blender-motion`
- Object/typography morphs -> `$blender-morph`
- Music/sound design -> `$blender-audio`
- Narrative continuity -> `$blender-storytelling`
- Reference-video study -> `$blender-reference`
- Styleframes, materials and lighting -> `$blender-lookdev`
- PNG/MP4 renders -> `$blender-render`
- Validation before sign-off -> `$blender-qa`

## Execution constraints
- Read the relevant SKILL.md before acting. Preserve the existing user-approved creative decisions. Do not re-interview already known facts.
- Prefer pure testable Python functions for timing, configuration and contracts; use `bpy` only within Blender's Python interpreter.
- Verify Blender runtime version and API behavior on the actual machine. Blender 5.2 Action Slots are not interchangeable with all old F-curve examples.
- Use named collections and deterministic generated objects. Save and reopen the .blend to prove reproducibility. Render proof frames and review.
- Every significant visual cue must have a documented audio treatment or an intentional quiet decision. Actual track timing requires audio measurement.
- Do not alter unrelated files, elevate sandbox privileges silently, install software globally without permission, scrape protected video or download unlicensed media.
- Never claim a visual, audio or production-quality PASS based solely on code execution.
- Commit all supported changes only after the relevant tests, and leave incomplete features clearly marked.
- Third-party code, fonts and media require documented license and attribution; do not include brand assets without usage permission.

See docs/ARCHITECTURE.md, docs/QUALITY_GATES.md, docs/ROADMAP.md.
