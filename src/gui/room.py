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


class Room:

    def __init__(self):
        self.cleanup()

    def cleanup(self):
        self.last_x = None
        self.last_y = None
        self.polygon_world = []
        self.polygon_canvas = []

    def last_point_exist(self):
        return self.last_x and self.last_y

    def vertexes(self):
        """Return number of vertexes drawn by user."""
        return len(self.polygon_world)
