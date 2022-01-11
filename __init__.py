
import bpy
from .gui import gui

bl_info = {
    "name": "Export Live For Speed SRE (.sre)",
    "author": "turbosnail",
    "version": (0, 0, 1),
    "blender": (2, 80, 0),
    "location": "File > Export",
    "description": "Export Live For Speed SRE (.sre)",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Import-Export"}


def register():
    bpy.utils.register_class(gui.SREExporterMenu)
    if (2, 80, 0) > bpy.app.version:
        bpy.types.INFO_MT_file_export.append(gui.menu_func)
    else:
        bpy.types.TOPBAR_MT_file_export.append(gui.menu_func)


def unregister():
    bpy.utils.unregister_class(gui.SREExporterMenu)
    if (2, 80, 0) > bpy.app.version:
        bpy.types.INFO_MT_file_export.remove(gui.menu_func)
    else:
        bpy.types.TOPBAR_MT_file_export.remove(gui.menu_func)
