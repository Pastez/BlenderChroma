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

import bpy
from .BlenderChroma import BlenderChromaOperator

def register():
    bpy.utils.register_class(BlenderChromaOperator)

def unregister():
    bpy.utils.unregister_class(BlenderChromaOperator)

if __name__ == "__main__":
    register()
    bpy.ops.pas.blenderchroma('INVOKE_DEFAULT')