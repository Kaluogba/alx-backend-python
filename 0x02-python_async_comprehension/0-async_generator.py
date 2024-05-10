#!/usr/bin/env python3

"""Async Generator

This module contains a coroutine called async_generator that yields
a random number between 0 and 10 asynchronously for 10 iterations.

"""

import asyncio
import random


async def async_generator() -> float:
    """Generate random numbers asynchronously.

    Yields:
        float: A random number between 0 and 10.

    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
