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

from gui.icons import *


class MainWindow:

    SCALE_UP_FACTOR = 1.1
    SCALE_DOWN_FACTOR = 0.9

    def __init__(self, window_width, window_height):
        self._drawing = None
        self.root = tkinter.Tk()

        self.icons = Icons()
        self.room_draw_mode = False

        self.canvas = Canvas(self.root, window_width, window_height)
        self.toolbar = Toolbar(self.root, self, self.canvas)
        self.palette = Palette(self.root)

        self.menubar = Menubar(self.root, self, self.canvas)

        self.root.config(menu=self.menubar)

        self.toolbar.grid(column=1, row=1, columnspan=2, sticky="WE")
        self.palette.grid(column=1, row=2, sticky="NWSE")
        self.canvas.grid(column=2, row=2, sticky="NWSE")

        self.canvas.bind("<ButtonPress-1>", self.on_left_button_pressed)
        self.canvas.bind("<B1-Motion>", self.on_left_button_drag)
        # scroll on Linux
        self.canvas.bind("<Button-4>", self.zoom_plus)
        self.canvas.bind("<Button-5>", self.zoom_minus)
        # scroll on windows
        self.canvas.bind("<MouseWheel>", self.zoom)

    def scroll_start(self, event):
        self.canvas.scan_mark(event.x, event.y)

    def scroll_move(self, event):
        self.canvas.scan_dragto(event.x, event.y, gain=1)
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def on_left_button_pressed(self, event):
        # get the coordinates before canvas scroll
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)
        print(event.x, event.y, x, y)
        item = self.canvas.find_closest(x, y)[0]
        print(self.canvas.type(item))
        print(self.canvas.gettags(item))
        self.canvas.itemconfig(item, fill='red')
        if self.room_draw_mode:
            pass
        else:
            self.scroll_start(event)

    def on_left_button_drag(self, event):
        if self.room_draw_mode:
            pass
        else:
            self.scroll_move(event)

    # zoom on Windows
    def zoom(self, event):
        if event.delta > 0:
            self.canvas.scale("all", event.x, event.y, 1.1, 1.1)
        elif event.delta < 0:
            self.canvas.scale("all", event.x, event.y, 0.9, 0.9)
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    # zoom on Linux
    def zoom_plus(self, event=None):
        if event:
            self.canvas.scale("all", event.x, event.y,
                              MainWindow.SCALE_UP_FACTOR,
                              MainWindow.SCALE_UP_FACTOR)
        else:
            self.canvas.scale("all", self.canvas.width/2, self.canvas.height/2,
                              MainWindow.SCALE_UP_FACTOR,
                              MainWindow.SCALE_UP_FACTOR)
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    # zoom on Linux
    def zoom_minus(self, event=None):
        if event:
            self.canvas.scale("all", event.x, event.y,
                              MainWindow.SCALE_DOWN_FACTOR,
                              MainWindow.SCALE_DOWN_FACTOR)
        else:
            self.canvas.scale("all", self.canvas.width/2, self.canvas.height/2,
                              MainWindow.SCALE_DOWN_FACTOR,
                              MainWindow.SCALE_DOWN_FACTOR)
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def quit(self):
        answer = messagebox.askyesno("Skutečně ukončit program?",
                                     "Skutečně ukončit program?")
        if answer:
            self.root.quit()

    def show(self):
        self.root.mainloop()

    @property
    def drawing(self):
        return self._drawing

    @drawing.setter
    def drawing(self, drawing):
        self._drawing = drawing

    def redraw(self):
        self.canvas.delete("all")
        self.canvas.draw_grid()
        self.canvas.draw_boundary()
        self.canvas.draw_entities(self.drawing.entities, 0, 0, 1)
