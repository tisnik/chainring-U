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

"""Module with class that represents the arc."""


from entities.entity import Entity
from geometry.bounds import Bounds


class Arc(Entity):
    """Class that represents the arc."""

    def __init__(self, x, y, radius, angle1, angle2):
        """Construct new arc from provided coordinates and angles."""
        self.x = x
        self.y = y
        self.radius = radius
        self.angle1 = angle1
        self.angle2 = angle2
        self._id = None

    def str(self):
        """Return textual representation of arc."""
        return "A {x} {y} {r} {a1} {a2}".format(
            x=self.x,
            y=self.y,
            r=self.radius,
            a1=self.angle1,
            a2=self.angle2)

    def draw(self, canvas, xoffset, yoffset, scale):
        """Draw the entity onto canvas."""
        extent = self.angle2 - self.angle1

        if extent < 0:
            extent += 360

        self._id = canvas.create_arc(self.x-self.radius, self.y-self.radius,
                                     self.x+self.radius, self.y+self.radius,
                                     start=self.angle1, extent=extent,
                                     outline="black", style="arc",
                                     tags="drawing")

    def transform(self, xoffset, yoffset, scale):
        """Perform the transformation of the entity into paper space."""
        self.x = self.x + xoffset
        self.y = self.y + yoffset
        self.x *= scale
        self.y *= scale
        self.radius *= scale

    def getBounds(self):
        """Compute bounds for given entity."""
        return Bounds(self.x - self.radius, self.y - self.radius,
                      self.x + self.radius, self.y + self.radius)
