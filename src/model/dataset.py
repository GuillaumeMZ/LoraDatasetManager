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

        # Used to store the duplicated images. The first element of the tuple is the duplicated image itself,
        # the second is the image it is a duplicate of.
        self.duplicated_images: list[tuple[DatasetImage, DatasetImage]] = []

        # Add and dedup the images
        for image in images:
            self.add_image(image)

    # Recognized image formats by Kohya's sd-scripts
    ALLOWED_IMAGE_FORMATS = ['.png', '.jpg', '.jpeg', '.webp']

    # Two images' hashes having a hamming distance less or equal to this threshold are considered to be identical
    _EQUALITY_DISTANCE_THRESHOLD = 10

    def add_image(self, image_to_add: DatasetImage):
        found = False
        dupe_source = None

        for image in self.images:
            if image_to_add.cached_hash - image.cached_hash <= Dataset._EQUALITY_DISTANCE_THRESHOLD:
                # The images are (nearly) the same
                found = True
                dupe_source = image
                break

        if found:
            self.duplicated_images.append((image_to_add, dupe_source))
        else:
            self.images.append(image_to_add)
