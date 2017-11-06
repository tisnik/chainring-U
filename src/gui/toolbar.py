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


class Toolbar(tkinter.LabelFrame):
    def __init__(self, parent, main_window, canvas):
        super().__init__(parent, text="Nástroje", padx=5, pady=5)

        button_import = tkinter.Button(self, text="Import", image=main_window.icons.file_import_icon)
        button_open = tkinter.Button(self, text="Otevřít", image=main_window.icons.file_open_icon)
        button_save = tkinter.Button(self, text="Uložit", image=main_window.icons.file_save_icon)
        button_quit = tkinter.Button(self, text="Ukončit", image=main_window.icons.exit_icon, command=main_window.quit)

        button_zoom_in = tkinter.Button(self, text="Zvětšit", image=main_window.icons.zoom_in_icon, command=main_window.zoom_plus)
        button_zoom_out = tkinter.Button(self, text="Zmenšit", image=main_window.icons.zoom_out_icon, command=main_window.zoom_minus)
        button_zoom_11 = tkinter.Button(self, text="1:1", image=main_window.icons.zoom_original_icon, command=main_window.redraw)

        button_view_grid = tkinter.Button(self, text="Mřížka", image=main_window.icons.view_grid_icon, command=canvas.toggle_grid)
        button_view_boundary = tkinter.Button(self, text="Okraj", image=main_window.icons.view_boundary_icon, command=canvas.toggle_boundary)

        button_room_list = tkinter.Button(self, text="Seznam místností", image=main_window.icons.room_list_icon)
        button_new_room = tkinter.Button(self, text="Nakreslit místnost", image=main_window.icons.edit_icon)

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
