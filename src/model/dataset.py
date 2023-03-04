from dataclasses import dataclass
from pathlib import Path
from PIL import Image
import re
from src.model.taglist import Taglist


class InvalidDatasetError(Exception):
    def __init__(self, cause):
        super().__init__(cause)


@dataclass
class DatasetImage:
    path: Path
    name: str
    pil_image: Image
    tags: Taglist
    concept_name: str


class Dataset:
    def __init__(self, dataset_path: str):
        self._load_dataset(dataset_path)

    def reload(self, save_before_reload: bool = False):
        if save_before_reload:
            self.save()

        self._load_dataset(str(self.dataset_path))

    def save(self):
        for image in self.images:
            if image.tags is None:
                continue

            file_path = Path(image.path.parent / f"{image.name}.txt")
            with file_path.open("w+") as output:
                output.write(str(image.tags))

    def _load_dataset(self, dataset_path: str):
        self.dataset_path = Path(dataset_path)
        self.concepts = []
        self.images: list[DatasetImage] = []

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
                image_description = Taglist(f.read())

        # register the image
        self.images.append(DatasetImage(
            path=image_path,
            name=image_stem,
            pil_image=Image.open(image_path),
            tags=image_description,
            concept_name=concept_name
        ))

    @staticmethod
    def _is_concept_name(name: str):
        # A valid concept name has the form X_Y where X is a number and Y is some text.
        concept_name_regex = re.compile(r"\d+_[a-zA-Z0-9]+")

        return concept_name_regex.match(name) is not None  # Maybe not the best way to check this ?
