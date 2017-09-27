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
