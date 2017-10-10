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
from tkinter import ttk

from gui.canvas import *
from gui.toolbar import *
from gui.menubar import *
from gui.palette import *


def test():
    print("Test!")


class MainWindow:

    def __init__(self):
        self.root = tkinter.Tk()

        self.canvas = Canvas(self.root, 800, 600)
        self.toolbar = Toolbar(self.root)
        self.palette = Palette(self.root)

        self.menubar = Menubar(self.root)

        self.root.config(menu=self.menubar)

        self.toolbar.grid(column=1, row=1, columnspan=2, sticky="WE")
        self.palette.grid(column=1, row=2, sticky="NWSE")
        self.canvas.grid(column=2, row=2, sticky="NWSE")

    def show(self):
        self.root.mainloop()

    def draw_entities(self, entities, xoffset, yoffset, scale):
        self.canvas.draw_entities(entities, xoffset, yoffset, scale)
