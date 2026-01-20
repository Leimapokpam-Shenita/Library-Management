from dataclasses import dataclass, field
from typing import Dict

@dataclass
class Book:
    book_id: str
    title: str
    author: str
    borrowed: bool = False 

@dataclass
class Library:
    books: Dict[str, Book] = field(default_factory=dict)

    def add_book(self, book_id: str, title: str, author: str) -> None:
        if not book_id or not title or not author:
            raise ValueError("book_id, title and author required")

        if book_id in self.books:
            raise ValueError("book already exists")

        self.books[book_id] = Book(
            book_id=book_id,
            title=title,
            author=author
        )

    def borrow_book(self, book_id: str) -> None:
        if book_id not in self.books:
            raise KeyError("book not found")

        if self.books[book_id].borrowed:
            raise ValueError("book already borrowed")

        self.books[book_id].borrowed = True

    def return_book(self, book_id: str) -> None:
        if book_id not in self.books:
            raise KeyError("book not found")

        self.books[book_id].borrowed = False
