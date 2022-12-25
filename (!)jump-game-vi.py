class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        result,dq = 0,collections.deque()
        for i, num in enumerate(nums):
            if dq and dq[0][0] == i-k-1:
                dq.popleft()
            result = num if not dq else dq[0][1]+num
            while dq and dq[-1][1] <= result:
                dq.pop()
            dq.append((i, result))
        return result
