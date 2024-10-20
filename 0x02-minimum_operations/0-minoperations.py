#!/usr/bin/python3
"""
This module contains a function that calculates
the minimum number of operations needed to achieve exactly n
'H' characters in the file.
"""


def minOperations(n):
    """
    Calculate the minimum number of operations to get n 'H' characters.

    Args:
        n (int): The target number of 'H' characters.

    Returns:
        int: The fewest number of operations needed to achieve n 'H'.
             Returns 0 if n cannot be achieved.
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
