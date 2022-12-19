class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        """
            n = len(nums)
            m = len(l) = len(r)
            O(n) space O(n * m) time
        """
        def check(nums: List[int]):
            snums = frozenset(nums)
            if len(snums) != len(nums):
                return len(snums) == 1
            mx, mn, = max(nums), min(nums)
            step = (mx - mn) // (len(nums) - 1)
            return all((i in snums for i in range(mn, mx, step)))
        return [check(nums[i:j + 1]) for i, j in zip(l, r)]
