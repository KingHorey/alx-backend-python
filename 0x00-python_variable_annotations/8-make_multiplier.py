#!/usr/bin/env python3
"""carry float, multiply by function"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ multiply by function"""

    def mul(times: float) -> float:
        """ helper function """
        return multiplier * times
    return mul
