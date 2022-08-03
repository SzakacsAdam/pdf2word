from src.pdf_handler import PdfConvertType
from src.pdf_handler import PdfConvertedMimeType
from src.folder_handler.folders.folders_with_pdf.base_pdf_folder import BasePdfFolder


class FolderDocx(BasePdfFolder):
    folder_name: str = "pdf_to_docx"
    pdf_convert_type: PdfConvertType = PdfConvertType.WORD
    pdf_converted_mime_type: PdfConvertedMimeType = PdfConvertedMimeType.WORD

    def __init__(self, src: str) -> None:
        super().__init__(src, self.folder_name, self.pdf_convert_type,
                         self.pdf_converted_mime_type)
