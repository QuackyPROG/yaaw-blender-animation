# Codex implementation brief — YAAW Blender Animation

## Role and target
Act as a Blender 5.2.2 technical director, motion designer, audio engineer and Python QA maintainer. Work within QuackyPROG/yaaw-blender-animation, with real tested files rather than prose-only proposals. The project is a reusable general-purpose Blender animation framework; do not hard-code it to one university logo or one campaign style.

## Read first
Read AGENTS.md, README.md, docs/ARCHITECTURE.md, docs/QUALITY_GATES.md, docs/ROADMAP.md, and all nine .agents/skills/*/SKILL.md. Audit the local toolchain, actual Blender API behavior and project tests. Report existing features versus planned features accurately. Preserve all approved user choices.

## Execute in this order
1. **Preflight:** find Blender 5.2.x executable, inspect bpy.app.version, real Eevee enum, ffmpeg/ffprobe, CPU/GPU/RAM, disk and missing dependencies. Avoid global installs without approval.
2. **Smoke proof:** run `blender --background --python-exit-code 3 --python blender_scripts/build_smoke.py`. If errors arise, fix them and add regression tests; do not assume shader or Action Slot API identifiers from older Blender versions. Reopen the saved .blend in a fresh Blender process; render selected frames and inspect actual screenshots.
3. **Native motion:** implement testable drop_impact, elastic_rebound, stagger_type, draw_curve, registered_contour_morph, camera_orbit and hero_settle modules. Each has documented inputs/outputs, generated examples, playback/frame determinism tests and compatibility checks.
4. **Audio:** implement frame-accurate audio event manifest, beat-phase analysis on actual lawfully obtained soundtrack and per-event SFX mix. Use licensed local input; no file-based claim of BPM/phase without waveform analysis. Verify encoded onset offsets.
5. **Artistic proof:** from projects/_template/project.json generate a 90-frame scene with 3D geometry, animation, typography and visual change, a safe camera move, synchronized music/SFX when licensed and an actual MP4. Render a contact sheet and compare transitions. Flag visual/listening review as required.
6. **Repository QA:** run offline and Blender integration tests; generate machine-readable report and human-viewable playback evidence, preserve clean source and avoid version-specific accidental data corruption.

## Failure rules
Do not equate successful Python script execution with a passing design review. Do not modify the academic/client brief, approved brand/wording, protected user files, audio licenses or render target simply to make an invalid build pass. Never fabricate a render, preview, soundtrack listening check or successful Blender 5.2 test.

## Deliverables per stage
Produce actual source modifications, test commands, commit SHA, exact proof PNG/.blend/MP4 paths, measured results and prioritized defects. Stop on unapproved paid calls, external downloads without permission, and on the visual approval gate before producing a long-form final film.
