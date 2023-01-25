#!/usr/bin/env python3
'''caching module'''

from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    '''MRUCache class inherits from BaseCaching'''
    def __init__(self):
        '''class constructor'''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        '''assigns to dict cache_data item value of key'''
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                mru = self.cache_data.popitem(False)
                print('DISCARD: {}'.format(mru[0]))

        if key is not None and item is not None:
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)

    def get(self, key):
        '''return value of cache_data linked to key'''
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
