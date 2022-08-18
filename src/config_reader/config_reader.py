from configparser import ConfigParser
from os import getcwd
from os.path import join

from .config_example import config_example


class ConfigReader:
    config_filename: str = "config.ini"
    example_config_filename: str = "config_example.ini"
    config: ConfigParser = ConfigParser()

    def __init__(self):
        self.cwd: str = getcwd()

    def create_example_config(self) -> None:
        conf_path: str = join(self.cwd, self.example_config_filename)
        try:
            with open(conf_path, "w+") as conf_file:
                conf_file.write(config_example)
        except OSError as err:
            return
