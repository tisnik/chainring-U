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


class Drawing:

    def __init__(self, entities, statistic, lines=0, metadata=None):
        self._entities = entities
        self._statistic = statistic
        self._lines = lines
        self._rooms = []
        self._metadata = metadata or {}
        self._room_counter = 1
        self._filename = None

    @property
    def entities(self):
        return self._entities

    @entities.setter
    def entities(self, entities):
        self._entities = entities

    @property
    def statistic(self):
        return self._statistic

    @statistic.setter
    def statistic(self, statistic):
        self._statistic = statistic

    @property
    def lines(self):
        return self._lines

    @lines.setter
    def lines(self, lines):
        self._lines = lines

    @property
    def metadata(self):
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        self._metadata = metadata

    @property
    def rooms(self):
        return self._rooms

    @rooms.setter
    def rooms(self, rooms):
        self._rooms = rooms

    @property
    def filename(self):
        return self._filename

    @filename.setter
    def filename(self, filename):
        self._filename = filename

    def rescale(self, xoffset, yoffset, scale):
        for entity in self._entities:
            entity.transform(xoffset, yoffset, scale)

    def find_entity_by_id(self, entity_id):
        for entity in self._entities:
            if entity._id == entity_id:
                return entity
        return None

    def add_new_room(self, canvas_id, polygon):
        room_id = self._room_counter
        self._rooms.append({"room_id": room_id,
                            "canvas_id": canvas_id,
                            "polygon": polygon})
        self._room_counter += 1
        return room_id

    def find_room(self, selector, value):
        for room in self._rooms:
            if room[selector] == value:
                return room
        return None

    def find_room_by_room_id(self, canvas_id):
        return self.find_room("room_id", canvas_id)

    def find_room_by_canvas_id(self, canvas_id):
        return self.find_room("canvas_id", canvas_id)