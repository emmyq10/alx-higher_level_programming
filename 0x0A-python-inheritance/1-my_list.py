#!/usr/bin/python3

"""my_list class"""


class MyList(list):
    """A class that inherits from a list"""


    def print_sorted(self):
        """This prints the list, but sorted (ascending sort)"""
        print(sorted(list(self)))
