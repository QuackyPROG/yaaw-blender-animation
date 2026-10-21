# Architecture — Blender-native motion automation

## Design goal
YAAW Blender Animation is an agent-operated creative production framework. Blender owns geometry, materials, lighting, animation, camera and editable scene output. CPython owns configuration validation, precise frame arithmetic, project orchestration, music analysis and render-output auditing. FFmpeg handles PCM conversion, sound mixing and final video encoding.

## Execution layers
```
Creative brief / reference / license manifest
                |
Story + exact timeline + 120-BPM phase audit
                |
    Scene builders (Python + bpy)
        |          |          |
  real geometry  typography  rigged camera
        |          |          |
        +---  keyframed native Blender Scene ---+
                               |
           headless still / draft / PNG frames
                               |
              audio arrangement + FFmpeg
                               |
         QA evidence, .blend and final MP4
```

## Canonical project model
Use a versioned project.json as one source of truth: video fps, frame_start/end, canvas, brand assets, style status, shots, persistent motif, camera poses, music timing analysis, audio events and gate status. Frame 1 is time zero, frame F maps to `(F-1)/fps`; shots use inclusive start/end and must cover the range without gaps or overlapping output frames. Sounds use stable IDs and measured times/frames. Never infer that a 120-BPM title establishes actual downbeat phase.

## Blender ownership boundaries
- `src/yaaw_blender`: pure-Python time math, validation and metadata.
- `blender_scripts`: import `bpy`, inspect installed version, build actual editable datablocks and save .blend. No browser DOM or CSS renderer.
- `.agents/skills`: narrowly scoped procedural instructions used by Codex in the repository.
- `tests`: CPython-independent tests and future optional Blender integration tests.
- `outputs/`: ignored generated preview/render files, not committed by default.

## Critical technical considerations
**Animation:** Work with Blender 5.2 Actions/Slots. Test F-curve construction against installed bpy and evaluate actual keyframed values through the dependency graph. Pure pose functions should be seek-safe and independent of previously evaluated frame.

**Morphing:** Mesh shape keys need identical topology. Noncorresponding outlines require planned resampling, winding/landmark registration and explicit point correspondence. Geometry Nodes can extrude/truncate curves; a hidden crossfade is not equivalent to contour morphing.

**Look development:** editable Text/Curve/Mesh components with authored normals, bevels, PBR material nodes, shadows and at least one physically meaningful light source. Keep typography screen-projected and readable during perspective camera movement.

**Rendering:** verify engine enum, save/reopen, render PNG/EXR masters, then encode MP4. Use separate shot output folders if memory/concurrency dictates. For an 8GB laptop, preflight memory and perform 1/4-resolution test renders before full-resolution long sequences.

**Audio:** actual licensed music and SFX acquisition requires permissions, source provenance and checksum; analysis generates downbeats/transients with confidence and optional human corrections. Export stereo 48 kHz mix; audit encoded onset/fps/sample rate.

## Skill and test contracts
Each skill produces tangible files: brief, storyboard, scene, stills, JSON timing, QA reports. Status values PASS, FAIL, BLOCKED, NOT_RUN and HUMAN_REVIEW_REQUIRED. An aesthetic subjective review must never be represented as a passing machine test.

## Documentation
Blender API: https://docs.blender.org/api/5.2/
Geometry Nodes: https://docs.blender.org/manual/en/5.2/modeling/geometry_nodes/
Blender CLI: https://docs.blender.org/manual/en/5.2/advanced/command_line/
Agent skills: https://developers.openai.com/codex/skills/
