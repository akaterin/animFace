bl_info = {
    "name": "Video Animation",
}

import bpy
import sys
sys.path.append("/Users/admin/Studies/animFace/blender-addon/")
sys.path.append("/Users/admin/Studies/animFace/face-units-extractor/")
from prepare_file import FilePreparer

class ActionUnitsLoadOperator(bpy.types.Operator):
    bl_label = "Load AUs file"
    bl_idname = "object.file_loader"

    filename = bpy.props.StringProperty()

    def __init__(self, au_reader=FilePreparer()):
        self.au_reader = au_reader

    def execute(self, context):
        print('executing..')
        print(self.filename)
        result = self.au_reader.prepare(self.filename)
        print(result)
        self.reset_current_frame(context)
        self.animate(context, result)
        return {'FINISHED'}

    def reset_current_frame(self, context):
        context.scene.frame_set(1)

    def animate(self, context, actionUnits):
        prevState = {}
        for frameNo, frame in enumerate(actionUnits):
            currentState = {}
            for actionUnit in frame:
                label, value = actionUnit
                currentState["Mfa" + label] = value
            dissapearingActionUnts = list(set(prevState.keys()) - currentState.keys())
            #TODO Should I set zero for new ones?
            for dissapearingAU in dissapearingActionUnts:
                currentState[dissapearingAU] = 0.0
            for label, value in currentState.items():
                obj = context.scene.objects.active
                obj[label] = value
                obj.keyframe_insert(data_path='["' + label + '"]', frame=frameNo)
            prevState = currentState

class VideoAnimationPanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Video Animation Panel"
    bl_idname = "OBJECT_PT_hello"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "Video Animation"

    def draw(self, context):
        layout = self.layout

        obj = context.object

        row = layout.row()
        row.prop(obj, "filename", expand=True)

        row = layout.row()
        props = layout.operator(ActionUnitsLoadOperator.bl_idname)
        props.filename = obj.filename

def register():
    bpy.utils.register_class(ActionUnitsLoadOperator)
    bpy.utils.register_class(VideoAnimationPanel)
    bpy.types.Object.filename = bpy.props.StringProperty()

def unregister():
    bpy.utils.unregister_class(ActionUnitsLoadOperator)
    bpy.utils.unregister_class(VideoAnimationPanel)
    del bpy.types.Object.filename


if __name__ == "__main__":
    register()

