from ..base_output_folder import BaseOutputFolder


class OutputDir(BaseOutputFolder):
    folder_name: str = "output_dir"

    def __init__(self, src: str, ):
        super().__init__(src, self.folder_name)

