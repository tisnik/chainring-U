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


from entities.entity import Entity
from geometry.bounds import Bounds


class Polyline(Entity):
    """Class that represents the polyline entity."""

    def __init__(self, x, y):
        """Construct new text from provided starting coordinates."""
        self.x = x
        self.y = y
        # graphics entity ID on the canvas
        self._id = None

    def str(self):
        """Return textual representation of text entity."""
        return "T {x} {y} {t}".format(
            x=self.x,
            y=self.y)

    def asDict(self):
        return {
            "T": "P",
            "x": self.x,
            "y": self.y,
        }

    def draw(self, canvas, xoffset, yoffset, scale):
        """Draw the entity onto canvas."""
        return (self.x, self.y, self.x, self.y)

    def transform(self, xoffset, yoffset, scale):
        """Perform the transformation of the entity into paper space."""
        pass

    def getBounds(self):
        """Compute bounds for given entity."""
        return Bounds(self.x, self.y,
                      self.x, self.y)
