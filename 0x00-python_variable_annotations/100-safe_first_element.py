#!/usr/bin/env python3
""" Import Union, Sequence and Any from typing """


from typing import Union, Sequence, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ Safe first element function"""
    if lst:
        return lst[0]
    else:
        return None
