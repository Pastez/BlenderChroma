from .ChromaPython import *
from time import sleep
import bpy

class BlenderChroma():
    def __init__(self, description: dict):
        info = ChromaAppInfo()
        info.Title = description.get('name')
        info.Description = description.get('description')
        info.DeveloperName = description.get('author')
        info.DeveloperContact = 'pastezzz@gmail.com'
        info.SupportedDevices = ['keyboard']
        info.Category = 'application'
        self.chromaApp = ChromaApp(info)
        sleep(1)
        self.lastMode = ''

    def modeChanged(self):
        mode = bpy.context.mode
        isEditMode = mode == 'EDIT_MESH'
        if (self.lastMode != mode):
            self.lastMode = mode

            color = ChromaColor(10, 10, 10)
            
            if (isEditMode):
                color = ChromaColor(5, 0, 0)

            tmp = [[0 for x in range(22)] for y in range(6)]
            for i in range(0, 6):
                for j in range(0, 22):
                    tmp[i][j] = color

            self.chromaApp.Keyboard.setCustomGrid(tmp)

        if (isEditMode):
            i = 2
            for mode in bpy.context.scene.tool_settings.mesh_select_mode:
                self.chromaApp.Keyboard.setPosition(Colors.RED if mode else Colors.BLUE, i, 1)
                i = i + 1
        else:
            i = 2
            for collection in bpy.data.collections:
                if not collection.use_fake_user:
                    self.chromaApp.Keyboard.setPosition(Colors.RED if collection.hide_viewport else Colors.GREEN, i, 1)
                    i = i + 1

        self.chromaApp.Keyboard.setCustomKey(keys=[
            ChromaKey(KeyboardKeys.G, Colors.WHITE),
            ChromaKey(KeyboardKeys.S, Colors.WHITE),
            ChromaKey(KeyboardKeys.Tab, Colors.WHITE if isEditMode else Colors.RED),
        ])
        
        self.chromaApp.Keyboard.applyGrid()

    def __del__(self):
        # bpy.types.SpaceView3D.draw_handler_remove(self.handle, 'WINDOW')
        del self.chromaApp

class BlenderChromaOperator(bpy.types.Operator):
    bl_idname = "pas.blenderchroma"
    bl_label = "Initialize Chroma"
    app: BlenderChroma = None

    def modal(self, context, event):
        self.app.modeChanged()
        if event.type == 'ESC':
            del self.app
            print('Chroma app closed')
            return {'FINISHED'}

        return {'PASS_THROUGH'}

    def invoke(self, context, event):
        self.app = BlenderChroma({
            "name": "Blender Chroma",
            "description": "Adds Razer Chroma support for Blender",
            "author": "Cheerapp Tomasz Kwolek"
        })
        print('chroma app invoke!!!')
        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}