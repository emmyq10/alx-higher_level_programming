#!/usr/bin/python3
"""Pascal's Triangle function is define."""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.

    Returns a list of lists of int representing the Pascal's triangle.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        row = [1]
        for i in range(len(tri) - 1):
            row.append(tri[i] + tri[i + 1])
        row.append(1)
        triangles.append(row)
    return triangles
