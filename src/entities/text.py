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


class Text(Entity):
    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text

    def str(self):
        return "T {x} {y} {t}".format(
            x=self.x,
            y=self.y,
            t=self.text)

    def draw(self, canvas, xoffset, yoffset, scale):
        return (self.x, self.y, self.x, self.y)

    def getBounds(self):
        return Bounds(self.x, self.y,
                      self.x, self.y)
