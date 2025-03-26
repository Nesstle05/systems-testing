from typing import List, Optional
from bookstore.services.book_filtering_service import BookFilterService
from bookstore.book import Book
from bookstore.book_repository import BookRepository, InMemoryBookRepository

class BookStoreService:
    """
    Bookstore service for basic operations
    """
    def __init__(self,
                 repository: BookRepository = None,
                 book_filter: BookFilterService = None):
        """
        Constructor
        
        :param repository: A repository implementing BookRepository
        :param book_filter: A filter service
        """
        self._repository = repository or InMemoryBookRepository()
        self._book_filter = book_filter or BookFilterService()


    def add_book(self, book: Book) -> Book:
        """Add a new book"""
        return self._repository.add(book)


    def get_books(self,
                  genre: Optional[str] = None,
                  min_price: Optional[float] = None,
                  max_price: Optional[float] = None) -> List[Book]:
        """
        Retrieve books with optional filtering
        
        :param genre: Optional genre to filter by
        :param min_price: Optional minimum price
        :param max_price: Optional maximum price
        :return: Filtered list of books
        """
        all_books = self._repository.get_all()

        # Apply filters using separate filter service
        filtered_by_genre = self._book_filter.filter_by_genre(all_books, genre)

        filtered_books = self._book_filter.filter_by_price_range(
            filtered_by_genre, min_price, max_price
        )

        return filtered_books


    def get_book_by_id(self, book_id: int) -> Optional[Book]:
        """Retrieve a specific book by ID"""
        return self._repository.get_by_id(book_id)


    def update_book(self, book_id: int, **kwargs) -> Optional[Book]:
        """Update book details"""
        return self._repository.update(book_id, **kwargs)


    def remove_book(self, book_id: int) -> bool:
        """Remove a book"""
        return self._repository.remove(book_id)
