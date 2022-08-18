from os import remove
from os.path import getmtime
from os.path import isfile
from os.path import join
from shutil import rmtree
from time import time

from ..base_folder import BaseFolder
from src.pdf_converter.file_types import PdfFile
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

    def move_pdf(self, pdf: PdfFile) -> None:
        src: str = pdf.file_path
        dest: str = join(self.folder_path, pdf.file_name)
        move_file(src, dest)

    @property
    def remove_time(self) -> int:
        return self._remove_time

    @remove_time.setter
    def remove_time(self, sec_time: int) -> None:
        if self._min_remove_delay < sec_time:
            self._remove_time: int = sec_time
        else:
            self._remove_time: int = self._min_remove_delay
