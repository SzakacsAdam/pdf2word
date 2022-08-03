from enum import Enum


class PdfConvertedMimeType(Enum):
    WORD: str = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    EXCEL: str = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    POWERPOINT: str = "application/vnd.openxmlformats-officedocument.presentationml.presentation"
    JPEG: str = "image/jpeg"
