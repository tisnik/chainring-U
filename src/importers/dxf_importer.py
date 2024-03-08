"""Importer for drawings stored in a DXF format."""

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

from drawing import Drawing
from entities.arc import Arc
from entities.circle import Circle
from entities.drawing_entity_type import DrawingEntityType
from entities.line import Line
from entities.polyline import Polyline
from entities.text import Text
from importers.dxf_codes import DxfCodes
from importers.dxf_reader_state import DxfReaderState


class DxfImporter:
    """Importer for drawings stored in a DXF format."""

    def __init__(self, filename):
        """Initialize the importer."""
        # TODO: make this option fully configurable
        self.debug = False
        self.filename = filename
        self.state_switcher = {
            DxfReaderState.BEGINNING:
                DxfImporter.process_beginning,
            DxfReaderState.BEGINNING_SECTION:
                DxfImporter.process_beginning_section,
            DxfReaderState.SECTION_HEADER:
                DxfImporter.process_section_header,
            DxfReaderState.SECTION_TABLES:
                DxfImporter.process_section_tables,
            DxfReaderState.SECTION_BLOCKS:
                DxfImporter.process_section_blocks,
            DxfReaderState.SECTION_ENTITIES:
                DxfImporter.process_section_entities,
            DxfReaderState.SECTION_OBJECTS:
                DxfImporter.process_section_objects,
            DxfReaderState.SECTION_CLASSES:
                DxfImporter.process_section_classes,
            DxfReaderState.SECTION_BLOCK:
                DxfImporter.process_section_block,
            DxfReaderState.ENTITY:
                DxfImporter.process_entity,
        }
        self.color = 0

    def dxf_entry(self, fin):
        """Generate pair dxf_code + dxf_data for each iteration."""
        linenumber = 0
        while True:
            line1 = None
            line2 = None
            linenumber += 1
            line1 = fin.readline()
            try:
                linenumber += 1
                line2 = fin.readline()
            except Exception as e:
                print("Error on line: {line}".format(line=linenumber))
                line2 = ""
            if not line1 or not line2:
                break
            code = int(line1.strip())
            data = line2.strip()
            yield code, data

    def init_import(self):
        """Initialize the object state before import."""
        self.state = DxfReaderState.BEGINNING
        self.entity_type = DrawingEntityType.UNKNOWN
        self.blockName = None
        self.statistic = {
            DrawingEntityType.UNKNOWN: 0,
            DrawingEntityType.LINE: 0,
            DrawingEntityType.CIRCLE: 0,
            DrawingEntityType.ARC: 0,
            DrawingEntityType.TEXT: 0,
            DrawingEntityType.POLYLINE: 0,
            DrawingEntityType.ATTRIB: 0
        }
        self.entities = []

    def detect_encoding(self):
        """Detect the encoding of DXF file."""
        encodings = ['utf-8', 'windows-1250', 'windows-1252']
        for e in encodings:
            try:
                with open(self.filename, 'r', encoding=e) as fin:
                    fin.readlines()
                    fin.seek(0)
            except UnicodeDecodeError as e:
                # ok, we expect some errors ;)
                pass
            else:
                print("Encoding: {e}".format(e=e))
                return e

    def import_dxf(self):
        """Import the DXF file and return structure containing all entities."""
        self.init_import()

        encoding = self.detect_encoding()

        with open(self.filename, encoding=encoding) as fin:
            lines = 0
            for code, data in self.dxf_entry(fin):
                function = self.state_switcher.get(self.state, lambda self,
                                                   code, data: "nothing")
                function(self, code, data)
                lines += 1
        # print(lines)
        # print(self.statistic)
        drawing = Drawing(self.entities, self.statistic, lines)
        return drawing

    def process_beginning(self, code, data):
        """Part of the DXF import state machine."""
        if code == DxfCodes.TEXT_STRING:
            if data == "SECTION":
                self.state = DxfReaderState.BEGINNING_SECTION
                print("section")
            elif data == "EOF":
                self.state = DxfReaderState.EOF
                print("eof")
        elif code == DxfCodes.COMMENT:
            print(data)
        else:
            raise Exception("unknown code {c} for state "
                            "BEGINNING".format(c=code))

    def process_beginning_section_name_attribute(self, code, data):
        """Change the state of DXF reader."""
        if data == "HEADER":
            self.state = DxfReaderState.SECTION_HEADER
            print("    section header")
        elif data == "TABLES":
            self.state = DxfReaderState.SECTION_TABLES
            print("    section tables")
        elif data == "BLOCKS":
            self.state = DxfReaderState.SECTION_BLOCKS
            print("    section blocks")
        elif data == "ENTITIES":
            self.state = DxfReaderState.SECTION_ENTITIES
            print("    section entities")
        elif data == "OBJECTS":
            self.state = DxfReaderState.SECTION_OBJECTS
            print("    section objects")
        elif data == "CLASSES":
            self.state = DxfReaderState.SECTION_CLASSES
            print("    section classes")
        else:
            raise Exception("unknown data {d} for state "
                            "BEGINNING_SECTION".format(d=data))

    def process_beginning_section(self, code, data):
        """Part of the DXF import state machine."""
        if code == DxfCodes.NAME:
            self.process_beginning_section_name_attribute(code, data)
        else:
            raise Exception("unknown code {c} for state "
                            "BEGINNING_SECTION".format(c=code))

    def process_section_header(self, code, data):
        """Part of the DXF import state machine."""
        if code == DxfCodes.TEXT_STRING:
            if data == "ENDSEC":
                self.state = DxfReaderState.BEGINNING
                print("    end section header")

    def process_section_tables(self, code, data):
        """Part of the DXF import state machine."""
        if code == DxfCodes.TEXT_STRING:
            if data == "ENDSEC":
                self.state = DxfReaderState.BEGINNING
                print("    end section tables")

    def process_section_blocks(self, code, data):
        """Part of the DXF import state machine."""
        if code == DxfCodes.TEXT_STRING:
            if data == "BLOCK":
                self.state = DxfReaderState.SECTION_BLOCK
                if self.debug:
                    print("    block")
            elif data == "ENDSEC":
                self.state = DxfReaderState.BEGINNING
                print("    end section blocks")

    def process_section_block(self, code, data):
        """Part of the DXF import state machine."""
        if code == DxfCodes.TEXT_STRING:
            if data == "ENDBLK":
                # print("        end block")
                self.state = DxfReaderState.SECTION_BLOCKS
        elif code == DxfCodes.NAME:
            self.state = DxfReaderState.SECTION_BLOCK
            self.blockName = data
            if self.debug:
                print("        begin block '{b}'".format(b=self.blockName))

    def process_section_entities_entity_type(self, code, data):
        """Change the state according to entity type code read from DXF."""
        self.polyline_points_x = []
        self.polyline_points_y = []
        if self.debug:
            print("Entity", data)
        if data == "LINE":
            self.state = DxfReaderState.ENTITY
            self.entityType = DrawingEntityType.LINE
        elif data == "CIRCLE":
            self.state = DxfReaderState.ENTITY
            self.entityType = DrawingEntityType.CIRCLE
        elif data == "ARC":
            self.state = DxfReaderState.ENTITY
            self.entityType = DrawingEntityType.ARC
        elif data == "LWPOLYLINE":
            self.state = DxfReaderState.ENTITY
            self.entityType = DrawingEntityType.POLYLINE
        elif data == "MTEXT" or data == "TEXT":
            self.state = DxfReaderState.ENTITY
            self.entityType = DrawingEntityType.TEXT
        elif data == "ATTRIB":
            self.state = DxfReaderState.ENTITY
            self.entityType = DrawingEntityType.ATTRIB

    def process_section_entities(self, code, data):
        """Part of the DXF import state machine."""
        if code == DxfCodes.TEXT_STRING:
            self.process_section_entities_entity_type(code, data)

    def process_section_objects(self, code, data):
        """Part of the DXF import state machine."""
        if code == DxfCodes.TEXT_STRING:
            if data == "ENDSEC":
                print("    end section objects")

    def process_section_classes(self, code, data):
        """Part of the DXF import state machine."""
        if code == DxfCodes.TEXT_STRING:
            if data == "ENDSEC":
                print("    end section classes")
                self.state = DxfReaderState.BEGINNING

    def process_entity_type_attribute(self, code, data):
        """Store the previously read entity and try to process next one."""
        self.statistic[self.entityType] += 1
        self.store_entity()
        self.state = DxfReaderState.SECTION_ENTITIES
        self.entityType = DrawingEntityType.UNKNOWN
        self.layer = None
        self.color = 0
        self.polyline_points_x = []
        self.polyline_points_y = []
        self.mirror = 1
        if data == "LINE":
            self.state = DxfReaderState.ENTITY
            self.entityType = DrawingEntityType.LINE
        elif data == "CIRCLE":
            self.state = DxfReaderState.ENTITY
            self.entityType = DrawingEntityType.CIRCLE
        elif data == "ARC":
            self.state = DxfReaderState.ENTITY
            self.entityType = DrawingEntityType.ARC
        elif data == "LWPOLYLINE":
            self.state = DxfReaderState.ENTITY
            self.entityType = DrawingEntityType.POLYLINE
        elif data == "MTEXT" or data == "TEXT":
            self.state = DxfReaderState.ENTITY
            self.entityType = DrawingEntityType.TEXT
        elif data == "ATTRIB":
            self.state = DxfReaderState.ENTITY
            self.entityType = DrawingEntityType.ATTRIB
        elif data == "ENDSEC":
            self.state = DxfReaderState.BEGINNING
            self.entityType = DrawingEntityType.UNKNOWN
            print("    end entities")

    def process_entity(self, code, data):
        """Part of the DXF import state machine."""
        if code == DxfCodes.LAYER_NAME:
            self.layer = data.replace(" ", "_")
        elif code == DxfCodes.X1:
            self.x1 = float(data)
            if self.entityType == DrawingEntityType.POLYLINE:
                self.polyline_points_x.append(self.x1)
        elif code == DxfCodes.Y1:
            self.y1 = float(data)
            if self.entityType == DrawingEntityType.POLYLINE:
                self.polyline_points_y.append(self.y1)
        elif code == DxfCodes.X2:
            self.x2 = float(data)
        elif code == DxfCodes.Y2:
            self.y2 = float(data)
        elif code == DxfCodes.RADIUS:
            self.radius = float(data)
        elif code == DxfCodes.ANGLE1:
            self.angle1 = float(data)
        elif code == DxfCodes.ANGLE2:
            self.angle2 = float(data)
        elif code == DxfCodes.COLOR:
            self.color = int(data)
        elif code == DxfCodes.PRIMARY_TEXT:
            self.text = data
        elif code == DxfCodes.MIRROR:
            self.mirror = int(float(data))
        elif code == DxfCodes.TEXT_STRING:
            self.process_entity_type_attribute(code, data)

    def store_entity(self):
        """Store entity read from DXF file."""
        if self.entityType == DrawingEntityType.LINE:
            self.store_line()
        elif self.entityType == DrawingEntityType.CIRCLE:
            self.store_circle()
        elif self.entityType == DrawingEntityType.ARC:
            self.store_arc()
        elif self.entityType == DrawingEntityType.POLYLINE:
            self.store_polyline()
        elif self.entityType == DrawingEntityType.TEXT:
            self.store_text()
        elif self.entityType == DrawingEntityType.ATTRIB:
            # TODO: make this layer(s) configurable
            if self.layer == "CKPOPISM":
                self.store_text()
        else:
            print("unknown entity?")

    def store_line(self):
        """Store line read from DXF file."""
        self.entities.append(Line(self.x1, -self.y1, self.x2, -self.y2, self.color, self.layer))

    def store_polyline(self):
        """Store polyline read from DXF file."""
        for i in range(0, len(self.polyline_points_y)):
            self.polyline_points_y[i] = -self.polyline_points_y[i]
        self.entities.append(Polyline(self.polyline_points_x, self.polyline_points_y,
                                      self.color, self.layer))
        self.polyline_points_x = []
        self.polyline_points_y = []

    def store_circle(self):
        """Store circle read from DXF file."""
        if self.mirror == -1:
            print("MIRROR")
            self.x1 = -self.x1
        self.entities.append(Circle(self.x1, -self.y1, self.radius, self.color, self.layer))

    def store_arc(self):
        """Store arc read from DXF file."""
        self.entities.append(Arc(self.x1, -self.y1,
                                 self.radius, self.angle1, self.angle2, self.color, self.layer))

    def store_text(self):
        """Store text read from DXF file."""
        if self.text:
            self.text = self.text.replace("\\U+00B2", u"\u00B2")
        self.entities.append(Text(self.x1, -self.y1, self.text, self.color, self.layer))


if __name__ == "__main__":
    from exporters.drawing_exporter import DrawingExporter
    importer = DxfImporter("Branna_3np.dxf")
    entities, statistic, lines = importer.import_dxf()
    print(lines)
    print(statistic)
    exporter = DrawingExporter("Branna_3np.drawing", entities)
    exporter.export()
