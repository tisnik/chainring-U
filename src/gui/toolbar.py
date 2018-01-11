#
#  (C) Copyright 2017, 2018  Pavel Tisnovsky
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

from gui.settings_dialog import SettingsDialog
from gui.drawing_info_dialog import DrawingInfoDialog


class Toolbar(tkinter.LabelFrame):
    def __init__(self, parent, main_window, canvas):
        super().__init__(parent, text="Nástroje", padx=5, pady=5)

        self.parent = parent
        self.main_window = main_window

        button_import = tkinter.Button(
            self, text="Import",
            image=main_window.icons.file_import_icon)

        button_open = tkinter.Button(
            self, text="Otevřít",
            image=main_window.icons.file_open_icon,
            command=main_window.open_drawing_command)

        button_save = tkinter.Button(
            self, text="Uložit",
            image=main_window.icons.file_save_icon,
            command=main_window.save_drawing_command)

        button_save_as = tkinter.Button(
            self, text="Uložit výkres pod jiným jménem",
            image=main_window.icons.file_save_as_icon,
            command=main_window.save_drawing_as_command)

        button_quit = tkinter.Button(
            self, text="Ukončit",
            image=main_window.icons.exit_icon,
            command=main_window.quit)

        button_zoom_in = tkinter.Button(
            self, text="Zvětšit",
            image=main_window.icons.zoom_in_icon,
            command=main_window.zoom_plus)

        button_zoom_out = tkinter.Button(
            self, text="Zmenšit",
            image=main_window.icons.zoom_out_icon,
            command=main_window.zoom_minus)

        button_zoom_11 = tkinter.Button(
            self, text="1:1",
            image=main_window.icons.zoom_original_icon,
            command=main_window.redraw)

        button_view_grid = tkinter.Button(
            self, text="Mřížka",
            image=main_window.icons.view_grid_icon,
            command=canvas.toggle_grid)

        button_view_boundary = tkinter.Button(
            self, text="Okraj",
            image=main_window.icons.view_boundary_icon,
            command=canvas.toggle_boundary)

        button_drawing_info = tkinter.Button(
            self, text="Informace o výkresu",
            image=main_window.icons.drawing_info_icon,
            command=self.show_drawing_info_dialog)

        button_room_list = tkinter.Button(
            self, text="Seznam místností",
            image=main_window.icons.room_list_icon)

        button_new_room = tkinter.Button(
            self, text="Nakreslit místnost",
            image=main_window.icons.edit_icon,
            command=self.main_window.draw_new_room_command)

        button_settings = tkinter.Button(
            self, text="Nastavení",
            image=main_window.icons.properties_icon,
            command=self.show_settings_dialog)

        spacer1 = tkinter.Label(self, text="   ")
        spacer2 = tkinter.Label(self, text="   ")
        spacer3 = tkinter.Label(self, text="   ")

        button_import.grid(column=1, row=1)
        button_open.grid(column=2, row=1)
        button_save.grid(column=3, row=1)
        button_save_as.grid(column=4, row=1)
        button_quit.grid(column=5, row=1)

        spacer1.grid(column=6, row=1)

        button_zoom_in.grid(column=7, row=1)
        button_zoom_out.grid(column=8, row=1)
        button_zoom_11.grid(column=9, row=1)
        button_view_grid.grid(column=10, row=1)
        button_view_boundary.grid(column=11, row=1)

        spacer2.grid(column=12, row=1)

        button_drawing_info.grid(column=13, row=1)
        button_room_list.grid(column=14, row=1)
        button_settings.grid(column=15, row=1)

        spacer3.grid(column=16, row=1)

        button_new_room.grid(column=17, row=1)

    def show_settings_dialog(self):
        SettingsDialog(self.parent)

    def show_drawing_info_dialog(self):
        DrawingInfoDialog(self.parent, self.main_window.drawing.statistic)
