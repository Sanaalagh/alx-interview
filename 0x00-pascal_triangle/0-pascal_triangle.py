#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row.

    Parameters:
    n (int): The number of rows of Pascal's Triangle to generate.

    Returns:
    list of lists of int: A list of lists representing Pascal's Triangle.
    """
    if n <= 0:
        return []

    # Initialize the triangle with the first row
    triangle = [[1]]

    for i in range(1, n):
        # Start each row with 1
        row = [1]
        # Calculate the middle elements
        for j in range(1, len(triangle[i - 1])):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        # End each row with 1
        row.append(1)
        # Add the row to the triangle
        triangle.append(row)

    return triangle
