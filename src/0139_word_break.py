"""
Given a string s and a dictionary of strings wordDict,
return true if s can be segmented into a space-separated
sequence of one or more dictionary words.
"""
import unittest
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[-1] = True
        for i in range(n - 1, -1, -1):
            for word in wordDict:
                m = len(word)
                if (i + m) <= n and s[i : i + m] == word:
                    dp[i] = dp[i + m]
                if dp[i]:
                    break
        return dp[0]


class TestSolution(unittest.TestCase):
    def test_wordBreak(self):
        solution = Solution()
        s = "leetcode"
        wordDict = ["leet", "code"]
        output = solution.wordBreak(s, wordDict)
        self.assertTrue(output)


if __name__ == "__main__":
    unittest.main()
