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


class Menubar(tkinter.Menu):

    def __init__(self, parent):
        super().__init__(tearoff=0)

        filemenu = tkinter.Menu(self, tearoff=0)
        filemenu.add_command(label="Importovat nový výkres")
        filemenu.add_command(label="Otevřít výkres")
        filemenu.add_separator()
        filemenu.add_command(label="Konec", command=parent.quit)

        self.add_cascade(label="Soubor", menu=filemenu)

        drawing = tkinter.Menu(self, tearoff=0)
        drawing.add_command(label="Seznam místností")
        self.add_cascade(label="Výkres", menu=drawing)

        helpmenu = tkinter.Menu(self, tearoff=0)
        helpmenu.add_command(label="O programu")
        self.add_cascade(label="Nápověda", menu=helpmenu)
