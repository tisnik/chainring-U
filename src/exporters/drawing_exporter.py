#
#  (C) Copyright 2017  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

from datetime import *

from drawing import Drawing


class DrawingExporter:
    VERSION = 1

    def __init__(self, filename, drawing):
        self.filename = filename
        self.entities = drawing.entities
        self.rooms = drawing.rooms

    @staticmethod
    def get_timestamp():
        return datetime.now().isoformat(sep=' ')

    @staticmethod
    def output_timestamp(fout):
        fout.write("created: {c}\n".format(c=DrawingExporter.get_timestamp()))

    @staticmethod
    def output_version(fout):
        fout.write("version: {v}\n".format(v=DrawingExporter.VERSION))

    @staticmethod
    def write_room(fout, room):
        vertexes = room["polygon"]
        fout.write("R {id} {vertex_count}".format(id=room["room_id"],
                                                  vertex_count=len(vertexes)))
        for vertex in vertexes:
            fout.write(" {x} {y}".format(x=vertex[0], y=vertex[1]))
        fout.write("\n")

    def export(self):
        with open(self.filename, "w") as fout:
            DrawingExporter.output_version(fout)
            DrawingExporter.output_timestamp(fout)
            fout.write("entities: {e}\n".format(e=len(self.entities)))
            fout.write("rooms: {r}\n".format(r=len(self.rooms)))
            for entity in self.entities:
                fout.write(entity.str())
                fout.write("\n")
            for room in self.rooms:
                DrawingExporter.write_room(fout, room)
