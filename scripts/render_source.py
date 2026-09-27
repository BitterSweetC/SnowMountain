import bpy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
bpy.ops.wm.open_mainfile(filepath=str(ROOT/'blender/snow_mountain_world.blend'))
scene=bpy.context.scene
assert bpy.data.collections.get('WEB_EXPORT')
assert bpy.data.objects.get('FPV_Camera').animation_data.action.name=='FPV_Flight'
scene.cycles.device='CPU';scene.cycles.samples=16;scene.render.resolution_percentage=75
scene.render.filepath=str(ROOT/'docs/blender-default.png');scene.camera=bpy.data.objects['Web_Default_Camera'];bpy.ops.render.render(write_still=True)
print('SOURCE_OPEN_RENDER_OK')
