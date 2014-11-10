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

    def test_get(self):
        h = HashTable(30)
        h.set('puppy', 'cute')
        actual = h.get('puppy')
        expected = 'cute'
        assert actual == expected

    def test_get_conflict(self):
        h = HashTable(30)
        h.set('hi', 'HI')
        h.set('w', 'W')
        assert h.hash('w') == h.hash('hi')
        actual1 = h.get('hi')
        expected1 = 'HI'
        assert actual1 == expected1
        actual2 = h.get('w')
        expected2 = 'W'
        assert actual2 == expected2

    def test_many(self):
        words = [line.strip() for line in open('/usr/share/dict/words')]
        words = words[:300]
        len_words = len(words)
        h = HashTable(len_words)
        for word in words:
            h.set(word, word)
        for word in words:
            assert h.get(word) == word
