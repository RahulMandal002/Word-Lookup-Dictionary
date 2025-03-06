import unittest
from src.trie import Trie
from src.spell_correct import SpellCorrector

class TestSpellCorrector(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()
        self.words = ["apple", "banana", "app", "bat"]
        for word in self.words:
            self.trie.insert(word)
        self.corrector = SpellCorrector(self.trie)

    def test_correct_spelling(self):
        suggestions = self.corrector.correct_spelling("aple")
        self.assertCountEqual(suggestions, ["apple", "app"])  # Check for same elements, ignoring order

if __name__ == "__main__":
    unittest.main()