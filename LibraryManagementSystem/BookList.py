from datetime import datetime

from Book import Book


class BookList:
    """Represents a collection of books in the library system."""

    def __init__(self):
        """Constructor for a BookList instance."""
        # We will use a dictionary where keys are book IDs and values are Book instances
        self.books = {}

    def add_book(self, book):
        """
        Adds a book to the collection.

        Parameters:
        - book (Book): A Book instance.
        """
        if isinstance(book, Book):
            self.books[book.book_id] = book
        else:
            raise ValueError("Only instances of the Book class can be added.")

    def search_books(self, **kwargs):
        """
        Searches for books in the collection by title, author, publisher, or publication date.

        Parameters (optional keyword arguments):
        - title (str): The title of the book.
        - author (str): The author of the book.
        - publisher (str): The publisher of the book.
        - publication_date (str): The publication date in "YYYY-MM-DD" format.

        Returns:
        - list: A list of matching Book instances.
        """
        # Empty list to store matching books
        matching_books = []
        
        # Iterate through all books in the collection
        for book in self.books.values():
            match = True
            for key, value in kwargs.items():
                if hasattr(book, key):
                    if key == "publication_date":
                        if book.get_publication_date() != value:
                            match = False
                            break
                    else:
                        if getattr(book, key) != value:
                            match = False
                            break
                else:
                    raise ValueError(f"The attribute {key} is not valid for Book instances.")
            
            # If the book matches all criteria, add to matching_books list
            if match:
                matching_books.append(book)
        
        return matching_books

    def remove_book_by_title(self, title):
        """
        Removes a book from the collection by its title.

        Parameters:
        - title (str): The title of the book.
        """
        book_ids_to_remove = [book_id for book_id, book in self.books.items() if book.title == title]

        if not book_ids_to_remove:
            raise ValueError(f"No books found with the title: {title}")

        for book_id in book_ids_to_remove:
            del self.books[book_id]

    def total_books(self):
        """Returns the total number of books in the collection."""
        return len(self.books)

    def get_book_by_id(self, book_id):
        """Retrieve a book object based on its book ID."""
        return self.books.get(book_id, None)

    def get_book_by_title(self, title):
        """Retrieve a book object based on its title."""
        for book in self.books.values():
            if book.title == title:
                return book
        return None
