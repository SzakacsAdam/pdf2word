from ..base_pdf_folder import BasePdfFolder


class FolderPptx(BasePdfFolder):
    pdf_convert_type: str = "pptx"
    folder_name: str = f"pdf_to_{pdf_convert_type}"

    def __init__(self, src: str) -> None:
        super().__init__(src, self.folder_name, self.pdf_convert_type)
