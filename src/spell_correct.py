class SpellCorrector:
    def __init__(self, trie):
        self.trie = trie

    def _edit_distance(self, word1, word2):
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                elif word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
        return dp[m][n]

    def correct_spelling(self, word, max_distance=2):
        suggestions = []
        all_words = self.trie.starts_with("")
        for valid_word in all_words:
            if self._edit_distance(word, valid_word) <= max_distance:
                suggestions.append(valid_word)
        return suggestions