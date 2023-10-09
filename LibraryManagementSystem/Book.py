import uuid
from datetime import datetime

class Book:
    """Represents a book in the library system."""
    
    def __init__(self, title, author, year, publisher, number_of_copies, publication_date):
        """
        Constructor for a Book instance.

        Parameters:
        - title (str): The title of the book.
        - author (str): The author of the book.
        - year (int): The publication year of the book.
        - publisher (str): The publisher of the book.
        - number_of_copies (int): The total number of copies of the book.
        - publication_date (datetime): The exact publication date of the book.
        """
        self.book_id = f"{title.replace(' ', '_')}-{author.replace(' ', '_')}-{year}"  # Generate a readable book ID.
        self.title = title
        self.author = author
        self.year = year
        self.publisher = publisher
        self.number_of_copies = number_of_copies
        self.available_copies = number_of_copies  # Initially, all copies are available.
        self.publication_date = publication_date

    # Setters
    def set_title(self, title):
        self.title = title

    def set_author(self, author):
        self.author = author

    def set_year(self, year):
        if isinstance(year, int):
            self.year = year
        else:
            raise ValueError("Year should be an integer.")
    
    def set_publisher(self, publisher):
        self.publisher = publisher

    def set_number_of_copies(self, copies):
        if isinstance(copies, int) and copies >= 0:
            self.number_of_copies = copies
        else:
            raise ValueError("Number of copies should be a non-negative integer.")
        
        # Ensure available copies is not more than total number of copies
        self.available_copies = min(self.available_copies, self.number_of_copies)

    def set_publication_date(self, date):
        if isinstance(date, datetime):
            self.publication_date = date
        else:
            raise ValueError("Publication date should be a datetime object.")
    
    # Getters
    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_year(self):
        return self.year

    def get_publisher(self):
        return self.publisher

    def get_number_of_copies(self):
        return self.number_of_copies

    def get_available_copies(self):
        return self.available_copies

    def get_publication_date(self):
        return self.publication_date.strftime("%Y-%m-%d")


    def decrease_available_copies(self):
        """Decrease the number of available copies by one."""
        self.available_copies -= 1

    def increase_available_copies(self):
        """Increase the number of available copies by one."""
        self.available_copies += 1
