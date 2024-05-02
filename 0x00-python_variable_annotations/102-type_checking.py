#!/usr/bin/env python3

from typing import Tuple, List


def zoom_array(lst: Tuple[int], factor: int = 2) -> List[int]:
    """
    Zooms in on the elements of a tuple by repeating them according to factor.

    Args:
        lst (Tuple[int]): The input tuple of integers.
        factor (int, optional):factor by which each element should be repeated

    Returns:
        List[int]: A list containing the zoomed-in elements.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)  # Changed 3.0 to 3
