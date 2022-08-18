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
        self.config_dict["src"] = self.__read_str("CONVERTER", "base.path",
                                                  getcwd())
        self.read_remove_time("backup")
        self.read_remove_time("junk_files")
        self.read_remove_time("output")
        self.read_remove_time("error")

    def read_remove_time(self, prefix: str) -> None:
        self.config_dict[f"{prefix}_rem_time"] = None
        if self.__read_bool("CONVERTER", f"{prefix}.remove", False):
            self.config_dict[f"{prefix}_rem_time"] = int(self.day_to_sec *
                self.__read_float("CONVERTER", f"{prefix}.remove.time", 1))

    def __read_str(self, section: str, propagate: str,
                   default: str) -> str:
        try:
            return self.config[section][propagate]
        except KeyError:
            return default

    def __read_int(self, section: str, propagate: str,
                   default: int) -> int:
        try:
            return int(self.config[section][propagate])
        except KeyError or ValueError:
            return default

    def __read_float(self, section: str, propagate: str,
                     default: float) -> float:
        try:
            return float(self.config[section][propagate])
        except KeyError or ValueError:
            return default

    def __read_bool(self, section: str, propagate: str,
                    default: bool) -> bool:
        truthy: tuple[str, str, str] = ("True", "true", "yes")
        try:
            val: str = self.config[section][propagate]
            return val in truthy
        except KeyError:
            return default

    def create_example_config(self) -> None:
        conf_path: str = join(self.cwd, self.example_config_filename)
        try:
            with open(conf_path, "w+") as conf_file:
                conf_file.write(config_example)
        except OSError as err:
            return
