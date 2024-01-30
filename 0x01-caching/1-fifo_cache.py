#!/usr/bin/env python3
""" class FIFCache that inherits from BaseCaching and is a caching system
"""
from collections import deque
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO Cache Class """
    def __init__(self):
        super().__init__()
        self.fifo_queue = deque()
        self.max_items = BaseCaching.MAX_ITEMS
        self.size = 0

    def put(self, key, item):
        """  Assign to the dictionary self.
        """
        if key and item:
            self.size += 1

            if self.size > self.max_items:
                if key in self.cache_data:
                    self.cache_data[key] = item
                    return

                old = self.fifo_queue.popleft()
                self.cache_data.pop(old)
                print(f"DISCARD: {old}")

            self.cache_data[key] = item
            self.fifo_queue.append(key)

    def get(self, key):
        """ Return the value in self.cache_data linked to key """
        if key and key in self.cache_data:
            return (self.cache_data[key])

        return (None)
