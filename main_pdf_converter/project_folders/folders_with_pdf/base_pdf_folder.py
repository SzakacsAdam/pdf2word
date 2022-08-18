from collections import deque

from src.main_pdf_converter.pdf_handler import PdfConvertType
from src.main_pdf_converter.pdf_handler import PdfConvertedMimeType
from src.main_pdf_converter.pdf_handler import PdfFile
from src.main_pdf_converter.pdf_handler.junk_file import JunkFile
from src.utils import wait_until_file_moved
from ..base_folder import BaseFolder


class BasePdfFolder(BaseFolder):
    supported_format: str = "pdf"
    pdf_queue: deque[PdfFile] = deque()
    junk_queue: deque[JunkFile] = deque()

    __slots__ = ("pdf_convert_type", "pdf_converted_mime_type")

    def __init__(self, src: str, folder_name: str,
                 pdf_convert_type: PdfConvertType,
                 pdf_converted_mime_type: PdfConvertedMimeType) -> None:
        super().__init__(src, folder_name)
        self.pdf_convert_type: PdfConvertType = pdf_convert_type
        self.pdf_converted_mime_type: PdfConvertedMimeType = pdf_converted_mime_type

    def read_folder(self) -> None:
        for file_path in self.get_new_file_paths():
            if not wait_until_file_moved(file_path):
                continue

            if file_path.endswith(self.supported_format):
                pdf: PdfFile = PdfFile(file_path=file_path,
                                       pdf_convert_type=self.pdf_convert_type,
                                       pdf_converted_mime_type=self.pdf_converted_mime_type)
                self.pdf_queue.append(pdf)
            else:
                junk: JunkFile = JunkFile(file_path)
                self.junk_queue.append(junk)
            self.already_read.add(file_path)

    def get_pdf_file(self) -> PdfFile | None:
        if self.pdf_queue:
            return self.pdf_queue.popleft()
        return None

    def get_junk_file(self) -> JunkFile | None:
        if self.junk_queue:
            return self.junk_queue.popleft()
        return None
