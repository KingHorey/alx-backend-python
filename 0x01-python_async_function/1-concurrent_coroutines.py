#!/usr/bin/env python3

""" import ascync module """

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int):
    """ run wait_random n times """
    output = []
    for i in range(n):
        result = await wait_random(max_delay)
        output.append(result)
    output = sorted(output)
    return output
