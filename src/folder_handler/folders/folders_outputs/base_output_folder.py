from os import remove
from os.path import getmtime
from os.path import isfile
from shutil import rmtree
from time import time

from src.folder_handler.folders.base_folder import BaseFolder


class BaseOutputFolder(BaseFolder):
    _remove_time: int = None

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
