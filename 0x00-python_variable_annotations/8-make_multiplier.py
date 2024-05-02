#!/usr/bin/env python3
"""
This module defines a function that generates a multiplier function.

The make_multiplier function takes a float multiplier as an argument
and returns a function that multiplies a float by the provided multiplier.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the provided multiplier.

    Args:
        multiplier (float): The multiplier to be used in the returned function.

    Returns:
        Callable[[float], float]: A function that takes a float as input.
    """

    def multiplier_function(x: float) -> float:
        return x * multiplier
    return multiplier_function
