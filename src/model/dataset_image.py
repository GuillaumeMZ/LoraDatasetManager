from imagehash import phash
from pathlib import Path
from PIL import Image
from src.model.taglist import Taglist


class DatasetImage:
    def __init__(self, path: Path, concept_name: str, tags: Taglist | None):
        self.path = path
        self.name = path.name
        self.concept_name = concept_name
        self.pil_image = Image.open(path)
        self.cached_hash = phash(self.pil_image)
        self.tags = tags
