class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        count = [0] * (n + 1)
        for x in citations:
            if x >= n:
                count[n] += 1
            else:
                count[x] += 1
        h = 0
        for i in reversed(range(0, n + 1)):
            h += count[i]
            if h >= i:
                return i
        return h
