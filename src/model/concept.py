from dataclasses import dataclass
from pathlib import Path
import re

# A valid concept name has the form X_Y where X is a number and Y is some text.
_CONCEPT_NAME_REGEX = re.compile(r"(\d+)_([a-zA-Z0-9]+)")


@dataclass
class Concept:
    name: str
    iterations: int
    path: Path

    @staticmethod
    def parse_concept_name(source: str) -> tuple[int, str] | None:
        parse_result = _CONCEPT_NAME_REGEX.fullmatch(source)
        if parse_result is None:
            return None
        else:
            return int(parse_result.group(1)), parse_result.group(2)
