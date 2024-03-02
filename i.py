from abc import ABC, abstractmethod
from typing import List

class BookManager(ABC):
    @abstractmethod
    def add_book(self, title: str, author: str, genre: str):
        pass

    @abstractmethod
    def remove_book(self, title: str):
        pass


class BookSearch(ABC):
    @abstractmethod
    def search_by_title(self, title: str) -> List[str]:
        pass

    @abstractmethod
    def search_by_author(self, author: str) -> List[str]:
        pass

    @abstractmethod
    def search_by_genre(self, genre: str) -> List[str]:
        pass


class BookBorrower(ABC):
    @abstractmethod
    def borrow_book(self, title: str, user_id: str) -> bool:
        pass

    @abstractmethod
    def return_book(self, title: str, user_id: str) -> bool:
        pass


class ReportGenerator(ABC):
    @abstractmethod
    def generate_borrowing_report(self) -> str:
        pass

    @abstractmethod
    def generate_overdue_report(self) -> str:
        pass

    @abstractmethod
    def generate_popularity_report(self) -> str:
        pass


class Library(BookManager, BookSearch, BookBorrower, ReportGenerator):
    def __init__(self):
        self.catalog = {}

    def add_book(self, title: str, author: str, genre: str):
        self.catalog[title] = {'author': author, 'genre': genre}

    def remove_book(self, title: str):
        if title in self.catalog:
            del self.catalog[title]

    def search_by_title(self, title: str) -> List[str]:
        return [book for book in self.catalog if title.lower() in book.lower()]

    def search_by_author(self, author: str) -> List[str]:
        return [title for title, info in self.catalog.items() if author.lower() == info['author'].lower()]

    def search_by_genre(self, genre: str) -> List[str]:
        return [title for title, info in self.catalog.items() if genre.lower() == info['genre'].lower()]

    def borrow_book(self, title: str, user_id: str) -> bool:
        if title in self.catalog:
            # Logic to borrow book
            return True
        return False

    def return_book(self, title: str, user_id: str) -> bool:
        if title in self.catalog:
            # Logic to return book
            return True
        return False

    def generate_borrowing_report(self) -> str:
        # Logic to generate borrowing report
        return "Borrowing report generated."

    def generate_overdue_report(self) -> str:
        # Logic to generate overdue report
        return "Overdue report generated."

    def generate_popularity_report(self) -> str:
        # Logic to generate popularity report
        return "Popularity report generated."