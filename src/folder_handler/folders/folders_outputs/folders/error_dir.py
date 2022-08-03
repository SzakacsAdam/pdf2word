from src.folder_handler.folders.folders_outputs.base_output_folder import \
    BaseOutputFolder


class ErrorDir(BaseOutputFolder):
    folder_name: str = "error_dir"

    def __init__(self, src: str):
        super().__init__(src, self.folder_name)
