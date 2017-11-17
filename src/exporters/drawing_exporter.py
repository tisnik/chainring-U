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


class DrawingExporter:
    VERSION = 1

    def __init__(self, filename, entities):
        self.filename = filename
        self.entities = entities

    @staticmethod
    def get_timestamp():
        return datetime.now().isoformat(sep=' ')

    @staticmethod
    def output_timestamp(fout):
        fout.write("created: {c}\n".format(c=DrawingExporter.get_timestamp()))

    @staticmethod
    def output_version(fout):
        fout.write("version: {v}\n".format(v=DrawingExporter.VERSION))

    def export(self):
        with open(self.filename, "w") as fout:
            DrawingExporter.output_version(fout)
            DrawingExporter.output_timestamp(fout)
            fout.write("entities: {e}\n".format(e=len(self.entities)))
            for entity in self.entities:
                fout.write(entity.str())
                fout.write("\n")
