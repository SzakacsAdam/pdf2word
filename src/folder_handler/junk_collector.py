from os import remove
from os.path import isfile
from shutil import copyfile
from shutil import copytree
from shutil import rmtree
from time import sleep

from src.utils import wait_until_file_moved
from src.utils import wait_until_folder_moved
from .folders import FolderDocx
from .folders import FolderPptx
from .folders import FolderXlsx
from .folders import JunkFiles
from .run_threaded import RunThreaded


class JunkCollector(RunThreaded):

    def __init__(self, src: str):
        super().__init__()
        self.junk_files: JunkFiles = JunkFiles(src)
        self.folder_docx: FolderDocx = FolderDocx(src)
        self.folder_xlsx: FolderXlsx = FolderXlsx(src)
        self.folder_pptx: FolderPptx = FolderPptx(src)
        self.to_move_junk: tuple = (
            self.folder_docx, self.folder_xlsx, self.folder_pptx
        )

    def collect_junk(self) -> None:
        dest_dir: str = self.junk_files.folder_path
        for folder in self.to_move_junk:
            for junk in folder.get_junk_files():
                if isfile(junk):
                    wait_until_file_moved(junk)
                    copyfile(junk, dest_dir)
                    remove(junk)
                else:
                    wait_until_folder_moved(junk)
                    copytree(junk, dest_dir)
                    rmtree(junk, ignore_errors=True)

    def run(self) -> None:
        sleep_time: int = 10
        while True:
            self.collect_junk()
            sleep(sleep_time)
