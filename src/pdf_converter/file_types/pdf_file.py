from os import sep
from time import time



class PdfFile:
    __slots__ = (
        "_file_path", "pdf_convert_type", "_file_name",
        "created"
    )

    def __init__(self, file_path: str,
                 pdf_convert_type: str) -> None:
        self._file_path: str = file_path
        self.pdf_convert_type: str = pdf_convert_type

        self._file_name: str = file_path.split(sep)[-1]
        self.created: int = int(time())

    @property
    def file_name(self) -> str:
        return self._file_name

    @property
    def file_path(self) -> str:
        return self._file_path

    @file_path.setter
    def file_path(self, path: str) -> None:
        self._file_path = path

