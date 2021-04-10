import os.path
from dataclasses import dataclass
from glob import glob
from typing import Any, Callable, Iterable, List, TypeVar

_T = TypeVar("_T")


def _from_list(f: Callable[[dict], _T], x: Iterable[Any]) -> List[_T]:
    if isinstance(x, dict):
        x = [x]

    return [f(y) for y in x]


@dataclass
class Character:
    id: str
    name: str

    @staticmethod
    def from_dict(obj: dict) -> "Character":
        id = obj["@id"]
        name = obj["@name"]

        return Character(id, name)


@dataclass
class Body:
    id: str
    xmin: int
    ymin: int
    xmax: int
    ymax: int
    character: str

    @staticmethod
    def from_dict(obj: dict) -> "Body":
        id = obj["@id"]
        xmin = int(obj["@xmin"])
        ymin = int(obj["@ymin"])
        xmax = int(obj["@xmax"])
        ymax = int(obj["@ymax"])
        character = obj["@character"]

        return Body(id, xmin, ymin, xmax, ymax, character)


@dataclass
class Face:
    id: str
    xmin: int
    ymin: int
    xmax: int
    ymax: int
    character: str

    @staticmethod
    def from_dict(obj: dict) -> "Face":
        id = obj["@id"]
        xmin = int(obj["@xmin"])
        ymin = int(obj["@ymin"])
        xmax = int(obj["@xmax"])
        ymax = int(obj["@ymax"])
        character = obj["@character"]

        return Face(id, xmin, ymin, xmax, ymax, character)


@dataclass
class Frame:
    id: str
    xmin: int
    ymin: int
    xmax: int
    ymax: int

    @staticmethod
    def from_dict(obj: dict) -> "Frame":
        id = obj["@id"]
        xmin = int(obj["@xmin"])
        ymin = int(obj["@ymin"])
        xmax = int(obj["@xmax"])
        ymax = int(obj["@ymax"])

        return Frame(id, xmin, ymin, xmax, ymax)


@dataclass
class Text:
    id: str
    xmin: int
    ymin: int
    xmax: int
    ymax: int
    text: str

    @staticmethod
    def from_dict(obj: dict) -> "Text":
        id = obj["@id"]
        xmin = int(obj["@xmin"])
        ymin = int(obj["@ymin"])
        xmax = int(obj["@xmax"])
        ymax = int(obj["@ymax"])
        text = obj["#text"]

        return Text(id, xmin, ymin, xmax, ymax, text)


@dataclass
class Page:
    index: int
    width: int
    height: int
    bodies: List[Body]
    faces: List[Face]
    frames: List[Frame]
    texts: List[Text]

    _image_path: str = ""

    @staticmethod
    def from_dict(obj: dict) -> "Page":
        index = int(obj["@index"])
        width = int(obj["@width"])
        height = int(obj["@height"])
        bodies: List[Body] = _from_list(Body.from_dict, obj["body"]) if "body" in obj else []
        faces: List[Face] = _from_list(Face.from_dict, obj["face"]) if "face" in obj else []
        frames: List[Frame] = _from_list(Frame.from_dict, obj["frame"]) if "frame" in obj else []
        texts: List[Text] = _from_list(Text.from_dict, obj["text"]) if "text" in obj else []

        return Page(index, width, height, bodies, faces, frames, texts)

    @property
    def image_path(self) -> str:
        if self._image_path == "":
            raise ValueError("image path is not set")

        return self._image_path

    @image_path.setter
    def image_path(self, image_path: str):
        self._image_path = image_path


@dataclass
class Book:
    title: str
    characters: List[Character]
    pages: List[Page]

    @staticmethod
    def from_dict(obj: dict, image_root: str) -> "Book":
        title = obj["@title"]
        characters = _from_list(Character.from_dict, obj["characters"]["character"])
        pages = _from_list(Page.from_dict, obj["pages"]["page"])

        for page, image_path in zip(pages, sorted(glob(os.path.join(image_root, "*.jpg")))):
            page.image_path = image_path

        return Book(title, characters, pages)
