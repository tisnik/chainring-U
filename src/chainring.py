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

from gui.main_window import *
from importers.dxf_importer import *
#from importers.binary_importer import *
from importers.drawing_importer import *
#from exporters.binary_exporter import *
from exporters.drawing_exporter import *
from geometry.bounds import Bounds
from geometry.rescaler import Rescaler

import sys
import configparser


config = configparser.ConfigParser()
config.read('config.ini')

window_width = config.getint('ui', 'window_width')
window_height = config.getint('ui', 'window_height')
mainWindow = MainWindow(window_width, window_height)

importer = DrawingImporter("output.drw")
drawing = importer.import_drawing()
#importer = DxfImporter("test-data/Building_1np.dxf")
#drawing = importer.import_dxf()

exporter = DrawingExporter("output2.drw", drawing)
exporter.export()

bounds = Bounds.computeBounds(drawing.entities)
xoffset, yoffset, scale = Rescaler.computeScale(bounds, mainWindow.canvas)

#ex = BinaryExporter("output3.bin", entities)
#ex.export_binary_drawing()

#with open("output.bin", "wb") as fout:
#    pickle.dump(entities, fout)

drawing.rescale(xoffset, yoffset, scale)

mainWindow.drawing = drawing
mainWindow.redraw()
mainWindow.show()
