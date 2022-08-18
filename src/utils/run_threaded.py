from threading import Thread


class RunThreaded(Thread):
    daemon: bool = True
    is_running: bool = True

    def __init__(self) -> None:
        super().__init__()
