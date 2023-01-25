#!/usr/bin/env python3
'''caching module'''

from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    '''fifocache class inherits from BaseCache'''
    def __init__(self):
        '''overloading the init class'''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        '''assign a dict cache_data the item value of key'''
        if key is not None and item is not None:
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_item = self.cache_data.popitem(False)
            print('DISCARD: {}'.format(first_item[0]))

    def get(self, key):
        '''return value in cache_data'''
        if key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
