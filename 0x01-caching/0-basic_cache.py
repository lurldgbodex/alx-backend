#!/usr/bin/env python3
'''caching Module'''

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''a caching class iherits from BaseCaching'''
    def put(self, key, item):
        '''assign to the cache_data dict item value of key'''
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        '''return value in self.cache_data'''
        if key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
