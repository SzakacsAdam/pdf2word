from os import sep
from time import time

from .pdf_convert_type import PdfConvertType
from .pdf_converted_mime_type import PdfConvertedMimeType
from .pdf_status import PdfStatus


class PdfFile:
    __slots__ = (
        "pdf_id", "file_path", "pdf_convert_type", "pdf_converted_mime_type", "_status", "file_name",
        "created"
    )

    def __init__(self, pdf_id: str, file_path: str,
                 pdf_convert_type: PdfConvertType,
                 pdf_converted_mime_type: PdfConvertedMimeType,
                 status: PdfStatus = PdfStatus.IN_QUEUE):
        self.pdf_id: str = pdf_id
        self.file_path = file_path
        self.pdf_convert_type: PdfConvertType = pdf_convert_type
        self.pdf_converted_mime_type: PdfConvertedMimeType = pdf_converted_mime_type
        self._status: PdfStatus = status

        self.file_name: str = file_path.split(sep)[-1].split('.')[-2]
        self.created: int = int(time())

    @property
    def status(self) -> PdfStatus:
        return self._status

    @status.setter
    def status(self, status: PdfStatus) -> None:
        self._status = status
