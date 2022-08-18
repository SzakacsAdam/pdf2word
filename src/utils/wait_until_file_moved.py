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
