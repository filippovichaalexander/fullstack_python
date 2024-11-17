from dataclasses import dataclass, field
from typing import List, Union, Optional
from collections import defaultdict
from collections import defaultdict

class InvalidBookAttributeError(Exception):
    pass

@dataclass
class Book:
    book_id: Optional[int] = field(init=False, default=None, compare=False)
    pages: int
    year: int
    author: str
    price: float

    def __post_init__(self):
        if self.pages <= 0:
            raise InvalidBookAttributeError("Количество страниц должно быть больше 0")
        if self.year < 0:
            raise InvalidBookAttributeError("Год выпуска не может быть отрицательным")
        if self.price <= 0:
            raise InvalidBookAttributeError("Цена должна быть больше 0")

    def __lt__(self, other):
        return self.price < other.price

class Library:
    def __init__(self):
        self.books = {}
        self.book_index = defaultdict(list)

    def add_book(self, book: Book):
        book.book_id = len(self.books) + 1
        self.books[book.book_id] = book
        self.book_index[book.author].append(book)

    def get_book_info(self, book_id: int):
        if book_id in self.books:
            return self.books[book_id]
        raise ValueError(f"Книга с id {book_id} не найдена")

    def find_books_by_author(self, *authors: Union[str, List[str]]):
        if len(authors) == 1 and isinstance(authors[0], list):
            authors = authors[0]
        results = []
        for author in authors:
            results.extend(self.book_index[author])
        return results
