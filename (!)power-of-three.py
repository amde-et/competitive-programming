class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and (math.log10(n)/math.log10(3)).is_integer()
