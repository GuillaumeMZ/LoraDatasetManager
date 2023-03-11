from pathlib import Path
from src.model.dataset_config import DatasetConfig
from src.model.concept import Concept
from src.model.dataset_image import DatasetImage


class Dataset:
    def __init__(self, path: Path, config: DatasetConfig, concepts: list[Concept], images: list[DatasetImage]):
        self.path = path
        self.config = config
        self.concepts = concepts
        self.images = images
