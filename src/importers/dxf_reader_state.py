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

"""State of the DXF reader finite automata."""

from enum import Enum


class DxfReaderState(Enum):
    """State of the DXF reader finite automata."""

    BEGINNING = 1,
    BEGINNING_SECTION = 2,
    SECTION_HEADER = 3,
    SECTION_TABLES = 4,
    SECTION_BLOCKS = 5,
    SECTION_BLOCK = 6,
    SECTION_BLOCK_ENTITY = 7,
    SECTION_ENTITIES = 8,
    SECTION_OBJECTS = 9,
    ENTITY = 10,
    LINE_IN_BLOCK = 11,
    EOF = 12
