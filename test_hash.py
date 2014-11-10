import unittest
from hash_table import HashTable

class HashTest(unittest.TestCase):

    def test_key_is_string(self):
        h = HashTable(100)
        with self.assertRaises(TypeError) as context:
            h.set(1, 1)
        self.assertEqual(context.exception.message, u"key must be a string.")
