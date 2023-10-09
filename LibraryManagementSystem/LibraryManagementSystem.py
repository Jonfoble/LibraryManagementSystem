from datetime import datetime
from Book import Book
from BookList import BookList
from User import User
from UserList import UserList
from Loans import Loans
from Extension import Extension
import re

class LibraryManagementSystem:
    
    def __init__(self):
        self.book_list = BookList()
        self.user_list = UserList()
        self.loans = Loans()
    
    def main_menu(self):
        while True:
            print("\nLibrary Management System:")
            print("1. Manage Books")
            print("2. Manage Users")
            print("3. Manage Loans")
            print("4. Exit")
            
            choice = input("Enter your choice (1/2/3/4): ")
            
            if choice == '1':
                self.manage_books_menu()
            elif choice == '2':
                self.manage_users_menu()
            elif choice == '3':
                self.manage_loans_menu()
            elif choice == '4':
                print("Exiting...")
                break
            else:
                print("Invalid choice!")

    def manage_books_menu(self):
        while True:
            print("\nManage Books:")
            print("a. Add Book")
            print("b. Modify Book")
            print("c. Remove Book")
            print("d. Search Books")
            print("e. List All Books")
            print("f. Return to Main Menu")

            choice = input("Enter your choice (a/b/c/d/e/f): ")

            if choice == 'a':
                self.add_book()
            elif choice == 'b':
                Extension.modify_book(self.book_list)
            elif choice == 'c':
                self.remove_book()
            elif choice == 'd':
                self.search_books()
            elif choice == 'e':
                self.list_all_books()
            elif choice == 'f':
                break
            else:
                print("Invalid choice!")

    def add_book(self):
        while True:
            title = input("Enter book title: ")
            author = input("Enter book author: ")

        # Handle publication year input
            try:
                year = int(input("Enter book publication year: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid publication year.")
                continue

        while True:
            publisher = input("Enter book publisher: ")

        # Handle number of copies input
            try:
                number_of_copies = int(input("Enter number of copies: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number for copies.")
            continue

        while True:
            publication_date_str = input("Enter publication date (YYYY-MM-DD): ")

        # Handle publication date input
            try:
                publication_date = datetime.strptime(publication_date_str, "%Y-%m-%d")
                break
            except ValueError:
                print("Invalid date format. Please enter the date in the format YYYY-MM-DD.")
                continue

        book = Book(title, author, year, publisher, number_of_copies, publication_date)
        self.book_list.add_book(book)
        print("Book added successfully!")

    def remove_book(self):
        title = input("Enter the title of the book to remove: ")
    
        try:
            self.book_list.remove_book_by_title(title)
            print(f"Books with title '{title}' removed successfully!")
        except ValueError:  # Assuming remove_book_by_title raises a ValueError for non-existent book titles
            print(f"No books found with the title '{title}'.")

    def search_books(self):
        search_type = input("Search by (title/author/publisher): ")
        search_value = input("Enter the search value: ")
    
        matching_books = []
        if search_type == "title":
            matching_books = self.book_list.search_books(title=search_value)
        elif search_type == "author":
            matching_books = self.book_list.search_books(author=search_value)
        elif search_type == "publisher":
            matching_books = self.book_list.search_books(publisher=search_value)
        else:
            print("Invalid search type!")
            return
    
        if not matching_books:
            print(f"No books found for {search_value}.")
            return
    
        print("\nMatching Books:")
        for book in matching_books:
            print(f"ID: {book.book_id}, Title: {book.get_title()}, Author: {book.get_author()}, Year: {book.get_year()}, Publisher: {book.get_publisher()}, Available Copies: {book.get_available_copies()}")


    def list_all_books(self):
        print("\nAll Books:")
        for book_id, book in self.book_list.books.items():
            print(f"ID: {book.book_id}, Title: {book.get_title()}, Author: {book.get_author()}, Year: {book.get_year()}, Publisher: {book.get_publisher()}, Available Copies: {book.get_available_copies()}, Publication Date: {book.get_publication_date()}")

    def manage_users_menu(self):
        while True:
            print("\nManage Users:")
            print("a. Add User")
            print("b. Modify User")
            print("c. Remove User")
            print("d. List All Users")
            print("e. Return to Main Menu")

            choice = input("Enter your choice (a/b/c/d/e): ")

            if choice == 'a':
                self.add_user()
            elif choice == 'b':
                Extension.modify_user(self.user_list)
            elif choice == 'c':
                self.remove_user()
            elif choice == 'd':
                self.list_all_users()
            elif choice == 'e':
                break
            else:
                print("Invalid choice!")

    def add_user(self):
        username = input("Enter username: ")
        firstname = input("Enter first name: ")
        surname = input("Enter surname: ")
        house_number = input("Enter house number: ")
        street_name = input("Enter street name: ")
        postcode = input("Enter postcode: ")

    # Handle email input with basic validation
        while True:
            email = input("Enter email: ")
            if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                print("Invalid email format. Please enter a valid email.")
                continue
            break

    # Handle date of birth input
        while True:
            dob_str = input("Enter date of birth (YYYY-MM-DD): ")
            try:
                dob = datetime.strptime(dob_str, "%Y-%m-%d")
                break
            except ValueError:
                print("Invalid date format. Please enter the date in the format YYYY-MM-DD.")
                continue

        user = User(username, firstname, surname, house_number, street_name, postcode, email, dob)
        self.user_list.add_user(user)
        print("User added successfully!")

    def remove_user(self):
        username = input("Enter the username of the user to remove: ")
        user = self.user_list.get_user_by_username(username)
        if user:
            del self.user_list.users[username]
            print(f"User with username '{username}' removed successfully!")
        else:
            print(f"No user found with username '{username}'.")

    
    def list_all_users(self):
        print("\nAll Users:")
        for user in self.user_list.users.values():
            print(f"Username: {user.get_username()}, First Name: {user.get_firstname()}, Surname: {user.get_surname()}, Email: {user.get_email()}, House Number: {user.get_house_number()}, Street Name: {user.get_street_name()}, Post Code: {user.get_postcode()}, Date of Birth: {user.get_dob()}")

    def manage_loans_menu(self):
        while True:
            print("\nManage Loans:")
            print("a. Borrow Book")
            print("b. Return Book")
            print("c. List Overdue Books")
            print("d. Return to Main Menu")

            choice = input("Enter your choice (a/b/c/d): ")

            if choice == 'a':
                self.borrow_book()
            elif choice == 'b':
                self.return_borrowed_book()
            elif choice == 'c':
                self.list_overdue_books()
            elif choice == 'd':
                break
            else:
                print("Invalid choice!")

    
    
    def borrow_book(self):
        username = input("Enter the username of the borrower: ")
        user = self.user_list.get_user_by_username(username)
    
        book_title = input("Enter the title of the book to borrow: ")
        book = self.book_list.get_book_by_title(book_title)
    
        if not user or not book:
            print("Invalid user or book provided.")
            return

        if book.get_available_copies() <= 0:
            print("Sorry, all copies of this book are currently borrowed.")
            return
    
    # Record the borrowing action in Loans and update book's availability
        self.loans.borrow_book(user, book)
        book.decrease_available_copies()
        print(f"{user.get_username()} has successfully borrowed {book.get_title()}.")
        input("Press any key to return to the main menu...")

        username = input("Enter your username: ")
        book_title = input("Enter the title of the book you want to borrow: ")
        if self.book_list.get_book_by_title(book_title):
                self.loans.borrow_book(username, book_title)
                print(f"You have successfully borrowed '{book_title}'.")
        else:
                print(f"No book found with title '{book_title}'.")

    def return_borrowed_book(self):
        username = input("Enter your username: ")
        book_title = input("Enter the title of the book you want to return: ")
        if book_title in self.loans.books_borrowed_by_user(username):
            self.loans.return_book(username, book_title)
            print(f"You have successfully returned '{book_title}'.")
        else:
            print(f"You haven't borrowed a book with title '{book_title}'.")

        username = input("Enter username of the borrower: ")
        book_id = input("Enter book ID to borrow: ")

        user = self.user_list.get_user_by_username(username)
        book = self.book_list.get_book_by_id(book_id)

        if user and book:
            self.loans.borrow_book(user, book)
            print(f"Book with ID '{book_id}' has been borrowed by '{username}'.")
        else:
            print("Either user or book not found.")

    def return_borrowed_book(self):
        username = input("Enter username of the borrower: ")
        book_id = input("Enter book ID to return: ")

        user = self.user_list.get_user_by_username(username)
        book = self.book_list.get_book_by_id(book_id)

        if user and book:
            self.loans.return_book(user, book)
            print(f"Book with ID '{book_id}' has been returned by '{username}'.")
        else:
            print("Either user or book not found.")

    def list_overdue_books(self):
        self.loans.overdue_books(self.user_list)


# Initialize the library management system and display the main menu
library_system = LibraryManagementSystem()
library_system.main_menu()
