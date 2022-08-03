from collections import deque
from time import time

from .pdf_file import PdfFile
from .pdf_status import PdfStatus


class PdfContainer:
    pdf_file_queue: deque[PdfFile] = deque()
    pdf_files: dict[str, PdfFile] = dict()

    __slots__ = "expiration_time"

    def __init__(self, expiration_time: int = 60 * 30):
        self.expiration_time: int = expiration_time

    def __contains__(self, item) -> bool:
        return item in self.pdf_files.keys()

    def add_pdf(self, pdf: PdfFile) -> None:
        self.pdf_file_queue.append(pdf)
        self.pdf_files[pdf.pdf_id] = pdf

    def get_next_item(self) -> PdfFile:
        if self.pdf_file_queue:
            return self.pdf_file_queue.popleft()
        return None

    def set_status(self, pdf: PdfFile, status: PdfStatus) -> None:
        stored_pdf: PdfFile = self.pdf_files.get(pdf.pdf_id)
        stored_pdf.status = status
        self.pdf_files.update({pdf.pdf_id: pdf})

    def check_expiration(self) -> None:
        now_time: int = int(time())
        exp: int = self.expiration_time
        exp_files: list[PdfFile] = [
            pdf
            for pdf in self.pdf_files.values()
            if now_time < pdf.created + exp
        ]
        for file in exp_files:
            self.pdf_files.pop(file.pdf_id)

    def remove_pdf_from_dict(self, pdf_id: str) -> None:
        try:
            self.pdf_files.pop(pdf_id)
        except KeyError:
            return None

    def get_pdf_names(self) -> list[str]:
        return list(self.pdf_files.keys())
