from time import sleep

from src.pdf_handler import PdfContainer
from .folders import FolderDocx
from .folders import FolderPptx
from .folders import FolderXlsx
from .run_threaded import RunThreaded


class FolderWatcher(RunThreaded):

    def __init__(self, src: str, container: PdfContainer):
        super().__init__()
        self.src: str = src
        self.container: PdfContainer = container
        self.watch_folders: tuple = (
            FolderDocx(src), FolderXlsx(src), FolderPptx(src)
        )

    def add_new_pdfs(self) -> None:
        for folder in self.watch_folders:
            for pdf in folder.new_pdf_files():
                self.container.add_pdf(pdf)
            folder.clean_already_read()

    def run(self) -> None:
        sleep_time: int = 10 ** -2
        while self.is_running:
            self.add_new_pdfs()
            sleep(sleep_time)
