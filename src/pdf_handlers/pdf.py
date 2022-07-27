from .pdf_convert_type import PdfConvertType
from os.path import join


class Pdf:
    __slots__ = ("file_name", "pdf_convert_type")

    def __init__(self, file_name: str,
                 pdf_convert_type: PdfConvertType = PdfConvertType.WORD):
        self.file_name: str = file_name
        self.pdf_convert_type: PdfConvertType = pdf_convert_type
