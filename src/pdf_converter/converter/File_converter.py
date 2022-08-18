from os.path import join
from time import sleep

import pythoncom
from PyPDF2 import PdfFileReader
from PyPDF2.errors import PdfReadError
from win32com.client import Dispatch

from src.folders import ErrorDir
from src.folders import BackUpPdf
from src.folders import OutputDir
from src.pdf_converter.folder_handlers import PdfFolders
from src.pdf_converter.file_types import PdfFile
from src.utils import RunThreaded


class FileConverter(RunThreaded):
    daemon: bool = True
    sleep_time: float = 10 ** -1

    __slots__ = (
        "av_doc", "av_doc_id", "pdf_folders", "error_dir", "backup_dir",
        "output_dir"
    )

    def __init__(self, av_doc_id, pdf_folders: PdfFolders, error_dir: ErrorDir,
                 backup_dir: BackUpPdf, output_dir: OutputDir):
        super().__init__()
        self.av_doc = None
        self.av_doc_id = av_doc_id

        self.pdf_folders = pdf_folders
        self.error_dir: ErrorDir = error_dir
        self.backup_dir: BackUpPdf = backup_dir
        self.output_dir: OutputDir = output_dir

    def __convert(self, pdf: PdfFile) -> bool:
        try:
            self.av_doc.Open(pdf.file_path, self.output_dir.folder_path)
            pd_doc = self.av_doc.GetPDDoc()
            j_object = pd_doc.GetJSObject()
            out_name: str = join(
                self.output_dir.folder_path,
                f"{pdf.file_name}.{pdf.pdf_convert_type}"
            )
            j_object.SaveAs(out_name,
                            f"com.adobe.acrobat.{pdf.pdf_convert_type}")
            pd_doc.Close()
            self.av_doc.Close(True)
        except AttributeError:
            return False
        else:
            return True

    @staticmethod
    def __is_valid_pdf(pdf: PdfFile) -> bool:
        try:
            with open(pdf.file_path, "rb") as file:
                PdfFileReader(file)
                return True
        except PdfReadError:
            return False

    def run(self) -> None:
        pythoncom.CoInitialize()
        self.av_doc = Dispatch(
            pythoncom.CoGetInterfaceAndReleaseStream(
                self.av_doc_id,
                pythoncom.IID_IDispatch
            )
        )

        while self.is_running:

            curr_pdf: PdfFile = self.pdf_folders.get_pdf_file()
            while curr_pdf is not None:
                print(f"{curr_pdf.file_name = }")
                if not self.__is_valid_pdf(curr_pdf):
                    self.error_dir.move_pdf(curr_pdf)
                    break

                if not self.__convert(curr_pdf):
                    self.error_dir.move_pdf(curr_pdf)
                    break

                self.backup_dir.move_pdf(curr_pdf)
                curr_pdf: PdfFile = self.pdf_folders.get_pdf_file()

            sleep(self.sleep_time)
