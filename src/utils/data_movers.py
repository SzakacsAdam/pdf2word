from os import remove
from shutil import copyfile
from shutil import copytree
from shutil import rmtree
from time import sleep

from .wait_until import wait_to_remove
from .wait_until import wait_until_file_moved
from .wait_until import wait_until_folder_moved


def move_dir(src: str, dest: str) -> None:
    wait_until_folder_moved(src)
    copytree(src, dest)
    rmtree(src)


def move_file(src: str, dest: str) -> None:
    wait_until_file_moved(src)
    copyfile(src, dest)
    wait_to_remove(src)


def copy_file(src: str, dest: str) -> None:
    copyfile(src, dest)


def remove_file(src: str) -> None:
    sleep_time: int = 10 ** -2
    is_removed: bool = False
    while not is_removed:
        try:
            remove(src)

        except PermissionError:
            pass
        except FileNotFoundError:
            pass

        else:
            is_removed = True
        finally:
            sleep(sleep_time)
