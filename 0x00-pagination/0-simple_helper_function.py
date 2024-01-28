#!/usr/bin/env python3
"""
Simple Helper Function
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Calculates the start and end indexes for a given page and page_size.
    """
    if page <= 0 or page_size <= 0:
        return (0, 0)  # Invalid input, return an empty range

    start_index = (page - 1) * page_size
    end_index = start_index + page_size - 1

    return start_index, end_index

if __name__ == "__main__":
    # Example Usage
    res = index_range(1, 7)
    print(type(res))
    print(res)

    res = index_range(page=3, page_size=15)
    print(type(res))
    print(res)
