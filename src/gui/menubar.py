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

from gui.about_dialog import *
from gui.help_dialog import *
from gui.settings_dialog import SettingsDialog
from gui.drawing_info_dialog import DrawingInfoDialog


class Menubar(tkinter.Menu):

    def __init__(self, parent, main_window, canvas):
        super().__init__(tearoff=0)

        self.parent = parent
        self.main_window = main_window

        filemenu = tkinter.Menu(self, tearoff=0)
        filemenu.add_command(label="Otevřít výkres",
                             image=main_window.icons.file_open_icon,
                             compound="left", underline=0)

        filemenu.add_command(label="Uložit výkres",
                             image=main_window.icons.file_save_icon,
                             compound="left", underline=0,
                             command=main_window.save_drawing_command)

        filemenu.add_command(label="Uložit výkres pod jiným jménem",
                             image=main_window.icons.file_save_as_icon,
                             compound="left", underline=0,
                             command=main_window.save_drawing_as_command)

        filemenu.add_separator()
        filemenu.add_command(label="Importovat nový výkres",
                             image=main_window.icons.file_import_icon,
                             compound="left", underline=0)
        filemenu.add_separator()
        filemenu.add_command(label="Konec", image=main_window.icons.exit_icon,
                             compound="left", underline=0,
                             command=parent.quit)

        edit = tkinter.Menu(self, tearoff=0)
        edit.add_command(label="Nakreslit místnost",
                         image=main_window.icons.edit_icon,
                         compound="left", underline=0,
                         command=self.main_window.draw_new_room_command)

        view = tkinter.Menu(self, tearoff=0)
        view.add_command(label="Zvětšit",
                         image=main_window.icons.zoom_in_icon,
                         compound="left", underline=1,
                         command=main_window.zoom_plus)
        view.add_command(label="Zmenšit",
                         image=main_window.icons.zoom_out_icon,
                         compound="left", underline=1,
                         command=main_window.zoom_minus)
        view.add_command(label="1:1",
                         image=main_window.icons.zoom_original_icon,
                         compound="left", underline=0,
                         command=main_window.redraw)
        view.add_separator()
        view.add_command(label="Mřížka",
                         image=main_window.icons.view_grid_icon,
                         compound="left", underline=0,
                         command=canvas.toggle_grid)
        view.add_command(label="Okraj výkresu",
                         image=main_window.icons.view_boundary_icon,
                         compound="left", underline=0,
                         command=canvas.toggle_boundary)

        tools = tkinter.Menu(self, tearoff=0)

        tools.add_command(label="Informace o výkresu",
                          image=main_window.icons.drawing_info,
                          compound="left", underline=0,
                          command=self.show_drawing_info_dialog)

        tools.add_command(label="Seznam místností",
                          image=main_window.icons.room_list_icon,
                          compound="left", underline=0)
        tools.add_separator()
        tools.add_command(label="Nastavení",
                          image=main_window.icons.properties_icon,
                          compound="left", underline=0,
                          command=self.show_settings_dialog)

        helpmenu = tkinter.Menu(self, tearoff=0)
        helpmenu.add_command(label="Nápověda",
                             image=main_window.icons.help_faq_icon,
                             compound="left", underline=0,
                             command=help)
        helpmenu.add_command(label="O programu",
                             image=main_window.icons.help_about_icon,
                             compound="left", underline=0, command=about)

        self.add_cascade(label="Soubor", menu=filemenu, underline=0)
        self.add_cascade(label="Upravit", menu=edit, underline=0)
        self.add_cascade(label="Zobrazit", menu=view, underline=0)
        self.add_cascade(label="Nástroje", menu=tools, underline=3)
        self.add_cascade(label="Nápověda", menu=helpmenu, underline=0)

    def show_settings_dialog(self):
        SettingsDialog(self.parent)

    def show_drawing_info_dialog(self):
        DrawingInfoDialog(self.parent, self.main_window.drawing.statistic)
