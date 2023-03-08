import json
from dataclasses import dataclass
from pathlib import Path
from PIL import Image
import re

from src.model.dataset_image import DatasetImage
from src.model.taglist import Taglist


class DatasetConfig:
    def __init__(self, config_file: Path):
        self._load_config(config_file)

    def _load_config(self, config_file: Path):
        with config_file.open() as file:
            contents = file.read()

        self._json = json.loads(contents)
        self.tags_groups = self._json["tags_groups"]




def are_images_identical(first: Image, second: Image) -> bool:



def is_concept_name(name: str):
    # A valid concept name has the form X_Y where X is a number and Y is some text.
    concept_name_regex = re.compile(r"\d+_[a-zA-Z0-9]+")
    return concept_name_regex.match(name) is not None  # Maybe not the best way to check this ?


class Dataset:
    def __init__(self, concepts: list[str], images: list[DatasetImage]):
        self.concepts = concepts
        self.images = images

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



    def _load_concept(self, concept_path):
        # First of all, register the concept name
        self.concepts.append(concept_path.name)

        # We will load all images files with their extension being one of the following: .png, .jpg, .jpeg, .webp
        for element in concept_path.iterdir():
            if (not element.is_file()) or (element.suffix not in [".png", ".jpeg", ".jpg", ".webp"]):
                continue

            self._load_image(element, concept_path.name)

    def _find_duplicates(self, image: Image) -> DatasetImage | None:
        for existing in self.images:
            if are_images_identical(image, existing.pil_image):
                return existing

        return None

    def _load_image(self, image_path: Path, concept_name: str):
        image_stem = image_path.stem

        # let's check if the image comes with a tag file
        tag_file_path = image_path.parent / f"{image_stem}.txt"

        image_description = None

        # if the image is tagged, we read the tags
        if tag_file_path.exists():
            with tag_file_path.open() as f:
                image_description = Taglist(f.read())

        pil_image = Image.open(image_path)
        # TODO: parallelize this
        duplicate = self._find_duplicates(pil_image)

        dataset_image = DatasetImage(
            path=image_path,
            name=image_stem,
            pil_image=pil_image,
            tags=image_description,
            concept_name=concept_name
        )

        # register the image to where it belongs
        if duplicate is None:
            self.images.append(dataset_image)
        else:
            print("duplicate found")
            self.duplicates.append(dataset_image)
