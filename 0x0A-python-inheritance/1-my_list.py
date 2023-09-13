class MyList(list):

    """my_list class"""


    def print_sorted(self):
        """A class that inherits from a list"""

        sorted_list = sorted(self)
        """This prints the list, but sorted (ascending sort)"""
        print(sorted_list)
