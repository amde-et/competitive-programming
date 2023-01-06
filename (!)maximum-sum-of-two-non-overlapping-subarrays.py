class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        res, L_max, M_max = nums[firstLen+secondLen-1], nums[firstLen-1], nums[secondLen-1]
        for i in range(firstLen+secondLen, len(nums)):
            L_max = max(L_max, nums[i-secondLen] - nums[i-firstLen-secondLen])
            M_max = max(M_max, nums[i-firstLen] - nums[i-firstLen-secondLen])
            res = max(res,
                         L_max + nums[i] - nums[i-secondLen],
                         M_max + nums[i] - nums[i-firstLen])
        return res
