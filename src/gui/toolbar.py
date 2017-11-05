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
import icons.view_grid
import icons.view_boundary

import icons.room_list
import icons.image


class Toolbar(tkinter.LabelFrame):
    def __init__(self, parent, main_window, canvas):
        super().__init__(parent, text="Nástroje", padx=5, pady=5)

        self.file_import_icon = tkinter.PhotoImage(data=icons.file_import.icon)
        self.file_open_icon = tkinter.PhotoImage(data=icons.file_open.icon)
        self.file_save_icon = tkinter.PhotoImage(data=icons.file_save.icon)
        self.application_exit_icon = tkinter.PhotoImage(data=icons.application_exit.icon)

        self.zoom_in_icon = tkinter.PhotoImage(data=icons.zoom_in.icon)
        self.zoom_out_icon = tkinter.PhotoImage(data=icons.zoom_out.icon)
        self.zoom_original_icon = tkinter.PhotoImage(data=icons.zoom_original.icon)
        self.view_grid_icon = tkinter.PhotoImage(data=icons.view_grid.icon)
        self.view_boundary_icon = tkinter.PhotoImage(data=icons.view_boundary.icon)

        self.room_list_icon = tkinter.PhotoImage(data=icons.room_list.icon)
        self.image_icon = tkinter.PhotoImage(data=icons.image.icon)

        button_import = tkinter.Button(self, text="Import", image=self.file_import_icon)
        button_open = tkinter.Button(self, text="Otevřít", image=self.file_open_icon)
        button_save = tkinter.Button(self, text="Uložit", image=self.file_save_icon)
        button_quit = tkinter.Button(self, text="Ukončit", image=self.application_exit_icon, command=main_window.quit)

        button_zoom_in = tkinter.Button(self, text="Zvětšit", image=self.zoom_in_icon, command=main_window.zoom_plus)
        button_zoom_out = tkinter.Button(self, text="Zmenšit", image=self.zoom_out_icon, command=main_window.zoom_minus)
        button_zoom_11 = tkinter.Button(self, text="1:1", image=self.zoom_original_icon, command=main_window.redraw)

        button_view_grid = tkinter.Button(self, text="Mřížka", image=self.view_grid_icon, command=canvas.toggle_grid)
        button_view_boundary = tkinter.Button(self, text="Okraj", image=self.view_boundary_icon, command=canvas.toggle_boundary)

        button_room_list = tkinter.Button(self, text="Room list", image=self.room_list_icon)
        button_new_room = tkinter.Button(self, text="New room", image=self.image_icon)

        spacer1 = tkinter.Label(self, text="  ")
        spacer2 = tkinter.Label(self, text="  ")
        spacer3 = tkinter.Label(self, text="  ")

        button_import.grid(column=1, row=1)
        button_open.grid(column=2, row=1)
        button_save.grid(column=3, row=1)
        button_quit.grid(column=4, row=1)

        spacer1.grid(column=5, row=1)

        button_zoom_in.grid(column=6, row=1)
        button_zoom_out.grid(column=7, row=1)
        button_zoom_11.grid(column=8, row=1)
        button_view_grid.grid(column=9, row=1)
        button_view_boundary.grid(column=10, row=1)

        spacer2.grid(column=11, row=1)

        button_room_list.grid(column=12, row=1)

        spacer3.grid(column=13, row=1)

        button_new_room.grid(column=14, row=1)
