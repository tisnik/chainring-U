"""Room exporter (serializer) to TXT (plain text file)."""

#
#  (C) Copyright 2019  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

class RoomTXTExporter:
    """Room exporter (serializer) to TXT."""

    def __init__(self, filename, drawing):
        """Initialize the exporter, set the filename to be created and a sequence of entities."""
        self.filename = filename
        self.rooms = drawing.rooms

    def export(self):
        rooms = self.rooms
        with open(self.filename, mode='w') as fout:
            fout.write("SAP ID          gr.ID   Zakreslena  Souřadnic\n")
            for room in rooms:
                room_id = room.get("room_id", "")
                canvas_id = room.get("canvas_id", "")
                drawn = "ano" if room["polygon"] is not None and len(room["polygon"]) > 0 else "ne "
                poly = None
                if room["polygon"] is not None:
                    typ = "?"
                    if "type" in room:
                        typ = room["type"]
                        poly = str(len(room["polygon"])) + " (" + typ + ")"
                else:
                    poly = "?"
                fout.write("{:<15} {:<7} {}         {}\n".format(room_id, canvas_id, drawn, poly))
