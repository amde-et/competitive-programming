class Solution(object):
    def minPairSum(self, nums):
        nums.sort()
        return max(nums[i]+nums[-1-i] for i in range(len(nums)//2))
