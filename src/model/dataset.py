from pathlib import Path
import re


class InvalidDatasetError(Exception):
    def __init__(self, cause):
        super().__init__(cause)


class Dataset:
    def __init__(self, dataset_path: str):
        self.dataset_path = Path(dataset_path)
        self.concepts = []
        self.images = []

        self._load_dataset()

    def reload(self):
        # Save, then load again
        # TODO: write the save method
        self._load_dataset()  #

    def _load_dataset(self):
        # First, check that dataset_path exists and is a folder
        if (not self.dataset_path.exists()) or (not self.dataset_path.is_dir()):
            raise InvalidDatasetError(f"The specified path ({self.dataset_path}) is not a directory or does not exist.")

        # For each subdirectory which corresponds to a concept, load it
        for element in self.dataset_path.iterdir():
            if (not element.is_dir()) or (not Dataset._is_concept_name(element.name)):
                continue

            self._load_concept(element)

    def _load_concept(self, concept_path):
        # First of all, register the concept name
        self.concepts.append(concept_path.name)

        # We will load all images files with their extension being one of the following: .png, .jpg, .jpeg, .webp
        for element in concept_path.iterdir():
            if (not element.is_file()) or (element.suffix not in [".png", ".jpeg", ".jpg", ".webp"]):
                continue

            self._load_image(element, concept_path.name)

    def _load_image(self, image_path: Path, concept_name: str):
        image_stem = image_path.stem

        # let's check if the image comes with a tag file
        tag_file_path = image_path.parent / f"{image_stem}.txt"

        image_description = None

        # if the image is tagged, we read the tags
        if tag_file_path.exists():
            with tag_file_path.open() as f:
                image_description = f.read()

        # register the image
        self.images.append({
            "image_path": image_path,
            "image_name": image_stem,  # No extension
            "tags": image_description,
            "concept_name": concept_name  # Is it really useful ?
        })

    @staticmethod
    def _is_concept_name(name: str):
        # A valid concept name has the form X_Y where X is a number and Y is some text.
        concept_name_regex = re.compile(r"\d+_[a-zA-Z0-9]+")

        return concept_name_regex.match(name) is not None  # Maybe not the best way to check this ?
