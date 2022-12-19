class Solution:
    def myPow(self, x: float, n: int) -> float:
        tmp = 1
        abs_n = abs(n)
        while abs_n:
            if abs_n & 1:
                tmp *= x
            abs_n >>= 1
            x *= x
        return 1 / tmp if n < 0 else tmp
