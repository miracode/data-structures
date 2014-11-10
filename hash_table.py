"""Implement a hash table of a given size"""


class HashTable(object):

    def __init__(self, size):
        if int(size) != size:
            raise TypeError(u"size must be an integer")
        self.size = size
        self.hlist = [[]] * size

    def get(self, key):
        pass

    def set(self, key, val):
        if str(key) != key:
            raise TypeError(u"key must be a string.")
        pass

    def hash(self, key):
        h_index = 0
        for char in key:
            h_index = (h_index + ord(char)) % self.size
        return h_index
