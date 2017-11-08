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
from geometry.bounds import Bounds

import sys
import configparser


config = configparser.ConfigParser()
config.read('config.ini')


def computeScale(bounds, canvas):
    canvas_width = canvas.winfo_reqwidth()
    canvas_height = canvas.winfo_reqheight()
    xdist = bounds.xmax - bounds.xmin
    ydist = bounds.ymax - bounds.ymin
    xscale = 0.99 * canvas_width / xdist
    yscale = 0.99 * canvas_height / ydist
    scale = min(xscale, yscale)
    return -bounds.xmin, -bounds.ymin, scale


window_width = config.getint('ui', 'window_width')
window_height = config.getint('ui', 'window_height')
mainWindow = MainWindow(window_width, window_height)

importer = DxfImporter("test-data/Building_1np.dxf")
entities, statistic, lines = importer.import_dxf()
bounds = Bounds.computeBounds(entities)
xoffset, yoffset, scale = computeScale(bounds, mainWindow.canvas)

for entity in entities:
    entity.transform(xoffset, yoffset, scale)

mainWindow.set_entities(entities)
mainWindow.redraw()
mainWindow.show()
