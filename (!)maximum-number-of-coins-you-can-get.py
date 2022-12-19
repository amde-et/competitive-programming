import itertools
class Solution(object):
    def maxCoins(self, piles):
        piles.sort()
        return sum(itertools.islice(piles, len(piles)//3, len(piles), 2))
