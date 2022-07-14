from . import Utility_Function

import bpy

addon_name = __package__.split(".")[0]


def append_panel_class(panels, cls, category, label):
    panel = cls 
    item = [panel, category, label]
    panels.append(item)

    return panels

def append_panel_module(panels, module, category, label):

    for cls in module.classes:
        if isinstance(cls, type):
            panels = append_panel_class(panels, cls, category, label)
    
    return panels

def update_panel(self, context):

    addon_preferences = Utility_Function.get_addon_preferences()
    
    message = ": Updating Panel locations has failed"

    panels = []

    from . import Panels

    panel_module = Panels
    category = addon_preferences.PANEL_Frame_Remapper_Category
    label = addon_preferences.PANEL_Frame_Remapper_Label
    panels = append_panel_module(panels, panel_module, category, label) 

    try:
        pass
        for item in panels:

            panel = item[0]
            category = item[1]
            label = item[2]
           
            if "bl_rna" in panel.__dict__:
                bpy.utils.unregister_class(panel)


            panel.bl_category = category
            panel.bl_label = label
            bpy.utils.register_class(panel)

    except Exception as e:
        print("\n[{}]\n{}\n\nError:\n{}".format(__name__, message, e))
        pass



ENUM_Tabs = [("PANELS", "Panels", "Panels"),("GENERAL", "General", "General") , ("KEYMAPS","Keymaps","Keymaps")]

ENUM_filter_mode = [("INCLUDE","Include","Include"),("EXCLUDE","Exclude","Exclude")]



class FRL_Preferences(bpy.types.AddonPreferences):

    bl_idname = addon_name 

    TABS_Preferences: bpy.props.EnumProperty(items=ENUM_Tabs)

    PANEL_Frame_Remapper: bpy.props.BoolProperty(default=True)
    PANEL_Frame_Remapper_Category: bpy.props.StringProperty(default="Frame Ranger Lite", update=update_panel)
    PANEL_Frame_Remapper_Label: bpy.props.StringProperty(default="Frame Remapper", update=update_panel)

    PANEL_Frame_Remapper_Output_Properties_Panel: bpy.props.BoolProperty(default=True)
    PANEL_Frame_Remapper_Side_Panel: bpy.props.BoolProperty(default=False)

    TU_Animation_Player: bpy.props.BoolProperty(default=True)
    TU_Frame_Range: bpy.props.BoolProperty(default=True)
    TU_Auto_Frame_Range: bpy.props.BoolProperty(default=True)


    def draw(self, context):

        layout = self.layout

        col = layout.column(align=True)

        col.prop(self, "PANEL_Frame_Remapper", text="Frame Remapper Panel")


        if self.PANEL_Frame_Remapper:
            box = col.box()
            box.prop(self, "PANEL_Frame_Remapper_Category", text="Category")
            box.prop(self, "PANEL_Frame_Remapper_Label", text="Label")
            box.prop(self, "PANEL_Frame_Remapper_Output_Properties_Panel", text="Output Properties Panel")
            box.prop(self, "PANEL_Frame_Remapper_Side_Panel", text="Side Panel")


        col.separator()
        col.label(text="Timeline Utility", icon="TIME")

        box = col.box()

        box.prop(self, "TU_Animation_Player", text="Animation Player")
        box.prop(self, "TU_Frame_Range", text="Frame Range")
        box.prop(self, "TU_Auto_Frame_Range", text="Auto Frame Range")









classes = [FRL_Preferences]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    update_panel(None, bpy.context)

def unregister():

    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
