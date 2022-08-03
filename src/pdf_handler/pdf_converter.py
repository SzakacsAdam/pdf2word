from os import remove
from os.path import join
from shutil import copyfile
from threading import Thread
from time import sleep

import pythoncom
from PyPDF2 import PdfFileReader
from PyPDF2.errors import PdfReadError
from win32com.client import Dispatch

from .pdf_container import PdfContainer
from .pdf_file import PdfFile


class PdfConverter(Thread):
    daemon: bool = True
    sleep_time: float = 10 ** -1
    out_dir_name: str = "output_dir"
    backup_dir_name: str = "backup"

    __slots__ = ("av_doc", "av_doc_id", "container", "backup", "out")

    def __init__(self, av_doc_id, container: PdfContainer, src: str):
        super().__init__()
        self.av_doc = None
        self.av_doc_id = av_doc_id
        self.container: PdfContainer = container
        self.backup: str = join(src, self.out_dir_name)
        self.out: str = join(src, self.out_dir_name)

    def __convert(self, pdf: PdfFile) -> None:
        self.av_doc.Open(pdf.file_path, self.out)
        pd_doc = self.av_doc.GetPDDoc()
        j_object = pd_doc.GetJSObject()
        out_name: str = join(self.out,
                             f"{pdf.pdf_id}.{pdf.pdf_convert_type.value}")
        j_object.SaveAs(out_name,
                        f"com.adobe.acrobat.{pdf.pdf_convert_type.value}")
        pd_doc.Close()
        self.av_doc.Close(True)

    def __clean_up_after_convert(self, pdf: PdfFile) -> None:
        dest_dir: str = join(self.backup, pdf.file_name)
        copyfile(pdf.file_path, dest_dir)
        remove(pdf.file_path)
        pdf.file_path = dest_dir

    @staticmethod
    def __pdf_validator(pdf: PdfFile) -> bool:
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
        while True:
            curr_pdf: PdfFile = self.container.get_next_item()
            if curr_pdf is not None:
                self.__convert(curr_pdf)
            sleep(self.sleep_time)
