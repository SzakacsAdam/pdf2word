from os import sep
from time import time

from .enums.pdf_convert_type import PdfConvertType
from .enums.pdf_converted_mime_type import PdfConvertedMimeType
from .enums.pdf_status import PdfStatus
from src.utils import sha1_hash


class PdfFile:
    __slots__ = (
        "_pdf_id", "_file_path", "pdf_convert_type",
        "pdf_converted_mime_type", "_status", "_file_name",
        "created"
    )

    def __init__(self, file_path: str,
                 pdf_convert_type: PdfConvertType,
                 pdf_converted_mime_type: PdfConvertedMimeType,
                 status: PdfStatus = PdfStatus.IN_QUEUE) -> None:
        self._file_path: str = file_path
        self.pdf_convert_type: PdfConvertType = pdf_convert_type
        self.pdf_converted_mime_type: PdfConvertedMimeType = pdf_converted_mime_type
        self._status: PdfStatus = status

        self._pdf_id: str = sha1_hash(file_path)
        self._file_name: str = file_path.split(sep)[-1]
        self.created: int = int(time())

    @property
    def status(self) -> PdfStatus:
        return self._status

    @status.setter
    def status(self, status: PdfStatus) -> None:
        self._status = status

    @property
    def file_name(self) -> str:
        return self._file_name

    @property
    def file_path(self) -> str:
        return self._file_path

    @file_path.setter
    def file_path(self, path: str) -> None:
        self._file_path = path

    @property
    def pdf_id(self) -> str:
        return self._pdf_id
