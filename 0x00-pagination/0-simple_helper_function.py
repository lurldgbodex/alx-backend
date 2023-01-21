#!/usr/bin/env python3
'''working with pagination'''

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''returns a tuple of size containing a start index
    and end index corresponding to the range of indexes
    to return in a list for those particular pagination
    parameters'''
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
