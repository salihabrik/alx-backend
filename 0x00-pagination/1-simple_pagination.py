#!/usr/bin/env python3
"""
Implement a method named get_page that takes two integer arguments page with default value 1 and page_size with default value 10.
"""


from typing import List
def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
    """
    Get a specific page of the dataset.

    Args:
        page (int): The page number.
        page_size (int): The size of the page.

    Returns:
        List[List]: The requested page of the dataset.
    """
    assert isinstance(page, int) and page > 0
    assert isinstance(page_size, int) and page_size > 0

    start_index, end_index = index_range(page, page_size)
    return self.dataset()[start_index:end_index]
