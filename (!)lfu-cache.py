class LFUCache(object):

    def __init__(self, capacity):
        self.__capa = capacity
        self.__size = 0
        self.__min_freq = float("inf")
        self.__freq_to_nodes = collections.defaultdict(collections.OrderedDict)
        self.__key_to_freq = {}
        

    def get(self, key):
        if key not in self.__key_to_freq:
            return -1
        value = self.__freq_to_nodes[self.__key_to_freq[key]][key]
        self.__update(key, value)
        return value
        

    def put(self, key, value):
        if self.__capa <= 0:
            return

        if key not in self.__key_to_freq and self.__size == self.__capa:
            del self.__key_to_freq[self.__freq_to_nodes[self.__min_freq].popitem(last=False)[0]]
            if not self.__freq_to_nodes[self.__min_freq]:
                del self.__freq_to_nodes[self.__min_freq]
            self.__size -= 1
        self.__update(key, value)

    def __update(self, key, value):
        freq = 0
        if key in self.__key_to_freq:
            freq = self.__key_to_freq[key]
            del self.__freq_to_nodes[freq][key]
            if not self.__freq_to_nodes[freq]:
                del self.__freq_to_nodes[freq]
                if self.__min_freq == freq:
                    self.__min_freq += 1
            self.__size -= 1

        freq += 1
        self.__min_freq = min(self.__min_freq, freq)
        self.__key_to_freq[key] = freq
        self.__freq_to_nodes[freq][key] = value
        self.__size += 1
