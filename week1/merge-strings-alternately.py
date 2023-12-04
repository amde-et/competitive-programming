
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        remainder = ""

        if len(word1) < len(word2):
            remainder = word2[len(word1):]
        elif len(word2) < len(word1):
            remainder = word1[len(word2):]
        
        for i in range(min(len(word1),len(word2))):
            ans += word1[i]
            ans += word2[i]
        ans += remainder

        return ans




        