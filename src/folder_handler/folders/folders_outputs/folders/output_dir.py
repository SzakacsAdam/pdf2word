from src.folder_handler.folders.folders_outputs.base_output_folder import \
    BaseOutputFolder


class OutputDir(BaseOutputFolder):
    folder_name: str = "output_dir"

    def __init__(self, src: str,):
        super().__init__(src, self.folder_name)

    @property
    def remove_time(self) -> int:
        return self._remove_time

    @remove_time.setter
    def remove_time(self, sec_time: int) -> None:
        min_delay: int = 60 * 60 + 60
        sec: int = sec_time if min_delay < sec_time else min_delay
        self._remove_time = sec
