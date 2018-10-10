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
import time

from gui.dialogs.about_dialog import *
from tkinter import filedialog
from draw_service import DrawServiceInterface


class RoomsFromSapDialog(tkinter.Toplevel):

    def __init__(self, parent, configuration):
        tkinter.Toplevel.__init__(self, parent)

        self.parent = parent
        self.configuration = configuration
        self.address = self.configuration.server_address
        self.port = self.configuration.server_port

        if self.address and self.port:
            self.url = DrawServiceInterface.get_url(self.address, self.port)

        self.drawServiceInterface = DrawServiceInterface(service_url=self.url)

        self.title("Import místností ze SAPu")

        self.add_label(0, 0, "Platnost od")
        self.add_label(1, 0, "(rok-mesic-den)")
        today = time.strftime("%Y-%m-%d")
        self.calendar = self.add_value_widget(0, 1, today)

        self.listArealsButton = tkinter.Button(self, text="Načíst seznam areálů", command=self.read_areals)
        self.listArealsButton.grid(row=2, column=1, sticky="WE")

        self.add_label(3, 1, "Areály")
        self.add_label(3, 2, "Budovy")
        self.add_label(3, 3, "Podlaží")

        self.arealList = tkinter.Listbox(self, height=10, width=30)
        self.arealList.grid(row=4, column=1, sticky="WE")
        self.arealList.bind('<<ListboxSelect>>', lambda event:self.on_areal_select(event))

        self.buildingList = tkinter.Listbox(self, height=10, width=30)
        self.buildingList.grid(row=4, column=2, sticky="WE")

        self.floorList = tkinter.Listbox(self, height=10, width=30)
        self.floorList.grid(row=4, column=3, sticky="WE")

        self.okButton = tkinter.Button(self, text="OK", command=self.ok)
        self.okButton.grid(row=5, column=1, sticky="WE")

        # close the dialog on 'x' click
        self.protocol("WM_DELETE_WINDOW", self.destroy)

        # get the focus
        self.grab_set()

        # how the buttons should behave
        self.bind("<Return>", lambda event: self.ok())
        self.bind("<Escape>", lambda event: self.destroy())

    def on_areal_select(self, event):
        widget = event.widget
        selection = widget.curselection()
        if selection:
            index = int(selection[0])
            value = widget.get(index)
            areal = self.areals[index]
            aoid = areal["AOID"]
            self.read_buildings(aoid)

    def read_areals(self):
        valid_from = self.calendar.get()
        if not self.url:
            messagebox.showerror("Nastala chyba", "Není nastavená adresa serveru")
            return
        data, message = self.drawServiceInterface.read_areals(valid_from)
        if data:
            self.areals = data
            self.arealList.delete(0, tkinter.END)
            for areal in data:
                val = "{name} ({aoid})".format(name=areal["Label"], aoid=areal["AOID"])
                self.arealList.insert(tkinter.END,  val)
        else:
            messagebox.showerror("Nastala chyba", "Nastala chyba: {e}".format(e=message))

    def read_buildings(self, aoid):
        valid_from = self.calendar.get()
        if not self.url:
            messagebox.showerror("Nastala chyba", "Není nastavená adresa serveru")
            return
        data, message = self.drawServiceInterface.read_buildings(valid_from, aoid)
        if data:
            self.buildings = data
            self.buildingList.delete(0, tkinter.END)
            for building in data:
                val = "{name} ({aoid})".format(name=building["Label"], aoid=building["AOID"])
                self.buildingList.insert(tkinter.END, val)
        else:
            messagebox.showerror("Nastala chyba", "Nastala chyba: {e}".format(e=message))

    def ok(self):
        self.destroy()

    def add_value_widget(self, row, column, value):
        widget = self.value_widget(value)
        widget.grid(row=row, column=column, sticky="W", padx=5, pady=5)
        return widget

    def value_widget(self, value):
        widget = tkinter.Entry(self, width=12)
        widget.insert(tkinter.END, value)
        return widget

    def add_label(self, row, column, text):
        label = tkinter.Label(self, text=text)
        label.grid(row=row, column=column, sticky="W", padx=5, pady=5)


class LoadDialogs:

    @staticmethod
    def load_drawing(root):
        filetypes = [('Výkresy', '*.drw'),
                     ('Výkresy z CADu', '*.dxf')]
        dialog = filedialog.Open(root, filetypes=filetypes)
        return dialog.show()

    @staticmethod
    def load_rooms(root):
        filetypes = [('Místnosti', '*.rooms')]
        dialog = filedialog.Open(root, filetypes=filetypes)
        return dialog.show()

    @staticmethod
    def load_rooms_from_sap(root, configuration):
        d = RoomsFromSapDialog(root, configuration)
        return None
