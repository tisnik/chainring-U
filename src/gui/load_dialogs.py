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

from tkinter import filedialog


class LoadDialogs:

    @staticmethod
    def load_drawing(root):
        filetypes = [('Výkresy', '*.drw')]
        dialog = filedialog.Open(root, filetypes=filetypes)
        return dialog.show()
