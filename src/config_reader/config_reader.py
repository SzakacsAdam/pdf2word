
import sys
from configparser import ConfigParser
from os import getcwd
from os.path import isfile
from os.path import join

from .config_example import config_example


class ConfigReader:
    config_filename: str = "config.ini"
    example_config_filename: str = "config_example.ini"
    config: ConfigParser = ConfigParser()
    config_dict: dict = dict()
    day_to_sec: int = 60 * 60 * 24

    def __init__(self):
        self.cwd: str = getcwd()
        self.conf_path: str = join(self.cwd, self.config_filename)
        if not isfile(self.conf_path):
            self.create_example_config()
            sys.exit()
        self.config.read(self.conf_path)

        self.read_config_file()
        print(self.config_dict)

    def read_config_file(self) -> None:
        self.config_dict["src"] = self.__read_parser(str, "CONVERTER",
                                                     "base.path",
                                                     getcwd())
        self.__read_remove_time("backup")
        self.__read_remove_time("junk_files")
        self.__read_remove_time("output")
        self.__read_remove_time("error")

    def __read_remove_time(self, prefix: str) -> None:
        self.config_dict[f"{prefix}_rem_time"] = None
        if self.__read_parser(bool, "CONVERTER", f"{prefix}.remove", False):
            conf_read: float = self.__read_parser(float, "CONVERTER",
                                                  f"{prefix}.remove.time", 1)
            conf_read_to_day: int = int(self.day_to_sec * conf_read)
            self.config_dict[f"{prefix}_rem_time"] = conf_read_to_day

    def __read_parser(self, convert_type: callable, section: str,
                      propagate: str, default: str | bool | float | int) \
            -> str | bool | float | int:
        try:
            return convert_type(self.config[section][propagate])
        except KeyError or ValueError:
            return default

    def create_example_config(self) -> None:
        conf_path: str = join(self.cwd, self.example_config_filename)
        try:
            with open(conf_path, "w+") as conf_file:
                conf_file.write(config_example)
        except OSError as err:
            return
