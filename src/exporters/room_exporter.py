#
#  (C) Copyright 2017, 2018  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

"""Room exporter to structured text format."""

from datetime import *

from drawing import Drawing


class RoomExporter:
    """Room exporter to structured text format."""

    VERSION = 1

    def __init__(self, filename, drawing):
        """Initialize the exporter, set the filename to be created and a sequence of entities."""
        self.filename = filename
        self.rooms = drawing.rooms

    @staticmethod
    def get_timestamp():
        """Get the timestamp for the current time and format it according to ISO."""
        return datetime.now().isoformat(sep=' ')

    @staticmethod
    def output_timestamp(fout):
        """Write the timestamp into the generated file."""
        fout.write("created: {c}\n".format(c=RoomExporter.get_timestamp()))

    @staticmethod
    def output_version(fout):
        """Write the version into the generated file."""
        fout.write("version: {v}\n".format(v=RoomExporter.VERSION))

    @staticmethod
    def write_room(fout, room):
        """Write the room data into the generated file."""
        vertexes = room["polygon"]
        # export only room with polygon
        if vertexes is not None:
            fout.write("R {id} {vertex_count}".format(id=room["room_id"],
                                                      vertex_count=len(vertexes)))
            for vertex in vertexes:
                fout.write(" {x} {y}".format(x=vertex[0], y=vertex[1]))
        # room without polygon
        else:
            fout.write("R {id} 0".format(id=room["room_id"]))

        if "type" in room:
            fout.write(" {t}".format(t=room["type"]))

        fout.write("\n")

    def export(self):
        """Export room list into the text file."""
        with open(self.filename, "w") as fout:
            RoomExporter.output_version(fout)
            RoomExporter.output_timestamp(fout)

            fout.write("rooms: {r}\n".format(r=len(self.rooms)))
            for room in self.rooms:
                RoomExporter.write_room(fout, room)
