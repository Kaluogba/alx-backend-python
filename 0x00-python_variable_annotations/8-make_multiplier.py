#!/usr/bin/env python3

"""
This module provides a function to create a multiplier function.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a function that multiplies a float by the specified multiplier.

    Args:
        multiplier (float): The multiplier to use.

    Returns:
        Callable[[float], float]
"""


def multiplier_function(x: float) -> float:
    """
        Multiply a float by the specified multiplier.

        Args:
            x (float): The float to be multiplied.

        Returns:
            float: The result of multiplying the input float by the multiplier.
        """
        return x * multiplier
    return multiplier_function


if __name__ == "__main__":
    print(make_multiplier.__annotations__)
    fun = make_multiplier(2.22)
    print("{}".format(fun(2.22)))
