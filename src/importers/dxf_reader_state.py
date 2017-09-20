from enum import Enum

class DxfReaderState(Enum):
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
