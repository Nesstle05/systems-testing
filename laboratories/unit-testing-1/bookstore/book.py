from typing import Optional

class Book:
    """Book entity class"""
    def __init__(self, title: str, author: str, genre: str, price: float):
        self.id: Optional[int] = None
        self.author = author
        self.title = title
        self.genre = genre
        self.price = price
