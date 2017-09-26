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

import icons.zoom_in
import icons.zoom_out
import icons.zoom_original


class Toolbar(tkinter.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, text="Nástroje", padx=5, pady=5)

        self.zoom_in_icon = tkinter.PhotoImage(data=icons.zoom_in.icon)
        self.zoom_out_icon = tkinter.PhotoImage(data=icons.zoom_out.icon)
        self.zoom_original_icon = tkinter.PhotoImage(data=icons.zoom_original.icon)

        b1 = tkinter.Button(self, text="Zvětšit", image=self.zoom_in_icon)
        b2 = tkinter.Button(self, text="Zmenšit", image=self.zoom_out_icon)
        b3 = tkinter.Button(self, text="1:1", image=self.zoom_original_icon)

        b1.grid(column=1, row=1)
        b2.grid(column=2, row=1)
        b3.grid(column=3, row=1)
