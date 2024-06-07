#!/usr/bin/env python3
""" Iterable and Sequence types"""
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ generates length of elements in a list"""
    return [(i, len(i)) for i in lst]
