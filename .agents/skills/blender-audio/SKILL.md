---
name: blender-audio
description: Use for licensed music analysis, beat/downbeat mapping, audio event manifests, sound-effect synchronization, mixing and loudness validation.
---

# Music-directed Blender sound choreography

Input: licensed local music, exact FPS, project frame range, and visual event IDs. First log title, creator, license, hash and attribution obligations; avoid unauthorized downloads.

Use ffprobe/FFmpeg or approved DSP packages to read the actual waveform, estimate BPM and first-downbeat phase, detect significant transients/section changes, and document confidence. A track title saying 120 BPM is not verified rhythm-phase data. Export music_events.json with seconds AND 1-based project frames.

For every significant object contact, lock, morph resolve, reveal or camera accent assign an SFX, musical accent or intentional-silence decision. Sounds must serve a hierarchy, not fill every micro-movement. Mix to 48 kHz WAV before final mux; report onset difference in frames, peak/loudness, duration and missing cues. The final audio must be listened to; mark HUMAN_REVIEW_REQUIRED until then.

Geometry Nodes audio-reactive effects are supplementary. FFT-reactive movement does not replace music structure analysis.
## Non-negotiable operation rules

- Use the approved project brief and declarative frame/event specification; never invent missing institutional facts, copy or licenses.
- Produce native Blender bpy objects and editable .blend scene data, not a browser animation mislabeled as Blender.
- Verify using actual tests, rendered frames, reproducible commands and output paths.
- Technical PASS is distinct from aesthetic or listening HUMAN_REVIEW_REQUIRED.
- If required assets or executable APIs are unavailable, report BLOCKED; never silently substitute.
