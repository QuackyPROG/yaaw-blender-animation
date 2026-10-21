# Quality and production acceptance

## Standard
A gate has status PASS, FAIL, BLOCKED, NOT_RUN or HUMAN_REVIEW_REQUIRED, plus an evidence path, procedure, threshold and measured outcome. Failure thresholds must not be weakened to make a build green.

## Gate 1 — Preflight
Check actual Blender executable and version, installed EEVEE engine identifier, Python interpreter, FFmpeg/ffprobe, GPU/CPU/RAM/disk. Verify all provided assets, rights and hashes. Abort only the stage whose dependency cannot be fulfilled.

## Gate 2 — Structural storyboard
Project config parses. Shot IDs unique. Inclusive intervals are contiguous and cover all requested frames exactly. Frame-to-time mapping is documented; beat/phase confidence never fabricated. Render text must match exact approved copy.

## Gate 3 — Native modeling and keyframes
The scene has named Blender collections/meshes/curves/text and meaningful nonzero modeled geometry. Objects have valid transform/action data and required animation keys. Generated .blend can be reopened in another Blender process. No raster poster substitutes for an editable modeled emblem.

## Gate 4 — Motion continuity
Use world-space AND screen-projected comparisons at adjacent shot boundaries. Sample frames at −2,−1,0,+1,+2 around every handoff. Inspect position, apparent velocity, hue/radius and silhouette. Flag sudden visible discontinuity outside documented designed impacts/match cuts.

## Gate 5 — Visual quality
A contact sheet includes anticipation, contact, morph midpoint, settle and final hold. Review at full resolution and downscaled; fonts cannot overlap important geometry, faces or logo. Aesthetic coherence and charming motion require human signoff and are not mechanically provable.

## Gate 6 — Audio and licenses
Each licensed audio asset has source, license, hash and permission. Cue manifest maps unique IDs to nominal and detected effective onsets. Compare audio transient and visual event ≤ 1 frame where measurable, otherwise send to listening review. Measure encoded peak/loudness and confirm no clipping, accidental dead air or unjustified jump.

## Gate 7 — Output integrity
Expected PNG count, correct dimensions, no missing/empty frames. MP4/optional MOV meets requested codec, fps, frame count and duration in ffprobe. Save reproducible Blender project, generator code, project configuration, asset manifest and QA reports.

## Approval boundary
Start with a representative 90-frame proof. Full-scene rendering cannot begin until the user approves rendered visual/motion/music quality. Subjective gate status remains HUMAN_REVIEW_REQUIRED until then.
