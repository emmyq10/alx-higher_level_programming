#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        result_row = list(map(lambda x: x ** 2, i))
        new_matrix.append(result_row)
        
    print new_matrix
