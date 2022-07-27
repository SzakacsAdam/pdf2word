class ConfigReader:
    config: dict[str, str | int] = dict()

    __slots__ = "config_path"

    def __init__(self, config_path: str):
        self.config_path: str = config_path
