from BookList import BookList
from UserList import UserList


class Extension:

    @staticmethod
    def modify_book(book_list):
        """Command Line Interface for modifying a book's details."""
        book_id = input("Enter the Book ID of the book you want to modify: ")

        book = book_list.get_book_by_id(book_id)
        if not book:
            print(f"No book found with ID {book_id}")
            return

        print("\nCurrent Details:")
        print(f"Title: {book.get_title()}")
        print(f"Author: {book.get_author()}")
        print(f"Year: {book.get_year()}")
        print(f"Publisher: {book.get_publisher()}")
        print(f"Number of Copies: {book.get_number_of_copies()}")

        # Taking new values
        title = input("\nEnter new title (Leave blank to keep current): ")
        author = input("Enter new author (Leave blank to keep current): ")
        year = input("Enter new publication year (Leave blank to keep current): ")
        publisher = input("Enter new publisher (Leave blank to keep current): ")
        num_copies = input("Enter new number of copies (Leave blank to keep current): ")

        # Updating book attributes
        if title:
            book.set_title(title)
        if author:
            book.set_author(author)

# Handle year input
        if year:
            try:
                book.set_year(int(year))
            except ValueError:
                print("Invalid input for year. Please provide a valid year.")

# Handle publisher input
        if publisher:
            book.set_publisher(publisher)

# Handle number of copies input
        if num_copies:
            try:
                book.set_number_of_copies(int(num_copies))
            except ValueError:
                print("Invalid input for number of copies. Please provide a valid number.")


        print("\nBook details updated successfully!")

    @staticmethod
    def modify_user(user_list):
        """Command Line Interface for modifying a user's details."""
        username = input("\nEnter the username of the user you want to modify: ")

        user = user_list.get_user_by_username(username)
        if not user:
            print(f"No user found with username {username}")
            return

        print("\nCurrent Details:")
        print(f"First Name: {user.get_firstname()}")
        print(f"Surname: {user.get_surname()}")
        print(f"House Number: {user.get_house_number()}")
        print(f"Street Name: {user.get_street_name()}")
        print(f"Postcode: {user.get_postcode()}")

        # Taking new values
        firstname = input("\nEnter new first name (Leave blank to keep current): ")
        surname = input("Enter new surname (Leave blank to keep current): ")
        house_number = input("Enter new house number (Leave blank to keep current): ")
        street_name = input("Enter new street name (Leave blank to keep current): ")
        postcode = input("Enter new postcode (Leave blank to keep current): ")

        # Updating user attributes
        if firstname:
            user.edit_firstname(firstname)
        if surname:
            user.edit_surname(surname)
        if house_number:
            user.edit_house_number(house_number)
        if street_name:
            user.edit_street_name(street_name)
        if postcode:
            user.edit_postcode(postcode)

        print("\nUser details updated successfully!")

# CLI Loop to allow choice between modifying books and users
def run_extension_cli():
    book_list = BookList()
    user_list = UserList()

    while True:
        print("\nLibrary Management Extension")
        print("1. Modify Book")
        print("2. Modify User")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            Extension.modify_book(book_list)
        elif choice == '2':
            Extension.modify_user(user_list)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice!")
# Extention is not needed for now