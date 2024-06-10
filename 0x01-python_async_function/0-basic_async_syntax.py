#!/usr/bin/env python3
'''Task 0's module.
'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''Waits for a random number of seconds.

    Args: max_delay (int): The maximum delay in seconds to wait. Defaults to 10.

    Returns:
        float: The actual number of seconds to wait.
    '''
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
