#!/usr/bin/python3
""" 
User class
"""

class User():
    """ Documentation """

    def __init__(self):
        """ Initialize User instance """
        self.__email = None

    @property
    def email(self):
        """ Getter for email property """
        return self.__email

    @email.setter
    def email(self, value):
        """ Setter for email property """
        if not isinstance(value, str):
            raise TypeError("Email must be a string")
        self.__email = value

if __name__ == "__main__":
    # Test the User class
    u = User()
    u.email = "john@snow.com"
    print(u.email)
