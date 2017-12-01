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
from drawing import Drawing
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
        self.metadata = {}
        self.entities = []

    def import_drawing(self):
        '''Import the file and return structure containing all entities.'''
        with open(self.filename) as fin:
            lines = 0
            for line in fin:
                self.parse_line(line)
                lines += 1
        drawing = Drawing(self.entities, self.statistic, lines)
        return drawing

    def parse_line(self, line):
        parts = line.split(" ")
        command = parts[0]
        function = self.commands.get(command,
                                     DrawingImporter.process_unknown_command)
        function(self, parts)

    def process_unknown_command(self, parts):
        print("Unknown command: '{c}'".format(c=parts[0]))
        sys.exit(0)

    def process_version(self, parts):
        print("Read attribute 'version': {v}".format(v=parts[1]))

    def process_created(self, parts):
        print("Read attribute 'created': {c}".format(c=parts[1]))

    def process_entities(self, parts):
        print("Read attribute 'entities': {e}".format(e=parts[1]))

    def process_line(self, parts):
        x1 = float(parts[1])
        y1 = float(parts[2])
        x2 = float(parts[3])
        y2 = float(parts[4])
        self.entities.append(Line(x1, y1, x2, y2))

    def process_circle(self, parts):
        x = float(parts[1])
        y = float(parts[2])
        radius = float(parts[3])
        self.entities.append(Circle(x, y, radius))

    def process_arc(self, parts):
        x = float(parts[1])
        y = float(parts[2])
        radius = float(parts[3])
        angle1 = float(parts[4])
        angle2 = float(parts[5])
        self.entities.append(Arc(x, y, radius, angle1, angle2))

    def process_text(self, parts):
        x = float(parts[1])
        y = float(parts[2])
        text = " ".join(parts[3:]).strip()
        self.entities.append(Text(x, y, text))
