#!/usr/bin/env python3
"""
This module contains a helper function 
for a given page number and page size.
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Calculate the start and end indices for a given page number and page size.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
