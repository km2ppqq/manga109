import os.path
from typing import List

import xmltodict

from .titles import ALL_TITLES
from .typing import Book


class Manga109:
    def __init__(self, root: str, annotation_type: str = "annotations", titles: List[str] = ALL_TITLES):
        self._root = root
        self.books = self._read_books(root, annotation_type, titles)

    @staticmethod
    def _read_books(root: str, annotation_type: str, titles: List[str]) -> List[Book]:
        books: List[Book] = []

        for title in titles:
            with open(os.path.join(root, annotation_type, f"{title}.xml")) as f:
                content = f.read()

            d = xmltodict.parse(content)
            book = Book.from_dict(d["book"], os.path.join(root, "images", title))
            for page in book.pages:
                page.image_path = os.path.join(root, "images", title, f"{page.index:03d}.jpg")
            books.append(book)

        return books
