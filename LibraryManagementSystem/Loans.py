from datetime import datetime, timedelta

from Book import Book
from User import User
from UserList import UserList

class Loans:
    """Represents the loan system in the library."""

    def __init__(self):
        """Constructor for a Loans instance."""
        # This will be a dictionary where keys are usernames and values are lists of tuples (book_title, due_date)
        self.loan_records = {}

    def borrow_book(self, user, book):
        """
        Assigns a book to a user.

        Parameters:
        - user (User): An instance of the User class.
        - book (Book): An instance of the Book class.
        """
        if not isinstance(user, User) or not isinstance(book, Book):
            raise ValueError("Invalid user or book instance provided.")

        due_date = datetime.now() + timedelta(days=14)  # 14 days from now

        if user.username in self.loan_records:
            # Check if the user has already borrowed this book
            for record in self.loan_records[user.username]:
                if record[0] == book.title:
                    raise ValueError(f"{user.username} has already borrowed the book with ID {book.title}.")
            self.loan_records[user.username].append((book.title, due_date))
        else:
            self.loan_records[user.username] = [(book.title, due_date)]

    def return_book(self, user, book):
        """
        Un-assigns a book from a user.

        Parameters:
        - user (User): An instance of the User class.
        - book (Book): An instance of the Book class.
        """
        if not isinstance(user, User) or not isinstance(book, Book):
            raise ValueError("Invalid user or book instance provided.")

        if user.username in self.loan_records:
            # Check if the user has borrowed this book
            for idx, record in enumerate(self.loan_records[user.username]):
                if record[0] == book.title:
                    self.loan_records[user.username].pop(idx)
                    break
            else:
                raise ValueError(f"{user.username} hasn't borrowed the book with ID {book.title}.")
        else:
            raise ValueError(f"{user.username} hasn't borrowed any books.")

    def books_borrowed_by_user(self, user):
        """Returns the total number of books borrowed by a user."""
        if not isinstance(user, User):
            raise ValueError("Invalid user instance provided.")

        return len(self.loan_records.get(user.username, []))

    def overdue_books(self, user_list):
        """
        Prints all overdue books along with the user's username and first name.

        Parameters:
        - user_list (UserList): An instance of the UserList class.
        """
        today = datetime.now()

        for username, loans in self.loan_records.items():
            user = user_list.get_user_by_username(username)
            if not user:
                raise ValueError(f"User with username '{username}' not found in the user list.")
            for book_title, due_date in loans:
                if due_date < today:
                    print(f"Overdue Book ID: {book_title}, User: {user.get_username()}, First Name: {user.get_firstname()}")
                    