#!/usr/bin/env python3

"""
Module to calculate the floor of a float.
"""

import math


def floor(n: float) -> int:
    """
    Return the floor of a given float.

    Args:
        n (float): The float number.

    Returns:
        int: The floor of the float number.
    """

    return math.floor(n)


if __name__ == "__main__":
    ans = floor(3.14)
    print(ans == math.floor(3.14))
    print(floor.__annotations__)
    print("floor(3.14) returns {}, which is a {}".format(ans, type(ans)))
