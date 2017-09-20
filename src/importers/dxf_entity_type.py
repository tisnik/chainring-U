from enum import Enum

class DxfEntityType(Enum):
    UNKNOWN = 1,
    LINE = 2,
    CIRCLE = 3,
    ARC = 4,
    TEXT = 5
