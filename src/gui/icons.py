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

import icons.application_exit
import icons.file_open
import icons.file_save
import icons.file_save_as
import icons.file_import
import icons.zoom_in
import icons.zoom_out
import icons.zoom_original
import icons.help_about
import icons.help_faq
import icons.room_list
import icons.system_run
import icons.image
import icons.properties
import icons.view_grid
import icons.view_boundary
import icons.edit
import icons.edit_delete
import icons.edit_delete_shred
import icons.edit_redo
import icons.drawing_info
import icons.checkbox
import icons.service


class Icons:

    def __init__(self):
        self.exit_icon = tkinter.PhotoImage(data=icons.application_exit.icon)
        self.file_import_icon = tkinter.PhotoImage(data=icons.file_import.icon)
        self.file_open_icon = tkinter.PhotoImage(data=icons.file_open.icon)
        self.file_save_icon = tkinter.PhotoImage(data=icons.file_save.icon)
        self.file_save_as_icon = tkinter.PhotoImage(
            data=icons.file_save_as.icon)
        self.zoom_in_icon = tkinter.PhotoImage(data=icons.zoom_in.icon)
        self.zoom_out_icon = tkinter.PhotoImage(data=icons.zoom_out.icon)
        self.zoom_original_icon = tkinter.PhotoImage(
            data=icons.zoom_original.icon)
        self.help_about_icon = tkinter.PhotoImage(data=icons.help_about.icon)
        self.help_faq_icon = tkinter.PhotoImage(data=icons.help_faq.icon)
        self.room_list_icon = tkinter.PhotoImage(data=icons.room_list.icon)
        self.system_run_icon = tkinter.PhotoImage(data=icons.system_run.icon)
        self.image_icon = tkinter.PhotoImage(data=icons.image.icon)
        self.view_grid_icon = tkinter.PhotoImage(data=icons.view_grid.icon)
        self.view_boundary_icon = tkinter.PhotoImage(
            data=icons.view_boundary.icon)
        self.edit_icon = tkinter.PhotoImage(data=icons.edit.icon)
        self.edit_delete_icon = tkinter.PhotoImage(data=icons.edit_delete.icon)
        self.edit_delete_shred_icon = tkinter.PhotoImage(
            data=icons.edit_delete_shred.icon)
        self.edit_redo_icon = tkinter.PhotoImage(data=icons.edit_redo.icon)
        self.properties_icon = tkinter.PhotoImage(data=icons.properties.icon)
        self.drawing_info_icon = tkinter.PhotoImage(
            data=icons.drawing_info.icon)
        self.checkbox_icon = tkinter.PhotoImage(data=icons.checkbox.icon)
        self.service_icon = tkinter.PhotoImage(data=icons.service.icon)
