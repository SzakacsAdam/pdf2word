from time import sleep

import pythoncom
from win32com.client import Dispatch
from win32com.client import DispatchEx
from win32com.client.dynamic import ERRORS_BAD_CONTEXT
from winerror import E_NOTIMPL

from src.pdf_converter.converter import FileConverter
from src.pdf_converter.folder_handlers import JunkCollector
from src.pdf_converter.folder_handlers import PdfFolders
from src.pdf_converter.folders import BackUpPdf
from src.pdf_converter.folders import ErrorDir
from src.pdf_converter.folders import FolderDocx
from src.pdf_converter.folders import FolderPptx
from src.pdf_converter.folders import FolderXlsx
from src.pdf_converter.folders import JunkDir
from src.pdf_converter.folders import OutputDir


class AcrobatConverter:
    src: str = "/test_dir"

    def __init__(self) -> None:
        pythoncom.CoInitialize()
        ERRORS_BAD_CONTEXT.append(E_NOTIMPL)
        # GenerateFromTypeLibSpec('Acrobat')
        adobe = DispatchEx('AcroExch.App')
        av_doc = Dispatch('AcroExch.AVDoc')
        av_doc_id = pythoncom.CoMarshalInterThreadInterfaceInStream(
            pythoncom.IID_IDispatch, av_doc)

        src: str = self.src
        self.folder_docx: FolderDocx = FolderDocx(src)
        self.folder_xlsx: FolderXlsx = FolderXlsx(src)
        self.folder_pptx: FolderPptx = FolderPptx(src)

        # output project_folders
        self.backup_dir: BackUpPdf = BackUpPdf(src)
        self.error_dir: ErrorDir = ErrorDir(src)
        self.junk_dir: JunkDir = JunkDir(src)
        self.output_dir: OutputDir = OutputDir(src)

        print(self.folder_docx)

        self.pdf_folders: PdfFolders = PdfFolders(
            (self.folder_docx, self.folder_xlsx, self.folder_pptx))

        self.junk_collector: JunkCollector = JunkCollector(self.pdf_folders,
                                                           self.junk_dir.folder_path)

        self.pdf_converter: FileConverter = FileConverter(av_doc_id=av_doc_id,
                                                          pdf_folders=self.pdf_folders,
                                                          error_dir=self.error_dir,
                                                          backup_dir=self.backup_dir,
                                                          output_dir=self.output_dir)

    def start_converter(self) -> None:
        self.pdf_folders.start()
        self.junk_collector.start()
        self.pdf_converter.start()

    def run(self) -> None:
        sleep_time: int = 2  # sec*min
        self.start_converter()
        while True:
            sleep(sleep_time)


if __name__ == '__main__':
    main: NewMain = NewMain()
    main.run()
