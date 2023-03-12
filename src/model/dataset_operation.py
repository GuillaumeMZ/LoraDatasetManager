from src.model.dataset import Dataset
from typing import Protocol

from src.model.dataset_image import DatasetImage


class DatasetOperationFilter(Protocol):
    def filter(self, image: DatasetImage) -> bool:
        """Tells if an operation will be applied to this image or not."""


class DatasetOperationApplication(Protocol):
    def apply(self, image: DatasetImage) -> None:
        """This method is called on all the matched images."""


class DatasetOperation:
    def __init__(self,
                 image_filter: DatasetOperationFilter,
                 application
                 ):
        self.image_filter = image_filter
        self.application = application

    def apply(self, dataset: Dataset):
        for image in dataset.images:
            if self.image_filter.filter(image):
                self.application.apply(image)
