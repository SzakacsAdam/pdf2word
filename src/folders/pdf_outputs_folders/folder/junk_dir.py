from ..base_output_folder import BaseOutputFolder


class JunkDir(BaseOutputFolder):
    folder_name: str = "junk_files"

    def __init__(self, src: str):
        super().__init__(src, self.folder_name)
