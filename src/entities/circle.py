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

from entities.entity import Entity
from entities.bounds import Bounds


class Circle(Entity):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def str(self):
        return "C {x} {y} {r}".format(
            x=self.x,
            y=self.y,
            r=self.radius)

    def draw(self, canvas, xoffset, yoffset, scale):
        canvas.create_oval(self.x-self.radius, self.y-self.radius,
                           self.x+self.radius, self.y+self.radius, fill="red")

    def transform(self, xoffset, yoffset, scale):
        self.x = self.x + xoffset
        self.y = self.y + yoffset
        self.x *= scale
        self.y *= scale
        self.radius *= scale

    def getBounds(self):
        return Bounds(self.x - self.radius, self.y - self.radius,
                      self.x + self.radius, self.y + self.radius)
