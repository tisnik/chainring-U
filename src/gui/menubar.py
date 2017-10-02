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

import icons.application_exit
import icons.file_open
import icons.file_save
import icons.file_import
import icons.zoom_in
import icons.zoom_out
import icons.zoom_original
import icons.help_about
import icons.help_faq
import icons.room_list

from gui.about_dialog import *


class Menubar(tkinter.Menu):

    def __init__(self, parent):
        super().__init__(tearoff=0)

        self.exit_icon = tkinter.PhotoImage(data=icons.application_exit.icon)
        self.file_import_icon = tkinter.PhotoImage(data=icons.file_import.icon)
        self.file_open_icon = tkinter.PhotoImage(data=icons.file_open.icon)
        self.file_save_icon = tkinter.PhotoImage(data=icons.file_save.icon)
        self.zoom_in_icon = tkinter.PhotoImage(data=icons.zoom_in.icon)
        self.zoom_out_icon = tkinter.PhotoImage(data=icons.zoom_out.icon)
        self.zoom_original_icon = tkinter.PhotoImage(
            data=icons.zoom_original.icon)
        self.help_about_icon = tkinter.PhotoImage(data=icons.help_about.icon)
        self.help_faq_icon = tkinter.PhotoImage(data=icons.help_faq.icon)
        self.room_list_icon = tkinter.PhotoImage(data=icons.room_list.icon)

        filemenu = tkinter.Menu(self, tearoff=0)
        filemenu.add_command(label="Otevřít výkres", image=self.file_open_icon,
                             compound="left", underline=0)
        filemenu.add_command(label="Uložit výkres", image=self.file_save_icon,
                             compound="left", underline=0)
        filemenu.add_separator()
        filemenu.add_command(label="Importovat nový výkres",
                             image=self.file_import_icon,
                             compound="left", underline=0)
        filemenu.add_separator()
        filemenu.add_command(label="Konec", image=self.exit_icon,
                             compound="left", underline=0,
                             command=parent.quit)

        edit = tkinter.Menu(self, tearoff=0)

        view = tkinter.Menu(self, tearoff=0)
        view.add_command(label="Zvětšit", image=self.zoom_in_icon,
                         compound="left", underline=1)
        view.add_command(label="Zmenšit", image=self.zoom_out_icon,
                         compound="left", underline=1)
        view.add_command(label="1:1", image=self.zoom_original_icon,
                         compound="left", underline=0)

        tools = tkinter.Menu(self, tearoff=0)
        tools.add_command(label="Seznam místností", image=self.room_list_icon,
                          compound="left", underline=0)

        helpmenu = tkinter.Menu(self, tearoff=0)
        helpmenu.add_command(label="Nápověda", image=self.help_faq_icon,
                             compound="left", underline=0)
        helpmenu.add_command(label="O programu", image=self.help_about_icon,
                             compound="left", underline=0, command=about)

        self.add_cascade(label="Soubor", menu=filemenu, underline=0)
        self.add_cascade(label="Upravit", menu=edit, underline=0)
        self.add_cascade(label="Zobrazit", menu=view, underline=0)
        self.add_cascade(label="Nástroje", menu=tools, underline=3)
        self.add_cascade(label="Nápověda", menu=helpmenu, underline=0)
