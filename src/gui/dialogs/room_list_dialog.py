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


class RoomListDialog(tkinter.Toplevel):
    def __init__(self, parent, drawing):
        tkinter.Toplevel.__init__(self, parent)
        self.title("Seznam místností")

        okButton = tkinter.Button(self, text="OK", command=self.ok)
        okButton.grid(row=3, column=1, sticky="WE")

        # close the dialog on 'x' click
        self.protocol("WM_DELETE_WINDOW", self.destroy)

        # get the focus
        self.grab_set()

        # how the buttons should behave
        self.bind("<Return>", lambda event: self.ok())
        self.bind("<Escape>", lambda event: self.destroy())

        # get the focus
        okButton.focus_set()

    def ok(self):
        self.destroy()

    @staticmethod
    def compute_sum(drawing_statistic):
        return sum(drawing_statistic.values())
