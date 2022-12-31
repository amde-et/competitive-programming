class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        pos = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[i], nums[pos] = nums[pos], nums[i]
                pos += 1
