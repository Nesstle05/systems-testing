from typing import List, Optional, Protocol
from bookstore.book import Book

class BookRepository(Protocol):
    """Protocol defining the interface for book storage"""
    def add(self, book: Book) -> Book:
        """Add a book to the repository"""


    def get_all(self) -> List[Book]:
        """Retrieve all books"""


    def get_by_id(self, book_id: int) -> Optional[Book]:
        """Retrieve a book by its ID"""


    def update(self, book_id: int, **kwargs) -> Optional[Book]:
        """Update a book's details"""


    def remove(self, book_id: int) -> bool:
        """Remove a book from the repository"""


class InMemoryBookRepository:
    """Concrete implementation of BookRepository using in-memory storage"""
    def __init__(self):
        self._books: List[Book] = []
        self._next_id = 1


    def add(self, book: Book) -> Book:
        """Add a new book to the repository"""
        if not book.title or not book.author:
            raise ValueError("Book must have a title and author")

        book.id = self._next_id
        self._next_id += 1
        self._books.append(book)

        return book


    def get_all(self) -> List[Book]:
        """Retrieve all books"""
        return self._books.copy()


    def get_by_id(self, book_id: int) -> Optional[Book]:
        """Retrieve a specific book by ID"""
        return next((book for book in self._books if book.id == book_id), None)


    def update(self, book_id: int, **kwargs) -> Optional[Book]:
        """Update book details"""
        book = self.get_by_id(book_id)

        if not book:
            raise ValueError(f"No book found with ID {book_id}")

        for key, value in kwargs.items():
            if hasattr(book, key):
                setattr(book, key, value)

        return book


    def remove(self, book_id: int) -> bool:
        """Remove a book from the repository"""
        book = self.get_by_id(book_id)

        if book:
            self._books.remove(book)
            return True

        return False
