import unittest
from hash_table import HashTable


class HashTest(unittest.TestCase):

    def test_key_is_string(self):
        h = HashTable(100)
        with self.assertRaises(TypeError) as context:
            h.set(1, 1)
        self.assertEqual(context.exception.message, u"key must be a string.")

    def test_hash(self):
        h = HashTable(30)
        actual = h.hash('puppy')
        expected = 4
        assert actual == expected

    def test_set(self):
        h = HashTable(30)
        h.set('puppy', 'cute')
        actual = h.hlist[4]
        expected = [('puppy', 'cute')]
        assert actual == expected
