from datetime import *

class DrawingExporter:

    def __init__(self, filename, entities):
        self.filename = filename
        self.entities = entities

    def get_timestamp():
        return datetime.now().isoformat(sep=' ')

    def export(self):
        with open(self.filename, "w") as fout:
            fout.write("created: {c}\n".format(c=DrawingExporter.get_timestamp()))
            fout.write("entities: {e}\n".format(e=len(self.entities)))
            for entity in self.entities:
                fout.write(entity.str())
                fout.write("\n")
