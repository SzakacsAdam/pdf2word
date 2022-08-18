from src.main_pdf_converter.project_folders.folders_outputs.base_output_folder import \
    BaseOutputFolder


class OutputDir(BaseOutputFolder):
    folder_name: str = "output_dir"

    def __init__(self, src: str, ):
        super().__init__(src, self.folder_name)

    @property
    def remove_time(self) -> int:
        return self._remove_time

    @remove_time.setter
    def remove_time(self, sec_time: int) -> None:
        self._remove_time: int = sec_time \
            if self._min_remove_delay < sec_time \
            else self._min_remove_delay
