from os import listdir
from os.path import join
from os.path import isdir
from os import mkdir


class BaseFolder:
    already_read: set = set()

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

    def clean_already_read(self) -> None:
        files: list[str] = self.get_file_names()
        to_remove_file: list[str] = [set_file for set_file in self.already_read if set_file not in files]
        for file in to_remove_file:
            self.already_read.remove(file)

