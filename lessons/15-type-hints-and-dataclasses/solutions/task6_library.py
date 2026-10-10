from dataclasses import dataclass, field

@dataclass
class Book:
    title: str
    author: str
    isbn: str
    on_loan: bool = False


@dataclass
class Library:
    books: dict[str, Book] = field(default_factory=dict)

    def add_book(self, book: Book) -> None:
        """Adds a book to the library"""
        self.books[book.isbn] = book

    def _find(self, isbn: str) -> Book:
        """Returns the book with the given ISBN, or raises a KeyError"""
        if isbn not in self.books:
            raise KeyError(f"There is no book with ISBN {isbn}")
        return self.books[isbn]

    def borrow(self, isbn: str) -> Book:
        """Marks a book as on loan, and returns it"""
        book = self._find(isbn)
        if book.on_loan:
            raise ValueError(f"'{book.title}' is already on loan")
        book.on_loan = True
        return book

    def return_book(self, isbn: str) -> None:
        """Marks a book as no longer on loan"""
        book = self._find(isbn)
        if not book.on_loan:
            raise ValueError(f"'{book.title}' isn't on loan")
        book.on_loan = False

    def available_books(self) -> list[Book]:
        """Returns a list of the books that aren't on loan"""
        return [book for book in self.books.values() if not book.on_loan]


library = Library()
library.add_book(Book("Frankenstein", "Mary Shelley", "9780141439471"))
library.add_book(Book("Dracula", "Bram Stoker", "9780141439846"))
library.add_book(Book("Emma", "Jane Austen", "9780141439587"))

book = library.borrow("9780141439471")
print(f"Borrowed '{book.title}'")

# Each of these should fail
try:
    library.borrow("9780141439471")
except ValueError as error:
    print(f"Error: {error}")

try:
    library.borrow("1234567890")
except KeyError as error:
    print(f"Error: {error}")  # KeyError puts quotes around its message

try:
    library.return_book("9780141439846")
except ValueError as error:
    print(f"Error: {error}")

library.return_book("9780141439471")
print("Available books:")
for book in library.available_books():
    print(f"  {book.title} by {book.author}")
