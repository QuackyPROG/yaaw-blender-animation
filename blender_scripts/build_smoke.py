"""Minimal Blender 5.2 native smoke renderer. Use Blender's bundled Python, not CPython.

NOT a finished YAAW motion showreel. Creates editable scene geometry, keyframes,
camera and lights, saves a .blend, renders a still; suitable for local preflight.
"""
from pathlib import Path
import bpy
from mathutils import Vector

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'outputs'/'smoke'
OUT.mkdir(parents=True, exist_ok=True)
if bpy.app.version[:2] != (5, 2):
    raise RuntimeError(f'Requires Blender 5.2.x, got {bpy.app.version_string}')

bpy.ops.wm.read_factory_settings(use_empty=True)
scene=bpy.context.scene
scene.frame_start=1; scene.frame_end=90; scene.render.fps=30
scene.render.resolution_x=640;scene.render.resolution_y=360;scene.render.resolution_percentage=100
scene.render.image_settings.file_format='PNG'
engines=[item.identifier for item in bpy.types.RenderSettings.bl_rna.properties['engine'].enum_items]
eevee=next((engine for engine in engines if 'EEVEE' in engine),None)
if not eevee: raise RuntimeError(f'Eevee render engine unavailable: {engines}')
scene.render.engine=eevee
if scene.world is None:
    scene.world=bpy.data.worlds.new('YAAW_WORLD')
scene.world.color=(0.03,0.06,0.15)

coll=bpy.data.collections.new('YAAW_PROOF_GEOMETRY');scene.collection.children.link(coll)
def move_to_proof_collection(obj):
    for c in list(obj.users_collection): c.objects.unlink(obj)
    coll.objects.link(obj)

def rgba(h):
    x=h.lstrip('#');rgb=[int(x[i:i+2],16)/255 for i in (0,2,4)]
    def srgb_to_linear(v): return v/12.92 if v<=0.04045 else ((v+0.055)/1.055)**2.4
    return tuple(srgb_to_linear(v) for v in rgb)+(1.0,)

mat=bpy.data.materials.new('MAT_SEED_ORANGE');mat.diffuse_color=rgba('#E97C1D')
mat.use_nodes=True
pbr=mat.node_tree.nodes.get('Principled BSDF')
if pbr:
    pbr.inputs['Base Color'].default_value=mat.diffuse_color
    pbr.inputs['Roughness'].default_value=0.36

bpy.ops.mesh.primitive_uv_sphere_add(segments=32, ring_count=16, location=(0,0,0.6))
ball=bpy.context.object;ball.name='SEED_01_MESH';move_to_proof_collection(ball);ball.data.materials.append(mat)
for frame,z in [(1,4.0),(13,0.6),(21,1.7),(36,1.0),(60,0.65),(90,0.65)]:
    ball.location.z=z; ball.keyframe_insert(data_path='location',frame=frame,index=2)
for frame,scale in [(1,(1,1,1)),(13,(1.23,1.23,0.74)),(18,(1,1,1)),(21,(0.93,0.93,1.11)),(36,(1,1,1))]:
    ball.scale=scale;ball.keyframe_insert(data_path='scale',frame=frame)

bpy.ops.mesh.primitive_cube_add(size=2, location=(0,0,-0.48))
plane=bpy.context.object;plane.name='GROUND_GEOMETRY';move_to_proof_collection(plane);plane.scale=(6,3,0.25)

font=bpy.data.curves.new('TextCurve',type='FONT');font.body='YAAW  /  MOTION';font.size=0.65;font.extrude=0.018;font.bevel_depth=0.006
text=bpy.data.objects.new('CAMPAIGN_TYPE',font);coll.objects.link(text);text.location=(-2.85,0,2.5)
text.hide_render=False
for frame,val in [(1,0.001),(19,0.001),(36,1.0)]:
    text.scale=(val,val,val);text.keyframe_insert(data_path='scale',frame=frame)

light_data=bpy.data.lights.new('KEY_SOFTBOX','AREA');light_data.energy=750;light_data.shape='DISK';light_data.size=5
light=bpy.data.objects.new('KEY_SOFTBOX',light_data);scene.collection.objects.link(light);light.location=(-3,-4,6)

cam_data=bpy.data.cameras.new('CAM_MAIN');cam=bpy.data.objects.new('CAM_MAIN',cam_data);scene.collection.objects.link(cam)
cam.location=(0,-10,4.2);target=Vector((0,0,1));direction=target-cam.location;cam.rotation_euler=direction.to_track_quat('-Z','Y').to_euler();cam_data.type='ORTHO';cam_data.ortho_scale=8
scene.camera=cam
text.rotation_euler=cam.rotation_euler

scene.frame_set(36)
blend=OUT/'yaaw_motion_smoke.blend';bpy.ops.wm.save_as_mainfile(filepath=str(blend))
scene.render.filepath=str(OUT/'yaaw_smoke_frame0036.png')
bpy.ops.render.render(write_still=True)
print('YAAW_BPY_SMOKE_OK',blend)
