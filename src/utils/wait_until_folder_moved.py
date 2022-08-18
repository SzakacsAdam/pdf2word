from os import scandir
from os import walk
from time import sleep


def wait_until_folder_moved(folder_path: str) -> None:
    sleep_time: float = 10 ** -2
    files_num: int = calc_files_in_dir(folder_path)
    dir_size: int = get_dir_size(folder_path)
    new_files_num: int = -1
    new_dir_size: int = -1
    while not all([files_num == new_files_num, dir_size == new_dir_size]):
        new_files_num: int = calc_files_in_dir(folder_path)
        new_dir_size: int = get_dir_size(folder_path)

        files_num, new_files_num = new_files_num, files_num
        dir_size, new_dir_size = new_dir_size, dir_size
        sleep(sleep_time)


def calc_files_in_dir(folder_path: str) -> int:
    return sum([
        len(files) for _, _, files in walk(folder_path)
    ])


def get_dir_size(folder_path: str) -> int:
    total: int = 0
    with scandir(folder_path) as it:
        for entry in it:
            if entry.is_file():
                total += entry.stat().st_size
            elif entry.is_dir():
                total += get_dir_size(entry.path)
    return total
