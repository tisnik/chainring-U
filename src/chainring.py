"""Entry point to the Chainring application."""

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

import sys

from configuration import Configuration

# from exporters.binary_exporter import *
from exporters.drawing_exporter import *
from exporters.json_exporter import *
from geometry.bounds import Bounds
from geometry.rescaler import Rescaler
from gui.dialogs.error_dialogs import (
    error_dialog_drawing_load,
    error_dialog_wrong_configuration,
)
from gui.dialogs.load_dialogs import LoadDialogs
from gui.main_window import *

# from importers.binary_importer import *
from importers.drawing_importer import DrawingImporter
from importers.dxf_importer import DxfImporter

configuration = Configuration()
# configuration.write()
try:
    configuration.check_configuration()
except Exception as e:
    error_dialog_wrong_configuration(str(e))
    sys.exit(1)


main_window = MainWindow(configuration)
drawing = None

# importer = DrawingImporter("input.drw")
# drawing = importer.import_drawing()
# importer = DxfImporter("test-data/Building_1np.dxf")
# importer = DxfImporter("test2.dxf")
# importer = DxfImporter("7701_cad.dxf")
# drawing = importer.import_dxf()

# exporter = DrawingExporter("output.drw", drawing)
# exporter.export()

# json_exporter = JSONExporter("output.json", drawing)
# json_exporter.export()

if drawing is None:
    drawing_file_name = LoadDialogs.load_drawing(None)
    if (
        drawing_file_name is not None
        and drawing_file_name != ""
        and drawing_file_name != ()
    ):
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
    # print(bounds)
    xoffset, yoffset, scale = Rescaler.computeScaleForCanvas(bounds, main_window.canvas)
    # print(xoffset, yoffset, scale)

    # ex = BinaryExporter("output3.bin", entities)
    # ex.export_binary_drawing()

    # with open("output.bin", "wb") as fout:
    #     pickle.dump(entities, fout)

    drawing.rescale(xoffset, yoffset, scale)

    # exporter = DrawingExporter("output2.drw", drawing)
    # exporter.export()

main_window.drawing = drawing
main_window.redraw()
main_window.add_all_rooms_from_drawing()
main_window.set_ui_items_for_actual_mode()
main_window.show()
