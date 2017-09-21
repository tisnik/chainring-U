#!/usr/bin/env python

import tkinter
from tkinter import ttk

from canvas import *
from toolbar import *
from menubar import *


def test():
    print("Test!")


root = tkinter.Tk()

canvas = Canvas(root, 800, 600)

menubar = Menubar(root)

root.config(menu=menubar)

toolbar = Toolbar(root)

toolbar.grid(column=1, row=1, columnspan=2, sticky="WE")
canvas.grid(column=2, row=2, sticky="NWSE")

root.mainloop()
