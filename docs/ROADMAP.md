# YAAW Blender — incremental implementation roadmap

## v0.1 — Scaffold
- [x] Native Python timing conversion, beat grid, project contract validator and 11 unit tests.
- [x] Nine scoped skills for narrative, motion, morph, audio, lookdev, reference, render, production and QA.
- [x] Blender 5.2-targeted bpy smoke builder for basic scene, keyframes, camera, lighting and save/render.
- [ ] Run the smoke builder on the owner's actual Blender 5.2.2 Windows installation; inspect render and saved file.
- [ ] Record real Blender version compatibility and render resource usage.

## v0.2 — Motion primitives
- [ ] F-curve / Action Slot inspection and stable named rig APIs.
- [ ] Drop/impact, spring settle, type stagger, curve growth and camera dolly/orbit.
- [ ] Resampled registered contour morph with actual image verification.
- [ ] Unit, Blender-integration and visual regression tests for each primitive.

## v0.3 — Music-led showreel pipeline
- [ ] FFmpeg-based reference contact sheet and shot annotation report.
- [ ] Real beat/downbeat phase estimation and manual confidence gate.
- [ ] Music-events, SFX-manifest and final stereo PCM mix generation.
- [ ] A/V onset drift and source-license audits.

## v0.4 — End-to-end reproducible proof
- [ ] CLI build/validate/render/encode/report commands.
- [ ] 90-frame native Blender proof with true 3D depth, matched object transformations, kinetic typography, camera motion, audio and actual final MP4.
- [ ] Human approval gate that blocks a full 750-frame production until quality is accepted.

## v1.0 — Curated motion library
- [ ] Every preset has real .blend, before/middle/after renders, parameter schema and tested benchmark.
- [ ] Improve render resilience: shot-level resume, cache hashes, packed assets, GPU-memory budget.
- [ ] Template project generation and consistent license/attribution strategy for release.

Important: roadmap items are plans, not shipping features. Keep README feature claims aligned with verified work.
