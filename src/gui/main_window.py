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

        self.canvas = Canvas(self.root, 1000, 700)
        self.toolbar = Toolbar(self.root, self, self.canvas)
        self.palette = Palette(self.root)

        self.menubar = Menubar(self.root, self, self.canvas)

        self.root.config(menu=self.menubar)

        self.toolbar.grid(column=1, row=1, columnspan=2, sticky="WE")
        self.palette.grid(column=1, row=2, sticky="NWSE")
        self.canvas.grid(column=2, row=2, sticky="NWSE")

        self.canvas.bind("<ButtonPress-1>", self.scroll_start)
        self.canvas.bind("<B1-Motion>", self.scroll_move)
        # scroll on Linux
        self.canvas.bind("<Button-4>", self.zoom_plus)
        self.canvas.bind("<Button-5>", self.zoom_minus)
        # scroll on windows
        self.canvas.bind("<MouseWheel>",self.zoom)

    def quit(self):
        answer = messagebox.askyesno("Skutečně ukončit program?",
                                     "Skutečně ukončit program?")
        if answer:
            self.root.quit()

    def show(self):
        self.root.mainloop()

    def set_entities(self, entities):
        self.entities = entities

    def redraw(self):
        self.canvas.delete("all")
        self.canvas.draw_grid()
        self.canvas.draw_boundary()
        self.canvas.draw_entities(self.entities, 0, 0, 1)
