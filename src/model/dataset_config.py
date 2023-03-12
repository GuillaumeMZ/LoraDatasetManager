import json
from pathlib import Path


class DatasetConfig:
    def __init__(self, config_file: Path):
        self._load_config(config_file)

    def _load_config(self, config_file: Path):
        with config_file.open() as file:
            contents = file.read()

        self._json = json.loads(contents)
        self.tags_groups = self._json["tags_groups"]