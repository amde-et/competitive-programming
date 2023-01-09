class Solution(object):
    def numberOfSubarrays(self, nums, k):
        result = 0
        dq = collections.deque([-1])
        for i in xrange(len(nums)):
            if nums[i]%2:
                dq.append(i)
            if len(dq) > k+1:
                dq.popleft()
            if len(dq) == k+1:
                result += dq[1]-dq[0]
        return result
