#!/usr/bin/python3


"""
This is MyInt class that inherits from int.
"""


class MyInt(int):
    """
    MyInt class.
    """

    def __eq__(self, other):
        """
        This overrides the equality operator.
        """

        return super().__ne__(other)

    def __ne__(self, other):
        """
        This overrides the inequality operator.
        """

        return super().__eq__(other)
