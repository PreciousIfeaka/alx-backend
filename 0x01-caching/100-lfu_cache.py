#!/usr/bin/env python3
"""This class inherits from the base class BaseCaching and defines
   the following methods:
   put: adds item to the cache
   get: return the value in the cache
"""


BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """A caching system that inherits from base cache"""
    key_list = []

    def lfu(self, lists):
        if lists == []:
            pass
        else:
            from collections import Counter
            key_count = Counter(lists)
            # print(key_count)
            min_key = min(key_count, key=lambda k: key_count[k])
            return min_key

    def put(self, key, item):
        """assign the key and value to the cache_data
        """
        if key and item:
            self.cache_data[key] = item
            lst_cpy = self.key_list.copy()
            self.key_list.append(key)
            lfu_key = self.lfu(lst_cpy)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                print(f"DISCARD: {lfu_key}")
                del self.cache_data[lfu_key]
                self.key_list.remove(lfu_key)
            return self.cache_data

    def get(self, key):
        """returns the cache_data item with the specified key
        """
        if key in self.cache_data:
            self.key_list.append(key)
            return self.cache_data[key]
        else:
            return None
