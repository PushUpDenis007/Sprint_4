import pytest
from main import BooksCollector 

@pytest.fixture
def book():
    return BooksCollector()

@pytest.fixture
def filled_book(book, books_dict):
    for name, genre in books_dict.items():
            book.add_new_book(name)
            book.set_book_genre(name, genre)
    return book