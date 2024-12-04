bl_info = {
    "name": "Center Plugin",
    "description": "Centers the selected object at the origin",
    "category": "Object",
    "blender": (4, 3, 0),
    "version": (0, 1, 0),
    "author": "Nightmare1984",
}

import bpy

class CenterPlugin(bpy.types.Operator):
    bl_idname = "object.center_plugin"
    bl_label = "Center Plugin"
    bl_options = {'REGISTER', 'UNDO'}
    bl_description = "Centers the selected object at the origin"

    def execute(self, context):
        for obj in context.selected_objects:
            if obj is not None:
                obj.location = (0.0, 0.0, 0.0)
        return {'FINISHED'}

def menu_func(self, context):
    self.layout.operator(CenterPlugin.bl_idname, text=CenterPlugin.bl_label, icon='OBJECT_ORIGIN').description = CenterPlugin.bl_description

def register():
    bpy.utils.register_class(CenterPlugin)
    bpy.types.VIEW3D_MT_object.append(menu_func)

def unregister():
    bpy.utils.unregister_class(CenterPlugin)
    bpy.types.VIEW3D_MT_object.remove(menu_func)

