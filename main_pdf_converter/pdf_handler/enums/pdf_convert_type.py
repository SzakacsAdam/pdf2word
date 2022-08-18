from enum import Enum


class PdfConvertType(Enum):
    WORD: str = "docx"
    EXCEL: str = "xlsx"
    POWERPOINT: str = "pptx"
    JPEG: str = "jpeg"
