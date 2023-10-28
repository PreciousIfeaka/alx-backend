#!/usr/bin/env python3
"""This class inherits from the base class BaseCaching and defines
   the following methods:
   put: adds item to the cache
   get: return the value in the cache
"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """A caching system that inherits from base cache"""

    def put(self, key, item):
        """assign the key and value to the cache_data
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """returns the cache_data item with the specified key
        """
        if key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
