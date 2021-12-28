from enum import Enum

class FileState(Enum):
    OK = 1
    OUT_OF_DATE = 2
    NOT_FOUND = 3