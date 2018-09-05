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

"""Module with class that represents the polyline entity."""

import sys

from entities.entity import Entity
from geometry.bounds import Bounds


class Polyline(Entity):
    """Class that represents the polyline entity."""

    def __init__(self, points_x, points_y, color, layer):
        """Construct new text from provided starting coordinates."""
        self.points_x = points_x
        self.points_y = points_y
        self.color = color
        self.layer = layer
        # graphics entity ID on the canvas
        self._id = None

    def str(self):
        """Return textual representation of text entity."""
        return "T {x} {y} {t}".format(
            x=self.x,
            y=self.y)

    def asDict(self):
        """Convert Polyline entity into proper dictionary."""
        return {
            "T": "P",
            "xpoints": self.points_x,
            "ypoints": self.points_y
        }

    def draw(self, canvas, xoffset=0, yoffset=0, scale=1):
        """Draw the entity onto canvas."""
        points = []
        for i in range(0, len(self.points_x)):
            x = self.points_x[i] + xoffset
            y = self.points_y[i] + yoffset
            x *= scale
            y *= scale
            points.append(x)
            points.append(y)
        self._id = canvas.create_polygon(points, fill="", outline="green")

    def transform(self, xoffset, yoffset, scale):
        """Perform the transformation of the entity into paper space."""
        for i in range(0, len(self.points_x)):
            self.points_x[i] = self.points_x[i] + xoffset
            self.points_y[i] = self.points_y[i] + yoffset
            self.points_x[i] *= scale
            self.points_y[i] *= scale

    def getBounds(self):
        """Compute bounds for given entity."""
        xmin = sys.float_info.max
        ymin = sys.float_info.max
        xmax = -sys.float_info.max
        ymax = -sys.float_info.max

        for x in self.points_x:
            if x < xmin:
                xmin = x
            if x > xmax:
                xmax = x

        for y in self.points_y:
            if y < ymin:
                ymin = y
            if y > ymax:
                ymax = y

        print(xmin, ymin, xmax, ymax)

        return Bounds(xmin, ymin,
                      xmax, ymax)
