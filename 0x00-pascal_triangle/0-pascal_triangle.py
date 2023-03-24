#!/usr/bin/python3

"""
This module contains a function that takes in a value and
builds a pascal triangle
by returning a list of lists containing the integers
"""


def pascal_triangle(n):
    """
     The function implements pascal's
     Triangle based on n
    """
    triangle = []
    if n == 0:
        return triangle
    triangle.append([1])
    i = 1
    while i < n:
        previous_row = triangle[i-1]
        new_row = []

        j = 0
        while j <= i:
            if j - 1 < 0:
                val1 = 0
            else:
                val1 = previous_row[j - 1]
            if j == i:
                val2 = 0
            else:
                val2 = previous_row[j]

            new_row.append(val1 + val2)
            j += 1
        triangle.append(new_row)
        i += 1
    return triangle
