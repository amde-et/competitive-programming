class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        VOWELS = set("aeiou")
        result = curr = 0
        for i, c in enumerate(s):
            curr += c in VOWELS
            if i >= k:
                curr -= s[i-k] in VOWELS
            result = max(result, curr)
        return result
