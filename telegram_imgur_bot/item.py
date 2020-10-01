from dataclasses import dataclass
from typing import Set


@dataclass
class Item:
    title: str
    images = []

    def to_json(self):
        return {"name": self.title, "img1": self.images[0], "img2": self.images[1]}
