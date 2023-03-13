import re
from src.model.dataset import Dataset
from src.model.dataset_image import DatasetImage
from src.model.taglist import Taglist
from typing import Protocol


# TODO: find better names for these classes
class DatasetOperationFilter(Protocol):
    def filter(self, image: DatasetImage) -> bool:
        """Tells if an operation will be applied to this image or not."""


class DatasetOperationApplication(Protocol):
    def apply(self, image: DatasetImage) -> None:
        """This method is called on all the matched images."""


class DatasetOperation:
    def __init__(self,
                 image_filter: DatasetOperationFilter,
                 application: DatasetOperationApplication
                 ):
        self.image_filter = image_filter
        self.application = application

    def apply(self, dataset: Dataset):
        for image in dataset.images:
            if self.image_filter.filter(image):
                self.application.apply(image)


# FILTERS

class UniversalOperationFilter(DatasetOperationFilter):
    """
    Does not filter any image.
    """
    def __init__(self):
        pass

    def filter(self, image: DatasetImage) -> bool:
        return True


class ConceptNameOperationFilter(DatasetOperationFilter):
    """
    Filters concepts by their names.
    """
    def __init__(self, concept_name: str):
        self.concept_name = concept_name

    def filter(self, image: DatasetImage) -> bool:
        return image.concept_name == self.concept_name


class ImageNameRegexOperationFilter(DatasetOperationFilter):
    """
    Keeps images only if their names are matched by a regex.
    """
    def __init__(self, regex: re):
        self.regex = regex

    def filter(self, image: DatasetImage) -> bool:
        return self.regex.fullmatch(image.name)


#  APPLICATIONS

class AddTagsApplication(DatasetOperationApplication):
    """
    Adds a tag or a list of tags to the selected images in a specific position.
    """
    def __init__(self, tags: str | Taglist, position: int = -1):
        self.tags = tags
        self.position = position

    def apply(self, image: DatasetImage) -> None:
        if isinstance(self.tags, str):
            image.tags.add_tag(self.tags, self.position)
        else:
            image.tags.add_tags(self.tags, self.position)


class RemoveTagsApplication(DatasetOperationApplication):
    """
    Removes a tag or a list of tags of the selected images in a specific position.
    """
    def __init__(self, tags: str | Taglist):
        self.tags = tags

    def apply(self, image: DatasetImage) -> None:
        if isinstance(self.tags, str):
            image.tags.remove_tag(self.tags)
        else:
            image.tags.remove_tags(self.tags)
