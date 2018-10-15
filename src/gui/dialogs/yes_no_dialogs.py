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


def dialog_store_vertex_with_three_vertexes():
    return messagebox.askyesno("Místnost jen se třemi rohy",
                               "Opravdu si přejete nakreslit místnost jen se třemi rohy?")


def dialog_delete_whole_room(sap_id):
    return messagebox.askyesno("Smazat místnost",
                               "Opravdu si přejete smazat celou místnost s označením " + sap_id + "?")


def dialog_delete_room_polygon(sap_id):
    return messagebox.askyesno("Smazat obrys mísnosti",
                               "Opravdu si přejete smazat obrys místnosti s označením " + sap_id + "?")


def dialog_load_new_drawing():
    return messagebox.askyesno("Smazat stávající výkres",
                               "Opravdu si přejete smazat stávající výkres a načíst výkres nový?")

def dialog_load_rooms():
    return messagebox.askyesno("Smazat stávající mísnosti",
                               "Opravdu si přejete smazat stávající místnosti a načíst místnosti ze souboru?")

def dialog_load_rooms_from_sap():
    return messagebox.askyesno("Smazat stávající mísnosti",
                               "Opravdu si přejete smazat stávající místnosti a načíst místnosti ze SAPu?")

def dialog_synchronize_rooms_with_sap():
    return messagebox.askyesno("Synchronizace se SAPem",
                               "Opravdu si přejete synchronizovat stávající místnosti ze SAPem?")
