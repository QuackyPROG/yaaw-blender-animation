# Blender-native architecture decisions

The implementation uses Blender as the authoritative editable animation environment. Every generic motion-design concept is implemented natively and tested against real Blender scene objects.

| Capability | Blender-native implementation | Verification |
|---|---|---|
| Frame-accurate timeline | Python Fraction, inclusive shot intervals | Offline unit tests |
| 3D scene construction | bpy meshes, curves, Text, collections | Blender smoke test |
| Elastic motion | Keyframes, Action Slots, F-curves and intentional easing | Frame samples |
| True shape morph | Registered contours, compatible shape keys or Geometry Nodes | Topology + visual tests |
| Flowing electricity / ribbons | Resample Curve, Trim Curve, Curve to Mesh | Geometry + render tests |
| Camera choreography | Camera rigs, Track To/Follow Path, explicit projections | Screen-space framing |
| Kinetic typography | Editable Text, per-word staggering and curve extrusion | Glyph bbox + readability |
| Music-led pacing | Measured PCM onsets, downbeat phase, JSON cues | Waveform and human listening |
| Sound | 48 kHz stereo mix and FFmpeg | A/V sync and peak checks |
| Export | Background Blender + PNG sequence + MP4 encode | Reopen/render/ffprobe |
| QA | Objective reports plus separate visual approval | Evidence manifest |

## Principles

1. Creative briefs override preset aesthetic defaults.
2. Every major motion needs a visual purpose; every significant sound cue has a named event.
3. A recurring motif maintains continuity rather than random decorative cuts.
4. A true morph cannot silently be replaced by an opacity crossfade.
5. The actual Blender scene and its renders are the ground truth.
6. Structural PASS is never automatic approval of an artistic result.
7. No unauthorized download, asset substitution or missing license declarations.
