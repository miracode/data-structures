"""Implement a hash table of a given size"""


class HashTable(object):

    def __init__(self, size):
        if int(size) != size:
            raise TypeError(u"size must be an integer")
        self.size = size
        self.hlist = []
        for i in range(size):
            self.hlist.append([])

    def get(self, key):
        index = self.hash(key)
        index_list = self.hlist[index]
        for pair in index_list:
            if pair[0] == key:
                return pair[1]

    def set(self, key, val):
        if str(key) != key:
            raise TypeError(u"key must be a string.")

        index = self.hash(key)
        self.hlist[index].append((key, val))

    def hash(self, key):
        h_index = 0
        for char in key:
            h_index = (h_index + ord(char)) % self.size
        return h_index
