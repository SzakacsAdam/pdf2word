from time import sleep

import pythoncom
from win32com.client import Dispatch
from win32com.client import DispatchEx
from win32com.client.dynamic import ERRORS_BAD_CONTEXT
from winerror import E_NOTIMPL

from src.folder_handler import FolderWatcher
from src.pdf_handler import PdfContainer
from src.pdf_handler.pdf_converter import PdfConverter


class Main:
    src: str = "F:\\pythonProjects\\newPdf2Word\\test_dir"

    expiration_time: int = 60 * 60  # sec*min
    container: PdfContainer = PdfContainer()

    def __init__(self) -> None:
        pythoncom.CoInitialize()
        ERRORS_BAD_CONTEXT.append(E_NOTIMPL)
        # GenerateFromTypeLibSpec('Acrobat')
        adobe = DispatchEx('AcroExch.App')
        av_doc = Dispatch('AcroExch.AVDoc')
        av_doc_id = pythoncom.CoMarshalInterThreadInterfaceInStream(
            pythoncom.IID_IDispatch, av_doc)

        self.folder_watcher: FolderWatcher = FolderWatcher(src=self.src,
                                                           container=self.container)
        self.pdf_convert: PdfConverter = PdfConverter(av_doc_id=av_doc_id,
                                                      container=self.container,
                                                      src=self.src)

    def start_converter(self) -> None:
        self.folder_watcher.start()
        self.pdf_convert.start()

    def run(self) -> None:
        sleep_time: int = 60 * 2  # sec*min
        while True:
            self.container.check_expiration()
            sleep(sleep_time)


if __name__ == '__main__':
    main: Main = Main()
    main.run()
