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

from importers.dxf_entity_type import *
from entities.line import *
from entities.circle import *
from entities.arc import *
from entities.text import *


class DrawingImporter:

    def __init__(self, filename):
        self.filename = filename

        self.commands = {
            "version:": DrawingImporter.process_version,
            "created:": DrawingImporter.process_created,
            "entities:": DrawingImporter.process_entities,
            "L": DrawingImporter.process_line,
            "C": DrawingImporter.process_circle,
            "A": DrawingImporter.process_arc,
            "T": DrawingImporter.process_text
        }

        self.statistic = {
            DxfEntityType.LINE: 0,
            DxfEntityType.CIRCLE: 0,
            DxfEntityType.ARC: 0,
            DxfEntityType.TEXT: 0,
        }
        self.entities = []

    def import_drawing(self):
        '''Import the file and return structure containing all entities.'''
        with open(self.filename) as fin:
            lines = 0
            for line in fin:
                self.parse_line(line)
                lines += 1
        return self.entities, self.statistic, lines

    def parse_line(self, line):
        print(line)
        parts = line.split(" ")
        command = parts[0]
        function = self.commands.get(command, DrawingImporter.process_unknown_command)
        function(self, parts)

