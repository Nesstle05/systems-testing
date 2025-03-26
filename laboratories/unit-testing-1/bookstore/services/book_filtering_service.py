from typing import List, Optional
from bookstore.book import Book

class BookFilterService:
    """Service for filtering books"""
    @staticmethod
    def filter_by_genre(books: List[Book], genre: Optional[str] = None) -> List[Book]:
        """Filter books by genre"""
        if not genre:
            return books
        return [book for book in books if book.genre.lower() == genre.lower()]


    @staticmethod
    def filter_by_price_range(books: List[Book], 
                               min_price: Optional[float] = None,
                               max_price: Optional[float] = None) -> List[Book]:
        """Filter books by price range"""
        if min_price is None and max_price is None:
            return books

        return [
            book for book in books
            if (min_price is None or book.price >= min_price) and
                (max_price is None or book.price <= max_price)
        ]
