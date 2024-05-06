#!/usr/bin/env python3
"""
Async routine that spawns wait_random n times with the specified max_delay.
"""

import asyncio
from typing import List
from random import uniform
from typing import Callable

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay in seconds.

    Returns:
        List[float]: A list of all the delays in ascending order.
    """
    delays = [wait_random(max_delay) for _ in range(n)]
    return sorted(await asyncio.gather(*delays))


if __name__ == "__main__":
    import asyncio
    print(asyncio.run(wait_n(5, 5)))
    print(asyncio.run(wait_n(10, 7)))
    print(asyncio.run(wait_n(10, 0)))
