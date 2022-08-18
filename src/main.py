from src.folders import BackUpPdf
from src.folders import ErrorDir
from src.folders import FolderDocx
from src.folders import FolderPptx
from src.folders import FolderXlsx
from src.folders import JunkDir
from src.folders import OutputDir

from src.pdf_converter import AcrobatConverter


class Main:
    src: str = "F:\\pythonProjects\\newPdf2Word\\test_dir"

    def __init__(self) -> None:
        self.acrobat_converter: AcrobatConverter = AcrobatConverter()

        src: str = self.src
        self.folder_docx: FolderDocx = FolderDocx(src)
        self.folder_xlsx: FolderXlsx = FolderXlsx(src)
        self.folder_pptx: FolderPptx = FolderPptx(src)

        # output project_folders
        self.backup_dir: BackUpPdf = BackUpPdf(src)
        self.error_dir: ErrorDir = ErrorDir(src)
        self.junk_dir: JunkDir = JunkDir(src)
        self.output_dir: OutputDir = OutputDir(src)

        pdf_read_folders: tuple = (self.folder_docx, self.folder_xlsx,
                                   self.folder_pptx)
        pdf_output_folders: dict = {"error_dir": self.error_dir,
                                    "backup_dir": self.backup_dir,
                                    "output_dir": self.output_dir}

    def start(self) -> None:
        self.acrobat_converter.run()


if __name__ == '__main__':
    main: Main = Main()
    main.start()
