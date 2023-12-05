class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l, zeros = 0, 0
        for r, n in enumerate(nums):
            zeros += n == 0
            if zeros > 0:
                zeros -= nums[l] == 0
                l += 1
        
        return r - l + 1