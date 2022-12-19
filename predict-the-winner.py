class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        if len(nums) % 2 == 0 or len(nums) == 1:
            return True
        tmp = [0] * len(nums)
        for i in reversed(range(len(nums))):
            tmp[i] = nums[i]
            for j in range(i+1, len(nums)):
                tmp[j] = max(nums[i] - tmp[j], nums[j] - tmp[j - 1])
        return tmp[-1] >= 0
