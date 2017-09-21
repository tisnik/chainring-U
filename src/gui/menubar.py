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
import icons.exit
import icons.open


class Menubar(tkinter.Menu):

    def __init__(self, parent):
        super().__init__(tearoff=0)

        self.exit_icon = tkinter.PhotoImage(data=icons.exit.icon)
        self.open_icon = tkinter.PhotoImage(data=icons.open.icon)

        filemenu = tkinter.Menu(self, tearoff=0)
        filemenu.add_command(label="Importovat nový výkres")
        filemenu.add_command(label="Otevřít výkres", image=self.open_icon,
                             compound="left", underline=0)
        filemenu.add_separator()
        filemenu.add_command(label="Konec", image=self.exit_icon,
                             compound="left", underline=0,
                             command=parent.quit)

        edit = tkinter.Menu(self, tearoff=0)
        view = tkinter.Menu(self, tearoff=0)

        tools = tkinter.Menu(self, tearoff=0)
        tools.add_command(label="Seznam místností")

        helpmenu = tkinter.Menu(self, tearoff=0)
        helpmenu.add_command(label="O programu")

        self.add_cascade(label="Soubor", menu=filemenu)
        self.add_cascade(label="Úpravy", menu=edit)
        self.add_cascade(label="Zobrazit", menu=view)
        self.add_cascade(label="Nástroje", menu=tools)
        self.add_cascade(label="Nápověda", menu=helpmenu)
