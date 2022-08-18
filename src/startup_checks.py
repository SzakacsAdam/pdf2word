from collections import deque
from os import system
from sys import getwindowsversion
from sys import platform

from win32com.client import DispatchEx
from win32com.client.dynamic import ERRORS_BAD_CONTEXT
from win32com.client.makepy import GenerateFromTypeLibSpec
from winerror import E_NOTIMPL


class StartupChecks:
    check_list: deque = deque()

    def __init__(self) -> None:
        pass

    def run(self) -> bool:
        self.check_list.append(self.check_acrobat())
        self.check_list.append(self.check_os())

        return all(self.check_list)

    @staticmethod
    def check_acrobat() -> bool:
        ERRORS_BAD_CONTEXT.append(E_NOTIMPL)
        GenerateFromTypeLibSpec('Acrobat')
        av_doc = DispatchEx('AcroExch.AVDoc')
        av_doc.Close(True)
        acrobat_close = system('taskkill /f /t /im Acrobat.exe')
        return True if acrobat_close == 0 else False

    @staticmethod
    def check_os() -> bool:
        if platform == "win32":
            if getwindowsversion()[0] == 10:
                return True
        return False
