from pathlib import Path
from src.model.dataset_config import DatasetConfig
from src.model.concept import Concept
from src.model.dataset_image import DatasetImage


class Dataset:
    def __init__(self, path: Path, config: DatasetConfig, concepts: list[Concept], images: list[DatasetImage]):
        self.path = path
        self.config = config
        self.concepts = concepts

        self.images: list[DatasetImage] = []
        self.duplicated_images: list[DatasetImage] = []

        # Add and dedup the images
        for image in images:
            self.add_image(image)

    # Recognized image formats by Kohya's sd-scripts
    ALLOWED_IMAGE_FORMATS = ['.png', '.jpg', '.jpeg', '.webp']

    # Two images' hashes having a hamming distance less or equal to this threshold are considered to be identical
    _EQUALITY_DISTANCE_THRESHOLD = 10

    def add_image(self, image_to_add: DatasetImage):
        if any(image.cached_hash - image_to_add.cached_hash <= Dataset._EQUALITY_DISTANCE_THRESHOLD
               for image in self.images):
            self.duplicated_images.append(image_to_add)
        else:
            self.images.append(image_to_add)
