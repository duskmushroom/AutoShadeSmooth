bl_info = {
    "name": "Auto Shade Smooth",
    "author": "DuskMushroom",
    "version": (1, 0),
    "blender": (3, 1, 2),
    "category": "Object",
    "location": "View3D > Object > Auto Shade Smooth",
    "description": "Saves a few clicks when smooth shading objects",
}


import bpy

class AutoShadeSmooth(bpy.types.Operator):
    """ Script"""      
    bl_idname = "object.autoshadesmooth"        
    bl_label = "Auto Shade Smooth"         
    bl_options = {'REGISTER', 'UNDO'}  

    def execute(self, context):        

        # The original script
        scene = context.scene
        bpy.ops.object.shade_smooth()
        bpy.context.object.data.use_auto_smooth = True

        return {'FINISHED'}            


def menu_func(self, context):
    self.layout.operator(AutoShadeSmooth.bl_idname)

def register():
    bpy.utils.register_class(AutoShadeSmooth)
    bpy.types.VIEW3D_MT_object_context_menu.append(menu_func)
    bpy.types.VIEW3D_MT_object.append(menu_func)  

def unregister():
    bpy.utils.unregister_class(AutoShadeSmooth)


if __name__ == "__main__":
    register()