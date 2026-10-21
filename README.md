# YAAW Blender Animation

**A Blender-native, agent-operated motion design workflow.** Build expressive brand animations, 2.5D/3D graphics, kinetic typography, music-led scenes and editable Blender projects using Codex and Python.

## Status

Early-stage project scaffold. The timing model, validation contracts, skill instructions and offline unit tests are implemented. A native `bpy` smoke builder is supplied but **has not been executed or visually verified under Blender 5.2.2**. This is not yet a production-grade animation engine.

## Core principles

- Blender is the source of truth: editable `.blend` files, real geometry, Action Slots, F-curves, materials, cameras, lights and scene collections.
- One recognizable motif can flow through multiple visual ideas. Transitions connect ideas; audio emphasizes significant motion.
- Creative briefs define fonts, colors, pacing and visual hierarchy. Never impose one universal aesthetic.
- Music is analyzed before locking significant sound cues. Exact frame intervals are represented in declarative project configuration.
- Render, inspect, improve and verify. Passing structural tests never means aesthetic approval.
- Retain license and attribution notices when incorporating third-party code or media.

## Repository

```text
.agents/skills/          Independent Codex skills for Blender workflows
src/yaaw_blender/       Frame-time conversion, audio grid and QA contracts
blender_scripts/        Blender 5.2 scene builders (requires bpy)
tests/                  Dependency-free offline Python tests
projects/_template/     Example declarative project
docs/                   Architecture, roadmap and acceptance gates
.github/workflows/      Static validation in GitHub Actions
```

## Getting started

```powershell
git clone https://github.com/QuackyPROG/yaaw-blender-animation.git
cd yaaw-blender-animation
python -m unittest discover -s tests -v
blender --background --python-exit-code 3 --python blender_scripts/build_smoke.py
```

If Blender is not in PATH, invoke its installed executable. The smoke builder writes `outputs/smoke/yaaw_motion_smoke.blend` and a reference PNG. Inspect both before accepting the render as successful.

Run Codex from the repository root and invoke `$blender-production` for an approved project brief. Read `AGENTS.md`, `docs/ARCHITECTURE.md`, `docs/QUALITY_GATES.md`, and `docs/CODEX_IMPLEMENTATION_PROMPT.md` before performing further implementation.

## Next milestones

1. Reproducible Blender 5.2.2 save/reopen/render proof.
2. Real Action Slot, camera, contour morph and editable typography primitives.
3. Audio beat analysis, reference breakdown and exact SFX event manifests.
4. Polished 90-frame audiovisual demonstration.
5. Reusable motion library after visual quality verification.
