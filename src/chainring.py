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

from gui.main_window import *
from importers.dxf_importer import *
#from importers.binary_importer import *
from importers.drawing_importer import *
#from exporters.binary_exporter import *
from exporters.drawing_exporter import *
from exporters.json_exporter import *
from geometry.bounds import Bounds
from geometry.rescaler import Rescaler
from configuration import *

import sys

configuration = Configuration()
#configuration.write()

mainWindow = MainWindow(configuration)

importer = DrawingImporter("input.drw")
drawing = importer.import_drawing()
#importer = DxfImporter("test-data/Building_1np.dxf")
#drawing = importer.import_dxf()

exporter = DrawingExporter("output.drw", drawing)
exporter.export()

#json_exporter = JSONExporter("output.json", drawing)
#json_exporter.export()

bounds = Bounds.computeBounds(drawing.entities)
print(bounds)
xoffset, yoffset, scale = Rescaler.computeScaleForCanvas(bounds, mainWindow.canvas)
print(xoffset, yoffset, scale)

#ex = BinaryExporter("output3.bin", entities)
#ex.export_binary_drawing()

#with open("output.bin", "wb") as fout:
#    pickle.dump(entities, fout)

drawing.rescale(xoffset, yoffset, scale)

exporter = DrawingExporter("output2.drw", drawing)
exporter.export()

mainWindow.drawing = drawing
mainWindow.redraw()
mainWindow.add_all_rooms_from_drawing()
mainWindow.show()
