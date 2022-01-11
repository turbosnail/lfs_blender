import bpy


class SreExport:

    file = ""

    def __init__(self, filepath):
        self.file = filepath

    def export(self):

        for obj in bpy.data.object:
            print(obj.type)

        file = open(self.file, 'w')
        file.write("%s\n" % "SREOBJ")
        file.close()
        return True
