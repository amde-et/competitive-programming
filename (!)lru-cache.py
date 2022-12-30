class LRUCache(object):

    def __init__(self, capacity):
        self.cache = collections.OrderedDict()
        self.capacity = capacity
        

    def get(self, key):
        if key not in self.cache:
            return -1
        val = self.cache[key]
        self.__update(key, val)
        return val
        

    def put(self, key, value):
        if key not in self.cache and len(self.cache) == self.capacity:
            self.cache.popitem(last=False)
        self.__update(key, value)


    def __update(self, key, val):
        if key in self.cache:
            del self.cache[key]
        self.cache[key] = val
 
