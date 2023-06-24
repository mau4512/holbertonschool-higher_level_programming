#!/usr/bin/python3
"""Defines a Pascal's Triangle function"""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n
    Returns:
        a list of list of integers representing the triangle
    """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        before = triangle[-1]
        base = [1]
        for i in range(len(before) - 1):
            base.append(before[i] + before[i + 1])
        base.append(1)
        triangle.append(base)
    return (triangle)
