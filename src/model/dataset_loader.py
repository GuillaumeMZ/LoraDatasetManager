from pathlib import Path
from src.model.dataset import Dataset
from src.model.dataset_image import DatasetImage
from src.model.concept import Concept
from src.model.taglist import Taglist


class InvalidDatasetError(Exception):
    def __init__(self, cause):
        super().__init__(cause)


class DatasetLoader:
    """
    Used to load a dataset from the filesystem.
    Use the load method to get a Dataset instance.
    """
    def __init__(self, dataset_path: Path):
        self.dataset_path = dataset_path
        self.concepts: list[Concept] = []
        self.images: list[DatasetImage] = []
        self.unused_items: list[Path] = []

        self._check_dataset_structure_validity()
        self._register_concepts()
        self._load_images()

    def _check_dataset_structure_validity(self):
        if (not self.dataset_path.exists()) or (not self.dataset_path.is_dir()):
            raise InvalidDatasetError(f"The given path ({self.dataset_path}) must be an existing directory.")

    def _register_concepts(self):
        for item in self.dataset_path.iterdir():
            if not item.is_dir():
                continue

            parsed_concept_name = Concept.parse_concept_name(item.name)

            if parsed_concept_name is None:
                self.unused_items.append(item)

            self.concepts.append(Concept(
                iterations=parsed_concept_name[0],
                name=parsed_concept_name[1],
                path=item
            ))

    def _load_images(self):
        images = [(image, cpt.name) for cpt in self.concepts
                  for image in cpt.path.iterdir()
                  if image.is_file() and image.suffix in Dataset.ALLOWED_IMAGE_FORMATS]

        for image in images:
            self._load_image(image[0], image[1])

    def _load_image(self, path: Path, concept_name: str):  # Won't be used by the downloader I think
        """
        Load the requested image and its tags, if present.
        """
        tag_file_path = path.parent / f"{path.stem}.txt"

        if not tag_file_path.exists():
            tags = None
        else:
            with tag_file_path.open() as file:
                tags = Taglist(file.read())

        self.images.append(
            DatasetImage(
                path,
                concept_name,
                tags
            )
        )

    def load(self):
        return Dataset(self.dataset_path, None, self.concepts, self.images)  # TODO: load config
