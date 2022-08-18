from time import sleep

from src.pdf_converter.file_types import PdfFile
from src.pdf_converter.file_types import JunkFile
from src.utils import RunThreaded


class PdfFolders(RunThreaded):
    __slots__ = "project_folders"

    def __init__(self, folders: tuple) -> None:
        super().__init__()

        self.folders: tuple = folders

    def get_pdf_file(self) -> PdfFile | None:
        for folder in self.folders:
            pdf_file = folder.get_pdf_file()
            if pdf_file is not None:
                return pdf_file
        return None

    def get_junk_file(self) -> JunkFile | None:
        for folder in self.folders:
            junk_file = folder.get_junk_file()
            if junk_file is not None:
                return junk_file
        return None

    def collect_files(self) -> None:
        for folder in self.folders:
            folder.read_folder()

    def clean_already_read(self) -> None:
        for folder in self.folders:
            folder.clean_already_read()

    def run(self) -> None:
        sleep_time: float = 1.0
        rem_counter: int = 0
        while self.is_running:
            self.collect_files()
            if rem_counter <= 10:
                rem_counter = 0
                # self.clean_already_read()

            sleep(sleep_time)
            rem_counter += 1
