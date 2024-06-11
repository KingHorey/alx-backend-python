#!/usr/bin/env python3

import asyncio
import random

""" import the async module """


async def wait_random(max_delay=10):
    """ async coroutine """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay