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

import tkinter


class Canvas(tkinter.Canvas):

    GRID_SIZE = 50

    def __init__(self, parent, width, height):
        super().__init__(parent, width=width, height=height,
                         background="white")
        self.draw_grid(width, height, Canvas.GRID_SIZE)

    def draw_grid(self, width, height, grid_size):
        for x in range(0, width, grid_size):
            self.create_line(x, 0, x, height, dash=7, fill="gray")
        for y in range(0, height, grid_size):
            self.create_line(0, y, width, y, dash=7, fill="gray")

    def draw_entities(self, entities, xoffset, yoffset, scale):
        for entity in entities:
            entity.draw(self, xoffset, yoffset, scale)
