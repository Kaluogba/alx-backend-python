#!/usr/bin/env python3

"""
This module contains a function to safely retrieve the first element of a list.
"""

from typing import Sequence, Any, Union, Optional


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Safely retrieves the first element of a list.

    Args:
        lst (Sequence[Any]): Input list.

    Returns:
        Union[Any, None]: The first element of the list if it exists, otherwise
                          None.
    """
    if lst:
        return lst[0]
    else:
        return None
