from abc import ABC, abstractmethod
from logger import logger
from typing import List


class Book:
    def __init__(self, title: str, author: str, year: int) -> None:
        self.title = title
        self.author = author
        self.year = year

    def __str__(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def remove_book(self, title: str) -> bool:
        pass

    @abstractmethod
    def show_books(self) -> None:
        pass


class Library(LibraryInterface):
    def __init__(self) -> None:
        self.books: List[Book] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def remove_book(self, title: str) -> bool:
        initial_len = len(self.books)
        self.books = [book for book in self.books if book.title != title]
        return len(self.books) < initial_len

    def show_books(self) -> None:
        if not self.books:
            logger.info("Library is empty.")
        else:
            for book in self.books:
                logger.info(book)


class LibraryManager:
    def __init__(self, library: LibraryInterface) -> None:
        self.library = library

    def add_book(self, title: str, author: str, year: int) -> None:
        book = Book(title, author, year)
        self.library.add_book(book)
        logger.info(f'Book with name "{title}" was added successfully.')

    def remove_book(self, title: str) -> None:
        if self.library.remove_book(title):
            logger.info(f'Book with name "{title}" was removed successfully.')
        else:
            logger.warning(f'Book with name "{title}" was not found.')

    def show_books(self) -> None:
        self.library.show_books()


def main() -> None:
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        if command == "add":
            title = input("Enter book title: ").strip()
            author = input("Enter book author: ").strip()
            try:
                year = int(input("Enter book year: ").strip())
            except ValueError:
                logger.warning("Year must be a valid integer.")
                continue
            manager.add_book(title, author, year)

        elif command == "remove":
            title = input("Enter book title to remove: ").strip()
            manager.remove_book(title)

        elif command == "show":
            manager.show_books()

        elif command == "exit":
            logger.info("Exiting the program.")
            break

        else:
            logger.warning("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
