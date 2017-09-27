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

import icons.file_open
import icons.file_save
import icons.file_import

import icons.zoom_in
import icons.zoom_out
import icons.zoom_original

import icons.room_list


class Toolbar(tkinter.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, text="Nástroje", padx=5, pady=5)

        self.file_import_icon = tkinter.PhotoImage(data=icons.file_import.icon)
        self.file_open_icon = tkinter.PhotoImage(data=icons.file_open.icon)
        self.file_save_icon = tkinter.PhotoImage(data=icons.file_save.icon)

        self.zoom_in_icon = tkinter.PhotoImage(data=icons.zoom_in.icon)
        self.zoom_out_icon = tkinter.PhotoImage(data=icons.zoom_out.icon)
        self.zoom_original_icon = tkinter.PhotoImage(data=icons.zoom_original.icon)

        self.room_list_icon = tkinter.PhotoImage(data=icons.room_list.icon)

        button_import = tkinter.Button(self, text="Import", image=self.file_import_icon)
        button_open = tkinter.Button(self, text="Otevřít", image=self.file_open_icon)
        button_save = tkinter.Button(self, text="Uložito", image=self.file_save_icon)

        button_zoom_in = tkinter.Button(self, text="Zvětšit", image=self.zoom_in_icon)
        button_zoom_out = tkinter.Button(self, text="Zmenšit", image=self.zoom_out_icon)
        button_zoom_11 = tkinter.Button(self, text="1:1", image=self.zoom_original_icon)

        button_room_list = tkinter.Button(self, text="Room list", image=self.room_list_icon)

        spacer1 = tkinter.Label(self, text="  ")
        spacer2 = tkinter.Label(self, text="  ")

        button_import.grid(column=1, row=1)
        button_open.grid(column=2, row=1)
        button_save.grid(column=3, row=1)

        spacer1.grid(column=4, row=1)

        button_zoom_in.grid(column=5, row=1)
        button_zoom_out.grid(column=6, row=1)
        button_zoom_11.grid(column=7, row=1)

        spacer2.grid(column=8, row=1)

        button_room_list.grid(column=9, row=1)
