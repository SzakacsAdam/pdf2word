from src.main_pdf_converter.pdf_handler import PdfConvertType
from src.main_pdf_converter.pdf_handler import PdfConvertedMimeType
from src.main_pdf_converter.project_folders.folders_with_pdf.base_pdf_folder import BasePdfFolder


class FolderPptx(BasePdfFolder):
    folder_name: str = "pdf_to_pptx"
    pdf_convert_type: PdfConvertType = PdfConvertType.POWERPOINT
    pdf_converted_mime_type: PdfConvertedMimeType = PdfConvertedMimeType.POWERPOINT

    def __init__(self, src: str) -> None:
        super().__init__(src, self.folder_name, self.pdf_convert_type,
                         self.pdf_converted_mime_type)
