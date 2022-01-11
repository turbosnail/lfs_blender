import bpy

from ..lfs import lfs


class SREExporterMenu(bpy.types.Operator):
    bl_idname = "export_sre.scene"
    bl_label = "Export SRE"

    filename_ext = ".sre"

    filepath = bpy.props.StringProperty(subtype='FILE_PATH')

    def execute(self, context):
        # Append .sre if needed
        filepath = self.filepath
        if not filepath.lower().endswith(self.filename_ext):
            filepath += self.filename_ext

        # exporter = lfs.SreExport(filepath)
        # exporter.export()

        return {"FINISHED"}

    def invoke(self, context, event):
        WindowManager = context.window_manager
        WindowManager.fileselect_add(self)
        return {"RUNNING_MODAL"}


def menu_func(self, context):
    self.layout.operator(SREExporterMenu.bl_idname, text="Live For Speed SRE (.sre)")