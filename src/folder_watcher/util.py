from hashlib import sha1
from time import sleep


def wait_until_file_moved(file_path: str) -> None:
    sleep_time: float = 10 ** -2
    is_moved: bool = False
    while not is_moved:
        try:
            with open(file_path, "rb") as _:
                pass
            is_moved = True
        except PermissionError:
            sleep(sleep_time)


def sha1_hash(file_path: str) -> str:
    block_size: int = 128
    h = sha1()
    with open(file_path, "rb") as file:
        while chunk := file.read(block_size * h.block_size):
            h.update(chunk)
    return h.hexdigest()
