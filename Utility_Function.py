import bpy

def get_addon_preferences():
    addon_name = __package__.split(".")[0]
    addon_preferences = bpy.context.preferences.addons[addon_name].preferences 
    return addon_preferences

def update_UI():

    for screen in bpy.data.screens:
        for area in screen.areas:
            area.tag_redraw()
