#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = list(map(lambda new: replace if new == search else new, my_list))
    return new_list
