from .pdf_convert_types import PdfConvertTypes
from os.path import join


class Pdf:
    __slots__ = ("file_name", "pdf_convert_type")

    def __init__(self, file_name: str,
                 pdf_convert_type: PdfConvertTypes = PdfConvertTypes.WORD):
        self.file_name: str = file_name
        self.pdf_convert_type: PdfConvertTypes = pdf_convert_type
