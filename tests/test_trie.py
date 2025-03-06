import unittest
from src.trie import Trie

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()
        self.words = ["apple", "banana", "app", "bat"]
        for word in self.words:
            self.trie.insert(word)

    def test_search(self):
        self.assertTrue(self.trie.search("apple"))
        self.assertFalse(self.trie.search("apples"))

    def test_starts_with(self):
        self.assertEqual(self.trie.starts_with("app"), ["app", "apple"])

if __name__ == "__main__":
    unittest.main()