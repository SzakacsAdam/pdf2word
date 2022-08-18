from os import remove
from os.path import getmtime
from os.path import join
from os.path import isfile
from shutil import rmtree
from time import time

from src.main_pdf_converter.project_folders.base_folder import BaseFolder
from src.main_pdf_converter.pdf_handler import PdfFile
from src.utils import move_file


class BaseOutputFolder(BaseFolder):
    _remove_time: int = None
    _min_remove_delay: int = 60 * 60 + 60

    def __init__(self, src: str, folder_name: str):
        super().__init__(src, folder_name)

    def remove_old_files(self) -> None:
        curr_time: int = int(time())
        files: list[str] = self.get_file_paths()
        for file in files:
            file_last_modified: int = int(getmtime(file))
            if curr_time < file_last_modified + self.remove_time:
                if isfile(file):
                    remove(file)
                else:
                    rmtree(file)

    @property
    def remove_time(self) -> int:
        return self._remove_time

    @remove_time.setter
    def remove_time(self, sec_time: int) -> None:
        self._remove_time = sec_time

    def move_pdf(self, pdf: PdfFile) -> None:
        src: str = pdf.file_path
        dest: str = join(self.folder_path, pdf.file_name)
        move_file(src, dest)
