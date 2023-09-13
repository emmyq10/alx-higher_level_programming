class MyList(list):

    """my_list class"""

    def print_sorted(self):
        """A class that inherits from a list"""

        sorted_list = sorted(self)
        print(sorted_list)
