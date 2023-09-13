#!/usr/bin/python3


"""
BaseGeometry update
"""


class BaseGeometry:
    """
    This BaseGeometry class defines the basic structure for geometric calc,
    this is updated to raise exception

    Methods:
    - area(): To raise an exception and should be implemented in derived class
    """

    @classmethod
    def area(self):
        """
        This calculates the area of the geometric shape.

        This method is intended to be overridden by derived classes to
        provide the specific implementation for calculating the area of
        the corresponding geometric shape.

        Raises:
        Exception: An exception is raised when called.
        """
        raise Exception("area() is not implemented")
