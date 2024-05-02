#!/usr/bin/env python3

from typing import Mapping, Any, TypeVar, Union

# Define a type variable for the default value
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely gets a value from a dictionary.

    Args:
        dct (Mapping): The dictionary to retrieve the value from.
        key (Any): The key to search for.
        default (Optional[T]): The default value. Defaults to None.

    Returns:
        Union[Any, T]: The value corresponding to the key or the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
