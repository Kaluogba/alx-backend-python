#!/usr/bin/env python3

"""A function to calculate the length of elements in a list."""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculate the length of each element in the input list.

    Args:
        lst (Iterable[Sequence]): Input list containing sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples.
    """
    return [(i, len(i)) for i in lst]


if __name__ == "__main__":
    element_length = __import__('9-element_length').element_length
    print(element_length.__annotations__)
