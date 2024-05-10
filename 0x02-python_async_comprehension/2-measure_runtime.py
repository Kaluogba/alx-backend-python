#!/usr/bin/env python3

"""Run time for four parallel comprehensions

This module contains a coroutine called measure_runtime that executes
async_comprehension four times in parallel using asyncio.gather.

"""

import asyncio
import time
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure the total runtime for four parallel comprehensions.

    Returns:
        float: The total runtime.

    """
    start_time = time.time()

    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    end_time = time.time()

    return end_time - start_time
