from os import listdir
from os import remove
from os.path import getmtime
from os.path import isfile
from os.path import join
from shutil import rmtree
from time import sleep
from time import time

from src.main_pdf_converter.project_folders import BackUpPdf
from src.main_pdf_converter.project_folders import ErrorDir
from src.main_pdf_converter.project_folders import JunkFiles
from src.main_pdf_converter.project_folders import OutputDir
from src.utils.run_threaded import RunThreaded


class ExpiredFileRemover(RunThreaded):

    def __init__(self, src: str, conf: dict) -> None:
        super().__init__()

        self.backup_pdf: BackUpPdf = BackUpPdf(src)
        self.backup_pdf.remove_time = conf[self.backup_pdf.folder_name]

        self.error_dir: ErrorDir = ErrorDir(src)
        self.error_dir.remove_time = conf[self.error_dir.folder_name]

        self.junk_files: JunkFiles = JunkFiles(src)
        self.junk_files.remove_time = conf[self.junk_files.folder_name]

        self.output_dir: OutputDir = OutputDir(src)
        self.output_dir.remove_time = conf[self.output_dir.folder_name]

        self.folders: tuple = (
            self.backup_pdf, self.error_dir, self.junk_files, self.output_dir
        )

    def remove_old_files(self) -> None:
        curr_time: int = int(time())
        for folder in self.folders:
            exp_time: int = folder.remove_time
            if exp_time is None:
                continue
            folder_path: str = folder.folder_path
            for file in listdir(folder_path):
                file_path: str = join(folder_path, file)
                file_age: int = int(getmtime(file_path))
                if curr_time < file_age + exp_time:
                    if isfile(file_path):
                        remove(file_path)
                    else:
                        rmtree(file_path)

    def run(self) -> None:
        sleep_time: int = 60
        while self.is_running:
            self.remove_old_files()
            sleep(sleep_time)
