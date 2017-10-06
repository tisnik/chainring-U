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


class Palette(tkinter.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, text="Výkres", padx=5, pady=5)
        button = tkinter.Button(self, text="Test")
        button.grid(column=1, row=1)
        listbox = tkinter.Listbox(self)
        listbox.grid(column=1, row=2, sticky="NWSE")
