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
from tkinter import messagebox

from exporters.drawing_exporter import *

from geometry.utils import GeometryUtils
from gui.canvas import *
from gui.toolbar import *
from gui.menubar import *
from gui.palette import *
from gui.status_bar import *

from gui.icons import *
from gui.canvas_mode import CanvasMode
from gui.room_error_dialog import *
from gui.dialogs.yes_no_dialogs import *
from gui.save_dialogs import SaveDialogs
from gui.floor_select_dialog import FloorSelectDialog
from gui.room import Room


class MainWindow:

    SCALE_UP_FACTOR = 1.1
    SCALE_DOWN_FACTOR = 0.9

    def __init__(self, window_width, window_height):
        self._drawing = None
        self.root = tkinter.Tk()

        self.icons = Icons()
        self.canvas_mode = CanvasMode.VIEW

        self.canvas = Canvas(self.root, window_width, window_height, self)
        self.toolbar = Toolbar(self.root, self, self.canvas)
        self.palette = Palette(self.root, self)
        self.statusbar = StatusBar(self.root)

        self.menubar = Menubar(self.root, self, self.canvas)

        self.root.config(menu=self.menubar)

        self.configure_grid()

        self.toolbar.grid(column=1, row=1, columnspan=2, sticky="WE")
        self.palette.grid(column=1, row=2, sticky="NWSE")
        self.canvas.grid(column=2, row=2, sticky="NWSE")
        self.statusbar.grid(column=1, row=3, columnspan=2, sticky="WE")

        self.canvas.bind("<ButtonPress-1>", self.on_left_button_pressed)
        self.canvas.bind("<B1-Motion>", self.on_left_button_drag)
        self.canvas.bind("<ButtonPress-3>", self.on_right_button_pressed)

        # scroll on Linux
        self.canvas.bind("<Button-4>", self.zoom_plus)
        self.canvas.bind("<Button-5>", self.zoom_minus)

        # scroll on windows
        self.canvas.bind("<MouseWheel>", self.zoom)

        self.room = Room()
        self.edited_room_id = None

    def configure_grid(self):
        tkinter.Grid.rowconfigure(self.root, 2, weight=1)
        tkinter.Grid.columnconfigure(self.root, 2, weight=1)

    def draw_new_room_command(self, event=None):
        self.canvas_mode = CanvasMode.DRAW_ROOM

    def save_drawing(self, filename):
        if filename:
            # set the new filename
            self.drawing.filename = filename
            exporter = DrawingExporter(filename, self.drawing)
            exporter.export()

    def save_drawing_command(self, event=None):
        filename = self.drawing.filename
        if filename is None:
            filename = SaveDialogs.save_drawing(self.root)
        self.save_drawing(filename)

    def save_drawing_as_command(self, event=None):
        filename = SaveDialogs.save_drawing(self.root)
        self.save_drawing(filename)

    def open_drawing_command(self, event=None):
        FloorSelectDialog(self.root)

    def delete_room_command(self, index, value):
        #print(index, value)
        if dialog_delete_whole_room(value):
            room = self.drawing.find_room_by_room_id(value)
            if room is not None:
                self.canvas.delete_object_with_id(room["canvas_id"])
            # must be deleted after the room is removed from canvas!
            self.drawing.delete_room(value)
            self.palette.delete_room_from_list(index)

    def delete_room_polygon_command(self, index, value):
        if dialog_delete_room_polygon(value):
            room = self.drawing.find_room_by_room_id(value)
            if room is not None:
                self.canvas.delete_object_with_id(room["canvas_id"])
            self.drawing.delete_room_polygon(value)
            self.palette.fill_in_room_info(room)

    def redraw_room_polygon_command(self, index, value):
        room = self.drawing.find_room_by_room_id(value)
        if room is not None:
            self.canvas.delete_object_with_id(room["canvas_id"])
        self.canvas_mode = CanvasMode.DRAW_ROOM
        self.edited_room_id = value

    def scroll_start(self, event):
        self.canvas.scan_mark(event.x, event.y)

    def scroll_move(self, event):
        self.canvas.scan_dragto(event.x, event.y, gain=1)
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def get_nearest_entity(self, x, y):
        return self.canvas.find_closest(x, y)[0]

    def finish_new_room(self):
        canvas_id = self.canvas.draw_new_room(self.room)
        if self.edited_room_id is None:
            room_id = self._drawing.add_new_room(canvas_id, self.room.polygon_world)
            self.palette.add_new_room(room_id)
        else:
            room_id = self.edited_room_id
            self._drawing.update_room_polygon(room_id, canvas_id, self.room.polygon_world)
        self.edited_room_id = None
        self.canvas.delete_temporary_entities()
        # cleanup
        self.room.cleanup()
        self.canvas_mode = CanvasMode.VIEW

    def on_right_button_pressed(self, event):
        if self.canvas_mode == CanvasMode.DRAW_ROOM:
            vertexes = self.room.vertexes()
            if vertexes == 0:
                error_dialog_no_points()
                return
            elif vertexes < 3:
                error_dialog_not_enough_points()
                return
            elif vertexes == 3:
                if dialog_store_vertex_with_three_vertexes():
                    self.finish_new_room()
            else:
                self.finish_new_room()

    def entity_with_endpoints(self, item):
        """Returns the drawing entity for the given canvas item."""

        # sanity check
        if item is None:
            return None

        # first check canvas entity type
        entity_type = self.canvas.type(item)
        if entity_type != "line":
            return None

        # then check the tags associated with the canvas entity
        tags = self.canvas.gettags(item)
        if "drawing" not in tags:
            return None

        # third check if canvas entity relates to drawing entity
        entity = self.drawing.find_entity_by_id(item)
        if entity is None:
            return None

        # fourth check drawing entity type
        # (not needed ATM)
        return entity

    def on_room_click_listbox(self, room_id):
        room = self.drawing.find_room_by_room_id(room_id)
        if room:
            self.palette.enable_all()
            self.palette.fill_in_room_info(room)
            self.canvas.highlight_room(room)

    def on_room_click_canvas(self, canvas_object_id):
        room = self.drawing.find_room_by_canvas_id(canvas_object_id)
        if room:
            self.palette.enable_all()
            self.palette.fill_in_room_info(room)
            self.palette.select_room_in_list(room)
            self.canvas.highlight_room(room)

    def draw_new_room_line(self, canvas_x, canvas_y):
        if self.room.last_point_exist():
            self.canvas.draw_new_room_temporary_line(self.room.last_x,
                                                     self.room.last_y,
                                                     canvas_x, canvas_y)
        self.room.last_x = canvas_x
        self.room.last_y = canvas_y

    def nearest_endpoint(self, x, y, item, entity):
        """Find nearest endpoint for given entity and coordinates [x,y]."""
        x1, y1, x2, y2 = self.canvas.coords(item)
        if GeometryUtils.square_length(x1, y1, x, y) < GeometryUtils.square_length(x2, y2, x, y):
            return x1, y1, entity.x1, entity.y1
        else:
            return x2, y2, entity.x2, entity.y2

    def add_vertex_to_room(self, event):
        # get the coordinates before canvas scroll
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)
        item = self.get_nearest_entity(x, y)

        entity = self.entity_with_endpoints(item)
        if entity is not None:
            canvas_x, canvas_y, world_x, world_y = self.nearest_endpoint(x, y, item, entity)
            self.canvas.draw_cross(canvas_x, canvas_y)
            self.draw_new_room_line(canvas_x, canvas_y)
            self.room.polygon_canvas.append((canvas_x, canvas_y))
            self.room.polygon_world.append((world_x, world_y))
            # self.canvas.itemconfig(item, fill='cyan')

    def on_left_button_pressed(self, event):
        if self.canvas_mode == CanvasMode.DRAW_ROOM:
            self.add_vertex_to_room(event)
        else:
            self.scroll_start(event)

    def on_left_button_drag(self, event):
        if self.canvas_mode == CanvasMode.DRAW_ROOM:
            pass
        else:
            self.scroll_move(event)

    # zoom on Windows
    def zoom(self, event):
        if event.delta > 0:
            self.canvas.scale("all", event.x, event.y, 1.1, 1.1)
        elif event.delta < 0:
            self.canvas.scale("all", event.x, event.y, 0.9, 0.9)
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    # zoom on Linux
    def zoom_plus(self, event=None):
        if event:
            self.canvas.scale("all", event.x, event.y,
                              MainWindow.SCALE_UP_FACTOR,
                              MainWindow.SCALE_UP_FACTOR)
        else:
            self.canvas.scale("all", self.canvas.width/2, self.canvas.height/2,
                              MainWindow.SCALE_UP_FACTOR,
                              MainWindow.SCALE_UP_FACTOR)
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    # zoom on Linux
    def zoom_minus(self, event=None):
        if event:
            self.canvas.scale("all", event.x, event.y,
                              MainWindow.SCALE_DOWN_FACTOR,
                              MainWindow.SCALE_DOWN_FACTOR)
        else:
            self.canvas.scale("all", self.canvas.width/2, self.canvas.height/2,
                              MainWindow.SCALE_DOWN_FACTOR,
                              MainWindow.SCALE_DOWN_FACTOR)
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def quit(self):
        answer = messagebox.askyesno("Skutečně ukončit program?",
                                     "Skutečně ukončit program?")
        if answer:
            self.root.quit()

    def show(self):
        self.root.mainloop()

    @property
    def drawing(self):
        return self._drawing

    @drawing.setter
    def drawing(self, drawing):
        self._drawing = drawing

    def redraw(self):
        self.canvas.delete("all")
        self.canvas.draw_grid()
        self.canvas.draw_boundary()
        self.canvas.draw_entities(self.drawing.entities, 0, 0, 1)
