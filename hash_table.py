"""Implement a hash table of a given size"""


class HashTable(object):

    def __init__(self, size):
        self.size = size

    def get(self, key):
        pass

    def set(self, key, val):
        if str(key) != key:
            raise TypeError("key must be a string.")
        pass

    def hash(self, key):
        pass
