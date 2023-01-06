class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res, i = 0, 0
        for j in range(len(nums)):
            k -= int(nums[j] == 0)
            while k < 0:
                k += int(nums[i] == 0)
                i += 1
            res = max(res, j-i+1)
        return res
