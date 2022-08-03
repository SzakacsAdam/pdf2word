from enum import Enum
from enum import auto


class PdfStatus(Enum):
    IN_QUEUE: int = 0
    START: int = 1
    ERROR: int = 2
    DONE: int = 3
    WAITING: int = 4
    REMOVE: int = 5

    def next(self) -> Enum:
        members: list[PdfStatus] = list(self.__class__)
        index: int = members.index(self) + 1
        if index >= len(members):
            return members[-1]
        return members[index]
