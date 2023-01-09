class Solution(object):
    def minSubArrayLen(self, target, nums):
        start = 0
        sum = 0
        min_size = float("inf")
        for i in xrange(len(nums)):
            sum += nums[i]
            while sum >= target:
                min_size = min(min_size, i - start + 1)
                sum -= nums[start]
                start += 1

        return min_size if min_size != float("inf") else 0
