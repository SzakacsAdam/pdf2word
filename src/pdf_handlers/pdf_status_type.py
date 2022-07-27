from enum import Enum
from enum import auto

class PdfStatusType(Enum):
    START: int = auto()
    ERROR: int = auto()
    DONE: int = auto()
    OK = auto()
