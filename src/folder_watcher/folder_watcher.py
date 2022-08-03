from collections import deque
from os import listdir
from os.path import join
from threading import Thread
from time import sleep

from .junk_collector import JunkCollector
from .util import sha1_hash
from .util import wait_until_file_moved
from ..pdf_handler import PdfContainer
from ..pdf_handler import PdfConvertType
from ..pdf_handler import PdfFile


class FolderWatcher(Thread):
    daemon: bool = True
    prefix: str = "pdf_to_"
    suffixes: tuple[str] = tuple([e.value for e in PdfConvertType])
    supported_format: str = "pdf"
    temp_read_files: set = set()
    junk_container: deque = deque()

    __slots__ = ("src", "container", "junk_collector")

    def __init__(self, src: str, container: PdfContainer):
        super().__init__()
        self.src: str = src
        self.container: PdfContainer = container
        self.junk_collector: JunkCollector = JunkCollector(src=src,
                                                           junk_container=self.junk_container)
        self.junk_collector.start()

    def read_dir(self, suffix: str) -> list[str]:
        curr_dir_name: str = f"{self.prefix}{suffix}"
        dir_path: str = join(self.src, curr_dir_name)
        return [
            join(dir_path, file) for file in listdir(dir_path)
        ]

    def clear_temp_file_name_holder(self) -> None:
        dir_contents: list[list[str]] = [self.read_dir(suffix)
                                         for suffix in self.suffixes]
        # unpacking nested list to list
        dir_content: list[str] = [inner
                                  for outer in dir_contents
                                  for inner in outer]

        files_to_remove: list[str] = [item
                                      for item in self.temp_read_files
                                      if item not in dir_content
                                      ]
        for set_item in files_to_remove:
            self.temp_read_files.remove(set_item)

    def add_new_files(self) -> None:
        for suffix in self.suffixes:
            dir_content: list[str] = self.read_dir(suffix)
            for file_path in dir_content:
                wait_until_file_moved(file_path)
                if file_path.endswith(self.supported_format):
                    if file_path not in self.temp_read_files:
                        pdf_id: str = sha1_hash(file_path)
                        pdf_convert_type: PdfConvertType = PdfConvertType(
                            suffix)
                        pdf: PdfFile = PdfFile(pdf_id=pdf_id,
                                               file_path=file_path,
                                               pdf_convert_type=pdf_convert_type)
                        self.container.add_pdf(pdf)
                        self.temp_read_files.add(file_path)
                else:
                    self.junk_container.append(file_path)

    def run(self) -> None:
        sleep_time: float = 10 ** -2
        while True:
            self.add_new_files()
            self.clear_temp_file_name_holder()
            sleep(sleep_time)
