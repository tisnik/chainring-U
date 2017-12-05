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

    def __init__(self, parent, main_window):
        super().__init__(parent, text="Výkres", padx=5, pady=5)
        self.main_window = main_window

        self.listbox = tkinter.Listbox(self)
        self.listbox.pack(fill=tkinter.BOTH, expand=True)
        self.group = tkinter.LabelFrame(self, text="Vybraná místnost",
                                        padx=5, pady=5)

        label1 = tkinter.Label(self.group, text="ID")
        label1.grid(column=1, row=1, sticky="W")
        label2 = tkinter.Label(self.group, text="Rohů")
        label2.grid(column=1, row=2, sticky="W")
        # button = tkinter.Button(self.group, text="Test")
        # button.pack()
        self.group.pack(fill=tkinter.X, expand=False)
        self.listbox.bind("<<ListboxSelect>>", self.on_room_click)

    def add_new_room(self, canvas_id):
        self.listbox.insert(tkinter.END, canvas_id)

    def on_room_click(self, event):
        selection = self.listbox.curselection()
        if selection:
            index = selection[0]
            value = self.listbox.get(index)
            self.main_window.on_room_click_listbox(value)
