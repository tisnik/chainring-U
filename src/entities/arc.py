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


class Arc:
    def __init__(self, x, y, radius, angle1, angle2):
        self.x = x
        self.y = y
        self.radius = radius
        self.angle1 = angle1
        self.angle2 = angle2

    def str(self):
        return "A {x} {y} {r} {a1} {a2}".format(
            x=self.x,
            y=self.y,
            r=self.radius,
            a1=self.angle1,
            a2=self.angle2)
