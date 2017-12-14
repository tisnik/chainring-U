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

from tkinter import messagebox


def error_dialog_no_points():
    messagebox.showerror("Chyba při kreslení místnosti",
                         "Nebyl zadán ani jeden bod")


def error_dialog_not_enough_points():
    messagebox.showerror("Chyba při kreslení místnosti",
                         "Místnost musí být definována alespoň třemi body")
