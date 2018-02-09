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

"""Drawing exporter to structured text format."""

from datetime import *

from drawing import Drawing
from geometry.bounds import Bounds
from geometry.rescaler import Rescaler


class DrawingExporter:
    """Drawing exporter to structured text format."""

    VERSION = 1
    SCALES = [
        [320, 240],
        [400, 300],
        [640, 480],
        [800, 600],
        [1024, 768]
    ]

    def __init__(self, filename, drawing):
        """Initialize the exporter, set the filename to be created and a sequence of entities."""
        self.filename = filename
        self.entities = drawing.entities
        self.rooms = drawing.rooms

    @staticmethod
    def get_timestamp():
        """Get the timestamp for the current time and format it according to ISO."""
        return datetime.now().isoformat(sep=' ')

    @staticmethod
    def output_timestamp(fout):
        """Write the timestamp into the generated file."""
        fout.write("created: {c}\n".format(c=DrawingExporter.get_timestamp()))

    @staticmethod
    def output_version(fout):
        """Write the version into the generated file."""
        fout.write("version: {v}\n".format(v=DrawingExporter.VERSION))

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
        fout.write("\n")

    def export(self):
        """Export the whole drawing into the text file."""
        with open(self.filename, "w") as fout:
            DrawingExporter.output_version(fout)
            DrawingExporter.output_timestamp(fout)

            bounds = Bounds.computeBounds(self.entities)
            fout.write("bounds: {b}\n".format(b=bounds))

            for scale in DrawingExporter.SCALES:
                xoffset, yoffset, s = Rescaler.computeScale(bounds, scale[0], scale[1])
                fout.write("scale: {w} {h} {s}\n".format(w=scale[0], h=scale[1], s=s))

            fout.write("entities: {e}\n".format(e=len(self.entities)))
            fout.write("rooms: {r}\n".format(r=len(self.rooms)))
            for entity in self.entities:
                fout.write(entity.str())
                fout.write("\n")
            for room in self.rooms:
                DrawingExporter.write_room(fout, room)
