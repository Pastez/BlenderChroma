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
        self.modeChanged('init')

    def modeChanged(self, mode):
        if (self.lastMode != mode):
            self.lastMode = mode

            color = ChromaColor(10, 10, 10)
            isEditMode = mode == 'EDIT_MESH'
            if (isEditMode):
                color = Colors.RED

            tmp = [[0 for x in range(22)] for y in range(6)]
            for i in range(0, 6):
                for j in range(0, 22):
                    tmp[i][j] = color
            self.chromaApp.Keyboard.setCustomGrid(tmp)
            self.chromaApp.Keyboard.setCustomKey(keys=[
                ChromaKey(KeyboardKeys.G, Colors.WHITE),
                ChromaKey(KeyboardKeys.S, Colors.WHITE),
                ChromaKey(KeyboardKeys.Tab, Colors.WHITE if isEditMode else Colors.RED),
            ])
            self.chromaApp.Keyboard.applyGrid()

    def __del__(self):
        # bpy.types.SpaceView3D.draw_handler_remove(self.handle, 'WINDOW')
        del self.chromaApp