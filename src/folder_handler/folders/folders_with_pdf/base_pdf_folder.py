from os import listdir
from os.path import join

from src.pdf_handler import PdfConvertType
from src.pdf_handler import PdfConvertedMimeType
from src.pdf_handler import PdfFile
from src.utils import sha1_hash
from src.utils import wait_until_file_moved
from ..base_folder import BaseFolder


class BasePdfFolder(BaseFolder):
    supported_format: str = "pdf"

    def __init__(self, src: str, folder_name: str,
                 pdf_convert_type: PdfConvertType,
                 pdf_converted_mime_type: PdfConvertedMimeType) -> None:
        super().__init__(src, folder_name)
        self.pdf_convert_type: PdfConvertType = pdf_convert_type
        self.pdf_converted_mime_type: PdfConvertedMimeType = pdf_converted_mime_type

    def new_pdf_files(self) -> list[PdfFile]:
        new_pdf_files: list[PdfFile] = []
        for file in self.get_new_file_names():
            file_path: str = join(self.folder_path, file)
            wait_until_file_moved(file_path)
            if file.endswith(self.supported_format):
                pdf_id: str = sha1_hash(file_path)
                pdf: PdfFile = PdfFile(pdf_id=pdf_id, file_path=file_path,
                                       pdf_convert_type=self.pdf_convert_type,
                                       pdf_converted_mime_type=self.pdf_converted_mime_type)
                new_pdf_files.append(pdf)
        return new_pdf_files

    def get_junk_files(self) -> list[str]:
        return [
            join(self.folder_path, file)
            for file in listdir(self.folder_path)
            if not file.endswith(self.supported_format)
        ]
