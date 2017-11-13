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
        # self.draw_grid(width, height, Canvas.GRID_SIZE)
        # self.draw_boundary(width, height)
        self._grid = True
        self._boundary = True
        self.width = width
        self.height = height

    def draw_grid(self):
        for x in range(0, self.width, Canvas.GRID_SIZE):
            self.create_line(x, 0, x, self.height, dash=7, tags="grid")
        for y in range(0, self.height, Canvas.GRID_SIZE):
            self.create_line(0, y, self.width, y, dash=7, tags="grid")
        if self._grid:
            self.show_grid()
        else:
            self.hide_grid()

    def draw_boundary(self):
        self.create_line(0, 0,
                         self.width, 0,
                         self.width, self.height,
                         0, self.height,
                         0, 0,
                         tags="boundary")
        if self._boundary:
            self.show_boundary()
        else:
            self.hide_boundary()

    def show_grid(self):
        self.itemconfig("grid", fill="blue")

    def hide_grid(self):
        self.itemconfig("grid", fill="")

    def toggle_grid(self):
        self._grid = not self._grid
        if self._grid:
            self.show_grid()
        else:
            self.hide_grid()

    def show_boundary(self):
        self.itemconfig("boundary", fill="red", width=2)

    def hide_boundary(self):
        self.itemconfig("boundary", fill="", width=2)

    def toggle_boundary(self):
        self._boundary = not self._boundary
        if self._boundary:
            self.show_boundary()
        else:
            self.hide_boundary()

    def draw_entities(self, entities, xoffset, yoffset, scale):
        for entity in entities:
            entity.draw(self, xoffset, yoffset, scale)
