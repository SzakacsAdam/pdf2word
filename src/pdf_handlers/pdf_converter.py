from os.path import join

from PyPDF2 import PdfFileReader
from PyPDF2.errors import PdfReadError
from win32com.client import DispatchEx
from win32com.client.dynamic import ERRORS_BAD_CONTEXT
from win32com.client.makepy import GenerateFromTypeLibSpec
from winerror import E_NOTIMPL

from .pdf import Pdf


class PdfConverter:
    __slots__ = ("src_dir", "out_dir")

    def __init__(self, src_dir: str, out_dir: str) -> None:
        self.src_dir: str = src_dir
        self.out_dir: str = out_dir

    def convert(self, pdf: Pdf) -> None:
        pdf_src: str = join(self.src_dir, pdf.file_name)
        pdf_out: str = join(self.out_dir, pdf.file_name)
        save_format: str = pdf.pdf_convert_type.value

        if self.__pdf_validator(pdf_src):
            self.__convert_acrobat(pdf_src=pdf_src, pdf_out=pdf_out,
                                   save_format=save_format)

    @staticmethod
    def __pdf_validator(pdf_src: str) -> bool:
        try:
            with open(pdf_src, "rb") as file:
                PdfFileReader(file)
                return True
        except PdfReadError:
            return False

    @staticmethod
    def __convert_acrobat(pdf_src: str, pdf_out,
                          save_format: str) -> None:

        ERRORS_BAD_CONTEXT.append(E_NOTIMPL)
        GenerateFromTypeLibSpec('Acrobat')
        adobe = DispatchEx('AcroExch.App')
        av_doc = DispatchEx('AcroExch.AVDoc')
        av_doc.Open(pdf_src, pdf_out)
        pd_doc = av_doc.GetPDDoc()
        j_object = pd_doc.GetJSObject()
        j_object.SaveAs(pdf_out, f"com.adobe.acrobat.{save_format}")
        pd_doc.Close()
        av_doc.Close(True)
