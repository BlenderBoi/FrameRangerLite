bl_info = {
    "name": "Frame Ranger Lite",
    "author": "BlenderBoi, Blastframe",
    "version": (2, 0, 2),
    "blender": (3, 1, 0),
    "description": "Utilities for Frame related operations",
    "warning": "",
    "wiki_url": "",
    "category": "Utility",
}

import bpy

from . import Autofit_Framerange 
from . import Animation_Player
from . import Operators
from . import Preferences
from . import Base_Panel


import addon_utils

modules =  [Base_Panel, Operators, Autofit_Framerange, Preferences, Animation_Player]

def register():

    for mod in addon_utils.modules():
        if mod.bl_info.get('name', (-1, -1, -1)) == "Frame Ranger" and mod.bl_info.get('author', (-1, -1, -1)) == "BlenderBoi":
            if addon_utils.check(mod.__name__)[1]:
                addon_utils.disable(mod.__name__, default_set=True, handle_error=None)

    for module in modules:
        module.register()

def unregister():


    for module in modules:
        module.unregister()

if __name__ == "__main__":
    register()














