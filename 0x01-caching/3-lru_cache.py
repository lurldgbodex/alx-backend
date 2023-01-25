#!/usr/bin/env python3
'''caching module'''

from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    '''class LRUCache inherits from BaseCaching'''
    def __init__(self):
        '''class constructor inherits super'''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        '''assign dict cache_data item value of key'''
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lru = self.cache_data.popitem()
                print('DISCARD: {}'.format(lru[0]))

        if key is not None and item is not None:
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)

    def get(self, key):
        '''return cache_data linked to key'''
        return self.cache_data.get(key, None)
