from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely retrieves a value from a dictionary.

    Args:
        dct (Mapping): The dictionary to retrieve the value from.
        key (Any): The key to lookup in the dictionary.
        default (Union[T, None], optional): The default value to return if the key is not found. Defaults to None.

    Returns:
        Union[Any, T]: The value associated with the key if found, otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default


if __name__ == "__main__":
    safely_get_value = __import__('101-safely_get_value').safely_get_value
    annotations = safely_get_value.__annotations__
    
    print("Here's what the mappings should look like")
    for k, v in annotations.items():
        print(f"{k}: {v}")
