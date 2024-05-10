#!/usr/bin/env python3

"""Async Comprehensions

This module contains a coroutine called async_comprehension that collects
10 random numbers using an async comprehension over async_generator.

"""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collect 10 random numbers using async comprehension.

    Returns:
        List[float]: A list containing 10 random numbers.

    """
    return [i async for i in async_generator()]
