class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        result = []
        for i in num:
            while k and result and result[-1] > i:
                result.pop()
                k -= 1
            result.append(i)
        return ''.join(result).lstrip('0')[:-k or None] or '0'
