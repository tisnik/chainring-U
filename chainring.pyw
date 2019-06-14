#
#  (C) Copyright 2017, 2018, 2019  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

import sys
sys.path.append('src')

from gui.main_window import *
from importers.dxf_importer import *
from importers.drawing_importer import *
from exporters.drawing_exporter import *
from exporters.json_exporter import *
from geometry.bounds import Bounds
from geometry.rescaler import Rescaler
from configuration import *
from gui.dialogs.error_dialogs import *
from gui.dialogs.load_dialogs import LoadDialogs

import sys

configuration = Configuration()

mainWindow = MainWindow(configuration)
drawing = None

if drawing is None:
    drawing_file_name = LoadDialogs.load_drawing(None)
    if drawing_file_name is not None and drawing_file_name != "" and drawing_file_name != ():
        if drawing_file_name.endswith(".drw"):
            importer = DrawingImporter(drawing_file_name)
            drawing = importer.import_drawing()
            if drawing is None:
                error_dialog_drawing_load()
        else:
            importer = DxfImporter(drawing_file_name)
            drawing = importer.import_dxf()
            if drawing is None:
                error_dialog_drawing_load()

if drawing is not None:
    bounds = Bounds.computeBounds(drawing.entities)
    xoffset, yoffset, scale = Rescaler.computeScaleForCanvas(bounds, mainWindow.canvas)

    drawing.rescale(xoffset, yoffset, scale)

mainWindow.drawing = drawing
mainWindow.redraw()
mainWindow.add_all_rooms_from_drawing()
mainWindow.set_ui_items_for_actual_mode()
mainWindow.show()
