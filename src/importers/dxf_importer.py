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

from importers.dxf_reader_state import *
from importers.dxf_entity_type import *
from entities.line import *
from entities.circle import *
from entities.arc import *
from entities.text import *


class DxfImporter():

    def __init__(self, filename):
        self.filename = filename
        self.state_switcher = {
            DxfReaderState.BEGINNING: DxfImporter.process_beginning,
            DxfReaderState.BEGINNING_SECTION: DxfImporter.process_beginning_section,
            DxfReaderState.SECTION_HEADER: DxfImporter.process_section_header,
            DxfReaderState.SECTION_TABLES: DxfImporter.process_section_tables,
            DxfReaderState.SECTION_BLOCKS: DxfImporter.process_section_blocks,
            DxfReaderState.SECTION_ENTITIES: DxfImporter.process_section_entities,
            DxfReaderState.SECTION_OBJECTS: DxfImporter.process_section_objects,
            DxfReaderState.SECTION_BLOCK: DxfImporter.process_section_block,
            DxfReaderState.ENTITY: DxfImporter.process_entity,
        }

    def dxf_entry(self, fin):
        """Generate pair dxf_code + dxf_data for each iteration."""
        while True:
            line1 = fin.readline()
            line2 = fin.readline()
            if not line1 or not line2:
                break
            code = int(line1.strip())
            data = line2.strip()
            yield code, data

    def import_dxf(self):
        self.state = DxfReaderState.BEGINNING
        self.entity_type = DxfEntityType.UNKNOWN
        self.blockName = None
        self.statistic = {
            DxfEntityType.LINE: 0,
            DxfEntityType.CIRCLE: 0,
            DxfEntityType.ARC: 0,
            DxfEntityType.TEXT: 0,
        }
        self.entities = []

        with open(self.filename) as fin:
            lines = 0
            for code, data in self.dxf_entry(fin):
                function = self.state_switcher.get(self.state, lambda self, code, data: "nothing")
                function(self, code, data)
                lines += 1
        print(lines)
        print(self.statistic)

    def process_beginning(self, code, data):
        if code == 0:
            if data == "SECTION":
                self.state = DxfReaderState.BEGINNING_SECTION
                print("section")
            elif data == "EOF":
                self.state = DxfReaderState.EOF
                print("eof")
        elif code == 999:
            print(data)
        else:
            raise Exception("unknown code {c} for state BEGINNING".format(c=code))

    def process_beginning_section(self, code, data):
        if code == 2:
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
                print("    section tables")
            else:
                raise Exception("unknown data {d} for state BEGINNING_SECTION".format(d=data))
        else:
            raise Exception("unknown code {c} for state BEGINNING_SECTION".format(c=code))

    def process_section_header(self, code, data):
        if code == 0:
            if data == "ENDSEC":
                self.state = DxfReaderState.BEGINNING
                print("    end section header")

    def process_section_tables(self, code, data):
        if code == 0:
            if data == "ENDSEC":
                self.state = DxfReaderState.BEGINNING
                print("    end section tables")

    def process_section_blocks(self, code, data):
        if code == 0:
            if data == "BLOCK":
                self.state = DxfReaderState.SECTION_BLOCK
                print("    block")
            elif data == "ENDSEC":
                self.state = DxfReaderState.BEGINNING
                print("    end section blocks")

    def process_section_block(self, code, data):
        if code == 0:
            if data == "ENDBLK":
                print("        end block")
                self.state = DxfReaderState.SECTION_BLOCKS
        elif code == 2:
            self.state = DxfReaderState.SECTION_BLOCK
            self.blockName = data
            print("        begin block '{b}'".format(b=self.blockName))

    def process_section_entities(self, code, data):
        if code == 0:
            if data == "LINE":
                self.state = DxfReaderState.ENTITY
                self.entityType = DxfEntityType.LINE
            elif data == "CIRCLE":
                self.state = DxfReaderState.ENTITY
                self.entityType = DxfEntityType.CIRCLE
            elif data == "ARC":
                self.state = DxfReaderState.ENTITY
                self.entityType = DxfEntityType.ARC
            elif data == "MTEXT" or data == "TEXT":
                self.state = DxfReaderState.ENTITY
                self.entityType = DxfEntityType.TEXT

    def process_section_objects(self, code, data):
        pass


if __name__ == "__main__":
    importer = DxfImporter("Branna_3np.dxf")
    importer.import_dxf()
