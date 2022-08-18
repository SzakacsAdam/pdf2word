from os import sep
from os.path import isfile


class JunkFile:
    def __init__(self, file_path: str) -> None:
        self.file_path: str = file_path
        self.file_name: str = file_path.split(sep)[-1]
        self.isfile: bool = isfile(file_path)
