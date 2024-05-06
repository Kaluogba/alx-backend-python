#!/usr/bin/env python3
"""
Creates an asyncio.Task that waits for a random delay.
"""

import asyncio
from typing import Any

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio.Task that waits for a random delay.

    Args:
        max_delay (int): The maximum delay in seconds.

    Returns:
        asyncio.Task: An asyncio Task.
    """
    return asyncio.create_task(wait_random(max_delay))


if __name__ == "__main__":
    import asyncio

    async def test(max_delay: int) -> float:
        task = task_wait_random(max_delay)
        await task
        print(task.__class__)

    asyncio.run(test(5))
