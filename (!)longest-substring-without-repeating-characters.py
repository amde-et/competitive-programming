class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result, left = 0, 0
        lookup = {}
        for right in range(len(s)):
            if s[right] in lookup:
                left = max(left, lookup[s[right]]+1)
            lookup[s[right]] = right
            result = max(result, right-left+1)
        return result
