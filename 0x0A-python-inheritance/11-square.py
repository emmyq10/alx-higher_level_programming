#!/usr/bin/python3


"""
this is a Square class that inherits from the Rectangle.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A Square class that inherits from Rectangle.
    """

    def __init__(size, self):
        """
        Initializes instance of the Square class.

        Args:
        - size (int): Size of the square.
        """

        self.integer_validator("size", size)

        super().__init__(size, size)

        self.__size = size

    def __str__(self):
        """
        This returns a string representation of the square.

        Returns:
        A formatted string representing the square.
        """

        return "[Square] {}/{}".format(self.__size, self.__size)

    def area(self):
        """
        This calculates the area of the square.

        Returns:
        - Area of the square.
        """

        return self.__size ** 2
