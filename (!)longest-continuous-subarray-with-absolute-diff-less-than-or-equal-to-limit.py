class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_dq, min_dq = collections.deque(), collections.deque()
        result, left = 0, 0
        for right, num in enumerate(nums):
            while max_dq and nums[max_dq[-1]] <= num:
                max_dq.pop()
            max_dq.append(right)
            while min_dq and nums[min_dq[-1]] >= num:
                min_dq.pop()
            min_dq.append(right)
            while nums[max_dq[0]]-nums[min_dq[0]] > limit:  
                if max_dq[0] == left:
                    max_dq.popleft()
                if min_dq[0] == left:
                    min_dq.popleft()
                left += 1
            result = max(result, right-left+1)
        return result
