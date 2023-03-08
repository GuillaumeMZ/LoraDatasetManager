from dataset_image import DatasetImage
from pathlib import Path
from imagehash import average_hash

class InvalidDatasetError(Exception):
    def __init__(self, cause):
        super().__init__(cause)


class DatasetLoader:
    """
    Used to load a dataset from the filesystem.
    """

    def __init__(self, dataset_path: Path):
        self.dataset_path = dataset_path

        # Check dataset's structure validity
        self._check_dataset_structure_validity()

        # Load the concepts (and the images by extension)
        self._load_concepts()

        # Filter the duplicated images
        self._find_duplicated_images()

        self.dataset = ...

IMAGE_COMPARISON_EQUALITY_THRESHOLD = 5

def _find_duplicated_images(images: list[DatasetImage]):
    duplicated_images: list[DatasetImage] = []
    single_images: list[DatasetImage] = []

    # Maybe parallelize this ?
    for unclassified_image in images:
        for classified_image in single_images:
            hamming_distance = unclassified_image.cached_hash - classified_image.cached_hash

            if hamming_distance <= IMAGE_COMPARISON_EQUALITY_THRESHOLD:
                # The two compared images are identical
                duplicated_images.append(unclassified_image)
            else:
                # They are not identical
                single_images.append(unclassified_image)

    return single_images, duplicated_images


    def _check_dataset_structure_validity(self):
        if (not self.dataset_path.exists()) or (not self.dataset_path.is_dir()):
            raise InvalidDatasetError(f"The given path ({self.dataset_path}) must be an existing directory.")

    def _load_images(self):

    def _load_dataset(self, dataset_path: Path):

        self.concepts = []
        self.images: list[DatasetImage] = []
        self.duplicates: list[DatasetImage] = []

        # First, check that dataset_path exists and is a folder
        if (not self.dataset_path.exists()) or (not self.dataset_path.is_dir()):
            raise InvalidDatasetError(f"The specified path ({self.dataset_path}) is not a directory or does not exist.")

        # For each subdirectory which corresponds to a concept, load it
        for element in self.dataset_path.iterdir():
            if (not element.is_dir()) or (not is_concept_name(element.name)):
                continue

            self._load_concept(element)
