class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        nums.append(float("inf"))
        result, duplicate = 0, 0
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                duplicate += 1
                result -= nums[i]
            else:
                move = min(duplicate, nums[i]-nums[i-1]-1)
                duplicate -= move
                result += move*nums[i-1] + move*(move+1)//2
        return result
