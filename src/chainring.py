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
from entities.bounds import Bounds

import sys


def computeBounds(entities):
    bounds = Bounds()
    for entity in entities:
        bounds.enlarge(entity.getBounds())
    print(bounds)


importer = DxfImporter("test-data/Building_1np.dxf")
entities, statistic, lines = importer.import_dxf()
bounds = computeBounds(entities)

mainWindow = MainWindow()
mainWindow.draw_entities(entities, -96817, 39874, 1/50.0)
mainWindow.show()
