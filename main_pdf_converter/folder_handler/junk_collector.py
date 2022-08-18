from os.path import join
from time import sleep

from .pdf_folders import PdfFolders
from src.main_pdf_converter.pdf_handler.junk_file import JunkFile
from src.utils import RunThreaded
from src.utils import move_file, move_dir


class JunkCollector(RunThreaded):
    __slots__ = ("pdf_folders", "junk_dir_path")

    def __init__(self, pdf_folders: PdfFolders, junk_dir_path: str):
        super().__init__()
        self.pdf_folders: PdfFolders = pdf_folders
        self.junk_dir_path: str = junk_dir_path

    def run(self) -> None:
        sleep_time: float = 10.0
        while self.is_running:
            curr_junk: JunkFile = self.pdf_folders.get_junk_file()
            while curr_junk is not None:
                src: str = curr_junk.file_path
                dest: str = join(self.junk_dir_path,
                                 curr_junk.file_name)
                if curr_junk.isfile:
                    move_file(src, dest)
                else:
                    move_dir(src, dest)

                curr_junk: JunkFile = self.pdf_folders.get_junk_file()

            sleep(sleep_time)
