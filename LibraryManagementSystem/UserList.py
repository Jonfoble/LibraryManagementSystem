from datetime import datetime

from User import User


class UserList:
    """Represents a collection of users in the library system."""

    def __init__(self):
        """Constructor for a UserList instance."""
        # Dictionary to store user instances. Keys will be usernames.
        self.users = {}

    def add_user(self, user):
        """
        Adds a user to the collection.

        Parameters:
        - user (User): An instance of the User class.
        """
        if isinstance(user, User):
            if user.username not in self.users:
                self.users[user.username] = user
            else:
                raise ValueError(f"A user with the username '{user.username}' already exists.")
        else:
            raise ValueError("Only instances of the User class can be added.")

    def remove_user_by_firstname(self, firstname):
        """
        Removes a user from the collection by their first name.

        Parameters:
        - firstname (str): The first name of the user.

        Returns:
        - str: A message indicating the result of the operation.
        """
        matched_users = [user for user in self.users.values() if user.firstname == firstname]

        if len(matched_users) > 1:
            return f"There are {len(matched_users)} users with the first name '{firstname}'. Please specify by username."

        elif len(matched_users) == 1:
            del self.users[matched_users[0].username]
            return f"User with the first name '{firstname}' has been removed."

        else:
            return f"No users found with the first name '{firstname}'."

    def count_users(self):
        """Returns the total number of users in the collection."""
        return len(self.users)

    def get_user_by_username(self, username):
        """
        Returns the details of a user by their username.

        Parameters:
        - username (str): The unique username of the user.

        Returns:
        - User: The User instance if found, otherwise None.
        """
        return self.users.get(username, None)
