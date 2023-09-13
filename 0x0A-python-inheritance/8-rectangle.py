#!/usr/bin/python3


"""
This class is a rectangle class that inherits from BaseGeometry.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        It initialize instance of the Rectangle class.

        Args:
        - width (int): width of the rectangle.
        - height (int): height of the rectangle.
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
