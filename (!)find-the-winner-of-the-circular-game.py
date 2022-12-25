class Solution(object):
    def findTheWinner(self, n, k):
        return reduce(lambda idx, n:(idx+k)%(n+1), xrange(1, n), 0)+1
