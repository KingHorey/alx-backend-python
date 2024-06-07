#!/usr/bin/env python3
""" import List and Tuple from typing """


from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """zoom array function"""
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in
