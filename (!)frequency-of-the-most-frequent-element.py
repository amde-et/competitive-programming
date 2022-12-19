class Solution(object):
    def maxFrequency(self, nums, k):
        left = 0
        nums.sort()
        for right in range(len(nums)):
            k += nums[right]
            if k < nums[right]*(right-left+1):
                k -= nums[left]
                left += 1
        return right-left+1
