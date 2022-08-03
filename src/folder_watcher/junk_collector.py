from collections import deque
from os import remove
from os import sep
from os.path import isfile
from os.path import join
from shutil import copyfile
from shutil import copytree
from shutil import rmtree
from threading import Thread
from time import sleep


class JunkCollector(Thread):
    junk_dir_name: str = "junk_files"

    __slots__ = ("junk_container", "junk_dir")

    def __init__(self, src: str, junk_container: deque) -> None:
        super().__init__()
        self.junk_container: deque = junk_container
        self.junk_dir: str = join(src, self.junk_dir_name)

    def rem_move_junk(self) -> None:
        while self.junk_container:
            curr_junk: str = self.junk_container.popleft()
            junk_name: str = curr_junk.split(sep)[-1]
            if isfile(curr_junk):
                dest_dir: str = join(self.junk_dir, junk_name)
                copyfile(curr_junk, dest_dir)
                remove(curr_junk)
            else:
                dest_dir: str = join(self.junk_dir, junk_name)
                copytree(curr_junk, dest_dir)
                rmtree(curr_junk, ignore_errors=True)

    def run(self) -> None:
        sleep_time: float = 10.0
        while True:
            self.rem_move_junk()
            sleep(sleep_time)
