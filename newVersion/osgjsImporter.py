import bpy
import struct

class CustomDrawOperator(bpy.types.Operator):
    bl_idname = "object.file_importer"
    bl_label = "Import"
 
    filepath = bpy.props.StringProperty(subtype="FILE_PATH")
 
    def execute(self, context):
        print()
        return {'FINISHED'}
 
    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}


bpy.utils.register_class(CustomDrawOperator)
bpy.ops.object.file_importer('INVOKE_DEFAULT')