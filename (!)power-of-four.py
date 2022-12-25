class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        while n and not (n & 0b11):
            n >>= 2
        return (n == 1)
