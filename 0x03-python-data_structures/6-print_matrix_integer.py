#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col, value in enumerate(row):
            if col == len(row) - 1:
                print("{:d}".format(value))
            else:
                print("{:d}".format(value), end=" ")
