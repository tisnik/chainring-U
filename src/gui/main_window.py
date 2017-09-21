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
