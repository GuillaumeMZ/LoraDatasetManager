from src.model.dataset import Dataset
from src.model.dataset_image import DatasetImage
from typing import Callable


class DatasetOperation:
    def __init__(self,
                 image_filter: Callable[[DatasetImage], bool],
                 operation: Callable[[DatasetImage], None]
                 ):
        self.image_filter = image_filter
        self.operation = operation

    def apply(self, dataset: Dataset):
        for image in dataset.images:
            if self.image_filter(image):
                self.operation(image)

