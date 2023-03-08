from imagehash import ImageHash
from dataclasses import dataclass
from pathlib import Path
from PIL import Image
from taglist import Taglist


@dataclass
class DatasetImage:
    """
    Do not create instances of this class directly.
    """
    path: Path
    name: str
    pil_image: Image
    tags: Taglist
    concept_name: str
    cached_hash: ImageHash
