from dataclasses import dataclass
from dataset_image import DatasetImage
from pathlib import Path
from imagehash import average_hash
import concept
from PIL import Image


class InvalidDatasetError(Exception):
    def __init__(self, cause):
        super().__init__(cause)


class DatasetLoader:
    """
    Loads a dataset in memory.
    Use members dataset_path, concepts, images and config when creating a Dataset.
    """
    def __init__(self, dataset_path: Path):
        self.dataset_path = dataset_path

        # Check dataset's structure validity
        self._check_dataset_structure_validity()

        self._register_concepts()

        # Load the images and filter duplicates.
        self._load_images()

    def _check_dataset_structure_validity(self):
        if (not self.dataset_path.exists()) or (not self.dataset_path.is_dir()):
            raise InvalidDatasetError(f"The given path ({self.dataset_path}) must be an existing directory.")

    def _register_concepts(self):
        self.concepts: list[concept.Concept] = []

        for item in self.dataset_path.iterdir():
            if not item.is_dir():
                continue

            parsed_concept_name = concept.parse_concept_name(item.name)

            if parsed_concept_name is None:
                continue

            self.concepts.append(concept.Concept(
                iterations=parsed_concept_name[0],
                name=parsed_concept_name[1],
                path=item
            ))

    # Recognized image formats by Kohya's sd-scripts
    _ALLOWED_IMAGE_FORMATS = ['.png', '.jpg', '.jpeg', '.webp']

    def _load_images(self):
        images = [(image, cpt.name) for cpt in self.concepts
                  for image in cpt.path.iterdir()
                  if (not image.is_file()) or (image.suffix not in DatasetLoader._ALLOWED_IMAGE_FORMATS)]

        images = list(map(lambda image: DatasetImage(
            path=image[0],
            name=image[0].name,
            concept_name=image[1]
        ), images))

        self._dedup_images(images)

    # Two images' hashes having a hamming distance less or equal to this threshold are considered to be identical
    _EQUALITY_DISTANCE_THRESHOLD = 10

    def _dedup_images(self, images: list[DatasetImage]):
        self.images: list[DatasetImage] = []
        self.duplicated_images: list[DatasetImage] = []

        for image in images:
            if any(image.cached_hash - loaded_image.cached_hash <= DatasetLoader._EQUALITY_DISTANCE_THRESHOLD
                   for loaded_image in self.images):
                self.duplicated_images.append(image)
            else:
                self.images.append(image)
