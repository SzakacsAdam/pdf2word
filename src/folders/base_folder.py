from os import listdir
from os import mkdir
from os.path import isdir
from os.path import join


class BaseFolder:
    already_read: set = set()
    __slots__ = ("src", "folder_name", "folder_path")

    def __init__(self, src: str, folder_name: str) -> None:
        self.src: str = src
        self.folder_name: str = folder_name
        self.folder_path: str = join(src, folder_name)

        self.create_directory()

    def create_directory(self) -> None:
        if not isdir(self.folder_path):
            mkdir(self.folder_path)

    def get_file_names(self) -> list[str]:
        return [
            file
            for file in listdir(self.folder_path)
        ]

    def get_file_paths(self) -> list[str]:
        return [
            join(self.folder_path, file)
            for file in listdir(self.folder_path)
        ]

    def get_new_file_names(self) -> list[str]:
        new_files: list[str] = [
            file
            for file in listdir(self.folder_path)
            if file not in self.already_read
        ]
        self.already_read.update(new_files)
        return new_files

    def get_new_file_paths(self) -> list[str]:
        new_files: list[str] = [
            join(self.folder_path, file)
            for file in listdir(self.folder_path)
            if join(self.folder_path, file) not in self.already_read
        ]
        self.already_read.update(new_files)
        return new_files

    def clean_already_read(self) -> None:
        new_file_paths: list[str] = self.get_file_paths()
        to_remove_file: list[str] = [file_path for file_path in
                                     self.already_read
                                     if file_path not in new_file_paths]
        for file in to_remove_file:
            self.already_read.remove(file)
