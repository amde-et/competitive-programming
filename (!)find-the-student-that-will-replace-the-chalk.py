class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        k %= sum(chalk)
        for i, x in enumerate(chalk):
            if k < x:
                return i
            k -= x
        return -1
