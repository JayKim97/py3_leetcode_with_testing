# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s or len(s) == 1:
            return len(s)
        i = maximum = 0
        repeat = {}
        start = maxim = 0
        for end, c in enumerate(s):
            if c in repeat:
                if repeat[c] >= start:
                    start = repeat[c] + 1
            maxim = max(maxim, end - start + 1)
            repeat[c] = end
        return maxim
