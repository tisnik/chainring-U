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


class Canvas(tkinter.Canvas):

    GRID_SIZE = 50
    CROSS_SIZE = 5

    def __init__(self, parent, width, height, main_window):
        super().__init__(parent, width=width, height=height,
                         background="white")
        # self.draw_grid(width, height, Canvas.GRID_SIZE)
        # self.draw_boundary(width, height)
        self._grid = True
        self._boundary = True
        self.width = width
        self.height = height
        self.main_window = main_window
        self.selected_room_item = None

    def draw_grid(self):
        for x in range(0, self.width, Canvas.GRID_SIZE):
            self.create_line(x, 0, x, self.height, dash=7, tags="grid")
        for y in range(0, self.height, Canvas.GRID_SIZE):
            self.create_line(0, y, self.width, y, dash=7, tags="grid")
        if self._grid:
            self.show_grid()
        else:
            self.hide_grid()

    def draw_boundary(self):
        self.create_line(2, 2,
                         self.width, 2,
                         self.width, self.height,
                         2, self.height,
                         2, 2,
                         tags="boundary")
        if self._boundary:
            self.show_boundary()
        else:
            self.hide_boundary()

    def show_grid(self):
        self.itemconfig("grid", fill="blue")

    def hide_grid(self):
        self.itemconfig("grid", fill="")

    def toggle_grid(self):
        self._grid = not self._grid
        if self._grid:
            self.show_grid()
        else:
            self.hide_grid()

    def show_boundary(self):
        self.itemconfig("boundary", fill="red", width=2)

    def hide_boundary(self):
        self.itemconfig("boundary", fill="", width=2)

    def toggle_boundary(self):
        self._boundary = not self._boundary
        if self._boundary:
            self.show_boundary()
        else:
            self.hide_boundary()

    def draw_entities(self, entities, xoffset, yoffset, scale):
        for entity in entities:
            entity.draw(self, xoffset, yoffset, scale)


    def draw_rooms(self, rooms, xoffset, yoffset, scale):
        for room in rooms:
            print(room["room_id"])
            room["canvas_id"] = self.draw_room(room)


    def draw_new_room_temporary_line(self, x1, y1, x2, y2):
        self.create_line(x1, y1, x2, y2,
                         fill='red', tags="new_room_temporary")

    def draw_cross(self, x, y):
        self.create_line(x-Canvas.CROSS_SIZE, y, x+Canvas.CROSS_SIZE, y,
                         fill='red', tags="cross")
        self.create_line(x, y-Canvas.CROSS_SIZE, x, y+Canvas.CROSS_SIZE,
                         fill='red', tags="cross")

    def delete_entities_with_tag(self, tag):
        """Delete all entities having given tag."""
        items = self.find_withtag(tag)
        for item in items:
            self.delete(item)

    def delete_temporary_entities(self):
        """Delete all temporary entities."""
        self.delete_entities_with_tag("cross")
        self.delete_entities_with_tag("new_room_temporary")

    def delete_object_with_id(self, object_id):
        self.delete(object_id)

    def draw_room(self, room):
        print(room)
        new_object = self.create_polygon(room["polygon"], width=2,
                                         fill="", activefill="#ffff80",
                                         outline="magenta", stipple="gray50")
        self.tag_bind(new_object, "<ButtonPress-1>",
                      lambda event, new_object=new_object: self.on_room_click(new_object))
        return new_object

    def draw_new_room(self, room):
        print(room)
        new_object = self.create_polygon(room.polygon_canvas, width=2,
                                         fill="", activefill="#ffff80",
                                         outline="magenta", stipple="gray50")
        self.tag_bind(new_object, "<ButtonPress-1>",
                      lambda event, new_object=new_object: self.on_room_click(new_object))
        return new_object

    def on_room_click(self, canvas_object_id):
        self.main_window.on_room_click_canvas(canvas_object_id)

    def highlight_room(self, room):
        """Highlight the given room and remove highlight for previously selected one."""
        if self.selected_room_item:
            self.itemconfig(self.selected_room_item, fill="", activefill="#ffff80", outline="magenta")
        item = room["canvas_id"]
        if item:
            self.selected_room_item = item
            self.itemconfig(self.selected_room_item, fill="#ff8080", activefill="", outline="cyan")
