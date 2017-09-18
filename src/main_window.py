#!/usr/bin/env python

import tkinter
from tkinter import ttk


def test():
    print("Test!")


root = tkinter.Tk()

menubar = tkinter.Menu(root)

filemenu = tkinter.Menu(menubar, tearoff=0)
filemenu.add_command(label="Importovat nový výkres")
filemenu.add_command(label="Otevřít výkres")
filemenu.add_separator()
filemenu.add_command(label="Konec", command=root.quit)

menubar.add_cascade(label="Soubor", menu=filemenu)

drawing = tkinter.Menu(menubar, tearoff=0)
drawing.add_command(label="Seznam místností")
menubar.add_cascade(label="Výkres", menu=drawing)

helpmenu = tkinter.Menu(menubar, tearoff=0)
helpmenu.add_command(label="O programu")
menubar.add_cascade(label="Nápověda", menu=helpmenu)

root.config(menu=menubar)

root.mainloop()
