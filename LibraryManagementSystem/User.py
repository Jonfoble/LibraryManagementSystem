from datetime import datetime


class User:
    """Represents a user in the library system."""

    def __init__(self, username, firstname, surname, house_number, street_name, postcode, email, dob):
        """
        Constructor for a User instance.

        Parameters:
        - username (str): The unique username of the user.
        - firstname (str): The first name of the user.
        - surname (str): The last name or surname of the user.
        - house_number (str): The house number of the user's address.
        - street_name (str): The street name of the user's address.
        - postcode (str): The postcode of the user's address.
        - email (str): The email address of the user.
        - dob (datetime): The date of birth of the user.
        """
        self.username = username
        self.firstname = firstname
        self.surname = surname
        self.house_number = house_number
        self.street_name = street_name
        self.postcode = postcode
        self.email = email
        self.dob = dob

    # Getters
    def get_username(self):
        return self.username

    def get_firstname(self):
        return self.firstname

    def get_surname(self):
        return self.surname

    def get_house_number(self):
        return self.house_number

    def get_street_name(self):
        return self.street_name

    def get_postcode(self):
        return self.postcode

    def get_email(self):
        return self.email

    def get_dob(self):
        return self.dob.strftime("%Y-%m-%d")

    # Setters (only for specific attributes as required)
    def edit_firstname(self, firstname):
        self.firstname = firstname

    def edit_surname(self, surname):
        self.surname = surname

    def edit_email(self, email):
        # Check if email format is valid
        if "@" in email and "." in email:
            self.email = email
        else:
            raise ValueError("Invalid email format.")

    def edit_dob(self, dob):
        if isinstance(dob, datetime):
            self.dob = dob
        else:
            raise ValueError("Date of birth should be a datetime object.")
    def edit_house_number(self, new_house_number):
        self.house_number = new_house_number

    def edit_street_name(self, new_street_name):
        self.street_name = new_street_name

    def edit_postcode(self, new_postcode):
        self.postcode = new_postcode

