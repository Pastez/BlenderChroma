# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name": "Blender Chroma",
    "description": "Adds Razer Chroma support for Blender",
    "author": "Cheerapp Tomasz Kwolek",
    "version": (0, 0, 1),
    "blender": (2, 81, 0),
    "category": "Generic"
}

from . import auto_load
from .BlenderChroma import BlenderChroma
import bpy

auto_load.init()

def register():
    auto_load.register()
    bpy.chromaApp = BlenderChroma(bl_info)

def unregister():
    auto_load.unregister()
    del bpy.chromaApp
    del bpy.chromaAppSubscribe



def edit_mode_changed(*args):
    if (bpy.chromaApp):
        bpy.chromaApp.modeChanged(bpy.context.mode)

bpy.chromaAppSubscribe = {}
subscribe_to = bpy.types.Object, "mode"

bpy.msgbus.subscribe_rna(
    key=subscribe_to,
    owner=bpy.chromaAppSubscribe,
    args=(1, 2, 3),
    notify=edit_mode_changed
    )