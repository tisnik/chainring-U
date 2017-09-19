import tkinter


class Toolbar(tkinter.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, text="Nástroje", padx=5, pady=5)
        b = tkinter.Button(self, text="B1")
        b.grid(column=1, row=1)
